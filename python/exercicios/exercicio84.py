pessoas = []
dadosTemporarios = []
resposta = "s"
maior = menor = 0

while True:
    dadosTemporarios.append(str(input("Digite o nome: ")))
    dadosTemporarios.append(float(input("Digite o peso (kg): ")))
    if len(pessoas) == 0:
        maior = menor = dadosTemporarios[1]
    else:
        if dadosTemporarios[1] > maior:
            maior = dadosTemporarios[1]
        if dadosTemporarios[1] < menor:
            menor = dadosTemporarios[1]

    pessoas.append(dadosTemporarios[:])
    dadosTemporarios.clear()
    resposta = str(input("Deseja continuar? [S/N] "))

    if resposta.lower() == "n":
        break

print("-"*30)
print(f"ao todo você cadastrou {len(pessoas)} pessoas")
print (f"o maior peso foi {maior}", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"C) O menor peso foi de {menor} kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")


