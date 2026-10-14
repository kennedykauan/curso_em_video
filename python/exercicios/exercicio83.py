expre = str(input('Digite sua expressão: '))
lista = []
a = lista.count('(')
b = lista.count(')')

for simb in expre:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua lista é válida')
else:
    print('Sua lista é inválida')
