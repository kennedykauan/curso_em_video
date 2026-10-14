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

def leiafloat(txt):
    while True:
        try:
            n = float(input(txt).strip())
        except (ValueError, TypeError):
            print('ERRO! Digite um número real!')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar nada')
            return 0
        else:
            return n


num1 = leiaint('Digite um valor inteiro: ')
num2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num1} e o valor real digitado foi {num2}')