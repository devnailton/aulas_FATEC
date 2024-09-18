"""notas1 = [7.5, 8.0, 9.0, 6.5]
soma1 = 0
for nota in notas1:
    soma1 += nota
media1 = soma1 / len(notas1)
print(media1)

notas2 = [5.5, 6.0, 8.0, 7.0]
soma2 = 0
for nota in notas2:
    soma2 += nota
media2 = soma2 / len(notas2)
print(media2)
"""


def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)

notas1 = [7.5, 8.0, 9.0, 6.5]
notas2 = [5.5, 6.0, 8.0, 7.0]

print(calcular_media(notas1))
print(calcular_media(notas2))