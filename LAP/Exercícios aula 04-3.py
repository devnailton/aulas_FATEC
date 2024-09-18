notas = [[0] * 4 for _ in range(5)]

for i in range(5):
    for j in range(4):
        notas[i][j] = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))

for i in range(5):
    soma = 0
    for j in range(4):
        soma += notas[i][j]
    media = soma / 4
    print(f"A média do aluno {i+1} é: {media:.2f}") 

    