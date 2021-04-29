number_terms = int(input("Insira o numero de termos: "))
array = [0,1,1]
for i in range(3,(number_terms)):
    number = array[i-1]+array[i-2]
    array.append(number)
print("Sequência de Fibonacci para",number_terms,"termos: ",array)
