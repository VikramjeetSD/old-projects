myfile=open("poem.txt","r")
c=0
p=myfile.read()
for k in p:
    if k=="e":
        c+=1
print(c)        
