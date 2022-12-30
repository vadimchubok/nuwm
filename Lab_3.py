import math
import matplotlib.pyplot as plot
import numpy as np

N = 9
k = 1.5  
hx = 10  
hy = 2  
Lx = 100  
By = 10  
t = 30   
D = 0.02  
G = 0.4  
y = 0.0065  
Cm = 350  
C1 = 350
C2 = 8 * N
H1 = 1.5
H2 = 0.5

nx = int(Lx / hx)
ny = int(By / hy)
C = 0.1 * Cm
V = (H1 - H2) * k / Lx   
M = 1 / (1 + (hx * V) / (2 * D))
r = -V / D
add = y / (2 * D) + G / (D * t)
a1 = M / math.pow(hx, 2) - r / hx
b1 = M / math.pow(hx, 2)
c1 = a1 + b1 + add
a2 = 1 / hy ** 2
b2 = a2
c2 = a2 + b2 + add
Fk = G / (D * t)
Fplus = y * C / (2 * D)

def drawArray():
    drawingArray = []
    for i in range(0, int(4.5 * t), int(t / 2)):
        drawingArray = massTrans(i, drawingArray)
        if i % t == 0:
            for j in range(len(drawingArray)):
                plot.plot([p * hx for p in range(len(drawingArray[j]))], [p for p in drawingArray[j]], label='{} step'. format(j))
            plot.title('two-dimensional mass transfer on the time layer {}'.format(i))
            plot.legend()
            plot.show()

def massTrans(T, firstArray):
    secondArray = []
    if T == 0:
        print("Mass in t = 0")
        for i in range(ny + 1):
            firstArray.append([C1])
            if i == 0:
                for j in range(1, nx):
                    firstArray[i].append(Cm)
                firstArray[i].append(C2)
                print(firstArray[i])
            else:
                for j in range(1, nx):
                    firstArray[i].append((C2 - C1) * j * hx / Lx + C1)
                firstArray[i].append(C2)
                print(firstArray[i])
        return firstArray
    elif T % t == 0:
        print("Mass in t = {}".format(T))
        for i in range(nx + 1):
            if i == 0:
                secondArray.append([C1])
                for j in range(ny):
                    secondArray[i].append(C1)
            elif i == nx:
                secondArray.append([C2])
                for j in range(ny):
                    secondArray[i].append(C2)
            else:
                L = [0]
                B = [Cm]
                for j in range(1, ny):
                    L.append(b2 / (c2 - a2 * L[j - 1]))
                    B.append((a2 * B[j - 1] + Fk * firstArray[j][i] + Fplus) / (c2 - a2 * L[j - 1]))
                secondArray.append([round(B[-1] / (1 - L[-1]), 5)])
                for j in range(ny - 1, 0, -1):
                    secondArray[i].append(round(L[j] * secondArray[i][ny - 1 - j] + B[j], 5))
                secondArray[i].append(Cm)
                secondArray[i].reverse()

        secondArray = [list(i) for i in zip(*secondArray)]
        for i in range(len(secondArray)):
            print(secondArray[i])
        return secondArray
    else:
        print("Mass in t = {}".format(T))
        for i in range(ny + 1):
            if i == 0:
                secondArray.append([C1])
                for j in range(1, nx):
                    secondArray[i].append(Cm)
                secondArray[i].append(C2)
                print(secondArray[i])
            else:
                secondArray.append([C2])
                L = [0]
                B = [C1]
                for j in range(1, nx):
                    L.append(b1 / (c1 - a1 * L[j - 1]))
                    B.append((a1 * B[j - 1] + Fk * firstArray[i][j] + Fplus) / (c1 - a1 * L[j - 1]))
                for j in range(nx - 1, 0, -1):
                    secondArray[i].append(round(L[j] * secondArray[i][nx - 1 - j] + B[j], 5))
                secondArray[i].append(C1)
                secondArray[i].reverse()
                print(secondArray[i])
        return secondArray


drawArray()