# ATIVIDADE COMPLEMENTAR PYTHON LAB003
# Nome: Exercício 01
# Autor: Bruno Elinton Guimarães de Araújo
# Data: 22/11/2020
# Descrição:

'''
ESTE PROGRAMA CALCULA E EXIBE OS MODOS TRANSMISSÃO (TE e TM) POSSÍVEIS EM UMA GUIA DE ONDA RETANGULAR CUJA AS CARACTERÍSTICAS SÃO:

                            > a = 50mm  --> DIMENSÃO DO GUIA AO LONGO DO EIXO X
                            > b = 45mm  --> DIMENSÃO DO GUIA AO LONGO DO EIXO Y
                            > σ = 0     --> CONDUTIVIDADE DO DIELÉTRICO
                            > ϵ = 9ϵ_0  --> PERMISIVIDADE DO DIELÉTRICO
                            > μ_r = 1   --> PERMEABILIDADE RELATIVA DO DIELÉTRICO
                            > f < 3 GHz --> FREQUÊNCIA DE OPERAÇÃO
                        

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
def frequenciaCorte(a, b, m, n, u):
    fc = (u/(2*a))*np.sqrt((m*m)+((a*a)/(b*b)*(n*n)))
    return fc
    
# FUNÇÃO QUE CALCULA OS MODOS DE TRANSMISSÃO
def modos(a, b, f, μ_r, ϵ):
    m = 0
    n = 1
    qtdMdTE = 0
    qtdMdTM = 0
    u = velocidadeFase(μ_r, ϵ)
    fc = frequenciaCorte(a, b, m, n, u)
    # CALCULANDO O VALOR MÁXIMO PARA n JUNTAMENTE COM OS MODOS TE
    while fc < f:
        fc = frequenciaCorte(a, b, m, n, u)
        if(fc < f):
            print(f"MODO: TE[{m}][{n}] --> fc =", "{0:.2E}".format(fc), " Hz")
            qtdMdTE+=1
        n+=1  
    C = n-1
    # CALCULANDO O VALOR MÁXIMO PARA m JUNTAMENTE COM OS MODOS TE
    n = 0
    m = 1
    fc = frequenciaCorte(a, b, m, n, u)
    while fc < f:
        fc = frequenciaCorte(a, b, m, n, u)
        if(fc < f):
            print(f"MODO: TE[{m}][{n}] --> fc =", "{0:.2E}".format(fc), " Hz")
            qtdMdTE+=1
        m+=1
    L = m-1
    # CALCULANDO MODOS TE E TM
    for i in range(1, L):
        for j in range(1, C):
            fc = frequenciaCorte(a, b, i, j, u)
            if(fc < f):
                print(f"MODOS: TE[{i}][{j}], TM[{i}][{j}] --> fc =", "{0:.2E}".format(fc), " Hz")
                qtdMdTE+=1
                qtdMdTM+=1
    print("\nQUANTIDADE DE MODOS:")            
    print(qtdMdTE, " --> MODOS TE")
    print(qtdMdTM, " --> MODOS TM")

# FUNÇÃO PRINCIPAL
def main():
    ϵ = 9*ϵ_0           # PERMISSIVIDADE DO DIELÉTRICO
    μ_r = 1             # PERMEABILIDADE DO DIELÉTRICO
    a = 50.0/1000.0     # COMPRIMENTO DO GUIA EM x      | UNIDADE: m
    b = 45.0/1000.0     # COMPRIMENTO DO GUIA EM y      | UNIDADE: m
    f = 3*10**9         # FREQUÊNCIA DE OPERAÇÃO        | UNIDADE: Hz
    print("---------------------< DADOS DA QUESTÃO >---------------------")
    print(f"ϵ = 9*ϵ_0, μ_r = 1, a = {a*1000}mm, b = {b*1000}mm,", "f = {0:.2E}".format(f), "Hz\n")
    print("-------------------< MODOS DE TRANSMISSÃO >-------------------")
    modos(a, b, f, μ_r, ϵ)

    
# INICIANDO A EXECUÇÃO DO PROGRAMA
main()
