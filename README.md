# DWLL
## _Django Web Launch Library_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Django Web Launch Library es una librería de elementos utilitarios que le permitirán generar aplicaciones Web (Backend-Frontend) con Django de forma rápida y sencilla, evitando la construcción de elementos habituales en sistemas Web y de esta forma evitar repetirlos para acelerar el desarrollo de su aplicación. DWLL contiene elementos que cubre los siguientes módulos

- Vistas
- Formularios
- Modelos
- Mensajes y Traducciones
- Configuración
- URLs
- Login

## Características

- Modelos y Mixins base para auditar modelos, filtros de activos y permitir soft-delete
- Vistas virtuales que permiten crear vistas de formato CRUD con muy pocas lineas de codigo
- Sistema de mensajes de texto a ser usados en todo el sitio Web y en el backend, con su respectiva administración de textos por lenguaje para la gestión de su traducción.
- Sistema de configuraciones para agregar banderas y propiedades administrables a su aplicación Web.
- Autogenerador de una plantilla de aplicación Web principal para arrancar el desarrollo de forma acelerada.

DWLL permite que los desarrolladores tomen un camino claro y directo en el desarrollo de sus aplicaciones, siguiendo el principio DRY, Don't Repeat Yourself:
Como [Joaquin Medina] escribe en [su Blog][df1]

> DRY, es una filosofía de definición de procesos que 
> promueve la reducción de la duplicación especialmente 
> en programación. Según este principio toda pieza de 
> información nunca debería ser duplicada debido a que 
> la duplicación incrementa la dificultad en los cambios 
> y evolución posterior, puede perjudicar la claridad 
> y crear un espacio para posibles inconsistencias

Esta librería le permitirá evitar reescribir los elementos comunes en el desarrollo de sus aplicaciones Web con Django, proporcionando un camino definido a seguir y con la menor cantidad de código posible.

## Tecnología

DWLL esta dirigido al desarrollo de aplicaciones Web con Django 4.0 y hace uso de las siguientes librerías:

- [Allauth] - Librería Django que permite el manejo de todo lo relacionado con la autenticación de usuarios.


## Instalación

DWLL requiere [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/) v4.0+ para funcionar.

1. Instale un entorno virtual para instalar Django y DWLL.

```sh
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv -p python3 venv
source venv/bin/activate
```

2. Instale Django y DWLL

```sh
pip install django
pip install dwll
```

3. Cree un proyecto Django, en este ejemplo llamaremos a este proyecto: "myproject"

```
django-admin startproject myproject
cd myproject
```

4. Incluir las siguientes aplicaciones en INSTALLED_APPS de su archivo myproject/myproject/settings.py:

```
'allauth',
'allauth.account',
'allauth.socialaccount',
'dwll',
```

5. Ejecute el generador de su primera aplicación...

```
./manage.py dwll-gen
```

...y siga las instrucciones indicadas en la consola. Puede elegir generar la plantilla de una aplicación con un modelo de ejemplo, o solamente la estructura base de una aplicación para iniciar. En este ejemplo llamaremos a la aplicacion "myapp" y al modelo "mymodel".

6. Una vez terminada la generación de la nueva app, copie el siguiente segmento de código al final de su archivo general de URLs: myproject/myproject/urls.py. 

```
from django.urls import include
urlpatterns.extend([
    path('', include('myapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('dwll/', include('dwll.urls'))
])
```

Y lo siguiente en su archivo de settings:

```
import os
INSTALLED_APPS.append('myapp')
TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'myapp', 'templates'))
LOGIN_REDIRECT_URL = '/'
```

**Nota:** Luego puede unificar el código copiado a discresión, el formato descrito acá es solo para efectos del ejemplo.

7. Una vez realizados las configuraciones del proyecto, realizaremos la migracion a la base de datos:

```
./manage.py makemigrations myapp
./manage.py migrate
```

Al hacerlo, deberia conseguir una salida similar a la siguiente (y adicionalmente un listado de todos los modelos migrados a su base de datos temporal):

```
Migrations for 'myapp':
  myapp/migrations/0001_initial.py
    - Create model MyModel
```

8. Ahora es necesario crear un super usuario para probar la aplicación y la administración del sistema.
```
./manage.py createsuperuser
```

Deberá seguir las instrucciones en consola. Puede ingresar el nombre, email y clave que prefiera, pero deberá recordarlos para poder usar esos datos luego.

9. Finalmente, ejecutaremos el proyecto con el siguiente comando:
```
./manage.py runserver
```

10. Podremos ingresar a la siguiente URL para ver nuestro nuevo home-page http://localhost:8000. Además en la siguiente dirección podrá revisar un ejemplo del CRUD autogenerado incluido http://localhost:8000/mymodels/ (para acceder deberá autentticarse con su usuario generado, o con cualquier usuario registrado en la consola administrativa de Django: http://localhost:8000/admin)

## Licencia

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dwll]: <https://github.com/jimuisrael/dwll>
   [df1]: <http://joaquin.medina.name/web2008/documentos/informatica/documentacion/logica/OOP/Principios/2012_07_30_OopNoTeRepitas.html>
   