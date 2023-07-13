n = int(input("Digite um número inteiro: "))

adjacente = False

while n > 0 and not adjacente:
    digito_1 = n % 10
    n = n // 10
    digito_2 = n % 10
    n = n // 10

    if digito_1 == digito_2:
        adjacente = True

if adjacente:
    print("sim")

else:
    print("não")
