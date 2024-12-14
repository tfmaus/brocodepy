# Especificadores de formato = {value:flags} formatam um valor com base nas flags inseridas

# .(number)f = arredonda para o número de casas decimais (ponto fixo)
# :(number) = aloca o número de espaços
# :03 = aloca zeros aos espaços
# :< = justifica à esquerda
# :> = justifica à direita
# :^ = alinha ao centro
# :+ = usa sinal de mais para indicar valor positivo
# := = posiciona sinal à posição mais a esquerda
# :  = insere um espaço antes de números positivos
# :, = separador milhar vírgula

preco1 = 3000.14159
preco2 = -9870.65
preco3 = 1200.34

print(f"Preço 1 é R${preco1:+,.2f}")
print(f"Preço 2 é R${preco2:+,.2f}")
print(f"Preço 3 é R${preco3:+,.2f}")