from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DECIMAL
from app.db.config import Base

class Typereport(Base):
    __tablename__ = "typereport"
    #pk
    typereport = Column(Integer, primary_key=True, index= True)

    typename = Column(VARCHAR(25), unique= True,nullable=False)
    description = Column(VARCHAR(200), nullable= False)

    #borrado suave
    del_ = Column("del",Boolean, default=False)