def notas(*num, situacao=False):
    """
     Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita múltiplas).
    :param situacao: (Opcional) Indica se deve ou não adicionar a situação da turma.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    analise = {}
    analise['total'] = len(num)
    analise['maior'] = max(num)
    analise['menor'] = min(num)
    analise['media'] = sum(num) / len(num)

    if situacao:
        if analise['media'] >= 7:
            analise['situacao'] = 'Boa'

        elif analise['media'] >= 5:
            analise['situacao'] = 'Razoável'

        else:
            analise['situacao'] = 'Ruim'

    return analise

listaDeNotas = []

print('-'*30)
print('Sistema de análise de notas')
print('-'*30)

while True:
    try:
        nota = float(input('Digite uma nota: '))
        if 0 <= nota <= 10:
            listaDeNotas.append(nota)
        else:
            print('Erro. A nota deve ser entre 0 e 10')
            continue
    except ValueError:
        print('Erro. Digite um número válido')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*30)

resultadoDaTurma = notas(*listaDeNotas, situacao=True)
print('Dicionário gerado')
print(resultadoDaTurma)




