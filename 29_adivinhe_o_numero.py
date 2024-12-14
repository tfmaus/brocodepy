# Jogo Adivinhe o Número em Python

import random

num_baixo = 1
num_alto = 100
resposta = random.randint(num_baixo, num_alto)
palpites = 0
rodando = True

print("Jogo Adivinhe o Número em Python")
print(f"Selecione um número entre {num_baixo} e {num_alto}")

while rodando:
    palpite = input("Informe seu palpite: ")
    if palpite.isdigit():
        palpite = int(palpite)
        palpites += 1
        
        if palpite < num_baixo or palpite > num_alto:
            print("Este número está fora do escopo!")
            print(f"Por favor, selecione um número entre {num_baixo} e {num_alto}")
        elif palpite < resposta:
            print("Muito baixo! Tente novamente!")
        elif palpite > resposta:
            print("Muito alto! Tente novamente")
        else:
            print(f"Correto! A resposta é {resposta}")
            print(f"Número de palpites: {palpites}")
            rodando = False
    else:
        print("Palpite Inválido")
        print(f"Por favor, selecione um número entre {num_baixo} e {num_alto}")