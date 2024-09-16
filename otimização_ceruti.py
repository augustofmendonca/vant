import math as mt
import numpy as np

control=0
"""entrada de dados"""
x= int(input("digite o número de criterios de analise:")) 
matriz= np.identity(x)

for i in range(0,x):
    for j in range(0,x):
        if i == j:
            continue
        else:
            matriz[i][j]= int(input(f'digite[{i},{j}]'))

"""soma dos elementos da matriz"""
s=0
s1=0
"""soma dos elementos da linha da matriz"""
z=[]
"""pesos dos elementos"""
w=[]

"""calculo das somas"""
for i in matriz:
    for j in i:
        s = s+j
        s1= s1 +j
    z.append(s1)
    s1=0
    
for i in z:
    t= i/s
    w.append(t)


sig=[]
for i in z:
    sig1= mt.sqrt(i**2)
    sig.append(sig1)

"""calculo da matriz normalizada"""
var=[]
cl=0
y= int(input("digite o numero de valores das caracteristicas desejadas:"))
matriz1=np.identity(y)

for i in range(0,y):
    for j in range(0,y):
       matriz1[i][j]= float(input("digite os valores das caracteristicas desejadas:"))
       
for i in matriz1:
    for j in i: 
        var1= j/ (sig[cl])
        var.append(var1)
    cl=cl+1

"""bloco de contrução da matriz normalizada"""
matriznormalizada=np.identity(y)

for i in range(0,y):
    for j in range(0,y):
        for h in var:
            matriznormalizada[i][j]= h

"""matriz normalizada aplicada aos pesos"""
var6=[]
cl=0
for i in var:
    var5= i * w[cl] 
    var6.append(var5)
cl=cl+1

"""bloco de contrução da matriz normalizada aplicada aos pesos"""
matriznormalizada_p=np.identity(y)

for i in range(0,y):
    for j in range(0,y):
        for h in var6:
            matriznormalizada_p[i][j]= h

"""bloco de prints"""
print(matriz)
print(s)
print(z)

cont=0
for i in w:
    cont= cont +1
    print(f'peso{cont}:{i} ')

cont=0
for i in var:
    cont= cont +1
    print(f'tabela normalizada{cont}:{i} ')

cont=0
for i in var6:
    cont= cont +1
    print(f'tabela normalizada aplicada aos pesos{cont}:{i} ')
    
print(matriznormalizada)
print(matriznormalizada_p)
    
control= int(input("deseja realizar novo calculo?(1=sim/ 0=não)"))
  
"""bloco de repetição do programa"""
while (control == 1):
    """entrada de dados"""
    x= int(input("digite o número de criterios de analise:")) 
    matriz= np.identity(x)

    for i in range(0,x):
        for j in range(0,x):
            if i == j:
                continue
            else:
                matriz[i][j]= int(input(f'digite[{i},{j}]'))

    """soma dos elementos da matriz"""
    s=0
    s1=0
    """soma dos elementos da linha da matriz"""
    z=[]
    """pesos dos elementos"""
    w=[]

    """calculo das somas"""
    for i in matriz:
        for j in i:
            s = s+j
            s1= s1 +j
        z.append(s1)
        s1=0
    
    for i in z:
        t= i/s
        w.append(t)


    sig=[]
    for i in z:
        sig1= mt.sqrt(i**2)
        sig.append(sig1)

    """calculo da matriz normalizada"""
    var=[]
    cl=0
    y= int(input("digite o numero de valores das caracteristicas desejadas:"))
    matriz1=np.identity(y)

    for i in range(0,y):
        for j in range(0,y):
           matriz1[i][j]= float(input("digite os valores das caracteristicas desejadas:"))
           
    for i in matriz1:
        for j in i: 
            var1= j/ (sig[cl])
            var.append(var1)
        cl=cl+1

    """bloco de contrução da matriz normalizada"""
    matriznormalizada=np.identity(y)

    for i in range(0,y):
        for j in range(0,y):
            for h in var:
                matriznormalizada[i][j]= h

    """matriz normalizada aplicada aos pesos"""
    var6=[]
    cl=0
    for i in var:
        var5= i * w[cl] 
        var6.append(var5)
    cl=cl+1

    """bloco de contrução da matriz normalizada aplicada aos pesos"""
    matriznormalizada_p=np.identity(y)

    for i in range(0,y):
        for j in range(0,y):
            for h in var6:
                matriznormalizada_p[i][j]= h

    """bloco de prints"""
    print(matriz)
    print(s)
    print(z)

    cont=0
    for i in w:
        cont= cont +1
        print(f'peso{cont}:{i} ')

    cont=0
    for i in var:
        cont= cont +1
        print(f'tabela normalizada{cont}:{i} ')

    cont=0
    for i in var6:
        cont= cont +1
        print(f'tabela normalizada aplicada aos pesos{cont}:{i} ')
    
    print(matriznormalizada)
    print(matriznormalizada_p)
    
    control= int(input("deseja realizar novo calculo?(1=sim/ 0=não)"))
    
    