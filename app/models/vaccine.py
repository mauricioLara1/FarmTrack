from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Vaccine(Base):
    __tablename__ = "vaccine"

    vaccine = Column(Integer, primary_key=True, index= True)
    vaccinename = Column(VARCHAR(25), unique= True,nullable=False)
    vaccinedescription = Column(VARCHAR(200), nullable= False)