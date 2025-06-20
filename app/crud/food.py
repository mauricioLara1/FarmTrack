from sqlalchemy.orm import Session
from app.models.food import Food
from app.schemas.food import FoodCreate

def get_foods(db: Session):
    return db.query(Food).filter(Food.del_ == False).all()

def create_food(db: Session, food_data: FoodCreate):
    db_item = Food(**food_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def soft_delete_food(db: Session, food_id: int):
    db_item = db.query(Food).filter(Food.food == food_id).first()
    if db_item:
        db_item.del_ = True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_food(db: Session, food_id: int):
    db_item = db.query(Food).filter(Food.food == food_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item