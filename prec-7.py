a=int(input("enter number:"))
n=0
for i in range(2,a):
    if a%i==0:
        n=n+1
if n==1:
        print("Number is not a prime")
else:
    print("Number is Prime")