vetor = []
vetor_inv = []
for i in range(10):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)
print("Vetor sem inverter",vetor)
'''Mostrando o vetor invertido'''
for i in range(9,-1,-1):
    vetor_inv.append(vetor[i])
print("Vetor invertido",vetor_inv)
