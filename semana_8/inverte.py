numeros = []  # Criada a variável que ira receber uma lista.

while (True):  # Enquanto Verdadeiro
    # Será recebido valores de n
    n = int(input("Digite um número, ou zero para terminar: "))

    if n != 0:  # Se n for diferente de 0
        numeros.append(n)  # Adiciona o n a lista numeros
    else:  # Se n for igual a 0
        # Para cada i do inicio ao fim da lista numeros, será printando o seus elementos, de trás para frente.
        for i in range(len(numeros) - 1, -1, -1):
            print(numeros[i])
        break  # Loop do for é finalizado.
