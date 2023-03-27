# BARONI Eneas - Curso CODERHOUSE Python

Pre-entrega del curso de Python en CoderHouse

## Instalación

1. Forkeá y cloná el repositorio.

2. Parado en la raíz del proyecto ejecutar 

   ```
   pip install virtualenv
   ```
    para instalar virtualenv

3. Luego Ejecutar 

   ```
   virtualenv venv
   ```

    para crear un entorno virtual

4. Activar el interprete  

5. Ejecutar

    ```
    pip install django
    ```
    
    para instalar django

6. Ejecutar

    ```
    pip install pillow
    ```
    
    para instalar pillow
    
7. Ejecutar

    ```
    pip install "django-phonenumber-field[phonenumbers]"
    ```
    
    para instalar django-phonenumber-field, para poder validar los camppos de formulario con datos de telefonos.


8. moverse a la carpeta del proyecto ejecutando

    ```
    cd baroni
    ```

9. Ejecutar

    ```
    python manage.py runserver
    ```

    para levantar el servidor

10. Abrir el navegador en la dirección http://localhost:8000/     


## Uso

El proyecto es un sitio web para un estudio de arquitectura, y cuenta con tres modelos. Obras, Clientes y Equipo

Rutas: 
 - / Home de la pagina. En la barra navegadora hay un buscador para buscar obras por su nombre.
 - /about Seccion de About de la pagina, desde aquí se puede acceder a la seccion de Equipo, donde están los miembros del estudio.
 - /obras/list-obras/ para visualizar las obras realizadas, desde aquí se puede acceder al formulario de carga.
 - /obras/create-obra/ para crear una obra.
 - /obras/obra-detail/:id para ver el detalle de una obra.
 - /clientes/list-clientes/ para visualizar los clientes, desde aquí se puede acceder al formulario de carga.
 - /clientes/create-cliente/ para crear un cliente.
 - /equipo/list-equipo/ para visualizar el equipo que integra el estudio, desde aquí se puede acceder al formulario de carga.
 - /equipo/member-detail/:id para ver el detalle de un miembro del equipo.
 - /equipo/create-member/ para agregar un miembro al equipo.
 - /admin/ para acceder al panel de administrador.


Para acceder al panel de administrador usar el Usuario admin y el Pass admin123
