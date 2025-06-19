
from sqlalchemy.orm import Session
from app.models.typedead import Typedead
from app.schemas.typedead import Typedeadcreate

def get_typedeads(db: Session):
    return db.query(Typedead).filter(Typedead.del_ == False).all()

def create_typedead(db: Session, typedead_data: Typedeadcreate):
    db_item = Typedead(**typedead_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def soft_delete_typedead(db: Session, typedead_id: int):
    db_item = db.query(Typedead).filter(Typedead.typedead == typedead_id).first()
    if db_item:
        db_item.del_ = True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_typedead(db: Session, typedead_id: int):
    db_item = db.query(Typedead).filter(Typedead.typedead == typedead_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
