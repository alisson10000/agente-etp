from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.modules.usuario.schema_usuario import UsuarioResponse, UsuarioCreate, UsuarioUpdate
from app.modules.usuario.service_usuario import (
    criar_usuario,
    get_usuario_por_id,
    listar_usuarios,
    atualizar_usuario,
    deletar_usuario
)
from app.core.database import get_db

router = APIRouter(
    prefix="/usuarios",  # Definido o prefixo correto
    tags=["Usuários"],
    responses={404: {"description": "Não encontrado"}}
)

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioResponse], status_code=status.HTTP_200_OK)
def listar(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return listar_usuarios(db, skip=skip, limit=limit)

@router.get("/{usuario_id}", response_model=UsuarioResponse, status_code=status.HTTP_200_OK)
def obter(usuario_id: int, db: Session = Depends(get_db)):
    usuario = get_usuario_por_id(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioResponse, status_code=status.HTTP_200_OK)
def atualizar(usuario_id: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = atualizar_usuario(db, usuario_id, usuario_update)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(usuario_id: int, db: Session = Depends(get_db)):
    usuario = deletar_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return None  # No content
