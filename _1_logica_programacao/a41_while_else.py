""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else: 
    # O else é executado sempre que nossa condição vai até o fim. pode servir como uma flag
    # existe esse else no for tambem
    print('Não encontrei um espaço na string.')
print('Fora do while.')