

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=59016e2a15959403edd1adb6270f600721a91813500711c7df3d5afdde5de6db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=b7fcfdc8693cd6e0d4ad70251c2d4294d6da78db2d2fbd4d25dc7f512e30b59b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Example Code**:
```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# X_train: Training data for the predictors
# X_test: Testing data for the predictors
# y_train: Training data for the target variable
# y_test: Testing data for the target variable
# test_size=0.3: 30% of the data will be used for testing, and 70% will be used for training
# random_state=42:Ensures reproducibility of the split. Using the same random state will produce the same split every time
```
### Generalization Error
- **Generalization Error**: Measures how well the model predicts new data. The error obtained using testing data approximates this error.
### Cross-Validation
**Cross-Validation**: A technique to assess the model's performance and estimate generalization error by splitting the data into multiple folds.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=3200f7f6643b691387d376961d8e89a283ca139a5d47a6eedd0c96126256700e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=5d519c5727cf9529c5a1644e59c1a957fffba2e99685d7c9d00ed4c7e29c739b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=746721bbb4a92532536b92313c1c1f9dba587c22eb27fd5e448ed3040596801e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Cross-Val Predict
**cross_val_predict** is used when you want to obtain the predicted values for each test fold during the cross-validation process. It returns the prediction for each data point when it was in the test set. This is useful for:
5. **Visualizing Predictions**: You can plot the predicted values against the actual values to see how well the model performs across the entire dataset.
6. **Diagnostics**: It helps in analyzing the residuals (differences between actual and predicted values) to diagnose model performance.
#### Example in Python
Here's an example using `cross_val_predict`:
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Initialize the model
model = LinearRegression()

# Get cross-validated predictions
y_pred = cross_val_predict(model, X, y, cv=5)

# Plot actual vs. predicted values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Cross-Validated Predictions')
plt.show()
```
In this example:
- `cross_val_predict` returns the predicted values for each test fold during the 5-fold cross-validation.
- A scatter plot is created to visualize the actual vs. predicted values.
#### Summary
- **Training Set**: Used to build the model.
- **Testing Set**: Used to evaluate model performance.
- **Cross-Validation**: Provides a robust estimate of model performance by averaging results across multiple folds.
___
## Model Selection and Polynomial Regression
When selecting the best polynomial order, our goal is to provide the best estimate of the
function $ y(x) $.
### Noise in Data
**Noise** in data refers to random variations or errors that obscure the true underlying patterns or relationships. It can come from various sources and affects the accuracy of models.
### **Underfitting** 
**Underfitting** occurs when the model is too simple to fit the data:
- Example: Fitting a linear function to data generated from a higher-order polynomial plus noise results in many errors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=386d95d5e9f6476afc88b19b6e104d7d607f8379c57641ce80eed887a0ffa30b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=d864cbd0c98f2d2553b504b8eb388f895f499c50367288957669e4d6c0ef930d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=70979e8d1c3a5f526690d04a5eef7e06dadf26f7b612244b96f4e59241916b86&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=a0cc87a58b84ae635b8b3e44b1666a528dc25ddeddf65e33296b390755c9252d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN37UOTX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIGHz0hIOnfBQvSuh5sL0Nc6YdR1ulpuTptC%2BLRMHowZQAiAlRsA5024CGWbkM7cPQuzw0NYw%2BaBInqcsu%2Fm%2FxMEjayqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwJNTDbUZQYQoj5MLKtwDylZGfYIWFJTblDU58WVEr4Hag9w4hsBssRHr%2Fv39BY0F57KhKOQkpbsOYSRJXQtYLEQ2FQqZ1EHrgIcdOF0Kth%2BKVvi6ICjZvpEarzddYlvo81Wk8y5O9N3uoPMmmiuzMvU0s7AmOS3yQQlG%2BOB%2B%2FJMybk4tk5M9YctwBySsMRLq08g6vC7TeqDEvng8AKtO8fNFxB8%2BnE8BILqjqdFg4q1rft%2FHBxTJQiFFpg4lKJwtt9A0m2EJtB7AH%2FYJgk2DO4E0ehanF7DgUA9dVmge3mPW5wq%2B6vGjXwM%2BZHJGhcVznzc6npXIc7PMxRl%2F46aIKggEx5KlLtYAbhdMLr5l41D5vsB1Ef2T2Z4ytUfbiyi2adw1ljQNFqeSra8IryQxlq7MAS8%2Fh6zJ8t1jRmCmMM8SHDM4ZzRF6etCHybnybVoMzOG9MFYiYm%2FDK0y%2B3FQ5%2BKupW2Ehb%2BA4ARefy%2FHZwnUDvttfOtTgTJuBx60tJk7VyqiCH6MntDMf0niAgQKnXenV7pgHyPTNX7nKLHMEF93EmygCjLUZOei6oxIr42yXtTs9BKhxNeVhKsgOZtqiVtZ4PCKiFLZysViV1kSD3Xnli1bRxxJAbb8SY3cRnBad%2Fnh1XohjD5yj4wwpL6avQY6pgGHTyQ0TbUEOIJygcoXL3Kj8tLeNoodV0ORT%2Fsgvg9XtzSShpscrWikRErV8zWjsNy7FMN0TJ50UXHh2jXFtYjWRpkKDtY2w9ndxSa76CXWJwB9GAA3RjYoBAiNRibQuPdJaDWPkXTmXDsOiYCQEnPyyfns%2FYx6y0lUMtePv5M6ddbKegEFsxdZroQVChZl7Z%2BIdEizXescG3C%2BHr52Iyp98Qa5uyqn&X-Amz-Signature=3be7cdb890815732a49cb0a5acabdd3aaf64447e6f07c6fd5859624f6111b138&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN37UOTX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIGHz0hIOnfBQvSuh5sL0Nc6YdR1ulpuTptC%2BLRMHowZQAiAlRsA5024CGWbkM7cPQuzw0NYw%2BaBInqcsu%2Fm%2FxMEjayqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwJNTDbUZQYQoj5MLKtwDylZGfYIWFJTblDU58WVEr4Hag9w4hsBssRHr%2Fv39BY0F57KhKOQkpbsOYSRJXQtYLEQ2FQqZ1EHrgIcdOF0Kth%2BKVvi6ICjZvpEarzddYlvo81Wk8y5O9N3uoPMmmiuzMvU0s7AmOS3yQQlG%2BOB%2B%2FJMybk4tk5M9YctwBySsMRLq08g6vC7TeqDEvng8AKtO8fNFxB8%2BnE8BILqjqdFg4q1rft%2FHBxTJQiFFpg4lKJwtt9A0m2EJtB7AH%2FYJgk2DO4E0ehanF7DgUA9dVmge3mPW5wq%2B6vGjXwM%2BZHJGhcVznzc6npXIc7PMxRl%2F46aIKggEx5KlLtYAbhdMLr5l41D5vsB1Ef2T2Z4ytUfbiyi2adw1ljQNFqeSra8IryQxlq7MAS8%2Fh6zJ8t1jRmCmMM8SHDM4ZzRF6etCHybnybVoMzOG9MFYiYm%2FDK0y%2B3FQ5%2BKupW2Ehb%2BA4ARefy%2FHZwnUDvttfOtTgTJuBx60tJk7VyqiCH6MntDMf0niAgQKnXenV7pgHyPTNX7nKLHMEF93EmygCjLUZOei6oxIr42yXtTs9BKhxNeVhKsgOZtqiVtZ4PCKiFLZysViV1kSD3Xnli1bRxxJAbb8SY3cRnBad%2Fnh1XohjD5yj4wwpL6avQY6pgGHTyQ0TbUEOIJygcoXL3Kj8tLeNoodV0ORT%2Fsgvg9XtzSShpscrWikRErV8zWjsNy7FMN0TJ50UXHh2jXFtYjWRpkKDtY2w9ndxSa76CXWJwB9GAA3RjYoBAiNRibQuPdJaDWPkXTmXDsOiYCQEnPyyfns%2FYx6y0lUMtePv5M6ddbKegEFsxdZroQVChZl7Z%2BIdEizXescG3C%2BHr52Iyp98Qa5uyqn&X-Amz-Signature=c5a1d72bafd1be90a555d97ddcd0e772fda68b1be3f3e62d949d9c2542939a20&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN37UOTX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIGHz0hIOnfBQvSuh5sL0Nc6YdR1ulpuTptC%2BLRMHowZQAiAlRsA5024CGWbkM7cPQuzw0NYw%2BaBInqcsu%2Fm%2FxMEjayqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwJNTDbUZQYQoj5MLKtwDylZGfYIWFJTblDU58WVEr4Hag9w4hsBssRHr%2Fv39BY0F57KhKOQkpbsOYSRJXQtYLEQ2FQqZ1EHrgIcdOF0Kth%2BKVvi6ICjZvpEarzddYlvo81Wk8y5O9N3uoPMmmiuzMvU0s7AmOS3yQQlG%2BOB%2B%2FJMybk4tk5M9YctwBySsMRLq08g6vC7TeqDEvng8AKtO8fNFxB8%2BnE8BILqjqdFg4q1rft%2FHBxTJQiFFpg4lKJwtt9A0m2EJtB7AH%2FYJgk2DO4E0ehanF7DgUA9dVmge3mPW5wq%2B6vGjXwM%2BZHJGhcVznzc6npXIc7PMxRl%2F46aIKggEx5KlLtYAbhdMLr5l41D5vsB1Ef2T2Z4ytUfbiyi2adw1ljQNFqeSra8IryQxlq7MAS8%2Fh6zJ8t1jRmCmMM8SHDM4ZzRF6etCHybnybVoMzOG9MFYiYm%2FDK0y%2B3FQ5%2BKupW2Ehb%2BA4ARefy%2FHZwnUDvttfOtTgTJuBx60tJk7VyqiCH6MntDMf0niAgQKnXenV7pgHyPTNX7nKLHMEF93EmygCjLUZOei6oxIr42yXtTs9BKhxNeVhKsgOZtqiVtZ4PCKiFLZysViV1kSD3Xnli1bRxxJAbb8SY3cRnBad%2Fnh1XohjD5yj4wwpL6avQY6pgGHTyQ0TbUEOIJygcoXL3Kj8tLeNoodV0ORT%2Fsgvg9XtzSShpscrWikRErV8zWjsNy7FMN0TJ50UXHh2jXFtYjWRpkKDtY2w9ndxSa76CXWJwB9GAA3RjYoBAiNRibQuPdJaDWPkXTmXDsOiYCQEnPyyfns%2FYx6y0lUMtePv5M6ddbKegEFsxdZroQVChZl7Z%2BIdEizXescG3C%2BHr52Iyp98Qa5uyqn&X-Amz-Signature=fcdf1b406de55dfd65bbc2a60b7b18f97b4dacca5c2baec78979c00209b58821&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=cec9af72133db49c7fb7ed83f8ade9db279c65bd5542ddc748e0367ebc9b5d9a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Calculating R-squared Values**
7. Create an empty list to store R^2 values.
8. Create a list of different polynomial orders.
9. Iterate through the list using a loop:
	- Create a polynomial feature object with the order as a parameter.
	- Transform the training and test data into polynomial features using the `fit_transform` method.
	- Fit the regression model using the transformed data.
	- Calculate the R^2 value using the test data and store it in the list.
Here's an example of how you can implement this in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Store R^2 values
r2_values = []

# List of polynomial orders
orders = [1, 2, 3, 4]

# Iterate through polynomial orders
for order in orders:
    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    x_poly = poly.fit_transform(x.reshape(-1, 1))

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Predict and calculate R^2
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    r2_values.append(r2)

# Plot R^2 values
plt.plot(orders, r2_values, marker='o')
plt.xlabel('Order of Polynomial')
plt.ylabel('R^2 Value')
plt.title('R^2 Value vs. Polynomial Order')
plt.show()
```
Output:
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=045bc8a9b62dfcd4f3cba36d6a24fe8c2df3c6724b289be658b07650aae1d032&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=ef19a0409543d8b38e430dbcaa65198ec3bb3c8b3fa04c351ca07e3f8ab778c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=ad1f44f6ecee944cb4302598498ed552fff4917c187e04ec7b0faca64bc24dc0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=fe806681839da348d249a1d529f018f24900cb4fe54a492424f4673216604a21&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QRFPZIW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAPjo9AGvQBlYReTIOwBvzRqg5UVZSc8XrlBbJW1L6lWAiEAjTZRBKE4uUIeXfWFM0sKW5KwUt%2B6VvE9a1DzezF7CT0qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDItLQY1%2FMH38HewCPyrcAyzkRlgHTtu8x9y4LeU1ZDr1PoRMCH5dwWzzaanQJ4cW%2BvFyiAL%2FKIGgLThVOAOTfGmkA62RjEsNiTdZmSLbxvYGnPYqkY%2BK0iucHkO1Qyx7r4cnbvfTesUiwSaCFmeIZfIv1eVilw8foBbtoe%2FdyZE%2BMfDcdY98GixpKA6lHdzxcuJC2QiRjc8O%2F2r1ANLASHGcLXT1OonHsAVTdC9W%2BPFn5TeoqR8NtiuP5ICfstGFZ1tW9vGK5f%2B386NIn3l%2B%2F%2F47cyPdrRoGrzL2Y57SwjtljhzueadueeyX90YpnQg5Kiy9g7kh%2F%2BEG27H2nxISTAsFkKKXAYm5lOCZQx8jZhBzOL28LLkMm8R9Ia4p5ZR0QImB%2F9%2BCdhtGeftXWrMam%2FpSBkiS8NNiIuv6zh%2Fzcui%2BfNZFg43BhTITjpQCK6bpLxXCIEzmEOCifqeBI9666u3fKZNWIGEAmXhGTLpbSzXP0MqpARLutoge%2FBXqdJAI8MftOFXRoorsWmqrH9AhnJcibia4MZ99MmAN4BQhJP35MfXDxFDPYzr3YU8nyhQDuslLFzpJs86LiXelXTwtIp7XVSHdHjwOspKekPi4kYekSEtsOI2GW4rNYLklovBPdyub%2F1hGtzQLiAvPMI%2B%2Bmr0GOqUBrAhbj8M2VZFP1f0GWzJHJuMhZuYbCZq2ageajtAFF5kW4h4YC2gIHo24xmoTlv2knFiGwvmrrBCnxiIb%2Bya7zK5RW2nczxUFwD7e9nxcTM7I9hvEQdRPvlIjU5g3%2F9%2FdVS2hbuFWbRvs6GH6%2BtFtj1qnA7F7AnVyAV6UTdxSEc3ol9EE6OUzojFGSMJVWb92tf3QxMn%2BjoRQiFPBXYAXZ2J3qQr4&X-Amz-Signature=601f2228be33656971378a4a81add8a2c38f95744dc0df736497420c43745de8&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GLRE36M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBGhyO20kgV9Xax%2FvLF5Ys%2FJLn8th6B6bn8%2BheSFZVPNAiEAyzkeOebqXYUK5bjphrhXlxeNfQXGshHwFvORoYLXgb8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBwhoCVe%2BM06Mi5FCrcA%2F%2BEY7zfxnvXAClWgjdTBxWkwHKbOAx1ovLcTiAi51xdxQjpQTk4iejJUpz%2BEb17CsHLcbTVIqG%2BgjdHKg27Nei07jN1IwlVd3v7kx4mENMVcaCZGdVk0aYX%2F6m3gfzmigc0yyosM5D8WW0CtNSW024L0CTHvvVCP9lurnrYF5bfj2t57luJG2zrNZVcCB7YBl2RMpX5vJPVmivLJ0t%2Ftq%2BlL0xzqM33xiLeExc1%2BXvHIUl5xJFUIM2ieaIoYp%2FO8BgoPUg1XYEMmq3vayv%2BFFPt%2FA16v4g9%2BCn1lRVI6%2FnSt8Sfuam4hQjLPJu8zipPzSmVisspfKjlyjYznacu8JogqIqqdnVUMvWk648QaSoLhOWeMtuvTt40okcEbNw0ZwuHe3Iz5fHcQGydSPaBKV%2FYCmXqR7zN414QPJeTcVd1Ko5VRs%2FJtLk8cdoTo6q4AjdVtaG7ZbIsEIWVyXfhV1oJfAnAOfvPkLa5D%2FhonEPAlk8WD06xuSTAr%2BIODqaEGkbD8uvujKkaDF%2FDN9Efr4AovsVY5REIF1Zly0up4gPJeqkoDPhh7JsojsaFLQZ8cI0s0bRcG%2BF1uSo%2FYY2scT3EgfPrGL8xk5sAVIQ8MdGQc6OHWboAmbdFhWwoMNy%2Bmr0GOqUBGjxnB46bG%2BWh1NlV0ml%2Fn6K1qIs7O6C9QQwRva9J8DwGJhhWFvEKqbGfn5iqyDe4YzdtgDTxeklpu7i6mTM2eVErbZsFDnheUazrTm8xPtzAIF0%2Fq%2FGPgFAhkNenYoLpmThOVYdnK%2B0Pfy3LsrGHKDG3N9z0vicy1ee%2BW9mUxqJi70trHxSepzckqKORr5W6opxMQVr3gsifohGgwR0BjtM5DVK3&X-Amz-Signature=80fac0646957fb99b5de4e0faafdc027792c73667511f1d1bb3160b1d1d876a6&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GLRE36M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBGhyO20kgV9Xax%2FvLF5Ys%2FJLn8th6B6bn8%2BheSFZVPNAiEAyzkeOebqXYUK5bjphrhXlxeNfQXGshHwFvORoYLXgb8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBwhoCVe%2BM06Mi5FCrcA%2F%2BEY7zfxnvXAClWgjdTBxWkwHKbOAx1ovLcTiAi51xdxQjpQTk4iejJUpz%2BEb17CsHLcbTVIqG%2BgjdHKg27Nei07jN1IwlVd3v7kx4mENMVcaCZGdVk0aYX%2F6m3gfzmigc0yyosM5D8WW0CtNSW024L0CTHvvVCP9lurnrYF5bfj2t57luJG2zrNZVcCB7YBl2RMpX5vJPVmivLJ0t%2Ftq%2BlL0xzqM33xiLeExc1%2BXvHIUl5xJFUIM2ieaIoYp%2FO8BgoPUg1XYEMmq3vayv%2BFFPt%2FA16v4g9%2BCn1lRVI6%2FnSt8Sfuam4hQjLPJu8zipPzSmVisspfKjlyjYznacu8JogqIqqdnVUMvWk648QaSoLhOWeMtuvTt40okcEbNw0ZwuHe3Iz5fHcQGydSPaBKV%2FYCmXqR7zN414QPJeTcVd1Ko5VRs%2FJtLk8cdoTo6q4AjdVtaG7ZbIsEIWVyXfhV1oJfAnAOfvPkLa5D%2FhonEPAlk8WD06xuSTAr%2BIODqaEGkbD8uvujKkaDF%2FDN9Efr4AovsVY5REIF1Zly0up4gPJeqkoDPhh7JsojsaFLQZ8cI0s0bRcG%2BF1uSo%2FYY2scT3EgfPrGL8xk5sAVIQ8MdGQc6OHWboAmbdFhWwoMNy%2Bmr0GOqUBGjxnB46bG%2BWh1NlV0ml%2Fn6K1qIs7O6C9QQwRva9J8DwGJhhWFvEKqbGfn5iqyDe4YzdtgDTxeklpu7i6mTM2eVErbZsFDnheUazrTm8xPtzAIF0%2Fq%2FGPgFAhkNenYoLpmThOVYdnK%2B0Pfy3LsrGHKDG3N9z0vicy1ee%2BW9mUxqJi70trHxSepzckqKORr5W6opxMQVr3gsifohGgwR0BjtM5DVK3&X-Amz-Signature=032b4668ad0e9ce1c3b0ef143e18c0826baa759f9564a281a2a4c732696e4bcc&X-Amz-SignedHeaders=host&x-id=GetObject)
12. **Model Training**:
	- **Procedure**: Use cross-validation to select the optimal Alpha. Split the data into training and validation sets.
	- **Steps**:
		1. **Train Model**: Fit the model using different values of Alpha.
		2. **Predict & Evaluate**: Use validation data to make predictions and calculate the R^2 or other metrics.
		3. **Select Alpha**: Choose the Alpha that maximizes the R^2 on validation data.
13. **Implementation in Python**:
	- **Import**:
```python
from sklearn.linear_model import Ridge
```
	- **Create & Fit Model**:
```python
ridge = Ridge(alpha=1.0)  # Set the desired alpha value
ridge.fit(X_train, y_train)
```
	- **Predict**:
```python
y_pred = ridge.predict(X_test)
```
14. **Cross-Validation**:
	- **Purpose**: Used to determine the best Alpha by comparing performance metrics (e.g., R^2) across different Alpha values.
	- **Process**: Train with various Alpha values, evaluate with validation data, and select the best-performing Alpha.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CDQWCXT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCICUR4nGxyLLojy7N2fzHZt67fYYz1OLLgxS5hjkrH9UbAiEA2PW%2Flh5A2Jsp4veXwdm8FpO73p8asi84RnoVju4Y6PgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJPg0OT6e0mE7nn%2BACrcA3M80WtnyXqBFdbia7ZMpxo4XwMULAiCvPtIO%2BmYbTyKvb%2BHLPw5WE%2F40Si1DsGOKG8GIEpvkaAbPfJxCyAyK010xRuZgptyT%2B25H%2BB4SOe9iRa5RpbspDG%2B3jn0I2ilE994DXHAdJhlV5W3JMYpINq5HTnYTJb3PP45Y3ZNS5uPf3mUJL25i%2BQ9sYJR1sE4Hy6hT9S4npdiC%2FjGK1eIFtCgrGiTIprqp9kzG1VU3PLiqT04G1dtMKsm9elNn8FX5gZ9wwpEUiu2qHkZZi3m%2BTFadaarQSZ40smDIw61cYZh2VNVb%2BoQ354vjD1tkDduaiHygvCVYtLcv%2BxMEAfM%2B17zgW6AgkE1FhAIVgXAOn9uDvRn4mO%2FKNxc8P0KuMKKxAbR4eZZQPWWXEuy2pijZH2grgoR8PExOUoSiRcbG8adwmyjU8ArxJ5XD4Sb4GCqdKrCJQks4fETzbXgEf0Uc3%2FgdYzZDxxcTyfsFd1tybCa9JESwaZQdP%2FbW0yAf49hoe5YufzZdOVl%2Fe3tx0paLc2C1U%2F6EZDRUmlmx7lThDsbGDDPMOsmnwQWkq8CuUVIZeX5JorHQKbxQvUNycFf3FdBvba%2F0FPKAuxoo7rX%2BvHs0vSx2Fa93R1iNZuKMNa%2Bmr0GOqUBVSycpwvtX84fUzmE4JW%2FZsnsM79c%2Btyp8oy%2B9AZ6%2BNMLp7DeN%2FZ9j7XM450qGaNOfDkBsZLoCXyn%2BxHBExXElcSYWPI0VjGlv9ost4XKX0EMVXIAC2lPHHaEd6DBdgeIRakmJaiQyIiQKVL7H%2BIJMeNs68BafcdPVE9OThhTmgqw8M9DOZ8%2FtXhaHPbW4WndBWZAIWD%2F%2F7HWrl2pA%2B64LbuBeTTR&X-Amz-Signature=cb3890f2b15259cf097e9e18139005c5fe3a3e501ccef4d59cae6d309af36b51&X-Amz-SignedHeaders=host&x-id=GetObject)
15. **Example Visualization**:
	- **Plot**: Shows R^2 values vs. different Alpha values for training and validation data.
	- **Interpretation**:
		- **Training Data**: R^2 might increase with Alpha but eventually converge.
		- **Validation Data**: R^2 may decrease with high Alpha due to reduced model flexibility.
___
## Grid Search for Hyperparameter Tuning
### **Grid Search**
A method for finding the best hyperparameters for a model by systematically evaluating different combinations.
- **Hyperparameters**: Values like Alpha in Ridge Regression that are not learned from the data but set before the training process.
- **Process**:
	1. **Define Hyperparameters**: Set up a grid of hyperparameter values to test. For Ridge Regression, this might include values for Alpha and normalization options.
	2. **Train and Evaluate**: Train the model using each combination of hyperparameters. Evaluate each model using cross-validation, typically using metrics like R² or Mean Squared Error (MSE).
	3. **Select Best Parameters**: Choose the hyperparameters that give the best performance based on the evaluation metric.
### **Implementation in Scikit-learn**
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Define parameter grid
param_grid = {
    'alpha': [0.1, 1, 10],
    'normalize': [True, False]
}

# Initialize Ridge model
ridge = Ridge()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, scoring='r2', cv=5)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_
cv_results = grid_search.cv_results_

# Results
print("Best Parameters:", best_params)
print("Best Score:", best_score)
print("Best Estimator:", best_estimator)
print("CV Results:", cv_results)
```
**Example Result:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRZPVL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBdI3crUE3jjmDk5%2BN2pNNpXLluufNBQkwxUa7WpHPcUAiBNWwFrhr07yMWRk5RVde4RExPf6weRAnpyDCubh8z%2FziqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWrtM5eNRDJ8m%2FL5wKtwDVuES4QLepxHfB8r92pyB4Ow7aNMzolW9lFgK8zoisWNHUxyRD4gO%2F99aNdfmj5r1VHnBt7hdDTDD5bk8ASGg%2BOm84BLrdv5jFWoB2a6e9dJ7%2BDFIGzSFreJ7cZgAOpUSXhtX9tf3Q7BkWG%2BIXY4ZpUahm3PMe7AKKBdufMgYTfwJtvpUQmSALSY51MEJAmZkM1VNLLY519QVUKuZkm6Ug%2BKfwLyP%2FhJ7xBYRwgsHGonADFJHbNn9acXfvCyzm5OEtgwQB1Wyl9jMODOK%2B%2BP0Q89PNuZcrGF30pj4X5SoDzIFyKcSsvo727u6Raa3x4s64kEBSr1sEZSYFzLjw0mzyI8xoXfATt3egyUKiQPEcgVOPrJ0cz1Q63CfuPDyMrA1F4zEGIKLqpbWSRREkf2dYT7ww1ZtoOteNJPzbZ7aQP3eqL%2BRlrmsUU19yaqgsm2vLbgjA7P7FcO1WjDHXrLFZjR%2FtmrfnmibR3GAUzWnCUe6X%2FzVVQmrPNEPuHGAUC9lUZWjkOaD7CWZ98tjmJMt0fiqZzCfcKlVkhVg7ssZvG%2F5xYyQDfKjD2maEKf4%2B3YOcttAFaV5mNURL52xPcIYZQIY08WmW7kHuIQp5tRGL%2F8OX3dqiq0YL7O%2BQo4wj76avQY6pgFumLr%2BstjrA4lgEvKwfE8SCVg%2BzLkH7LJhCvroRDcFHrvwOU57aHiSJZPr8GA7NPyOtHl0DgI7PAuPzRSZKgtTulOslnyPG8ztAvZy7Aem6LQ0kUNzG8uHW9Au%2FcgkYwZovkQM6VBpJIsHszeh4VfuYgl2E7TsZ6knXAsoyhYudNumlVzd%2B71GGpWbRjbIZOzoJ3suDS%2Bd3zJU6%2FWyeNCw4cROvR5P&X-Amz-Signature=d7b2cfbee1172f646f5bcd08e193d55d477ceceb7dbd85cea2134dc0e151a37f&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Key Attributes**:
	- `**best_estimator_**`: Best model found.
	- `**cv_results_**`: Detailed results for each hyperparameter combination, including scores and parameters.
- **Advantages**: Efficiently explores multiple hyperparameter values to find the best combination, reducing the manual effort required for model tuning.
___
## Cheat Sheet: Model Evaluation and Refinement
### Splitting Data for Training and Testing
The process involves separating the target attribute from the rest of the data, treating it as the output, and the rest as input. Then, split these into training and testing subsets.
```python
from sklearn.model_selection import train_test_split

# Define target and features
y_data = df['target_attribute']
x_data = df.drop('target_attribute', axis=1)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
```
### Cross Validation Score
Cross-validation involves creating multiple subsets of training and testing data to evaluate the model’s performance using the R² value.
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation
Rcross = cross_val_score(lre, x_data[['attribute_1']], y_data, cv=n)

# Calculate mean and standard deviation of scores
Mean = Rcross.mean()
Std_dev = Rcross.std()
```
### Cross Validation Prediction
Generate predictions using a cross-validated model.
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation prediction
yhat = cross_val_predict(lre, x_data[['attribute_1']], y_data, cv=4)
```
### Ridge Regression and Prediction
Use Ridge regression to create a model that avoids overfitting by adjusting the alpha parameter and making predictions.
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

# Initialize polynomial features
pr = PolynomialFeatures(degree=2)

# Transform features
x_train_pr = pr.fit_transform(x_train[['attribute_1', 'attribute_2']])
x_test_pr = pr.transform(x_test[['attribute_1', 'attribute_2']])

# Initialize Ridge model
RigeModel = Ridge(alpha=1)

# Fit the model
RigeModel.fit(x_train_pr, y_train)

# Make predictions
yhat = RigeModel.predict(x_test_pr)
```
### Grid Search
Use Grid Search to find the optimal alpha value for Ridge regression by performing cross-validation.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Define parameter grid
parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000]}]

# Initialize Ridge model
RR = Ridge()

# Initialize GridSearchCV
Grid1 = GridSearchCV(RR, parameters, cv=4)

# Fit GridSearchCV
Grid1.fit(x_data[['attribute_1', 'attribute_2']], y_data)

# Get the best model
BestRR = Grid1.best_estimator_

# Evaluate the model
score = BestRR.score(x_test[['attribute_1', 'attribute_2']], y_test)
```
___