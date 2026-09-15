from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockResponse

from fastapi import HTTPException

router = APIRouter(prefix="/stocks",tags=["Stocks"])

@router.post("/createstock", response_model=StockResponse)
def createstock(stock: StockCreate, db:Session = Depends(get_db)):
    new_stock = Stock(
        symbol = stock.symbol,
        company = stock.company,
        exchange = stock.exchange,
        sector = stock.sector,
        currentprice = stock.currentprice
    )

    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)

    return new_stock

@router.get("/")
def getstocks(db:Session = Depends(get_db)):
    stocks = db.query(Stock).all()
    return {
        "status":"All Stocks",
        "Stocks": stocks
    }
@router.get("/{stock_id}")
def getstocks(stock_id: int, db:Session = Depends(get_db)):
    stock = db.query(Stock).get(stock_id)
    if not stock:
        return HTTPException(404,f"Stock not found at id: {stock_id}")
    return{
        "status":"Stock Found",
        "stock":stock
    }