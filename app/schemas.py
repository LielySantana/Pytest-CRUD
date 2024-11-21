from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    category: str

    class Config:
        from_attributes = True  
