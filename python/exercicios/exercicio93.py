dicionarioJogador = {}
listaDeGolsPorPartida = []
totalGols = 0

dicionarioJogador['nome'] = str(input("Digite o nome do jogador: "))
dicionarioJogador['partidas'] = int(input(f"Digite o número de partidas que {dicionarioJogador['nome']} jogou: "))

for c in range(0, dicionarioJogador['partidas']):
    gols = int(input(f"Quantos gols na partida {c+1}: "))
    listaDeGolsPorPartida.append(gols)
    dicionarioJogador['gols'] = listaDeGolsPorPartida[:]

    totalGols += gols

print(dicionarioJogador)
print(f'{dicionarioJogador['nome']} fez um total de {totalGols} gols em sua carreira')


