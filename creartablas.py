from app.database import UserBase, InventoryBase, user_engine, inventory_engine
from app.routes import user, category, product

# Crear tablas para la base de datos de usuarios
print("Creando tablas para la base de datos de usuarios...")
UserBase.metadata.create_all(bind=user_engine)
print("Tablas creadas en la base de datos de usuarios.")

# Crear tablas para la base de datos de inventario
print("Creando tablas para la base de datos de inventario...")
InventoryBase.metadata.create_all(bind=inventory_engine)
print("Tablas creadas en la base de datos de inventario.")
