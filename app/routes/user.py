from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.database import get_user_db
from app.security import verify_token
from app.exceptions import ForbiddenError

router = APIRouter(prefix="/users", tags=["Users"])

def is_admin(token: dict = Depends(verify_token)):
    if token.get("role") != "admin":
        raise ForbiddenError(detail="No tienes permisos para realizar esta acción")

@router.post("/", response_model=UserResponse, dependencies=[Depends(is_admin)])
def create_user(user: UserCreate, db: Session = Depends(get_user_db)):
    return crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=UserResponse, dependencies=[Depends(is_admin)])
def get_user(user_id: int, db: Session = Depends(get_user_db)):
    return crud.get_user(db, user_id=user_id)

@router.get("/", response_model=list[UserResponse], dependencies=[Depends(is_admin)])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_user_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@router.put("/{user_id}", response_model=UserResponse, dependencies=[Depends(is_admin)])
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_user_db)):
    return crud.update_user(db, user_id=user_id, user=user)

@router.delete("/{user_id}", response_model=UserResponse, dependencies=[Depends(is_admin)])
def delete_user(user_id: int, db: Session = Depends(get_user_db)):
    return crud.delete_user(db, user_id=user_id)

