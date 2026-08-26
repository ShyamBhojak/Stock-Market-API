from fastapi import FastAPI

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