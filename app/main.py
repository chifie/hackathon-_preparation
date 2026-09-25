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

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()