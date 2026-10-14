numero_por_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 's'
resposta = 0

while continuar =='s':
    resposta = int((input('Digite um número entre 0 e 20: ')))
    while 0 < resposta > 20:
        resposta = int(input("O nùmero digitado é maior ou menor do que foi pedido. digite novemente: "))
    print('O número digitado por extenso é: ', numero_por_extenso[resposta])
    continuar = str.lower(input('Deseja continuar? sim [s] não [n]? '))


 