"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome ->> ')
idade = input('Digite sua idade ->> ')

# se nome e idade forem digitados
if nome and idade:
    # seu nome é {nome}
    print(f'Seu nome é {nome}')

    # seu nome invertido 
    nome_invertido = nome[::-1]
    print(f'Seu nome invertido é {nome_invertido}')

    # seu nome contem ou não espaços 
    if ' ' in nome:
        print(f'Olá {nome}, seu nome possui espaços')
    else: 
        print(f'Olá {nome}, seu nome não possui espaços')

    # seu nome contém n letras
    print(f'Seu nome têm {len(nome)} letras')

    # a primeira letra do seu nome é 
    print(f'A primeira letra do seu nome é {nome[0]}')

    # a ultima letra do seu nome é 
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('DESCULPE, você deixou campos vazios.')