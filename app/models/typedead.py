from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Typedead(Base):
    __tablename__ = "typedead"
    #pk
    typedead = Column(Integer, primary_key=True, index= True)

    typedeadname = Column(VARCHAR(25), unique= True,nullable=False)
    typedeaddescription = Column(VARCHAR(200), nullable= False)

    #borrado suave
    del_ = Column("del",Boolean, default=False)