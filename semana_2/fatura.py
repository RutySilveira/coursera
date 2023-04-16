nome = input("Digite o nome do cliente: ")

dia_vencmt = int(input("Digite o dia de vencimento: "))

mes = input(str("Digite o mês de vencimento: "))

valor_fat = input("Digite o valor da fatura: ")

print("Olá,", nome)

print(
    'A sua fatura com vencimento em', dia_vencmt, 'de',
    mes, 'no valor de R$', valor_fat, 'está fechada.'
)
