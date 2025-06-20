from sqlalchemy.orm import Session
from app.models.typereport import Typereport
from app.schemas.typereport import TypereportCreate

def get_typereports(db: Session):
    return db.query(Typereport).filter(Typereport.del_ == False).all()

def create_typereport(db: Session, typereport_data: TypereportCreate):
    db_item = Typereport(**typereport_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def soft_delete_typereport(db: Session, typereport_id: int):
    db_item = db.query(Typereport).filter(Typereport.typereport == typereport_id).first()
    if db_item:
        db_item.del_ = True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_typereport(db: Session, typereport_id: int):
    db_item = db.query(Typereport).filter(Typereport.typereport == typereport_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item