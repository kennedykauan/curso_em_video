numeros = [[], []]
for c in range(0, 7):
    numero = int(input(f"Digite o {c+1} numero: "))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares digitados foram: {numeros[0]}')
print(f"Os numeros impares digitados foram: {numeros[1]}")
