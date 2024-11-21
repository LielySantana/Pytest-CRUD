from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    name = Column(String)
    description = Column(String)