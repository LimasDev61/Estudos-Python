# ==============================================================================
# VENV - AMBIENTES VIRTUAIS (DOCUMENTAÇÃO TÉCNICA)
# ==============================================================================
# O Virtual Environment (venv) é uma ferramenta para criar ambientes isolados.
# Isso garante que as dependências de um projeto não interfiram em outro
# (ex: Projeto A usa Django 3, Projeto B usa Django 4).
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. PADRÕES DE PROJETO (ONDE SALVAR?)
# ------------------------------------------------------------------------------
# Localização: Sempre na RAIZ do projeto, ao lado do 'main.py'.
# Nomenclatura Padrão: Recomenda-se usar '.venv' (com ponto).
# Motivo: O ponto oculta a pasta em sistemas Unix e a maioria das IDEs
# (VS Code) já reconhece esse nome automaticamente como ambiente virtual.

# ------------------------------------------------------------------------------
# 2. CICLO DE VIDA BÁSICO (COMANDOS)
# ------------------------------------------------------------------------------

# Criar o ambiente (Modo Seguro):
# python -m venv .venv

# Ativar o ambiente (Windows):
# .\.venv\Scripts\activate
# (O terminal deve mostrar '(.venv)' no início da linha após isso)

# Desativar (Voltar para o sistema global):
# deactivate

# ------------------------------------------------------------------------------
# 3. WORKFLOW COMPLETO DE ENGENHARIA (GIT & COLABORAÇÃO)
# ------------------------------------------------------------------------------
# Este é o ciclo profissional para compartilhar código sem quebrar ambientes.

# PASSO A (Criador do Projeto):
# 1. Criar Venv:    python -m venv .venv
# 2. Ativar Venv:   .\.venv\Scripts\activate
# 3. Instalar Libs: python -m pip install pandas requests
# 4. Congelar:      python -m pip freeze > requirements.txt
# 5. Git Ignore:    GARANTA que a pasta '.venv/' está no arquivo '.gitignore'.
#                   (Nunca suba a pasta venv para o GitHub! Ela é pesada e inútil lá).
# 6. Commit/Push:   Envie apenas o código fonte e o 'requirements.txt'.

# PASSO B (Colega/Clonagem):
# 1. Clonar repo:   git clone url_do_repo
# 2. Criar Venv:    python -m venv .venv (Cria o isolamento local dele)
# 3. Ativar Venv:   .\.venv\Scripts\activate
# 4. Restaurar:     python -m pip install -r requirements.txt (Baixa as versões exatas)

# ------------------------------------------------------------------------------
# 4. TÉCNICA AVANÇADA: EXECUÇÃO DIRETA (SEM 'ACTIVATE')
# ------------------------------------------------------------------------------
# É possível rodar scripts na venv sem modificar o PATH (sem ativar).
# Muito utilizado em servidores de Automação (CI/CD), Agendador de Tarefas e Cron.

# Como funciona:
# O executável 'python.exe' dentro da pasta Scripts já "sabe" onde ele mora.
# Ao chamá-lo diretamente, ele usa as bibliotecas daquela pasta automaticamente.

# Comando (PowerShell):
# .\.venv\Scripts\python.exe main.py

# Alternar entre ambientes rapidamente (Exemplo):
# .\venv_projetoA\Scripts\python.exe script_A.py
# .\venv_projetoB\Scripts\python.exe script_B.py

# Verificação Técnica (Dentro do código Python):
# import sys
# print(sys.executable)
# (Isso mostrará o caminho completo do interpretador que está rodando o script)

# ------------------------------------------------------------------------------
# 5. INTEGRAÇÃO COM VS CODE (GUI)
# ------------------------------------------------------------------------------
# O VS Code pode gerenciar isso visualmente para você.

# Método 1 (Barra de Status):
# Clique na versão do Python no canto inferior direito (ou esquerdo) da janela.

# Método 2 (Command Palette):
# 1. Pressione: Ctrl + Shift + P
# 2. Digite: "Python: Select Interpreter"
# 3. Escolha o ambiente que tem o caminho '.\.venv\Scripts\python.exe'

# Obs: Ao selecionar aqui, o VS Code ativará o terminal automaticamente
# quando você abrir uma nova janela.