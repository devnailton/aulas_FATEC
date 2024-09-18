"""
idades_grupo1 = [15, 20, 17, 22, 30]
permitidos_grupo1 = []
for idade in idades_grupo1:
    if idade >= 18:
        permitidos_grupo1.append(True)
    else:
        permitidos_grupo1.append(False)
print(permitidos_grupo1)

idades_grupo2 = [13, 25, 18, 16, 21]
permitidos_grupo2 = []
for idade in idades_grupo2:
    if idade >= 18:
        permitidos_grupo2.append(True)
    else:
        permitidos_grupo2.append(False)
print(permitidos_grupo2)
"""

def verificar_permissao_acesso(idades):
    return [idade >= 18 for idade in idades]

idades_grupo1 = [15, 20, 17, 22, 30]
idades_grupo2 = [13, 25, 18, 16, 21]

print(verificar_permissao_acesso(idades_grupo1))
print(verificar_permissao_acesso(idades_grupo2))