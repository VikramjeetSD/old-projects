def find(a,b):
    s=a+b
    p=a*b
    r=a/b
    return s,p,r
a=int(input("Enter First No. :  "))
b=int(input("Enter Second No. :  "))
s,p,r=find(a,b)
print("Sum is :  ",s)
print("product is : ",p)
print("remainder is : ",r)

