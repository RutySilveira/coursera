import math as m


def computador_escolhe_jogada(n, m):
    # Se a quantidade permitida de peças a serem removidas for maior ou igual
    # a quantidade de peças no tabuleiro, retorne a quantidade de peças do tabuleiro (remova tudo)
    if m >= n:
        return n

    count = 1
    n = n - 1

    # Enquanto a quantidade de peças restantes no tabuleiro nao for múltiplo de m + 1, o computador pode remover
    while n % (m + 1) != 0 and count < m and count < n:
        # + enquanto a quantidade de peças a serem removidas no tabuleiro nao for maior do que a permitida, o computador pode remover
        # + enquanto a quantidade de peças a serem removidas no tabuleiro nao for maior do que a quantidade de peças do tabuleiro, o computador pode remover
        count = count + 1  # Atualiza a quantidade de peças à serem removidas
        n = n - 1  # Atualiza a quantidade de peças no tabuleiro

    if count > 0:
        return count  # Retorna a quantidade de peças para remover


def usuario_escolhe_jogada(n, m):
    while True:  # Loop infinito
        count = int(input("Quantas peças voce vai tirar? "))
        # Se essa condição não for verdadeira, sai do loop infinito retornando a escolha do usuário, peças à remover
        if (count > m or count > n or count == 0):
            print("Oops! Jogada inválida! Tente de novo.")

        else:
            return count


def partida():  # essa funcao n recebe parametros
    # numero de pecas inicial dispostas no tabuleiro
    num_valido = False
    n = int(input("Quantas peças? "))
    while not num_valido:
        print("Numero de peças inválido, digite um número válido")
        n = int(input("Quantas peças? "))
    if n > 0:
        num_valido = True
    else:
        if m >= 1:
            num_valido = True
            m = int(input("Limite de peças por jogada? "))
        else:
            print("Numero de peças inválido, digite um número válido")
            m = int(input("Limite de peças por jogada? "))

    num_valido = True

    computador_joga = True

    if n % (m + 1) != 0:  # Se o numero de peças do tabuleiro nao for multiplo de (m + 1), o computador começa
        print("\nComputador começa!")
    else:
        print("\nVoce começa!")  # Se for multiplo de (m + 1) o usuario começa
        computador_joga = False

    while (n > 0):  # Enqt tiver peças no tabuleiro, continue o jogo
        if computador_joga:
            qtd_pc_remover = computador_escolhe_jogada(n, m)
            print("O computador tirou %d peças. \n" % qtd_pc_remover)
            # Irá atualizar a quantidade de peças de acordo com a quantidade de peças que o computador removeu
            n = n - qtd_pc_remover
            computador_joga = False  # Flag que diz se o computador deve jogar a próxima rodada
        else:
            qtd_pc_remover = usuario_escolhe_jogada(n, m)
            print("Voce tirou %d peças. \n" % qtd_pc_remover)
            # Irá atualizar a quantidade de peças de acordo com a quantidade de peças que o usuario removeu
            n = n - qtd_pc_remover
            computador_joga = True  # Flag que diz se o computador deve jogar a próxima rodada

        if n != 0:  # Se a quantidade de peças restantes no tabuleiro for igual a 0, nao ira imprimir essa mensagem
            print("Agora restam", n, "peças no tabuleiro.")

    if computador_joga:  # Se o computador jogou por ultimo, quer dizer que ele ganhou, caso contrario quem venceu foi o usuario
        print("Fim do jogo! Voce ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")


jogador_venceu = False
pontuacao_jogador = 0
pontuacao_computador = 0

# Enquanto o placar de ambos os jogadores nao somarem juntos o valor 3, o laço continua
while pontuacao_jogador + pontuacao_computador != 3:
    if jogador_venceu is True:
        # pontuacao_jogador inicia-se zerada, somada a 1 caso o jogador venca uma rodada. E irá atualizando a cada rodada
        pontuacao_jogador = pontuacao_jogador + 1
    else:
        pontuacao_computador = pontuacao_computador + 1


def campeonato():  # Criada a funcao campeonato

    partida()  # chamada a funcao partida, a qual sera chamada 3 vezes
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você", pontuacao_jogador, "x",  # Ao final de todas as rodadas será impresso o placar final do jogo
          pontuacao_computador, "Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
partida_ou_campeonato = int(input(""))

if partida_ou_campeonato == 2:  # Se a opcao escolhida for campeonato = 2 será chamada a funcao campeonato
    print("Voce escolheu campeonato")
    campeonato()
else:  # Caso contrario sera chamada a funcao partida
    print("Voce escolheu partida")
    partida()


n = int(input("Quantas peças? "))
m = int(input("Limite de peças por jogada? "))
