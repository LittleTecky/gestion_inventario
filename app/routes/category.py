from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.database import get_inventory_db
from app.security import verify_token

def require_auth(token: dict = Depends(verify_token)):
    pass

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse, dependencies=[Depends(require_auth)])
def create_category(category: CategoryCreate, db: Session = Depends(get_inventory_db)):
    return crud.create_category(db=db, category=category)

@router.get("/{category_id}", response_model=CategoryResponse, dependencies=[Depends(require_auth)])
def get_category(category_id: int, db: Session = Depends(get_inventory_db)):
    return crud.get_category(db, category_id=category_id)

@router.get("/", response_model=list[CategoryResponse], dependencies=[Depends(require_auth)])
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_inventory_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@router.put("/{category_id}", response_model=CategoryResponse, dependencies=[Depends(require_auth)])
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_inventory_db)):
    return crud.update_category(db, category_id=category_id, category=category)

@router.delete("/{category_id}", response_model=CategoryResponse, dependencies=[Depends(require_auth)])
def delete_category(category_id: int, db: Session = Depends(get_inventory_db)):
    return crud.delete_category(db, category_id=category_id)