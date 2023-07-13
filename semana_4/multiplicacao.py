tamanho = int(input("Digite uma sequência de números: "))

produto = 1  # o produto comecará em 1. Inicia-se c/ o numero neutro da operação
i = 0  # o i comecará em zero até chegar no valor da variavel tamanho.

while i < tamanho:  # Enqt i for menor que tamanho, o laço continua
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1  # i recebe o valor anterior somado a 1

print("O produto dos valores digitados é: ", produto)
