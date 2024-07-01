from datetime import date
nome = 'João Vitor'
sobrenome = 'Viana do Amaral'
idade = 19
ano_nascimento = date.day().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.69
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
