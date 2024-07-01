# calculadora com whilie 
apresentacao = '-=-' * 20
while True: 
    print(apresentacao)
    numero1 = input('Digite um número ->> ').strip()
    # confere se o usuario realmente digitou um número
    nao_e_um_numero = not numero1.isnumeric()
    if nao_e_um_numero:
        while nao_e_um_numero:
            numero1 = input('Você não digitou um número!\nDigite um número ->> ').strip()
    numero1_float = float(numero1)

    print(apresentacao)
    numero2 = input('Digite um outro número ->> ').strip()
    # confere se o usuario realment digitou um número
    nao_e_um_numero = not numero2.isnumeric()
    if nao_e_um_numero:
        while nao_e_um_numero:
            numero2 = input('Você não digitou um número!\nDigite um número ->> ').strip()
    numero2_float = float(numero2)

    print(apresentacao)   
    operador = input('Digite um operador existente (+ - / * % //) ->> ').strip()
    # confere se o usuario digitou um operador valido
    if not operador in '+ - / * % //':
        while not operador in '+ - / * % //':
            operador = input('Você digitou um operador inválido!\nDigite um operador existente (+ - / * % //) ->> ').strip()

    operador_soma = operador == '+'
    operador_subracao = operador == '-'
    operador_multiplicacao = operador == '*'
    operador_divisao = operador == '/'
    operador_divisao_inteira = operador == '//'
    operador_resto_divisao = operador == '%'
    
    print(apresentacao)
    # condição calculadora
    if operador_soma:
        soma = numero1_float + numero2_float
        print(f'A soma de {numero1_float} com {numero2_float} é {soma}')

    elif operador_multiplicacao:
        multiplicacao = numero1_float * numero2_float
        print(f'A multiplicação de {numero1_float} com {numero2_float} é {multiplicacao}')

    elif operador_divisao:
        divisao12 = numero1_float / numero2_float
        print(f'A divisão de {numero1_float} por {numero2_float} é {divisao12}')

    elif operador_divisao_inteira:
        divisao_inteira12 = numero1_float // numero2_float
        print(f'A divisão inteira de {numero1_float} por {numero2_float} é {divisao_inteira12}')

    elif operador_resto_divisao:
        resto12 = numero1_float % numero2_float
        print(f'O resto da divisão de {numero1_float} por {numero2_float} é {resto12}')

    elif operador_subracao:
        subtracao12 = numero1_float - numero2_float 
        print(f'A subtração de {numero1_float} por {numero2_float} é {subtracao12}')
    else:
        print('Não deveria nunca acontecer isso... ')
    
    print(apresentacao)
    # condição de saida - escrever uma palavra que começa com s
    saida = str(input('O usuario deseja [s]air? ->> ')).strip().lower().startswith('s')
    if saida:
        break
print(apresentacao)
print('Encerrando...')