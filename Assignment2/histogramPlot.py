import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('mem.csv', sep=',', skiprows=0,header=None, index_col =0).dropna()
# data = pd.read_csv('testMementos.csv', sep=',', index_col =0)
 
data.plot(kind='bar')
plt.ylim(0, 1000)
plt.ylabel("URIs")
plt.xlabel('Mementos')
plt.title('Histogram')
L=plt.legend()
L.get_texts()[0].set_text('URIs')
plt.show()