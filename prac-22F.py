import pandas as pd
df=pd.DataFrame({'a':range(1,6),
                 'b':range(10,0,-2),
                 'c':range(10,5,-1)
    
})
print(df)
c=df[df['a']>df['b']]
print(c)