import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginal = Image.open(sys.argv[1])

imagemComBorda = ImageFilter.imagemOriginal((3,3), (0, 1, 0, 1, -5, 1, 0, 1, 0), 1, 0 )

imagem = imagemOriginal.filter(imagemComBorda)
imagemComBorda.save(sys.argv[2])