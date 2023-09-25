from sympy import *
c,x = symbols('c x', real=True)

#para fluxo constante
def fluxos(fluxo,tempo):
    array = []
    for i in range(tempo):
        array.append(fluxo)
    return array

def rendimentoFluxo(fluxo,tempo):
    flux = simplify(fluxo)
    total =  tempo*flux
    return total

def TIR(fluxos):
    V=0
    for i in range(len(fluxos)):
        V+=fluxos[i]/(1+x)**(i+1)
    return V



"ex :solucao = solve(Eq(investimento1,investimento2),x)"

#calcular uma parcela para amortizar Dk= divida total, n = numero de parcelas, r = valor da parcela

def  valordasnparcelas(d,i,n):
    r = d * ((i   *   ((1+i)**n))/(((1+i)**n) - 1) )
    return r









#Ms = P * (1 + n * i), Ms = P ( (a + 1)/2a * n * i ) com a= nº de vezes aplicadas



'''i=taxa
a= aplicações
p= montante
n = quantidade de vezes
'''

def Msaplic(a,p,n,i):
        Msapl = p ( (a + 1)/(2*a) * n * i ) 
        return Msapl



#Mc = P * (1 + i)^(n/a) /a  * 1 - (1+i)^n /1 -(1+i)^n/a


'''
i=taxa
a = aplicação
p= montante
n = qunatidade de vezes
'''

def Mcaplic(P,i,n,a):
   MCapl = P * ((1 + i)^(n/a)) /a  * (1 - (1+i)^n /(1 -(1+i)^(n/a)))
   return MCapl



