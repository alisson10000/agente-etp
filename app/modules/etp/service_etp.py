from sqlalchemy.orm import Session
from app.modules.etp.model_etp import ETP
from app.modules.etp.schema_etp import ETPCreate, ETPUpdate


# Criar ETP
def criar_etp(db: Session, etp: ETPCreate):
    db_etp = ETP(**etp.dict())
    db.add(db_etp)
    db.commit()
    db.refresh(db_etp)
    return db_etp


# Listar ETPs
def listar_etps(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ETP).offset(skip).limit(limit).all()


# Obter ETP por ID
def get_etp_por_id(db: Session, etp_id: int):
    return db.query(ETP).filter(ETP.id == etp_id).first()


# Atualizar ETP
def atualizar_etp(db: Session, etp_id: int, etp_update: ETPUpdate):
    db_etp = get_etp_por_id(db, etp_id)
    if not db_etp:
        return None
    for key, value in etp_update.dict(exclude_unset=True).items():
        setattr(db_etp, key, value)
    db.commit()
    db.refresh(db_etp)
    return db_etp


# Deletar ETP
def deletar_etp(db: Session, etp_id: int):
    db_etp = get_etp_por_id(db, etp_id)
    if not db_etp:
        return None
    db.delete(db_etp)
    db.commit()
    return db_etp
