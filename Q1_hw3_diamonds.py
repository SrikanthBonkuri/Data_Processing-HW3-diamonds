
# Q1.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

f = df.plot.scatter("carat", "price")
fig = f.get_figure()
f.get_figure().savefig('figs/Q1_Relationship of carat vs price')

#plt.cla()   # Clear axis
#plt.clf()   # Clear figure
#plt.close() # Close a figure window
