'''
Esccopo de variaveis

[                           ]

Dois casos de escopos:

1 - Varoáveis globais:
  - Variáveis globais são reconhecidaas, ou seja, seu escopo compreende, todo o programa

2 - Variáveis locais:
  - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
  está limitado ao bloco onde foi declarado

Para declarar variáveis em Python fazemos:

nome_de_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma varável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42
'''

numero = 42
print(numero)
print(type(numero))


nome = 'Hello, world.'
print(nome)
print(type(nome))

nao_existo = 'Olá'
print(nao_existo)

numero = 35
# novo = 0

if numero > 10:
    novo = numero + 10  # A variavel 'novo' está declarada localmente dentro do bloco de if. Portanto, é local
    print(novo)

# print(novo)
