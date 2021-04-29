num = int(input("Digite um número: "))
soma = 0
lista =[]
for i in range(1,num+1):
    soma = soma + i
    lista.append(i)
print(lista)
print("A soma dos",num,"primeiros números inteiros é",soma)

