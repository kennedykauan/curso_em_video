produtos = ['Biscoito', 2.50,
            'bombril', 3,
            'arroz', 7,]
print('-'*40)
print(f'{"lista de produtos":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else :
        print(f'R${produtos[pos]:>.2f}')