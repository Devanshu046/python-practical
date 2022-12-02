a=int(input("enter number:"))

x,y=0,1
print(x)
print(y)

for i in range(0,a-2):
    c=x+y
    x=y
    y=c
    print(c)