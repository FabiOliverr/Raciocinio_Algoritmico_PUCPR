# ==============================================================================
# EXERCÍCIO 1: Permissão para Dirigir (Baseado na Página 15 e 16 do PDF)
# Enunciado: Desenvolva um programa que avalie se uma pessoa pode dirigir.
# Requisitos:
#  - Peça para o usuário digitar a "idade" (int).
#  - Se a idade for MAIOR OU IGUAL a 18, exiba a mensagem: "Pode dirigir!"
#  - Se a idade for MENOR que 18, calcule quantos anos faltam para ela completar 18
#    e exiba: "Não pode dirigir! Faltam X anos para você poder tirar a carteira."
#  - Use a estrutura if/else padrão.
# ==============================================================================

# Digite o seu código do Exercício 1 aqui embaixo:

idade_motorista = int(input("Qual a sua idade? "))
print(idade_motorista)

if idade_motorista >= 18:
    print("Pode dirigir!, mas com cuidado!")
else:
    idade_faltante = (18 - idade_motorista)
    print("Espere um pouco, ainda falta", idade_faltante, " ano para você poder dirigir!")