from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., gt=0)

