from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Shedstate(Base):
    __tablename__ = "shedstate"

    shedstate = Column(Integer, primary_key=True, index= True)

    shedname = Column(VARCHAR(25), unique= True,nullable=False)
    sheddescription = Column(VARCHAR(200), nullable= False)

    del_ = Column("del",Boolean, default=False)