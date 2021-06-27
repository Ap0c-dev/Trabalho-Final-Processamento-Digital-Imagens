# -*- coding: utf:8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
     
    for i, arg in enumerate(sys.argv):
        if (i == 1):
            entradaPrincipal = arg
        elif (i == 2):                
            saidaPrincipal = arg
        elif (i == 3):
            teste = arg

entrada = open (sys.argv[1], "r+")
saida = open (sys.argv[2], "w+")

original = Image.open(entradaPrincipal)
imgPng = original.convert('RGBA')

pixels = list(imgPng.getdata())

for i, p in enumerate(pixels):
    pixels[i] = (p[0], p[1], p[2], int(teste) * 3)

outputImg = Image.new('RGBA', original.size)
outputImg.putdata(pixels)

entrada.close()
saida = outputImg.save(saidaPrincipal)