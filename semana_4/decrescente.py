
# Pois o decrescente tem q ser sempre true, se for false, a sequencia se encerra
decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

# coloco um valor para comecar a sequencia, que seja diferente de zero.
valor = 1

while valor != 0 and decrescente:  # só para qnd chega em zero e enqt a sequencia é decrescente
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:  # se o valor for maior que o anterior, ent o decrescente é falso
        decrescente = False  # indicador de passagem, linha 9 e 10

    anterior = valor  # o valor de anterior será o proximo valor da interação

if decrescente:  # Se o decrescente se manterm como true
    print("A sequência está em ordem decrescente!")
else:
    print("A sequência não está em ordem decrescente!")
