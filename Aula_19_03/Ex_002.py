# ==============================================================================
# EXERCÍCIO 2: Verificador de Saldo Bancário (Baseado na Página 15 do PDF)
# Enunciado: Crie um simulador de conta corrente que avise o cliente sobre o saldo.
# Requisitos:
#  - Peça para o usuário digitar o "saldo_atual" (float).
#  - Se o saldo for MAIOR OU IGUAL a 0, exiba a mensagem: "Saldo positivo! Conta regular."
#  - Se o saldo for MENOR que 0, exiba: "Atenção! Seu saldo está negativo: R$ [saldo_atual]"
#  - Use a estrutura if/else padrão.
# ==============================================================================

# Digite o seu código do Exercício 2 aqui embaixo:

seu_saldo = float(input("Qual o seu saldo? "))
print("R$",seu_saldo)

if seu_saldo >= 0:
    print("Saldo positivo! Conta regular.")
else:
    print("Atenção! Seu saldo está negativo: R$",seu_saldo)