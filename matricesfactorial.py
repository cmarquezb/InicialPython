import numpy as tabla
M = tabla.array([1,8,8,1,9,8,8,1,2,9,2,6,7,9,6,3,8,3,8,6,9,7,2,3,9,4,6,1,6,5,4,3,9,8,7,1,6,3,5,6,3,3,7,9,4,1,7,3,8,2,7,7,6,3,3,5,6,4,2,2,9,8,8,8,5,9,7,1,5,2,3,4,6,6,5,4,8,5,3,1,9,6,6,6,5,4,7,4,3,4,5,3,1,7,3,8,8,1,1,3,3,3,9,6,7,1,6,1,9,9,6,9,2,3,2,1,2,5,7,3,4,3,1,8,7,9,5,5,6,5,6,9,9,6,2,2,1,3,5,1,6,8,7,5,9,3,7,6,5,2,5,7,5,9])
P = tabla.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
Q = tabla.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

A=B=C=D=E=F=G=H=I=J=K=L= tabla.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
N=O=R=S=T=U=V=W=X=Y=Z=A1= tabla.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# print("largo de M", M.size) estamos ok   
jj=kk=aux=ll=cont1=0
cont2=cont3=cont4=cont5=0
cont6=cont7=cont8=cont9=0
aaa=0
for ii in range(0,M.size-1):
        if M[ii]==1:
                cont1=cont1+1
        elif M[ii]==2:
                cont2=cont2+1
        elif M[ii]==3:
                cont3=cont3+1
        elif M[ii]==4:
                cont4=cont4+1
        elif M[ii]==5:
                cont5=cont5+1
        elif M[ii]==6:
                cont6=cont6+1
        elif M[ii]==7:
                cont7=cont7+1
        elif M[ii]==8:
                cont8=cont8+1
        elif M[ii]==9:
                cont9=cont9+1
        if M[ii+1]>M[ii]:                  
                aaa=aaa+M[ii]
        else:     
                A[jj]=aaa+M[ii]
                aaa=0
                jj=jj+1

aux=1  
producto = 1
producto = cont1*cont2*cont3*cont4*cont5*cont6*cont7*cont8*cont9
# http://nayuki.eigenstate.org/res/karatsuba-multiplication/karatsuba.py
# http://nayuki.eigenstate.org/page/karatsuba-multiplication
_CUTOFF = 2048

def naive(x, y):
    total = 0
    yy = [int(i) for i in str(y)]
    for i, yyy in enumerate(yy[::-1]):
        total += x * yyy * (10 ** i)
    return total
    
def kara(x, y):
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        #print('naive')
        return naive(x, y)
    else:
        #print('karatsuba')
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half
        a = kara(xhigh, yhigh)
        b = kara(xlow + xhigh, ylow + yhigh)
        c = kara(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True             

b=1
entero = 0.1e1
for ii in range(0,90):
        if A[ii]==0:
                entero *= 1
        elif A[ii]==9:
                entero *= 1
        else:            
                entero *= A[ii]
        
         
#b = b*(2**66)
c= 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
primi = 2142982825303188546009012574364051288730081983630838380068184914265112576
d=c/primi
elmod=1
elmod= c % d
primi = 2142982825303188546009012574364051288730081983630838380068184914265112576
elmod= c % primi
print("el primer valor de A es ", A[:])
print ("el valor de P es", format(entero, '.90f'))
print ("el valor de Q es", format(d,'.99f'))

print ("el valor de Resto es", elmod)

primo = False

print ("el valor de Resto es",isPrime(primi))
