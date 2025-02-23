def solicitar_usuario():
    palavras_a = []
    demais_palavras = []
    
    for x in range(10):
        palavra = input(f"Digite a {x+1}ª palavra: ")
        
        if palavra.lower().startswith('a'):
            palavras_a.append(palavra)
        else:
            demais_palavras.append(palavra)

    with open('palavra_a.txt', 'w') as arquivo_a:
        for palavra in palavras_a:
            arquivo_a.write(palavra + "\n")

    with open('demais_palavras.txt', 'w') as arquivo_demais:
        for palavra in demais_palavras:
            arquivo_demais.write(palavra + "\n")

solicitar_usuario()