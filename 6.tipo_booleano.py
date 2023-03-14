'''
Tipo Boleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False - > Falso

Obs: Sempre com a inicial maiúscula

Errado:
 true, false

 Certo:
 True, False
'''

logado = False
ativo = True
print(f'B1 -> {ativo}')
print(f'B2 -> {logado}')

'''
Operações básicas:
'''

# NEGAÇÃO: NÃO(NOT)

'''
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
'''
print(f'A NEGAÇÃO de B1 é: {not(ativo)}')

print(f'A NEGAÇÃO de B2 é: {not(logado)}')




# DISJUNÇÃO: OU(OR)

'''
É UMA OPERAÇÃO BINÁRIA, OU SEJA, DEPENDE DE DOIS VALORES. oU UM OU OUTRO DEVE SER VERDADEIRO.
'''
print(f'A DISJUNÇÃO de B1 e B2 é : {ativo or logado}')



# CONJUNÇÃO: E(AND)

'''
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros
'''
print(f'A CONJUNÇÃO de B1 e B2 é : {ativo and logado}')

