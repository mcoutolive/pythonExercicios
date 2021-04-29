import numpy as np
matriz_A = np.random.rand(4,2)
matriz_B = np.random.rand(4,2)
matriz_C = np.random.rand(4,2)

for i in range(4):
    for j in range(2):

        print("Elemento da Matriz A com Índice", i, j)
        numero_A = float(input(" Insira um valor: "))
        matriz_A[i, j] = numero_A

        print("Elemento da Matriz B com Índice", i, j)
        numero_B = float(input(" Insira um valor: "))
        matriz_B[i, j] = numero_B

        matriz_C[i,j]=matriz_A[i,j]+matriz_C[i,j]

print("A=",matriz_A)
print("B=",matriz_B)
print("C=",matriz_C)