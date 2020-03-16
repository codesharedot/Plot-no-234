import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 10*x

plt.plot(x, y,'r:',linewidth=6)
plt.savefig('chart.png')