senha_correta = "segredo123"
senha1 = input("Digite sua senha: ")
if senha1 == senha_correta:
    print("Acesso permitido")
else:
    print("Senha incorreta")
    tentativas_restantes1 = 2
    while tentativas_restantes1 > 0:
        senha1 = input("Digite sua senha novamente: ")
        if senha1 == senha_correta:
            print("Acesso permitido")
            break
        else:
            tentativas_restantes1 -= 1
            print(f"Tentativas restantes: {tentativas_restantes1}")
    if tentativas_restantes1 == 0:
        print("Número de tentativas excedido. Acesso bloqueado.")

senha2 = input("Digite sua senha: ")
if senha2 == senha_correta:
    print("Acesso permitido")
else:
    print("Senha incorreta")
    tentativas_restantes2 = 2
    while tentativas_restantes2 > 0:
        senha2 = input("Digite sua senha novamente: ")
        if senha2 == senha_correta:
            print("Acesso permitido")
            break
        else:
            tentativas_restantes2 -= 1
            print(f"Tentativas restantes: {tentativas_restantes2}")
    if tentativas_restantes2 == 0:
        print("Número de tentativas excedido. Acesso bloqueado.")


senha3 = input("Digite sua senha: ")
if senha3 == senha_correta:
    print("Acesso permitido")
else:
    print("Senha incorreta")
    tentativas_restantes3 = 2
    while tentativas_restantes3 > 0:
        senha3 = input("Digite sua senha novamente: ")
        if senha3 == senha_correta:
            print("Acesso permitido")
            break
        else:
            tentativas_restantes3 -= 1
            print(f"Tentativas restantes: {tentativas_restantes3}")
    if tentativas_restantes3 == 0:
        print("Número de tentativas excedido. Acesso bloqueado.")


##Otimizado
def solicitar_senha():
    return input("Digite sua senha: ")

def verificar_senha(senha_digitada, senha_correta):
    if senha_digitada == senha_correta:
        print("Acesso permitido")
        return True
    else:
        print("Senha incorreta")
        return False

def autenticar_usuario(senha_correta, tentativas=3):
    while tentativas > 0:
        senha_digitada = solicitar_senha()
        if verificar_senha(senha_digitada, senha_correta):
            return True
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")
    
    print("Número de tentativas excedido. Acesso bloqueado.")
    return False

senha_correta = "segredo123"

autenticar_usuario(senha_correta)
autenticar_usuario(senha_correta)
autenticar_usuario(senha_correta)