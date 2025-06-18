from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Race(Base):
    __tablename__ = "race"
    #pk
    race = Column(Integer, primary_key=True, index= True)

    racename = Column(VARCHAR(25), unique= True,nullable=False)
    description = Column(VARCHAR(200), nullable= False)
    minweigh = Column(DECIMAL(5,2), nullable= False)
    maxweigh = Column(DECIMAL(5,2), nullable= False)

    #borrado suave
    del_ = Column("del",Boolean, default=False)