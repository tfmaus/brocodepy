# Programa Carrinho de Compras

comidas = []
precos = []
total = 0

while True:
    comida = input("Informe uma comida para comprar (S para sair): ")
    if comida.lower() == "s":
        break
    else:
        preco = float(input(f"Informe o preço de {comida}: R$"))
        comidas.append(comida)
        precos.append(preco)
        
print("----- SEU CARRINHO ------")

for comida in comidas:
    print(comida, end=" ")
    
for preco in precos:
    total = total + preco
    
print()
print(f"Seu total é: R${total}")