# ==============================================================================
# EXERCÍCIO 3: O Desconto do Cinema (Baseado no Slide 16 do PDF)
# Enunciado: Um cinema oferece desconto baseado na idade do cliente. Peça para o
# usuário digitar a sua "idade" (int).
# Requisitos:
#  - O cliente tem direito a meia-entrada se a idade for MENOR que 12 OU se a
#    idade for MAIOR OU IGUAL a 60.
#  - Crie a variável booleana "meia_entrada" que junte essas duas condições usando
#    o operador lógico correto (and ou or).
#  - Imprima na tela o resultado: "Tem direito a meia-entrada? [True/False]"
# ==============================================================================

# Digite o seu código do Exercício 3 aqui embaixo:

nome_cliente = input("Digite o seu nome: ")
idade_cliente = int(input("Digite sua idade: "))

print(nome_cliente)
print(idade_cliente)

validacao_idade = (idade_cliente < 12 or idade_cliente >= 60)
print(validacao_idade)

meia_entrada = (validacao_idade == True)
bonus_negado = (validacao_idade == False)

print("Obrigado por escolher nosso estabelecimento, aqui está sua meia entrada!" * meia_entrada)
print("Devido não atender requisitos, informamos que o bônus não será aplicado!"* bonus_negado)