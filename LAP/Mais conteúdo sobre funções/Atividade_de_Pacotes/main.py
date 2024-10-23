#from matematica import *
from matematica import soma, subtracao, divisao, multiplicacao
from matematica.avancados.cubo import cubo
from matematica.avancados.quadrado import quadrado

a = 10
b = 5

print(f"Soma: {soma(a, b)}")
print(f"Subtração: {subtracao(a, b)}")
print(f"Divisão: {divisao(a, b)}")
print(f"Multiplicação: {multiplicacao(a, b)}")
print(f"Quadrado de {a}: {quadrado(a)}")
print(f"Cubo de {a}: {cubo(a)}")