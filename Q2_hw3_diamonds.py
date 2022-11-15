
# Q2.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

plt.cla()   # Clear axis
plt.clf()   # Clear figure


import math

def log_function(x):
    return math.log(x)

df['log_price'] = df['price'].transform(log_function)
df['log_carat'] = df['carat'].transform(log_function)

# Show a scatterplot that visualizes the relationship between carat and price
sns.set_style("whitegrid")
#reg = sns.regplot(data=df,x='log_price', y='log_carat', line_kws={'color': 'red'}, scatter_kws={'alpha':0.005})
reg = sns.regplot(data=df,x='log_carat', y='log_price', line_kws={'color': 'red'})

# Title and save
fig = reg.get_figure()
fig.subplots_adjust(top=0.925)
fig.suptitle('Carat by Price (with Logarithmic Transformations)')
reg.get_figure().savefig('figs/Q2_Log_Transformed_Carat_by_Price')


from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
import statsmodels.api as sm

X = df[['log_carat']].copy() # Double square brackets returns the single column dataframe
y = df['log_price'].copy() # Will be a numpy type array

# Fit regression model
results = sm.OLS(y, X).fit()

# Inspect the results and inspect R squared to comment on explained variance
print(results.summary())

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X, y)
y_pred = linear_regression.predict(X)

print("Explained Variance Score on Log Transformations:",explained_variance_score(y, y_pred))


X1 = df[['carat']]
y1 = df['price']

results1 = sm.OLS(y1, X1).fit()
print(results1.summary())

linear_regression.fit(X1, y1)
y_pred1 = linear_regression.predict(X1)

print("Explained Variance Score on carat vs price:",explained_variance_score(y1, y_pred1))
