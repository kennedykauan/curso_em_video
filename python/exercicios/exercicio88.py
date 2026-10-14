import random

todosOsJogos = []

print("-" * 30)
print(f"{'GERADOR DE JOGOS DA MEGA SENA':^30}")
print("-" * 30)

quantidaDeJogos = int(input("Quantos jogos você deseja gerar? "))

for i in range(0, quantidaDeJogos):
    jogo = random.sample(range(1, 61),6)
    jogo.sort()
    todosOsJogos.append(jogo)

for i, jogo in enumerate(todosOsJogos):
    print(f"Jogo {i+1}: {jogo}")