"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# o uso de del move os indices dos itens. se a lista for muito grande requer muito processamento
# del lista[2]
# na lista é interessante ou adicionar ou remover coisas no final dela e não no inicio
# print(lista)
# print(lista[2])
# append(adiciona_valores_ao_final_da_lista)
lista.append(50)
lista.pop()
# o metodo .pop remove o ultimo item da lista no momento, lembre-se mutavel
lista.append(60)
lista.append(70)
# o pop() retorna um inteiro == ultimo valor
# podemos passar para o pop(indice_doq_quero_que_remova)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)