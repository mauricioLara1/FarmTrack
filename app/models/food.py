from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Food(Base):
    __tablename__ = "food"
    #pk
    food = Column(Integer, primary_key=True, index= True)

    namefood = Column(VARCHAR(25), unique= True,nullable=False)
    infofood = Column(VARCHAR(200), nullable= False)
    amountlb= Column(DECIMAL(10,2), nullable= False)

    #borrado suave
    del_ = Column("del",Boolean, default=False)