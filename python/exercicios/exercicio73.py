times = ("Palmeiras", "Flamengo", "Fluminense", "São Paulo", "Athletico-PR", "Bahia", "Atlético-MG", "Internacional",
 "Red Bull Bragantino", "Coritiba", "Vasco da Gama", "Vitória", "Cruzeiro", "Botafogo", "Santos", "Corinthians",
 "Grêmio", "Mirassol", "Remo", "Chapecoense")
print(f'Os cinco primeiros colocados são: ', {times[0:5]})
print(f'Os quatro últimos colocados são: ', {times[-4:]})
print(f'Em ordem alfabética fica assim: {sorted(times)}')
print(f'E o chapeconse está na posição ', {times.index("Chapecoense")+1})