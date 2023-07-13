n = int(input("Digite um número inteiro: "))

soma = 0

while n > 0:  # Enqt maior que 0, continua o laço
    resto = n % 10  # resto recebe resto da divisao por 10
    n = n // 10  # n recebe valor da divisao inteira por 10

    soma = soma + resto  # soma recebe

print(soma)
