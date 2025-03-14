from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ==========================
# CONEXÃO COM O BANCO DE DADOS
# ==========================

# String de conexão com MariaDB
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/agenteetp"

# Engine de conexão
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True  # Mantém a conexão ativa automaticamente
)

# Gerenciador de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# ================================
# FUNÇÃO PARA INJETAR SESSÃO NAS ROTAS
# ================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
