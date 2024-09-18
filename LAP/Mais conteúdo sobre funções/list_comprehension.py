"""pares = []
for i in range(21):
    if i % 2 == 0:
        pares.append(i)
print(pares)
"""
#List Comprehension
pares = [i for i in range(21) if i % 2 == 0]
print(pares)
#######################################################


"""
celsius = [0, 10, 20, 30]
valores_em_fahrenheit = []
for c in celsius:
    fahrenheit = (c * 9/5) + 32
    valores_em_fahrenheit.append(fahrenheit)
print(valores_em_fahrenheit)
"""
celsius = [0, 10, 20, 30]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)

#######################################################
#Crie uma lista que recebe os quadrados dos valores de outra lista
numeros = [ 1, 2, 3, 4, 5, 6]
#numeros_ao_quadrado = [1 ** 2, 2**2, 3**2, 4**2, 5**2, 6**2]
#ERA ESSE FRANKSTEIN
numeros_ao_quadrado = []
for i in numeros:
    numeros_ao_quadrado.append(i**2)
print(numeros_ao_quadrado)
#VIROU ESSE TIREX
numeros_ao_quadrado = [i**2 for i in numeros]
print(numeros_ao_quadrado)

#######################################################
"""
numeros = [1, 2, 3, 4, 5, 6]
quadrados_pares = []
for num in numeros:
    if num % 2 == 0:
        quadrados_pares.append(num**2)
print(quadrados_pares)
"""

numeros = [1, 2, 3, 4, 5, 6]
quadrados_pares = [num**2 for num in numeros if num % 2 == 0]
print(quadrados_pares)
