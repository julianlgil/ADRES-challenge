import csv
import re

class Validator:
    @staticmethod
    def validate(file):
        errors = []
        rows = file.read().decode('utf-8').splitlines()
        reader = csv.reader(rows)

        for row_num, row in enumerate(reader, start=1):
            if len(row) != 5:
                errors.append(f"Fila {row_num}: Se esperaban 5 columnas, se encontraron {len(row)}.")
                continue

            if not Validator.validate_col1(row[0]):
                errors.append(f"Fila {row_num}, Columna 1: Número entre 3 y 10 dígitos requerido.")

            if not Validator.validate_col2(row[1]):
                errors.append(f"Fila {row_num}, Columna 2: Correo electrónico inválido.")

            if not Validator.validate_col3(row[2]):
                errors.append(f"Fila {row_num}, Columna 3: Solo 'CC' o 'TI' permitidos.")

            if not Validator.validate_col4(row[3]):
                errors.append(f"Fila {row_num}, Columna 4: Valor entre 500000 y 1500000 requerido.")

        return errors

    @staticmethod
    def validate_col1(value):
        return value.isdigit() and 3 <= len(value) <= 10

    @staticmethod
    def validate_col2(value):
        email_regex = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        return email_regex.match(value) is not None

    @staticmethod
    def validate_col3(value):
        return value in ["CC", "TI"]

    @staticmethod
    def validate_col4(value):
        return value.isdigit() and 500000 <= int(value) <= 1500000