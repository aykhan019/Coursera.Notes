

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=00def112351a4f0f6f144b3da6d76581c1a161cef1f570204fd0f95ca13f74a7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=a692ea1c5b1f702c85a3b0765e51035c80dfed23befd8685711f488b9e3188be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=06aab3246ce475605ab7f81601fb5277b80920f91ca5d434645f9399dbe5ac34&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=5e02c2a6d4f3a71a0998d5c5569e7e5cbc4ec3ed39ba2df1631fbb1c199b5653&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=ff498dd15d95ce6ca72724897804b9387e7b1354f28b9af637c92294514398de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=e170c1be037c10fdeeed55b6dc7f8379387998211715e71bcc52a0ab33d0db3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=f5ea6323e99b5a60b8bfe64ec7f5f219c13bcfbfd2ff44349408f64e3f02c1bb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=68c0206774c32bf021a1a0a9ed3c58cf1bf8ea45a3732c78bf19eca95f4be44c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=1e3147c11f6ea88d480711faa00888c7266f2229c1135e2aed56a6034e5db885&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=349e45659749ff138bbb8b6e845e4aeb3e3782d025d41694ec7fe6d34298e2c6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=9fcac549770e037bb18d19d7b72ccebb0d54f548338159b6f0a14283be94f566&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=8986005c8148a275c6789a6e7d91cfecc33e3521fed4278ff8949f05c4029309&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=f4a9cf4c1c001baa302cccf921e46ab1bbd6d766e2237adbd3ea09baa8c172f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=9b38bb5bbc46e5e33969a733a3b9342573cbf52212fd49ece5d90385d40cefa7&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=7b9301603e97cb7e9c23d449031ad415a83accc740232cc99f497a57ea4fa4c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=50450076d208f0f573e542f0dc9a60c006f6ad21842f54f100353399137d6660&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=54be6f21964c2e5184674163541aa71070de2d2484cbe87ca5ca202e1a4e94d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PE5GOG2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiatoVvjuIZbplwbK4jYZK1lbwGCagRou8fSlR1PTNmgIgav7z8uSW81QcUBRetTC6ujngFFmAUET72eO9%2FVONIyQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJiJL5qajRjW72C6ISrcA4YyI1FmoGTtRxuTu82kgs7Arg9uPnGBEYiuPNz0cbArM8V8qJ7fCyg%2BSR%2B9n1awfoQS3gfPjUU6rp1ZRP29skM2lbK709lXnXZhHv3C3Ld0GYh76huPyFt%2BOM0mOw3AQU%2F9QJJkwGSTV2i6WGR2qppZ9jJKapNcKnwaiCfeiGkS2X%2Fuek%2BzDgmXbWW6oD5xb3aaZtEhe4qBfJj3iaJTlm5gb0EeveKh0dq%2B%2FCF0fFkxNg1yBfYAuBZ45CxmEOwFYUqJB1M0kxBjn3vz1A%2FXzoZMq9g3wnPwamMTrmrnE1WRybBt2sC8HqAmee5UUylqyVMx9mZ%2BoZY5peE1u%2BapnVsPq5Yl3vJ%2B95fEOqDmEiIZco3kQkekgvPWws5tuCscdYe47C38ME8mYvzTmfwFiHID0EBW6BkxhIoaxmbeQtCOL%2FiBXaO2C7JuhlMYbiUAIcZZ3HOMugFOGZ6GD00SxNSFA9211mKdVS17EImRufYiSl6%2F1oPm%2BApLyxB8t0z%2BLtMjVmI33VpLeadFjid7w9wbBC8NBazKSPO2IxyELybL4mw1UOorFwilN7zUScNmEE7UQwNXup%2F40d0P0GCqyWgEQgyHOOXpId%2FLbttUZK1761BOu0PQ7xV0BSa0MODQ8LwGOqUBL38UMGoWWtWKRgvxDM5JJ3S03gWz3W29zHLLaLEqL7KdcfzUrwTJUJU04PLXWUxq%2FZq0h8IhsvVzwUJE5HXYPsQ6bJ4uuk%2BHV2%2FhFHB4cvXN4jI7MJMMoTyiXNzDLuzOleo6AhKAm%2FrMUTOCyQalUzUfruL5zuCVtwCu6gB%2B7Hlf2xBXkhsu3ITwIVbWeLjuh98eKOBN%2FxKTRdAityhtdsZdnGZE&X-Amz-Signature=4366dc49fac6a6986bb52784f8afbd1ebb1b1a62eb30d9036659186dc8781caf&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKK7N6C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh4TeYmVA364jzSfJ8K7HRZuD9x%2F9kA5efWCYE6zx1sQIhAN%2F1LenwoDhVlK9XH7c4t6Q8wHwWg1y59sqk7RBhWhIVKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUI1HXs1pzB0QOvPAq3AOo4ikQrEeI0EF2P%2Fxu1qjqK9%2Fh1PBZHl%2FJfQ3WtCo4yPLSRmjiJlHPqNOfKAkpUUzBdoh9eO2ReQpo6vrywwm1cci5kmY1J10jvk3JdaJhbZk0970C8IOAN5FLTFrVYHxkzLE004SuIclQDlTP0Fwcbur2QZC8SLFPPIEpMHl%2BQ%2BjWeNLAayBYMh3krxgGr%2BRzz3EKDKQK%2B38s2JrPi5PUElBVgc7AyAstJ1%2FUPDJtRFcNqm5yOsjXpOA0ww171r0ekNML19smDjjQDmCyCWV104GAEZu7AGhzqRClrZqpKN17%2BOKNoTjTAgyguwKXWrnTGQV2DpFjGYMqgT20gAX0fUh9zetPBhITvpo0Ju4PtYXpMwxr8ba1AGs1X5LZU7z8ISy0cfiBIq8tRPVFEP3HtD4KEb1EJVp7f530bXpP55ywFzsuRwvcyLfeeHbLSxt%2F%2BQ9%2BQunNtlN6MaQtsgWMMJ%2F%2FhpgcBZFUt4vyPszCwsbAju3d8fyuQSWUOrmJ5Bdveh%2Fm9b0f2gxKbGo%2F1aqqL%2BUc0V3PwrulZEXYgF%2BP7XSWRhYfxjSQ7hCEhOMxeLMZOyxU0k%2Bzkl4l4VdQpEB6crQQZDMl2BrWDJDNoMKc7nPSsocTABAzehEMqTCZ0PC8BjqkAfzMbuvFzCtUeG%2Bh7UmYic2%2Bwzu3DQawg3BsQSFEnUGEV2QEv9oRek5us%2B324zvxSaOvG%2Bbr2X01xhgBvRUxMDX5zoeJqulh2SoiDVsdUsR45PS61DLEsE7d7FhIb4c1In6vQK8okBB1hK5IMhY8MWWPBN1%2Bzlm1rACL8mWMfsqetPgUsFXW673gVbT4fbfhpiCR26uMiddFIReh50jPzGBEmgnC&X-Amz-Signature=c2deff1b7b2bcfa25281b21d80018d3c2266cb4e5526fe6763b6b9e3afd14215&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKK7N6C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh4TeYmVA364jzSfJ8K7HRZuD9x%2F9kA5efWCYE6zx1sQIhAN%2F1LenwoDhVlK9XH7c4t6Q8wHwWg1y59sqk7RBhWhIVKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUI1HXs1pzB0QOvPAq3AOo4ikQrEeI0EF2P%2Fxu1qjqK9%2Fh1PBZHl%2FJfQ3WtCo4yPLSRmjiJlHPqNOfKAkpUUzBdoh9eO2ReQpo6vrywwm1cci5kmY1J10jvk3JdaJhbZk0970C8IOAN5FLTFrVYHxkzLE004SuIclQDlTP0Fwcbur2QZC8SLFPPIEpMHl%2BQ%2BjWeNLAayBYMh3krxgGr%2BRzz3EKDKQK%2B38s2JrPi5PUElBVgc7AyAstJ1%2FUPDJtRFcNqm5yOsjXpOA0ww171r0ekNML19smDjjQDmCyCWV104GAEZu7AGhzqRClrZqpKN17%2BOKNoTjTAgyguwKXWrnTGQV2DpFjGYMqgT20gAX0fUh9zetPBhITvpo0Ju4PtYXpMwxr8ba1AGs1X5LZU7z8ISy0cfiBIq8tRPVFEP3HtD4KEb1EJVp7f530bXpP55ywFzsuRwvcyLfeeHbLSxt%2F%2BQ9%2BQunNtlN6MaQtsgWMMJ%2F%2FhpgcBZFUt4vyPszCwsbAju3d8fyuQSWUOrmJ5Bdveh%2Fm9b0f2gxKbGo%2F1aqqL%2BUc0V3PwrulZEXYgF%2BP7XSWRhYfxjSQ7hCEhOMxeLMZOyxU0k%2Bzkl4l4VdQpEB6crQQZDMl2BrWDJDNoMKc7nPSsocTABAzehEMqTCZ0PC8BjqkAfzMbuvFzCtUeG%2Bh7UmYic2%2Bwzu3DQawg3BsQSFEnUGEV2QEv9oRek5us%2B324zvxSaOvG%2Bbr2X01xhgBvRUxMDX5zoeJqulh2SoiDVsdUsR45PS61DLEsE7d7FhIb4c1In6vQK8okBB1hK5IMhY8MWWPBN1%2Bzlm1rACL8mWMfsqetPgUsFXW673gVbT4fbfhpiCR26uMiddFIReh50jPzGBEmgnC&X-Amz-Signature=861d7950900257d9e66e0580d99e6320c68d8a03ee9bab087feb79953130ef79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O6OL3KO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBz3loyweiKVUilfkp9mL8A%2BjK%2F5nytLJ3QpHAwnxoMgIhAIPr41xdW8HWf6g2nffitWxujYx7Gj5VQcf%2BbOMWv0rjKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVM5tQdi0V4dHPJEUq3AOq0Cag0ytgbT5y1E2tr0R1JjLSizzgXj5SJsepIHmr1cZaKhOPS1km0R6XNToWU6YVCB2jag4SAkD9blP3RsEUiqSwkkyWOsD01EvwfdChWGBUvu70tEQxHezaZvG9YlI9uclqVipihtC4ssvMPTod0UguiafstoR3Z0qY7Pxv8n2sAloJUoflkgytwP119dOw11KXzadeda%2B93p0DyRgmVTpFZR%2ByC6I5bDbu9EkTQRWjEbcbIr%2Fa8mmVfi2TEw%2FrTeClT%2FrfnAGA%2BQXtUwR2M9mTv4JpaJfzwdz5mJeukf%2FH0AEXhoovHVrioqvgp6N8jdtoOkkXQ6bJFHZEB8zq8KXbZQDW0aQHfiDOHb9U9DvWt7%2F3crx5VczCxLsJGHkWe6LzrIHfBzUJp9dkpJp2ppQWErgg%2BZjpwXHHz8U%2FKp9QPhCCaIH72RPPf5cFDLejZdIkGQo3Jupqs27EfwA4OBSJYV%2FvKmDVFct%2BxSkgj%2FSPrVxxReTEM%2BZYYmiGFYpR3CebrvRJSOZH8RER0egf4ShppBDEFnnQ0o%2FWvvt8D1FF3KsXoo7IRCkPh7cdPtA6mRKbcS4ghG5gVlGgFTZ8KXlaqoDZ3mvrP%2FCp3hAaHwmltZAzBnfQDx0ZgTCG0PC8BjqkAYD4hnlQPaEtLWy5%2Fc%2BDDyzL6pTAftWXmpBEmnG%2BkA7%2Fg32dZoX%2BQ48r4lV42mBCUMCZFWIGPG40qN1RgAo1tf6fcIkooY4Ha%2FfftbHiZREhzDoVXHuSWbM2Ht4cqUMChH%2B01Eq3bm6aN1DPEtvqfGX%2BGlR7Ra%2Ft8YFKcej%2Bi3REPDTRhZPkvPWnOH5JYUL5sqT5JKz2d1dNemha6aXK6mdt3fC0&X-Amz-Signature=5be65627dbb9f45c6877db620d84afe5c784f3249e57bc4339f2409fe16ae4ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=356d27985821410fa936900f2f59e293d7e84b99dbcfee46083a59a0274f7950&X-Amz-SignedHeaders=host&x-id=GetObject)
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