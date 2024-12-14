import random

opcoes = ("pedra", "papel", "tesoura")
rodando = True

while rodando:

    jogador = None
    computador = random.choice(opcoes)

    while jogador not in opcoes:
        jogador = input("Escolha entre (pedra, papel, tesoura): ")

    print(f"Jogador: {jogador}")
    print(f"Computador: {computador}")

    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você venceu!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você venceu!")
    elif jogador == "papel" and computador == "pedra":
        print("Você venceu!")
    else:
        print("Você perdeu!")

    if not input("Jogar novamente? (s/n): ").lower() == "s":
        rodando = False

print("Obrigado por jogar!")
