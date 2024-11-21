from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate

def create_item(db: Session, category_name: str, item: ItemCreate):
    db_item = Item(category=category_name, name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_category_items(db: Session, category_name: str):
    return db.query(Item).filter(Item.category == category_name).all()



def delete_item(db: Session, item_id: int):
    """
    Delete an item by ID.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None
