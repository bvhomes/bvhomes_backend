from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    city = Column(String(100), nullable=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    message = Column(Text, nullable=True)
    status = Column(String(50), default="new")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
