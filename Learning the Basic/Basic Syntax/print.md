> Print
> 

A função print() da ao computador a capacidade de se comunicar e exibir textos no console para o usuário. Ela pode receber um ou mais argumentos e, por padrão, converte esses argumentos em strings antes de exibi-los.

```python
print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parâmetros

- `objetos`: um ou mais objetos que você deseja imprimir. Você pode passar números, strings, listas, etc.
- `sep`: define o separador entre os objetos, padrão é um espaço (`' '`).
- `end`: define o que é adicionado no final da impressão. O padrão é uma nova linha (`'\n'`).
- `file`: permite redirecionar a saída para um arquivo ou outro objeto semelhante a um arquivo.
- `flush`: se `True`, força a saída a ser exibida imediatamente.
    
    ### Objetos:
    
    ```python
    print("Ola, Mundo!") # Strings
    print(23, 10 * 3) # Números
    frutas = ["uva", "banana", "pera"]
    print(frutas) # Listas
    pessoa = {"nome": "Matheus", "Idade": 17}
    print(pessoa) # Dicionário
    ```
    
    ### Separador:
    
    ```python
    print("Olá", "mundo")  # Saída: Olá mundo
    print("Maçã", "Banana", "Cereja", sep=", ")  # Saída: Maçã, Banana, Cereja
    print("2024", "10", "19", sep="-")  # Saída: 2024-10-19
    print(1, 2, 3, 4, 5, sep=" - ")  # Saída: 1 - 2 - 3 - 4 - 5
    print("Python", "é", "divertido", sep=" *** ")  # Saída: Python *** é *** divertido
    ```
    
    ### Final:
    
    ```python
    print("Olá, mundo!")  # A saída termina com uma nova linha
    print("Como você está?")
    print("Olá", end=" ")
    print("mundo!")  # Saída: Olá mundo!
    print("Python", end=" é incrível! ")
    print("Vamos programar.")  # Saída: Python é incrível! Vamos programar.
    ```
    
    ### File:
    
    - (Como usar o File)
        
        ## Como usar o File (Detalhado)
        
        O parâmetro file na função print permite que você escolha onde a saída será enviada. Por padrão, a saída vai para o console (ou terminal), mas você pode redirecioná-la para um arquivo ou outro objeto que se comporte como um arquivo.
        
        ### Como usar o `file`
        
        1. **Abrindo um arquivo**:
            - Para usar o parâmetro `file`, primeiro você precisa abrir um arquivo com a função `open()`. O modo de abertura pode ser:
                
                ```python
                with open("exemplo.txt", "w") as arquivo:
                with open("exemplo.txt", "a") as arquivo:
                ```
                
                - `'w'`: para escrever (cria um novo arquivo ou sobrescreve um existente).
                - `'a'`: para anexar (adiciona ao final de um arquivo existente).
        2. **Passando o arquivo para `print()`**:
            - Depois de abrir o arquivo, você pode passar o objeto de arquivo como argumento para o parâmetro `file` na função `print()`.
                
                ```python
                with open("exemplo.txt", "w") as arquivo:
                    print("Esta é a primeira linha.", file=arquivo)
                    print("Esta é a segunda linha.", file=arquivo)
                ```
                
                ---
                
            
            <aside>
            💡
            
            Reforçando…
            
            > Open() - Função do python utilizada para abrir arquivos.
            > 
            
            Syntax → open(<file_name>, <mode>)
            
            **Modo**: uma string que especifica o modo de abertura do arquivo. Os modos mais comuns são:
            
            - `'r'`: modo de leitura (padrão). O arquivo deve existir.
            - `'w'`: modo de escrita. Cria um novo arquivo ou sobrescreve um existente.
            - `'a'`: modo de anexação. Adiciona conteúdo ao final de um arquivo existente.
            - `'b'`: modo binário (pode ser combinado com outros modos, como `'rb'` ou `'wb'`).
            
            > With - É uma estrutura de controle utilizada para fechar o arquivo automaticamente ao fim do bloco de código.
            > 
            
            > as - A palavras as permite que você atribua um nome ao objeto retornado pela função.
            > 
            </aside>
            
            ---
            
    
    ```python
    # Escrevendo em um Arquivo de Texto:
    with open("exemplo.txt", "w") as f:
    	print("Ola Mundo!", file=f)
    # Escrevendo Várias Linhas em um Arquivo:
    with open("lista_frutas.txt", "w") as f:
        print("Maçã", file=f)
        print("Banana", file=f)
        print("Cereja", file=f)  # Cada fruta em uma linha
    # Usando o Modo Append (Adicionar):
    with open("saida.txt", "a") as f:
        print("Nova linha adicionada.", file=f)  # Adiciona ao final do arquivo existente
    # Redirecionando para sys.stdout:
    import sys
    with open("saida.txt", "w") as f:
        print("Esta linha vai para o arquivo.", file=f)
        print("Esta linha vai para o console.", file=sys.stdout)
    ```