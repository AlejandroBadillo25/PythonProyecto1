# PythonProyecto1 

Mi primer proyecto de desarrollo web con Python y Django. Este proyecto incluye diferentes aspectos del framework como URLs, templates, modelos de Django, base de datos, panel de administración, formularios y herencia de clases.

## Descripción

Este es un proyecto educativo que implementa un sistema de blog básico con las siguientes funcionalidades:
- Creación y listado de posts
- Sistema de autenticación de usuarios
- Estados de publicación (Borrador/Publicado)
- Búsqueda de posts por título
- Panel de administración de Django

## Características

- **Gestión de Posts**: Crear y listar publicaciones
- **Sistema de Usuarios**: Autenticación integrada con Django
- **Búsqueda**: Filtrado de posts por título
- **Estados**: Los posts pueden estar en estado borrador o publicado
- **Templates**: Sistema de herencia de plantillas con base.html
- **Base de datos**: SQLite para desarrollo

## Estructura del Proyecto

```
PythonProyecto1/
│
├── AppCoder/          # Aplicación principal del blog
│   ├── models.py      # Modelo Post con estados y autor
│   ├── views.py       # Vistas para listar y crear posts
│   ├── forms.py       # Formularios para Post
│   ├── urls.py        # URLs de la app
│   └── templates/     # Plantillas HTML
│
├── Main/              # Aplicación base
│   ├── views.py       # Vista principal
│   └── templates/     # Plantillas base (index, base.html)
│
├── MiProyecto/        # Configuración del proyecto
│   ├── settings.py    # Configuración de Django
│   ├── urls.py        # URLs principales
│   └── wsgi.py        # Configuración WSGI
│
├── db.sqlite3         # Base de datos SQLite
├── manage.py          # Script de gestión de Django
└── README.md          # Este archivo
```

## Tecnologías Utilizadas

- **Python 3.x**
- **Django 5.2.9**
- **SQLite** (base de datos)
- **HTML/CSS** (templates)

## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/AlejandroBadillo25/PythonProyecto1.git
cd PythonProyecto1
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install django
```

4. Realizar las migraciones:
```bash
python manage.py migrate
```

5. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

7. Acceder a la aplicación en: `http://127.0.0.1:8000/`

## Uso

### URLs Disponibles

- `/` - Página principal
- `/AppCoder/post/list` - Lista de posts con búsqueda
- `/AppCoder/post/create` - Crear nuevo post (requiere autenticación)
- `/admin/` - Panel de administración de Django

### Crear un Post

1. Accede a `/AppCoder/post/create`
2. Debes estar autenticado (logged in)
3. Completa el formulario con título y contenido
4. Selecciona el estado (Borrador o Publicado)
5. Guarda el post

### Buscar Posts

1. Accede a `/AppCoder/post/list`
2. Usa el campo de búsqueda para filtrar por título

## Autor

Alejandro Badillo

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.