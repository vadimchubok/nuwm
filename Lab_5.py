import math
import matplotlib.pyplot as plot

N = 9
l = 100  
h = 10  
t = 30  
T = 5  
k = 0.001  
G = 0.4  
y = 0.0002  
Y = 20000  
D = 0.02  
C = 0.15  
e = 0.6  
H1 = 59
H2 = 26
C1 = 350
C2 = 8
n = int(l / h)  
v = 2.8 * math.pow(10, -3)  
aa = 51.2 * math.pow(10, -7)  
V = (H1 - H2) * k / l  
Aa = k * (1 + e) / (Y * aa)
Bb = v * (1 + e) / (Y * aa)

def get_a_b_c(M, Rp, Rm, add):
    a = M / math.pow(h, 2) - Rm / h
    b = M / math.pow(h, 2) + Rp / h
    c = a + b + add
    return a, b, c

def get_F(T):
    F = []
    for i in range(0, len(T) - 1):
        F.append([])
        for j in range(1, len(T[i + 1]) - 1):
            F[i].append(T[i + 1][j - 1] - 2 * T[i + 1][j] + T[i + 1][j + 1])
    return F

def NaporWuthFiltr(F):
    FkC = Bb / h ** 2
    FkH = 1 / t
    a = b = Aa / h ** 2
    c = 1 / t - 2 * a
    firstArray = [H1]
    for i in range(1, n):
        firstArray.append((H2 - H1) * i * h / l + H1)
    firstArray.append(H2)
    print(firstArray)
    firstarrayForDrawing = [firstArray.copy()]
    for i in range(1, T):
        secondArray = [H2]
        L = [0]
        B = [H1]
        for j in range(1, n):
            L.append(b / (c - a * L[j - 1]))
            B.append((a * B[j - 1] + FkH * firstArray[j] + FkC * F[i - 1][j - 1]) / (c - a * L[j - 1]))
        for j in range(n - 1, 0, -1):
            secondArray.append(round(L[j] * secondArray[n - 1 - j] + B[j], 5))
        secondArray.append(H1)
        secondArray.reverse()
        firstarrayForDrawing.append(secondArray)
        firstArray[:] = secondArray[:]
        print(secondArray)
    return firstarrayForDrawing
def Masoperenos():
    Fk = G / (D * t)
    Fplus = C * y / D
    M = 1 / (1 + (V * h) / (2 * D))
    r = - V / D
    a, b, c = get_a_b_c(M, 0, r, y / D + Fk)
    firstArray = [C1]
    for i in range(1, n):
        firstArray.append(round(C1 * math.exp(-i * h * math.log(C1 / C2) / l), 5))
    firstArray.append(C2)
    print(firstArray)
    array_plot = [firstArray.copy()]
    for i in range(1, T):
        secondArray = [C2]
        L = [0]
        B = [C1]
        for j in range(1, n):
            L.append(b / (c - a * L[j - 1]))
            B.append((a * B[j - 1] + Fk * firstArray[j] + Fplus) / (c - a * L[j - 1]))
        for j in range(n - 1, 0, -1):
            secondArray.append(round(L[j] * secondArray[n - 1 - j] + B[j], 5))
        secondArray.append(C1)
        secondArray.reverse()
        array_plot.append(secondArray)
        firstArray[:] = secondArray[:]
        print(secondArray)
    return array_plot

firstarrayForDrawing = Masoperenos()
F = get_F(firstarrayForDrawing)
secondArrayForDrawing = NaporWuthFiltr(F) 

def drawMasoperenos():
    for i in range(len(firstarrayForDrawing)):
        plot.plot([p * h for p in range(len(firstarrayForDrawing[i]))], [p for p in firstarrayForDrawing[i]])
    plot.show()

def drawNaporWuthFiltr():
    for i in range(len(secondArrayForDrawing)):
        plot.plot([p * h for p in range(len(secondArrayForDrawing[i]))], [p for p in secondArrayForDrawing[i]])
    plot.show()
drawMasoperenos()
drawNaporWuthFiltr()
