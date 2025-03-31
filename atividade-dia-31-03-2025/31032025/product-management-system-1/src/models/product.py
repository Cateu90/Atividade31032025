from pydantic import BaseModel, Field, condecimal

class Product(BaseModel):
    id: int = Field(..., description="The unique identifier for the product")
    name: str = Field(..., min_length=1, description="The name of the product")
    description: str = Field(..., description="A brief description of the product")
    price: condecimal(gt=0, description="The price of the product, must be greater than zero")