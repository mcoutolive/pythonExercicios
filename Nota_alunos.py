num = int(input(" Digite o número de alunos matriculados: "))
maior = 0
menor = 0
for i in range (1,(num+1)):
    print( " Nota do aluno ", i)
    nota = float(input(" Digite a nota do aluno: "))
    if (nota>=0):
        if (nota>maior):
            maior = nota
        if (nota<maior):
            menor = nota
print(" Menor nota: ", menor)
print(" Maior nota: ", maior)

