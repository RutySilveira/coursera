
meu_cartao = int(input("Digite o número do seu cartão de crédito: "))

cartao_lido = 1
# Pois inicialmente n encontrei na lista, ent False, pois o while deve continuar ate encontrar, sendo ent true
cartao_na_lista = False

# Enqt o cartao lido for diferente de zero e enqt nao encontrar o cartao_na_lista
while cartao_lido != 0 and not cartao_na_lista:
    cartao_lido = int(input("Digite o número do próximo cartão: "))
    if cartao_lido == meu_cartao:
        cartao_na_lista = True  # indicador de passagem

if cartao_na_lista:
    print("EBA!!! Meu cartão está na lista.")
else:
    print("Xi, meu crtão não está na lista.")
