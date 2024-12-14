# For Loops = executa um bloco de código um determinado número de vezes
#             Você pode iterar por faixa, string, sequência, etc.

# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)
    
# print("FELIZ ANO NOVO!")

# for x in range(1, 11, 3):
#     print(x)

# cartao = "1234-5678-9012-3456"

# for x in cartao:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue # pula essa iteração
#     else:
#         print(x)
        
for x in range(1, 21):
    if x == 13:
        break # pára na iteração anterior
    else:
        print(x)
    