# iteração com for
# use for para coisas 'FINITAS'
# algo iteravel te entrega um valor por vez
str = 'joão vitor viana do amaral'.title()
for i in str: 
        print(i, end = ' ')
        # i passa a ser uma str
        # o 'i' aqui é igual a str[indice]
        # esse for faz um loop completo começando com o indice = 0 e indo até o indice = n
print('\n')

# o programa acima é igual a esse de baixo
for i in range(0, len(str)):
    # i passa a ser um número
    # aqui o i representa os indices da string precisando usar 
    # o i nesse caso vai de 0 até o tamanho-1 da str
    # em uma str de tamanho = 10 caracteres, precisaremos de 11 de range
    # como a função len começa a contagem do 1 e não do zero ela vai retorna 11 e não 10
    print(str[i], end = ' ')

