def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0,1
    elif valor < 2000:
        imposto = valor *0.13
    else:
        imposto = valor * 0.2

    return imposto


preco_produto1 = 5000
preco_produto2 = 2500

print(calcular_imposto(preco_produto1))