from pydantic import BaseModel

class StockCreate(BaseModel):
    symbol:str
    company:str
    exchange:str
    sector: str | None = None
    currentprice: float

class StockResponse(BaseModel):
    id:int
    symbol: str
    company: str
    exchange: str
    sector: str | None
    currentprice: float

    class Config:
        from_attributes: True