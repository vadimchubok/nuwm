import math
import matplotlib.pyplot as plot

N = 9
k = 1.5  
G = 0.4  
l = 100   

n = 10  
t = 30  
T = 5  
h = l / n  
y = 0.0065  

D = 0.00001  
C = 0.1 * k  
Cp = 4.2 * math.pow(10, 6)  
Cn = 3 * math.pow(10, 6)  
lam = 0.3  
Dt = lam / Cp  
C0 = 5
C1 = 35
C2 = 5
T0 = 10
T1 = 30
T2 = 10
H1 = 5
H2 = 1
V = (H1 - H2) * k / l


def get_coef(M, Rp, Rm, add):
    a = M / math.pow(h, 2) - Rm / h
    b = M / math.pow(h, 2) + Rp / h
    c = a + b + add

    return a, b, c
def get_F(T):
    F = []
    for i in range(0, len(T)-1):
        F.append([])
        for j in range(1, len(T[i+1])-1):
            F[i].append(Dt*(T[i+1][j-1]-2*T[i+1][j]+T[i+1][j+1])/(D*h**2))
    return F


def massTrans(F):
    Fk = G / (D * t)
    Fplus = y * C / (2 * D)
    M = 1 / (1 + (h * V) / (2 * D))
    r = -V / D
    a, b, c = get_coef(M, 0, r, y / D + G / (D * t))
    firstArray = [C1]
    for i in range(1, n):
        firstArray.append(C0)
    firstArray.append(C2)
    print("Mass")
    print(firstArray)

    DrawingArray = [firstArray.copy()]
    for i in range(1, T):
        secondArray = [C2]
        L = [0]
        B = [C1]
        for j in range(1, n):
            L.append(b / (c - a * L[j - 1]))
            B.append((a * B[j - 1] + Fk * firstArray[j] + Fplus + F[i-1][j-1]) / (c - a * L[j - 1]))
        for j in range(n - 1, 0, -1):
            secondArray.append(round(L[j] * secondArray[n - 1 - j] + B[j], 5))
        secondArray.append(C1)
        secondArray.reverse()
        DrawingArray.append(secondArray)
        firstArray[:] = secondArray[:]
        print(secondArray)

    return DrawingArray

def heatTrans():
    firstArray = [T1]
    r = -V * Cp / lam
    M = 1 / (1 + 0.5 * h * math.fabs(r))
    nT = Cn / lam
    Fk = nT / t
    a, b, c = get_coef(M, 0, r, Fk)

    for i in range(1, n):
        firstArray.append(T0)
    firstArray.append(T2)
    print("Heat")
    print(firstArray)

    DrawingArray = [firstArray.copy()]
    for i in range(1, T):
        secondArray = [T2]
        L = [0]
        B = [T1]
        for j in range(1, n):
            L.append(b / (c - a * L[j - 1]))
            B.append((a * B[j - 1] + Fk * firstArray[j]) / (c - a * L[j - 1]))
        for j in range(n - 1, 0, -1):
            secondArray.append(round(L[j] * secondArray[n - 1 - j] + B[j], 5))
        secondArray.append(T1)
        secondArray.reverse()
        DrawingArray.append(secondArray)
        firstArray[:] = secondArray[:]
        print(secondArray)
    return DrawingArray

firstDrawingArray = heatTrans()
F = get_F(firstDrawingArray)
secondDrawingArray = massTrans(F)

def teploperenos():
    for i in range(len(firstDrawingArray)):
        plot.plot([p * h for p in range(len(firstDrawingArray[i]))], [p for p in firstDrawingArray[i]], label='{} time layer'. format(i))
    plot.legend()
    plot.show()

def teplomasoperenos():
    for i in range(1, len(secondDrawingArray)):
        plot.plot([p * h for p in range(len(secondDrawingArray[i]))], [p for p in secondDrawingArray[i]], label='{} time layer'. format(i))
    plot.legend()
    plot.show()

teploperenos()
teplomasoperenos()
