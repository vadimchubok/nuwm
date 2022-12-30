
import math
import matplotlib.pyplot as plot
import random

D=1.7
Q=1.5
y=0.05
L=20
n=20
x0=9
h=L/n

x1=2.8
C1=0.416
C_1=0.4
A1=lambda x: math.sinh(math.sqrt(y/D)*(L-x))
A2=lambda x: math.sinh(math.sqrt(y/D)*x)

def con(x):
    Cx=[]
    for i in range(n+1):
        if i*h<x:
            Cx.append((Q/(math.sqrt(y/D)*D*math.sinh((math.sqrt(y/D)*L))))*A1(x)*math.sinh(math.sqrt(y/D)*i*h))
        else:
            Cx.append((Q/(math.sqrt(y/D)*D*math.sinh((math.sqrt(y/D)*L))))*A2(x)*math.sinh(math.sqrt(y/D)*(L-i*h)))        
    return Cx

def get_x(xi,C):
    if 0<x1<L/2:
        return L-math.asinh(C/((Q/(math.sqrt(y/D)*D*math.sinh((math.sqrt(y/D)*L))))*math.sinh(math.sqrt(y/D)*xi)))/math.sqrt(y/D)
    else:
        return math.asinh((C/((Q/(math.sqrt(y/D)*D*math.sinh((math.sqrt(y/D)*L))))*math.sinh(math.sqrt(y/D)*(L-xi)))))/math.sqrt(y/D)

Cx=con(x0)
firstArray=sorted([random.uniform(0, 10) for i in range(9)])
firstArray.append(L/2)
print("mass ", firstArray, sep=' ')
secondArray=[con(i) for i in firstArray]
def grafrosp():
    plot.plot([p*h for p in range(len(Cx))],[p for p in Cx])
    plot.show()
def grafZall():
    for i in range(len(secondArray)):
        plot.plot([p*h for p in range(len(secondArray[i]))], [p for p in secondArray[i]])
    plot.show()

x01=get_x(x1, C1)
x_0=get_x(x1, C_1)
print('accurate', x01, sep=' = ')
print('approx', x_0, sep=' = ')
grafZall()
grafrosp()
