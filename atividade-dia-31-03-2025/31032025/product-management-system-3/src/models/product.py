from pydantic import BaseModel, Field, condecimal, conint

class Product(BaseModel):
    id: conint(ge=1)
    name: str = Field(..., max_length=100)
    price: condecimal(gt=0)
    stock: conint(ge=0)

    class Config:
        orm_mode = True