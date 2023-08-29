'''
    Exercício 2:
    Preencha um dicionário com as informações de 5 produtos.
    - Utilize o nome do produto como chave e o preço como valor.
    - Solicite os dados ao usuário.
    Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
'''

produtos = {}

while len(produtos) < 5:
    tituloProduto = input("Informe o nome do produto: ").title()
    preco = float(input("Informe o preço do produto: "))
    if tituloProduto in produtos:
        print("Já existe esse produto cadastrado no sistema! Tente novamente")
    else:
        produtos[tituloProduto] = preco
        print("Cadastro realizado com sucesso")

print(produtos)

for i in produtos.keys():
    if produtos[i] > 50:
        print(i)
