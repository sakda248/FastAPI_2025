## 📌 คำสั่งตรวจสอบข้อมูลใน Pydantic (Data Validation & Constraints)
Pydantic เป็นเครื่องมือที่ช่วย ตรวจสอบความถูกต้องของข้อมูล (Data Validation) และ กำหนดข้อจำกัด (Constraints) ในการรับค่าต่าง ๆ ใน FastAPI โดยอัตโนมัติ

### 🔹 1. คำสั่งตรวจสอบข้อมูลพื้นฐาน
✅ กำหนดประเภทข้อมูล

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str   # ต้องเป็น string เท่านั้น
    price: float   # ต้องเป็นตัวเลขทศนิยม
    quantity: int   # ต้องเป็นจำนวนเต็ม
```
✅ ถ้าป้อนผิดประเภท → จะเกิด ValidationError ทันที 🚨

### 🔹 2. กำหนดค่าขั้นต่ำ-ขั้นสูง (constr, conint, confloat)
✅ ใช้ constr สำหรับ string

```python
from pydantic import BaseModel, constr

class User(BaseModel):
    username: constr(min_length=3, max_length=20)  # ความยาวระหว่าง 3-20 ตัวอักษร
```
✅ ใช้ conint สำหรับ int

```python
from pydantic import conint

class Product(BaseModel):
    stock: conint(ge=0, le=100)  # ค่าต้องอยู่ระหว่าง 0-100
```
✅ ใช้ confloat สำหรับ float

```python
from pydantic import confloat

class Order(BaseModel):
    discount: confloat(ge=0, le=1)  # ค่าส่วนลดต้องอยู่ระหว่าง 0.0 - 1.0
📌 หมายเหตุ:

ge=x → ต้องมากกว่าหรือเท่ากับ x (greater than or equal)
le=x → ต้องน้อยกว่าหรือเท่ากับ x (less than or equal)
```

### 🔹 3. ตรวจสอบค่า Enum (กำหนดค่าที่รับได้)
✅ ใช้ Enum เพื่อตรวจสอบค่าที่อนุญาต

```python
from pydantic import BaseModel
from enum import Enum

class Category(str, Enum):
    electronics = "electronics"
    fashion = "fashion"
    food = "food"

class Product(BaseModel):
    name: str
    category: Category  # ต้องเป็นค่าที่อยู่ใน Category เท่านั้น
```
📌 ถ้าส่งค่าอื่นที่ไม่ใช่ "electronics", "fashion", "food" จะเกิด Error

### 🔹 4. ตรวจสอบรูปแบบอีเมล & URL
✅ ใช้ EmailStr และ AnyUrl

```python
from pydantic import BaseModel, EmailStr, AnyUrl

class User(BaseModel):
    email: EmailStr  # ต้องเป็นอีเมลที่ถูกต้อง
    website: AnyUrl  # ต้องเป็น URL ที่ถูกต้อง
```
📌 ถ้าใส่อีเมลผิดรูปแบบ เช่น "hello.com" ระบบจะ Reject ทันที

### 🔹 5. ใช้ Field เพื่อกำหนดค่าขั้นต่ำ, ค่าเริ่มต้น
✅ ใช้ Field เพื่อกำหนดเงื่อนไขเพิ่มเติม

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    age: int = Field(default=18, ge=18, le=100)  # อายุเริ่มต้น 18 และต้องอยู่ในช่วง 18-100 ปี
    username: str = Field(..., min_length=3, max_length=15)  # บังคับต้องกรอก
```
📌 ... หมายถึงค่าที่ต้องใส่ ไม่สามารถเว้นว่างได้

### 🔹 6. ตรวจสอบข้อมูล List และ Dict
✅ ตรวจสอบ List ที่ต้องมีค่าอย่างน้อย 1 ค่า

```python
from pydantic import BaseModel

class Order(BaseModel):
    items: list[str]  # ต้องเป็น list ของ string
```

✅ ตรวจสอบ Dictionary

```python
class Config(BaseModel):
    settings: dict[str, int]  # Dictionary ที่ key เป็น string และ value เป็น int
```
### 🔹 7. กำหนดเงื่อนไขเชิงตรรกะด้วย @validator
✅ สามารถสร้างเงื่อนไขเพิ่มเติมได้ เช่น ห้ามมีช่องว่างใน username

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str

    @validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("Username ห้ามมีช่องว่าง")
        return v
```
📌 ถ้าป้อน "John Doe" จะเกิด Error ทันที!

