FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Crear la carpeta "facturas" si no existe
RUN mkdir -p facturas

# Comando por defecto al iniciar el contenedor
CMD ["python", "extract_cufe.py"]