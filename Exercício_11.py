vetor_A = [0,0,0,0,0]
vetor_B = [0,0,0,0,0]
char = 'char'
numa = -1
numb = -1
while(numa<=0)or(numa>=10000):
    numa = int(input(" Insira um valor maior que 0 e menor que 10.000: "))
    char = str(numa)
    if (numa>=1000)and(numa<=9999):
        char = '0' + char
    elif (numa>=100)and(numa<=999):
        char = '0' + '0' + char
    elif (numa>=10)and(numa<=99):
        char = '0' + '0' + '0' + char
    else:
        char = '0' + '0' + '0' + '0' + char
for i in range(5):
    vetor_A[i]=char[i]
print(vetor_A)
while(numb<=0)or(numb>=10000):
    numb = int(input(" Insira um valor maior que 0 e menor que 10.000: "))
    char = str(numb)
    if (numb>=1000)and(numb<=9999):
        char = '0' + char
    elif (numb>=100)and(numb<=999):
        char = '0' + '0' + char
    elif (numb>=10)and(numb<=99):
        char = '0' + '0' + '0' + char
    else:
        char = '0' + '0' + '0' + '0' + char
for i in range(5):
    vetor_B[i]=char[i]
print(vetor_B)