from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.exceptions import ResourceNotFoundException, ConflictException
from app.security import hash_password, verify_password
from fastapi import HTTPException, status

# Crear un nuevo usuario
def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ConflictException("A user with this email already exists.")

    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role or "user"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener un usuario por su ID
def get_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise ResourceNotFoundException("User not found.")
    return db_user

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Actualizar un usuario
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise ResourceNotFoundException("User not found.")

    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.hashed_password = hash_password(user.password)
    if user.role:
        db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar un usuario
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise ResourceNotFoundException("User not found.")

    db.delete(db_user)
    db.commit()
    return db_user

# Crear una categoría
def create_category(db: Session, category: CategoryCreate):
    existing_category = db.query(Category).filter(Category.name == category.name).first()
    if existing_category:
        raise ConflictException("A category with this name already exists.")

    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Obtener una categoría por su ID
def get_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise ResourceNotFoundException("Category not found.")
    return db_category

# Obtener todas las categorías
def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

# Actualizar una categoría
def update_category(db: Session, category_id: int, category: CategoryUpdate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise ResourceNotFoundException("Category not found.")

    if category.name:
        db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

# Eliminar una categoría
def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise ResourceNotFoundException("Category not found.")

    db.delete(db_category)
    db.commit()
    return db_category

# Crear un producto
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
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
    return db.query(Product).offset(skip).limit(limit).all()

# Filtrar productos por rango de precios
def get_products_by_price_range(db: Session, min_price: float, max_price: float):
    return db.query(Product).filter(Product.price >= min_price, Product.price <= max_price).all()

# Obtener productos por categoría
def get_products_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 10):
    return db.query(Product).filter(Product.category_id == category_id).offset(skip).limit(limit).all()

# Obtener un producto por ID
def get_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise ResourceNotFoundException("Product not found.")
    return db_product

# Actualizar un producto
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise ResourceNotFoundException("Product not found.")

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
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise ResourceNotFoundException("Product not found.")

    db.delete(db_product)
    db.commit()
    return db_product

# Verificar las credenciales del usuario y generar el token JWT
def authenticate_user(db: Session, username: str, password: str):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials."
        )
    return db_user
    