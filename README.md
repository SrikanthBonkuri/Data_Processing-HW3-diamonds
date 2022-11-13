
# hw-diamonds

## Assignment

Use the [diamonds dataset](https://ggplot2.tidyverse.org/reference/diamonds.html) to answer the questions below.
You can get the data directly from the [ggplot2 github repo](https://github.com/tidyverse/ggplot2/).

## Question 1

Visualize the relationship between "price" and "carat" and comment on the type of model that 
might be appropriate for modeling their relationship.

#### Visualization:
![Q1_Relationship of carat vs price](https://user-images.githubusercontent.com/45035308/201501479-cf2ca704-739a-4830-8f00-c9950bbc8b96.png)


## Question 2

Investigate logarithmic transformations to see if you can find a more appropriate relationship
between "price" and "carat" for univariate linear regression.
Use data visualization to help justify your choice of model.
Use explained variance as a metric for model performance.

#### Visualization:
![Q2_Log_Transformed_Carat_by_Price](https://user-images.githubusercontent.com/45035308/201501489-a8be080c-f78f-4762-8f39-e3c4609fcc58.png)

<img width="514" alt="image" src="https://user-images.githubusercontent.com/45035308/201500621-7467a320-51e7-44c9-8065-0b1b73c39ba5.png">

<img width="514" alt="image" src="https://user-images.githubusercontent.com/45035308/201500659-4445ad3e-2924-4f5c-9d33-330732ba51ee.png">



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
<img width="521" alt="image" src="https://user-images.githubusercontent.com/45035308/201500716-bfd0ffb2-7947-4f9c-b08f-d348fa2344e9.png">


Using `simple_train_test_split`:

<img width="519" alt="image" src="https://user-images.githubusercontent.com/45035308/201500739-0663dbbc-c74b-4024-8640-640d6e587293.png">



## Question 4

Use one-hot encoding to find the best 2-input model by adding either "cut", "color" or "clarity" as a second predictor along with "log(carat)" to model "log(price)". Which 2-input model has the best performance? Report the explained variance score and compare to the corresponding univariate model in question 2. What's the shape of the feature matrix for the "best" model?
