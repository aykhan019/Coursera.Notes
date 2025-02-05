

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=1cec3922e73ee45cd31838feec6981ff63aa6995d73346154b735f4fb14bd0f3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=a88a7b832361936e996ae23c43c8578612548a2e8e0a7ef36a8a0781f4165c34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=a1d06ebad2986de36a89064e6232b2c0cb53deaedbb81f54dcaa6d83806d60e8&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=44fb164d44984e80f7edf674ed12e4615faf1a79cc3b48b177616b09cfdffbd3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=797bafd339631f353796d062567d780f31ab656fbfa54ea4cde287d1b5bc0321&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=a3ffbe570835cf18f1512f2e03ea18deb10db551aa747c324ffb49b1bf795253&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=cabd97e1980426610e853f99e6740b3352747160d4a79ac2ab9417581149137a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=8d5da8bbd6da0b2ae830b037b9a515e844ce77042f28957e726af8b9b4576f8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=a1e9e9680e8c2ae7e85acfb809d938ac3350d8055deff7eea7d104b81d524729&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC2BD35L%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCICKflvA3qugF%2F7IAOSY%2FESfc84IyD0N5XFSNDEQ2x3VjAiEAu0XC7JNWRIrYTfygxvxjSJAP%2FR7zPTBVWn0dg9%2Bdozgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDL45Ypw4lN0frSqKXircAzH0CVZEYhbyPHoCdObz7TTGe3M1iX%2B4XxjQ8J80IrfeLJ4AlWhXV2ESudjTvpXrySSCpulyNMJWLixvWDMEkaQgNVPscoWxG775sgJm1sHDx2jJA%2FUs9Qmi0yUYN7gaOHSRkUgHsRddZooi%2FhB07wWbe%2BARsOk2HDrUT8XwQH%2FURF0zQfGwTmHCwYo46ysG7CVVNwf6iyEl%2B%2BGSvqKejcZy4w%2BQ1FV8b2N7FM5r98QVv5B4fWh59YC%2FCOPh8BDJRxtfWDlQeYek1ldARol%2BncxfGXClWLhuvV4kS5tzQ86JD%2BSS9I3bbK2L7e4r%2FcOshrj3Ty6GMfpjdM5r2vrWdofBHsq1diwjwPLTrOxErW2bLOpn%2B1NY45KGOYzy3GQI84aXSXLfN%2F%2B%2Fz%2FbacWKI%2BzRjk%2BX%2BTujLZGIMtRDBl7nqLG6G5vkZQKRMgcR%2BKu0oKVhdJgQnUXhAjUMpvf4VVdBEPEpKyGeWCbo9LZb3tnxz9BWJpgoAkNEgUPfOh4%2FgmxfHGgT7tnuygXCAxPA7EFMQzErjCOQya1Jfj%2Bih1aHV%2FXu1cbpVHgT0WE8sRCU1kOWV4m4iQrNnO4Th6ca0aWyqXqNJxdWtrN16SBBGL54w1PmcnhLqJciIPT%2F9MPyKjb0GOqUBovNh2QsnKdUe7X%2FUNZGiVZeaLmt52tXJTbnJwzgHev8BHm2U%2FXIqYZgGd68vmSs7w6ENW6j8XAJEV0aR8mwEEeKpMxPiV7%2BQzKr5wvXi7oIBGVd0iI%2BtjpsOuSYZfWVptMhgyyPhKNjZ9alHW%2BMpcT6mY9%2BoWzWVSKuRbr7BBy3JFUSJpif%2B0kr5zjv8I4TKMUr8uRei2KpwZWeoLSKZtkuTlZPK&X-Amz-Signature=9307e5d89496113c5e0f8631a545f32a73c35315122f4bb23fa3fae609864115&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC2BD35L%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCICKflvA3qugF%2F7IAOSY%2FESfc84IyD0N5XFSNDEQ2x3VjAiEAu0XC7JNWRIrYTfygxvxjSJAP%2FR7zPTBVWn0dg9%2Bdozgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDL45Ypw4lN0frSqKXircAzH0CVZEYhbyPHoCdObz7TTGe3M1iX%2B4XxjQ8J80IrfeLJ4AlWhXV2ESudjTvpXrySSCpulyNMJWLixvWDMEkaQgNVPscoWxG775sgJm1sHDx2jJA%2FUs9Qmi0yUYN7gaOHSRkUgHsRddZooi%2FhB07wWbe%2BARsOk2HDrUT8XwQH%2FURF0zQfGwTmHCwYo46ysG7CVVNwf6iyEl%2B%2BGSvqKejcZy4w%2BQ1FV8b2N7FM5r98QVv5B4fWh59YC%2FCOPh8BDJRxtfWDlQeYek1ldARol%2BncxfGXClWLhuvV4kS5tzQ86JD%2BSS9I3bbK2L7e4r%2FcOshrj3Ty6GMfpjdM5r2vrWdofBHsq1diwjwPLTrOxErW2bLOpn%2B1NY45KGOYzy3GQI84aXSXLfN%2F%2B%2Fz%2FbacWKI%2BzRjk%2BX%2BTujLZGIMtRDBl7nqLG6G5vkZQKRMgcR%2BKu0oKVhdJgQnUXhAjUMpvf4VVdBEPEpKyGeWCbo9LZb3tnxz9BWJpgoAkNEgUPfOh4%2FgmxfHGgT7tnuygXCAxPA7EFMQzErjCOQya1Jfj%2Bih1aHV%2FXu1cbpVHgT0WE8sRCU1kOWV4m4iQrNnO4Th6ca0aWyqXqNJxdWtrN16SBBGL54w1PmcnhLqJciIPT%2F9MPyKjb0GOqUBovNh2QsnKdUe7X%2FUNZGiVZeaLmt52tXJTbnJwzgHev8BHm2U%2FXIqYZgGd68vmSs7w6ENW6j8XAJEV0aR8mwEEeKpMxPiV7%2BQzKr5wvXi7oIBGVd0iI%2BtjpsOuSYZfWVptMhgyyPhKNjZ9alHW%2BMpcT6mY9%2BoWzWVSKuRbr7BBy3JFUSJpif%2B0kr5zjv8I4TKMUr8uRei2KpwZWeoLSKZtkuTlZPK&X-Amz-Signature=a7b587d06f6f8fb77e6425e2d8968ad20a45a55c9092cc1dd59cec18b957ac5f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WC2BD35L%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCICKflvA3qugF%2F7IAOSY%2FESfc84IyD0N5XFSNDEQ2x3VjAiEAu0XC7JNWRIrYTfygxvxjSJAP%2FR7zPTBVWn0dg9%2Bdozgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDL45Ypw4lN0frSqKXircAzH0CVZEYhbyPHoCdObz7TTGe3M1iX%2B4XxjQ8J80IrfeLJ4AlWhXV2ESudjTvpXrySSCpulyNMJWLixvWDMEkaQgNVPscoWxG775sgJm1sHDx2jJA%2FUs9Qmi0yUYN7gaOHSRkUgHsRddZooi%2FhB07wWbe%2BARsOk2HDrUT8XwQH%2FURF0zQfGwTmHCwYo46ysG7CVVNwf6iyEl%2B%2BGSvqKejcZy4w%2BQ1FV8b2N7FM5r98QVv5B4fWh59YC%2FCOPh8BDJRxtfWDlQeYek1ldARol%2BncxfGXClWLhuvV4kS5tzQ86JD%2BSS9I3bbK2L7e4r%2FcOshrj3Ty6GMfpjdM5r2vrWdofBHsq1diwjwPLTrOxErW2bLOpn%2B1NY45KGOYzy3GQI84aXSXLfN%2F%2B%2Fz%2FbacWKI%2BzRjk%2BX%2BTujLZGIMtRDBl7nqLG6G5vkZQKRMgcR%2BKu0oKVhdJgQnUXhAjUMpvf4VVdBEPEpKyGeWCbo9LZb3tnxz9BWJpgoAkNEgUPfOh4%2FgmxfHGgT7tnuygXCAxPA7EFMQzErjCOQya1Jfj%2Bih1aHV%2FXu1cbpVHgT0WE8sRCU1kOWV4m4iQrNnO4Th6ca0aWyqXqNJxdWtrN16SBBGL54w1PmcnhLqJciIPT%2F9MPyKjb0GOqUBovNh2QsnKdUe7X%2FUNZGiVZeaLmt52tXJTbnJwzgHev8BHm2U%2FXIqYZgGd68vmSs7w6ENW6j8XAJEV0aR8mwEEeKpMxPiV7%2BQzKr5wvXi7oIBGVd0iI%2BtjpsOuSYZfWVptMhgyyPhKNjZ9alHW%2BMpcT6mY9%2BoWzWVSKuRbr7BBy3JFUSJpif%2B0kr5zjv8I4TKMUr8uRei2KpwZWeoLSKZtkuTlZPK&X-Amz-Signature=ef1a2967df31a3510b5e7d2a17537c37480518a94b29f5127326b6a76a30b5e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=ec2fa01f9c1833a8d17aae7f1c69a72bfeefdedc66d9c4c485bc8b07ecfa05d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=d700fb0749774de9f5e55ddd3bcee1bf0f880d759d3759d6d8bd926226d3e57b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=35481c24f527c6c23e7c498c050a672c3b3dadbd40fdcd0bae3aa10be00f0238&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=089f6f828702ffef6e2babbc5b9a6b9923160ece3c21627257d98657b0f55ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=50bbdd1faf86ddd568e922ca3c206107396cee24c8e26d69a6d66837168874e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NUPP72O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCp18zfPzJl1HEAhkGvh4nsxjY2ldxk2mtB3z4MnfZlxQIhAJ9GRaVYrdiyCVTU7A6gmmGPcrgJad08X54qUszc4wGEKv8DCEQQABoMNjM3NDIzMTgzODA1Igyf%2FHdWvehQ29odwGoq3ANVDvZgR5LhJApubio8laeUQhaI1FLSlsSBiGDLDTk7LSpOHnj7M12waX7G1ahQtaYbciLxUd%2BgSQN48XyYaesRgwDNOBUBLW1utMm%2Fh5MnW24Z1C8BHeRp9m6Df7Am7yPXYWA2FfEq480WDFbfZLHYcGXesQWZU7EZj6UF7vHmoYcZCSmd6YAg84xvCfinoiDyZIhxOr9%2F88wO%2F7X8LYnfJFZDuSiyVXvAGxaeaz132q8GHN93bLQQpKiEhPa1MVykILg4raQo2tkbJikGhhlwWpB17Rv3xcN30wz%2F9m8H0iof0zExXeKyAFatUcwLiO4trT3PnUtyJ8uNiEMB%2F8btSCCpdcDE9qOgT5Lmslq8LXQj1p4XWx005Mq%2BLpUQZS4ifzulyaRWnjBv5LLOhdqODsuPqhg%2BGU2DuKscxKVlVV6Ta48xdQRsfYYr4Pk%2F6mtuBLqODbUDWFdh0kb8%2BaX08Br2hDg7Jdw0u7kdEXpmz5uj%2F6C6p8PmYMpqzW%2Fl4qymeM8%2BEibhWC2TP%2FHzeStfv1lBHgJ4i3Vd7OrWME4%2Bgbet7ESj8H1xO3E83uEcaqTNkuOb1tvrvw70Ef3mX6YdnYWFIoa%2FxCS0QIDZqmP%2F%2FhgGroj6U4W4igew9jDWio29BjqkASFAhkEPNQBfU6eZdFYC2D2qKzAAlH6XrLEhdsSpvKJloO%2BSwwFAwBy9KQrd9qBr63g4ByNH7KXyKGJTsggytu74nIrcgCLLmA2qPv5Ut%2B2mWR%2FBdXGY6B8J5%2BY1hjHfcTrxR3Fmg90do%2B2VLS%2Bf6lTQkk1xbPvns0B%2F5im8rnT3Nwqjt31yIJ5gpaIoJo20oFBgHykovIkNsMVYAUdqM4b6qfin&X-Amz-Signature=1567dab0fd0dd5a4da594031ce41364bcbff5dcc30b1f7307ed4eefcd7a8dbc0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2ZV2HBW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIESi%2Bv%2Fdkkppnb4H4NWcpV65akdmhTNCZrpRXOzdiGOfAiAHgkMAyC4o2hq0HyCDHzh%2FNml3nbeon4w7WInIXTGLzyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM31g3BOzyYrh4LJGdKtwDXz0T%2BJC3K8w0vsoAI5%2FXg6msLklAGTHvsiGtHjpWMno0kyDJuCquT1rog4Mv0a4bnoXdt4ZVM9KeALBmS4J1cl%2BipFgPPqLyKJ1LDZ0%2BN4jYsiw3%2Bav%2F%2FKN%2BKLPV4caP%2F%2B%2F6U7FTuo8pF46Ou1hPCzFxUw1%2BdOHHbbIoLwbYQi%2Butn38jECSuVu8TLW98fkV%2BJYd5hbnV%2BQevC1RF%2BPP8sTrDHfttmKJFuKctBz4xq0Y1qA5FyDI5mF8%2Fr3mqvr1QaBdQnIF20HzljWJajVCnEFxX0bVU3Z6hWw5QA3l9fC9a07O2f%2FImhjA79%2FhipF%2Fp7DJ4OjvhgwlkuIsdcZjtXYq8tt%2FO6VuMp0fPj9nbuef51A3w%2FHgklFefq62NgdThwY2U5whCbU0bdr5AYTyybXghm8SjN8zTv9cmzg65BtqADSx8ZbRn%2BhHnySohG23drXMh5s3YAFSZDYt9oDzqs8Q2tOcbPh3lwSky4Cq6CPvFxTO%2F3Jml6X7C%2FSxfTUe8S2z0BWditlzW1vMHy2kWJDimB6Mhm5ODYZgA6N2KNAOrIEQ7Dl4SguvkiBqBnwM4K4ubXFLO%2Fkgx0l%2B%2B6U%2FLrdrc7EdfMO9FHgLdg0XbEAeuR4vPbS1M5TtG5Uw04qNvQY6pgFbpHnDXkadahkDkJTMR0rKhw%2F5GaCCJ8egRZbhCrToYtlIiIb3fAvQLgm%2BaPsq%2BZvAjevCc%2FFVGfkEOAO83XB%2BkR7c2QPWgwngdSBA%2F%2B7PciEyFojHco6LeC4L%2BdHWQ8k5c3dFWIGBPK%2BKKUA7dh6G8mcXD5WQYN97NSWqdEhq%2Fg2NdWM5Ra7cKOBCyor17YE9qW4Yo4VEzQKnhSs%2FGMRRNy7RQPX2&X-Amz-Signature=e74ad81fdff5265327a67514e7d63190864d891beb0c290102a3b236a2e858ce&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2ZV2HBW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIESi%2Bv%2Fdkkppnb4H4NWcpV65akdmhTNCZrpRXOzdiGOfAiAHgkMAyC4o2hq0HyCDHzh%2FNml3nbeon4w7WInIXTGLzyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM31g3BOzyYrh4LJGdKtwDXz0T%2BJC3K8w0vsoAI5%2FXg6msLklAGTHvsiGtHjpWMno0kyDJuCquT1rog4Mv0a4bnoXdt4ZVM9KeALBmS4J1cl%2BipFgPPqLyKJ1LDZ0%2BN4jYsiw3%2Bav%2F%2FKN%2BKLPV4caP%2F%2B%2F6U7FTuo8pF46Ou1hPCzFxUw1%2BdOHHbbIoLwbYQi%2Butn38jECSuVu8TLW98fkV%2BJYd5hbnV%2BQevC1RF%2BPP8sTrDHfttmKJFuKctBz4xq0Y1qA5FyDI5mF8%2Fr3mqvr1QaBdQnIF20HzljWJajVCnEFxX0bVU3Z6hWw5QA3l9fC9a07O2f%2FImhjA79%2FhipF%2Fp7DJ4OjvhgwlkuIsdcZjtXYq8tt%2FO6VuMp0fPj9nbuef51A3w%2FHgklFefq62NgdThwY2U5whCbU0bdr5AYTyybXghm8SjN8zTv9cmzg65BtqADSx8ZbRn%2BhHnySohG23drXMh5s3YAFSZDYt9oDzqs8Q2tOcbPh3lwSky4Cq6CPvFxTO%2F3Jml6X7C%2FSxfTUe8S2z0BWditlzW1vMHy2kWJDimB6Mhm5ODYZgA6N2KNAOrIEQ7Dl4SguvkiBqBnwM4K4ubXFLO%2Fkgx0l%2B%2B6U%2FLrdrc7EdfMO9FHgLdg0XbEAeuR4vPbS1M5TtG5Uw04qNvQY6pgFbpHnDXkadahkDkJTMR0rKhw%2F5GaCCJ8egRZbhCrToYtlIiIb3fAvQLgm%2BaPsq%2BZvAjevCc%2FFVGfkEOAO83XB%2BkR7c2QPWgwngdSBA%2F%2B7PciEyFojHco6LeC4L%2BdHWQ8k5c3dFWIGBPK%2BKKUA7dh6G8mcXD5WQYN97NSWqdEhq%2Fg2NdWM5Ra7cKOBCyor17YE9qW4Yo4VEzQKnhSs%2FGMRRNy7RQPX2&X-Amz-Signature=d13a2366cc658bf9c7f51f624990779e994b9ef5ba271c544b81e79198468a17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYSVCLTL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIEPFR065UqJFyPSux%2FuWSn%2BVzWJYDTnqw7UBUMgcDKfEAiEA4DwFiecKk1ZeVmBRz1uMIbBFGdjYW9%2FOJ8SHmVn%2Bp0sq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDHaaBHkqd86zLE%2FX7SrcA41FB0%2BCvKcnKqlIHwwocqNp%2F5n%2BHiLfokKV%2F2Ws2WK0qNsJlNu7c%2BBXnDG9yHpAWG%2FlApGzzU1y3CgUT79WpeqWOiO8UvFQUs9X%2F2oV0qtHl%2FvzQal1IuTGVoNER9Scq8Vn4kOynssnVVotdltGP2%2BUO9OEMPdJslXfqnroN0hjQAdgEbGnfzkUd7jcTyJSQ5ugVT%2FN1DmkmvcDb1N%2BCJUGJidJ2TxOJy8pJfQwhi5aoE%2Bqe1H%2B8z5UE7dzZEABV1D6TtjV9qxjKdhWzzhm49bOgsANH6%2BauT7I8tWIBzrB4Nupv9LxVc9vZuc6McvMX3AEgY%2BOfpkerQVr260Ma6Sh7CMAxlFCpHkv6gz3rZp0%2B6L5AiljVpAfR7RSbAM%2FVU9BxnYWI6UWxstSZQFOnZC0kHswKI7YcN4Ela4brpPvOp265ospOpRHkeXmjMGkG3aJIqEacOTMzTfKe%2FkgJZlq3%2FMusjUHTcwX656deLYILmg1seT1MayYzD9xIhAlU%2F8NOl%2FqOA8i02KUXUFjQkv2yCb%2Fci3rI7tC9PSKb30h9dtBaBvIzVBZQM5%2BL3azor6afGYMp155rH8Z11VxFrvDWX%2BCcDX0ks%2F4vjPkkdz3iAasxFRhCTFCin4%2FMN%2BKjb0GOqUBKLr7%2FP7%2BF%2F%2Bwec0pUrem%2Bz4rkyEmzN2V%2BY93fjUKHN%2FJWaU53DAY0XCxFcF4fkASxwereTwAKf5iLxqoPqbPQv%2B48hAK%2FeZKYK3DroN32F9mz3ijRDNObYEEwOib4GPuDUzM7bnp4A7qoat%2BY7zTVCOtqdbYgjJ1fq1CzfNm7utparzAdS6aAhvkHlqmvDj0140lM83RdJu2owGlnswFCgIEsVVj&X-Amz-Signature=d103dfffd5036ac56beadc0f144458f5545a81e3243541e4df0834b6c6ad46a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=12153b28dc9936356cda0db81901bdf1be7da4299a3107d7c2c5049dc88d3e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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