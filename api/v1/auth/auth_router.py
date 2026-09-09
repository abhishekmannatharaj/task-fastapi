from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import User
from api.v1.auth.user_schemas import UserCreate, UserResponse, Token
from api.v1.auth.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication & Users"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered."
        )

    hashed_pwd = hash_password(user_in.password)
    new_user = User(email=user_in.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user or not verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials."
        )

    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}