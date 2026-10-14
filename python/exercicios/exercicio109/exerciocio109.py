import moeda

valor = float(input('Digite um valor R$ '))
print(f'a metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobrar(valor))}')
print(f'Se aumentarmos em 10% teremos {moeda.moeda(moeda.aumentar(valor))}')
print(f'Se diminuirmos em 13% teremos {moeda.moeda(moeda.diminuir(valor))}')