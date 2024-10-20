'''
    numeros = [10, 20, 30, 40, 50]
    Dada uma lista de numeros, calcule a média dos valores dessa lista
'''

numeros = [10, 20, 30, 40, 50]
soma = 0

for numero in numeros:
    soma += numero

print(soma/(len(numeros)))