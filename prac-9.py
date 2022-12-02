def fact(n):
   if(n==0 or n==1):
      return 1
   else:
      return n*fact(n-1)
num=int(input("enter num:"))
print("fact of",num,"is",fact(num))