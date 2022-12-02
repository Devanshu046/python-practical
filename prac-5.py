a=int(input("enter first number:"))
b=int(input("enter second number:"))

print('''-----simple Claculator-----
press 1 For Addition
Press 2 For Substraction
Press 3 For Muliplication
Press 4 for Division''')

n=int(input("enter any(1/2/3/4):"))

if n==1:
    c=a+b
    print("Addition of Two number is :",c)
elif n==2:
    c=a-b
    print("Substraction  of Two is :",c)
elif n==3:
    c=a*b
    print("Muliplication of Two is :",c)
elif n==4:
    c=a/b
    print("Division of Two is :",c)
else:
    print()



    
