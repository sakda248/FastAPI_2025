from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# 🔹 กำหนด Database URL (SQLite)
DATABASE_URL = "sqlite:///./database.db"

# 🔹 สร้าง engine เชื่อมต่อกับฐานข้อมูล
engine = create_engine(DATABASE_URL, echo=True)

# 🔹 สร้าง Base สำหรับกำหนดตาราง
Base = declarative_base()

# 🔹 กำหนดโครงสร้างตาราง users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)

# 🔹 กำหนดโครงสร้างตาราง products
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)

# 🔹 ฟังก์ชันสร้างตาราง
def init_db():
    print("📌 กำลังสร้างตารางฐานข้อมูล...")
    Base.metadata.create_all(bind=engine)
    print("✅ ตารางถูกสร้างเสร็จเรียบร้อย!")

# 🔹 เรียกใช้ฟังก์ชันสร้างตาราง
if __name__ == "__main__":
    init_db()
