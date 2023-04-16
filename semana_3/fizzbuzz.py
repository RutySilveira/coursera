numero = int(input("Digite um numero inteiro: "))

divisibilidade = (numero % 3 == 0) and (numero % 5 == 0)

if divisibilidade:
    print("FizzBuzz")

else:
    print(numero)
