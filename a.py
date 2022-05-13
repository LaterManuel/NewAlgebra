import ast
from audioop import mul
from cgitb import text
from threading import BrokenBarrierError
from turtle import pos

abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#DEFINIENDO INVERSO
def inv(a,b):
    for x in range(1,b):
        if((a%b)*(x%b) % b==1):
            return x
def mod1(a,b):
    c=0
    val=1
    while val==1:
        if a<=b*c:
            return c-1
        c=c+1
print(mod1(27,22))
def inv2(a,b):
    r = [a,b]
    s = [1,0] 
    t = [0,1]
    i = 1 
    q = [[]]
    while (r[i] != 0): 
        q = q + [r[i-1] // r[i]]
        r = r + [r[i-1] % r[i]]
        s = s + [s[i-1] - q[i]*s[i]]
        t = t + [t[i-1] - q[i]*t[i]]
        i = i+1
    return (s[i-1])
#Lista de posiciones del texto en el abecedario
def postext(texto):
    listador=[]
    for i in texto:
        contador=0
        for a in abc:
            if i==a:
                listador.append(contador)
                break
            contador=contador+1
    return listador
def encriptadoPOS(a,b,list):
    listador=[]
    for i in list:
        c=(a*i+b)%27
        listador.append(c)
    return listador
def encriptado(a,b,list):
    listador=[]
    for i in list:
        c=(a*i+b)%27
        listador.append(abc[c])
    return listador
def descifradoPOS(a,b,list):
    listador=[]
    for i in list:
        m=((i-b)*inv2(a,27))%27
        listador.append(m)
    return listador
def descifrado(a,b,list):
    listador=[]
    for i in list:
        m=((i-b)*inv2(a,27))%27
        listador.append(abc[m])
    return listador
def impresorlista(list):
    for i in list:
        print(i,end=" ")
    print()

def a_la_fuerza(astr):
    a=postext(astr)
    for i in range(20,40):
        for x in range(0,20):
            print("Con Clave ",i," ",x)
            b=descifrado(i,x,a)
            impresorlista(b)
phrase3="SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV"
a_la_fuerza(phrase3)

