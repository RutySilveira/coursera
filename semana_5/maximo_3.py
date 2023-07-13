def maximo(x, y, z):  # criada a funcao maximo que irá receber dois parâmetros

    if x > y and x > z:  # Se x for maior que y e z
        return (x)  # retorno x, sendo o maior numero
    if y > x and y > z:  # Se y maior que z e z
        return y  # retorno x, sendo o maior numero
    else:
        return (z)  # caso contrário retorno y como o maior numero.


x = int(input("Digite o primeiro numero: "))  # recebo o valor de x
y = int(input("Digite o segundo número: "))  # recebo o valor de y
z = int(input("Digite o terceiro número: "))  # recebo o valor de y


# print chama a funcao máximo que ira retornar o maior numero.
print(maximo(x, y, z))
