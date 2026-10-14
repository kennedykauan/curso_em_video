lista = []
valor = int(input("Digite um valor: "))
lista.append(valor)
resposta = str(input("Quer continuar? [S/N] "))

while resposta.lower() == 's':
    valor = int(input("Digite outro valor: "))
    lista.append(valor)
    resposta = str(input("Quer continuar? [S/N] "))
print(f'A lista possui {len(lista)} números')
print(f'Em valores decrescente fica asssim: {sorted(lista, reverse = True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado na posição: {lista.index(5)+1}')
else:
    print('O valor 5 não está na lista')
