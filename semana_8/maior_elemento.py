def maior_elemento(numbers):  # Definida a funcao maior_elemento
    # Criada a variavel que recebe o numero máximo da lista numbers
    numero_maximo = max(numbers)
    return numero_maximo  # Retorna o valor da variavel, sendo o numero máximo.


# Teste para verificar se a funcao maior_elemento esta correta.
def test_maior_elemento():
    assert maior_elemento([1, 6, 5, 7, 9, 2]) == 9
    assert maior_elemento([1, 2, 4, 6, 8, 5]) == 8
