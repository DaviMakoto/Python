from tkinter import *

telaInicial = Tk() #Instanciar
telaInicial['bg'] = '#cc22fa' # Altera cor de fundo
telaInicial.title('Minha Primeira Tela')

largura = 850 # altura do programa
altura = 650 # largura do programa
larguraUser = telaInicial.winfo_screenwidth() # 1920 - 850 = 1070 / 2 = 535
alturaUser = telaInicial.winfo_screenheight()
print(larguraUser, alturaUser) # Tela do usuário
larguraX = int((larguraUser - largura)/2)
alturaY = int((alturaUser - altura)/2)
telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(False, False)
telaInicial.minsize(850, 650)
telaInicial.maxsize(1070, 650)

def entrar():
    print('UUUUUUI!')

btnEntrar = Button(telaInicial, text='Botão do Ryan', command=entrar) # Cria instância do botão
btnEntrar.pack()

labMsg = Label(telaInicial, text='Label')
labMsg.pack()

# Última linha
telaInicial.mainloop() # Abre uma tela