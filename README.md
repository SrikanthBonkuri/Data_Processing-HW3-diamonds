
# hw-diamonds

## Assignment

Use the [diamonds dataset](https://ggplot2.tidyverse.org/reference/diamonds.html) to answer the questions below.
You can get the data directly from the [ggplot2 github repo](https://github.com/tidyverse/ggplot2/).

## Question 1

Visualize the relationship between "price" and "carat" and comment on the type of model that 
might be appropriate for modeling their relationship.

#### Visualization:
![image](https://user-images.githubusercontent.com/45035308/201222209-1a9b9305-f369-446f-90ed-8115d1432080.png)


## Question 2

Investigate logarithmic transformations to see if you can find a more appropriate relationship
between "price" and "carat" for univariate linear regression.
Use data visualization to help justify your choice of model.
Use explained variance as a metric for model performance.

#### Visualization:
![image](https://user-images.githubusercontent.com/45035308/201222395-f5b57579-707d-4bca-9898-fb944588e9c8.png)



                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:              log_price   R-squared (uncentered):                   0.204
Model:                            OLS   Adj. R-squared (uncentered):              0.204
Method:                 Least Squares   F-statistic:                          1.382e+04
Date:                Sat, 12 Nov 2022   Prob (F-statistic):                        0.00
Time:                        19:43:52   Log-Likelihood:                     -1.8155e+05
No. Observations:               53940   AIC:                                  3.631e+05
Df Residuals:                   53939   BIC:                                  3.631e+05
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
log_carat     -5.0247      0.043   -117.540      0.000      -5.108      -4.941
==============================================================================
Omnibus:                    24261.989   Durbin-Watson:                   0.021
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2866.434
Skew:                           0.097   Prob(JB):                         0.00
Kurtosis:                       1.887   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.


                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                  price   R-squared (uncentered):                   0.881
Model:                            OLS   Adj. R-squared (uncentered):              0.881
Method:                 Least Squares   F-statistic:                          4.004e+05
Date:                Sat, 12 Nov 2022   Prob (F-statistic):                        0.00
Time:                        19:48:07   Log-Likelihood:                     -4.8462e+05
No. Observations:               53940   AIC:                                  9.692e+05
Df Residuals:                   53939   BIC:                                  9.692e+05
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
carat       5666.2701      8.955    632.750      0.000    5648.718    5683.822
==============================================================================
Omnibus:                    26109.286   Durbin-Watson:                   0.344
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           146424.223
Skew:                           2.340   Prob(JB):                         0.00
Kurtosis:                       9.576   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.


## Question 3

Use the `simple_train_test_split` function below and `sklearn.model_selection.train_test_split` 
to evaluate the explained variance of the univariate model.
Use explained variance as a metric for model performance.
Describe the results and create a visualization that helps explain the differences between the two approaches.
```
def simple_train_test_split(X, y, test_size=.3):
    n_training_samples = int((1.0 - test_size) * X.shape[0])

    X_train = X[:n_training_samples,:]
    y_train = y[:n_training_samples]

    X_test = X[n_training_samples:,:]
    y_test = y[n_training_samples:]

    return X_train, X_test, y_train, y_test
```

#### Results:

Using `sklearn.model_selection.train_test_split`:

                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                  price   R-squared (uncentered):                   0.902
Model:                            OLS   Adj. R-squared (uncentered):              0.902
Method:                 Least Squares   F-statistic:                          3.483e+05
Date:                Sat, 12 Nov 2022   Prob (F-statistic):                        0.00
Time:                        19:54:03   Log-Likelihood:                     -3.4175e+05
No. Observations:               37758   AIC:                                  6.835e+05
Df Residuals:                   37757   BIC:                                  6.835e+05
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
carat       5982.4796     10.136    590.198      0.000    5962.612    6002.347
==============================================================================
Omnibus:                    13600.498   Durbin-Watson:                   0.445
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            49102.122
Skew:                           1.820   Prob(JB):                         0.00
Kurtosis:                       7.239   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Using `simple_train_test_split`:
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                  price   R-squared (uncentered):                   0.881
Model:                            OLS   Adj. R-squared (uncentered):              0.881
Method:                 Least Squares   F-statistic:                          2.800e+05
Date:                Sat, 12 Nov 2022   Prob (F-statistic):                        0.00
Time:                        19:54:06   Log-Likelihood:                     -3.3924e+05
No. Observations:               37758   AIC:                                  6.785e+05
Df Residuals:                   37757   BIC:                                  6.785e+05
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
carat       5661.3335     10.698    529.179      0.000    5640.365    5682.303
==============================================================================
Omnibus:                    18235.537   Durbin-Watson:                   1.799
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           102209.523
Skew:                           2.333   Prob(JB):                         0.00
Kurtosis:                       9.573   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

 

## Question 4

Use one-hot encoding to find the best 2-input model by adding either "cut", "color" or "clarity" as a second predictor along with "log(carat)" to model "log(price)". Which 2-input model has the best performance? Report the explained variance score and compare to the corresponding univariate model in question 2. What's the shape of the feature matrix for the "best" model?
