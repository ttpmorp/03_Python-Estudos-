'''
Estruturas condicionais
if(se), else(então), elif(então se)


'''

# idade = 26
# idade = 6
idade = int(input('Digite sua idade: '))

"""
# Estrutura condicional if, em C
if (idade < 18){
    print('Menor de idade');
}else{
    printf('Maior de idade');
}
"""
#------------------------------------------------------------------
"""
# Estrutura condicional if, em Java
if (idade < 18){
    system.out.println('Menor de idade');
}else{
    system.out.println('Maior de idade');
}
"""
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')



