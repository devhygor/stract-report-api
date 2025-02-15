# API de Relatórios - Processo Seletivo Stract

## Como rodar a aplicação

### 1. Clone o repositório e acesse a pasta:
```bash
    git clone https://github.com/devhygor/stract-report-api.git
    cd stract-report-api
```

### 2. Crie um ambiente virtual (opcional porem recomendado):

#### Linux/Mac:
Criar ambiente virtual:
```bash
    python3 -m venv venv
```
Ativar ambiente virtual:
```bash
    source venv/bin/activate
```
---
#### Windows:
Criar ambiente virtual:
```bash
    python3 -m venv venv
```
Ativar ambiente virtual:
* Se estiver usando o **PowerShell**:
```bash
    .\venv\Scripts\Activate
```
* Se estiver usando o **Prompt de Comando (CMD)**:
```bash
    venv\Scripts\activate
```
---
>OBS: Caso deseje desativar o ambiente virtual basta rodar o comando `deactivate` funciona para ambos os sistemas.:

### 3. Instale as dependências:
```bash
    pip install -r requirements.txt
```

### 4. Execute o servidor Flask:
```bash
    python3 app.py
```

### 5. Acesse os endpoints no navegador:
- http://localhost:5000/
- http://localhost:5000/facebook
- http://localhost:5000/facebook/resumo
- http://localhost:5000/geral
- http://localhost:5000/geral/resumo