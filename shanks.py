import math as mt

def dislog(h,g,p):
    n = p-1
    t = mt.floor(mt.sqrt(n))
    k = n//t
    L1 = [(g**(i*k))%p for i in range(t)]
    L2 = [(h*g**(i))%p for i in range(k+1)]
    for i in range(t):
        l1 = L1[i]
        for j in range(k+1):
            if L2[j] == l1:
                print(g,"^",i*k,"=",h,"*",g,"^",j)
                return i*k-j


print(dislog(21,11,71))
print(dislog(116,156,593))
print(dislog(2213,650,3571))