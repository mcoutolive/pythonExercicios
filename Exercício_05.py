vetor = []
nota = 0
soma = 0
contador = 0
while (contador<15):
    nota = float(input("Insira a nota do aluno: "))
    if (nota>=0)and(nota<=10):
        contador+=1
        soma = soma + nota
        vetor.append(nota)
    else:
        print("Valor inválido")
mediageral = (soma/15)
print("Lista com todas as notas:",vetor)
print("A média geral da sala é:",mediageral)