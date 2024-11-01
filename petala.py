import math as mt
from pyautocad import Autocad, APoint
import numpy as np

acad = Autocad(create_if_not_exists=True)
arq_nome = acad.doc.name

'''dimensão do modelo solido'''
comprimento= float(input('digite o comprimento do sólido em centímetros(insira somente números):\n---> '))
fator_k = float(input('digite o fator k(insira somente números):\n---> '))
fator_b = float(input('digite o fator b(insira somente números):\n---> '))
n_petalas = int(input('digite a quantidade de petalas:\n---> '))
fator_a= comprimento/(1+fator_k)


'''definição do passo'''
passo= mt.pi/10000
abertura= 2*mt.pi/n_petalas
area=0
angulo=[0]
x=[0]
z=[fator_a]
arco1=[0]
arco2=[0]
deslocamento=[0]

"""inicia as listas"""
"""for i in range(1,10002):
    x.append(0)
    angulo.append(0)
    arco1.append(0)
    arco2.append(0)
    deslocamento.append(0)"""


for i in range(0,10000):
    angulo.append(i* passo)
    x.append(fator_b* mt.sin(angulo[i+1]))
    if(angulo[i+1] > mt.pi/2):
        z.append(fator_a * fator_k * mt.cos(angulo[i+1]))
    else:
         z.append(fator_a * mt.cos(angulo[i+1]))
    deslocamento.append(mt.sqrt(((x[i+1]-x[i])**2)+((z[i+1]-z[i])**2))+deslocamento[i])
    arco1.append((abertura*x[i+1])/2)
    arco2.append((-abertura*x[i+1])/2)
    area=((arco1[i+1]-arco2[i+1]+arco1[i]-arco2[i])*((deslocamento[i+1]-deslocamento[i])/2)) + area
    

"""arco2_= reversed(arco2)
deslocamento_= reversed(deslocamento)

exportar=[[arco1,arco2_], [deslocamento, deslocamento_] ]
mx=0
my=0
for i in range(len(exportar)):
    mx=mx + exportar[i][1]
    my=my + exportar[i][2]

mx=0
my= my/length(exportar)
viscircles[[mx, my], 10]
anterior=[-1, 0] 

for i in range(len(exportar)):
    dir1=[(exportar[i][1]-anterior[1]) , exportar[i][2]-anterior[2]] /(mt.sqrt(((exportar[i][1]-anterior[1])**2)+((exportar[i][2]-anterior[2])**2)))
    dir2=[dir1(2) -dir1(1)]
    ampliado[i][1]= exportar[i][1]+(dir2[1]*10)
    ampliado[i][2]= exportar[i][2]+(dir2[2]*10)
    anterior=[exportar[i][1] , exportar[i][2]]"""


print("aguarde, gerando arquivo......")   

for i in range(0,10000):
    l1 = acad.model.AddLine(APoint(arco1[i],deslocamento[i]), APoint(arco1[i+1], deslocamento[i+1]))   
    l2 = acad.model.AddLine(APoint(arco2[i],deslocamento[i]), APoint(arco2[i+1], deslocamento[i+1]))
print(f"processo completo(checar arquivo {arq_nome} no autocad)")




    