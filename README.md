
# hw-diamonds

## Assignment

Use the [diamonds dataset](https://ggplot2.tidyverse.org/reference/diamonds.html) to answer the questions below.
You can get the data directly from the [ggplot2 github repo](https://github.com/tidyverse/ggplot2/).

## Question 1

Visualize the relationship between "price" and "carat" and comment on the type of model that 
might be appropriate for modeling their relationship.

#### Visualization:

![Q1_Relationship of carat vs price](https://user-images.githubusercontent.com/45035308/201501479-cf2ca704-739a-4830-8f00-c9950bbc8b96.png)

The relation doesn't seems to be linear. Instead it is the price which is increasing exponentially with carat.


## Question 2

Investigate logarithmic transformations to see if you can find a more appropriate relationship
between "price" and "carat" for univariate linear regression.
Use data visualization to help justify your choice of model.
Use explained variance as a metric for model performance.

#### Visualization:
![Q2_Log_Transformed_Carat_by_Price](https://user-images.githubusercontent.com/45035308/201501489-a8be080c-f78f-4762-8f39-e3c4609fcc58.png)

<img width="514" alt="image" src="https://user-images.githubusercontent.com/45035308/201500621-7467a320-51e7-44c9-8065-0b1b73c39ba5.png">

Explained Variance Score on Log Transformations: 0.9329893079520857

<img width="514" alt="image" src="https://user-images.githubusercontent.com/45035308/201500659-4445ad3e-2924-4f5c-9d33-330732ba51ee.png">

Explained Variance Score on carat vs price: 0.8493305264354858

* The Logarithmic transformed relationship has best score.

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

* Using `sklearn.model_selection.train_test_split`:

<img width="520" alt="image" src="https://user-images.githubusercontent.com/45035308/201953034-bffe1038-ad69-4a2c-857d-7c4a48b7c3d6.png">

Explained Variance Score on sklearn.model_selection.train_test_split: 0.9338222756481153

![Q3_Log_Transformed_Carat_by_Price-sklearn test split](https://user-images.githubusercontent.com/45035308/201953549-cb7c0ceb-01e9-4cd7-9f4e-fc34f326ad0c.png)


* Using `simple_train_test_split`:

<img width="513" alt="image" src="https://user-images.githubusercontent.com/45035308/201953425-6cc0a2ec-34c1-4009-a42a-40e5454441c6.png">

Explained Variance Score on simple_train_test_split: 0.7178769798196256

![Q3_Log_Transformed_Carat_by_Price-simple test split](https://user-images.githubusercontent.com/45035308/201953590-42382032-c340-4299-b9e9-103a9edb9a32.png)

* The simple train test split is biased or has splitted data concentrated towards higher and lower values respectively though the data set.
  Whereas in sklearn split, it's not biased and training and test set randomly scattered though the dataset.
  The best score is observed on sklearn selection split model.
  


## Question 4

Use one-hot encoding to find the best 2-input model by adding either "cut", "color" or "clarity" as a second predictor along with "log(carat)" to model "log(price)". Which 2-input model has the best performance? Report the explained variance score and compare to the corresponding univariate model in question 2. What's the shape of the feature matrix for the "best" model?

#### Results:

* Adding "cut" as second predictor:

Feature Matrix Shape: (53940, 6)

<img width="469" alt="image" src="https://user-images.githubusercontent.com/45035308/201957271-dca3f6c5-c983-4b4d-868d-264d1ec96037.png">

Explained Variance Score of log_price vs (log_carat, cut): 0.937101149869116

* Adding "color" as second predictor:

Feature Matrix Shape: (53940, 8)

<img width="461" alt="image" src="https://user-images.githubusercontent.com/45035308/201958120-64957f7b-d53d-4170-92a7-f92436f23b74.png">

Explained Variance Score of log_price vs (log_carat, color): 0.9453594219733898

* Adding "clarity" as second predictor:

Feature Matrix Shape: (53940, 9)

<img width="459" alt="image" src="https://user-images.githubusercontent.com/45035308/201958685-9a4bd951-48c4-4549-a0e4-93fb72141b20.png">

Explained Variance Score of log_price vs (log_carat, clarity): 0.9653665672815918

* The 'cut' feature has 5 categories in it. The 'color' and 'clarity' features had 7 and 8 categories in it respectively.
* The 2-input model (log_carat, clarity) with feature matrix shape (53940, 9) has best performance among these.

