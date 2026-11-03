# Projeto 4 - Ataque de força bruta (exercício didático)
#
# Objetivo: mostrar, na prática, por que senhas curtas e simples são
# inseguras. O programa testa combinações de caracteres até encontrar
# uma senha "alvo" definida pelo próprio usuário, no próprio script.
#
# Uso previsto: ambiente de estudo, testando apenas senhas que você
# mesmo definiu abaixo. Não use este código contra contas, sistemas
# ou senhas de terceiros.

import itertools
import time

# 1. Conjunto de caracteres a testar
caracteres = "abc"

# 2. Senha alvo (defina aqui, dentro do próprio script, só para teste)
senha_alvo = "ca"

# Tamanho máximo de senha a tentar
tamanho_maximo = 3


def forca_bruta(caracteres, alvo, tamanho_maximo):
    tentativas = 0
    inicio = time.time()

    # repeat=1 testa senhas de 1 caractere, depois 2, até o tamanho_maximo
    for tamanho in range(1, tamanho_maximo + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativas += 1
            tentativa = "".join(combinacao)  # transforma a tupla em string
            print(f"Tentativa {tentativas}: {tentativa}")

            if tentativa == alvo:
                duracao = time.time() - inicio
                print(f"\nSenha encontrada: '{tentativa}'")
                print(f"Tentativas necessárias: {tentativas}")
                print(f"Tempo decorrido: {duracao:.4f} segundos")
                return tentativa, tentativas, duracao

    print("\nSenha não encontrada dentro do tamanho máximo definido.")
    return None, tentativas, time.time() - inicio


if __name__ == "__main__":
    print("=== Ataque de força bruta (exercício didático) ===")
    print(f"Conjunto de caracteres: '{caracteres}'")
    print(f"Tamanho máximo testado: {tamanho_maximo}\n")
    forca_bruta(caracteres, senha_alvo, tamanho_maximo)