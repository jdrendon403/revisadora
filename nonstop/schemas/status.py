from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Status(BaseModel):
    articulo: str = Field(max_length=40, default=None)
    cliente: str = Field(max_length=40, default=None)
    n_articulo: str = Field(max_length=40, default=None)
    color: str = Field(max_length=40, default=None)
    peso: float = Field(default=0.0)
    metros: float = Field(default=0.0)
    n_rollo: int = Field(default=0)
    rendimiento: float = Field(default=0.0)
    operario: str = Field(max_length=40, default=None)
    ancho: float = Field(default=0.0)
    last_update: Optional[str] = Field(default=None)