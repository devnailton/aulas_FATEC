from aritmetica.operacoes import soma, divisao
from geometria.formas import area_retangulo, raio_circulo, area_circulo

def obter_valores_usuario():
    """Solicita ao usuário dois valores numéricos e os retorna."""
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1, valor2

def main():
    a, b = obter_valores_usuario()
    resultado_soma = soma(a, b)
    print(f"A soma de {a} e {b} é: {resultado_soma}")

    num, den = obter_valores_usuario()
    resultado_divisao = divisao(num, den)
    print(f"O resultado da divisão de {num} por {den} é: {resultado_divisao}")

    largura, altura = obter_valores_usuario()
    area = area_retangulo(largura, altura)
    print(f"A área do retângulo de largura {largura} e altura {altura} é: {area}")

    raio = float(input("Digite o raio do círculo para calcular a área: "))
    area_do_circulo = area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {area_do_circulo}\n")

    area = float(input("Digite a área do círculo para calcular o raio: "))
    raio_calculado = raio_circulo(area)
    print(f"O raio do círculo com área {area} é: {raio_calculado}\n")

if __name__ == "__main__":
    main()