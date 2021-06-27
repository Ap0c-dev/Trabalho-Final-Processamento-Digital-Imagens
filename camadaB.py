import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginalB = Image.open(sys.argv[1])

matriz = imagemOriginalB.load()

for i in range(imagemOriginalB.size[0]):
    for j in range(imagemOriginalB.size[1]):
        b = matriz[i, j][0]
        matriz[i,j] = (0, 0, b)

imagemOriginalB.save(sys.argv[2])