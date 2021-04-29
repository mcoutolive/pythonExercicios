num = int(input(" Digite um número: "))
soma = 0
for i in range(0,(num+1)):
    if (i%2==0):
        print(i)
        soma = soma + i
    else:
        pass
print(soma)