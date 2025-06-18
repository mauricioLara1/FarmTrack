from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Typeworker(Base):
    __tablename__ = "typeworker"

    typeworker = Column(Integer, primary_key=True, index= True)
    title = Column(VARCHAR(25), unique= True,nullable=False)
    description = Column(VARCHAR(200), nullable= False)