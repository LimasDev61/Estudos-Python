# **Curiosidades sobre Convenção de Nomes**

---

### **Introdução** 📌

Na Engenharia de Software, as convenções de nomes **servem** para deixar o código legível e organizado para outros
desenvolvedores (e para nós mesmos). Portanto, não é apenas “estética”.  
Em Python, seguimos majoritariamente a **PEP 8**, o guia de **estilo oficial** da linguagem.

---

### 🧩 **1. O Padrão de Escrita**

Aqui podemos ver padrões que separam iniciantes de profissionais.

Tipo de Entidade | Padrão | Exemplo
-----------------|--------|---------------------------------------
Classe | PascalCase | Usuario, BancoDeDados
Funções/Métodos | snake_case | calcular_media(), obter_nomes()
Variáveis | snake_case | nome_pessoa, data_atual
Constantes | UPPER_CASE | PI, DATA_BASE, DATABASE, URL
Módulos (.py) | snake_case (curto) | auth_user.py, main.py
---
---

### 🔍 **2. O Significado dos Underlines ( _ )**

No Python, o uso do _(underscore)_ antes ou depois do nome é uma **mensagem para outros programadores**.

#### Exemplos:

**(1) _single_leading_underscore (ex: _preco)**

Indica que o atributo ou método está <span style="color:red"><strong>protegido</strong></span>.

→ O Python não impede que você acesse *objeto._preco*, mas a convenção diz:  
“Ei, isso é interno da classe, não mexa a menos que saiba o que está fazendo.”

---

**(2) __double_leading_underscore (ex: __senha)**

Ativa o <span style="color:red"><strong>Name Mangling</strong></span> (Desfiguração de Nomes).

→ O Python altera o nome internamente para *NomeDaClasse__senha*.  
Isso dificulta o acesso direto e evita conflitos em herança.  
É o mais próximo que temos de um atributo <span style="color:red"><strong>privado</strong></span>.

---

#### <strong>(3) \_\_double\_leading\_and\_trailing\_\_ (ex: \_\_init\_\_)</strong>

São os <span style="color:red"><strong>Dunder Methods</strong></span> (Double Under).

→ **Regra de ouro:**  
nunca crie seus próprios nomes (variáveis, métodos etc.) assim.  
Eles são reservados para comportamentos especiais da linguagem Python  
(ex: *_\_dict__*, *_\_iter__*, *_\_name__*).

---

**(4) Single Underscore _ (Variável “joga fora”)**

Usamos quando recebemos um valor, mas não pretendemos utilizá-lo.

→ Exemplo: queremos repetir algo três vezes, mas não precisamos do índice.

```python
for _ in range(3):
    print("Executando.")

```

**Saída:**
```text
Executando.
Executando.
Executando.

```
---
### 🧠 **3. Curiosidades de Engenharia**

→ **Getters e Setters:**

Em outras linguagens (como C#), é comum ver *get_valor()* e *set_valor()*.  
Em Python isso é considerado **não pythônico**. Usamos o decorador  
<span style="color:red"><strong>@property</strong></span> para manter a interface limpa.

---

→ **Nomes de variáveis e memória:**

Com a a quantidade de memória disponível atualmente, é preferível usar nomes descritivos.  
Evite *a*, *b*, *x1*. Prefira *usuario_cadastrado_recentemente*.  
Código legível é mais importante que economizar caracteres.

---

→ **Módulos vs. Classes:**

É comum iniciantes usarem o mesmo nome para arquivos e classes  
(ex: arquivo *User.py* com a classe *User*).  
Em Python, o arquivo deve ser *user.py* (minúsculo)  
e a classe *User* (PascalCase).

---
---
> 🙏 **Obrigado por acessar este conteúdo!**  
> Espero que tenha sido útil!


