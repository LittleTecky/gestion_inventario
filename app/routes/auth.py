from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, security, exceptions
from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.database import get_user_db
import logging

router = APIRouter()
logger = logging.getLogger("gestion-inventario")

@router.post("/register/", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_user_db)):
    logger.info(f"Registrando nuevo usuario: {user.email}")
    return crud.create_user(db=db, user=user)

@router.post("/login/", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_user_db)):
    logger.info(f"Intento de login para el usuario: {user.username}")
    db_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        logger.error(f"Credenciales incorrectas para el usuario: {user.username}")
        raise exceptions.UnauthorizedError(detail="Credenciales incorrectas")

    access_token = security.create_access_token(
        data={"sub": db_user.username, "role": db_user.role}
    )
    logger.info(f"Usuario autenticado exitosamente: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected")
def protected_route(token: dict = Depends(security.verify_token)):
    logger.info("Acceso autorizado a endpoint protegido")
    return {"message": "Acceso autorizado", "user": token}
    
