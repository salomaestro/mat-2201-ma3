import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")

x = np.linspace(0, 3, 100)

f = lambda x: 1 + x + 2 * (x-0) * (x-1)

y = f(x)

plt.plot(x, y)
plt.scatter([0, 1, 2], [1, 2, 7], color="red")
plt.show()