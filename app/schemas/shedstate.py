from pydantic import BaseModel, Field

class Shedstatebase(BaseModel):
    shedname: str = Field(max_length=25)
    sheddescription: str = Field(max_length=200)

class Shedstatecreate(Shedstatebase):
    pass

class ShedstateOut(Shedstatebase):
    shedstate:int
    del_: bool

    class Config:
        orm_mode = True
