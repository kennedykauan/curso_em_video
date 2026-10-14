def leiaint(num):
    while num.lower() in 'abcdefghijklmnopqrstuvwxyz':
        print('Digite um número!', end=' ')
        num = input('').strip()
    else:
        print(f'Voce digitou o número {num}')

resposta = input('Digite um número inteiro ')
leiaint(resposta)