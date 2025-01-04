from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import InventoryBase as BaseInventory

class Category(BaseInventory):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relación con los productos
    products = relationship("Product", back_populates="category")
    