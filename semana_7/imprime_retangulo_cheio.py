largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:  # Enquanto altura for maior que zero, o laço continua. Esse while comanda a altura do retangulo.
    # Altura recebe altura - 1, Aqui é onde ocorre a formacao da altura.
    altura = altura - 1
    aux = largura  # aux recebe a largura do retangulo.
    while aux > 0:  # Enquanto aux for maior que 0 o laço continua.
        # Printa # e o end coloca um espaço entre as cerquilhas que continuam sendo printadas na mesma linha.
        print("#", end='')
        # Aqui é onde é atualizado o numero de # a se formarem, p/ formar a largura.
        aux = aux - 1
    print("")  # Salta p/ a próxima linha.


# while altura > 0:
    # print(largura * '#')
    # altura = altura - 1
