# Conversos Temperatura

unidade = input("Temperatura está em Celcius ou Fahrenheit? (C/F)? ")
temp = float(input("Informe a temperatura: "))
    
if unidade == "C":
    temp = (temp * 1.8) + 32
    unidade = "°F"
    print(f"A temperatura é {round(temp,2)}{unidade}")
elif unidade == "F":
    temp = (temp - 32) * 0.5555
    unidade = "°C"
    print(f"A temperatura é {round(temp,2)}{unidade}")
else:
    print(f"{unidade} não é unidade de temperatura válida!")
    
    