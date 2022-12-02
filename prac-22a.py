from this import d
import pandas as pd 
df=pd.read_csv('demo.csv')

# creting dictionary 
dict1={
    'Name':['a','b','c','d'],
    'age':[10,11,12,13]
}
df1=pd.DataFrame(dict1)

# creating list

list1=[
    ('ram','apple',23),
    ('shyam','google',25),
    ('sheeta','hp',21)
]
df2=pd.DataFrame(list1,columns=('Name','company','age'))

print(df)
print(df1)
print(df2)
