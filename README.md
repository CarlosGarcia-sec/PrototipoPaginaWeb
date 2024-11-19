# Escape Rooms para Ayuntamientos

Este proyecto es un prototipo de una página web para un trabajo de la universidad. Es mi primera página web y está diseñada para mostrar cómo se pueden crear experiencias de escape room en pueblos para atraer turistas y ofrecer actividades emocionantes para los ciudadanos.

## Descripción

La página web está desarrollada utilizando Flask, un microframework de Python, y está diseñada para ser simple y fácil de usar. Incluye varias secciones como Inicio, Sobre Nosotros, Reseñas y Contacto.

## Características

- **Inicio**: Página principal con una introducción y enlaces a las demás secciones.
- **Sobre Nosotros**: Información sobre el proyecto y su misión.
- **Reseñas**: Sección donde los usuarios pueden ver y añadir reseñas.
- **Contacto**: Formulario de contacto para que los usuarios puedan enviar mensajes.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto localmente:

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/escape-rooms-ayuntamientos.git
    cd escape-rooms-ayuntamientos
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Ejecuta la aplicación:
    ```sh
    flask run
    ```

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:5000/`.
2. Navega por las diferentes secciones del sitio web:
    - **Inicio**: Información general sobre el proyecto.
    - **Sobre Nosotros**: Detalles sobre la misión y visión del proyecto.
    - **Reseñas**: Opiniones de los usuarios sobre las experiencias de escape room.
    - **Contacto**: Formulario para que los interesados puedan ponerse en contacto.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `templates/`: Directorio que contiene las plantillas HTML.
- `static/`: Directorio que contiene archivos estáticos como CSS e imágenes.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `Procfile`: Archivo para el despliegue en Heroku.
- `runtime.txt`: Archivo que especifica la versión de Python.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo:

- **Correo electrónico**: 846499@unizar.es
