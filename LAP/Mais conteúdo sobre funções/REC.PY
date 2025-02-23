def verificar(a):
    try:
        return a
    except ValueError:
        print("Erro: não é um formato valido")

nome = str(input("Insira seu nome: ")) 
sobrenome = str(input("Insira seu sobrenome: ")) 
idade = int(input("Insira sua idade: "))

resultado = verificar(idade)
print(nome, sobrenome, resultado)