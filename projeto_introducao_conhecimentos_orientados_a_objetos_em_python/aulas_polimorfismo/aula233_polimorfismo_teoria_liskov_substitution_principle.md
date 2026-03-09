# Teoria: Polimorfismo, Assinatura de Métodos e Liskov Substitution Principle

Vamos abordar o **Polimorfismo**, a **Assunção de Métodos** e o **Princípio de Substituição de Liskov(LSP)**. Na jornada de aprendizado de Engenharia de Software, esses conceitos são os que garantem que o seu código seja *plugável* e fácil de estender.

---
## 1. Polimorfismo: "Muitas Formas"

O **Polimorfismo** é a capacidade de um objeto ser tratado como uma instância de sua superclasse, mas comportar-se de acordo com sua subclasse real.

Entendeu? Se a resposta for "não", vamos compreender agora.

Em Python, isso acontece através da **Sobreposição (Override)**. O programa chama o mesmo método em objetos de tipos diferentes, e cada um reage à sua maneira.

```Python
class Notificacao(ABC):
    @abstractmethod
    def enviar(self) -> bool pass

class Email(Notificacao):
    def enviar(self) -> bool:
        print("Enviando E-mail...")
        return True

class SMS(Notificacao):
    def enviar(self) -> bool:
        print("Enviando SMS...")
        return True

# POLIMORFISMO EM AÇÃO:
# A função não sabe se é Email ou SMS, ela só sabe que é uma "Notificacao"
def disparar_alerta(notificacao: Notificacao):
    notificacao.enviar()

disparar_alerta(Email()) # Saída: Enviando E-mail...
disparar_alerta(SMS()) # Saída: Enviando SMS...
```
---
## 2. Assinatura de Métodos

A **Assinatura** é o *ID* de um método. Em muitas linguagens(como Java), a assinatura inclui o nome do método + tipos dos parâmetros. No Python, como a tipagem é dinâmica, a assinatura foca no **nome** e na **quantidade/ordem dos parâmetros**.

- ```Regra de Ouro do Polimorfismo:``` Para que o polimorfismo funcione corretamente via herança, a subclasse deve manter a mesma assinatura do pai. Se o pai recebe *(mensagem)*, a filha não deve mudar para *(mensagem, prioridade)*, ou você quebrará o código que espera apenas a mensagem.

---
## 3. Liskov Substitution Principle(LSP)

Este é o *L* do acrônimico <a href="https://www.google.com/search?client=opera-gx&q=solid&sourceid=opera&ie=UTF-8&oe=UTF-8" target="_blank">
  <strong>S-O-L-I-D</strong>
</a>. O princípio, criado por ***Barbara Liskov***, diz o seguinte:

> "Se $S$ é um subtipo de $T$, então objetos do tipo $T$ podem ser substituídos por objetos do tipo $S$ sem quebrar o programa."

- ```Na prática:``` Uma classe filha deve ser capaz de fazer tudo o que a classe pai faz, sem comportamentos inesperados. Se a sua subclasse *quebra* quando usada no lugar do pai, violamos o **LSP**.

- ```Exemplo de Violação do LSP:``` Imagine uma classe **Passaro** com o método ***voar()***. Se criamos uma subclasse **Pinguim**, teremos um problema, pois pinguins não voam. Ao tentar fazer um pinguim voar, seu programa pode lançar um erro inesperado.

    - ```Solução na Engenharia:``` Criar uma hierarquia melhor, como **PassaroQueVoa** e **PassaroQueNaoVoa**.
