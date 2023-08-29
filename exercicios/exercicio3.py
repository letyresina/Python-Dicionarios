'''
    Exercício 3:
    Preencha um dicionário com os dados de 5 alunos.
    - Utilize o ra do aluno como chave e uma lista de três notas como valor.
    - Solicite os dados ao usuário.
    Percorra o dicionário e exiba a média de cada aluno.
'''

alunos = {}


while len(alunos) < 5:
    notas = []

    ra = int(input("Informe o RA do aluno: "))

    if ra in alunos:
        print("RA já cadastrado. Tente novamente")

    else:
        while len(notas) < 3:
            nota = float(input("Informe a nota do aluno: "))
            notas.append(nota)
    
        alunos[ra] = notas

print(alunos)

for i in alunos.keys():
    mediaAritmetica = sum(alunos[i]) / 3
    print(f"A média aritmética de {i} é de {mediaAritmetica}")