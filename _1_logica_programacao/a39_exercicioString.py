nome = 'Luiz Otávio'
# fazer de forma automatica com que '*L*u*i*z* *O*t*á*v*i*o*'
tamanho_nome = len(nome)
novo_nome = ''
indice = 0
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(f'{novo_nome=}')
"""aux = indice = 0
par = impar = None
while True:
    par= aux % 2 == 0
    impar = aux % 2 == 1
    if par:
        novo_nome += '*'
    elif impar:
        novo_nome += nome[indice]
        indice += 1
    aux += 1
    # condição de quebra
    if indice == len(nome):
        break
# mostra o novo nome
novo_nome += '*' 
print(f'{novo_nome=}')
"""
