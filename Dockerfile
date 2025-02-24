FROM python:3.11-slim

# Variables de entorno para Django
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear directorio de la aplicación
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

# Exponer el puerto (8000 por defecto para Django)
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]