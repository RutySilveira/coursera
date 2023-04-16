numero_converter = int(
    input("Digite o numero em segundos que deseja converter: "))

dias = int(numero_converter // 86400)

horas = int((numero_converter % 86400) / 3600)

minutos = int((numero_converter % 3600) / 60)

segundos = int(numero_converter % 60)

print(dias, "dias,", horas, "horas,", minutos,
      "minutos e", segundos, "segundos.")
