vetor = []
vetor_inv = []
numero_par = 0
contador = 0
'''Inserindo 10 números pares'''
while (contador < 10):
    numero_par = int(input("Insira um numero par: "))
    if (numero_par%2==0):
        vetor.append(numero_par)
        contador += 1
    else:
        pass
print(vetor)
'''Mostrando o vetor invertido'''
for i in range(9,-1,-1):
    vetor_inv.append(vetor[i])
print(vetor_inv)