
#Função Calcular Impostos

#aliquota1 = IR = 0.2
#aliquota2 = ISS = 0.15
#aliquota3 = CSLL = 0.05

def calcular_imposto_total(preco):
    if preco > 2000:
        imposto_ir = 0.3 * preco
    else:
        imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    #A Função deve devolver algo, retornar algo
    #Sempre no Final da Função
    return imposto_total

precos = [1500, 1100, 1000, 3000]
for preco in precos:
    impostos = calcular_imposto_total(preco)
    print(impostos)

mais_precos = [2500, 2100, 1400, 1000]
for preco in mais_precos:
    print(calcular_imposto_total(preco))