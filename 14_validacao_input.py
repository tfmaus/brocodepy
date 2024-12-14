# Exercício de Validação de Inputs de Usuário
# 1 - nome de usuário não tem mais de 12 caracteres
# 2 - nome de usuário não deve conter espaços
# 3 - nome de usuário não deve conter dígitos

username = input("Informe o usuário: ")

username.find(" ") # se nenhum espaço for encontrado, retorna -1

if len(username) > 12:
    print("Seu nome de usuário não pode ter mais de 12 caracteres.")
elif not username.find(" ") == -1:
    print("Seu nome de usuário não pode conter espaços.")
elif not username.isalpha():
    print("Seu nome de usuário deve conter apenas letras.")
else:
    print(f"Seja bem-vindo, {username}!")