def area(a, b):
    s = a * b
    return s


largura = float(input('Qual a largura? '))
comprimento = float(input('Qual a comprimento? '))
print('-'*50)
areaTotal = area(comprimento, largura)
print(f'A area do terreno é {areaTotal}')