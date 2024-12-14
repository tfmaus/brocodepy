# Conversor de Peso

peso = float(input("Informe o seu peso: "))
unidade = input("Kilos ou libras? (K ou L): ")

if unidade == "K":
    peso = peso * 2.205
    unidade = "lbs"
    print(f"Seu peso é: {round(peso,2)} {unidade}.")
elif unidade == "L":
    peso = peso / 2.205
    unidade = "kgs"
    print(f"Seu peso é: {round(peso,2)} {unidade}.")
else:
    print(f"{unidade} não é válido!")