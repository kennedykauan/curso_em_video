matriz = [[],[],[]]
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l].append(int(input(f"Digite um número ")))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()