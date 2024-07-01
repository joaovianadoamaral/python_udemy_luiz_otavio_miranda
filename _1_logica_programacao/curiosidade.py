# use ... ou pass para não precisar escrever o código.

#não é recomendado fazer conversões direto no input já que não se pode verificar o que o usuário digitou
# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# # quando se usa strings nomeadas, dela pra frente tem que nomear todas
# a=b=c=1
# string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# formato = string.format(
#     nome1=a, nome2=b, nome3=c
# )

# podemos usar a função format com indices sendo que para '{2}{1}{0}'.format(a,b,c)
# será printado na tela as variaveis na ordem : c b a. já que a possui o indice 0, b o indice 1, e c o indice 2
# quando é passado 3 argumentos no format(), não necessariamente se usará os 3.

# escolha entre f-strings, método .format() e interpolação '%s, %f, %d'.

# boas práticas de programação:
'''
no python não existe restrição de constantes em si.
use letras maiusculas, por convenção para constantes.
evite muitas condições no if.
contagem de afastamento da margem. (quanto mais blocos dentro de blocos)
'''

# use \ para a continuação de código ex:

if True and False \
    and True: # a condição do laço if continua nessa linha
    print(1)

# no vs code vc consegue renomear todas as variaveis colocando o cursor nela e apertando f2

# crlt + k + c - comentarios

# id(variavel) - aponta onde a variavel/ conteudo dela está na memória.

# é ruim declarar variaveis dentro de blocos, pode ser confuso, essa variavel inclusive pode
# atrapalhar o fluxo do programa gerando bugs e erros.

# None - Não é um valor, declarar fora para possivelmente atribuir um valor futuro.
# use variavel is None / variavel is not None ao invés de variavel == None e vice versa.

# caso eu queira saber se o interpretador entrou em uma condição. não crie a variavel la dentro
# Flag é uma bandeira que marca um local.


# solucionar problemas é chamado de algoritmo

# str, int, float e bool são dados imutaveis. não é possivel alterar o conteúdo em si.
# crie outro variavel.
# esses tipos imutaveis são objetos - possuem metodos.
# existem dados mutaveis.

# leia a documentação oficial de python

# o break busca o laço mais próximo.



