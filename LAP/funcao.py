precos = [1500, 1100, 1000, 3000]

#aliquota1 = IR = 0.2
#aliquota2 = ISS = 0.15
#aliquota3 = CSLL = 0.05

#Coloca entre parênteses todas as informações que a função precisa pra funcionar
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

for preco in precos:
    imposto_total = calcular_imposto_total(preco)
    print(imposto_total)

mais_precos = [2500, 2100, 1400, 1000]
for preco in mais_precos:
    #imposto_total = calcular_imposto_total(preco)
    print(calcular_imposto_total(preco))