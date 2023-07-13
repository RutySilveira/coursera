def vogal(n):  # Criada a funcao vogal
    vogais = ("a", "e", "i", "o", "u", "A", "E",
              "I", "O", "U")  # lista de vogais

    if n in vogais:  # in serve para analisar se n esta contindo na lista vogais
        return True
    else:
        return False


n = input("Digite uma letra: ")  # Recebo uma letra
print(vogal(n))  # a funcao print chama a funcao vogal
