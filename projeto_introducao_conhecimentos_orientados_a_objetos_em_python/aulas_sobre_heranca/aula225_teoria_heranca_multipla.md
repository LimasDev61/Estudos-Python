# Teoria - Herança Mútipla - Python Orientado a Objetos

Na Engenaria de Software, a **Herança Mútipla** ocorre quando uma classe filha derivada de ***duas ou mais superclasses***. O Python é uma das poucas linguagens modernas(ao contrário de Java ou C#) que suporta esse recurso de forma nativa e robusta.

Embora poderosa, ela introduz uma complexibilidade clássica: se ambas as classes pai tiverem um método com o mesmo nome, qual deles o Python deve executar?

---
## 1. O Conceito: "É um" de várias fontes

A herança mútipla é útil quando um objeto possui naturezas distintas que se complementam.

- <span style="color:gray">``Exemplo:``</span> Um *Smartphone* pode ser visto tanto como um *Eletronico* quanto como um *GadgetCumunicacao*.

- <span style="color:gray">``Sintaxe:``</span> Basta separar as classes pai por vírgula dentro dos parênteses.

```Python
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
```

Saída:
```
LOG: Iniciando sistema
Conectando ao banco de dados...
```

---
## 2. O Problema do Diamante (Diamond Problem)

O maior desafio da herança múltipla acontece quando duas classes pai herdam de uma mesma classe avó e ambas sobrescrevem o mesmo método. Sem uma regra clara, o interpretador ficaria "confuso".

```Python

# Diamond
#           A
#         /   \
#        B     C
#         \   /
#           D
```

---
## 3. MRO: Method Resolution Order

Para resolver esse conflito, o Python utiliza um algoritmo chamado **C3 Linearization** para criar o **MRO**. Ele define uma ordem linear e determinística de busca para os métodos.

Podemos consultar essa ordem em qualquer classe usando o atributo *__mro__* ou o método **.mro()**.

```Python
class A:
    def fala(self):
        print("Fala de A")

class B(A):
    def fala(self):
        print("Fala de B")

class C(A):
    def fala(self):
        print("Fala de C")

class D(B, C):
    pass

# Qual será a saída?
objeto = D()
objeto.fala() # Saída: "Fala de B" 

# Resultado da ordem de resolução de métodos (MRO)
print(D.mro())
# Ordem: D -> B -> C -> A -> object
```

```O que acontece aqui?``` O Python busca primeiro em **D**. Se não char, busca em **B**(o primeiro pai listado). Se não achar em **B**, busca em **C**, e por último na base **A**. No exemplo acima, ele executará a "Fala de B".

```Descubra mais sobre o C3linearization:``` https://en.wikipedia.org/wiki/C3_linearization

---
## 4. Mixins: O uso inteligente da Herança Múltipla

Na Engenharia de Software profissional, raramente usamos herança mútipla para criar hierarquias complexas de "seres". Em vez disso, usamos **Mixins**.

Um **Mixin** é uma classe pequena que não foi feita para ser instanciada sozinha, mas sim para "adicionar" uma habilidade a outra classe.

- ```Dica de Roadmap:``` Mixins são comuns em frameworks como Django e em sistemas de log e serelização.

```Python
class JsonMixin:
    def para_json(self):
        import json
        return json.dumps(self.__dict__)

class Produto(JsonMixin): # Adiciona a 'habilidade' de virar JSON
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p = Produto("Mouse", 50)
print(p.para_json())
```

---
## 5. Veredito: Usar ou não usar?

- ```Vantagens:``` Extrema flexibilidade e reaproveitamente de "habilidades"(Mixins).

- ```Risco:``` O código pode ser tornar um "espaguete" difícil de rastrear se a hierarquia for muito profunda.

A Herança mútipla não consome mais RAM significativamentes,mas consome mais **espaço mental** do desenvolvedor. Use com parcimônio.