from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Agente ETP",
    description="API para geração automatizada de ETP (Estudo Técnico Preliminar).",
    version="1.0.0"
)

# Permite acesso via navegador/cliente externo (ex.: Postman)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo do payload que será enviado via Postman
class ETPRequest(BaseModel):
    orgao: str
    objeto: str
    justificativa: str
    valor_estimado: str
    data: str

@app.post("/gerar-etp")
def gerar_etp(request: ETPRequest):
    # Simula uma resposta estática por enquanto
    return {
        "mensagem": "ETP gerado com sucesso!",
        "orgao": request.orgao,
        "objeto": request.objeto,
        "justificativa": request.justificativa,
        "valor_estimado": request.valor_estimado,
        "data": request.data,
        "link_documento": "http://exemplo.com/etp_gerado.docx"  # Simulado por enquanto
    }
