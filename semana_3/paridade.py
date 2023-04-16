numero = int(input("Digite um numero inteiro: "))

sendo_par = int(numero % 2 == 0)

if sendo_par:
    print("O numero", numero, "é par.")
else:
    print("O numero", numero, "é ímpar.")
