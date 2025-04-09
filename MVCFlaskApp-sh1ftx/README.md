# MVCFlaskApp

## 📌 Estrutura do Repositório
```php
FlaskCRUD/
├── app/                
│   ├── static/         # Arquivos CSS, JS, imagens
│   │   ├── css/
│   │   │   ├── style.css
│   │   ├── js/
│   │   │   ├── scripts.js
│   ├── templates/      # Arquivos HTML (views)
│   │   ├── base.html   # Template base
│   │   ├── index.html  # Página inicial
│   │   ├── users.html  # CRUD de usuários
│   │   ├── products.html # CRUD de produtos
│   ├── models.py       # Definição das classes do banco de dados (Model)
│   ├── routes.py       # Rotas e lógica da aplicação (Controller)
│   ├── forms.py        # Formulários Flask-WTF (opcional)
│   ├── __init__.py     # Inicialização do app Flask
│   ├── config.py       # Configurações do projeto
│   ├── database.db     # Banco de dados SQLite (ou script para outro DB)
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto (Flask, Flask-WTF, SQLite, etc.)
├── README.md           # Documentação geral do projeto
├── .gitignore          # Arquivos a serem ignorados pelo Git (ex: database.db)
└── LICENSE             # Licença do projeto (opcional)
```

## 📌 Descrição dos Arquivos
- 📁 **app/** → Diretório principal do aplicativo Flask  
- 📂 **static/** → Contém os arquivos de estilo e scripts JS  
- 📂 **templates/** → Guarda os arquivos HTML baseados no Flask Jinja  
- 📄 **models.py** → Define os modelos do banco de dados (Usuário, Produto, etc.)  
- 📄 **routes.py** → Define as rotas da aplicação (`@app.route('/')`, CRUD)  
- 📄 **forms.py** *(opcional)* → Gerencia formulários usando Flask-WTF  
- 📄 **config.py** → Contém as configurações do Flask e do banco  
- 📄 **database.db** → Arquivo SQLite ou pode ser substituído por um script SQL  
- 📄 **main.py** → Arquivo que inicia o servidor Flask (`flask run`)  
- 📄 **requirements.txt** → Lista de dependências para instalar com `pip install -r requirements.txt`  
- 📄 **README.md** → Explicação sobre como rodar o projeto  
- 📄 **.gitignore** → Evita versionar arquivos desnecessários (ex: banco de dados, venv)  
- 📄 **LICENSE** → Define a licença do projeto (MIT, GPL, etc.)  

## 📌 Comandos para Rodar o Projeto
```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/FlaskCRUD.git
cd FlaskCRUD

# 2. Criar um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python main.py
```

Atenciosamente!