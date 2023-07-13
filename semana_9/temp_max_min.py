# Função que recebe lista de temperaturas, e que irá printar a maior e menor temperatura da lista.
def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", mínima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), "C.")

# Função que irá calcular a temperatura máxima e retorna-lá.


def máxima(temps):
    # Variável que irá guardar a temperatura máxima recebida.
    max = temps[0]
    # Variável que irá percorrer toda a lista com os valores de temperatura guardadas em temps.
    i = 1
    # Enquanto i for menor que o comprimento da lista temps.
    while i < len(temps):
        # Se temps de i for maior que o valor guardado em max, o valor será atualizado com o maior valor encontrado.
        if temps[i] > max:
            max = temps[i]
        # i recebe i + 1, para ir para o próximo indice da lista, até chegar ao final do array.
        i = i + 1
    # Retorna a temperatura máxima.
    return max

# Função que irá calcular a temperatura mínima e retorna-lá.


def mínima(temps):
    # Variável que irá guardar a temperatura mínima recebida, que irá comecar com a primeira temperatura da lista.
    min = temps[0]
    # Variável que irá percorrer toda a lista com os valores de temperatura guardadas em temps, comecando com 1, pois já foi inicializada com uma temperatura da posicao zero.
    i = 1
    # Enquanto i for menor que o comprimento da lista temps.
    while i < len(temps):
        # Se temps de i for menor que o valor guardado em min, o valor será atualizado com o menor valor encontrado.
        if temps[i] < min:
            min = temps[i]
        # i recebe i + 1, para ir para o próximo indice da lista, até chegar ao final do array.
        i = i + 1
    # Retorna a temperatura mínima.
    return min

# Funcao que irá fazer o calculo dos testes.


def teste_pontual_mínima(temp_min, valor_esperado_min):
    valor_calculado_min = mínima(temp_min)
    if valor_calculado_min != valor_esperado_min:
        print("Valor errado para array", temp_min)
        # Printa o valor esperado e o valor que foi calculado.
        print("Valor esperado: ", valor_esperado_min,
              ". Valor calculado: ", valor_calculado_min)


def teste_pontual_máximo(temp_max, valor_esperado_max):
    valor_calculado_max = máxima(temp_max)
    if valor_calculado_max != valor_esperado_max:
        print("Valor errado para array", temp_max)
        # Printa o valor esperado e o valor que foi calculado.
        print("Valor esperado: ", valor_esperado_max,
              ". Valor calculado: ", valor_calculado_max)


# Teste que irá verificar se a funcao mínima esta correta.
def testa_mínima():
    print("Iniciando os testes")
    # teste_pontual que recebe como parametro as temperaturas e o valor esperado.
    teste_pontual_mínima([0], 0)
    teste_pontual_mínima([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_mínima([30, 27, 25, 26, 27, 29, 30, 32, 25, 18, 19, 21, 20, 20,
                          22, 23, 25, 24, 26, 28, 31, 29, 27, 28, 30, 26, 27, 28, 29, 30], 18)
    teste_pontual_mínima([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes")


def testa_máximo():
    print("Iniciando os testes")
    # teste_pontual que recebe como parametro as temperaturas e o valor esperado.
    teste_pontual_máximo([0], 0)
    teste_pontual_máximo([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_máximo([30, 27, 25, 26, 27, 29, 30, 32, 25, 18, 19, 21, 20, 20,
                          22, 23, 25, 24, 26, 28, 31, 29, 27, 28, 33, 26, 27, 28, 29, 30], 33)
    teste_pontual_máximo([-20, -25, -10, -15, -12], -10)
    print("Finalizando os testes")
