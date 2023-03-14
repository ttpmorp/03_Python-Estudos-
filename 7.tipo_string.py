'''
Tipo string

Em Python, um dado é considerado do tió string sempre que:

- Estiver entre aspas simples -> 'oi'
- Estiver entre aspas dupalas -> "oi"
- Estiver entre aspas triplas -> ' ' 'oi ' ' '
- Estiver entre aspas duplas triplas -> """oi"""

nome = 'Julia'
print(nome)


nome = "Ginas's Bar"
print(nome)


nome = 'Julia \nCristinny'
print(nome)


nome = """JULIA
CRISTINNY"""
print(nome)




nome = 'JULIA CRISTINNY'
print(nome)


nome = "JULIA \" CRISTINNY"
print(nome)


nome = 'julia cristinny'
print(nome.upper()) #Transforma tudo em maiúsculo

nome = 'JULIA CRISTINNY'
print(nome.lower()) #Transforma tudo em minúsculo


nome = 'JULIA CRISTINNY'
print(nome.split()) #Transforma uma lista de strings

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10, 11,  12,  13,  14]
# ['J', 'u', 'l', 'i', 'a', ' ', 'C', 'r', 'i', 's', 't', 'i', 'n', 'n', 'y']
nome = 'Julia Cristinny'
print(nome[0:4])  #Slice de tring
print(nome[6:15]) #Slice de tring


# [0,            1]
# ['Julia', 'Cristinny']
print(nome.split()[0]) # Primeira parte da palavra
print(nome.split()[1]) # Segunda parte da palavra


print(nome[14], nome[13])

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) #Inversão da string

print(nome.replace('J', 'C')) #Troca a letra pedida por outra

print(nome.replace('i', 'u'))


""""
#Trocadilhos de programação
texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])
"""""

'''



