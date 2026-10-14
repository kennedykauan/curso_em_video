def contador(i, f, p):
    if p == 0:
        p = 1

    if i > f and p >0:
        p *= -1

    elif i <f and p ==0:
        p *= -1

    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')

    if i > f:
        for c in range(i, f-1, p):
            print(c, end=' ')

    print()

inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)

inicio = 10
fim = 0
passo = -2
contador(inicio, fim, passo)

inicio = int(input('digite o Inicio: '))
fim = int(input('digite o Fim: '))
passo = int(input('digite o Passo: '))

contador(inicio, fim, passo)
