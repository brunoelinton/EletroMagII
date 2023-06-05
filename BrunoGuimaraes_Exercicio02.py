# ATIVIDADE COMPLEMENTAR PYTHON LAB003
# Nome: Exercício 02
# Autor: Bruno Elinton Guimarães de Araújo
# Data: 22/11/2020
# Descrição:

'''
ESTE PROGRAMA CALCULA E EXIBE OS CINCO MODOS TRANSMISSÃO (TE e TM) POSSÍVEIS EM UM GUIA DE ONDA RETANGULAR CUJA AS CARACTERÍSTICAS SÃO:

                            > a = 90mm  ----------> DIMENSÃO DO GUIA AO LONGO DO EIXO X
                            > b = 70mm  ----------> DIMENSÃO DO GUIA AO LONGO DO EIXO Y
                            > c = 120mm ----------> DIMENSÃO DO GUIA AO LONGO DO EIXO Z
                            > σ_c = 5,8x10^7    --> CONDUTIVIDADE DA PAREDE DO GUIA
                            > ϵ = 3ϵ_0  ----------> PERMISIVIDADE DO DIELÉTRICO
                            > μ_r = 1   ----------> PERMEABILIDADE RELATIVA DO DIELÉTRICO
                        

CONSTANTES:

                            > ϵ_0 = 8,854 x 10^-12 F/m
                            > μ_0 = 4π x 10^-7 H/m

'''

# IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
import numpy as np
from numpy import pi
import scipy as sp
import matplotlib.pyplot as plt

# DEFINIÇÃO DE CONSTANTES
ε_0 = 8.854*10**-12     # --> CONSTANTE DE PERMISIVIDADE DO ESPAÇO LIVRE (VÁCUO)    | UNIDADE: F/m
μ_0 = 4*pi*10**-7       # -- CONSTANTE DE PERMEABILIDADE DO ESPAÇO LIVRE (VÁCUO)    | UNIDADE: H/m

# FUNÇÃO QUE CALCULA A VELOCIDADE DE FASE DA ONDA
def velocidadeFase(μ_r, ϵ):
    u = 1/np.sqrt(μ_0*μ_r*ϵ)
    return u

# FUNÇÃO QUE CALCULA A FREQUÊNCIA DE CORTE
def frequenciaCorte(a, b, c, m, n, p, u):
    fc = (u/2) * np.sqrt(np.power((m/a), 2) + np.power((n/b), 2) + np.power((p/c), 2))
    return fc
    
# FUNÇÃO QUE CALCULA OS MODOS DE TRANSMISSÃO
def modos(a, b, c, μ_r, ϵ):
    m = 0
    n = 1
    qtdMdTE = 0
    qtdMdTM = 0
    u = velocidadeFase(μ_r, ϵ)
    M = []
    menoresModos = []
    modosInvalidos = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                fc = frequenciaCorte(a, b, c, i, j, k, u)
                I = np.zeros((1, 4), np.dtype(float))
                I[0][0] = fc
                I[0][1] = i
                I[0][2] = j
                I[0][3] = k
                M.append(I)

    # REMOVENDO ELEMENTOS INVÁLIDOS
    limite = len(M)
    cont = 0
    while(cont < limite):
        for i in range(len(M)):
            if((M[i][0][1] == 0 and M[i][0][2] == 0) or (M[i][0][1] == 1 and (M[i][0][2] == M[i][0][3] == 0)) or (M[i][0][2] == 1 and (M[i][0][1] == M[i][0][3] == 0))):
                M.pop(i)
                break;
        cont += 1;
        i = 0
          
    # OBTENDO OS CINCO MENORES MODOS DE TRANSMISSÃO
    limite = len(M)
    cont = 0
    i = 0
    while(cont < 5):
        menor = M[i][0][0]
        j = i
        for i in range(len(M)):
            if(M[i][0][0] <= menor):
                menor = M[i][0][0]
                aux = M[i]
                j = i
        menoresModos.append(aux)
        M.pop(j)
        cont +=1
        i = 0

    # EXIBINDO OS 5 MENORES MODOS
    for i in range(len(menoresModos)):
        if(menoresModos[i][0][1] != 0 and menoresModos[i][0][2] != 0 and menoresModos[i][0][3] != 0):
            print(f"MODOS: TE[{int(menoresModos[i][0][1])}][{int(menoresModos[i][0][2])}][{int(menoresModos[i][0][3])}], TM[{int(menoresModos[i][0][1])}][{int(menoresModos[i][0][2])}][{int(menoresModos[i][0][1])}] --> fc =", "{0:.2E}".format(menoresModos[i][0][0]), " Hz")
        else:
            print(f"MODOS: TE[{int(menoresModos[i][0][1])}][{int(menoresModos[i][0][2])}][{int(menoresModos[i][0][3])}] --> fc =", "{0:.2E}".format(menoresModos[i][0][0]), " Hz")
    

# FUNÇÃO PRINCIPAL
def main():
    ϵ = 3*ϵ_0           # PERMISSIVIDADE DO DIELÉTRICO
    μ_r = 1             # PERMEABILIDADE DO DIELÉTRICO
    a = 90.0/1000.0     # COMPRIMENTO DO GUIA EM x      | UNIDADE: m
    b = 70.0/1000.0     # COMPRIMENTO DO GUIA EM y      | UNIDADE: m
    c = 120.0/1000.0    # COMPRIMENTO DO GUIA EM y      | UNIDADE: m
    
    print("---------------------< DADOS DA QUESTÃO >---------------------")
    print(f"ϵ = 3*ϵ_0, μ_r = 1, a = {a*1000}mm, b = {b*1000}mm, c = {c*1000}mm, σ_c = 5,8x10^7 S/m\n")
    print("-------------------< MODOS DE TRANSMISSÃO >-------------------")
    
    modos(a, b, c, μ_r, ϵ)

    
# INICIANDO A EXECUÇÃO DO PROGRAMA
main()
