n = int(input("Digite um número inteiro:"))

primo = True
i = n


while n > 1 or primo:
    i = i - 1
    mod = n % i

if mod != 0:
    primo = False

if primo:
    print("primo")

else:
    print("não primo")
