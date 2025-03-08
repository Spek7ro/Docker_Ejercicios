FROM python:3.13-slim

# Copiar todo el contenido de la carpeta actual al contenedor, menos 
# los archivos y carpetas que se encuentren en .dockerignore
COPY . /app 

# Cambiar el directorio de trabajo del contenedor
WORKDIR /app

# Establecer variables de entorno, para que no se escriban en el archivo de configuración de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Indicar que estoy en un contenedor Docker 
ENV AM_I_IN_A_DOCKER_CONTAINER True

# Crear un directorio para almacenar los logs
RUN mkdir -p /app/logs

# Instalar las dependencias de la aplicación
RUN pip install -r requirements.txt

# Crear un volumen para almacenar los logs del contenedor
VOLUME /app/logs

# Ejecutar el script main.py cuando se inicie el contenedor
CMD [ "python3", "./main.py" ]
