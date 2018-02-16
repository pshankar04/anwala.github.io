import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("carbonDate.csv")
# df.plot()  # plots all columns against index
df.plot(kind='scatter',x='currentAge',y='Mementos') # scatter plot
plt.show()