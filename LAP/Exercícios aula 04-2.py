"""funcionarios = [
    [None, None, None, None, None],  
    [None, None, None, None, None]  
]"""
funcionarios = [[None] * 3 for _ in range(2)]

for i in range(3):
    nome = input(f"Digite o  nome do funcionário [{i}]:")
    salario = float(input(f"Digite o salário do funcionário  [{i}]:"))
    funcionarios[0][i] = nome
    funcionarios[1][i] = salario

for i in range(3):
    print(f"{funcionarios[0][i]} - Salário R$ {funcionarios[1][i]}")