from datetime import datetime
dicionarioTrabalhador = {}

dicionarioTrabalhador['nome'] = str(input("Digite o seu nome: "))
nasc = int(input("Digite o seu ano de nascimento: "))
dicionarioTrabalhador['idade'] = datetime.now().year - nasc
dicionarioTrabalhador['carteiraDeTrabalho'] = int(input("Digite sua carteira de trabalho: "))

if dicionarioTrabalhador['carteiraDeTrabalho'] != 0:
    dicionarioTrabalhador['anoDeContratação'] = int(input('Digite o seu ano de contração: '))
    dicionarioTrabalhador['salario'] = float(input("Digite o salario respectivo: "))

if dicionarioTrabalhador['idade'] >= 65:
    dicionarioTrabalhador['aposentadoria'] = 'Pode aposentar'
else:
    dicionarioTrabalhador['aposentadoria'] = 'Não pode aposentar'
print('-' * 50)
for k, v in dicionarioTrabalhador.items():
    print(f'{k} tem o valor {v}')