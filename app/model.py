from sqlalchemy import Column, Integer, String

from .db import Base

# model/table
class  Place(Base):
    __tablename__ = "address_demo"

    # fields 
    id = Column(Integer,primary_key=True, index=True)
    latititude = Column(Integer)
    longitude = Column(Integer)
