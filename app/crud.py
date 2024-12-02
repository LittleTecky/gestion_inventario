from sqlalchemy.orm import Session
from app import models, schemas, security
from fastapi import HTTPException, status
from typing import Optional

# Crear un nuevo usuario
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.hash_password(user.password)  # Asegúrate de implementar hash_password
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener un usuario por su ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Actualizar un usuario
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        if user.username:
            db_user.username = user.username
        if user.email:
            db_user.email = user.email
        if user.password:
            db_user.hashed_password = security.hash_password(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user

# Eliminar un usuario
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Crear una categoría
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Obtener una categoría por su ID
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

# Obtener todas las categorías
def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()

# Actualizar una categoría
def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category and category.name:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)
    return db_category

# Eliminar una categoría
def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# Crear un producto
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Obtener todos los productos
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

# Filtrar productos por rango de precios
def get_products_by_price_range(db: Session, min_price: float, max_price: float):
    return db.query(models.Product).filter(models.Product.price >= min_price, models.Product.price <= max_price).all()


# Obtener productos por categoría
def get_products_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Product).filter(models.Product.category_id == category_id).offset(skip).limit(limit).all()

# Obtener un producto por ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Actualizar un producto
def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        if product.name:
            db_product.name = product.name
        if product.description:
            db_product.description = product.description
        if product.price:
            db_product.price = product.price
        if product.category_id:
            db_product.category_id = product.category_id
        db.commit()
        db.refresh(db_product)
    return db_product

# Eliminar un producto
def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# Verificar las credenciales del usuario y generar el token JWT
def authenticate_user(db: Session, username: str, password: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user and security.verify_password(password, db_user.hashed_password):
        return db_user
    return None
