from random import randint


def buscaBinaria(x, vector, begin, end):
    meio = (begin + end) // 2
    if x not in vector:
        return -1
    else:
        if x == vector[meio]:
            return x
        elif x < vector[meio]:
            return buscaBinaria(x, vector, begin, meio)
        else:
            return buscaBinaria(x, vector, meio, end)

z, y = 0, 0
numeros = [0]
numeros[0] = randint(0, 10)
for c in range(1, 50):
    numeros.append(numeros[c - 1] + 2)
print(numeros)
num = int(input())
c = buscaBinaria(num, numeros, y, len(numeros))
print(c)
