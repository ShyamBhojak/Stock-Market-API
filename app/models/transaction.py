from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    transaction_type = Column(String(10), nullable=False)
    quantity = Column(Numeric(15,4), nullable=False)
    price = Column(Numeric(15,2), nullable=False)
    totalAmount = Column(Numeric(15,2), nullable=False)
    createdAt = Column(DateTime(timezone=True),server_default=func.now())
    