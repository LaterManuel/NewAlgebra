from tkinter import E


def inv(a,b):
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
def euclides(a,b):
    if b==0:
        return a
    else:
        return euclides(b,a%b)
a=euclides(5,7)
if a==1:
    print(inv(5,7))
else :
    "No existe inverso"
