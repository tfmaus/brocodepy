# Operadores lógicos = avaliam múltiplas funções (or, and, not)
#                      or = pelo menos uma condição deve ser True
#                      and = ambas condições devem ser True
#                      not = invert a condição (not False, not True)

# OR
# temp = 20
# chovendo = True

# if temp > 35 or  temp < 0 or chovendo:
#     print("O evento ao ar livre está cancelado.")
# else:
#     print("O evento ao ar livre está agendado.")

# AND
# temp = 20
# ensolarado = True

# if temp >= 28 and ensolarado:
#     print("Está calor la fora!")
#     print("Está ensolarado!")
# elif temp <= 0 and ensolarado:
#     print("Está frio lá fora!")
#     print("Está ensolarado!")
# elif temp < 28 and temp > 0 and ensolarado:
#     print("Está agradável lá fora!")
#     print("Está ensolarado!")

# NOT
# temp = 20
# ensolarado = False

# if temp >= 28 and not ensolarado:
#     print("Está calor la fora!")
#     print("Está nublado!")
# elif temp <= 0 and not ensolarado:
#     print("Está frio lá fora!")
#     print("Está nublado!")
# elif temp < 28 and temp > 0 and not ensolarado:
#     print("Está agradável lá fora!")
#     print("Está nublado!")