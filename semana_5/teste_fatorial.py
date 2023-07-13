def fatorial(n):
    if n < 0:  # Se o valor n de entrada for menor que zero, a funcao retorna 0. Pois o fatorial de numero negativo nao é definido
        return 0
    i = fat = 1  # inicio o fat com 1 pois é o elemento neutro da multiplicacao, o indice i tambem vale 1
    while i <= n:
        fat = fat * i  # durante cada iteracao do loop o valor de fat é atualizada
        i = i + 1
    return fat


def test_fatorial0():  # testando o fatorial de 0
    assert fatorial(0) == 1  # Por definicao o fatorial de 0 deve ser  == a 1


def test_fatorial1():
    assert fatorial(1) == 1


def test_fatorial_negativo():
    assert fatorial(-10) == 0


def test_fatorial4():
    assert fatorial(4) == 24


def test_fatorial5():
    assert fatorial(5) == 120
