a=input("enter string:")
n=0
for i in range(0,len(a)):
    if a[i].lower() in ("a", "e","i","o","u")  :
       n+=1
print("no of vowel is :",n)