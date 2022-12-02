
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])


plt.bar(X, Y, color='g')
plt.title("Students over 11 Years")
plt.xlabel("Years")
plt.ylabel("Number of Students")


plt.show()
