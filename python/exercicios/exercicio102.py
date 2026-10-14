def fatorial(n, show = True):
    """
    Calcula o fatorial de um número
    :param n: O numero a ser calculado
    param s: Se deseja ver o fatorial
    :return none
    """
    f = 1
    if show:
        print(f'{n}! = ', end='')

    for cont in range(n, 0, -1):
        f *= cont

        if show:
            if cont == 1:
                print(f'{cont} = {f}', end=' ')
            else :
                print(f'{cont} x', end=' ')

    print(f'\nO resultado é {f}')


print('Bem vindo à calculadora de fatorial')
numFatorial = int(input('Digite o número que você deseja saber o fatorial: '))
fatorial(numFatorial)