import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,50*np.pi, 0.1)
y = np.sin(x)

plt.plot(x,y,color = "blue")
plt.show()