from app.database import engine
from app.models import Base

# Crear todas las tablas
Base.metadata.create_all(bind=engine)
