#Imagine que você tem duas variáveis já preenchidas no sistema:valor_dolar (quantos dólares o cliente quer converter)cotacao_atual (que hoje vale 5.20)
#Usando os operadores matemáticos ( + , - , * , / ), como você digitaria a linha de código completa para calcular
#essa conversão e guardar o resultado final dentro de uma variável chamada valor_real?

valor_dolar = int(50)
cotacao_atual = float(5.20)
conversao_BRL = cotacao_atual * valor_dolar
print("A conversão em BRL é : " + str(conversao_BRL))