

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=29499e560dc0d63f19499bb44d1c95eae228a7ad19d9d8347aadd53d57e92546&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=9c3bc4a75d869dab158c9dc116766fa790e8a09a40448eae936461e736053349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=d59e19dfe173b3fd97068c5d7c20af8e2a76cf93c46532e0ac0cb412a2ab3bf0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=d3a581abcc2d58a431d11003e3cee63e6319fd8082deed1c2d3cb40651b6fca0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=201f2c781981ea6d4c29f318b63f06eea4e74e6edab198b31b28580747d7eeb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=026c307b68229620ccf34c907f1123fe5e2eec5e0fb9e1282f04771b856c45b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=824158243fc544b143db2ec04f07908c87490e84817a42dc477953ebb841b632&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=71dc110e1863e99947bff6f45566df0853ec3967c3d35311ce1608d225e13ae3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=51e76e1710eb7803a2e4e644998e3624d52b54cac5b6123c0c21cffee2b2797f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZPRCMSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFkGV9a6tqEeDBax%2FVcHG3BOLwZhu46UNe0%2BTp9h5IVtAiBx3ATRqP51j2%2FBGwmA8QhqD2a3ifVLAN4KlgHKyA9cRSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPv3FD9Q0g5RbFmyQKtwDXlf35zqFgET%2BItO6tkMY3bX9YdpgleoAmOOxA76kXBny6RFO1O%2BCDX88lBCdXtq1duXTU0V3pjEt%2BUBv%2FP2OI3%2FNRy2akyUrL0xqGTdSlb06YKG3QOmIn5wKDpN5KzQ3za5nXqAWYPFZgnEk7vx6eqwl9XlerTL%2BpD5ZA1P%2FYUO6nF6bOq4WOWx7R%2FOh8L1dK3iSRcga%2B1u85aF7Zcpq%2F6aJKYZ0L5%2Bnn0okFC0wV4THxfwB%2BcajPCyY9Dd7uNnMh1Co9X1kkdCoS7aL2uBOt2YYb3zAvDoh0%2FdTgxxnFbp09LqQIfeWITpWbroNZE0z3sVIsrhf0XMQdXrwQnFxUmIuQ4qOsDIBcSPNaGNOI3x105%2BTZ%2BphCT1Gn9bk8O4OG7yqExu%2B3XrbxhHac%2B9gJcjLlDvJzf5yOco1cZ5jaraW7xnBPnJhKdwUgSOdf4gtxEC%2BNUB%2FC1gfuTd0A6sCmlaTf5VljBDrZlBDwP11VHnyJm9kKlym0UdEYj9OVknwahN0xHFZyrc9FsSe4wqHXZw2Y6hI83sbzUzDfnGDJ6daHlYHzHRXYXGJSViL4KDtAA%2BhGt76GlG2K90afvIhPOHTjeagMdJAFwNn5INdQrbqXYLfykeywsAMdtIwzuH7vAY6pgHgyRq7ZfwW0g45JoFop7ZeDj%2BrQkIm5zCwQtlWLALKWuQ5oZM8x%2F6G0CgvJnpe1xFP%2BxgTBwoi1u3Z51tYSEzHKvffz1jwU3DU9mojs1Bz%2BH1pn3V7pb%2Bf%2BodETEe%2BlQMfebEifvq7nLNqnBUCcN4KweXjZLlwhmsO00FZ7ZO75oXm0qxacOctN24mzTZF%2B69q1RhXwVrfnP3MsWMg%2BB2%2FESH4UtTj&X-Amz-Signature=60ee89a8e27584d86685c22c715151b29c01673fe7a823e1c7fca365aae25500&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZPRCMSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFkGV9a6tqEeDBax%2FVcHG3BOLwZhu46UNe0%2BTp9h5IVtAiBx3ATRqP51j2%2FBGwmA8QhqD2a3ifVLAN4KlgHKyA9cRSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPv3FD9Q0g5RbFmyQKtwDXlf35zqFgET%2BItO6tkMY3bX9YdpgleoAmOOxA76kXBny6RFO1O%2BCDX88lBCdXtq1duXTU0V3pjEt%2BUBv%2FP2OI3%2FNRy2akyUrL0xqGTdSlb06YKG3QOmIn5wKDpN5KzQ3za5nXqAWYPFZgnEk7vx6eqwl9XlerTL%2BpD5ZA1P%2FYUO6nF6bOq4WOWx7R%2FOh8L1dK3iSRcga%2B1u85aF7Zcpq%2F6aJKYZ0L5%2Bnn0okFC0wV4THxfwB%2BcajPCyY9Dd7uNnMh1Co9X1kkdCoS7aL2uBOt2YYb3zAvDoh0%2FdTgxxnFbp09LqQIfeWITpWbroNZE0z3sVIsrhf0XMQdXrwQnFxUmIuQ4qOsDIBcSPNaGNOI3x105%2BTZ%2BphCT1Gn9bk8O4OG7yqExu%2B3XrbxhHac%2B9gJcjLlDvJzf5yOco1cZ5jaraW7xnBPnJhKdwUgSOdf4gtxEC%2BNUB%2FC1gfuTd0A6sCmlaTf5VljBDrZlBDwP11VHnyJm9kKlym0UdEYj9OVknwahN0xHFZyrc9FsSe4wqHXZw2Y6hI83sbzUzDfnGDJ6daHlYHzHRXYXGJSViL4KDtAA%2BhGt76GlG2K90afvIhPOHTjeagMdJAFwNn5INdQrbqXYLfykeywsAMdtIwzuH7vAY6pgHgyRq7ZfwW0g45JoFop7ZeDj%2BrQkIm5zCwQtlWLALKWuQ5oZM8x%2F6G0CgvJnpe1xFP%2BxgTBwoi1u3Z51tYSEzHKvffz1jwU3DU9mojs1Bz%2BH1pn3V7pb%2Bf%2BodETEe%2BlQMfebEifvq7nLNqnBUCcN4KweXjZLlwhmsO00FZ7ZO75oXm0qxacOctN24mzTZF%2B69q1RhXwVrfnP3MsWMg%2BB2%2FESH4UtTj&X-Amz-Signature=427d8c22a851f2a485f09757f4028b1f0e894ea2f0abc583eef8c60006b74b7c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZPRCMSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFkGV9a6tqEeDBax%2FVcHG3BOLwZhu46UNe0%2BTp9h5IVtAiBx3ATRqP51j2%2FBGwmA8QhqD2a3ifVLAN4KlgHKyA9cRSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPv3FD9Q0g5RbFmyQKtwDXlf35zqFgET%2BItO6tkMY3bX9YdpgleoAmOOxA76kXBny6RFO1O%2BCDX88lBCdXtq1duXTU0V3pjEt%2BUBv%2FP2OI3%2FNRy2akyUrL0xqGTdSlb06YKG3QOmIn5wKDpN5KzQ3za5nXqAWYPFZgnEk7vx6eqwl9XlerTL%2BpD5ZA1P%2FYUO6nF6bOq4WOWx7R%2FOh8L1dK3iSRcga%2B1u85aF7Zcpq%2F6aJKYZ0L5%2Bnn0okFC0wV4THxfwB%2BcajPCyY9Dd7uNnMh1Co9X1kkdCoS7aL2uBOt2YYb3zAvDoh0%2FdTgxxnFbp09LqQIfeWITpWbroNZE0z3sVIsrhf0XMQdXrwQnFxUmIuQ4qOsDIBcSPNaGNOI3x105%2BTZ%2BphCT1Gn9bk8O4OG7yqExu%2B3XrbxhHac%2B9gJcjLlDvJzf5yOco1cZ5jaraW7xnBPnJhKdwUgSOdf4gtxEC%2BNUB%2FC1gfuTd0A6sCmlaTf5VljBDrZlBDwP11VHnyJm9kKlym0UdEYj9OVknwahN0xHFZyrc9FsSe4wqHXZw2Y6hI83sbzUzDfnGDJ6daHlYHzHRXYXGJSViL4KDtAA%2BhGt76GlG2K90afvIhPOHTjeagMdJAFwNn5INdQrbqXYLfykeywsAMdtIwzuH7vAY6pgHgyRq7ZfwW0g45JoFop7ZeDj%2BrQkIm5zCwQtlWLALKWuQ5oZM8x%2F6G0CgvJnpe1xFP%2BxgTBwoi1u3Z51tYSEzHKvffz1jwU3DU9mojs1Bz%2BH1pn3V7pb%2Bf%2BodETEe%2BlQMfebEifvq7nLNqnBUCcN4KweXjZLlwhmsO00FZ7ZO75oXm0qxacOctN24mzTZF%2B69q1RhXwVrfnP3MsWMg%2BB2%2FESH4UtTj&X-Amz-Signature=62adc52ae359e59326f9449ae2fc30b6799e7be39e76d46093c287652834d541&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=6b0ad8e0060dbd6923107a44b74a9f6993ba19bfcfbee9569ef635530f0007a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=4039a92880222cb4926427c99432227c2d56e5fb9829b6c5c5b41dda033ce9c7&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=05038546b9c9d2c59872db7965d5611840b01489bfbe3f14d30a90a73ae7511e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=e315de8c7adf8f008bfe9d24d1b287b159b39bad6473d37008d158213502fdd2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=e788db64ca7546a9e636fd67f844618cf744aa07c5af2ace610517e66b3855a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH2GTYKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwTXTnzFvpmOzoL7vi4YKomiJ3Xbwisl%2BH%2FS3Df4jM0AIgIfQ3QwZqq5kytutY0EUO5vllvpJCwVR5DBLAntkZihsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERB7Z5e4AslRsKC6CrcA%2FwUu15%2BFVW8%2BrCQn1IdWjvyHDNUNMD6erEoWTKUrtQd2Pw10aWBOwptnTgM43CdNIkIA4NZOua4uRw5f0zBa%2Fu0Cp9qijd%2BieJP4Dsjk9WTtfB00juOlFDVFip2ufoOWD7i01MxqaB3N8Yv9Z%2BobUqnxX7s465hLX88yPPNreo7C1lzWYUs8F7RQ%2F4HmAambBBGShQgj6BECqru1fAdxuQpH%2Bi%2FChqd7twy9x6AuyusgfkmLCc3Jfql3ZO4ns64FNhgs8p%2FfWCSTedjTN968KMU24PztUeGeIdpr5nUixkEY3M9tuj3ecZcscNHkAcZGWzpIWojSQ%2BOBuGoBGkz3p1PBFGpQsHiF6b%2BsqwfMO0sqyk7z4rTIpstGj7bY8A%2BcfbUtDcFk7M75PqVIZTSY2xTYa2llObT9iQG8YfsFJJgLbum23kDtWPabhm2VtQEE22n3d%2FbP2jGCnZz2p2PDfKMupEeCij7%2BLNHfYYnlj6VK7RLw%2B7FRKZDD95fX0doEGpr4idEyfRCKaXC65YDloZW9XT6swWUPcMG43NR5GnFp6%2Fmi%2BrtTheuw%2Bz4kd7ebVqPcE1fyEyaTOoViz0QdmGu408A2zBgMug0GM8qoLIbKqq%2FIZdIsziA2qLqMLbh%2B7wGOqUBdrehGt7YcnRjNQ8G5ewB%2FrweRQ%2BgzkSz5JG8hile0dsHSvFoIMPIbpADkFoi8VzMrFnEiRpr5b6OctXdaen3pyMSorR3MZfpWwY%2F03B2t06HPscHh4Nb8%2BUw5zOKX21E8WTFy8GV494IqkLGF96LgwSuCBd1C4RCRdJdyNi4zgBtp1prHLXqLMMSfdkhMrgiMYbJx4GyQPP9M8RFagwnOtoOOXEP&X-Amz-Signature=1569d04063bb167f50de9f82b9d0ea1a20cd7fe57e0c4c741d1a13a394344509&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QB55M5O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAEkHo8MxPCgJmBtc%2B70Z0jTtjOvWTLfcRGgHYayMo1AIhAPfDsIFU%2BtrLbxWKutQZNgOb04dRvRydJ%2B8Hy%2Bt1YcBAKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywGeQjKyDT5%2BkX%2Bl0q3AOSYI%2FLwals3ne793K45n%2FRRTsXXlpAJJFka0exrluOmm9QTL8ys7jS4cKXzG8jrqdMDYenE3Mb6nbuf0rVHsZNgWjI6tdlUkcx1JWdTKTP5aVvWScdwXTtUfdRZCjoJi5bt1aUA385DO6mT6P3ntHajXRuBB93A10vZ0GdV0pvNaA%2FG9c6iTrU84I1OZQV4ek8FoqCnDr7BS41PPgQWusUN5tulRUgq3woWhyS2FFF5eQRXcm%2B6Vs8a%2FTtsSJm6tiCzfXU0EczBX8Yw%2FgGcLJe9CgtJMuOfvJMOoXbRSEjVlKapQMws0dt9wbzp4OHr3hSeixCKhMFi5uz7nuy8m4JJTuN%2FoujeQ8NZUX6rChXIt%2FHqMcoYMK2yCbqKztYvVHdm0z%2FblR1yr2w0brgX0s02xlh1Gno%2BL5lNtuYKvn540nP%2BuPfZHqXhcC2wtgpYn6Okum94n39bigWU%2FpeswfwHtIXwlm6WNXlo2SSq78fArUVsRrbipTTe%2ByL7nyqFcu29NY9W67XMINXHywOFDYNOfrv6pihJsWbtaqA4PlFBY3BijIkFLf9ZMXirS3uzCnYiX36GG3dfjxUnknEcoZObbXnz2QdFVan%2BEB4dYv6zSL5wPJ3WfUQNmARfTDh4fu8BjqkAW3XHIljBJlfOVCwGw89ZEfK3ZCUF99IiTNi9aTHg0qiec9%2BjIFtMW%2BQ3WKPVCdC2C4KODRE5cgcq5ndigE3lViKw9sQyw9fEfRZ7jz5ubVWpJANxDq1ma%2BxMSKdrpVuTuYW4sqxBcA03J%2BNnSpdyFDtFENWIxY3tZtJJqEJy%2BXnNVV4IkHpB%2BCdpEJU%2F2zHvbhwLmFGV8xJoO1YgmJiuDem0c1h&X-Amz-Signature=1b24b2ee4afc57375e1f1ea42ab488ee9944cfcea311850934edf110bbb89de1&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QB55M5O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAEkHo8MxPCgJmBtc%2B70Z0jTtjOvWTLfcRGgHYayMo1AIhAPfDsIFU%2BtrLbxWKutQZNgOb04dRvRydJ%2B8Hy%2Bt1YcBAKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywGeQjKyDT5%2BkX%2Bl0q3AOSYI%2FLwals3ne793K45n%2FRRTsXXlpAJJFka0exrluOmm9QTL8ys7jS4cKXzG8jrqdMDYenE3Mb6nbuf0rVHsZNgWjI6tdlUkcx1JWdTKTP5aVvWScdwXTtUfdRZCjoJi5bt1aUA385DO6mT6P3ntHajXRuBB93A10vZ0GdV0pvNaA%2FG9c6iTrU84I1OZQV4ek8FoqCnDr7BS41PPgQWusUN5tulRUgq3woWhyS2FFF5eQRXcm%2B6Vs8a%2FTtsSJm6tiCzfXU0EczBX8Yw%2FgGcLJe9CgtJMuOfvJMOoXbRSEjVlKapQMws0dt9wbzp4OHr3hSeixCKhMFi5uz7nuy8m4JJTuN%2FoujeQ8NZUX6rChXIt%2FHqMcoYMK2yCbqKztYvVHdm0z%2FblR1yr2w0brgX0s02xlh1Gno%2BL5lNtuYKvn540nP%2BuPfZHqXhcC2wtgpYn6Okum94n39bigWU%2FpeswfwHtIXwlm6WNXlo2SSq78fArUVsRrbipTTe%2ByL7nyqFcu29NY9W67XMINXHywOFDYNOfrv6pihJsWbtaqA4PlFBY3BijIkFLf9ZMXirS3uzCnYiX36GG3dfjxUnknEcoZObbXnz2QdFVan%2BEB4dYv6zSL5wPJ3WfUQNmARfTDh4fu8BjqkAW3XHIljBJlfOVCwGw89ZEfK3ZCUF99IiTNi9aTHg0qiec9%2BjIFtMW%2BQ3WKPVCdC2C4KODRE5cgcq5ndigE3lViKw9sQyw9fEfRZ7jz5ubVWpJANxDq1ma%2BxMSKdrpVuTuYW4sqxBcA03J%2BNnSpdyFDtFENWIxY3tZtJJqEJy%2BXnNVV4IkHpB%2BCdpEJU%2F2zHvbhwLmFGV8xJoO1YgmJiuDem0c1h&X-Amz-Signature=5c873aff60975853f286bbf7f463b6069f6c0e2a361fad27d76b0c5f1a54c899&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PK4LD3Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUMr67EGHzRlA4ROs794cKRj2Yu0A159ymV9pTira9HAiAm%2B2O5%2BGKu8F1JTTtdbbHaofXGz41bOQxXMD8G1vU6nCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZhrZzXVOVK0pwffNKtwDer5pTgkHUDHniaSDIUParvqi01JlHMtchjuOiBIhkY3OObAdAYmTcrEF2sRBOr9x1Hhy%2BKTTUVjE1IWf7%2B6wIql%2BUlFs7MGkNg0ZeM5kFgq7SxMiyvNnxJpkiZvtGJ4bmBi2my0qrT4NKXP6DQudfLzhLYaBCCiwMTKe1nn%2FYZA7u%2Bl4RJynODcbPeZ3qGQHNtKSK2NmXhl2xz8Z6lx%2BjXXcW93pad0cLi2bd16iPwzX%2B8p6g6cTe%2FKjT77LWFTbg3Nx0uAIwV6DP6MJygoFASMZGwCd0zdfEusN%2Bh0WWj0e4FAdHQcVn7ZFcshxkABsUGbLroBbyAOiElfqE52IqYHzXFZ8Z852ud2iORPsnf1GhXLpqlQh%2F7ElKZc1Dq0GzVXDScAAiIF2PbWLDSHhUs%2B%2Bw%2FkiMKT4EjlfhApLYHQXkQ%2BOC1ByD0hd7eS5Q%2BcQZytgvl8C%2FPdGedlfYSyKmRzjl4N3miZ%2BKOH8vpiq69LSfV4ZIt%2B7CXpSAT2uVdelcFgxVwpnCGHAZ%2BC7fJPgoKK9Fy9pE3Me%2FVQL%2Bc2YBQSILHZwrgZ9UBX756PHDGS91I%2B9vT3jIJoxcflq4IGHhPHkZq1CsASJv5Uqim2x9Z8izcmdY4Yv4bpCQHwwjeH7vAY6pgEN1ZC6%2FkmeOhyXLdbdgTzqewMOxomIxdeOFnPpo5BPsAF8ym6PuJqE3ITy33pUpSMUL%2BhuYvNNyJScshxj8GQ4WHFCnTzBKsNutdlgVRr4aDLV6H1Yq9iR%2FmAE%2BC2uAZtaob116wJeBM61xIbjyXeoTJ0AptwGZfn57V1miIMFOXOAtM%2Fh8y%2F%2BuG%2BxdGRYiKs0xRoU%2FSTFwNzHl%2Bruebc75VS9MI2j&X-Amz-Signature=8fce23046fbc78a1ab3e284a40001e7c2cb2c74eab75c54ad8ecda80db4ac8af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DJAJ6B4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAx2ZAMg3p98csYnYe5v63E%2BzMe7CciGQp7j5iIuLdBeAiAG2PQs4a45buibwXmGsilu4a4sNPGqO%2Fw1z9uM4hfChCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC%2BYFiHCfnbWO9vkiKtwDPPahTfSqgNgNBfMqFi4Gw9b3srASJQ5o55F6m%2FfeGgTP4qNZg%2B2MWcCG0mec3YWr67vXCZY5qWvlxpwpkcZdaNg1%2FqcBA4osQP6AihbN6%2BE9qNJJMdiD5B9%2B7ZNxYwo2ZJn%2Fs4klWX8jrnvsRica%2BJIFMmU0EL4EZXCQMeZ%2BiXo8kXKuF3Ufdm6aQITUWH0UTWPjkcpKPL3LKgGkquMJ2KkEPyCrS%2FMh4hOI%2FK9DJcFXkwxmanFt%2F9wJdAJFcDsj9Ol3dNsxTOQxedOBcfP8nrqHQM38%2FgQ2xJqB9QjweG2hBi%2Frnxs4%2F%2FgyV8PSWLrFMAaP%2FCwkSiJ3SQc%2FEySfN4KbKTV9IoPMIHbQbyjkf0P4I3paHLzKDlCgJ4Otz7ecO%2F5T%2BcabXZTBW1sd1YKovjqF0AB3UaHDJYa8OjsnrHOKYa5MftuFs9M9wnpXQUbgV6QZsaLQT%2Fx6jviY1mho3Ytn4Ci2yWMbjgViAl1b9V6i2qjwORAf9YsQG9nENplyb0oY2Wo42qbM20yDwhTRfb4B3oaQZtNtH3L0TWLEvkM2Cfop8%2FLrWgWF55eQXER%2Ffvfcn0RypB2QoqmVaBS5fXkUMKZduw8iODl0JDpBRZEfcNFuuqk0Qtgjl%2F4w1%2BH7vAY6pgHUiRpNyePQtZjdJ7oWi8Ak7QR9UA%2FDaA3MDF3Zb95Ilq0fcIrsALBp0zDd06xAa%2B%2F3eMcfrNPS70khFJ8AQaVSrx1SGTSRzj0IL%2FrTrtaCrGn86KflZQHDFBNnju86aoSvKaxD5mAHLimteCWTJHVBjcIPBLxhVaNblDJexnUbfqI29WYcDkAVys5sLJFXtCBBbfkI3kCXJY78ai8jNKmB37Jst0dj&X-Amz-Signature=4d13f6631638a5444ad2678d57974dac66d2e127b2ac6a534d71b00caa3a6052&X-Amz-SignedHeaders=host&x-id=GetObject)
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