vetor = []
for i in range(5):
    numero = float(input(" Insira um valor: "))
    vetor.append(numero)
print("A posição do menor valor é:",vetor.index(min(vetor)))
print("A posição do maior valor é:",vetor.index(max(vetor)))