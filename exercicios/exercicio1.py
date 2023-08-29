'''
    Exercício 1:
    reencha um dicionário com as informações de 5 pessoas.
    - Utilize o cpf da passoa como chave e o nome como valor.
    - Solicite os dados ao usuário.
'''

pessoas = {}

while len(pessoas) < 5:
    cpf = input("Informe o CPF: ")
    nome = input("Informe o nome do portador do CPF: ")
    if cpf not in pessoas:
        pessoas[cpf] = nome
        print("Cadastro feito com sucesso!")
    else:
        print("Já existe esse CPF cadastrado no sistema! Tente novamente")

print(f"{pessoas}")