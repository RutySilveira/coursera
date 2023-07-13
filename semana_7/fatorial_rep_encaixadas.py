# Recebe o primeiro numero inteiro da sequencia de numeros.
n = int(input("Digite um número inteiro: "))
while n >= 0:  # Enquanto n for maior ou igual a zero.
    # Fatorial começa com 1, pois 1 é o numero final da fatoracao.
    fatorial = 1
    while n > 1:  # Enquanto n maior que 1.
        fatorial = fatorial * n  # Fatorial recebe, fatorial vezes n.
        n = n - 1  # n recebe, n -1.
    # O resultado final é alocado na variavel fatorial, que será imprimida.
    print(fatorial)
    # Sera recebido uma sequencia de numeros a serem fatorados, o 2 numero em diante é recebido aqui.
    n = int(input("Digite um número inteiro: "))
