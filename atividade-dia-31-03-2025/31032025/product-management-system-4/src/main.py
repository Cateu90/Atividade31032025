from pydantic import BaseModel, Field
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = Field(default=None, description="ID do produto")
    nome: str = Field(..., description="Nome do produto")
    preco: float = Field(..., gt=0, description="Preço do produto, deve ser maior que zero")
    quantidade: int = Field(..., ge=0, description="Quantidade do produto, deve ser maior ou igual a zero")