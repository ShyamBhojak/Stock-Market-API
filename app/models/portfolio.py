from sqlalchemy import Column, String, Numeric, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.base import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    stock_id = Column(
        Integer,
        ForeignKey("stocks.id"),
        nullable=False
    )

    quantity = Column(
        Numeric(15,4),
        default=0,
        nullable=False
    )

    average_price = Column(
        Numeric(15,2),
        default=0,
        nullable=False
    )
    createdAt = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updatedAt = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )