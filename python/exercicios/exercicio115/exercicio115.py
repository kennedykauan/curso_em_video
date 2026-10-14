from modulos.interface import *
from modulos.arquivo import *

arq = "curso-em-video.txt"

if not arquivoexiste(arq):
    criararq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do programa'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do arquivo, até logo!')
        break
    else:
        print('Por favor digite uma entrada válida')
