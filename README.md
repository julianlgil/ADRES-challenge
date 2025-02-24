# **PRUEBA TECNICA DESARROLLADOR FULLSTACK - ADRES**

---

## 📝 **Contenido**
1. [Validación de archivo texto con Django](#1-requisitos-técnicos)
2. [Validación de archivo texto con Django](#2-validación-de-csv-con-django)
3. [Extracción de CUFE de PDFs con Python](#3-extracción-de-cufe-de-pdfs-con-python)

---
## 1. **Requisitos técnicos**

### **Software necesario:**
- **Docker:** Versión 20.10 o superior  
- **Docker Compose:** Versión 1.29 o superior  

## 2. **Validación de archivo de texto con Django**

### **Descripción:**
Aplicación web desarrollada con **Django** que permite cargar un archivo de texto tipo csv y valida su estructura y contenido según los siguientes criterios:
- El archivo debe tener exactamente 5 columnas.
- **Columna 1:** Números enteros entre 3 y 10 caracteres.
- **Columna 2:** Correos electrónicos válidos.
- **Columna 3:** Valores permitidos: "CC" o "TI".
- **Columna 4:** Números entre 500000 y 1500000.
- **Columna 5:** Cualquier valor permitido.

### **Instrucciones de uso:**
#### Con Docker:
```bash
docker compose up --build
```
Accede a la aplicación en: [http://localhost:8000/](http://localhost:8000/)

### **Resultados esperados:**
- Si la validación es exitosa: mensaje de “Archivo validado”.
- Si hay errores: se muestra la fila y columna con el error.
---

## 3. **Extracción de CUFE de PDFs con Python**

### **Descripción:**
Script en Python que extrae el **CUFE** de archivos PDF utilizando una expresión regular. Guarda la información en una base de datos **SQLite** con los siguientes datos:
- Nombre del archivo.
- Número de páginas.
- CUFE encontrado (o "No encontrado").
- Peso del archivo (KB).

### ️ **Instrucciones de uso:**
Se deben poner los archivos pdf dentro de la carpeta facturas
#### Con Docker Compose:
```bash
cd invoices
```
```bash
docker-compose up --build
```

### **Funcionalidades:**
- **Extracción precisa:** Utiliza la expresión regular `\\b[a-fA-F0-9]{96}\\b` para identificar el CUFE.
- **Base de datos SQLite:** Guarda la información extraída de forma estructurada.

### 🧪 **Ejemplo de resultados:**
```
✅ factura1.pdf | Páginas: 2 | CUFE: f2e7a47d94... | Peso: 120.5 KB
✅ factura2.pdf | Páginas: 1 | CUFE: No encontrado | Peso: 98.3 KB
```