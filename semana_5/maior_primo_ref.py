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


def maior_primo(n):
    if n <= 2:
        return 2

    if éPrimo(n):
        return n
    return maior_primo(n - 1)


n = int(input("Digite um número inteiro: "))
print(maior_primo(n))
