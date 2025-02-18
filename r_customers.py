from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.c_users import User
from models.c_table_users import T_User
from conn_db import get_db

from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/users")
def add_user(user: User, db: Session = Depends(get_db)):
    db_user = T_User(username=user.username, email=user.email, full_name=user.full_name, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "เพิ่ม User สำเร็จ!", "user": user}

@router.get("/users/")
def get_user(db: Session = Depends(get_db)):
    user = db.query(T_User).limit(10).all()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(T_User).filter(T_User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
def update_user(user_id: int, user_data: User, db: Session = Depends(get_db)):
    user = db.query(T_User).filter(T_User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.username = user_data.username
    user.email = user_data.email
    user.full_name = user_data.full_name
    user.hashed_password = user_data.password
    
    db.commit()
    db.refresh(user)
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(T_User).filter(T_User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}