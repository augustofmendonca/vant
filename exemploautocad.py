import math as mt
from pyautocad import Autocad, APoint
import numpy as np

acad = Autocad(create_if_not_exists=True)



fator_a1= float(input("digite o fator a1: "))
fator_b = float(input("digite o fator b: "))


x=[]
y=[]


for i in range(0,100):
    x.append(fator_a1*mt.cos(i))
    y.append(fator_b*mt.sin(i))
    

for i in range (0,99):
    l1 = acad.model.AddLine(APoint(x[i],y[i]), APoint(x[i+0.0001],y[i+0.0001]))

