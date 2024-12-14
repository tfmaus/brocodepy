# While Loops = executa algum código enquanto a condição permanecer True

# nome = input("Informe seu nome: ")

# 1:
# while nome == "":
#     print("Você não informou o seu nome!")
#     nome = input("Informe seu nome: ")

# print(f"Olá, {nome}!")

# 2:
# idade = int(input("Informe sua idade: "))

# while idade < 0:
#     print("Você não pode informar uma idade negativa!")
#     idade = int(input("Informe sua idade: "))
    
# print(f"Você tem {idade} anos de idade!")

# 3:
# comida = input("Informe sua comida favorita (S para SAIR): ")

# while not comida == "S":
#     print(f"Você gosta de {comida}")
#     comida = input("Informe outra comida que você gosta (S para SAIR): ")

# print("tchau!")

# 4:
num = int(input("Informe um número entre 1 e 10: "))

while num < 1 or num > 10:
    print(f"O número {num} não é válido!")
    num = int(input("Informe um número entre 1 e 10: "))
    
print(f"Você escolheu o número {num}!")
