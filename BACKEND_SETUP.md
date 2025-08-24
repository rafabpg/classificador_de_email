# ⚙️ Setup Backend (FastAPI)

Este guia descreve como configurar e executar o **backend** do projeto, desenvolvido em **FastAPI**.

---

### 📋 Pré-requisitos

- Python
- Conta no Hugging Face

---

## 🧠 Passo a Passo de Configuração

- ``cd backend``

### 🪟 Windows Setup

1. 🔧 Criar ambiente virtual:  

`` python -m venv env_name ``

2. ▶️ Ative o ambiente:

`` env_name/Scripts/activate ``

3. 📦 Instalar dependências: 

`` pip install -r requirements.txt ``

4. 📄 Crie o arquivo `.env` na raiz do projeto.

5. ✍️ Adicione variáveis ​​ao `.env` conforme `.env_example`:

`` API_TOKEN = "api token do hugging face" ``

6. 🚀 Rode o servidor:
  
`` uvicorn app.main:app --reload ``

---

### 💻 Linux

1. 🔧 Criar ambiente virtual: 
  
`` python3 -m venv env_name ``

2. ▶️ Ative o ambiente:

`` source env_name/bin/activate ``

3. 📦 Instalar dependências:

`` pip install -r requirements.txt ``

4. 📄 Crie o arquivo `.env` na raiz do projeto.

5. ✍️ Adicione variáveis ​​ao `.env` conforme `.env_example`: 

`` API_TOKEN = "api token do hugging face" ``  

6. 🚀 Rode o servidor: 

`` uvicorn app.main:app --reload ``