import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

f = df.plot.scatter("carat", "price")
f.get_figure().savefig('figs/Relationship of carat vs price')