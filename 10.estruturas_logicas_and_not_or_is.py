'''
Estrutura lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários
    - and, or, is

Para o 'and', ambos os valores precisam ser True.
Para o 'or', um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True = False e se for False = True
'''

ativo = True
logado = True


if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Voceê precisa ativar sua conta. Por favor, cheque seu e-mail')
