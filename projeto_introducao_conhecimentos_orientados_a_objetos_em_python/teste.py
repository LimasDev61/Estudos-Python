class Logavel:
    def log(self, mensagem):
        print(f"LOG: {mensagem}")

class Conexao:
    def conectar(self):
        print("Conectando ao banco de dados...")

# Herança Múltipla
class BancoDeDados(Logavel, Conexao):
    pass

db = BancoDeDados()
db.log("Iniciando sistema") # Vem de Logavel
db.conectar()               # Vem de Conexao