"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
# o insert recebe dois argumentos insert(indice, valor que quero adicionar)
lista.insert(100, 5)
# o insert considera se você colocar um número muito grande no indice e pega o ultimo
# pode gerar erros porque no caso acima podemos supor que o indice 100 exista, mesmo ele não existindo
print(lista[4])