# Teoria: HERANÇA, Generalização e Especialização 

A **Herança** é o segundo pilar da Programação Orientada a Objetos. Na Engenharia de Software, ela é a ferramente nos permite aplicar os conceitos de **Geralização** e **Especialização** para criar a hierarquias de código eficientes e evitar a repetição desnecessária(princípio DRY - Don't Repeat Yourself). 

---
## 1. Generalização vs. Especialização

Estes termos descrevem a difereção em que você está olhando para a hierarquia de classes: 

- <span style="color:gray">``Generalização(Caminho para cima):``</span> É o processo de encontrar características comuns em várias classes e agrupá-las em uma **Superclasse**(ou Classe Pai).

    - **Exemplo:** iPhone, Galaxy e Pixel são todos *Smartphones*.

- <span style="color:gray">``Especialização(Caminho para baixo):``</span> É o processo de pegar uma classe genérica e criar **Subclasses**(ou Classes Filhas) que possuam comportamentos específicos.

    - **Exemplo:** A partir da classe genérica *Smartphone*, podemos criar especializações como o *iPhone* (especializado em ecossistema iOS), o *SmartphoneDobravel* (especializado em hardware flexível) e o *Galaxy* pode ser um *SmartphoneProdutividade* (especializado em multitarefa e uso de caneta Stylus).

---
## 2. A Hierarquia "É um"(Is-a)

Diferente da *Agregação/Composição*("Tem um"), a Herança define que uma classe **É UMA** versão da outra.

- ``Superclasse(Pai):`` Contém os atributos e métodos genéricos.

- ``Subclasse(Filha):`` Herda tudo da *Superclasse* e pode adcionar ou modificar(sobrescrever) comportamentos.

---

## 3. Exemplo Prático: Sistema de Dispostivos

Vamos ver um código exemplo, hierarquia de eletrônicos.

```
# SUPERCLASSE(Generalização)
class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f"{self.nome} está ligado.")

# SUBCLASSE (Especialização)
class Smartphone(Eletronico): # Entre parênteses indicamos a herança
    def __init__(self, nome, modelo):
        # super() chama o construtor da classe Pai
        super().__init__(nome)
        self.modelo = modelo

    def conectar_5g(self):
        print(f"{self.nome} {self.modelo} conectando ao 5G...")

# --- Uso ---
celular = Smartphone("iPhone", "15 Pro")
celular.ligar()        # Método herdado de Eletronico
celular.conectar_5g()  # Método específico de Smartphone
```

### Pontos Chave:

- ``Herança:`` A classe *Smartphone* recebe automáticamente os atributos e métodos de *Eletronico*.

- ``Encapsulamento Sugerido:`` O atributo *_ligado* utiliza o prefixo **_**(underscore), que na comunidade indica que o atriuto deve ser tratado como um "protegido" ou de uso interno

- A função super():Ela é crucial para que o *nome* seja ininicializado corretamente pela classe pai, permitindo que a subclasse foque apenas nos seus atributos específicos(como *modelo*).