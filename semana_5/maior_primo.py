# funcao criada p/ verificar se é primo ou nao.Se primo retorna True, se nao primo retorna False.
def éPrimo(n):

    if n != 2 and n % 2 == 0:
        return False
    elif n != 3 and n % 3 == 0:
        return False
    elif n != 5 and n % 5 == 0:
        return False
    elif n != 7 and n % 7 == 0:
        return False
    else:
        return True


def maior_primo(n):  # funcao criada p/ verificar o maior numero primo
    while n >= 2:  # Enqt n for maior ou igual a 2, o laço continua
        if n <= 2:  # Se n for menor ou igual a 2, retorno o valor 2
            return 2
        if éPrimo(n):  # Se o n for primo, irei retorna-lo
            return n
        # Retorno o valor atual de n - 1 e continuo o laço.
        return maior_primo(n - 1)


n = int(input("Digite um número inteiro: "))
# Print chama a funcao maior_primo(n) com o valor atual de n, sendo o maior primo
print(maior_primo(n))
