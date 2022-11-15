
# Q4.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('diamonds.csv');

#plt.cla()   # Clear axis
#plt.clf()   # Clear figure
#plt.close() # Close a figure window

import math

def log_function(x):
    return math.log(x)

df['log_price'] = df['price'].transform(log_function)
df['log_carat'] = df['carat'].transform(log_function)


from sklearn.metrics import explained_variance_score
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

X = df[['log_carat', 'cut']]
y = df['log_price'].copy()

#creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

#perform one-hot encoding on 'cut' column 
encoder_X = pd.DataFrame(encoder.fit_transform(X[['cut']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_X = X.join(encoder_X)

#drop 'cut' column
final_X.drop('cut', axis=1, inplace=True)

#rename columns
final_X.columns = ['log_carat', 'Fair', 'Good', 'Ideal', 'Premium', 'Very Good']

#view final df
print(final_X)

print("Feature Matrix Shape: ", final_X.shape)

results = sm.OLS(y, final_X).fit()
print(results.summary())

linear_regression = LinearRegression()

linear_regression.fit(final_X, y)
y_pred = linear_regression.predict(final_X)

print("Explained Variance Score on log_price vs (log_carat, cut):",explained_variance_score(y, y_pred))


# Similarly, now considering color as 2nd input

X1 = df[['log_carat', 'color']]

#perform one-hot encoding on 'cut' column 
encoder_X1 = pd.DataFrame(encoder.fit_transform(X1[['color']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_X1 = X1.join(encoder_X1)

#drop 'cut' column
final_X1.drop('color', axis=1, inplace=True)

#rename columns
final_X1.columns = ['log_carat', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#view final df
print(final_X1)

print("Feature Matrix Shape: ", final_X1.shape)

results1 = sm.OLS(y, final_X1).fit()
print(results1.summary())

linear_regression1 = LinearRegression()

linear_regression1.fit(final_X1, y)
y_pred1 = linear_regression1.predict(final_X1)

print("Explained Variance Score on log_price vs (log_carat, color):",explained_variance_score(y, y_pred1))


# Similarly, now considering clarity as 2nd input

X2 = df[['log_carat', 'clarity']]

#perform one-hot encoding on 'cut' column 
encoder_X2 = pd.DataFrame(encoder.fit_transform(X2[['clarity']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_X2 = X2.join(encoder_X2)

#drop 'cut' column
final_X2.drop('clarity', axis=1, inplace=True)

#rename columns
final_X2.columns = ['log_carat', 'I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']

#view final df
print(final_X2)

print("Feature Matrix Shape: ", final_X2.shape)

results2 = sm.OLS(y, final_X2).fit()
print(results2.summary())

linear_regression2 = LinearRegression()

linear_regression2.fit(final_X2, y)
y_pred2 = linear_regression2.predict(final_X2)

print("Explained Variance Score on log_price vs (log_carat, clarity):",explained_variance_score(y, y_pred2))
