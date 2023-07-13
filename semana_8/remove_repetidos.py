def remove_repetidos(numbers):
    # Cria uma lista vazia para armarzenar os elementos únicos.
    valores_unicos = []

    # Para cada item do inicio ao fim em numbers:
    for i in range(len(numbers)):
        valor = numbers[i]  # Valor recebe, numbers[i]
        ehRepetido = False  # Verifica se numbers sao repetidos ou nao.

        # Para cada item do inicio ao fim em valores:
        for j in range(len(valores_unicos)):
            # Se valor for igual a valores, os numeros contidos em valores, então é repetido, e nao entra na lista valores.
            if valor == valores_unicos[j]:
                ehRepetido = True

        if not ehRepetido:  # Se não for repetido, o numero é adicionado a valores.
            valores_unicos.append(numbers[i])

    # Retorna a lista valores, com seus respectivos numeros de forma ordenada.
    return sorted(valores_unicos)


# Testes para verificar se a funcao remove_repetidos está correta.
def test_remove_repetidos():
    assert remove_repetidos([2, 4, 2, 2, 3, 3, 1]) == [1, 2, 3, 4]
    assert remove_repetidos([1, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
