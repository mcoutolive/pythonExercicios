vetor = []
contador_negativos = 0
soma_positivos = 0
contador_zeros = 0
for i in range(10):
    numero = float(input("Insira um numero: "))
    vetor.append(numero)
    if (numero<0):
        contador_negativos+=1
    elif (numero>0):
        soma_positivos = soma_positivos + numero
    else:
        contador_zeros+=1
print("Lista com os números digitados",vetor)
print("Quantidade de números negativos:",contador_negativos)
print("Soma de todos os números positivos:",soma_positivos)
print("Quantidade de zeros:",contador_zeros)

