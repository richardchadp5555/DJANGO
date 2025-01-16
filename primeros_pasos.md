# Primeros Pasos en Django

**Autor:** Richard Chadwick Plaza  
**Fecha:** 16 de enero de 2025  

Este documento explica los pasos realizados para configurar un proyecto Django desde cero y establecer una página de inicio personalizada (`index.html`). Aquí detallo cada paso de forma estructurada para que sea fácil de entender y replicar.

---

## 1. Crear el Proyecto

Primero, creamos un nuevo proyecto Django llamado `mi_proyecto`:

```bash
django-admin startproject mi_proyecto
```

Esto genera la siguiente estructura:

```
mi_proyecto/
├── manage.py
├── mi_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

---

## 2. Crear una Aplicación

Creamos una aplicación dentro del proyecto para manejar funcionalidades específicas:

```bash
python manage.py startapp mi_aplicacion
```

Esto añade una nueva carpeta `mi_aplicacion` con los siguientes archivos:

```
mi_aplicacion/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
```

Luego, registramos la aplicación en `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'mi_aplicacion',
]
```

---

## 3. Crear una Carpeta de Plantillas

Creamos una carpeta llamada `templates` en `mi_proyecto/mi_proyecto` para almacenar nuestras plantillas HTML globales:

```
mi_proyecto/
├── mi_proyecto/
│   ├── templates/
│   │   └── index.html
```

Dentro de `templates`, añadimos un archivo `index.html` con el siguiente contenido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página Principal</title>
</head>
<body>
    <h1>¡Bienvenido a la página principal!</h1>
</body>
</html>
```

---

## 4. Configurar la Carpeta de Plantillas

En `settings.py`, configuramos la ubicación de las plantillas. Editamos la sección `TEMPLATES`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'mi_proyecto/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 5. Crear una Vista

En `mi_proyecto/mi_proyecto`, creamos un archivo `views.py` y definimos una función `index` para cargar el archivo `index.html`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

---

## 6. Configurar las Rutas

Editamos el archivo `urls.py` en `mi_proyecto/mi_proyecto` para conectar la URL raíz (`/`) con la vista `index`:

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
```

---

## 7. Probar la Configuración

1. Iniciamos el servidor:
   ```bash
   python manage.py runserver
   ```
2. Abrimos el navegador y visitamos [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Deberíamos ver el contenido del archivo `index.html`.

---

## Resultado Final

Cuando se inicia el servidor, se carga automáticamente la página `index.html` como página principal del proyecto.

Este es el contenido que se muestra en el navegador:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página Principal</title>
</head>
<body>
    <h1>¡Bienvenido a la página principal!</h1>
</body>
</html>
