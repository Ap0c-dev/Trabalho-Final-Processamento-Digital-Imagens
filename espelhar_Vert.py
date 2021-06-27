import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")   

imagemOriginal = Image.open(sys.argv[1])
imagemEspelhadaVert = imagemOriginal.transpose(Image.FLIP_TOP_BOTTOM)
imagemEspelhadaVert.save(sys.argv[2])    