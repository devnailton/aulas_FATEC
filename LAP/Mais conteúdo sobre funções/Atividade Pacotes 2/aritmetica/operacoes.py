def soma(a, b):
    print('Cálculo da soma:')
    return a + b

def divisao(a, b):
    print('Cálculo da Divisão:')
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."