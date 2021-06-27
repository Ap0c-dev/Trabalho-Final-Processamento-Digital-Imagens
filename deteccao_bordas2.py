import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginal = Image.open(sys.argv[1])

kernel = ImageFilter.Kernel((3,3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1, 0)

imagemComBorda = imagemOriginal.filter(kernel)
imagemComBorda.save(sys.argv[2])