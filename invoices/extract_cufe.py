import os
import re
import sqlite3
from typing import Tuple
from PyPDF2 import PdfReader

DB_NAME = "adres.db"
PDF_FOLDER = "facturas"
CUFE_REGEX = "(\\b([0-9a-fA-F]\\n*){95,100}\\b)"

def create_database(db_name: str = DB_NAME) -> None:
    """Crea la base de datos SQLite y la tabla de facturas si no existen."""
    with sqlite3.connect(db_name) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_archivo TEXT NOT NULL,
                numero_paginas INTEGER,
                cufe TEXT,
                peso_archivo REAL
            )
        ''')


def extract_cufe(pdf_path: str) -> Tuple[str, int, str, float]:
    try:
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        content = "".join(page.extract_text() or "" for page in reader.pages)

        match = re.search(CUFE_REGEX, content)
        cufe = match.group(0).replace("\n", "") if match else "No encontrado"

        file_size = round(os.path.getsize(pdf_path), 2)
        filename = os.path.basename(pdf_path)

        return filename, num_pages, cufe, file_size

    except Exception as error:
        print(f"Error en {pdf_path}: {error}")
        return os.path.basename(pdf_path), 0, "Error", 0.0

def insert_invoice(data: Tuple[str, int, str, float], db_name: str = DB_NAME) -> None:
    with sqlite3.connect(db_name) as conn:
        conn.execute('''
            INSERT INTO facturas (nombre_archivo, numero_paginas, cufe, peso_archivo)
            VALUES (?, ?, ?, ?)
        ''', data)


def process_pdfs(folder: str = PDF_FOLDER) -> None:
    if not os.path.isdir(folder):
        print(f"Carpeta '{folder}' no encontrada.")
        return

    pdf_files = [file for file in os.listdir(folder) if file.lower().endswith(".pdf")]

    if not pdf_files:
        print("No se encontraron archivos PDF.")
        return

    for pdf_file in pdf_files:
        data = extract_cufe(os.path.join(folder, pdf_file))
        insert_invoice(data)
        print(f"{data[0]} | Páginas: {data[1]} | Peso: {data[3]} KB | CUFE: {data[2][:10]}...")

def main() -> None:
    create_database()
    process_pdfs()

if __name__ == "__main__":
    main()
