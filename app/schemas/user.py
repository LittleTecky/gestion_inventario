from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario, entre 3 y 50 caracteres.")
    email: EmailStr = Field(..., description="Correo electrónico válido.")
    password: str = Field(..., min_length=6, description="Contraseña, mínimo 6 caracteres.")
    role: Optional[str] = Field("user", description="Rol del usuario, por defecto 'user'.")

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
    role: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str
    