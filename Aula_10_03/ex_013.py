# 10. Desafio Final: Crie um mini-programa de 3 linhas.
# Linha 1: Pergunte o preco_original do produto (use input e converta para float).
# Linha 2: Calcule o preco_com_desconto (tirando 10% do valor).
# Linha 3: Mostre (print) o novo valor na tela.

preco_original = float(input("Qual o valor do produto ? "))
desconto = int(10)
#Desconto aplicado sobre o produto.
desconto_produto = (desconto / 100) * preco_original
#Valor do produto - o desconto para saber quanto o cliente pagará.
preco_final = preco_original - desconto_produto
print("O valor do produto é : "+ str(preco_original) + " e com o desconto de 10%  ficou : "+ str(preco_final))