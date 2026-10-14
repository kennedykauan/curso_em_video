numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ',)))


print('O número nove foi digitado', numeros.count(9), 'vezes')

if 3 in numeros:
    print('O primeiro número 3 foi digitado na posição: ', numeros.index(3)+1)
else:
    print('O número três não foi digitado nenhuma vez.')

print('os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')




