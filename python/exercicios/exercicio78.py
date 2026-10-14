valores = []
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor digitado foi {maior} ', end = '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'na posição {i}')
print(f'O menor valor digitado foi {menor} ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'na posição {i}')