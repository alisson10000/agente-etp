from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class VisibilidadeEnum(str, Enum):
    publico = "publico"
    privado = "privado"
    restrito = "restrito"

class StatusEnum(str, Enum):
    rascunho = "rascunho"
    em_andamento = "em_andamento"
    concluido = "concluido"


# Schema Base
class ETPBase(BaseModel):
    titulo: str = Field(..., max_length=255)
    descricao: Optional[str] = None
    visibilidade: Optional[VisibilidadeEnum] = VisibilidadeEnum.privado
    status: Optional[StatusEnum] = StatusEnum.rascunho


# Schema para criação
class ETPCreate(ETPBase):
    criado_por: int  # ID do usuário


# Schema para atualização
class ETPUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    visibilidade: Optional[VisibilidadeEnum] = None
    status: Optional[StatusEnum] = None


# Schema de resposta
class ETPResponse(ETPBase):
    id: int
    criado_por: int
    data_criacao: datetime

    class Config:
        from_attributes = True
