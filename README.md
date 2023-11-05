# E-commerce NutriStyle
NutriStyle es un sitio web de E-Commerce formado por un equipo multidisciplinario de expertos en nutrición, medicina y cocina. Nuestra plataforma especializada ofrece viandas saludables.
Esta aplicación ha sido desarrollada utilizando el marco de trabajo Django, junto con tecnologías web como Bootstrap, HTML, CSS , JavaScript y como base de datos PostgreSQL.

<ul>
<h2>Integrantes: </h2>
  <li> Florencia Oviedo 💻</li>
  <li> Fernando Rojas 💻</li>
  <li> Dana Angellotti 💻</li>
  <li>Martin Verstraeten 💻</li>
  <li> Gabriela Silva 💻</li>
  <li> Ivana Germir 💻</li>
  <li> Adriana Da Silva 💻</li>
  <li> Juan Pablo Ayoroa 💻</li>
 </ul>

## Metodología Ágiles
Aplicamos la metodologia SCRUM en el proyecto con asignaciones de tareas por sprint.

## Brief

Hemos preparado un breve informativo que proporciona detalles adicionales sobre nuestro proyecto y los pasos que seguimos para llegar al resultado final. Podés acceder a él en [Brief](https://drive.google.com/file/d/1fbLWgHTvenVI_MaYhmyX_VmZexKky5Ds/view?usp=sharing)  

## Figma
Realizamos el maquetado de nuestra página, utilizando Figma, el cual nos proporciona una gran cantidad de elementos visuales. Podés acceder a él en [Figma](https://www.figma.com/file/780vnDRRmVu9nQfBhxHqf0/NutriStyle?type=design&node-id=0-1&mode=design&t=ImzpkiP21BJktXKk-0)  

## Instalación de Bibliotecas. 
Aquí explicamos como se instalan las bibliotecan que permiten poder ver el proyecto correctamente.

Antes de comenzar con la configuración del E-commerce NutriStyle, es importante asegurarse de que todas las bibliotecas y dependencias necesarias estén instaladas. 
A continuación verán una guía paso a paso para configurar el entorno de desarrollo desde la terminal:

- En Windows:
### 1. Crear un Entorno Virtual (en "myenv" poner el nombre de tu nuevo entorno virtual):

```shell
python -m venv myenv
```

### 2. Activar el Entorno Virtual:



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

### 1. Conectar con la base de datos:  
* En PostgreSQL segui los siguientes pasos:
  
   - Ingresa a PGAdmin4 y creeá una nueva base de datos llamada "EcommerceNS"
   - Click derecho sobre la base de datos
   - Click en restore
   - Seleccionar el archivo de la base de datos del proyecto ( se encuentra en el proyecto como archivo: "EcommerceNS.sql")
   - Click derecho sobre la base de datos
   - Click en refresh
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

Esto iniciará el servidor de desarrollo de Django para que puedas ver el sitio web. Recordatorio: Siempre con el entorno virtual activado.

¡Muchas gracias!


