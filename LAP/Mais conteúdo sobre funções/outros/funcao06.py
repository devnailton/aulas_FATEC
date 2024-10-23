def celsius_para_kelvin(celsius):
    return celsius + 273.15

print(celsius_para_kelvin(31))


#São Paulo - Ceará - Mato Grosso - Brasília - New York, Pequim, Londres, Paris
temperaturas = [15, 29, 31, 27, 23, 21, 15, 15]

#Use a função criada, itere sobre sobre a lista e converta os valores de celsius para kelvin. Por fim exiba o resultado

"""
temperaturas_kelvin = []
for temperatura in temperaturas:
    temperaturas_kelvin.append(celsius_para_kelvin(temperatura))
    """
"""
temperaturas_kelvin = [temperatura + 273.15 for temperatura in temperaturas]
"""

"""
LIST COMPREHENSION
VARIAVEL = [ACAO PARA VALOR_INDIVUAL NO CONJUNTO_DE_VALORES]

ACAO = PODE SER UM CÁLCULO
PODE SER UMA FUNÇÃO
PARA É O FOR
VALOR_INDIVIDUAL = VALORES DE UMA LISTA POR EXEMPLO
CONJUNTO_DE_VALORES = LISTA, MATRIZ, BANCO DE DADOS
"""
temperaturas_kelvin = [celsius_para_kelvin(temperatura) for temperatura in temperaturas]

print(temperaturas_kelvin)
