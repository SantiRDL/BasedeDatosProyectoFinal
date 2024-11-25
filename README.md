Linka informe: https://docs.google.com/document/d/1K6nwYGvybKRjx53ykI6GSgC5jRwDzvNAO3IJwZWEXA8/edit?usp=sharing

Requisitos para levantar proyecto:
-MySQL workbench o programa que permita hacer consultas con MySQL
-Python
-npm (node.js)
-IDE: VsCode, DataGrip u otra que soporte y permita trabajar con MySQL, Python y React

A: instalar dependencias
    1:pararse en el directorio "backend" en la terminal y ejecutar el comando "pip install". 
    2:repetir para "frontend" pero con "npm install"

B: levantar la base de datos
    1: Usar MySQL workbench o similar para crear la base de datos.
    2: Conectarse a la BD usando un plugin (sqltools en vscode) o herramienta nativa de la IDE elegida con los parametros de config.py. probar la conexión.
    3: Si se conectó, correr el script en create.sql para crear las tablas.

C: levantar los endpoints del backend
    1: Correr el script app.py para levantar los endpoints. (python app.py)

D: levantar el frontend
    1: pararse en "frontend" y correr npm start para que se levante la pagina.
