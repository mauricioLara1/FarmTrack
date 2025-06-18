from sqlalchemy.orm import Session
from app.models.race import Race
from app.schemas.race import RaceCreate

def get_races(db: Session):
    return db.query(Race).filter(Race.del_ == False).all()

def create_race(db: Session, race_data: RaceCreate):
    db_item = Race(**race_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def soft_delete_race(db: Session, race_id: int):
    db_item = db.query(Race).filter(Race.race == race_id).first()
    if db_item:
        db_item.del_ = True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_race(db: Session, race_id: int):
    db_item = db.query(Race).filter(Race.race == race_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
