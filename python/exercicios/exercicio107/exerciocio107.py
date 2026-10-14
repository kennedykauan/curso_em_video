import moeda

valor = float(input('Digite um valor R$ '))
print(f'a metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.dobrar(valor, True)}')
print(f'Se aumentarmos em 10% teremos {moeda.aumentar(valor, 10, True)}')
print(f'Se diminuirmos em 13% teremos {moeda.diminuir(valor, 13, True)}')