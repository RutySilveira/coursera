def soma_elementos(numbers):  # Criada a função soma_elementos.
    # A variável soma_total recebe a soma de numbers.
    soma_total = sum(numbers)
    return soma_total  # Retorna o valor da variável soma_total.


# Teste que irá verificar se a função soma_elementos esta correta.
def test_soma_elementos():
    assert soma_elementos([1, 6, 5, 7, 9, 2]) == 30
    assert soma_elementos([1, 8, 9, 9, 8, 5]) == 40
