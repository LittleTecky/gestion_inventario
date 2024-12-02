from pydantic import BaseModel
from typing import Optional

# Esquema para crear un usuario
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Esquema para la respuesta del usuario (sin la contraseña)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

        # Esquema para actualizar un usuario
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

# Esquema para crear una categoría
class CategoryCreate(BaseModel):
    name: str

# Esquema para la respuesta de la categoría
class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Esquema para actualizar una categoría
class CategoryUpdate(BaseModel):
    name: Optional[str] = None

# Esquema para crear un producto
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

# Esquema para la respuesta del producto
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int

    class Config:
        orm_mode = True

# Esquema para actualizar un producto
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

# Esquema para la respuesta de login (con el token)
class Token(BaseModel):
    access_token: str
    token_type: str

# Esquema para el login (usuario y contraseña)
class UserLogin(BaseModel):
    username: str
    password: str
