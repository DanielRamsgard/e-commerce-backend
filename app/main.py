from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from . import send_res

class Order(BaseModel):
    email: str
    total: int
    item_list: str
    address: str

app = FastAPI()


@app.post("/order/")
async def send_mail(order : Order):
    try: 
        send_res(order.email, order.total, order.address, order.item_list)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))