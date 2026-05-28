#Testando a lógica e entendendo como o "input" conversa com o "float" lendo oque entra no teclado como caractere string e transformando em número real.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4

print("Média = ",media) #Utilizando String dentro do input e usando um separador para ter uma saída com String e valor real

#Bloco de decisão#
presenca = int(input("Digite a % da presenca (0 a 100) "))
passou_direto = (media >=7.0) and (presenca >= 75)

#Na lingua de computadores ( True = 1 False = 0 ) assim, podemos fazer uma condição usando este método sem utilizar uma função!
recado_reprovou = passou_direto == False
recado_passou = passou_direto == True
print("Parabéns por ter passado de ano! " * recado_passou)
print("Você não conseguiu passar, sinto muito! " * recado_reprovou)


cont = 0

while cont <= 9:
    print("Loop rodando! O contador atual é:", cont)
    cont = cont +1 # Quando contador chegar a 9 que seria cont = 9 <= 9 ele vira false e logo sairá do nosso loop.

print("O While chegou ao fim, pois a condição do contador agora é False!")
print("Valor final do contador na memória é : ", cont)
print("\n--- Iniciando o Teste do For ---")

# O range(0, 10) vai gerar os números de 0 até 9 automaticamente!
for contador_for in range(0, 10):
    print("For rodando! O contador atual é:", contador_for)

print("O for terminou de rodar perfeitamente!")
