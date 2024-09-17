import time 
import math as mt
from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
arq_nome = acad.doc.Name

'''dimensão do modelo solido'''
comprimento= float(input('digite o comprimento do sólido em centímetros(insira somente números): '))
fator_k = float(input('digite o fator k(insira somente números): '))
fator_b = float(input('digite o fator b(insira somente números): '))
fator_a= comprimento/(1+fator_k)


'''definição do passo'''
passo= mt.pi/10000
abertura= (2*(mt.pi))/4
area=0
angulo=[]
x=[]
z=[fator_a]
arco1=[]
arco2=[]
deslocamento=[]
"""10002"""
for i in range(1,10002):
    x.append(0)
    angulo.append(0)
    arco1.append(0)
    arco2.append(0)
    deslocamento.append(0)

"""10000"""
for i in range(-1,10000):
    angulo[i+1]= i* passo
    x[i+1]= fator_b* mt.sin(angulo[i+1])
    if(angulo[i+1] > mt.pi/2):
        z.append(fator_a * fator_k * mt.cos(angulo[i+1]))
    else:
         z.append(fator_a * mt.cos(angulo[i+1]))
    deslocamento[i+1]=mt.sqrt(((x[i+1]-x[i])**2)+((z[i+2]-z[i])**2))+deslocamento[i]
    arco1[i+1]=(abertura*x[i+1])/2
    arco2[i+1]=(-abertura*x[i+1])/2
    area=((arco1[i+1]-arco2[i+1]+arco1[i]-arco2[i])*((deslocamento[i+1]-deslocamento[i])/2)) + area

print("aguarde, gerando arquivo......")

for i in range(0,10000):
    l1 = acad.model.AddLine(APoint(arco1[i],deslocamento[i]), APoint(arco1[i+1], deslocamento[i+1]))   
    l2 = acad.model.AddLine(APoint(arco2[i],deslocamento[i]), APoint(arco2[i+1], deslocamento[i+1]))
print(f"processo completo(checar arquivo {arq_nome})")



