def dobrar(num = 0, formato = False):
    res = num * 2
    return res if formato is False else moeda(res)

def aumentar(num = 0, taxa = 0, formato = False):
    res = num + (taxa * num/100)
    return res if formato is False else moeda(res)

def diminuir(num = 0, taxa = 0, formato = False):
    res = num - (num * taxa/100)
    return res if formato is False else moeda(res)


def metade(num= 0, formato = False):
    res =  num/2
    return res if formato is False else moeda(res)


def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num = 0, taxaa = 10, taxar = 5):
    print(f'-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-'*30)
    print(f'Preço analisado {moeda(num)}')
    print(f'-'*30)
    print(f'A metade de {moeda(num)} é \t\t\t{metade(num,True)}')
    print(f'O dobro de {moeda(num)} é \t\t\t{dobrar(num,True)}')
    print(f'Se diminuirmos em {taxar}% teremos \t{diminuir(num, taxar, True)}')
    print(f'Se aumentarmos em {taxaa}% teremos \t{aumentar(num, taxaa,True)}')
    print('-'*30)