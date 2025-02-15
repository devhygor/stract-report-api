# API de Relatórios - Processo Seletivo Stract
Essa aplicação consome dados de uma API externa e gera relatórios em formato CSV, conforme o processo seletivo da Stract.

---

## 🚀 Como rodar a aplicação

### 1. Clone o repositório e acesse a pasta:
```bash
git clone https://github.com/devhygor/stract-report-api.git
cd stract-report-api
```

### 2. Crie um ambiente virtual (opcional, mas recomendado):

#### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```bash
python3 -m venv venv
```
- Se estiver usando o **PowerShell**:
```bash
.\venv\Scripts\Activate
```
- Se estiver usando o **Prompt de Comando (CMD)**:
```bash
venv\Scripts\activate
```

---

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor Flask:
```bash
python3 app.py
```

---

## 🔗 Endpoints

### 🌐 Raiz
- **`GET /`**
  Retorna minhas informações (nome, email e LinkedIn).
  - Exemplo: [http://localhost:5000/](http://localhost:5000/)

---

### 📊 Relatórios por Plataforma
- **`GET /<platform>`**
  Gera um relatório detalhado de anúncios para a plataforma especificada.
  - Exemplo: [http://localhost:5000/facebook](http://localhost:5000/facebook)

- **`GET /<platform>/resumo`**
  Gera um resumo consolidado por conta na plataforma especificada, somando os valores das métricas numéricas.
  - Exemplo: [http://localhost:5000/facebook/resumo](http://localhost:5000/facebook/resumo)

---

### 📊 Relatórios Gerais
- **`GET /geral`**
  Retorna todos os anúncios de todas as plataformas.
  - Exemplo: [http://localhost:5000/geral](http://localhost:5000/geral)

- **`GET /geral/resumo`**
  Gera um resumo consolidado por plataforma, somando as métricas numéricas.
  - Exemplo: [http://localhost:5000/geral/resumo](http://localhost:5000/geral/resumo)

---

## 📚 Dependências
- **Python 3.8+** (recomenda-se usar a versão 3.8 ou superior)
- As seguintes dependências serão instaladas automaticamente ao rodar `pip install -r requirements.txt`:
  - Flask
  - Requests
  - Pytest (Para rodar os tests unitarios)
