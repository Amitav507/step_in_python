import math
a=int(input("enter list range "))
# print(len(a))
z=[None]*a
i=0
while a > i :
    z[i]=input("enter element ")
    i=i+1
for i in range(0,a) :
    print(z[i])
for i in range(0,a) :
    print(z[ :i+1])
input("press key to exit ")