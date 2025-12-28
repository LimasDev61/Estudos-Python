# ==============================================================================
# PIP - PYTHON PACKAGE INSTALLER (DOCUMENTAÇÃO TÉCNICA - MODO SEGURO)
# ==============================================================================
# O PIP é o gerenciador de pacotes padrão. A forma mais segura de executá-lo é
# invocando o módulo através do interpretador Python (python -m pip).
# Isso evita conflitos de PATH e garante a instalação no ambiente correto.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. GERENCIAMENTO DE PACOTES (INSTALAÇÃO E REMOÇÃO)
# ------------------------------------------------------------------------------

# Instalar a versão mais recente (Estável):
# python -m pip install nome_do_pacote

# Instalar versão específica ("Pinning" - Essencial para evitar quebras):
# python -m pip install requests==2.25.1

# Instalar com operadores lógicos (Mínimo ou Máximo):
# python -m pip install "requests>=2.0.0"
# python -m pip install "requests<=3.0.0"

# Atualizar um pacote já instalado:
# python -m pip install --upgrade nome_do_pacote

# Desinstalar um pacote:
# python -m pip uninstall nome_do_pacote
# Dica: Use a flag -y para pular a confirmação (útil em scripts):
# python -m pip uninstall -y nome_do_pacote

# ------------------------------------------------------------------------------
# 2. INSPEÇÃO E ANÁLISE (O QUE TENHO INSTALADO?)
# ------------------------------------------------------------------------------

# Listar todos os pacotes do ambiente atual:
# python -m pip list

# Verificar pacotes desatualizados (Manutenção):
# python -m pip list --outdated

# Ver detalhes técnicos de um pacote (Versão, Local, Dependências):
# python -m pip show nome_do_pacote
# NOTA: Para ver dependências, procure as linhas "Requires" e "Required-by".

# Verificar histórico de versões disponíveis (Sem instalar):
# python -m pip index versions nome_do_pacote

# BUSCA DE PACOTES (Via Terminal):
# Como o 'pip search' nativo foi descontinuado, se tiver o plugin instalado:
# python -m pip_search nome_do_pacote

# ------------------------------------------------------------------------------
# 3. CONGELAMENTO DE AMBIENTE (REQUISITOS)
# ------------------------------------------------------------------------------

# Gerar a lista de dependências para salvar o projeto:
# python -m pip freeze > requirements.txt

# Instalar tudo de uma vez a partir de um arquivo:
# python -m pip install -r requirements.txt

# ------------------------------------------------------------------------------
# 4. SEGURANÇA E AMBIENTE (BOAS PRÁTICAS)
# ------------------------------------------------------------------------------

# CHECKLIST ANTES DE INSTALAR:
# 1. Venv Ativa?
#    Verifique se o python que está rodando é o da venv.
#    Comando de verificação (Windows): 'Get-Command python'
#    Comando de verificação (Linux/Mac): 'which python'

# 2. Atualização do Próprio PIP (Crucial usar o -m aqui):
#    Comando Obrigatório para Update:
#    python -m pip install --upgrade pip

# Verificar versão do PIP sendo executado pelo Python atual:
# python -m pip --version

# ------------------------------------------------------------------------------
# 5. DEEP DIVE TÉCNICO: POR QUE USAR 'python -m'? (O PULO DO GATO)
# ------------------------------------------------------------------------------
# O Problema do Windows ("Access Denied"):
# No Windows, arquivos executáveis (.exe) são bloqueados enquanto estão rodando.
# Se você rodar apenas 'pip install --upgrade pip', você está usando o
# 'pip.exe' para tentar deletar e substituir a si mesmo. Isso falha.

# A Solução (python -m pip):
# Ao usar este comando, quem roda o processo é o 'python.exe'.
# O código do pip é carregado na memória como um módulo.
# Resultado: O arquivo 'pip.exe' no disco fica livre para ser atualizado,
# deletado ou substituído sem gerar conflitos de permissão.

# Dica de Ouro:
# Adote 'python -m pip' como padrão absoluto em seus scripts e automações.