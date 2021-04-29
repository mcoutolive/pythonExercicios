maior=0
menor=0
soma=0
vetor = []
for i in range(5):
    numero = float(input(" Insira um valor: "))
    vetor.append(numero)
    soma = soma + numero
    if (vetor[i]>maior):
        maior = vetor[i]
    if (vetor[i]<menor):
        menor = vetor[i]
media = soma/5
print("O maior valor é:",maior)
print("O menor valor é:",menor)
print("A média dos valores é:",media)

