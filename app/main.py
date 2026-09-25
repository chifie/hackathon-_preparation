from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Product
from .schemas import ProductCreate, ProductResponse


Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartStock AI")


@app.get("/")
def home():
    return {
        "message": "SmartStock AI API is running"
    }
@app.post("/products", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        quantity=product.quantity,
        sales_last_7_days=product.sales_last_7_days
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()