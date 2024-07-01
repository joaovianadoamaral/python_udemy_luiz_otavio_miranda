"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('-'*30)
numero = input('Digite um número inteiro ->> ')
if numero.isdigit(): # serve para saber se o usuario apenas digitou números, o float possui ponto
    numero_int = int(numero)
    # se par ou impar
    par_impar = numero_int % 2 == 0
    if par_impar:
        print('Esse é um número par.')
    else:
        print('Esse é um número impar')
else:
    print('Você não digitou um número inteiro.')
print('-'*30)
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('-'*30)
horas = input('Digite as horas ->> ')
# bom dia
mais_que_meia_noite = horas >= '00-00'
menos_que_meio_dia = horas < '12-00'

# boa tarde 
mais_que_meio_dia = horas >= '12-00'
menos_que_18 = horas < '18-00'

# boa noite
mais_igual_18 = horas >= '18-00'
menos_que_meia_noite = horas <= '23-59'

if  mais_que_meia_noite and menos_que_meio_dia :
    print(f'Bom dia')
elif mais_que_meio_dia and menos_que_18:
    print(f'Boa tarde')
elif mais_igual_18 and menos_que_meia_noite:
    print(f'Boa noite')

print('-'*30)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('-'*30)

nome = input('Nome ->> ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_longo = len(nome) > 6

if nome and nome_curto:
    print('Seu nome é curto')
elif nome and nome_normal:
    print('Seu nome é longo')
elif nome and nome_longo :
    print('Seu nome é muito grande')
else: 
    print('você não digitou um nome valido')

print('-'*30)