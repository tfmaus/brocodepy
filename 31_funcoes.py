# Função = um bloco de código reusável
#          coloque () depois do nome da função para invocá-la

# def happy_bithday(nome, idade):
#     print(f"Happy birthday to {nome}!")
#     print(f"Você tem {idade} anos!")
#     print("Happy birthday to you!")
#     print()

# happy_bithday("Bro", 20)
# happy_bithday("Steve", 30)
# happy_bithday("Joe", 40)

# def mostrar_fatura(usuario, total, data):
#     print(f"Olá {usuario}")
#     print(f"Sua fatura de R${total:.2f} vence em {data}")

# mostrar_fatura("BroCode", 42.50, "01/01/2025")

# return = declaração usada para encerrar uma função
#          e enviar um resultado de volta ao solicitante

# def soma(x, y):
#     z = x + y
#     return z

# def subtrai(x, y):
#     z = x - y
#     return z

# def multiplica(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(soma(1, 2))
# print(subtrai(1, 2))
# print(multiplica(1, 2))
# print(divide(1, 2))

def criar_nome(nome, sobrenome):
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    return nome + " " + sobrenome

nome_completo = criar_nome("bro", "code")

print(nome_completo)