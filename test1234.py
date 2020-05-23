def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p    
def add(n):
    p=0
    for i in range(1,n+1):
        p=p+i
    return p

for a in range(1,5):
    print(add(a)/fact(a))
