'''
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não vírgula.

'''

# Errado do ponto de vista do float mas gera uma dupla
valor = 1, 44

print(valor)

# Certo do ponto de vista float

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))

print(valor2)
print(type(valor2))

# Podemos converter um float para um int
'''
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
'''
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trabalhar com números complexos
variavel = 5j

