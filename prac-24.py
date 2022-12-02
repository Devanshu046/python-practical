import matplotlib.pyplot as plt
import numpy as np
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
myLabels=["java","python","php","js","c#","c++"]

plt.pie(y,labels=myLabels)
plt.show()
