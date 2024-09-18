

"""quadrados = [x**2 for x in range(1, 21)]
print(quadrados)"""

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares)"""


"""frutas = ["maçã", "banana", "melancia", "uva", "manga", "Goiaba", "Acerola", "mamão"]
frutas_com_m = [fruta for fruta in frutas if fruta.startswith("m")]
print(frutas_com_m)"""

"""
frutas = ["maçã", "banana", "melancia", "uva", "manga", "Goiaba", "Acerola", "mamão"]

nomes_grandes = list(filter(lambda fruta: len(fruta) > 5, frutas))

print(nomes_grandes)"""

"""
frutas = ["maçã", "banana", "melancia", "uva", "manga", "Goiaba", "Acerola", "mamão"]

frutas_maiusculas = list(map(lambda fruta: fruta.upper(), frutas))

print(frutas_maiusculas)"""


numeros = [2, 3, 5, 10, 15, 22, 33, 45, 60, 17]

numeros_modificados = list(map(lambda num: num * 2 if num % 3 == 0 else num - 1 if num % 5 == 0 else num + 10, numeros))

resultado_final = list(filter(lambda num: num > 20, numeros_modificados))

print(resultado_final)
