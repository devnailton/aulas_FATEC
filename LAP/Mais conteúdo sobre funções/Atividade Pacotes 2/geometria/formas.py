pi = 3.141592653589793

def area_retangulo(largura, altura):
    print('Cálculo da área do Retângulo:')
    return largura * altura

def raio_circulo(area):
    print('Cálculo do Raio de um círculo:')
    if area <= 0:
        return "A área deve ser um valor positivo."
    raio = (area / pi) ** 0.5
    return raio

def area_circulo(raio):
    print('Cálculo da Área de um círculo:')
    if raio <= 0:
        return "O raio deve ser um valor positivo."
    area = pi * raio ** 2 
    return area