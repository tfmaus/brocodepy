# Programa Estande de Concessão

# Dicionário {key:value}

menu = {"pizza": 3.00, 
        "nachos": 4.50,
        "pipoca": 6.00,
        "batata frita": 2.50,
        "salgadinhos": 1.00,
        "pretzel": 3.50,
        "refrigerante": 3.00,
        "limonada": 4.25}

cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:12}: R${value:.2f}")
print("--------------------")

while True:
    comida = input("Selecione um item (s para Sair): ").lower()
    if comida == "s":
        break
    elif menu.get(comida) is not None:
        cart.append(comida)

print("------SEU PEDIDO------")
for comida in cart:
    total += menu.get(comida)
    print(comida, end=" ")

print()
print(f"Total é: R${total:.2f}")