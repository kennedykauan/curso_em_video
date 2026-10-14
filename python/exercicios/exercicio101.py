from datetime import date
def verificarvoto(ano):
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        voto = 'Proibido'

    elif 16 <= idade < 18 or idade >= 70:
        voto = 'Opcional'

    else:
        voto = 'Obrigatório'
    return idade, voto


anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
idadeUsuario, statusVoto = verificarvoto(anoDeNascimento)
print(f'Com {idadeUsuario} anos o voto é {statusVoto}')