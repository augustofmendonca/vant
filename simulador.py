import math as mt
from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
arq_nome = acad.doc.name

print(f"welcome to AD&E system\n")
var = 1 #controla o looping while e garante a continuidade do sistema 
while var != 0:

    control=int(input("digite a opção desejada:(1 = impressão dos moldes/ 2 = solido 3D / 3 = simulação física )\n ------->"))
    
    if(control == 1):
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
            
            
        print("aguarde, gerando arquivo......")   


        for i in range(0,10000):
            l1 = acad.model.AddLine(APoint(arco1[i],deslocamento[i]), APoint(arco1[i+1], deslocamento[i+1]))   
            l2 = acad.model.AddLine(APoint(arco2[i],deslocamento[i]), APoint(arco2[i+1], deslocamento[i+1]))
            

        for i in range(0,10000):
            l3 = acad.model.AddLine(APoint(arco1[i],deslocamento[i]), APoint(arco1[i+1], deslocamento[i+1]))
            l3.Rotate(APoint(5+arco1[i],deslocamento[i]-5), -mt.pi/2)
            
            l4 = acad.model.AddLine(APoint(arco2[i],deslocamento[i]), APoint(arco2[i+1], deslocamento[i+1]))
            l4.Rotate(APoint(arco2[i]-5,deslocamento[i]-5), mt.pi/2)
    
         
        print(f"processo completo(checar arquivo {arq_nome} no autocad)")

    elif(control == 2):
        fator_a= float(input("digite o fator a1: "))
        fator_b = float(input("digite o fator b: "))

        print("                            ")
        print("gerando pontos, aguarde.... ")
        print("                            ")


        x_1=[]
        y_1=[]


        x2=[]
        y2=[]
        z2=0

        x3=[]
        y3=[]
        z3=0

        """passo de giro dos circulos"""

        step = 2.0*mt.pi/99.0

        for i in range(0,100):
            x_1.append(fator_a*mt.cos(i*step))
            y_1.append(fator_b*mt.sin(i*step))

        """ c = variavel de controle do raio """
        r=0
        """ b = variavel de controle da disperção dos circulos na distancia """
        b=0
        """ d = variavel de controle da impressão das linhas """
        d=0

        for j in range(0,99):
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
                    l2 = acad.model.AddLine(APoint(x2[i],y2[i],z2), APoint(x3[i],y3[i],z3))
            x2=x
            y2=y
            z2=b
            
            
            b=x_1[j]
            r=y_1[j]
            d=d+1

        print(f"processo completo(checar arquivo {arq_nome} no autocad)") 

    elif(control == 3):
        print("entrou na  simulação física\n")

    var= int(input("deseja continuar?(1= sim / 0 = não)\n ----->"))