'''
    Exercício 4:
    Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é
    a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.
'''

quantidadeVogais = {}

def contaVogais(texto):
    vogais = "aeiouAEIOU"
    for i in texto:
        if i in vogais:
            if i not in quantidadeVogais:
                quantidadeVogais[i] = 1
            else:
                quantidadeVogais[i] += 1

    return quantidadeVogais

texto = input("Informe um texto qualquer: ")
print(f"{contaVogais(texto)}")

