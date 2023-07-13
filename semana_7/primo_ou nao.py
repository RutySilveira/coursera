def éPrimo(x):  # definida a funcao que ira testar se é primo ou nao
    fator = 2  # O teste começa com o valor valendo 2, sendo o primeiro numero primo
    # Se utilizado para garantir que o resultado será true para o 2 e o 3 como primos.
    if x == 2 or x == 3:
        return True

    # Enqt o resto da divisao pelo fator for diferente de zero e o fator menor ou igual a divisao de x por 2. Se ambos verdadeiros o teste pelo fator 2 passou.
    while x % fator != 0 and fator <= x/2:
        # Soma-se 1 ao fator, para o teste continuar com outros numeros
        fator = fator + 1
        # Se o resto da divisao pelo fator for igual a zero, entao nao é primo e retorna false
        if x % fator == 0:
            return False
         # Senao, caso o resto da divisao nao seja igual a zero, entao retorna True para primo
        else:
            return True


n = int(input("Digite um número inteiro: "))

# Enquanto n maior que zero
while n > 0:
    # Se o resultado da funcao éPrimo retornar True, entao irá imprimir "é primo".
    if éPrimo(n):
        print(n, "é primo!")
     # Se o resultado da funcao éPrimo retornar False, entao irá imprimir "nao primo".
    else:
        print(n, "não é primo :-(")
    n = int(input("Digite um número inteiro: "))
