def dobrar(num = 0, format = False):
    res = num * 2
    return res if not format else moeda(res)


def aumentar(num = 0, taxa = 0, format = False):
    res = num + (taxa * num/100)
    return res if not format else moeda(res)


def diminuir(num = 0, taxa = 0, format = False):
    res = num - (num * taxa/100)
    return res if not format else moeda(res)


def metade(num = 0, format = False):
    res =  num/2
    return res if not format else moeda(res)


def moeda(num = 0, moeda = 'R$', format = False):
    return f'{moeda}{num:.2f}'.replace('.', ',')

