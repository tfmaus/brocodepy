# Calculadora Python

operador = input("Informe uma uma operação (+ - * /): ")
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if operador == "+":
    resultado = num1 + num2
    print(round(resultado,3))
elif operador == "-":
    resultado = num1 - num2
    print(round(resultado,3))
elif operador == "*":
    resultado = num1 * num2
    print(round(resultado,3))
elif operador == "/":
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = num1 / num2
        print(round(resultado,3))
else:
    print(f"{operador} não é um operador válido!")