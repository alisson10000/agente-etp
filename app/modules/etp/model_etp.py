from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum

# Enum para visibilidade
class VisibilidadeEnum(str, enum.Enum):
    publico = "publico"
    privado = "privado"
    restrito = "restrito"

# Enum para status
class StatusEnum(str, enum.Enum):
    rascunho = "rascunho"
    em_andamento = "em_andamento"
    concluido = "concluido"

class ETP(Base):
    __tablename__ = 'etps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.rascunho)
    visibilidade = Column(Enum(VisibilidadeEnum), default=VisibilidadeEnum.privado)
    criado_por = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    data_criacao = Column(DateTime(timezone=True), default=func.now())

    # Relacionamento com o usuário
    usuario = relationship("Usuario", backref="etps")
    
    def atualizar_status(self, novo_status: str):
        self.status = novo_status

    def definir_visibilidade(self, visibilidade: str):
        self.visibilidade = visibilidade

    def __repr__(self):
        return f"<ETP(id={self.id}, titulo='{self.titulo}', status='{self.status}', visibilidade='{self.visibilidade}')>"
