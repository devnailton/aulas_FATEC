"""lista = [76, 99, 90, 65, 50, 71, 33]

for i in range(len(lista)):
    print(lista[i])"""


"""idades = [76, 99, 90, 65, 50, 71, 33]
dobro = []
for idade in idades:
    dobro.append(idade * 2)

print(dobro)"""

"""idades = [76, 99, 90, 65, 50, 71, 33]
dobro = [x*2 for x in idades]

print(dobro)"""

"""frutas = ["maça", "banana", "uva", "kiwi", "manga"]
novalista = [x for x in frutas]

print(novalista)"""


"""frutas = ["maça", "banana", "uva", "kiwi", "manga"]
novalista = [x for x in frutas if x.startswith('m')]

print(novalista)"""

"""frutas = ["maça", "banana", "uva", "kiwi", "manga"]
novalista = [x for x in frutas if x.endswith('a')]

print(novalista)"""

"""lista = ['Fábio', 'Jefferson', 'Ivy', 'Ianka', 'Jonh', 'Maria', 'Ygor', 'João']

newlist = list(map(lambda x: x, lista))

print(newlist)"""

"""precos = [1000, 5500, 5250, 625, 998, 653, 745, 200]

precos_produtos = list(filter(lambda preco: preco > 700, precos))"""


"""lista = ['Fábio', 'Jefferson’, Ivy’, ‘Ianka', 'Jonh', 'Maria', 'Ygor', 'João']


nomes2= list(filter(lambda nome: nome.startswith('J'), lista))

print(nomes2)"""

lista_nomes = ['Fábio', 'Jefferson', 'Ivy', 'Ianka', 'Jonh', 'Maria', 'Ygor', 'João', 'Albert']

# Função lambda para verificar se um nome começa com 'a'
nomes_com_a = [x for x in lista_nomes if 'a' in x.lower()]

print(nomes_com_a)
