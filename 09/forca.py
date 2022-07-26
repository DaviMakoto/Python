from random import randint

palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao',
'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa',
'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = randint(0, len(palavras) - 1)
palavra_secreta = palavras[indice]
tentativa = []
chutes = []

for i in range(len(palavra_secreta)):
    tentativa.append('_')
print(palavra_secreta)
print(tentativa)


def exibirMsg(msg):
    print(msg)

def jogar():
    tentativas = 5
    while(True):
        chute = input('Digite uma letra: ')
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        else:
            exibirMsg(f'Letra {chute} não encontrada')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas!')
            exibirMsg(tentativa)

        if(tentativas <= 0):
            exibirMsg('Você perdeu ;( \nJOGUE NOVAMENTE!')
            exibirMsg(f'A palavra secreta era {palavra_secreta.upper()}')
            break

def encontraLetra(chute):
    temLetra = False
    for i, letra in enumerate(palavra_secreta):
        if (chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra
       
        

while(True):
    exibirMsg('!!!!!!!!!!Jogo da forca!!!!!!!!!!!!')
    menu = int(input(' 1 - Jogar \n 2 - Sair \n R:'))
    if(menu == 1):
        jogar()
    else:
        print('Tchau')
        break