dicionarioAluno = {}

dicionarioAluno['nome'] = (input("Digite o nome do aluno: "))
dicionarioAluno['media'] = float(input(f"Digite a média de {dicionarioAluno['nome']}: "))

if dicionarioAluno['media'] < 5:
    dicionarioAluno['situação'] = 'Reprovado'
else: dicionarioAluno['situação'] = 'Aprovado'

print(f"A média do aluno {dicionarioAluno['nome']} é {dicionarioAluno['media']}, sua situação é {dicionarioAluno['situação']}")