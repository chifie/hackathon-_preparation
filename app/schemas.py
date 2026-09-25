from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    quantity: int
    sales_last_7_days: int


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True