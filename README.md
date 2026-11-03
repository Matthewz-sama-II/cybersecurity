## Projeto 3 - Gerador de hash em Python
 
### Descrição
Programa de terminal em que o usuário digita um texto e escolhe um algoritmo (MD5, SHA-1, SHA-256 ou SHA-512). O programa retorna o hash em formato hexadecimal.
 
### Tecnologias
- Python 3 (biblioteca padrão `hashlib`, sem instalação adicional)
### Como executar
```bash
python projeto3_hash.py
```
 
### Exemplo
Entrada: `abc` com SHA-256
 
```
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```
 
### Conceitos demonstrados
- Um hash é determinístico: a mesma entrada gera sempre o mesmo resultado.
- Uma pequena alteração na entrada muda todo o hash (efeito avalanche).
- O hash é uma função de via única: não é possível reverter o resultado para o texto original.
- MD5 e SHA-1 são considerados fracos para uso em segurança. Para guardar senhas, recomenda-se usar salt e algoritmos lentos, como bcrypt ou argon2.
---
