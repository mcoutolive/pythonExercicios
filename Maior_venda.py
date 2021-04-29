lista = []
for i in range(1,5):
    print(i, " de março de 2020: ")
    num = int(input(" Digite o número de vendas "))
    lista.append(num)
print("O maior número de vendas para este mês foi de",max(lista))
print("O menor número de vendas para este mês foi de",min(lista))
