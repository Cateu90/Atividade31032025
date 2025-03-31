from pydantic import BaseModel, Field, condecimal, conint

class Produto(BaseModel):
    id: int = Field(default=None, description="Identificador único do produto")
    nome: str = Field(..., max_length=100, description="Nome do produto")
    preco: condecimal(gt=0, description="Preço do produto, deve ser maior que zero")
    quantidade: conint(ge=0, description="Quantidade do produto, deve ser maior ou igual a zero")