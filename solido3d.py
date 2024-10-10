import math as mt
from pyautocad import Autocad, APoint
import numpy as np
acad = Autocad(create_if_not_exists=True)

r=float(input("raio: "))

x2=[]
y2=[]
z2=0

x3=[]
y3=[]
z3=0

"""passo de giro dos circulos"""

step = 2.0*mt.pi/99.0

""" c = variavel de controle do raio """
c=0
""" b = variavel de controle da disperção dos circulos na distancia """
b=0
""" d = variavel de controle da impressão das linhas """
d=0

for j in range(0,14):
    x=[]
    y=[]
    x3=[]
    y3=[]
    for i in range(0,100):
        x.append(((r)*mt.cos(i*step)))
        y.append(((r)*mt.sin(i*step)))
        x3.append(((r)*mt.cos(i*step)))
        y3.append(((r)*mt.sin(i*step)))
        z3=b
    for i in range (0,99):
        l1 = acad.model.AddLine(APoint(x[i],y[i],b), APoint(x[i+1],y[i+1],b))
    
    if d >0:
        for i in range (0,99):   
            l2 = acad.model.AddLine(APoint(x2[i],y2[i],z2), APoint(x3[i+1],y3[i+1],z3))
    x2=x
    y2=y
    z2=b
    
    """condição elipse"""
    if c < 5:
        r=r+1
    elif c>=5:
        r=r-1
    c=c+1
    """condição elipse"""
    
    d=d+1
    b=b+1



