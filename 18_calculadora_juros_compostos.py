# Calculadora de Juros Compostos

principal = 0
taxa = 0
tempo = 0

# while principal <= 0:
#     principal = float(input("Informe o valor inicial: "))
#     if principal <= 0:
#         print("Valor inicial não pode ser menor ou igual a zero!")
        
# while taxa <= 0:
#     taxa = float(input("Informe a taxa de juros: "))
#     if taxa <= 0:
#         print("A taxa de juros não pode ser menor ou igual a zero!")
        
# while tempo <= 0:
#     tempo = int(input("Informe o período: "))
#     if tempo <= 0:
#         print("O período não pode ser menor ou igual a zero!")
        
# montante = principal * pow((1 + taxa / 100), tempo)
    
# print(f"O montante depois de {tempo} anos é de R${round(montante,2): ,}")

while True:
    principal = float(input("Informe o valor inicial: "))
    if principal < 0:
        print("Valor inicial não pode ser menor ou igual a zero!")
    else:
        break
        
while True:
    taxa = float(input("Informe a taxa de juros: "))
    if taxa < 0:
        print("A taxa de juros não pode ser menor ou igual a zero!")
    else:
        break
        
while True:
    tempo = int(input("Informe o período: "))
    if tempo < 0:
        print("O período não pode ser menor ou igual a zero!")
    else:
        break
        
montante = principal * pow((1 + taxa / 100), tempo)
    
print(f"O montante depois de {tempo} anos é de R${round(montante,2): ,}")