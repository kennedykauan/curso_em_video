lista = []
listapar = []
listaimpar = []

numero = int(input('Digite um número: '))
resposta = str(input("Você quer continuar? [s/n]: "))

lista.append(numero)

if numero % 2 == 0:
    listapar.append(numero)
elif numero % 2 != 0:
    listaimpar.append(numero)


while resposta.lower() == "s":
    numero = int(input('Digite outro número: '))
    resposta = str(input("Você quer continuar? [s/n]: "))
    if numero % 2 == 0:
        listapar.append(numero)
    elif numero % 2 != 0:
        listaimpar.append(numero)

print(f'A lista original é: {lista}')
print(f'Os números pares são {listapar}')
print(f'Os números impares são {listaimpar}')
