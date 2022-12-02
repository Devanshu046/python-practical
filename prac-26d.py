# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd


# Initialize the lists for X and Y
data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.plot(X, Y)


# Show the plot
plt.show()
