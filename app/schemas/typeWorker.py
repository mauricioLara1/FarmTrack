from pydantic import BaseModel, Field

class Typeworkerbase(BaseModel):
    title: str = Field(max_length=25)
    description: str = Field(max_length=200)

class Typeworkercreate(Typeworkerbase):
    pass

class TypeworkerOut(Typeworkerbase):
    typeworker:int

    class Config:
        orm_mode = True
