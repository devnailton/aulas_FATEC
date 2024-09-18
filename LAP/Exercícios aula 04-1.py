salarios_antigos = []

for i in range(2):
    salario = float(input(f"Digite o salário do funcionário {i+1}: "))
    salarios_antigos.append(salario)

salarios_novos = []

for salario in salarios_antigos:
    if salario < 1400:
        novo_salario = salario * 1.12
    elif 1400 <= salario <= 5000:
        novo_salario = salario * 1.08
    else:
        novo_salario = salario * 1.05
    salarios_novos.append(novo_salario)

for i in range(len(salarios_antigos)):
    print(f"Salário antigo do funcionário {i+1}: R$ {salarios_antigos[i]}")
    #print(f"Salário antigo do funcionário {i+1}: R$ {salarios_antigos[i]:.2f}")
    print(f"Salário novo do funcionário {i+1}: R$ {salarios_novos[i]}")

    