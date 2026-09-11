from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockResponse

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