import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginalG = Image.open(sys.argv[1])

matriz = imagemOriginalG.load()

for i in range(imagemOriginalG.size[0]):
    for j in range(imagemOriginalG.size[1]):
        g = matriz[i, j][0]
        matriz[i,j] = (0, g, 0)

imagemOriginalG.save(sys.argv[2])