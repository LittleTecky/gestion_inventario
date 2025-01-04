from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.database import get_inventory_db
from app.security import verify_token

def require_auth(token: dict = Depends(verify_token)):
    pass

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse, dependencies=[Depends(require_auth)])
def create_product(product: ProductCreate, db: Session = Depends(get_inventory_db)):
    return crud.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=ProductResponse, dependencies=[Depends(require_auth)])
def get_product(product_id: int, db: Session = Depends(get_inventory_db)):
    return crud.get_product(db, product_id=product_id)

@router.get("/", response_model=list[ProductResponse], dependencies=[Depends(require_auth)])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_inventory_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@router.get("/filter/price", response_model=list[ProductResponse], dependencies=[Depends(require_auth)])
def get_products_by_price_range(min_price: float, max_price: float, db: Session = Depends(get_inventory_db)):
    return crud.get_products_by_price_range(db, min_price=min_price, max_price=max_price)

@router.get("/category/{category_id}", response_model=list[ProductResponse], dependencies=[Depends(require_auth)])
def get_products_by_category(category_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_inventory_db)):
    return crud.get_products_by_category(db, category_id=category_id, skip=skip, limit=limit)

@router.put("/{product_id}", response_model=ProductResponse, dependencies=[Depends(require_auth)])
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_inventory_db)):
    return crud.update_product(db, product_id=product_id, product=product)