time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    tot = int(input(f"Digite o número de partidas que {jogador['nome']} jogou: "))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c+1}: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    resp = str(input("Quer continuar? [S/N]")).upper()[0]
    if resp == "N":
        break

print("-="*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-="*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-="*40)

while True:
    busca = int(input("Mostrar os dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"erro não existe o jogador com o código {busca}! ")
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}! ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
        print('-'*50)
print("Volte sempre!")



