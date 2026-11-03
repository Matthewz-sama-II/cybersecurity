# Projeto 3 - Gerador de hash em Python
# O usuário digita um texto e o programa retorna o hash dele.

import hashlib

# Algoritmos disponíveis no menu
ALGORITMOS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512",
}


def gerar_hash(texto, algoritmo="sha256"):
    """Recebe um texto e devolve o hash em formato hexadecimal."""
    objeto_hash = hashlib.new(algoritmo)
    objeto_hash.update(texto.encode("utf-8"))  # o hash trabalha com bytes
    return objeto_hash.hexdigest()


def escolher_algoritmo():
    """Mostra o menu e devolve o nome do algoritmo escolhido (padrão: SHA-256)."""
    print("\nEscolha o algoritmo:")
    for numero, nome in ALGORITMOS.items():
        print(f"  {numero} - {nome.upper()}")
    escolha = input("Opção [3]: ").strip()
    return ALGORITMOS.get(escolha, "sha256")


def main():
    print("=== Gerador de Hash ===")

    while True:
        texto = input("\nDigite o texto: ")
        algoritmo = escolher_algoritmo()
        resultado = gerar_hash(texto, algoritmo)

        print(f"\nTexto: {texto}")
        print(f"Algoritmo: {algoritmo.upper()}")
        print(f"Hash: {resultado}")
        print(f"Tamanho: {len(resultado)} caracteres hexadecimais")

        outra = input("\nGerar outro hash? (s/n): ").strip().lower()
        if outra != "s":
            print("Encerrando.")
            break


if __name__ == "__main__":
    main()