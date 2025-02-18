from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database.db"

# สร้าง Engine เชื่อมต่อฐานข้อมูล
engine = create_engine(DATABASE_URL)

# สร้าง Session สำหรับติดต่อฐานข้อมูล
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง Base สำหรับ ORM Models
Base = declarative_base()

# ฟังก์ชันใช้สร้าง session ในแต่ละ request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
