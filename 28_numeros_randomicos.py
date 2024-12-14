import random

baixo = 1
alto = 100
opcoes = ("pedra", "papel", "tesoura")
cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(baixo, alto)
# number = random.random()
# opcao = random.choice(opcoes)
random.shuffle(cartas)

print(cartas)