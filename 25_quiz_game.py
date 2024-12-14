# Quiz Game em Python

perguntas = ("Quantos elementos existem na tabela periódica dos elementos? ", 
             "Qual animal que põe os maiores ovos? ", 
             "Qual o gás mais abundante na atmosfera da Terra? ", 
             "Quantos ossos tem o corpo humano? ", 
             "Qual o planeta mais quente no sistema solar? ")

opcoes = (("A. 116", "B. 117", "C. 118", "D. 119"), 
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"), 
          ("A. Nitrogênio", "B. Oxigênio", "C. Dióxido de Carbono", "D. Hidrogênio"), 
          ("A. 206", "B. 207", "C. 208", "D. 209"), 
          ("A. Mercúrio", "B. Vênus", "C. Terra", "D. Marte"))

respostas = ("C", "D", "A", "A", "B")
palpites = []
placar = 0
num_pergunta = 0

for pergunta in perguntas:
    print("-----------------")
    print(pergunta)
    for opcao in opcoes[num_pergunta]:
        print(opcao)
    palpite = input("Escolha (A, B, C, D): ").upper()
    palpites.append(palpite)
    if palpite == respostas[num_pergunta]:
        placar += 1
        print("Correto!")
    else:
        print("Incorreto!")
        print(f"{respostas[num_pergunta]} é a resposta correta!")
    num_pergunta += 1

print("-----------------")
print("    RESULTADO    ")
print("-----------------")

print("Respostas: ", end="")
for resposta in respostas:
    print(resposta, end=" ")
print()

print("Palpites: ", end="")
for palpite in palpites:
    print(palpite, end=" ")
print()

placar = int(placar / len(perguntas) * 100)
print(f"Seu placar é {placar}%")