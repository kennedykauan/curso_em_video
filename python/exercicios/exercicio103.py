def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


print('Seja bem vindo a ficha de jogador')
jogador = (input('Digite o seu nome do jogador: ')).strip()
golsJogador = (input(f'Digite o número de gols feito pelo {jogador} '))

if golsJogador.isnumeric():
    golsJogador = int(golsJogador)
else:
    golsJogador = 0

if jogador.strip() == '':
    ficha(gols=golsJogador)

else:
    ficha(jogador, golsJogador)
