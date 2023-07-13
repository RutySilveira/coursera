def n_primos(number):  # Criada a funcao n_primos.
    count = 0  # Para contar a quantidade de numeros primos encontrados.

    while number >= 2:  # Entra no loop enquanto number maior ou igual a 2.
        # Variavel auxiliar p/ verificar se é primo, e vai incrementando até a metade do numero recebido.
        aux = 2
        ehPrimo = True  # Variavel que indica se o numero é primo, comecando com True

        # Enquanto o número é primo e o auxiliar nao ultrapassar metade no numero.
        while ehPrimo and aux <= number / 2:
            if number % aux == 0:  # Se o resto da dvivisao for igual a zero.
                ehPrimo = False  # Então não é um numero primo.
            aux = aux + 1  # Incrementa em 1 o auxiliar.

        if ehPrimo:  # Se é primo for True, então o numero é primo.
            count = count + 1  # Incrementa 1 na contagem dos números primos.

        number = number - 1  # Decrementa o numero, para continuar os testes

    return count  # Retorna a contagem dos números primos.


number = int(input("Digite um numero maior ou igual a 2: "))
print(n_primos(number))
