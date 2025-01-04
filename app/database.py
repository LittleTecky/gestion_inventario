from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# URLs para las dos bases de datos
USER_DATABASE_URL = os.getenv("USER_DATABASE_URL")  # Base de datos para usuarios
INVENTORY_DATABASE_URL = os.getenv("INVENTORY_DATABASE_URL")  # Base de datos para inventario

# Motores de bases de datos
user_engine = create_engine(USER_DATABASE_URL)
inventory_engine = create_engine(INVENTORY_DATABASE_URL)

# Bases para cada conjunto de modelos
UserBase = declarative_base()  # Modelos de usuario
InventoryBase = declarative_base()  # Modelos de inventario

UserSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=user_engine)
InventorySessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=inventory_engine)

def get_user_db():
    db = UserSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_inventory_db():
    db = InventorySessionLocal()
    try:
        yield db
    finally:
        db.close()
        