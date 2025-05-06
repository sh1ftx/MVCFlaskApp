```
   _________   _____________ ___________.__                 __      _____                 
  /     \   \ /   /\_   ___ \\_   _____/|  | _____    _____|  | __ /  _  \ ______ ______  
 /  \ /  \   Y   / /    \  \/ |    __)  |  | \__  \  /  ___/  |/ //  /_\  \\____ \\____ \ 
/    Y    \     /  \     \____|     \   |  |__/ __ \_\___ \|    </    |    \  |_> >  |_> >
\____|__  /\___/    \______  /\___  /   |____(____  /____  >__|_ \____|__  /   __/|   __/ 
        \/                 \/     \/              \/     \/     \/       \/|__|   |__|    
```

## Índice

1. [Introdução](#introdução)
2. [Objetivos do Projeto](#objetivos-do-projeto)
3. [Arquitetura do Projeto](#arquitetura-do-projeto)
   1. [Modelo MVC](#modelo-mvc)
4. [Estrutura de Diretórios](#estrutura-de-diretórios)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)
6. [Funcionalidades Implementadas](#funcionalidades-implementadas)
7. [Como Executar o Projeto](#como-executar-o-projeto)
8. [Participantes do Projeto](#participantes-do-projeto)
9. [Considerações Finais](#considerações-finais)

## Introdução

O **MVCFlaskApp** é uma aplicação web desenvolvida utilizando o framework Flask, seguindo a arquitetura **MVC** (Model-View-Controller). O objetivo deste projeto é demonstrar a implementação de uma aplicação web funcional com as operações CRUD (Create, Read, Update, Delete), que permite gerenciar usuários e produtos. Além disso, o projeto utiliza boas práticas de organização de código, com separação clara entre as camadas da aplicação.

## Objetivos do Projeto

O objetivo principal deste projeto é criar uma aplicação web simples para gerenciar usuários e produtos, implementando as operações CRUD essenciais. O sistema foi projetado para ser modular e fácil de entender, de modo que sirva como exemplo didático de aplicação de conceitos fundamentais do Flask e da arquitetura MVC. O projeto também permite a exploração do uso de banco de dados SQLite integrado ao Flask, além de ser responsivo, com uma interface de fácil utilização.

## Arquitetura do Projeto

### Modelo MVC

A arquitetura do projeto segue o padrão **MVC (Model-View-Controller)**, onde:

- **Model**: Representa a camada responsável pela manipulação de dados e interações com o banco de dados. No projeto, esta camada é representada pela classe `models.py`.
  
- **View**: A camada de visualização (View) é responsável pela interface com o usuário. No projeto, são utilizadas as **views** em HTML com o motor de templates **Jinja2**, localizadas na pasta `templates/`.

- **Controller**: A camada de controle é responsável pela lógica de controle da aplicação. As rotas, que são responsáveis por processar as requisições HTTP, estão localizadas no arquivo `controllers.py`. A lógica de renderização das páginas também está centralizada no arquivo `views.py`.

A separação clara entre essas camadas proporciona maior organização, facilitando a manutenção e escalabilidade da aplicação.

## Estrutura de Diretórios

A estrutura de diretórios do projeto é organizada da seguinte maneira:

```

MVCFLASKAPP/
├── App/
│   ├── **pycache**/                # Cache de compilação Python (automático)
│   ├── static/                     # Arquivos estáticos
│   │   ├── css/                    # Estilos CSS separados por página
│   │   │   ├── page\_cadastro.css
│   │   │   ├── page\_edit.css
│   │   │   ├── page\_list.css
│   │   │   └── style.css
│   │   ├── js/                     # Scripts JS separados por página
│   │   │   ├── edit\_product.js
│   │   │   ├── edit\_user.js
│   │   │   ├── register\_product.js
│   │   │   └── user\_register.js
│   ├── templates/                 # Views (HTML com Jinja2)
│   │   ├── edit\_product.html
│   │   ├── edit\_user.html
│   │   ├── index.html
│   │   ├── product\_list.html
│   │   ├── register\_product.html
│   │   ├── user\_list.html
│   │   └── user\_register.html
│   ├── **init**.py                # Inicialização do pacote Flask
│   ├── controllers.py             # Controladores (rotas e lógica intermediária)
│   ├── crud.py                    # Operações CRUD (Create, Read, Update, Delete)
│   ├── models.py                  # Definições de modelos (tabelas/banco)
│   └── views.py                   # Lógica de renderização e retorno de templates
├── database\_teste\_mvc.db          # Banco de dados SQLite
├── main.py                        # Arquivo principal para rodar a app
├── requirements.txt               # Dependências do projeto
├── README.md                      # Documentação (em construção)
├── LICENSE                        # Licença do projeto
└── .gitignore                     # Ignora arquivos desnecessários no Git

````

### Detalhes dos Diretórios

- **App/**: Contém todos os arquivos da aplicação.
- **App/static/**: Contém os arquivos estáticos, como arquivos CSS e JavaScript, organizados por tipo e página.
- **App/templates/**: Contém os templates HTML usados pela aplicação, com a utilização do motor de templates Jinja2.
- **App/controllers.py**: Define as rotas e a lógica de controle da aplicação.
- **App/crud.py**: Contém funções para as operações CRUD de usuários e produtos.
- **App/models.py**: Define os modelos do banco de dados, com as tabelas necessárias.
- **App/views.py**: Define a lógica de renderização e exibição das views.

## Tecnologias Utilizadas

- **Python**: Principal linguagem de programação.
- **Flask**: Framework web para desenvolvimento de aplicações em Python.
- **Jinja2**: Motor de templates utilizado para gerar o HTML dinâmico.
- **SQLite**: Banco de dados leve, integrado ao Flask.
- **CSS**: Para estilizar a interface web.
- **JavaScript**: Para manipulação dinâmica da interface do usuário.

## Funcionalidades Implementadas

- **Cadastro de Usuários e Produtos**: Permite registrar novos usuários e produtos no sistema.
- **Listagem de Usuários e Produtos**: Exibe uma lista de usuários e produtos cadastrados.
- **Edição de Usuários e Produtos**: Permite editar os dados dos usuários e produtos.
- **Exclusão de Usuários e Produtos**: Permite excluir usuários e produtos do sistema.
- **Banco de Dados**: Utiliza SQLite para armazenar dados de usuários e produtos.

## Como Executar o Projeto

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/sh1ftx/MVCFlaskApp.git
   cd MVCFlaskApp ```

2. **Instale as Dependências**:

   Utilize o `pip` para instalar as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a Aplicação**:

   Inicie o servidor Flask:

   ```bash
   python main.py
   ```

4. **Acesse a Aplicação**:

   Abra o navegador e acesse o endereço local:

   ```
   http://127.0.0.1:5000
   ```

## Participantes do Projeto

* [Gleison Oliveira](https://github.com/gleiSUN)
* [Kayky Rodrigues](https://github.com/xFrostzss)
* [Fernando Sena](https://github.com/FernandosenaDev)
* [Vinycius Huellyson](https://github.com/VINYCIU51)

## Considerações Finais

O **MVCFlaskApp** foi desenvolvido para demonstrar como aplicar a arquitetura MVC em uma aplicação web simples, utilizando Flask e SQLite. Ele serve como base para aplicações mais complexas, podendo ser estendido para incluir novas funcionalidades como autenticação de usuários, validação de formulários e integração com outros bancos de dados.

A separação clara entre as camadas da aplicação torna o código mais organizado e facilita a manutenção. O uso de Flask, Jinja2 e SQLite proporciona uma base sólida e fácil de entender para desenvolvedores iniciantes em Python.
