from fastapi import APIRouter
from models.c_products import Product
from fastapi.responses import JSONResponse

router = APIRouter()

products = [
    { "id": 1,"name": "ดาบมังกร", "price": 1000, "quantity": 5},
    { "id": 2,"name": "กระบี่อิงฟ้า", "price": 2000, "quantity": 10}
    ]

@router.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "สินค้าเพิ่มสําเร็จ!", "product": product}

@router.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return {"error": "ไมพบสสินค้า!"}

@router.get("/products/")
def get_producs():

    return {"result": products}

@router.put("/products/{id}")
def update_product(id: int, updated_product:Product):
    for index, product in enumerate(products):
        if product["id"] == id:
            products[index] = updated_product
            return {"message": "สินค้าอัปเดตสําเร็จ!", "product": updated_product} 
    return {"error": "ไม่พบสินค้า!"}

@router.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product["id"] == id:
            del products[index]
            return{"message":"สนสินค้าถูกลบแล้ว!"}
    return {"error": "ไม่พบสินค้า!"}