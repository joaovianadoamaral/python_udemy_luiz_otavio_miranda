
"""
Iterável -> str, range, etc (__iter__) dois __ é um dunder.
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# quando os valores são acabados usando .__next__() ou next() surge um erro
# iteratador = iter(texto)  # iterator

# o laço for trabalha exatamente igual a esse laço while
# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
# StopIteration é um erro que não existe mais valor no next e quando da esse erro no try ele trata no except
#     except StopIteration: 
#         break

for letra in texto:
    print(letra)