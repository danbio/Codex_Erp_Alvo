# Prompt de Geração de Projeto ERP Completo

## 1. Instrução Principal

Desenvolva uma aplicação ERP completa em uma única execução, sem interrupções. Siga rigorosamente as diretrizes definidas no arquivo `AGENTS.md` como a autoridade máxima para padrões, convenções, arquitetura e regras de negócio.

## 2. Objetivo Central

Gerar um sistema ERP 100% funcional, utilizando a stack e as funcionalidades detalhadas em agents.md na raiz do projeto.

### 2.1. Stack Tecnológica

- **Linguagem:** Python 3.12+
- **Framework:** Django 5.2.8
- **Banco de Dados:** PostgreSQL (produção), SQLite (desenvolvimento)
- **Frontend:** Bootstrap 5.3.8

### 2.2. Entregáveis Esperados

- Projeto Django (`Alvo Gestão`) totalmente configurado.
- Todos os apps Django (`alunos`, `professores`, etc.) criados e funcionais.
- `models.py` completos, com campos, relacionamentos e docstrings.
- `forms.py` para todas as operações de CRUD.
- `views.py` utilizando Class-Based Views (CBVs) para CRUD completo.
- `urls.py` configuradas para cada app.
- Templates HTML para todas as views (listagem, criação, edição, exclusão).
- Sistema de autenticação de usuários completo (login, logout, reset de senha).
- Template `base.html` com layout responsivo, navbar, breadcrumbs e sistema de mensagens.
- Código com type hints e validado pelo linter `Ruff`.
- Migrações do banco de dados geradas e prontas para serem aplicadas.

## 3. Estrutura do Projeto
- Conforme agents.md
### 3.1. Nome do Projeto Django

- `erp_escola`

### 3.2. Aplicações (Apps)

- `alunos`
- `professores`
- `cursos`
- `turmas`
- `matriculas`
- `financeiro`
- `dashboard` (app para a página inicial com métricas)

### 3.3. Estrutura de Cada App

Cada app deve conter, no mínimo:
- `models.py`
- `forms.py`
- `views.py`
- `urls.py`
- `admin.py` (com os modelos registrados)
- `templates/<nome_do_app>/` (com os arquivos `.html`)

## 4. Modelos de Dados (models.py)

### 4.1. `alunos.Aluno`
- `nome`: `CharField`
- `cpf`: `CharField` (utilizar `localflavor` para validação)
- `data_nascimento`: `DateField`
- `email`: `EmailField`
- `telefone`: `CharField`
- `endereco`: `CharField` (rua, cidade, estado)
- `ativo`: `BooleanField` (default `True`)

### 4.2. `professores.Professor`
- `nome`: `CharField`
- `cpf`: `CharField`
- `especialidade`: `CharField`
- `telefone`: `CharField`
- `email`: `EmailField`

### 4.3. `cursos.Curso`
- `nome`: `CharField`
- `descricao`: `TextField`
- `carga_horaria`: `IntegerField`

### 4.4. `turmas.Turma`
- `curso`: `ForeignKey` para `cursos.Curso`
- `professor`: `ForeignKey` para `professores.Professor`
- `data_inicio`: `DateField`
- `data_fim`: `DateField`
- `horario`: `CharField` (ex: "Ter/Qui — 19h às 22h")
- `vagas`: `PositiveIntegerField`

### 4.5. `matriculas.Matricula`
- `aluno`: `ForeignKey` para `alunos.Aluno`
- `turma`: `ForeignKey` para `turmas.Turma`
- `data_matricula`: `DateField` (auto_now_add)
- `status`: `CharField` com `choices` (`ativo`, `trancado`, `concluído`)

### 4.6. `financeiro.Pagamento`
- `matricula`: `ForeignKey` para `matriculas.Matricula`
- `valor`: `DecimalField`
- `data_vencimento`: `DateField`
- `data_pagamento`: `DateField` (pode ser nulo)
- `status`: `CharField` com `choices` (`em aberto`, `pago`, `atrasado`)

## 5. Frontend e Templates

- Utilizar **Bootstrap 5.3** em todos os templates.
- Criar um `base.html` que será estendido por todos os outros.
- A `navbar` no `base.html` deve conter links para as listagens de todos os módulos.
- Implementar um sistema de `breadcrumb` dinâmico.
- Criar templates para as 4 operações do CRUD (Create, Read, Update, Delete) para cada modelo.
- Estilizar todos os formulários com as classes do Bootstrap.

## 6. Autenticação e Usuários

- Implementar o sistema `django.contrib.auth` completo.
- Criar as rotas e templates para `login`, `logout` e `password_reset`.
- A rota de login principal deve ser `/accounts/login/`.
- Proteger as views principais com o decorador `@login_required` ou `LoginRequiredMixin`.
- A `navbar` deve exibir o nome do usuário logado e um link para logout.

## 7. Rotas (URLs)

Configurar as seguintes rotas principais, cada uma com suas sub-rotas de CRUD:
- `/alunos/`
- `/professores/`
- `/cursos/`
- `/turmas/`
- `/matriculas/`
- `/financeiro/`
- `/dashboard/`

## 8. Configurações do Projeto

- Configurar o `settings.py` para usar **PostgreSQL** em produção e **SQLite** em desenvolvimento, lendo a `DATABASE_URL` do ambiente.
- Configurar o `staticfiles`.
- Criar um arquivo `.env.example` com as seguintes variáveis:
  - `SECRET_KEY`
  - `DEBUG`
  - `DATABASE_URL`

## 9. Dashboard

- O app `dashboard` deve ter a view principal do projeto (`/`).
- A página deve exibir cards com as seguintes métricas (contagens simples):
  - Total de alunos
  - Total de professores
  - Total de cursos
  - Total de turmas ativas
  - Total de matrículas
  - Total de pagamentos em aberto

## 10. Testes

Criar testes unitários simples para validar a criação dos seguintes modelos:
- `Aluno`
- `Curso`
- `Turma`

## 11. Padrões de Código

- Todo o código (nomes de variáveis, funções, comentários, docstrings) deve ser em **Português do Brasil**.
- Utilizar **type hints** em todas as assinaturas de funções e métodos.
- Manter o código limpo, organizado e seguir as convenções do `AGENTS.md`.
- Utilizar **Class-Based Views (CBVs)** para todas as views de CRUD.

## 12. Instruções de Execução

- Execute todas as tarefas de uma só vez, sem pedir confirmações intermediárias.
- Crie, modifique e escreva os arquivos necessários para completar o projeto.
- Ao finalizar, garanta que o projeto está coeso, funcional e que nenhum requisito foi omitido.
- **Pare somente quando o ERP estiver completamente gerado e funcional.**