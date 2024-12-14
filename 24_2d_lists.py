# frutas = ["maçã", "laranja", "banana", "côco"]
# vegetais = ["salsa", "cenouras", "batatas"]
# carnes = ["frango", "peixe", "peru"]

# compras = [frutas, vegetais, carnes]

# print(compras[0][0])

# for colecao in compras:
#     for comida in colecao:
#         print(comida, end=" ")
#     print()

teclado_num = ((1, 2, 3), 
               (4, 5, 6), 
               (7, 8, 9), 
               ("*", 0, "#"))

for linha in teclado_num:
    for num in linha:
        print(num, end=" ")
    print()