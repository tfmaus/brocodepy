# Coleções = variável usada para armazenar múltiplos valores
# Lista = [] ordenada e alterável. Duplicatas OK
# Set   = {} desordenada e imutável, mas pode adicionar e remover. Sem Duplicatas
# Tupla = () ordenada e inalterável. Duplicatas OK. Mais rápida


# frutas = ["maçã", "laranja", "banana", "côco"] # lista
# frutas = {"maçã", "laranja", "banana", "côco"} # set
frutas = ("maçã", "laranja", "banana", "côco", "côco") # tupla

# COMANDOS LISTA []

# print(dir(frutas))
# print(help(frutas))
# print(len(frutas))

# print("maçã" in frutas)

# frutas[1] = "abacaxi"
# frutas.append("abacaxi") # .append inclui elementos ao final da lista
# frutas.remove("maçã")
# frutas.insert(0, "abacaxi") # .insert insere o elemento no índice definido
# frutas.sort() # ordem alfabética
# frutas.reverse() # ordem reversa com base na lista original
# frutas.clear()
# print(frutas.index("côco")) # mostra a posição do elemento na lista
# print(frutas.count("abacaxi")) # conta o número de determnados elementos

# COMANDOS SET {}

# print(dir(frutas))
# print(help(frutas))
# print(len(frutas))

# print("maçã" in frutas)

# frutas.add("abacaxi")
# frutas.remove("banana")
# frutas.pop() # remove o primeiro elemento que aparecer (aleatório)
# frutas.clear()

# COMANDOS TUPLA ()

# print(dir(frutas))
# print(help(frutas))
# print(len(frutas))

# print("maçã" in frutas)

# print(frutas.index("maçã"))
print(frutas.count("côco"))

# print(frutas[1])

# for fruta in frutas:
print(frutas)