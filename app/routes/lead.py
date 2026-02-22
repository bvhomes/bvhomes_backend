
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.lead import Lead
from app.models.product import Product
from app.schemas.lead import LeadCreate, LeadResponse
from app.core.auth import get_current_admin
from app.services.email_service import send_lead_notification
from app.services.whatsapp_service import send_whatsapp_message

router = APIRouter(prefix="/leads", tags=["Leads"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LeadResponse)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == lead.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_lead = Lead(**lead.dict())
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    send_lead_notification(new_lead)
    send_whatsapp_message(new_lead.phone)

    return new_lead

@router.get("/", response_model=List[LeadResponse])
def get_all_leads(
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    return db.query(Lead).order_by(Lead.created_at.desc()).all()
