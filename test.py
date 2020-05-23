import random

low=25
point =5
for i in range (1,5):
 Number=low + random.randrange(0,point);
 print(Number,end=":")
 point-=1;
print()
