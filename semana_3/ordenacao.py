numero_1 = int(input("Digite o primeiro numero inteiro: "))

numero_2 = numero = int(input("Digite o segundo numero inteiro: "))

numero_3 = numero = int(input("Digite o terceiro numero inteiro: "))

crescente = (numero_1 < numero_2) and (numero_2 < numero_3)

if crescente:
    print("crescente")

else:
    print("não está em ordem crescente")
