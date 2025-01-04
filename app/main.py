import logging
from fastapi import FastAPI
from app.routes import user, category, product, auth

# Configuración básica de logging
log_file = "gestion_inventario.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file, mode='a', encoding='utf-8')
    ]
)
logger = logging.getLogger("gestion-inventario")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Endpoint '/' consultado")
    return {"message": "Bienvenido a la API de gestión de inventario"}

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(product.router)

