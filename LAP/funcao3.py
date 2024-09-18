"""precos1 = [100, 200, 150, 80]
desconto1 = 0.1
precos_com_desconto1 = []
for preco in precos1:
    precos_com_desconto1.append(preco * (1 - desconto1))
print(precos_com_desconto1)

precos2 = [300, 400, 250, 120]
desconto2 = 0.15
precos_com_desconto2 = []
for preco in precos2:
    precos_com_desconto2.append(preco * (1 - desconto2))
print(precos_com_desconto2)
"""

def aplicar_desconto(precos, desconto):
    return [preco * (1 - desconto) for preco in precos]

precos1 = [100, 200, 150, 80]
precos2 = [300, 400, 250, 120]

print(aplicar_desconto(precos1, 0.1))
print(aplicar_desconto(precos2, 0.15))