numero = int(input("Digite um numero inteiro: "))

divisibilidade = (numero % 5 == 0)

if divisibilidade:
    print("Buzz")

else:
    print(numero)
