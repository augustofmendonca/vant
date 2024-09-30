import math as mt
from pyautocad import Autocad, APoint
import numpy as np

acad = Autocad(create_if_not_exists=True)
arq_nome = acad.doc.name

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


passo_t=(2*mt.pi)/40
passo_zs=[comprimento/100,((comprimento-((20*comprimento)/100))/50)]
t_atual=0
z_atual=fator_a
raios=[]
volume=0
soma_centro=0
desenho3d=[]
j=1

print("aguarde, gerando arquivo......")
"""(1)=[0]/ (2)=[1]"""
for i in range(0, 71*40):
    if (i % 40 == 1 and i>40): 
        j=j+1
        if (j<=11):
            z_atual=z_atual-passo_zs[0]
            passo_z=passo_zs[0]
        elif (j<=61): 
            z_atual=z_atual-passo_zs[1]
            passo_z=passo_zs[1]
        else:
            z_atual=z_atual-passo_zs[0]
            passo_z=passo_zs[0]

        if(z_atual>=0):
            raios[j]= fator_b * mt.sqrt(1-(z_atual/fator_a)**2)
        elif (j==71):
            raios[j]=0
        else:
            raios[j]= fator_b * mt.sqrt(1-(z_atual/(fator_k*fator_a))**2)

        if(raios[j]>=raios[j-1]):
            volume=volume + mt.pi*passo_z*((raios[j]**2)+(raios[j-1]**2))+(raios[j]*raios[j-1])/3;
            soma_centro=soma_centro+(z_atual+passo_z*((raios[j]**2)+2*raios[j]*raios[j-1]+3*raios[j-1]**2)/(4*(raios[j]**2+raios[j]*raios[j-1]+raios[j-1]**2)))*(mt.pi*passo_z*(raios[j]**2+raios[j-1]**2+raios[j]*raios[j-1])/3);
        else:
            volume=volume+mt.pi*passo_z*(raios[j]**2+raios[j-1]**2+raios[j]*raios[j-1])/3;
            soma_centro=soma_centro+(z_atual+passo_z-passo_z*(3*raios[j]**2+2*raios[j]*raios[j-1]+raios[j-1]**2)/(4*(raios[j]**2+raios[j]*raios[j-1]+raios[j-1]**2)))*(mt.pi*passo_z*(raios[j]**2+raios[j-1]**2+raios[j]*raios[j-1])/3);

    secoes3d=np.identity(71*40)
    for i in range(0,71*40):
        raios.append(0)
    secoes3d[0][i]=raios[j]*mt.cos(t_atual) 
    secoes3d[1][i]=raios[j]*mt.sin(t_atual)
    secoes3d[2][i]=z_atual
    
    """verificar esta parte (variaveis para se plotar pontos)"""
    """if (i<40):
        desenho3d=desenho3d[secoes3d[1][i]/1000, secoes3d[2][i]/1000, secoes3d[0][i]/1000]
    elif (i % 40 ==0):
        desenho3d=desenho3d[secoes3d[1][i]/1000, secoes3d[2][i]/1000, secoes3d[0][i]/1000, secoes3d[i-41][2]/1000, secoes3d[i-41][3]/1000, secoes3d[i-41][1]/1000]
    else:
        desenho3d=desenho3d[secoes3d[1][i]/1000, secoes3d[2][i]/1000, secoes3d[0][i]/1000, secoes3d[i-40][2]/1000, secoes3d[i-40][3]/1000, secoes3d[i-40][1]/1000, secoes3d[i][2]/1000, secoes3d[i][3]/1000, secoes3d[i][1]/1000]"""
    
    t_atual=t_atual+passo_t

print("aguarde, gerando arquivo......")

"""passa codigo para o autocad""" """(diferenciar eixo x em l3 e l4)"""
for i in range(0,10000):
    l1 = acad.model.AddLine(APoint(arco1[i],deslocamento[i]), APoint(arco1[i+1], deslocamento[i+1]))   
    l2 = acad.model.AddLine(APoint(arco2[i],deslocamento[i]), APoint(arco2[i+1], deslocamento[i+1]))
    l3 = acad.model.AddLine(APoint(0,deslocamento[i],arco1[i]), APoint(0,deslocamento[i+1],arco1[i+1]))
    l4 = acad.model.AddLine(APoint(0,deslocamento[i],arco2[i]), APoint(0,deslocamento[i+1],arco2[i+1]))

print(f"processo completo(checar arquivo {arq_nome} no autocad)")


area_total=4*area 
centro_empuxo=soma_centro/volume
print("dados gerais do projeto:")
print(volume/1000000000)
print(area_total/1000000)
print(centro_empuxo/1000)
