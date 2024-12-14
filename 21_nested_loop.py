# Nested Loop = um loop dentro de outro loop (outer, inner)
#             outer loop:
#               inner loop: 
# while dentro de while; for dentro de for; for dentro de while; while dentro de for...

linhas = int(input("Informe o número de linhas: "))
colunas = int(input("Informe o número de colunas: "))
simbolo = input("Informe um símbolo: ")

for x in range(linhas):
    for y in range(colunas):
        print(simbolo, end="") # alinha lado a lado e pode colocar algum caractere
    print()