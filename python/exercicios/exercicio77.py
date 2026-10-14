palavras = ('marcelo', 'kennedy', 'joao')

for p in palavras:
    print(f'\n na palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')