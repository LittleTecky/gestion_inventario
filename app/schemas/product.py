from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del producto, entre 1 y 100 caracteres.")
    description: str = Field(..., min_length=5, description="Descripción del producto, mínimo 5 caracteres.")
    price: float = Field(..., gt=0, description="Precio del producto, debe ser mayor a 0.")
    category_id: int = Field(..., description="ID de la categoría a la que pertenece el producto.")

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: Optional[int]  

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=5)
    price: Optional[float] = Field(None, gt=0)
    category_id: Optional[int] = None
