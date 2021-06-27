import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])
imagemComFiltro = imagemOriginal.filter(ImageFilter.EMBOSS)
imagemComFiltro.save(sys.argv[2])