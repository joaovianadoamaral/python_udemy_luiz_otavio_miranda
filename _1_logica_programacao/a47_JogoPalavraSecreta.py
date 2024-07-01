"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

letra = None

palavra_secreta = 'perfume'.lower()
tam_palavra_secreta = len(palavra_secreta)

letras_certas = ''

tentativa = 0
# comando para limpar terminal
os.system('cls')

while True :
    letra_digitada = input('Digite uma letra: ')

    tentativa += 1

    # permite o usuario digitar somente uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    # se existe a letra digitada na palavra secreta
    if letra_digitada in palavra_secreta:
        # salva a letra 
        letras_certas += letra_digitada

    # imprime a palavra formatada com * e letras
    palavra_formada = ''
    for letra in palavra_secreta:
        esta_nas_palavras_acertadas =  letra in letras_certas

        if esta_nas_palavras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)

    # se não existe mais '*' na palavra formatada o usuario ganhou
    condicao_vitoria = palavra_formada == palavra_secreta
    if condicao_vitoria:
        break

# mostra na tela que o usuario ganhou
print('-=-' * 20)
print(
    f'parabéns!! você ganhou\n'
    f'A palavra era {palavra_secreta}\n'
    f'Você gastou {tentativa} tentativas'
)

    
