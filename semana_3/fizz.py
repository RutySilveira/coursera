numero = int(input("Digite um numero inteiro: "))

divisibilidade = (numero % 3 == 0)

if divisibilidade:
    print("Fizz")

else:
    print(numero)
