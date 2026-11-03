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

## Projeto 4 - Ataque de força bruta (exercício didático)
 
### Descrição
Exercício prático para demonstrar por que senhas curtas e simples são uma vulnerabilidade de segurança. O script gera combinações de caracteres com `itertools.product`, testa cada uma contra uma senha "alvo" definida no próprio código e exibe o progresso até encontrá-la, contando o número de tentativas e o tempo decorrido.
 
> Uso restrito a ambiente de estudo: o script testa apenas uma senha definida pelo próprio autor, dentro do código. Não deve ser usado contra contas, sistemas ou senhas de terceiros.
 
### Tecnologias
- Python 3 (bibliotecas padrão `itertools` e `time`, sem instalação adicional)
### Como executar
```bash
python projeto4_forca_bruta.py
```
Para testar outros cenários, altere no início do script:
- `caracteres`: o conjunto de caracteres a testar (ex.: `"abc"`, letras minúsculas, letras + números).
- `senha_alvo`: a senha que o script deve encontrar.
- `tamanho_maximo`: o maior tamanho de senha testado.
### Testes realizados
| Caracteres | Tamanho máximo | Tentativas até achar | Tempo |
|---|---|---|---|
| `"abc"` (3) | 2 | 5 | ~0s |
| `"abc"` (3) | 3 | 10| ~0s |
| `"abcdefghij"` (10) | 3 | 15 | ~1s |
| `"abcdefghijklmnopqrstuvwxyz"` (26) | 4 | 20 | ~2s |

### Conceitos demonstrados
- O número de combinações cresce exponencialmente: (quantidade de caracteres) elevado ao tamanho da senha. Pequenos aumentos no tamanho ou na variedade de caracteres (minúsculas, maiúsculas, números, símbolos) tornam a busca exaustiva muito mais lenta.
- É esse crescimento exponencial que protege senhas longas e complexas: o tempo necessário para testar todas as combinações se torna proibitivo.
- Senhas reais, protegidas por hash e salt (ver Projeto 3), são ainda mais resistentes a esse tipo de ataque: o atacante precisaria gerar o hash de cada tentativa e compará-lo ao hash salvo, o que é computacionalmente mais caro. Algoritmos como bcrypt e argon2 são projetados para serem propositalmente lentos, o que torna a força bruta inviável na prática.
---
 
## Segurança
 
- Nenhuma chave de API ou credencial está armazenada neste repositório.
- Os experimentos de cibersegurança (Projetos 3 e 4) foram realizados apenas em ambiente de estudo, com senhas e dados criados pelo próprio autor. O script do Projeto 4 não deve ser usado contra contas, sistemas ou senhas de terceiros.
 
