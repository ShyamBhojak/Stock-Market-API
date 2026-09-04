from sqlalchemy import Integer, String, Column, Numeric, DateTime
from sqlalchemy.sql import func

from app.core.base import Base

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    symbol = Column(
        String(20),
        unique=True,
        index=True,
        nullable=False
    )
    company = Column(String(50), nullable=False)
    exchange = Column(String(50), nullable=False)
    sector = Column(String(100),nullable=True)
    currentprice = Column(Numeric(15,2), default=0)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
