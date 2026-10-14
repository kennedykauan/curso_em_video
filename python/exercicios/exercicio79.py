numeros = []

a = (int(input('Digite um número: ')))
resposta = str(input('Quer continuar? [S/N] '))
numeros.append(a)

while resposta.lower() == 's':
    a = int(input('Digite outro número: '))
    if a in numeros:
        print('Esse número já está na lista. Não é permitido repetir os números nessa lista.')
    else:
        resposta = str(input('Quer continuar? [S/N] '))
        numeros.append(a)
numeros.sort()
print(numeros)