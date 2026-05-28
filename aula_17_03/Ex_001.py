# ==============================================================================
# EXERCÍCIO 1: O Sistema de Frequência e Média (Estilo Aula PUCPR)
# Enunciado: Peça para o usuário digitar a sua "media_final" (float) e a sua
# "porcentagem_presenca" (int).
# Requisitos:
#  - Crie uma variável booleana chamada "aprovado". O aluno só é aprovado se
#    a média for maior ou igual a 7.0 E a presença for maior ou igual a 75.
#  - Imprima as mensagens "Parabéns, você passou!" ou "Sinto muito, você reprovou!"
#    na tela utilizando a nossa técnica de multiplicação de strings (sem usar if/else).
# ==============================================================================

# Digite o seu código do Exercício 1 aqui embaixo:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4 #Aqui obtemos a média das notas do aluno.
print(media)

presenca = int(input("Digite sua presença (0 a 100)"))
resultado = (media >=7.0) and (presenca >= 75)

print(resultado)

aprovado = resultado == True
reprovado = resultado == False
print("Parabéns, você foi aprovado!!" * aprovado)
print("Infelizmente você não passou.." * reprovado)