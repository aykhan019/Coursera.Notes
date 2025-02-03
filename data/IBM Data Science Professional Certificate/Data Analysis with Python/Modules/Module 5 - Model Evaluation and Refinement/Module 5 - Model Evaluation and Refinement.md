

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=e7f94951dc849a9525bb4458810f23007ed410da44b504de9cf7d98181240509&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=3dbcb95c2929fc3e6c211825917dff6a6c2ac0cf9ea8a39c225cc28e7e95c456&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=95135ce0263bb4d7b8bfcaca31d4bbcc7de8775f791eadeb47552ecba7c05119&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=f19e0c4ae29c29d8850b5deafff8f6e4e8d9258f82e645816bde3a638e7a80a4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=8024041c670c22754697d5ccf3f9e314a1480d78325b37e3a6ec7a0370a10369&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=7082caaf5b9b9ff5356e065f1bd7ae68c860943c031ace23c90ac73ab03ff063&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=508da43edfcd295607ed4db60ee5049ca27ebd50fae51d78221461353d9b9894&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=795e066e9bf3368168c3a3ad57f2281878333a075cf9a2cb003909bd5d6645ec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=d98335c3132df45934d3ef146473d1d162c3304dc13570eccf3e145d6d046b03&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRX2MVN5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXZIORmyiD91LThhrWlNV0L5%2FB2IYGUKILBFWZr%2Fm6AAIgB7X9wUAmqxVargq8RlGKSMFP4bm8X1B7A8Oa4WVMe8QqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKCKK8hya1wcK7PCCrcA%2BIHnU8za26egKD%2F8hteJQPIjFhtXSvwm4giq26rHXI7to%2FL4EsW1U76Z%2FAS1ARzwdpyJCQ71FI5Ay9mrei6lEDB2wslQiwssq%2Bb0UHNpD5tbdG8ijgo5U0JEFj9zM4TUstvtsp8sNY39333w71QHH%2BmN%2Ffddo%2BbAgpgnTosC8wVNmFsjEE2w%2FNWsu8Ek8CVYHDyEOBNrsphrJtUoM1QsG5cYpN%2FTuJKr%2BrsT5NbM6mqaSrDeY6MBeC%2BAO%2BVAi3quarg%2F7Jaw45FTS0RTPFVVVv4c7PAb3T3rtUBbJDxe6F7hazBmfm7FsgMooo5R480jsGeE1qMuVHpg7S3%2FyBgMB3DB%2BXqB8fPQ%2FarUnpeVMso5TMwdoIgxk9qQIAjuAk91uJJEETDwjblqMgzzpPR3Eh1iwG8kBXEgTNf4phY6FdPrvHhthbtHkPCXdSQsw83ZMh82cKFMVaF%2FfpYwcLi6sFcK2oeUqHwbehYcMsOVw57nRcQqD8mr8pFaMxJude7WnCdLwrfBTBh00kg24uk16AuaBzcZa3nwUhiEjno6WxhtBt9LQkMI1rQPlP9AylD%2B9LEI%2F67ctA6lbON4uvW%2BXMCJJRaTbR%2FVCrLud0jm4CPy5lyOEIttLF1pxnIMMrk%2F7wGOqUBTgNVTpKWfEaGeNrMfev0RuuaSARoLtjKmvIUuid%2F2tHnBEyWWDw2wI2vGLx6MDlyJHfzQfHI5ZqDZCnVz6%2F7UDA648CWmpkMt2BUT%2FkLIQrOyJ72lM%2BI2nwxvMjmV9gEa4Lli31JV%2F42VMg39TJovL03ln5jbFF3SbzJrf5n5G89WRThMM8W9GOjDzhkvTuBr7bIM2e9wQp7kTg447s70tKJKiHf&X-Amz-Signature=65eb2baa2e681ef5592c4d9c7237db4de001a5cb82a570b08512145b71070b57&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRX2MVN5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXZIORmyiD91LThhrWlNV0L5%2FB2IYGUKILBFWZr%2Fm6AAIgB7X9wUAmqxVargq8RlGKSMFP4bm8X1B7A8Oa4WVMe8QqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKCKK8hya1wcK7PCCrcA%2BIHnU8za26egKD%2F8hteJQPIjFhtXSvwm4giq26rHXI7to%2FL4EsW1U76Z%2FAS1ARzwdpyJCQ71FI5Ay9mrei6lEDB2wslQiwssq%2Bb0UHNpD5tbdG8ijgo5U0JEFj9zM4TUstvtsp8sNY39333w71QHH%2BmN%2Ffddo%2BbAgpgnTosC8wVNmFsjEE2w%2FNWsu8Ek8CVYHDyEOBNrsphrJtUoM1QsG5cYpN%2FTuJKr%2BrsT5NbM6mqaSrDeY6MBeC%2BAO%2BVAi3quarg%2F7Jaw45FTS0RTPFVVVv4c7PAb3T3rtUBbJDxe6F7hazBmfm7FsgMooo5R480jsGeE1qMuVHpg7S3%2FyBgMB3DB%2BXqB8fPQ%2FarUnpeVMso5TMwdoIgxk9qQIAjuAk91uJJEETDwjblqMgzzpPR3Eh1iwG8kBXEgTNf4phY6FdPrvHhthbtHkPCXdSQsw83ZMh82cKFMVaF%2FfpYwcLi6sFcK2oeUqHwbehYcMsOVw57nRcQqD8mr8pFaMxJude7WnCdLwrfBTBh00kg24uk16AuaBzcZa3nwUhiEjno6WxhtBt9LQkMI1rQPlP9AylD%2B9LEI%2F67ctA6lbON4uvW%2BXMCJJRaTbR%2FVCrLud0jm4CPy5lyOEIttLF1pxnIMMrk%2F7wGOqUBTgNVTpKWfEaGeNrMfev0RuuaSARoLtjKmvIUuid%2F2tHnBEyWWDw2wI2vGLx6MDlyJHfzQfHI5ZqDZCnVz6%2F7UDA648CWmpkMt2BUT%2FkLIQrOyJ72lM%2BI2nwxvMjmV9gEa4Lli31JV%2F42VMg39TJovL03ln5jbFF3SbzJrf5n5G89WRThMM8W9GOjDzhkvTuBr7bIM2e9wQp7kTg447s70tKJKiHf&X-Amz-Signature=d45b5e28c3cfde08d8c7cc90dd8128df72fc9922c86fbd3e6dfcfd2ccff39d86&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRX2MVN5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXZIORmyiD91LThhrWlNV0L5%2FB2IYGUKILBFWZr%2Fm6AAIgB7X9wUAmqxVargq8RlGKSMFP4bm8X1B7A8Oa4WVMe8QqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKCKK8hya1wcK7PCCrcA%2BIHnU8za26egKD%2F8hteJQPIjFhtXSvwm4giq26rHXI7to%2FL4EsW1U76Z%2FAS1ARzwdpyJCQ71FI5Ay9mrei6lEDB2wslQiwssq%2Bb0UHNpD5tbdG8ijgo5U0JEFj9zM4TUstvtsp8sNY39333w71QHH%2BmN%2Ffddo%2BbAgpgnTosC8wVNmFsjEE2w%2FNWsu8Ek8CVYHDyEOBNrsphrJtUoM1QsG5cYpN%2FTuJKr%2BrsT5NbM6mqaSrDeY6MBeC%2BAO%2BVAi3quarg%2F7Jaw45FTS0RTPFVVVv4c7PAb3T3rtUBbJDxe6F7hazBmfm7FsgMooo5R480jsGeE1qMuVHpg7S3%2FyBgMB3DB%2BXqB8fPQ%2FarUnpeVMso5TMwdoIgxk9qQIAjuAk91uJJEETDwjblqMgzzpPR3Eh1iwG8kBXEgTNf4phY6FdPrvHhthbtHkPCXdSQsw83ZMh82cKFMVaF%2FfpYwcLi6sFcK2oeUqHwbehYcMsOVw57nRcQqD8mr8pFaMxJude7WnCdLwrfBTBh00kg24uk16AuaBzcZa3nwUhiEjno6WxhtBt9LQkMI1rQPlP9AylD%2B9LEI%2F67ctA6lbON4uvW%2BXMCJJRaTbR%2FVCrLud0jm4CPy5lyOEIttLF1pxnIMMrk%2F7wGOqUBTgNVTpKWfEaGeNrMfev0RuuaSARoLtjKmvIUuid%2F2tHnBEyWWDw2wI2vGLx6MDlyJHfzQfHI5ZqDZCnVz6%2F7UDA648CWmpkMt2BUT%2FkLIQrOyJ72lM%2BI2nwxvMjmV9gEa4Lli31JV%2F42VMg39TJovL03ln5jbFF3SbzJrf5n5G89WRThMM8W9GOjDzhkvTuBr7bIM2e9wQp7kTg447s70tKJKiHf&X-Amz-Signature=61aef505c846da4f3350b53fcb7ad1bfaece8c08607736ce70df7a993ed1b73c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=bc753e129e84d9f75a4f6581ce4fbfe21695a408af5386cc7048ce05a8bf2341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=062c4ecc16cc6f6342db0a687b78cd996c03531be56d6602ccb8a98ad7c657d6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=2afc900d77d3239b01da796dddbcc7a14ec2a7eb45902590b59dba5a824ea0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=a1ac40610b963f4618cb352c2ec65448b33da672a2b54071d8abe676cd19a5c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=8cc38e4fb47a0dead06d3a5f647496f2a1273fb7739383dd7d6f166cc209358a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECQO4MO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG4kWkEvhngtJgLjIlBN7AWFZWuQmcna9MJ3xq0xeef0AiEAx%2BWhO37ee%2F%2BQ4MJaWryY4I9Lfb5%2F%2FrTzVdS4sV0eYucqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHlaUd4E8mHMrszdyrcA2IeBKRLmq6GOXhYgfRUmjCsqb2iJ%2BbCCAoLnVz6X8KyEtWY1%2B04pRcr51z7oKHopoEaoS4%2FFKpMgvR35p9WzjUyg0lAJo1cTs4O6BBtG0%2Bvr8nFQa8j9V8oBHVGp4gNgzjwrt0geFwDCBEQBmbHoSeC0lJDBNsgxcvyiu42an8xH2yS5dnxcf1CF1grIECV37ww0sizalvJXRAZJYoXiFgKGp%2FX3yZwCkmio63RK2qh2oyETRzHDuVWOBtZYOm3YH7CSKCbEkY%2FzObRxQbgXfgXcCpiZC0ngDU4PIaz%2BGv54PwwjbKot4vrnA0onL7RDIPxjreXGRPKgz1%2F1yU5S2%2FTUnk2sDhumnBzuxEfonaULaO9WJ9NFMbV3IOrECA6zS5SZiW38Q00CkSj8T8mQFP83kzsGEWMeB0HzNjaRzH5k6zAzcc2ZifF9OwSuSt9Qo1BmB0pIIhZa1t11hdUohYsNY2W8yephpynbxl9UXALz7T5clQpcGNf5U%2FdTDTFZPQMIv9AedUuprWJx5LJIOXdsubv%2FNHunMQEiXVRAgsS0anMup3wglhP07p%2Fyj1USZt8T7LHqo5VHq5LOGymG%2FOZjcx5ZaAeXnFx04ermRur01VUsX81ca8v9b5YMObk%2F7wGOqUB0sAd9QnoKnxEwsr8EtYTVLnH7nEG%2BYwXVj48vK1pGPfzsT%2FJeg5xUcNd6BQDPylrzNng1r6adhx0Gfv7rIypnr29aTBwmePQbGBmidNxqCgzwyR%2Be5myS0tllNcka%2B0abNwK4s9VpH9udaX%2F9dtDkLTx4Ek7TpDjdjAxmpU0MhZwVQKElkLqH80NKq8yl6vfOqlo7HjxGT2txHkVjt%2ByQ3018LaQ&X-Amz-Signature=40a622d9029d4fc548ca448fe2c294299091ee32b9390c8ce4bc060ddda94e6a&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBMYETDZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFypy2Mi6E%2FiMgc7mgYEHFau0B7HZpyhxElnvn5JPnSxAiEAlwc5%2FBdImC0pqlTkZHSSo%2FDSw33jCzTJFaGL642VI8oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA03DGKLQ1KSiNGZPyrcA7ti5FRvtwz1w0hktXGMDnPB6AFZijJdIf%2FvO%2Bw7LmPwP709ixrKQQT9B496EbNVFXSMOlDuVdcE%2BA6vJOY5MQPezezkmeCcvmA1FPlMyA6XF6hjJc2MGfTlK0k3gkqUHNmirZ99%2Bji1DOt%2BXzubGZjjcLtz1JUzKmAsiP8zb5AQpWyhI5A3XoDrQ7sImSoSapxqz8CsbLW7Yx6Jb6GOhJJHZEA%2FROmrON0YxkatkxyvR17%2BbK5Ip6fjXoDvJnsr0pPUgUVy1DwG5RjrdD7vr8L%2F7uA%2F%2FnMAe5lcN%2Fvlwom0gl183Lkrupt5W0YdUc2QpAz3fh9YnSWQqq8OM3d9%2Fc%2BfJjwnZgvCqUSw%2FZHKrBLFEvMf9t3yB1DGdLZ6WgoNKXc3tG%2FUyTVHqL06ia7rN9Hudzme8F1ZiVlnrFe2c5drMlT%2F19HBPK%2FdTnUkf0z5JoycNhsqs6z2oXLsM3I5BG%2B5l6i5NhjYqUrqYKrl5%2BRlee62d5Dq4DPLgWY3GoQXrXNyWVcGCJe4vPk%2FBY%2B9Y9cD7OJqBKPdpwSqQ%2BmlCD%2BldU9A1qqxOBZ%2F8y4c2MpSTLFAqZvkDK4LOXdFCQTXEwIBzN%2Fh8YCrM1WGDKjflPEfkh31VlX4Efdt226cMI7l%2F7wGOqUB7vW7yXVv3G34QB21SNk4eoRZEGjQIIL6mFEAbZcpaXEGrdTWDRf3qAofCIIHloEiVXDxQ93pU2%2FTfBH%2BQ2S6zn3Jb%2BIFeWH97vgNsmV45o%2Bh3OQCYjnCDxjJzSAOTwTDIiY9MPtsZxMXV%2B%2BFd0pqUDGTkOV%2F2ShzAgxXa2QKu2UV3Lox0%2FMYyyZcXCUlLXbj4PI5KuTG9f8tPWCzuBWkv7jASnhB&X-Amz-Signature=33a8fed57e7ee68d4ce9f79237b1358fca39f8c218f1c484d3b044ed536f3c1a&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBMYETDZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFypy2Mi6E%2FiMgc7mgYEHFau0B7HZpyhxElnvn5JPnSxAiEAlwc5%2FBdImC0pqlTkZHSSo%2FDSw33jCzTJFaGL642VI8oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA03DGKLQ1KSiNGZPyrcA7ti5FRvtwz1w0hktXGMDnPB6AFZijJdIf%2FvO%2Bw7LmPwP709ixrKQQT9B496EbNVFXSMOlDuVdcE%2BA6vJOY5MQPezezkmeCcvmA1FPlMyA6XF6hjJc2MGfTlK0k3gkqUHNmirZ99%2Bji1DOt%2BXzubGZjjcLtz1JUzKmAsiP8zb5AQpWyhI5A3XoDrQ7sImSoSapxqz8CsbLW7Yx6Jb6GOhJJHZEA%2FROmrON0YxkatkxyvR17%2BbK5Ip6fjXoDvJnsr0pPUgUVy1DwG5RjrdD7vr8L%2F7uA%2F%2FnMAe5lcN%2Fvlwom0gl183Lkrupt5W0YdUc2QpAz3fh9YnSWQqq8OM3d9%2Fc%2BfJjwnZgvCqUSw%2FZHKrBLFEvMf9t3yB1DGdLZ6WgoNKXc3tG%2FUyTVHqL06ia7rN9Hudzme8F1ZiVlnrFe2c5drMlT%2F19HBPK%2FdTnUkf0z5JoycNhsqs6z2oXLsM3I5BG%2B5l6i5NhjYqUrqYKrl5%2BRlee62d5Dq4DPLgWY3GoQXrXNyWVcGCJe4vPk%2FBY%2B9Y9cD7OJqBKPdpwSqQ%2BmlCD%2BldU9A1qqxOBZ%2F8y4c2MpSTLFAqZvkDK4LOXdFCQTXEwIBzN%2Fh8YCrM1WGDKjflPEfkh31VlX4Efdt226cMI7l%2F7wGOqUB7vW7yXVv3G34QB21SNk4eoRZEGjQIIL6mFEAbZcpaXEGrdTWDRf3qAofCIIHloEiVXDxQ93pU2%2FTfBH%2BQ2S6zn3Jb%2BIFeWH97vgNsmV45o%2Bh3OQCYjnCDxjJzSAOTwTDIiY9MPtsZxMXV%2B%2BFd0pqUDGTkOV%2F2ShzAgxXa2QKu2UV3Lox0%2FMYyyZcXCUlLXbj4PI5KuTG9f8tPWCzuBWkv7jASnhB&X-Amz-Signature=c70c85e2c23d5b8f90edc2e9f4c5c62b134e920e6705953f507215994b5c3a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDN5PLRP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIJbJ1XmmCymAFg9TtRhbt0Y%2B78%2Fnq%2BJL0wbGGgf4QgwIgZHFR5sJIikUBd8gTYCADVDgkOlx%2Bhqf%2Bv3LVXJ5owgQqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7XkNQ%2FegXqh9y9oCrcAxpLsK5vvjTzyytXv%2F24UiC%2BMs%2F2ASUPWpsPMMP%2BTObweZmw2oTVQXClw5UpwMeo5zYKYE8hkeuFizzjiYPsC64u6pbbCBsJhUcNJ8ju1JWkjr5MRgLCB1mTpHpTwVwmD%2FwSPaPv%2FHbJGR014wZk96R13TPYKZKM76qr6K87izyz9YKxTj83yBcXUz%2FoS5rz8cXCDVJhUzQCuUtcCTrlady1nf2GAx9Lbht2QqkTNVjH2WOODKnJsUC11v9BhwNeWVCZG2uSPL38N8uyqbTlFqKpeQLOORr8MGY4rQkdKHRNkMYO2pvBiGjlVIBZAuIRX5w%2FN2gJaHcU2emmK8GcG931sUfN3YdrWVuPcITCQiLBit3k4SXh8JRxi3wyVEAYACXfeb35XqyB8Q91e%2Bl9TFtHG50SuuC0aDUeLjmVlYc0XsUVUCtBrBL7Zrw5erodAHcL9PUv7xF5bZCgC2vMnLnmBb9JX7zbAvVXaoJ25YlupbuPJksXEJAgjb3%2Fd9WGOEpkUqli3bR2lYd4VzCZXD00DLpIxfQk1yZNyetryYiOM5oB2penEmj%2BuGJoJY3FreILlINqlomkKUVx8nyQVOCCzgt7VRTM6elnbIameymAdh6qGZIW7rhvw6caMMbl%2F7wGOqUB7nkdetPhs%2FX9Mn80qR1h%2F%2B%2BJ77ZwBDxglSKHjjtFltQB39Xvpl1JmoGtplcJopQAQmh7WXbfNZ07F8ZCRbLqjTH5vCCJwVZtY6yC5uZM%2BCJpkNVPkVIKEcoxtM82bm13cAh1PP9chr%2BrDHhnukSjQ9UWBddRc6JvR4qU1LoGQkxf9KElc80DzS9qUG%2BpogyB%2FpY0bccWXEWZ3hmCvLQITBmgKUmZ&X-Amz-Signature=a6c8a422d443909c87621d701912f73a53d723b488813ec87432544f071c7e71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GV6HBQH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHv5rsWKf8xxj7NRw2podRZFB7vlh53zsnLeyA4bkUuAiEA%2Fd2%2FPAsaSb7lae5O5tpUMLmcuHipJmAv%2F8mFXzh5Ry8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7ADFYry6UeqD8woSrcA252OCkh489rTtndUqumh3C5XqqeuTRcvfKNWdY71iMwNUPYxyj5XJjvIg1fc2IQnn5VJbXQGnEYwJYCaTmc5NDf52Dgen2R8U3JICBsqnMBEd4zA%2B1xI9oOUJUlEWcWTmuXnlQMUYQN%2B4ARIvpxF0Q25252cNlskST4unJfmC0BYlLHQvcuZ3esXTiv0wjEN5UlULK3WLZo5xNoUDO2SWeHOT2nU%2Fs3LYhNWAwaQc9LEp4yqsggKZOVESiKHRUnDfjPJFyUSH9T9LTuhWlRm4kMt6VfrrgMGz6w7kTe2liND9WQ4mxvYGqlsUGyToY6GAtrY7gtz3rrg1Qlfh4vPX0Qb5DfL%2FP0I6%2Bj4ziRfzmra9Y2lx881gMm0n33lC3gFvJ5ZGDuTLzqbJdb7TpIjSZnV1tdEhe%2FSuP51yIJSaazn3vGHx2RlH8wVH7GjRhBxjxRLrTq86T9GzRJZ8rmBP5NOyxVp1XY4d4UMw8aBeG0%2BMuMBikBRCcX%2B0Y%2FeKUAJcnF6WOk736h29TbbHQ27P8sRRAS%2FqHSYvKs1TjQ3fAqpKkezy69C5bIenzrJ46cmnSYT1lw3jbDfQA467V4eUBWgzo2RIi7y3iSR7xT%2F3DDgUq%2F4C6pBU0OtPxjMIfl%2F7wGOqUBM%2BbKV461sZNcqZ1s37FlI3Xwasd%2BJFN1h2ZPbigLgC7ySGFlymmwmKN7d0pIe7dZ3qR3%2BOR0QgUlwzs4hTqixoLuVFLBCgNPbXCEsdcAszTd0Vl1DLyBczyECDI8xEk1Tvo272FIMkG4AK0De2RxSlYRfmsYLWUno5FN7up6QjkGcIqfHIznMJvwiun3s%2FzyuyT%2FlvRm0eEB8ZHfR0uj0jf9aIOH&X-Amz-Signature=7a0a8034d3592db3f9e5589c416a3dd06e2c0d2abb5a3e412709de2fe8122231&X-Amz-SignedHeaders=host&x-id=GetObject)
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