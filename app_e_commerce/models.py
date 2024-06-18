from sqlalchemy import Column, Integer, String
from app_e_commerce.database import Base

class CustomerOrder(Base):
    __tablename__ = "Orders_New"

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    address = Column(String(100))
    order = Column(String(250))
    total = Column(Integer)