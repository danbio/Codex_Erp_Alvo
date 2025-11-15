# AGENTS.md

## 1. Visão geral do projeto

Este repositório contém um sistema web de gestão (ERP) desenvolvido em **Python + Django**, com foco em:
- Cadastro e gestão alunos, professores, turmas, matriculas, calendario de aulas, etc.).
- Módulos administrativos (financeiro, propostas, turmas, contratos etc.).
- Interface web limpa e responsiva com **Bootstrap 5.3**.

O objetivo principal dos agentes de IA é:
- **Acelerar o desenvolvimento**, gerando código coerente com a arquitetura atual.
- **Manter a organização do projeto**, seguindo as convenções definidas abaixo.
- **Evitar “gambiarras”** e soluções que fujam das boas práticas do Django.

---

## 2. Stack, versões e dependências principais

- Linguagem: **Python 3.12+**
- Framework web: **Django 5.2.3 ou superior**
- Banco de dados: **PostgreSQL** (em produção) / SQLite (em desenvolvimento, se configurado)
- Frontend: **HTML5 + Bootstrap 5.3**, JavaScript mínimo (sem frameworks SPA por enquanto)
- Ferramentas:
  - `pip` para dependências
  - `ruff` para lint
  - `djlint` para templates html (django)

## 3. Estrutura inicial do projeto
```
Codex_Erp_Alvo/
├── manage.py
├── requirements.txt
├── .env                          # Variáveis de ambiente (não commitado)
├── .gitignore
├── ruff.toml                     # Configuração do linter
├── .djlintrc                     # Configuração do djlint
│
├── config/                       # Configurações principais do Django
│   ├── __init__.py
│   ├── settings.py               # Settings principal
│   ├── urls.py                   # URLconf raiz
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                         # Todos os apps Django ficam aqui
│   ├── setup/                    # App central (models comuns, utils, etc.)
│   ├── alunos/                   # Gestão de alunos
│   ├── professores/              # Gestão de professores
│   ├── turmas/                   # Gestão de turmas
│   ├── matriculas/               # Gestão de matrículas
│   ├── calendario/               # Calendário de aulas
│   ├── financeiro/               # Módulo financeiro
│   ├── propostas/                # Propostas comerciais
│   ├── contratos/                # Gestão de contratos
│   ├── configuracoes/            # Gestão de configurações do projeto
│   └── accounts/                 # Autenticação e usuários
│
├── static/                       # Arquivos estáticos globais
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/                    # Templates globais
│   ├── base.html                 # Template base com Bootstrap
│   ├── components/               # Componentes reutilizáveis
│   └── errors/                   # Páginas de erro (404, 500, etc.)
│
└── media/                        # Uploads de usuários (não commitado)
```
## 4. Diretrizes para códigos
- Usar o mcp Context7 para acessar documentação.
- Use sempre o principio "DRY" do django.
- Use Class Based Views.
- Maximize o reuso de códigos e arquivos.
- Isole os módulos, mantendo-os "autosuficientes".
- Siga o PEP8.
- Opte sempre por usar função nativa do Django.
- Não adicionar dependencias ao projeto a menos que estritamente necessárias, e após aprovação.
- Use váriaveis e funções em portugues do brasil.
- Caso haja entendimento ambiguo de alguma solicitação, optar sempre por seguir a documentação, ou perguntar explicitamente.
- Adicionar docstrings e documentar didaticamente todo o código.
- Não use javascript a menos que estritamente necessário, se usar documente didaticamente.

## 5. Templates e Frontend
- Use Bootstrap 5.3.8 como framework de frontend
- Não use css/js inline, crie style.css e jspersonalizado.js em static/, e agrupe todas as novas classes css  e funções js nestes arquivos 
- Prefira as classes padrão do framework ao invés de criar nova classe
- Use o padrão "mobile first"

## 6. Atualização e evolução
- Este é um documento vivo, sempre que o fluxo de trabalho, a arquitetura e ou estilo mudarem, atualize acrescentando as linha necessárias a este arquivo
- Não despreze ou apague as diretrizes deste arquivo
- Documente aqui as features de cada módulo

## 7. Usuários

## 8. Alunos

## 9. Cursos
- Turmas
- Professores
- Caledário de aulas
- etc
## 10. Matriculas

## 11. Financeiro

## 12. Configurações
- Dados da empresa
- Logotipo
- Etc.
