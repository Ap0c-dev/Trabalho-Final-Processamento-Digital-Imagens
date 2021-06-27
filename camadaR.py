import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginalR = Image.open(sys.argv[1])

matriz = imagemOriginalR.load()

for i in range(imagemOriginalR.size[0]):
    for j in range(imagemOriginalR.size[1]):
        r = matriz[i, j][0]
        matriz[i,j] = (r, 0, 0)

imagemOriginalR.save(sys.argv[2])