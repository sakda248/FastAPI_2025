from fastapi import FastAPI
from routes.r_products import router as products_router
from routes.r_customers import router as customers_router
from pydantic import BaseModel

app = FastAPI()

app.include_router(products_router)
app.include_router(customers_router)


