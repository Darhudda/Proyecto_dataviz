# Imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY requirements.txt .
COPY app_project.py .
COPY cargar_datos.py .


# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Dash
EXPOSE 8050

# Comando para correr la app
CMD ["python", "app_project.py"]
