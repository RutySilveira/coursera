n = int(input("Digite um número inteiro: "))

if n != 2 and n % 2 == 0:
    print("não primo")
elif n != 3 and n % 3 == 0:
    print("não primo")
elif n != 5 and n % 5 == 0:
    print("não primo")
elif n != 7 and n % 7 == 0:
    print("não primo")
else:
    print("primo")
