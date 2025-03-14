from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.modules.usuario.model_usuario import Usuario
from app.modules.usuario.schema_usuario import UsuarioCreate, UsuarioUpdate

# Configurando o contexto de criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# =================================
# Função para criptografar a senha
# =================================
def gerar_hash_senha(senha: str):
    return pwd_context.hash(senha)


# ============================
# Serviço para criar um usuário
# ============================
def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=gerar_hash_senha(usuario.senha),
        tipo=usuario.tipo,
        status=usuario.status
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# ================================
# Serviço para obter usuário por ID
# ================================
def get_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


# =================================
# Serviço para listar todos usuários
# =================================
def listar_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()


# ===================================
# Serviço para atualizar dados do usuário
# ===================================
def atualizar_usuario(db: Session, usuario_id: int, usuario_update: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    # Atualizando apenas campos informados
    for field, value in usuario_update.dict(exclude_unset=True).items():
        if field == "senha" and value:
            setattr(db_usuario, "senha_hash", gerar_hash_senha(value))
        else:
            setattr(db_usuario, field, value)

    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# ============================
# Serviço para deletar usuário
# ============================
def deletar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario
