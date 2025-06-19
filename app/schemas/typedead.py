
from pydantic import BaseModel, Field

class Typedeadbase(BaseModel):
    typedeadname: str = Field(max_length=25)
    typedeaddescription: str = Field(max_length=200)

class Typedeadcreate(Typedeadbase):
    pass

class TypedeadOut(Typedeadbase):
    typedead:int
    del_: bool

    class Config:
        orm_mode = True

