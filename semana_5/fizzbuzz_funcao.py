def fizzbuzz(n):  # Criada a funcao fizzbuzz

    if n % 3 == 0 and not n % 5 == 0:
        return "Fizz"
    elif n % 5 == 0 and not n % 3 == 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n


n = int(input("Digite um número inteiro: "))
# print chama a funcao fizzbuzz que ira printar o resultado.
print(fizzbuzz(n))
