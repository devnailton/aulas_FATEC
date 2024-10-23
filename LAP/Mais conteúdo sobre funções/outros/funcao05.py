def juntar_nomes(nome, sobrenome):
    return nome + " " + sobrenome

#print(juntar_nomes("Tiago", "Lima"))

#Crie uma lista que contenha a função criada, e que irá conter nomes completos, a partir de 5 nomes e sobrenomes digitados pelo usuário
"""
nomes_completos = []
for i in range(2):
    nome = input("Digite o primeiro nome: ")
    sobrenome = input("Digite o sobrenome: ")
    nomes_completos.append(juntar_nomes(nome, sobrenome))"""

nomes_completos = [juntar_nomes(input("Digite o nome:"), input("Digite o sobrenome")) for i in range(2)]
print(nomes_completos)
