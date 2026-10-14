matriz = [[0,0,0],[0,0,0],[0,0,0]]
maiorValor = terceiraColuna = somaPares = 0


for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f"Digite um número para [{l}, {c}] ")))

print("-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
print("-" * 30)

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]

        if c == 2:
            terceiraColuna += matriz[l][c]

    for c in range(0, 3):
        if c == 0:
                maiorValor = matriz[1][c]
        elif matriz[1][c] > maiorValor:
                maiorValor = matriz[1][c]

print(f"A soma dos numeros pares é {somaPares}")
print(f"A soma da terceira coluna é {terceiraColuna}")
print(f"O maior valor digitado foi {maiorValor}")