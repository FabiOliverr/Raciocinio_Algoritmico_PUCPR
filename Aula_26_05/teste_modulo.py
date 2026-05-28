# ==============================================================================
# EXPERIMENTO: Entendendo o Escopo antes dos Módulos
# ==============================================================================

# Esta é uma variável GLOBAL
nome_global = "Fábio"

# Aqui estamos criando o nosso primeiro módulo bem simples!
def meu_primeiro_modulo():
    # Esta é uma variável LOCAL (só existe aqui dentro)
    nome_local = "Professor Emerson"
    print("Dentro do módulo eu vejo o:", nome_local)
    print("Dentro do módulo eu também vejo o:", nome_global)

# --- PROGRAMA PRINCIPAL ---
# Chamando o módulo para ele rodar
meu_primeiro_modulo()

print("Fora do módulo eu vejo o:", nome_global)

# ATENÇÃO: Descomente a linha abaixo para ver o Python dar um erro!
# print(nome_local)