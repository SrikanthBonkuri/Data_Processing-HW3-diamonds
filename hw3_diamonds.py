
# Q1.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

#f = df.plot.scatter("carat", "price")
#fig = f.get_figure()
#f.get_figure().savefig('figs/Q1_Relationship of carat vs price')


# Q2.

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


#Q1 Plot

f = df.plot.scatter("carat", "price")
fig = f.get_figure()
f.get_figure().savefig('figs/Q1_Relationship of carat vs price')



from sklearn.metrics import explained_variance_score
import statsmodels.api as sm

X = df[['log_carat']].copy() # Double square brackets returns the single column dataframe
y = df['log_price'].copy() # Will be a numpy type array

# Fit regression model
results = sm.OLS(y, X).fit()

# Inspect the results and inspect R squared to comment on explained variance
print(results.summary())


y_pred = results.predict(X)

print(explained_variance_score(y, y_pred))

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X, y)

from sklearn.model_selection import cross_val_score
print(cross_val_score(linear_regression, X, y, cv=10, scoring="explained_variance").mean())


X1 = df['carat']
y1 = df['price']

results1 = sm.OLS(y1, X1).fit()
print(results.summary())
y_pred1 = results.predict(X1)
explained_variance_score(y_pred1, y1)


# Q3.

def simple_train_test_split(X, y, test_size=.3):
    n_training_samples = int((1.0 - test_size) * X.shape[0])

    X_train = X[:n_training_samples]
    y_train = y[:n_training_samples]

    X_test = X[n_training_samples:]
    y_test = y[n_training_samples:]

    return X_train, X_test, y_train, y_test

X = df[['carat']].copy()
# X['const'] = 1.
y = df['price'].copy()


X_train1, X_test1, y_train1, y_test1 = simple_train_test_split(X, y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# For sklearn.model_selection.train_test_split:
results = sm.OLS(y_train, X_train).fit() 
# Inspect the results and inspect R squared to comment on explained variance
print(results.summary())

# Using simple_train_test_split:
results1 = sm.OLS(y_train1, X_train1).fit()
# Inspect the results and inspect R squared to comment on explained variance
print(results1.summary())



