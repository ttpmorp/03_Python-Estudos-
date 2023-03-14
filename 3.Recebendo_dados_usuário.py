'''
Redebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:
- Aspas simples:
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;


Exemplos:
- Aspas simples -> 'Julia Cristinny'
- Aspas duplas -> "Julia Cristinny"
- Aspas simples triplas ->
'''


# Entrada de dados
# print("Qual seu nome?")
# nome = input()  # Input -> Entrada

nome = input('Qual o seu nome? ')


# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a), %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
# print(f'Seja bem-vindo(a), {nome}')


# print("Qual a sua idade?")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento


# Saída de dados
# Exemplo de print 'antigo' 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos'.format(nome, idade))

# # Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade}')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.

print(f'A {nome} nasceu em {2022 - int(idade)}') -> Utilizar apenas quando entrada for:
idade = input('Qual sua idade? '))

ou

print('Qual sua idade? ')
idade = input()

"""
print(f'A {nome} nasceu em {2022 - idade}')

