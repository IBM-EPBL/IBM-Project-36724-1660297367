import random
a=int(input("enter the starting value: "))
b=int(input("enter the stop value: "))
i=1
while i<20:
    temp=random.randint(a,b)
    hum=random.randint(a,b)
    i+=1
    if temp>75 and hum>25:
        print("WARNING")
    else:
        print("NORMAL")
