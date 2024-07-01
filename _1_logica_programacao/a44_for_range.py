
"""
For + Range
range -> range(start, stop, step)
quando se passa um valor só: 
exp range(x), o start = 0 por padrão, o stop é o x - 1 e step=1 por padrão
função range não precisa do for e nem vice - versa
existem palavras reservadas no python que não se pode usar em variaveis - range é uma delas
"""
numeros = range(0, 100, 8)

# aqui já não é mais indices e sim os números em si
for numero in numeros:
    print(numero)