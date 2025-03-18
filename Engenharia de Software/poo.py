class Celular:
    marca = 'Nokia'
    modelo = 'Inquebrável'
    cor = 'Azul'
    tem_camera = False
    bateria = 10000000

    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')



celular_da_maria = Celular()
celular_do_Lucas = Celular()


celular_da_maria.jogar_cobrinha()
celular_do_Lucas.fazer_ligacoes()
celular_do_Lucas.cor = "Preto"

print(celular_do_Lucas.cor)