from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class Comanda(BaseModel):
    id: Optional[int] = None
    numero: int
    data_abertura: datetime
    data_fechamento: Optional[datetime] = None
    valor_total: float = 0.0

    @field_validator('numero')
    def validar_numero(cls, v):
        if v <= 0:
            raise ValueError('O número da comanda deve ser maior que zero.')
        return v

    @field_validator('data_abertura')
    def validar_data_abertura(cls, v):
        if v > datetime.now():
            raise ValueError('A data de abertura não pode ser no futuro.')
        return v

    @field_validator('data_fechamento')
    def validar_data_fechamento(cls, v, values):
        if v is not None and values['data_abertura'] is not None and v < values['data_abertura']:
            raise ValueError('A data de fechamento não pode ser anterior à data de abertura.')
        return v

    @field_validator('valor_total')
    def validar_valor_total(cls, v):
        if v < 0:
            raise ValueError('O valor total não pode ser negativo.')
        return v
