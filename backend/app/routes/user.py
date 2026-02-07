from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import LoginRequest, LoginResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}


@router.post("/logout")
def logout():
    return {"message": "Logged out"}
