import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []  # Lista onde os textos serão inseridos.
    # Enter p/ começar novo texto.
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:  # Enquanto texto continuar a entrar.
        textos.append(texto)  # Adiciono o texto, a lista textos.
        i += 1  # i recebe i + 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos  # Retorna a lista textos.


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+',
                         texto)  # Aqui o texto é dividido em sentenças e armazenado na variável.
    # Se A ultima setença for uma string vazia. ela é removida de sentenças.
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas  # O resultado da variavel sentenças é retornado.


def tamanho_medio_sentencas(sentencas):
    # A função recebe uma lista de sentenças e devolve o tamanho médio das sentenças.
    soma = 0
    # Para cada sentença na lista sentencas, soma recebe o tamanho da sentenca, que vai somando todos os tamanhos das sentencas da lista.
    for sentenca in sentencas:
        soma += len(sentenca)
    # é retornado o tamnho medio das sentencas, dividindo a soma dos tamanhos pelo numero total de sentencas.
    return soma / len(sentencas)


def complexidade_sentenças(sentencas):
    # A função recebe uma lista de sentencas e devolve a complexidade das sentencas.
    qtd_frases = 0
    # Para cada sentenca na lista sentencas.
    for sentenca in sentencas:
        # Frases recebe uma lista de frases
        frases = separa_frases(sentenca)
        # qnt de frases recebe e soma o tamanho de todas as frases
        qtd_frases += len(frases)
    # retorna a complexidade media, dividindo o numero total de frases pelo numero total de sentencas.
    return qtd_frases / len(sentencas)


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

# A função recebe uma sentença como entrada, divide-a em frases, e retorna uma lista de frases, extraídas da sentença.


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()  # É um dicionário que irá armazenar a frequência de cada palavra na lista.
    # Contador que armazena a quantidade de palavras únicas encontradas .
    unicas = 0
    # Para cada palavra na lista_palavras a variável p recebe a versão em letras minusculas da palavra.
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:  # Se a palavra p já esta no dicionario, significa que ela ja foi encontrada anteriormente na lista.
            # Se a frequencia da palavra p é igual a 1. Significa que a palavra p era unica antes de encontrar a palavra atual, e ao encontrar novamente ela não será mais única.
            if freq[p] == 1:
                unicas -= 1  # Então decrementa-se a variável únicas em 1 .
            # Em seguida, incrementa-se a frequencia da palavra em 1 no dicionario freq.
            freq[p] += 1
        else:  # Caso contrário, se p não estiver no dicionário freq, significa que é a primeira vez que a palavra é encontrada na lista.
            # Então a palavra é adicionada ao dicionário freq com uma frequência inicial de 1.
            freq[p] = 1
            unicas += 1  # Então incrementa-se 1 em unicas.

    # O valor de únicas é retornado como resultado da função, representando o número de palavras que aparecem apenas uma vez na lista de palavras.
    return unicas


# Função que recebe como parâmetro uma lista de palavras.
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()  # É um dicionário que irá armazenar a frequência de cada palavra na lista.
    # Para cada palavra na lista_palavras a variável p recebe a versão em letras minusculas da palavra.
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:  # Se a palavra p já esta no dicionario, significa que ela ja foi encontrada anteriormente na lista.
            # Em seguida, incrementa-se a frequencia da palavra em 1 no dicionario freq.
            freq[p] += 1
        # Caso contrário, se a palavra nao estiver na lista, adiciona-se a palavra ao dicionario freq com uma frequência inicial de 1 .
        else:
            freq[p] = 1

    # Retorna o numero de palavras diferentes no dicionário freq.
    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    as_a = le_assinatura()
    as_b = le_assinatura()
    diferença = abs(as_b - as_a)
    resultado = (diferença / 6)
    return resultado


def calcula_assinatura(texto):  # Ruty
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_tamanhos = []  # Lista onde sera armazenado o tamanho das palavras
    # Contador onde sera armazenado o total de palavras no texto.
    total_palavras = 0
    for palavra in texto:  # Para cada palavra no texto, total de palavras recebe + 1
        total_palavras = total_palavras + 1
        p = palavra.lower()  # Transforma a palavra em minuscula
        # Adiciona o tamanho da palavra na lista_tamanhos
        lista_tamanhos.append(len(p))
        # Media recebe o calculo da media do tamanho das palavras do texto
    media = float(sum(lista_tamanhos) / total_palavras)
    # Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    resultado_relacao_type_token = float(
        n_palavras_diferentes(texto) / total_palavras)
    # Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    resultado_razao_hapax = float(n_palavras_unicas(texto) / total_palavras)
    # Média simples do número de caracteres por sentença. Chamo a def separa_sentencas(texto), com a soma dos tamanhos das sentenças dividido pelo numero total de sentenças. Obtendo então o tamanho medio das sentenças.

    tamanho_medio_sentenca = float(
        sum(len(separa_sentencas(texto))) / len(separa_sentencas(texto)))
    # Média simples do número de frases por sentença. Soma do numero de frases por setença, dividido pelo numero de sentenças.
    complexidade_de_sentenças = float(
        sum(len(separa_frases(texto))) / len(separa_sentencas(texto)))
    # Média simples do número de caracteres por frase.
    tamanho_medio_frase = float(sum(len(separa_frases(texto))) /
                                len(separa_frases(texto)))

    return media, resultado_relacao_type_token, resultado_razao_hapax, tamanho_medio_sentenca, complexidade_de_sentenças, tamanho_medio_frase


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    textos = le_textos()
    ass_cp = le_assinatura()
    maior_probabilidade = 0
    texto_infectado = 0

    for i in enumerate(textos):
        lista_valores_assinatura = calcula_assinatura(textos)
        probabilidade = compara_assinatura(
            lista_valores_assinatura, ass_cp)

        if probabilidade > maior_probabilidade:
            maior_probabilidade = probabilidade
            # Adiciona 1 porque os índices começam em 0, mas o número do texto começa em 1
            texto_infectado = i + 1

    return texto_infectado
