vetor_A = []
soma_impar=0
soma_par=0
soma_total=0
contador_impar=0
for i in range(5):
    valor_vetor = int(input("Insira um valor: "))
    vetor_A.append(valor_vetor)
    soma_total = soma_total + vetor_A[i]
    if (vetor_A[i]%2==0):
        soma_par = soma_par + vetor_A[i]
    else:
        soma_impar = soma_impar + vetor_A[i]
        contador_impar+=1
porcent_impar_par=(contador_impar/5)*100
print("A soma dos números ímpares é igual a",soma_impar)
print("A soma dos números pares é igual a",soma_par)
print("A soma total dos números é igual a ",soma_total)
print(porcent_impar_par,"% dos valores do vetor são ímpares")

