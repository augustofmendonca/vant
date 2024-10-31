import math as mt

##dados do balão##
M_0= float(input("digite o valor de massa estrutural e componentes do balão:(Kg)\n--->"))
M_P= float(input("digite o valor de massa de carga útil:(Kg)\n--->"))
P_F= float(input("digite o valor de densidade do material do envelope:(Kg/m^2)\n--->"))
P_g0= int(input("escolha o gás a ser utilizado( 1=hélio / 2=hidrogenio ):\n--->"))
fator_segurança=float(input("digite o valor do fator de segurança:(em decimal ..ex: 0,10 = 10%)\n--->"))
P_a = float(input("digite o valor de densidade do ar na altitude desejada:(Kg/m^2)\n--->"))
flag_volume = int(input("o projeto apresenta limitação em volume de gás?:( 1=sim / 2=não ):\n--->"))


#constantes#
#unidade (kg/m^3)
P_a0 = 1.225

if (P_g0 == 1):
    P_g0 = 0.179
elif(P_g0 == 2):
    P_g0 = 0.0899 
# end #
sigma = P_a/P_a0

if (flag_volume == 1):
    volume_gas = float(input("digite o volume limite de gas:(m^3)\n--->"))
    area_envelope =float(input("digite a area do solido:(m^2)\n--->"))
    p_envelope = area_envelope * P_F
    empuxo_liquido_newtons = volume_gas*(P_a - P_g0 )*9.8
    empuxo_liquido_kgf = volume_gas*(P_a - P_g0 )
    empuxo_util = empuxo_liquido_kgf - ( M_0 + p_envelope)
    carga_util = empuxo_util- (fator_segurança * empuxo_util)
    if (empuxo_util >= 0):
        print(f"#-----------------------------------------------------------------------#")
        print(f"|o empuxo liquido do projeto será de: {empuxo_liquido_newtons} N        |")
        print(f"|o empuxo liquido do projeto será de: {empuxo_liquido_kgf} Kgf          |")
        print(f"|o empuxo util do projeto será de: {empuxo_util} Kgf                    |")
        print(f"|o peso do envelope será de: {p_envelope} Kg                            |")
        print(f"|o peso total do projeto será de: {p_envelope} Kg                       |")
        print(f"|a carga paga será de: {carga_util} Kg                                  |")
        print(f"#-----------------------------------------------------------------------#")
    elif(empuxo_util == 0):
        print(f"             !!!!!!!!!!!!!!!!!!   CUIDADO   !!!!!!!!!!!!!!!!             ")
        print(f"                                                                         ")
        print(f"                     PROJETO NO LINEAR DE ESTABILIDADE                   ")
        print(f"                                                                         ")
        print(f"             !!!!!!!!!!!!!!!!!!   CUIDADO   !!!!!!!!!!!!!!!!             ")
        print(f"#-----------------------------------------------------------------------#")
        print(f"|o empuxo liquido do projeto será de: {empuxo_liquido_newtons} N        |")
        print(f"|o empuxo liquido do projeto será de: {empuxo_liquido_kgf} Kgf          |")
        print(f"|o empuxo util do projeto será de: {empuxo_util} Kgf                    |")
        print(f"|o peso do envelope será de: {p_envelope} Kg                            |")
        print(f"|o peso total do projeto será de: {p_envelope} Kg                       |")
        print(f"|a carga paga será de: {carga_util} Kg                                  |")
        print(f"#-----------------------------------------------------------------------#")
    elif(empuxo_util < 0):
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"                                                ")
        print(f"             PROJETO SEM ESTABILIDADE           ")
        print(f"                                                ")
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  
elif(flag_volume == 2):
    s = float(input("digite o valor de área da geometria do envelope:(m^2)\n--->"))
    v = float(input("digite o valor de volume da geometria do envelope:(m^3)\n--->"))
    K_sv= s/v
    
# end #

