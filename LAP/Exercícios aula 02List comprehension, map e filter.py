palavras = ["massa", "carro", "correr", "sol", "rir", "corrida", "ousado", "ressaca", "carroça", "cor", "muscular", "dor", "asa", "sonar", "assessor", "rua", "massagista", "sentimento", "passaporte", "assessoria", "obstáculos", "massagem", "ressaltar", "azul"]
numeros = [9, 56, 45, 59, 555, 489, 723, 220, 49, 87, 74, 71, 51, 46, 125, 265, 433, 547, 589, 33]
"""
01 -

palavras_com_digrafos = [palavra for palavra in palavras if "rr" in palavra or "ss" in palavra]
print(palavras_com_digrafos)"""

"""palavras_terminadas_em_ar = list(filter(lambda palavra: palavra.endswith("ar"), palavras))
print(palavras_terminadas_em_ar)"""

"""multiplos_de_3_e_5 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numeros))
print(multiplos_de_3_e_5)"""

"""

5 - 

resultado = list(map(lambda x: x + 5, filter(lambda x: x % 3 == 0, numeros)))

resultado1 = [x for x in numeros if x % 3 == 0]
resultado2 = [x + 5 for x in numeros if x % 3 == 0]

print(resultado1)
print(resultado2)"""

"""

06 - 
multiplos_de_3 = [x for x in numeros if x % 3 == 0]
multiplos_de_4 = [x for x in numeros if x % 4 == 0]


print("Múltiplos de 3:", multiplos_de_3)
print("Múltiplos de 4:", multiplos_de_4)

multiplos_de_3_multiplicados = [x * 3 for x in multiplos_de_3]
multiplos_de_4_subtraidos = [x - 2 for x in multiplos_de_4]

print("Múltiplos de 3 multiplicados por 3:", multiplos_de_3_multiplicados)
print("Múltiplos de 4 subtraídos de 2:", multiplos_de_4_subtraidos)"""

"""
7 - 
multiplos_de_3_ou_4 = [x for x in numeros if x % 3 == 0 or x % 4 == 0]

print("Números múltiplos de 3 ou 4:", multiplos_de_3_ou_4)

for numero in multiplos_de_3_ou_4:
    if numero % 2 == 0:
        print("ADS")
    else:
        print("LAP 2")

multiplos_de_3_multiplicados = [x * 6 for x in multiplos_de_3_ou_4 if x % 3 == 0]

multiplos_de_4_somados = [x + 7 for x in multiplos_de_3_ou_4 if x % 4 == 0]

print("Múltiplos de 3 multiplicados por 6:", multiplos_de_3_multiplicados)
print("Múltiplos de 4 somados a 7:", multiplos_de_4_somados)

"""


precos = [9, 56, 45, 59, 555, 489, 723, 220, 49, 87, 74, 71, 51, 46, 125, 265, 433, 547, 589, 33]

#impostos = list(map(lambda x: x * 0.3 if x > 70 else 0, precos))

impostos = list(map(lambda x: x * 0.3, filter(lambda x: x > 70, precos)))

print(impostos)