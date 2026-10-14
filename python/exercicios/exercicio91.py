from random import randint
from operator import itemgetter

vencedor = 0

dicionarioJogador = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6),}

ranking = []



for k, v in dicionarioJogador.items():
    print(f'{k} tirou {v} nos dados.')

ranking = sorted(dicionarioJogador.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v} com no dado.')








