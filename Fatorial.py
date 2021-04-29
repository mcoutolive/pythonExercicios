num = int(input("Digite um número: "))
fatorial = 1
for i in range(1,num):
    fatorial = fatorial*(i+1)
print(num,'! = ',fatorial)