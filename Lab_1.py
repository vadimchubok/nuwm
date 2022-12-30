import math
import matplotlib.pyplot as plt

N = 9
H_1 = 1.5 + 0.1 * math.sin(N)  
H_2 = 0.5 + 0.1 * math.cos(N)
k = 1.25  
L = 50 
D = 0.01 * N
V = (H_1 - H_2) * k / L 
y = 0.065  
G = 0.2  

arnum = 0

n = 20  
t = 30   
T = 4  
h = L / n  
C = 0.1 * k  

Fk = G / (D * t)
Fplus = y * C / D
M = 1 / (1 + (h * V) / (2 * D))
rminus = -V / D
a = M / math.pow(h, 2) - rminus / h
b = M / (h*h)
firstArray = [arnum]
arr = []
c = 2*M/(h*h)-rminus/h+0/D+G/(D*t)

def drawarr(arrayForDraw):
    for i in range(len(arrayForDraw)):
        plt.plot([x*h for x in range(len(arrayForDraw[i]))],
        [x for x in arrayForDraw[i]])
    plt.show()

def prinFirstArray():
    for i in range(T):
        arr.append(N - b + math.pow(math.sin(N * L),2)* t)
    for i in range(1, n - 1):
        firstArray.append(round((rminus-6)+ math.pow(math.sin(N * n * i),2),5))
    firstArray.append(N - b + math.pow(math.sin(N * L),2)* 1)
    print(firstArray)
    arrayForDrawing = [firstArray.copy()]
    printSecondArray(arrayForDrawing)

def printSecondArray(arrayForDraw):

    for i in range(1, T):
        secondArray = [arr[i]]
        L = [0]
        B = [arnum]
        for j in range(1, n):
            L.append(b / (c - a * L[j - 1]))
            B.append((a * B[j - 1] + firstArray[j] * Fk + Fplus) / (c - a * L[j - 1]))
        for k in range(n - 1, 0, -1):
            secondArray.append(round(L[k] * secondArray[n - 1 - k] + B[k], 5))
        secondArray.append(arnum)
        secondArray.reverse()
        arrayForDraw.append(secondArray)
        firstArray[:] = secondArray[:]
        print(secondArray)
    drawarr(arrayForDraw) 
prinFirstArray()
