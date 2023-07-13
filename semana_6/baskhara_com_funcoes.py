import math


def delta(a, b, c):  # definida a funcao delta que recebe, a b, c . E retorna na linha abaixo
    return b ** 2 - 4 * a * c


def main():  # criada uma funcao principal que ira ler os 3 valores
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)  # aqui a funcao será chamada


def imprime_raizes(a, b, c):  # essa funcao ira imprimir as raizes
    # criada a variavel d para a funcao delta n ser chamada varias vzs
    d = delta(a, b, c)
    if d == 0:
        raiz_1 = (-b + math.sqrt(d)) / (2 * a)
        print("A única raiz é: ", raiz_1)
    else:
        if d < 0:
            print("Esta equacao nao possui raizes reais")
        else:
            raiz_1 = (-b + math.sqrt(d)) / (2 * a)
            raiz_2 = (-b - math.sqrt(d)) / (2 * a)
            print("A primeira raiz é: ", raiz_1)
            print("A segunda raiz é: ", raiz_2)
