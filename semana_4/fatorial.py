n = int(input("Digite o valor de n: "))

# Pois a variavel nao pode comecar vazia, ent colocamos o elemento neutro da multiplicacao.
fatorial = 1

while n > 1:  # Enqt o numero recebido for maios que 1 o laco continua
    # fatorial recebe 1 * n . Sendo fatorial e n mudado a cada rodada do laço
    fatorial = fatorial * n
    n = n - 1  # Aqui o numero de n irá mudando a cada rodada

print(fatorial)
