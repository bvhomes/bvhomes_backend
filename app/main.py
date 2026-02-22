from app.models.lead import Lead
from fastapi import FastAPI
from app.database import engine
from app.database import Base
from app.models.product import Product
from app.routes.product import router as product_router
from app.models.user import User
from app.routes.auth import router as auth_router
from app.routes.lead import router as lead_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(lead_router)
app.include_router(product_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "BV Homes Backend Running"}
