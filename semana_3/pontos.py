import math

x_a = int(input("Digite a coordenada de x do ponto A: "))
y_a = int(input("Digite a coordenada de y do ponto A: "))

x_b = int(input("Digite a coordenada de x do ponto B: "))
y_b = int(input("Digite a coordenada de y do ponto B: "))

dif_x_quad = (x_a - x_b) ** 2
dif_y_quad = (y_a - y_b) ** 2
distancia = float(math.sqrt(dif_x_quad + dif_y_quad))

if distancia >= 10:
    print("longe")
else:
    print("perto")
