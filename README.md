# E-commerce NutriStyle

Esta aplicación ha sido desarrollada utilizando el marco de trabajo Django, junto con tecnologías web como Bootstrap, HTML, CSS y JavaScript.

## Instalación de Bibliotecas

Antes de comenzar con la configuración del E-commerce NutriStyle, es importante asegurarse de que todas las bibliotecas y dependencias necesarias estén instaladas. 
A continuación verán una guía paso a paso para configurar el entorno de desarrollo desde la terminal:


### 1. Crear un Entorno Virtual (en "myenv" poner el nombre de tu nuevo entorno virtual):

```shell
python -m venv myenv
```

### 2. Activar el Entorno Virtual:

- En Windows:

```shell
myenv\Scripts\activate
```

### 3. Instalar Django:

```shell
pip install Django
```

### 4. Instalar Pillow (para el manejo de imágenes):

```shell
pip install Pillow
```

### 4. Instalar Psycopg2 (para el manejo de la base de datos):

```shell
pip install psycopg2
```

## Ejecutar el Proyecto

### 1. Conectar con a base de datos:
* Si queres usar SQLite debes tener el siguiente codigo habilitado en el archivo settings.py:
```shell
  DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        }
    }
```
  
* Si vas a usar PostgreSQL segui los siguientes pasos:
   - Ingresa a PGAdmin4 y creeá una nueva base de datos llamada "EcommerceNS"
   - Clic derecho sobre la base de datos
   - Clic en restore
   - Seleccionar el archivo de la base de datos del proyecto (lo podés descargar del drive: Archivo "EcommerceNS.sql"
     https://drive.google.com/drive/folders/1wc4B5qLCEeQQeVHW_KKMDvD-T-AnNriQ
   - Clic derecho sobre la base de datos
   - Clic en refresh
   - Con esto se te deberían haber cargado las tablas
   - Verificar que tu usuario y contraseña personal de PgAdmin4 coincidan con lo que está en el archivo settings.py:
  ```shell
     DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'EcommerceNS',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': 5432,
        }
      }
  ```
     
### 2.  Levantar el Servidor de Desarrollo:

```shell
python manage.py runserver
```

Esto iniciará el servidor de desarrollo de Django para que puedas comenzar a trabajar en tu proyecto.

## Estructura del Proyecto

Carpetas y archivos más importantes:

- **ecomm**: Esta es la carpeta principal del proyecto.

  - `apps.py`: Configuración de las aplicaciones.
  - `forms.py`: Definición de formularios personalizados.
  - `models.py`: Definición de modelos de base de datos.
  - `urls.py`: Configuración de las direcciones URL de la aplicación.
  - `views.py`: Implementación de las vistas y lógica de la aplicación.

- **app**: Esta es la aplicación principal de la Tienda de Ropa en Línea.

  - **migrations**: Contiene archivos de migración de base de datos.
  - **static**: Aquí se almacenan los archivos estáticos como imágenes, CSS y JavaScript.
  - **templates**: Contiene los archivos HTML que definen la interfaz de usuario.

## Funcionalidades Principales

### Explorar Productos

Los usuarios pueden navegar y ver una amplia gama de productos de moda.

### Agregar al Carrito

Los productos se pueden agregar al carrito de compras para su posterior compra.

### Registro y Autenticación

Los usuarios pueden registrarse y autenticarse en el sitio.

### Recuperación de Contraseña

La función de recuperación de contraseña permite a los usuarios restablecer sus contraseñas a través del correo electrónico.

### Gestión de Direcciones de Envío

Los usuarios pueden agregar y gestionar múltiples direcciones de envío.

### Cambio de Contraseña

Los usuarios pueden cambiar sus contraseñas desde su perfil.

### Cerrar Sesión

Los usuarios pueden cerrar sesión de sus cuentas.

## Uso de Bloques y Templates

La estructura del proyecto utiliza bloques y templates para facilitar la personalización de las páginas. Puedes modificar los archivos HTML dentro de la carpeta `templates` para cambiar la apariencia de la aplicación. Los archivos HTML están diseñados para ser modulares, lo que facilita la creación de nuevas páginas y la personalización de las existentes.

Este README proporciona una visión general del proyecto y cómo configurarlo.
```
