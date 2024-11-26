# Usar una imagen base de Python (Python 3.11 slim en este caso)
FROM python:3.11-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt para instalar las dependencias
COPY requirements.txt /app/

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY . /app/

# Exponer el puerto donde la aplicación estará corriendo
EXPOSE 5000

# Definir el comando para ejecutar tu aplicación (suponiendo que usas Flask)
CMD ["python", "run.py"]
