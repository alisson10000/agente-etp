from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from app.core.database import Base  # Base herdada do SQLAlchemy declarative base
import enum

# ===============================
# ENUMS para refletir o banco de dados
# ===============================

class TipoUsuarioEnum(enum.Enum):
    admin = 'admin'
    comum = 'comum'
    gestor = 'gestor'


class StatusUsuarioEnum(enum.Enum):
    ativo = 'ativo'
    inativo = 'inativo'
    bloqueado = 'bloqueado'


# ===============================
# Model Usuário
# ===============================

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)  # Armazenar sempre como hash seguro

    # ENUMS refletindo exatamente como está no banco
    tipo = Column(Enum(TipoUsuarioEnum), default=TipoUsuarioEnum.comum, nullable=True)
    status = Column(Enum(StatusUsuarioEnum), default=StatusUsuarioEnum.ativo, nullable=True)

    data_criacao = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    ultimo_login = Column(TIMESTAMP, nullable=True)  # Pode ser null conforme o banco

    def __repr__(self):
        return (
            f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', "
            f"tipo='{self.tipo.value if self.tipo else None}', "
            f"status='{self.status.value if self.status else None}')>"
        )
