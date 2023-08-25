# cadastro de cliente
#código do cliente (key) / nome do cliente 
cadastro = {
    123: "João",
    532: "Paulo",
    897: "Maria"
}

print(cadastro)

# acessar uma chave
print(cadastro[123])

# Alterar um valor
cadastro[532] = "Paulo Vieira"
print(cadastro)

# inserir um valor novo no dicionário -> insira uma chave que não existe!
cadastro[652] = "Fernando"
print(cadastro)

# Remover um item 
cadastro.pop(123)
print(cadastro)

# caso você tente remover uma chave inexistente, você pode tratar o erro de KeyError

# busca especifica de uma chave 
codigo = int(input("Informe o código: "))
if codigo in cadastro:
    print(f"Cliente cadastrado {cadastro[codigo]}")
else:
    print("Cliente não cadastrado")

# percorrer dicionário
for codigos in cadastro.keys(): # percorre somente as chaves
    print(codigos)

# preenchendo dicionário com inputs
dadosCliente = {} # dicionário vazio
for i in range(3):
    chave = int(input("Digite o código do cliente: "))
    nome = input("Informe o nome do cliente: ")
    dadosCliente[chave] = nome

print(dadosCliente) 

# limitando pra nao ir o mesmo codigo 
clientes = {}
while len(clientes) < 3:
    chave = int(input("Digite o código do cliente: "))
    nome = input("Informe o nome do cliente: ") 
    if chave not in clientes:
        clientes[chave] = nome
    else:
        print("Codigo já cadastrado")

print(clientes)

# dicionario com listas
alunos = {
    1234: [9, 8, 7],
    2345: [6, 7, 8],
    2233: [2, 4, 6]
}

# acessando a lista
print(alunos) # mostra tudo
print(alunos[1234]) # mostra a lista de uma chave especifica
print(alunos[2233][2]) # mostra, se houver, a nota dentro de uma chave de um dicionário