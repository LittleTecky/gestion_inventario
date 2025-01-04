# Gestión de Inventario - API RESTful

## Descripción del Proyecto

Este proyecto consiste en una API RESTful para la gestión de inventarios, que incluye operaciones CRUD sobre productos, categorías y usuarios. La API utiliza autenticación JWT para proteger endpoints y separa las bases de datos de usuarios e inventario.

## Tecnologías Utilizadas

- **Python 3.11.0**
- **FastAPI** para la creación de la API
- **SQLAlchemy** como ORM
- **PostgreSQL** como base de datos
- **JWT** para autenticación
- **Docker** para la contenedorización

---

## Ejecución del Proyecto

### 1. Ejecución Local

#### Requisitos Previos

- Python 3.11 o superior
- PostgreSQL instalado y configurado

#### Pasos

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu_usuario/gestion-inventario.git
   cd gestion-inventario
   ```

2. **Configurar el Entorno Virtual**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate   # Windows
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Variables de Entorno**
   Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```dotenv
   USER_DATABASE_URL=postgresql://postgres:password@localhost/usuarios
   INVENTORY_DATABASE_URL=postgresql://postgres:password@localhost/inventario
   SECRET_KEY=tu_clave_secreta
   ```

5. **Crear las Bases de Datos**
   Ejecutar los siguientes comandos en la terminal de PostgreSQL:
   ```sql
   CREATE DATABASE usuarios;
   CREATE DATABASE inventario;
   ```

6. **Crear las Tablas**
   ```bash
   python creartablas.py
   ```

7. **Iniciar la Aplicación**
   ```bash
   uvicorn app.main:app --reload
   ```

8. **Acceder a la API**
   La API estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000). Puedes explorar los endpoints en la documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

### 2. Despliegue con Docker

#### Requisitos Previos

- Docker y Docker Compose instalados

#### Pasos

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu_usuario/gestion-inventario.git
   cd gestion_inventario
   ```

2. **Configurar Variables de Entorno**
   Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```dotenv
   USER_DATABASE_URL=postgresql://postgres:password@db/usuarios
   INVENTORY_DATABASE_URL=postgresql://postgres:password@db/inventario
   SECRET_KEY=tu_clave_secreta
   ```

3. **Construir e Iniciar los Contenedores**
   ```bash
   docker-compose up --build
   ```

4. **Verificar la API**
   - La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).
   - La documentación interactiva está en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

5. **Verificar el Esquema de la Base de Datos**
   Ingresar al contenedor de PostgreSQL para verificar las bases de datos y tablas:
   ```bash
   docker exec -it gestion_inventario-db-1 psql -U postgres
   \l  # Listar bases de datos

   \c usuarios  # Conectar a la base de datos "usuarios"
   \dt  # Listar tablas

   # Conectar a la base de datos "inventario"
   \c inventario
   \dt  # Listar tablas en "inventario"
   ```

---

## Ejemplos de Uso de la API

### Registrar un Usuario

#### Método: `POST`
#### URL: `/register/`
#### Cuerpo:
```json
{
  "username": "usuario1",
  "email": "Usuario@example.com",
  "password": "contraseña123",
  "role": "user"
}
```

### Iniciar Sesión y Obtener Token JWT

#### Método: `POST`
#### URL: `/login/`
#### Cuerpo:
```json
{
  "username": "usuario1",
  "password": "contraseña123"
}
```

#### Respuesta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```
#### Token JWT
Algunos endpoints requieren autentificación. para acceder a estos endpoints protegidos, es necesario incluir el token JWT.

##### En la documentación interactiva
Cuando accedas a los endpoints protegidos, verás que puedes incluir el token en la sección de parámetros de consulta (query parameters) bajo la clave token.

##### En postman
1.Ve a la pestaña Params.

2.Agrega:
```
Key: token
Value: <tu_token_jwt>.
```

### Obtener Productos Filtrados por Precio

#### Método: `GET`
#### URL: `/products/filter/price?min_price=100&max_price=500`

#### Respuesta:
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

#### Método: `GET`
#### URL: `/products/category/{category_id}`

#### Respuesta:
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


