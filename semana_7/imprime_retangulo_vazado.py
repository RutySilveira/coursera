largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux = altura
while aux > 0:
    if aux == 1 or aux == altura:
        print(largura * '#')
    else:
        print("#", ((largura - 4) * " "), "#")

    aux = aux - 1
