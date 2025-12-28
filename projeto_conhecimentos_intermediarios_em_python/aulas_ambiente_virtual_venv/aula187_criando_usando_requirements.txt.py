# ==============================================================================
# REQUIREMENTS.TXT - GESTÃO DE DEPENDÊNCIAS
# ==============================================================================
# O arquivo requirements.txt é o "Snapshot" (retrato) do seu ambiente.
# Ele garante a REPRODUTIBILIDADE do projeto, assegurando que o código rode
# exatamente igual na máquina de qualquer desenvolvedor ou servidor.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CRIAÇÃO (SNAPSHOT)
# ------------------------------------------------------------------------------
# Após instalar suas bibliotecas e garantir que o código funciona, você deve
# "congelar" o estado atual das versões.

# Comando:
# python -m pip freeze > requirements.txt

# Análise do Comando:
# A. python -m pip freeze:
#    Lista todos os pacotes instalados no ambiente virtual ativo,
#    junto com suas dependências transitivas (ex: pandas instala numpy).
#
# B. > requirements.txt:
#    Operador de redirecionamento de saída (Output Redirection).
#    Pega o texto que apareceria no terminal e escreve dentro do arquivo.
#    Atenção: Se o arquivo já existir, ele será SOBRESCRITO completamente.

# Exemplo de Saída no arquivo:
# requests==2.25.1
# pandas==1.2.4
# numpy==1.19.5  <-- Dependência trazida automaticamente pelo pandas

# ------------------------------------------------------------------------------
# 2. INSTALAÇÃO (RESTORE)
# ------------------------------------------------------------------------------
# Usado quando você clona um repositório ou faz deploy no servidor.

# Comando:
# python -m pip install -r requirements.txt

# Análise do Comando:
# A. -r (Read/Requirement):
#    Instrui o pip a ler um arquivo de texto em vez de buscar um pacote online.

# ------------------------------------------------------------------------------
# 3. BOAS PRÁTICAS DE ENGENHARIA
# ------------------------------------------------------------------------------

# A. Versionamento: Exato (==) vs Flexível (>=)
#    - Aplicações Finais (Apps, APIs): Use SEMPRE '=='.
#      Isso "trava" a versão (Pinning). Garante que nenhuma atualização automática
#      quebre seu sistema em produção.
#    - Bibliotecas (Libs): Às vezes usam '>=', mas exige cuidado redobrado.

# B. Higiene do Ambiente (Clean Up)
#    Se você desinstalar uma biblioteca que não usa mais, o requirements.txt
#    não atualiza sozinho. Você deve fazer o processo manual:
#
#    1. python -m pip uninstall pacote_inutil
#    2. python -m pip freeze > requirements.txt (Gera o arquivo limpo novamente)

# C. Onde Salvar?
#    Raiz do projeto (root), no mesmo nível do .gitignore e main.py.

# D. O Perigo dos Comentários (#)
#    Você PODE comentar o arquivo manualmente para documentar:
#       django==4.0 # Framework Web
#
#    CUIDADO: Ao rodar 'pip freeze > requirements.txt' novamente,
#    o Python vai APAGAR todos os seus comentários manuais e reescrever o arquivo
#    do zero. Se quiser manter comentários, evite usar o redirecionador '>' direto.

# E. Usar python -m (Regra de Ouro)
#    É a melhor prática para garantir que o pip use o ambiente virtual correto,
#    evitando conflitos de PATH e permissões no Windows.

# ------------------------------------------------------------------------------
# 4. WORKFLOW COMPLETO (GIT & EQUIPE)
# ------------------------------------------------------------------------------

# PASSO 1: Configuração Inicial
# a. Criar Venv:     python -m venv .venv
# b. Ativar Venv:    .\.venv\Scripts\activate
# c. Instalar:       python -m pip install requests pandas

# PASSO 2: Versionamento
# a. Congelar:       python -m pip freeze > requirements.txt
# b. Git Ignore:     Garanta que a pasta '.venv/' está no .gitignore.
#                    (Ela é pesada e inútil no GitHub).
# c. Commit:         Suba apenas o código fonte e o requirements.txt.

# PASSO 3: Retomada (Outro Dev ou Outro PC)
# a. Clone:          git clone ...
# b. Recriar Venv:   python -m venv .venv
# c. Ativar:         .\.venv\Scripts\activate
# d. Restaurar:      python -m pip install -r requirements.txt

# ------------------------------------------------------------------------------
# 5. REFERÊNCIA: ARQUIVO .GITIGNORE RECOMENDADO (PADRÃO)
# ------------------------------------------------------------------------------
# Este conteúdo deve ficar num arquivo chamado apenas ".gitignore" (sem extensão).

# --- Sistema Operacional (Windows/Mac) ---
# Thumbs.db
# Desktop.ini
# .DS_Store

# --- IDEs e Editores (VS Code, etc) ---
# .vscode/
# .idea/
# *.swp

# --- Python & Ambientes Virtuais ---
# __pycache__/
# *.pyc
# venv/
# .venv/
# env/

# --- Segurança (CRÍTICO) ---
# Nunca suba chaves de API ou senhas
# .env
# config.ini

# --- Arquivos de Log e Bancos Locais ---
# *.log
# *.sqlite3

# Regra de Ouro: Se o arquivo é gerado automaticamente pelo computador (compilados,
# pastas de dependências) ou contém senhas, ele deve estar no .gitignore.

# ==============================================================================
# FIM DA DOCUMENTAÇÃO
# ==============================================================================