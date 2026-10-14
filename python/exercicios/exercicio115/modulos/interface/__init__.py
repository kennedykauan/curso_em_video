def leiaint(txt):
    while True:
        try:
            n = int(input(txt).strip())
        except (ValueError, TypeError):
            print(f'ERRO! por favor digite um número inteiro')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar nada')
            return 0
        else:
            return n

def linha(tamanho = 42):
    return '-'*tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 0
    for item in lista:
        print(f'{c+1} {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
