def isprimroot(g,p):
    elems = set(range(1,p))
    remainders = set()
    a = 0
    while remainders != elems:
        a += 1
        l1 = len(remainders)
        r = (g**a)%p
        print(g,"^",a,"%",p,"=",r)
        remainders.add(r)
        l2 = len(remainders)
        if l1 == l2:
            break
    else:
        print(remainders)
        return True
    print(remainders)
    return False


L = []
for p in [2,3,5,7,11,13,17,23,31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
    if isprimroot(4,p):
        L.append(p)
print(L,len(L))   

