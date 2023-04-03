def gcd(x,y):
    x , y = max((x,y)),min((x,y))
    if y == 0:
        return x
    return gcd(y,x%y)

print(gcd(2813,8051))