def escreva(txt):
    tam = len(txt) + 4
    print('-'*tam)
    print(f'  {txt}')
    print('-'*tam)


texto = str(input('Digite uma frase: ')).strip()
escreva(texto)