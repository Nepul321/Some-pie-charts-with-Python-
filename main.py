import matplotlib.pyplot as plt
import numpy as np

y = np.array([50, 20, 10, 15, 5])
my_labels = ["Bitcoin", "Ethereum", "Dogecoin", "Binance coin", 'XRP']

plt.pie(y, labels = my_labels)
plt.show()