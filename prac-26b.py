
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('hist.csv')


plt.hist(df['Award_Amount'])
plt.show()
