from aritmetica.operacoes import soma, divisao
from geometria.formas import area_retangulo, raio_circulo, area_circulo

def obter_valores_usuario():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1, valor2

def salvar_resultados(resultado):
    with open("resultados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(resultado + "\n")

def ler_resultados():
    with open("resultados.txt", "r", encoding="utf-8") as arquivo:
        #conteudo = arquivo.readlines()
        for linha in arquivo:
            try:
                conteudo = linha.strip()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
    return conteudo

def main():
    a, b = obter_valores_usuario()
    resultado_soma = soma(a, b)
    resultado_soma = f"A soma de {a} e {b} é: {resultado_soma}"
    print(resultado_soma)
    salvar_resultados(resultado_soma)  

    num, den = obter_valores_usuario()
    resultado_divisao = divisao(num, den)
    resultado_divisao_str = f"O resultado da divisão de {num} por {den} é: {resultado_divisao}"
    print(resultado_divisao_str)
    salvar_resultados(resultado_divisao_str)  

    largura, altura = obter_valores_usuario()
    area = area_retangulo(largura, altura)
    area_retangulo_str = f"A área do retângulo de largura {largura} e altura {altura} é: {area}"
    print(area_retangulo_str)
    salvar_resultados(area_retangulo_str)  

    raio = float(input("Digite o raio do círculo para calcular a área: "))
    area_do_circulo = area_circulo(raio)
    area_circulo_str = f"A área do círculo com raio {raio} é: {area_do_circulo}"
    print(area_circulo_str)
    salvar_resultados(area_circulo_str)  

    area = float(input("Digite a área do círculo para calcular o raio: "))
    raio_calculado = raio_circulo(area)
    raio_calculado_str = f"O raio do círculo com área {area} é: {raio_calculado}"
    print(raio_calculado_str)
    salvar_resultados(raio_calculado_str)  

    print("Todos os resultados foram salvos no arquivo 'resultados.txt'.")

    conteudo_resultados = ler_resultados()
    print(conteudo_resultados)

if __name__ == "__main__":
    main()