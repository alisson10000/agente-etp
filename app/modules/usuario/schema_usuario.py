from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime


# ===============================
# Enums de Tipo e Status de Usuário
# ===============================

class TipoUsuarioEnum(str, Enum):
    admin = 'admin'
    comum = 'comum'
    gestor = 'gestor'


class StatusUsuarioEnum(str, Enum):
    ativo = 'ativo'
    inativo = 'inativo'
    bloqueado = 'bloqueado'


# =======================================
# Schema base para compartilhamento comum
# =======================================

class UsuarioBase(BaseModel):
    nome: str = Field(..., max_length=255, description="Nome completo do usuário")
    email: EmailStr = Field(..., max_length=255, description="Email único do usuário")
    tipo: Optional[TipoUsuarioEnum] = Field(default=TipoUsuarioEnum.comum, description="Tipo de usuário")
    status: Optional[StatusUsuarioEnum] = Field(default=StatusUsuarioEnum.ativo, description="Status da conta do usuário")


# =========================================
# Schema para criação de novo usuário
# =========================================

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=6, max_length=255, description="Senha do usuário (mínimo 6 caracteres)")


# ========================================
# Schema para atualização parcial do usuário
# ========================================

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, max_length=255, description="Nome completo do usuário")
    email: Optional[EmailStr] = Field(default=None, max_length=255, description="Email único do usuário")
    senha: Optional[str] = Field(default=None, min_length=6, max_length=255, description="Nova senha (mínimo 6 caracteres)")
    tipo: Optional[TipoUsuarioEnum] = Field(default=None, description="Tipo de usuário")
    status: Optional[StatusUsuarioEnum] = Field(default=None, description="Status da conta do usuário")


# ======================================
# Schema para resposta/retorno do usuário
# ======================================

class UsuarioResponse(UsuarioBase):
    id: int = Field(..., description="Identificador único do usuário")
    data_criacao: datetime = Field(..., description="Data de criação do usuário")
    ultimo_login: Optional[datetime] = Field(default=None, description="Data do último login")

    class Config:
        from_attributes = True  # Para converter de ORM (SQLAlchemy) para Pydantic
