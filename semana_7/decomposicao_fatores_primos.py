n = int(input("Digite um numero inteiro > 1: "))

fator = 2  # fator comeca com 2 pois é o primeiro numero primo
# No incio fa fatoracao inicamos com zero, pois ainda sera fatorado no segundo while.
multiplicidade = 0

while n > 1:  # Enquanto n maior que 1 pois poderá ser fatorado
    while n % fator == 0:  # Enquanto o resto da divisao de n pelo fator for zero, a fatoracao continua
        # A cada divisao é somado 1 p/ a multiplicidade
        multiplicidade = multiplicidade + 1
        n = n / fator  # n recebe n dividido pelo fator
    if multiplicidade > 0:  # Se a multiplicidade for maior que zero, irá imprimir
        print("fator ", fator, "multiplicidade = ", multiplicidade)
    fator = fator + 1  # Aqui o fator muda
    multiplicidade = 0  # A multiplicidade é zerada para ser reiniciada para o novo fator
