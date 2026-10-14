def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! {entrada} é um valor inválido')
        else:
            valido = True
            return float(entrada)