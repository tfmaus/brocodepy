import math

# amigos = 10

# amigos = amigos + 1
# amigos += 1
# amigos = amigos - 2
# amigos -= 2
# amigos = amigos * 3
# amigos *= 3
# amigos = amigos / 2
# amigos /= 2
# amigos = amigos ** 2
# amigos **= 2
# remainder = amigos % 3

# print(remainder)

# x = 3.14
# y = 4
# z = 5

# resultado = round(x) # arredondar
# resultado = abs(y) # valor absoluto, distância de zero como número inteiro
# resultado = pow(y, 3) # base e expoente
# resultado = max(x,y,z) # valor máis alto
# resultado = min(x,y,z) # valor mais baixo

# print(resultado)

# x = 9.9

# print(math.pi)
# print(math.e)
# resultado = math.sqrt(x) # raiz quadrada
# resultado = math.ceil(x) # arredonda float para cima
# resultado = math.floor(x) # arredonda float para baixo

# print(resultado)

# Exercício 1 - Circunferência de um Círculo
# C = 2*pi*r

# raio = float(input("Informe o raio do círculo: "))

# circunferencia = 2 * math.pi * raio

# print(f"A circunferência do círculo é {round(circunferencia,2)}cm")

# Exercício 2 - Área de um Círculo
# A = pi * r²

# area = math.pi * pow(raio,2)

# print(f"A área do círculo é {round(area,2)}cm²")

#Exercício 3 - Hipotenusa

lado_a = float(input("Informe a medida de A: "))
lado_b = float(input("Informe a medida de B: "))

hipotenusa = math.sqrt(pow(lado_a,2)+pow(lado_b,2))

print(f"A hipotenusa é {round(hipotenusa,2)}cm")
