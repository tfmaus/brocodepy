# Dicionário = um coleção de pares de {key:value}
#              ordenado e mutável. Sem duplicatas          

capitais = {"USA":"Washington D.C.", 
            "Índia":"Nova Delhi", 
            "China":"Pequim", 
            "Rússia":"Moscou"}

# print(dir(capitais))
# print(help(capitais))

# print(capitais.get("Índia"))

# if capitais.get("Rússia"):
#     print("Essa capital existe.")
# else:
#     print("Essa capital não existe.")

# capitais.update({"Alemanha":"Berlim"})
# capitais.update({"USA":"Detroit"})
# capitais.pop("China")
# capitais.popitem() # Remove o último item inserido no dicionário
# capitais.clear() # Limpa o dicionário

# keys = capitais.keys()
# values = capitais.values()

# for key in capitais.keys():
#     print(key)

# for value in capitais.values():
#     print(value)

items = capitais.items()
for key, value in capitais.items():
    print(f"{key}: {value}")