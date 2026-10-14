def funcaohelp(resposta):
    while True:
        if resposta == 'fim':
            print('-'*30)
            print('FIM')
            break

        else:
            print(help(resposta))
            resposta = str(input('Digite a função ou a biblioteca ')).lower()

resp = str(input('Digite a função ou a biblioteca ')).lower()
funcaohelp(resp)