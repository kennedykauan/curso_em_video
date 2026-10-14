listaDeDicionarios = []
dicionarioDados = {}
idadeGeral = 0
listaMulheres = []

print('Bem-Vindo ao cadastro de usuários')

while True:
    dicionarioDados.clear()
    dicionarioDados['nome'] = str(input("Digite o seu nome: "))


    dicionarioDados['sexo'] = str(input("Digite o seu sexo: ").upper())


    dicionarioDados['idade'] = int(input("Digite sua idade: "))

    idadeGeral += dicionarioDados['idade']

    if dicionarioDados['sexo'] == 'F':
        listaMulheres.append(dicionarioDados.copy())

    listaDeDicionarios.append(dicionarioDados.copy())


    resp = str(input("Deseja cadastrar outra pessoa? [S/N]")).upper()
    if resp == 'N':
        break

print(f"Foram cadastradas {len(listaDeDicionarios)} pessoas")
print(listaDeDicionarios)
media = idadeGeral / len(listaDeDicionarios)
print(f"A média da idade do grupo é {media:5.2f} anos")
print(f'As mulheres cadastradas foram: {listaMulheres}')
