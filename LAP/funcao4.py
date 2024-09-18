"""numeros1 = [10, 15, 20, 25, 30]
pares1 = []
for numero in numeros1:
    if numero % 2 == 0:
        pares1.append(numero)
print(pares1)

numeros2 = [7, 18, 21, 24, 29]
pares2 = []
for numero in numeros2:
    if numero % 2 == 0:
        pares2.append(numero)
print(pares2)
"""


def filtrar_pares(numeros):
    return [numero for numero in numeros if numero % 2 == 0]

numeros1 = [10, 15, 20, 25, 30]
numeros2 = [7, 18, 21, 24, 29]

print(filtrar_pares(numeros1))
print(filtrar_pares(numeros2))