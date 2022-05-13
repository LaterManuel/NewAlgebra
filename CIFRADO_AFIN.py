import ast
from audioop import mul
from cgitb import text
from threading import BrokenBarrierError
from turtle import pos

abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#DEFINIENDO INVERSO
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
#LISTA DE POSICIONES DEL ENCRIPTADO
def encriptadoPOS(a,b,list):
    listador=[]
    for i in list:
        c=(a*i+b)%27
        listador.append(c)
    return listador
#LISTA DE LETRAS CIFRADAS
def encriptado(a,b,list):
    listador=[]
    for i in list:
        c=(a*i+b)%27
        listador.append(abc[c])
    return listador
#LISTA DE POSICIONES DEL DESCIFRADO
def descifradoPOS(a,b,list):
    listador=[]
    for i in list:
        m=((i-b)*inv2(a,27))%27
        listador.append(m)
    return listador
#LISTA DE LETRAS DESCIFRADAS
def descifrado(a,b,list):
    listador=[]
    for i in list:
        m=((i-b)*inv2(a,27))%27
        listador.append(abc[m])
    return listador
#iMPRESOR DE LISTAS 
def impresorlista(list):
    for i in list:
        print(i,end=" ")
    print()
#DESENCRIPTADOR POR FUERZA BRUTA
def a_la_fuerza(astr):
    a=postext(astr)
    for i in range(23,24):
        for x in range(10,20):
            print("Con Clave ",i," ",x)
            b=descifrado(i,x,a)
            impresorlista(b)

phrase="ELEMENTALMIQUERIDOWATSON"
x,y=4,7
a=postext(phrase)
print("Posicion base")
impresorlista(a)
b1=encriptadoPOS(x,y,a)
print("Posiciones del encriptado")
impresorlista(b1)
b=encriptado(x,y,a)
print("Encriptado")
impresorlista(b)
print()
phrase2="OKHFSNKFNWFCWJHSNCHQYWFSWF"
x,y=4,7
a=postext(phrase2)
print("Posicion base")
impresorlista(a)
b1=descifradoPOS(x,y,a)
print("Posiciones del descifrado")
impresorlista(b1)
b=descifrado(x,y,a)
print("Descifrado")
impresorlista(b)
print()
phrase3="SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV"
#LA CLAVE SE CONSIGUE EN {A,B}={23,17}
a_la_fuerza(phrase3)



