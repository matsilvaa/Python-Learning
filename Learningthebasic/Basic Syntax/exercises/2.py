'''
    Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, João e Pedro. Cada valor na lista representa o gasto em uma das semanas do mês:

    Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro. Para isso, crie um código em Python que responda a essa pergunta.
'''

gastos_joao = [300, 500, 200, 800]
gastos_pedro= [200, 400, 500, 700]

soma_j = 0
soma_p = 0

for soma1 in gastos_joao:
    soma_j += soma1

for soma2 in gastos_pedro:
    soma_p += soma2

if(soma_j > soma_p):
    print("Joao gastou mais!")

if(soma_p > soma_j):
    print("Pedro gastou mais!")

if(soma_j == soma_p):
    print("Ambos gastaram a mesma quantidade!")