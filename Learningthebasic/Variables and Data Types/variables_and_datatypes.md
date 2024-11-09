- Variáveis
    
    No python podemos usamos as variáveis para armazenar diversos tipos de dados podendo ser acessados novamente pelo seu nome.
    
    <aside>
    💡
    
    Tipos de Variáveis: 
    
    Tipos Numéricos:
    
    - `Int - Números Inteiros`: Guardam números inteiros sem casas decimais.
        
        ```python
        idade = 12
        ```
        
    - `Float - Números Decimais`: Guardam números com casas decimais.
        
        ```python
        altura = 1.41
        ```
        
    - `complex - Números Complexos` : Guardam números com partes imaginárias.
        
        ```python
        x = 3 - 12y
        ```
        
    
    Tipos de Texto:
    
    - `Str - Textos e caracteres` : Guardam textos e conjuntos de caracteres.
        
        ```python
        # Todos os valores str devem ser armazenados entre "" ou ''
        nome = "matheus"
        senha = "a3uni23n4523m-ni234!"
        ```
        
    
    Tipos de Sequência:
    
    - `list - Coleção mutável` : Coleção mutável de itens ordenados de diferentes tipos.
        
        ```python
        lst = [1, 2, 4, 5, "ola!"]
        ```
        
    - `tuple - Coleção imutável` : Coleção imutável de itens ordenados de diferentes tipos.
        
        ```python
        tup = [1, 3, "ovo"]
        ```
        
    - `range - Sequencia de números` : Sequência de números normalmente usadas para loops
        
        ```python
        r = range(5) # Sequencia de 0 a 4
        ```
        
    
    Tipo de Mapeamento:
    
    - `dict - Dicionário` : Guardam pares de informações (chave: valor), como em um dicionário.
        
        ```python
        pessoa = {"nome": "João", "idade": 10}
        ```
        
    
    Tipo de Conjunto:
    
    - **`set`** : Um conjunto mutável, que não permite elementos duplicados.
        
        ```python
        s = {1, 2, 3, 4}
        ```
        
    - **`frozenset`**: Um conjunto imutável. Uma vez criado, não pode ser alterado.
        
        ```python
        fs = frozenset([1, 2, 3])
        ```
        
    
    Tipo de Boleano:
    
    - `Bool - True or False` : Guardam os valores Verdadeiro ou Falso.
        
        ```python
        isTor = True
        Loginsucl = False
        ```
        
    
    Tipo de Binários:
    
    - **`bytes`** : Uma sequência **imutável** de bytes.
        
        ```python
        b = b'hello'
        ```
        
    - **`bytearray`** : Uma sequência **mutável** de bytes.
        
        ```python
        ba = bytearray([65, 66, 67])
        ```
        
    - **`memoryview`** : Um objeto que permite acessar a memória interna de objetos que suportam o protocolo de buffer (por exemplo, arrays).
        
        ```python
        mv = memoryview(b'hello')
        ```
        
    </aside>