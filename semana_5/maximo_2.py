def maximo(x, y):  # criada a funcao maximo que irá receber dois parâmetros

    if x > y:  # Se x for maior que y
        return (x)  # retorno x, sendo o maior numero
    else:
        return (y)  # caso contrário retorno y como o maior numero


x = int(input("Digite o primeiro numero: "))  # recebo o valor de x
y = int(input("Digite o segundo número: "))  # recebo o valor de y

# print chama a funcao máximo que ira retornar o maior numero.
print(maximo(x, y))
