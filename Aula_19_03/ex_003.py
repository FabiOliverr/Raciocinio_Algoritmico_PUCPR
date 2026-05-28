# ==============================================================================
# EXERCÍCIO 3: Classificador de Alíquota de Imposto (Baseado na Página 18)
# Enunciado: Escreva um algoritmo que leia o salário de um funcionário e calcule
# o valor do desconto do imposto baseado na tabela do professor.
# Requisitos:
#  - Peça para o usuário digitar o "salario" (float). OK
#  - Se o salário for MENOR que 1257.13, o imposto é 0%. Exiba: "Isento de imposto." OK
#  - Se o salário for de 1257.13 até 2512.08, a alíquota é de 15%.
#    Calcule o desconto (salario * 15 / 100) e exiba: "Desconto de 15%: R$ [valor_do_desconto]"
#  - Se o salário for MAIOR que 2512.08, a alíquota é de 27.5%.
#    Calcule o desconto (salario * 27.5 / 100) e exiba: "Desconto de 27.5%: R$ [valor_do_desconto]"
#  - DICA: Use a estrutura if / elif / else para cobrir as três faixas salariais.
# ==============================================================================

salario_funcionario = float(input("Digite aqui o seu salário: "))
print("R$",salario_funcionario)

imposto_salario_menor = (salario_funcionario * 15) / 100
imposto_salario_maior = (salario_funcionario * 27.5) / 100
desconto_menor = (salario_funcionario - imposto_salario_menor)
desconto_maior = (salario_funcionario - imposto_salario_maior )

if salario_funcionario < 1257.13:
    print("Isento de Imposto.")
elif salario_funcionario >= 1257.13 and salario_funcionario <= 2512.08:
    print("A alíquota é de 15%")
    print("Desconto sobre seu salário aplicado no valor de R$",imposto_salario_menor)
    print("Seu saldo final após impostos é de R$",desconto_menor)
else:
    print("A alíquota é de 27.5%.")
    print("Desconto sobre seu salário aplicado no valor de R$",imposto_salario_maior)
    print("Seu saldo final após impostos é de R$",desconto_maior)

