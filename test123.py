def find(a,b):
    if (a>b):
        return a,b
    else :
        return b,a

num1=int(input("1 :  "))
num2=int(input("2 :  "))
x,y=find(num1,num2)
print(x,"is greter than ",y)
