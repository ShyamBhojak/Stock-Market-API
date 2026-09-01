from fastapi import FastAPI
from app.core.database import engine
from app.core.base import Base
from app.models import User, Stock, Portfolio

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Stock Market API",
    description="Backend API for Stock Market Application",
    version="1.0.0"
)

@app.get("/")
def home():
    return{
        "message":"Stock Market API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status":"ok"
    }