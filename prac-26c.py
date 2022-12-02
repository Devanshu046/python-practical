import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('piedata.csv')

value1 = data["value"]
label1 = ['a', 'b', 'c', 'd']


plt.pie(value1, labels=label1)
plt.show()
