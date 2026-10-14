ficha = []

while True:
    nome = str(input("Digite o Nome: "))
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resposta = str(input("Deseja cadastrar outro? [S/N]: ")).upper()
    if resposta == "N":
        break

print("-" * 45)

for i, aluno in enumerate(ficha):
    # aluno[0] é o Nome, aluno[1] são as Notas, aluno[2] é a Média
    print(f'ID {i} -> O aluno {aluno[0]:<12} teve média {aluno[2]:.1f} (Nota 1: {aluno[1][0]} | Nota 2: {aluno[1][1]})')
print("-" * 45)


while True:
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if opcao == 999:
        print("FINALIZANDO SISTEMA...")
        break

    if opcao <= len(ficha) - 1:
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")
    else:
        print(f"Aviso: Aluno com ID {opcao} não foi encontrado.")
    print("-" * 35)

print("<<< VOLTE SEMPRE >>>")