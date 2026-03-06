
from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    created_at: datetime

    class Config:
        from_attributes = True
