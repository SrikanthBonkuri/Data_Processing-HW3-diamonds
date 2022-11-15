
# Q3.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

plt.cla()   # Clear axis
plt.clf()   # Clear figure
#plt.close() # Close a figure window


import math

def log_function(x):
    return math.log(x)

df['log_price'] = df['price'].transform(log_function)
df['log_carat'] = df['carat'].transform(log_function)

sns.set_style("whitegrid")

from sklearn.metrics import explained_variance_score
import statsmodels.api as sm

X = df[['log_carat']].copy() # Double square brackets returns the single column dataframe
y = df['log_price'].copy() # Will be a numpy type array


from sklearn.linear_model import LinearRegression



def simple_train_test_split(X, y, test_size=.3):
    n_training_samples = int((1.0 - test_size) * X.shape[0])

    X_train = X[:n_training_samples]
    y_train = y[:n_training_samples]

    X_test = X[n_training_samples:]
    y_test = y[n_training_samples:]

    return X_train, X_test, y_train, y_test



X_train1, X_test1, y_train1, y_test1 = simple_train_test_split(X, y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# For sklearn.model_selection.train_test_split:
results = sm.OLS(y_train, X_train).fit() 
# Inspect the results and inspect R squared to comment on explained variance
print(results.summary())

linear_regression = LinearRegression()

linear_regression.fit(X_train, y_train)
y_pred = linear_regression.predict(X_test)

print("Explained Variance Score on sklearn.model_selection.train_test_split:",explained_variance_score(y_test, y_pred))

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, linear_regression.predict(X_train), color = 'blue')
plt.title('Logarithmic carat vs price (Test set of sklearn split)')
plt.xlabel('log_carat')
plt.ylabel('log_price')
plt.show()
plt.savefig('figs/Q3_Log_Transformed_Carat_by_Price-sklearn test split')

plt.cla()   # Clear axis
plt.clf()   # Clear figure

# Using simple_train_test_split:
results1 = sm.OLS(y_train1, X_train1).fit()
# Inspect the results and inspect R squared to comment on explained variance
print(results1.summary())

linear_regression1 = LinearRegression()

linear_regression1.fit(X_train1, y_train1)
y_pred1 = linear_regression1.predict(X_test1)

print("Explained Variance Score on simple_train_test_split:",explained_variance_score(y_test1, y_pred1))

# Visualising the Test set results
plt.scatter(X_test1, y_test1, color = 'red')
plt.plot(X_train1, linear_regression1.predict(X_train1), color = 'blue')
plt.title('Logarithmic carat vs price (Test set of simple split)')
plt.xlabel('log_carat')
plt.ylabel('log_price')
plt.show()
plt.savefig('figs/Q3_Log_Transformed_Carat_by_Price-simple test split')


