vetor_A = []
vetor_B = []
'''Para índices que variam de 0 a 9'''
for i in range(10):
    valor_vetor = int(input("Insira um valor: "))
    vetor_A.append(valor_vetor)
    if (i%2==0):
        valor_vetor = 5 * valor_vetor
        vetor_B.append(valor_vetor)
    else:
        valor_vetor = 5 + valor_vetor
        vetor_B.append(valor_vetor)
'''Mostrando os valores invertidos com a função reverse'''
vetor_A.reverse()
vetor_B.reverse()
print(vetor_A)
print(vetor_B)