import sys
from PIL import Image, ImageFilter

tamanhoHeader = 100 
textoOculto = "Não existem métodos fáceis para resolver problemas difíceis - Rene Descartes"

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

def __init__(self):

    self.contador = 0
    self.novosDados = ''
    self.original_image = ''
    self.textoAesconder = ''

    
    for i in range(0, tamanhoHeader):
        Image.open('imagens/img_transp.png')
        self.dadosImagem = self.original_image[i]
        self.contador += 1


        for char in range(0, len(self.esc_txt)):
            Image.open('imagens/img_transp.png')
            charAtual = self.esc_txt[char] 
            vlrAtual = '{0:0b}'.format(ord(charAtual)) 

            for bit in range(0, len(vlrAtual)):
                novoBin = ''

                #Substituindo o byte da imagem com o bit atual
                vlrBinAtual = '{0:09b}'.format((self.original_image[self.contador]))
                novoBin = vlrBinAtual[:7]
                novoBin += vlrAtual[bit]

                novoByte = chr(int(novoBin, 2))

                self.novosDados = novoByte
                self.contador += 1

     #Copia o restante do arquivo 
        self.novosDados = self.original_image[self.contador:]


