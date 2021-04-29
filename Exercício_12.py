import numpy as np
vetor_1=[]
vetor_2=[]
vetor_3=[]
vetor_4=[]
vetor_5=[]
matriz =np.array([[vetor_1],[vetor_2],[vetor_3],[vetor_4],[vetor_5]])
resposta = str('f')
gabarito = ['a','c','d','a','b','b','c','d','a','d']

for i in range(0,10):
    while (resposta!='a')or(resposta!='b')or(resposta!='c')or(resposta!='d'):
        print("Aluno nº",1)
        questao = i + 1
        print("Questão nº:",questao)
        resposta = str(input("Digite a resposta para a questão: "))
        vetor_1.append(resposta)

for i in range(0,10):
    while (resposta!='a')or(resposta!='b')or(resposta!='c')or(resposta!='d'):
        print("Aluno nº",2)
        questao = i + 1
        print("Questão nº:",questao)
        resposta = str(input("Digite a resposta para a questão: "))
        vetor_2.append(resposta)

for i in range(0,10):
    while (resposta!='a')or(resposta!='b')or(resposta!='c')or(resposta!='d'):
        print("Aluno nº",3)
        questao = i + 1
        print("Questão nº:",questao)
        resposta = str(input("Digite a resposta para a questão: "))
        vetor_3.append(resposta)

for i in range(0,10):
    while (resposta!='a')or(resposta!='b')or(resposta!='c')or(resposta!='d'):
        print("Aluno nº",4)
        questao = i + 1
        print("Questão nº:",questao)
        resposta = str(input("Digite a resposta para a questão: "))
        vetor_4.append(resposta)

for i in range(0,10):
    while (resposta!='a')or(resposta!='b')or(resposta!='c')or(resposta!='d'):
        print("Aluno nº",5)
        questao = i + 1
        print("Questão nº:",questao)
        resposta = str(input("Digite a resposta para a questão: "))
        vetor_5.append(resposta)

print(matriz)


