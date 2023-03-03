# BARONI Eneas - Curso CODERHOUSE Python

Pre-entrega del curso de Python en CoderHouse

## Instalación

1. Forkeá y cloná el repositorio

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


7. moverse a la carpeta del proyecto ejecutando

    ```
    cd baroni
    ```

8. Ejecutar

    ```
    python manage.py runserver
    ```

    para levantar el servidor

9. Abrir el navegador en la dirección http://localhost:8000/
    
 


## Uso

El proyecto es un sitio web para un estudio de arqiutectura, y cuenta con tres modelos. Obras, Clientes y Equipo

Rutas: 
 - /obras/list-obras/ para visualizar las obras realizadas
 - /obras/create-obra/ para crear una obra
 - /obras/obra-detail/:id para ver el detalle de una obra
 - /clientes/list-clientes/ para visualizar los clientes
 - /clientes/create-cliente/ para crear un cliente
 - /equipo/list-equipo/ para visualizar el equipo que integra el estudio
 - /equipo/member-detail/:id para ver el detalle de un miembro del equipo
 - /equipo/create-member/ para agregar un miembro al equipo
 - /admin/ para acceder al panel de administrador
 

En el buscador del Navbar se pueden buscar obras por nombre

Para acceder al panel de administrador usar el Usuario admin y el Pass admin123