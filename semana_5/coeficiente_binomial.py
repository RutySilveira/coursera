def fatorial(n):  # criada a funcao fatorial, que ira receber um  numero que irei chamar de n
    fat = 1  # elemento neutro da multiplicacao. Aqui irei guardar o valor das multiplicacoes feitas. mas irei inicialá c/ o elem neutro
    while (n > 1):
        fat = fat * n  # fat recebe fat vezes o n corrente (que ira mudando)
        # n recebe n - 1 , ate que n chegue a 1, entao o while ira parar.
        n = n - 1
        return fat


# p/ calcular o numero binomial, preciso de dois parametros
def numero_binomial(n, k):

    # retornara o valor da funcao numero_binomial(n,k). A linha 14 esta a formula que irá devolver um valor
    return fatorial(n) / (fatorial(k) * fatorial(n-k))


def testa_fatorial():  # funcao que ira fazer p teste
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
