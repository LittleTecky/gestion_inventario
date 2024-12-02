# Gestión de Inventario - API RESTful

## Descripción del Proyecto

Este proyecto consiste en una API RESTful para la gestión de inventarios de productos, categorías y usuarios. La aplicación permite realizar operaciones CRUD sobre productos, categorías y usuarios, con autenticación JWT para proteger algunos endpoints.

## Tecnologías Utilizadas

- **Python 3.11.0**
- **FastAPI** para la creación de la API
- **SQLAlchemy** como ORM
- **PostgreSQL** como base de datos
- **JWT** para autenticación
- **Docker** para la contenedorización

## Instrucciones para Configurar el Entorno de Desarrollo

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/gestion-inventario.git
cd gestion-inventario
```
### 2. Crear un Entorno Virtual

```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalar las Dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear la Base de Datos y Tablas

Ejecute el siguiente script en la terminal de PostgreSQL:

```bash
CREATE DATABASE inventory;
```

A continuación ejecute el siguiente script en :

```bash
python creartablas.py
```

### 5. Configuración de Variables de Entorno
asegúrese de tener el archivo .env en la raíz del proyecto con las siguientes variables:
```dotenv
# Para ejecutar localmente
DATABASE_URL=postgresql://postgres:1993@localhost/inventory
SECRET_KEY=mi_clave_secreta

# Para ejecutar usando Docker
DATABASE_URL=postgresql://postgres:1993@db/inventory
SECRET_KEY=mi_clave_secreta
```

## Instrucciones para Ejecutar la Aplicación Localmente

#### 1. Ejecutar la API con Uvicorn:

```bash
uvicorn app.main:app --reload
```
#### 2. La API estará disponible en http://127.0.0.1:8000.

Documentación Interactiva
Accede a la documentación interactiva de la API en http://127.0.0.1:8000/docs, donde podrás probar todos los endpoints de la API.

## Instrucciones para Desplegar la Aplicación Usando Docker

#### 1. Crear los Contenedores Docker

```bash
docker-compose up --build
```

#### 2. La Aplicación Estará Disponible en

```bash
http://127.0.0.1:8000
```
La base de datos PostgreSQL estará disponible en el puerto 5432.

## Ejemplos de Uso de la API

### Registrar un Usuario

##### Método: ```POST```
##### URL: ```/register/```
##### Cuerpo:
```json
{
  "username": "juanperez",
  "email": "juan@example.com",
  "password": "contraseña123"
}
```

### Iniciar Sesión (Login) y Obtener Token JWT

##### Método: ```POST```
##### URL: ```/login/```
##### Cuerpo:
```json
{
  "username": "juanperez",
  "password": "contraseña123"
}
```
##### Respuesta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

```

### Obtener Productos Filtrados por Precio

##### Método: ```GET```
##### URL: ```/products/filter/price?min_price=100&max_price=500```
##### Cuerpo:
```json
[
  {
    "id": 1,
    "name": "Smartphone",
    "description": "Un teléfono inteligente",
    "price": 299.99,
    "category_id": 1
  }
]

```

### Obtener Productos por Categoría

##### Método: ```GET```
##### URL: ```/products/category/{category_id}```
##### Cuerpo:
```json
[
  {
    "id": 1,
    "name": "Smartphone",
    "description": "Un teléfono inteligente",
    "price": 299.99,
    "category_id": 1
  }
]
```