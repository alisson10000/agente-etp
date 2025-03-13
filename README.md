🧠 Agente ETP - Gerador Inteligente de Estudo Técnico Preliminar (ETP)

✨ Descrição

O Agente ETP é um agente inteligente desenvolvido em FastAPI com o objetivo de automatizar a criação de Estudos Técnicos Preliminares (ETP) de forma rápida, inteligente e personalizada. Voltado para o setor público (como Câmaras Municipais), o agente é capaz de analisar dados e gerar textos completos para os principais itens exigidos em um ETP, seguindo a Lei 14.133/2021 (Nova Lei de Licitações).

🚀 Tecnologias Utilizadas
Python 3.11+
FastAPI (Framework principal)
Uvicorn (Servidor ASGI)
Pydantic (Validação de dados)
OpenAI API ou Modelos LLM locais (futuramente integrado)
Postman (Para testes de API - fase inicial)
⚙️ Instalação e Execução
1. Clone o Repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/agente-etp.git
cd agente-etp
2. Crie e Ative o Ambiente Virtual
bash
Copiar
Editar
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
3. Instale as Dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute o Servidor FastAPI
bash
Copiar
Editar
uvicorn main:app --reload
O servidor estará disponível em: http://127.0.0.1:8000

📖 Documentação Interativa
Após rodar o servidor, acesse a documentação automática gerada pelo FastAPI:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
✅ Funcionalidades Previstas
 📑 Geração automática de Estudos Técnicos Preliminares (ETP).
 🧠 Integração com modelo de IA para elaboração dos textos (OpenAI ou Llama).
 ⚙️ Endpoints para cada seção do ETP:
 Objetivo da Contratação.
 Definição dos Requisitos da Solução.
 Análise de Riscos.
 Estimativas de Custo.
 💾 Integração com banco de dados para armazenar ETPs gerados.
 🔐 Controle de acesso e segurança (JWT/Token API).
📂 Estrutura do Projeto
bash
Copiar
Editar
agente-etp/
│
├── main.py                # Arquivo principal com rotas FastAPI
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação do projeto
├── services/              # (A ser criado) Lógica de geração do ETP
└── models/                # (A ser criado) Modelos Pydantic para entrada/saída
🚧 Em Desenvolvimento
Este projeto está em fase inicial. Em breve, novas funcionalidades serão implementadas, incluindo:

Integração com modelo de IA.
Geração de PDFs automáticos.
Frontend com painel para usuários gerenciarem ETPs.
💡 Como Contribuir
Faça um Fork do repositório.
Crie uma branch: git checkout -b minha-feature
Commit suas alterações: git commit -m 'Minha nova feature'
Faça o Push da sua branch: git push origin minha-feature
Abra um Pull Request.
📞 Contato
Caso tenha dúvidas, sugestões ou queira contribuir:

Nome: Alisson Lima De Souza
Email: alisson.lima.souza@gmail.com
