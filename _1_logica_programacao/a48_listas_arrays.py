"""
Listas em Python
Tipo list - Mutável
= array do javascript
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

# uma lista vazia retorna falsy - > False
# print(bool([]))  # falsy
# print(lista, type(lista))
# duas maneiras de criação de lista: lista = [], ou lista = list()
# usar list() - modelo de coerção
#        0    1      2              3    4
#       -5   -4     -3             -2   -5
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

# é um dado mutavel porque podemos sobrescrever o item inteiro 
# ex lista [3] = 1, o valor cujo indice for 3 passa a a ser 1