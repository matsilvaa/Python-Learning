lista = [12, 7, 34, 3, 25, 18, 45, 22, 9, 16, 1, 39, 6, 27, 4, 11, 14, 30, 20, 8] # Lista Principal
lista_ordenada = sorted(lista)

alvo = 45

lista_ordenada.append(alvo)
lista_ordenada = sorted(lista_ordenada) #Ordenando a lista com o alvo

print(lista_ordenada)

vistos = set()
for numero in lista_ordenada:
    complemento = alvo - numero

    if complemento in vistos:
        print("Os valores são:")
        print(complemento)
        print(numero)
    vistos.add(numero)


