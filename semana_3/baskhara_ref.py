import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: ", raiz_1)
else:
    if delta < 0:
        print("Esta equacao nao possui raizes reais")
    else:
        raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é: ", raiz_1)
        print("A segunda raiz é: ", raiz_2)
