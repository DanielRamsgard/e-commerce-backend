from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app_e_commerce.send_res import send_res
from typing import Annotated
import app_e_commerce.models
from app_e_commerce.models import CustomerOrder
from app_e_commerce.database import engine, SessionLocal
from sqlalchemy.orm import Session


class Order(BaseModel):
    email: str
    total: int
    item_list: str
    address: str

app = FastAPI()
app_e_commerce.models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


db_dependancy = Annotated[Session, Depends(get_db)]


origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://d1jg1a4h2yqjdm.cloudfront.net",
    "http://localhost:80"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/order/")
async def send_mail(order : Order, db : db_dependancy):
    db_order = CustomerOrder(
        email=order.email,
        address=order.address,
        total=order.total,
        order=order.item_list
    )
    db.add(db_order)
    db.commit()

    try: 
        send_res(order.email, order.total, order.address, order.item_list)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))