# Timer Contagem Regressiva

import time

tempo = int(input("Informe o tempo em segundos: "))

# for x in reversed(range(1, tempo)):
#     print(x)
#     time.sleep(1)

# # time.sleep(tempo)

# print("TIME IS UP!")

# for x in range(tempo, 0, -1):
#     print(x)
#     time.sleep(1)

# print("TIME IS UP!")

for x in range(tempo, 0, -1):
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)

print("TIME IS UP!")