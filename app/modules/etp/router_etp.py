from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.modules.etp.schema_etp import ETPResponse, ETPCreate, ETPUpdate
from app.modules.etp.service_etp import (
    criar_etp,
    get_etp_por_id,
    listar_etps,
    atualizar_etp,
    deletar_etp
)
from app.core.database import get_db  # Função para injeção de dependência do banco

router = APIRouter(
    prefix="/etps",
    tags=["ETPs"],
    responses={404: {"description": "Não encontrado"}}
)

# ======================================
# Rota para criar um novo ETP
# ======================================
@router.post("/", response_model=ETPResponse, status_code=status.HTTP_201_CREATED)
def criar(etp: ETPCreate, db: Session = Depends(get_db)):
    return criar_etp(db, etp)

# ======================================
# Rota para listar todos os ETPs
# ======================================
@router.get("/", response_model=List[ETPResponse], status_code=status.HTTP_200_OK)
def listar(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return listar_etps(db, skip=skip, limit=limit)

# ======================================
# Rota para obter um ETP por ID
# ======================================
@router.get("/{etp_id}", response_model=ETPResponse, status_code=status.HTTP_200_OK)
def obter(etp_id: int, db: Session = Depends(get_db)):
    etp = get_etp_por_id(db, etp_id)
    if etp is None:
        raise HTTPException(status_code=404, detail="ETP não encontrado")
    return etp

# ======================================
# Rota para atualizar dados do ETP
# ======================================
@router.put("/{etp_id}", response_model=ETPResponse, status_code=status.HTTP_200_OK)
def atualizar(etp_id: int, etp_update: ETPUpdate, db: Session = Depends(get_db)):
    etp = atualizar_etp(db, etp_id, etp_update)
    if etp is None:
        raise HTTPException(status_code=404, detail="ETP não encontrado")
    return etp

# ======================================
# Rota para deletar um ETP
# ======================================
@router.delete("/{etp_id}", status_code=status.HTTP_200_OK)  # Retornando 200 OK
def deletar(etp_id: int, db: Session = Depends(get_db)):
    etp = deletar_etp(db, etp_id)
    if etp is None:
        raise HTTPException(status_code=404, detail="ETP não encontrado")
    return {"message": "ETP deletado com sucesso!", "etp_id": etp_id}
