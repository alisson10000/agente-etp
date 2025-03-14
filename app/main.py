from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.core.database import engine, Base
from app.modules.usuario.router_usuario import router as usuario_router
from app.modules.etp.router_etp import router as etp_router

# ================================
# Criação da instância do FastAPI
# ================================
app = FastAPI(
    title="Agente ETP API",
    description="API para gerenciamento de usuários e geração de ETP com integração via agentes inteligentes.",
    version="1.0.0"
)

# ================================
# Middleware CORS (liberar acesso externo)
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar as URLs permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================
# Criação automática das tabelas no banco de dados
# =====================================
Base.metadata.create_all(bind=engine)

# =====================================
# Inclusão das rotas dos módulos
# =====================================
app.include_router(usuario_router)  # ✅ Inclui o router corretamente sem prefixo repetido

app.include_router(etp_router)  # Pronto, vai adicionar as rotas de ETP

# =====================================
# Rota raiz (saúde do servidor)
# =====================================
@app.get("/")
def read_root():
    return {"message": "🚀 API Agente ETP rodando com sucesso!"}

# =====================================
# Rota temporária para geração de ETP (Exemplo de uso)
# =====================================
class ETPRequest(BaseModel):
    orgao: str
    objeto: str
    justificativa: str
    valor_estimado: str
    data: str

@app.post("/gerar-etp")
def gerar_etp(request: ETPRequest):
    """
    Endpoint temporário de geração de ETP (simulação).
    """
    return {
        "mensagem": "ETP gerado com sucesso!",
        "orgao": request.orgao,
        "objeto": request.objeto,
        "justificativa": request.justificativa,
        "valor_estimado": request.valor_estimado,
        "data": request.data,
        "link_documento": "http://exemplo.com/etp_gerado.docx"
    }
