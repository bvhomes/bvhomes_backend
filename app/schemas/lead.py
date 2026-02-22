from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    city: Optional[str] = None
    product_id: int
    message: Optional[str] = None

class LeadResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    city: Optional[str]
    product_id: int
    message: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
