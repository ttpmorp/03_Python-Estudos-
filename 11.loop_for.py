'''
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estrututras


C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python
for item in interalvel:
    //execução do loop


Utilizamos loops ára iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Julia'

- Lista
    Lista = [1, 3, 5]

- Range
    numeros = range(1, 5)
'''

nome = 'você é gay'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# exemplo de for 1 (iterando sbore stg)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
    
