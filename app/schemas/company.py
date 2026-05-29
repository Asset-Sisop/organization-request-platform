from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    description: str


class CompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int

    class Config:
        from_attributes = True