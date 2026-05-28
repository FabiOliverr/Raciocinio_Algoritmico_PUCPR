# ==============================================================================
# EXERCÍCIO 2: O Radar da Polícia (Estilo Slide 20)
# Enunciado: Peça para o usuário digitar a "velocidade_carro" (int).
# Requisitos:
# - Crie uma variável booleana chamada "levar_multa", que será True caso a
#   velocidade do carro seja MAIOR que 80.
# - Crie outra variável booleana chamada "isento_multa", que será o inverso da primeira.
# - Exiba a mensagem "Você foi multado por excesso de velocidade!" multiplicada
#   por "levar_multa" e a mensagem "Velocidade segura. Boa viagem!" multiplicada
#   por "isento_multa" (sem usar if/else).
# ==============================================================================

# Digite o seu código do Exercício 2 aqui embaixo:

velocidade_carro = int(input("Digite a velocidade do carro: "))

print("Velocidade do carro: ", velocidade_carro)

alta_velocidade = (velocidade_carro > 80)
isento_multa = (velocidade_carro <= 80)

Recebe_multa = (alta_velocidade == True)
Recebe_isencao = (isento_multa == True)

print("Está rápido demais!! Vai receber uma multa!" * Recebe_multa)
print("Está seguindo as regras, pode ir sem multas!"* Recebe_isencao)