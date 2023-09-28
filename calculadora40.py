''' Calculadora com o While '''

while True:
    num1 = input('Digite o primeiro número da conta: ')
    num2 = input('Digite o segundo número da conta: ')    
    operador = input('Digite o operador (+ - / *) da conta: ')    
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except:
        print('Digite um número!')
        continue

    operadores_validos = '+-*/'
    if operador not in operadores_validos:
        print('Escolha um dos operadores válidos.')
        continue
    
    if len(operador) > 1:
        print('Escolha apenas um operador.')
        continue

    print('Estou realizando a sua conta, confira o resultado abaixo:')

    if operador == '+':
        print(f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = ', num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = ', num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ', num1_float * num2_float)
    else:
        print('Você não deve chegar até essa parte.')

    saida = input('Quer sair da calculadora? [s]im [n]ão: ').lower().startswith('s')


    if saida is True:
        print('Você está saindo da calculadora!')
        break