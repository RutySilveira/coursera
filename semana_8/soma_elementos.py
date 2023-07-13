def soma_elementos(numbers):  # Criada a funcao soma_elementos.
    soma = 0  # A contagem da variavel se inicia com o zero.

    for i in numbers:  # Para cada i em numbers:
        soma = soma + i  # Soma recebe soma + i

    # Retorna o valor da variavel soma, que consta a soma de todos os elementos da lista numbers.
    return soma


# Teste para verificar se a funcao soma_elementos esta correta.
def test_soma_elementos():
    assert soma_elementos([2, 4, 2, 2, 3, 3, 1]) == 17
    assert soma_elementos([1, 2, 3, 3, 3, 4]) == 16
