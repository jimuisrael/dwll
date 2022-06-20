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

Esta librería le permitirá evitar reescribir los elementos comunes en el desarrollo de sus aplicaciones, proporcionando un camino definido a seguir y con menor cantidad de código.

## Tecnología

DWLL esta dirigido al desarrollo de aplicaciones Web con Django 4.0 y hace uso de las siguientes librerías:

- [Allauth] - Librería Django que permite el manejo de todo lo relacionado con la autenticación de usuarios.


## Instalación

DWLL requiere [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/) v4.0+ para funcionar.

Instale un entorno virtual para instalar Django y DWLL.

```sh
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv -p python3 venv
source venv/bin/activate
```

Instale Django

```sh
pip install django
```
Instale DWLL

```sh
pip install dwll
```

Cree un proyecto Django, en este caso de ejemplo llamaremos a este proyecto como "myproject"

```
django-admin startproject myproject
cd myproject
```

Ejecute el generador de su primera aplicación
```
./manage.py dwll-gen
```

Siga los pasos, puede elegir generar una aplicación con un modelo ejemplo o solamente la estructura base de una aplicación de inicio.

Ahora registre la nueva aplicación agregando el siguiente código al final del archivo settings (myproject/settings.py):
```
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS.extend([
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dwll',
    'myproject'
])

import os
TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'myproject', 'templates'))
```

Ahora agreguemos las siguientes lineas al archivo myproject/urls.py:
```
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('koko.urls')),
    path('accounts/', include('allauth.urls')),
    path('dwll/', include('dwll.urls'))
]
```
Una vez realizados estas configuraciones del proyecto, realizaremos la migracion a la base de datos:
```
./manage.py makemigrations myproject
./manage.py migrate
```

Crearemos un super usuario de administracion para probar con el siguiente correo:
```
./manage.py createsuperuser
```

Y finalmente ejecutaremos el proyecto
```
./manage.py runserver
```


## Licencia

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dwll]: <https://github.com/jimuisrael/dwll>
   [df1]: <http://joaquin.medina.name/web2008/documentos/informatica/documentacion/logica/OOP/Principios/2012_07_30_OopNoTeRepitas.html>
   