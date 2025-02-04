

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=0c0310eb9eabf0a6e61a3505a6509eb500817b101038a48b7d0c8a5d0ad3d29c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=11ff663283dd15cb71dddbc835592ec8b5f8d19df2b952bb47e864aaf496adbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=d934b4b224605bae79a49717461b5a41f7aaf469d938e8dea8165f2c4664b8ff&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=ca374ef0400803e929e4468fff521ed239536f66623e8eae6929dd85ebdf0c0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=ee6a6ec7a029900901eb6ed83b134e19581e91cee40614b593844717027f4d6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=821012a6cf003e00a2bb447b3c9382482888fdfedbf8660874bbdd97aa6dfde2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=354fa21a273f511c4d582971384ae1ddd4242ac96e6b4e34b5a51dcbbf13bdef&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=062eebbb5cb5e2ae1b4193bb17b305d3bddc3eb6109aaa654b7a1ff06b59601f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=d9f0d0aadbe073bd8972e0136167f8fe1919542edaa65c86281d01fd2268a56d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673G4MBFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAQJ8haFJCMPNjFRMh6rJDBD1h3m5L4is5SGRJFBh30HAiB1TQ4iLzfcO0GTMZPDEdSp307KWouog60vpm2XzjXsUSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMAyWQeucaoqaRxm3UKtwDgKzE7xtQ6ycrm7bQlFAGQXG4hfYUjJRDgO9Kf1shEl%2Fhze5ixhphPPKMWkb4TXfZLVGDmTXF0SlmVha84AmSgXy6x4lBZnuox%2Bcuepl3HefO%2FUsbSYzbSS6KhlRePKQZze4H3CNV512LO9dQkP9dO275uygORkGP8sPWedEHL2nRfBZ8pRUOlie4DOtpRHdIN8I6arxnjPXh2yOmmLrQw4RGZRHXGKR1aDWUFmh0HCCmi%2BR1ywCBZE4kcK4eMMsF9k%2FCFunxYxbEvnvYrzODaBUzwEk4udpWhZstSoCHDmbpm2Semm%2FT8h8pBkVtzijO919ShnGC1Mp0o%2B9vZp2Xn9qHi485r%2FJE4ZB8XrF9JYycTbKFIGF%2BfweNvVJBH6p0oul7IBKdcXGkNPlEgOp7I7IL5jnu1Lq4b3HiM68mh8Kr24RCgeHZH5h495V78foqfEhYav8ZR5vc8uwpE9Q5AYYzV2HRy95KCuoxhNlD3N5%2FtxdTErVbJrkGTEqH9ZrfGQ0G%2BqMnf2wlvNzA7js5E6uBLmlG9zC14IzeXvRGr5iJkXyIMun92qTT6Y5yTFP%2By0Mei%2F8cba3P8eyLqrX25LKXYE57EftZPZW1Jvq0Tf3bTvzc63PjuhQ8CeIwkZSKvQY6pgHKQMnQETzWUlsLWZQwJP3uf9Z03GTvII9pbcuW4Bn12KPkKB4MDkSGTHm6mEYfE9KRdOlxI5B22mJEm69Nb%2B1U23VG68KA%2B20ldoZVA5B70phCvpv%2B34wXQaSpVls9TLltIROGzhP61coY0UtLiuLst1EYd1PCQXPt0O1R8HMEpC8OqLGSEm4LPTPWFCyxxX3eESA9vxJVYqwtRhAf2rklv1SmJ71a&X-Amz-Signature=139ffb48be9a7877fc8b7bbf5c63002d7577ff2cbbde6ae4690b16419050fd8e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673G4MBFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAQJ8haFJCMPNjFRMh6rJDBD1h3m5L4is5SGRJFBh30HAiB1TQ4iLzfcO0GTMZPDEdSp307KWouog60vpm2XzjXsUSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMAyWQeucaoqaRxm3UKtwDgKzE7xtQ6ycrm7bQlFAGQXG4hfYUjJRDgO9Kf1shEl%2Fhze5ixhphPPKMWkb4TXfZLVGDmTXF0SlmVha84AmSgXy6x4lBZnuox%2Bcuepl3HefO%2FUsbSYzbSS6KhlRePKQZze4H3CNV512LO9dQkP9dO275uygORkGP8sPWedEHL2nRfBZ8pRUOlie4DOtpRHdIN8I6arxnjPXh2yOmmLrQw4RGZRHXGKR1aDWUFmh0HCCmi%2BR1ywCBZE4kcK4eMMsF9k%2FCFunxYxbEvnvYrzODaBUzwEk4udpWhZstSoCHDmbpm2Semm%2FT8h8pBkVtzijO919ShnGC1Mp0o%2B9vZp2Xn9qHi485r%2FJE4ZB8XrF9JYycTbKFIGF%2BfweNvVJBH6p0oul7IBKdcXGkNPlEgOp7I7IL5jnu1Lq4b3HiM68mh8Kr24RCgeHZH5h495V78foqfEhYav8ZR5vc8uwpE9Q5AYYzV2HRy95KCuoxhNlD3N5%2FtxdTErVbJrkGTEqH9ZrfGQ0G%2BqMnf2wlvNzA7js5E6uBLmlG9zC14IzeXvRGr5iJkXyIMun92qTT6Y5yTFP%2By0Mei%2F8cba3P8eyLqrX25LKXYE57EftZPZW1Jvq0Tf3bTvzc63PjuhQ8CeIwkZSKvQY6pgHKQMnQETzWUlsLWZQwJP3uf9Z03GTvII9pbcuW4Bn12KPkKB4MDkSGTHm6mEYfE9KRdOlxI5B22mJEm69Nb%2B1U23VG68KA%2B20ldoZVA5B70phCvpv%2B34wXQaSpVls9TLltIROGzhP61coY0UtLiuLst1EYd1PCQXPt0O1R8HMEpC8OqLGSEm4LPTPWFCyxxX3eESA9vxJVYqwtRhAf2rklv1SmJ71a&X-Amz-Signature=816098e0cef684e05d43b4fcb8d74d8fe2ec982f5fcc38914284d639e70c21af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673G4MBFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAQJ8haFJCMPNjFRMh6rJDBD1h3m5L4is5SGRJFBh30HAiB1TQ4iLzfcO0GTMZPDEdSp307KWouog60vpm2XzjXsUSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMAyWQeucaoqaRxm3UKtwDgKzE7xtQ6ycrm7bQlFAGQXG4hfYUjJRDgO9Kf1shEl%2Fhze5ixhphPPKMWkb4TXfZLVGDmTXF0SlmVha84AmSgXy6x4lBZnuox%2Bcuepl3HefO%2FUsbSYzbSS6KhlRePKQZze4H3CNV512LO9dQkP9dO275uygORkGP8sPWedEHL2nRfBZ8pRUOlie4DOtpRHdIN8I6arxnjPXh2yOmmLrQw4RGZRHXGKR1aDWUFmh0HCCmi%2BR1ywCBZE4kcK4eMMsF9k%2FCFunxYxbEvnvYrzODaBUzwEk4udpWhZstSoCHDmbpm2Semm%2FT8h8pBkVtzijO919ShnGC1Mp0o%2B9vZp2Xn9qHi485r%2FJE4ZB8XrF9JYycTbKFIGF%2BfweNvVJBH6p0oul7IBKdcXGkNPlEgOp7I7IL5jnu1Lq4b3HiM68mh8Kr24RCgeHZH5h495V78foqfEhYav8ZR5vc8uwpE9Q5AYYzV2HRy95KCuoxhNlD3N5%2FtxdTErVbJrkGTEqH9ZrfGQ0G%2BqMnf2wlvNzA7js5E6uBLmlG9zC14IzeXvRGr5iJkXyIMun92qTT6Y5yTFP%2By0Mei%2F8cba3P8eyLqrX25LKXYE57EftZPZW1Jvq0Tf3bTvzc63PjuhQ8CeIwkZSKvQY6pgHKQMnQETzWUlsLWZQwJP3uf9Z03GTvII9pbcuW4Bn12KPkKB4MDkSGTHm6mEYfE9KRdOlxI5B22mJEm69Nb%2B1U23VG68KA%2B20ldoZVA5B70phCvpv%2B34wXQaSpVls9TLltIROGzhP61coY0UtLiuLst1EYd1PCQXPt0O1R8HMEpC8OqLGSEm4LPTPWFCyxxX3eESA9vxJVYqwtRhAf2rklv1SmJ71a&X-Amz-Signature=0dd2bf99313e1d0b970ccf1a3143fc0bd80894d105a4e759763bfcbcc00a2f29&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=48a7e8855d522dad3f11735de49c31ce5ef1d9f72c89c0634ba798382d8b4255&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=6fd61b6b8e15c83335e9e92baebb832ede8288a8cccfd9e6cf348581e68d8bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=ece3d09f412d207974bcd0764f0a6f0993b1bc8739578a5288c460c22f9bb22b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=148fea667412b64dc2fea4c9c6330dbcb484e455bab3fc14a899934ddf34c071&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=1089c53ec408553d32e2f05bf90a7f28e5627485ae4f4fa8146c7f9a8ad75bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSG5RWWR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIFuMrpcXYee%2BKFZFNKpYqbzk7yFzCs9p8je7d99%2FcV%2BWAiEAgaTedEXuIN8YIXim3gKcFqGlm9QTY5%2F%2B5zub%2BDGETokq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDEw61SK%2FfkGklPMKCircAzIdKf%2BD7au%2B3t2cZMrzjFzw6AVGpFVwgb1O2yUVFTatPiRkLUzRIxnqSIfahX06C8j4axj5KBp8kdaQSn7aeGv%2BkXu6b8bPaw8bEAfbSokDkHIpvB3wDvbLKdgNUn3%2Fqza7wQ7O6xeJa%2B1VZLvKO6h%2FBseGZJ0lbIdzFJyuL9N5HLwulmaCXhtKyC8t6CTCUoHxI69HW08sL5sq8glIAI8K%2B94JjRgpZNG%2BGYnPUGqEsAsY26hgrHNed5H9Bo3A%2B8kLcQnbLBTOaZkCBSTe%2FluW1DcuLHuxe5Ga9XmpBqsqN12Nbn8XVy%2F4KWALW92tV2HXjSBE4Cylpy44uJyRVck34OUV0cmaa6xZtXlOndW3L5HSsNLqVOyCptVYOPWnxnZMMgxmByE9Pr21H18OKz4vONO6IGgHh6B4IwFsbA6Nxw1w2%2FMv6WSwxhekOOhH%2FgDUa%2BTBXbRim%2BeIeWglE%2F1HtYiQ5%2BRgU5sti8IMzkdveLkPh4lo4kTedWIA3wMZUu53iReYGN09W2cTDSBwAbUYoIuW5pu3KfYHVBoU9ttAhrv9uvIlGzQcD3bhH1HXSXlHGdSuVoik%2FDe7gqSVYdcNT26WaDL0T7vsz6tkVCeGRbNLDRTz6%2FbLE8yKMNuUir0GOqUBUVPGVVfW9fM1JNotaXcaTSfX8EBvW8kOb1FOLlo0F84ndWzUDDZAk7l9HQYR%2BQkHu6fWAMZHrhBSzBa6DFyqKbxfgkcy4qCJvVDifbTqHM%2F%2FUadRLd6gTF%2BXNQ6Qt%2BTFvoxRTyv%2FQ3cxBK%2Fz8XcKME5xRDENAUXJxpIsoFKng13Siiqci8TtMLNPFvDevVlj6l4M4JYI1Jfi0sbxbWHko3qgsahB&X-Amz-Signature=862361b0471d2d5748ed88923d7a2ddb056d8dd99ebcaaf558cc122a06c340cb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3NSWOCF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIEeHxknGnPCIqDfcJCAJ%2Fen%2FFjuP1aQlMBoU6pe0njSyAiEAt%2BYQr%2BUYi6AK%2Bdq6u4yeYvRPQWVHw1PNlRPR1IsViagq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDNRNmhuOpMAUvcYX4CrcA6VYx7iZyQLX0K9MrXRh%2BDTdlzepiVLFZ9cotriukC7kZ%2B%2FF4Q%2BPjAF0ejMubU472l%2BqecP8zLwJMHB03s7yvTu%2BUhA1J4IFUgvNb7aHQCRy80CqJiZNl5o1Mozc91Ipdw06iI1Ap4PvgT8H6t3fDYMTa2hAfM6vJzHsMxv5glzzBw02Cebn1jWycKCKB0tSxohPAxACpf02z4xKo%2BMTaEf7PfwHxjj%2FtJQEDJG00RDN1V%2FijL8rHbCzWYSL5RXJfXXrvXazePe2vRINr6I3LOqE%2BL2CyuBx2shb7TG9eLvbWhRRgSq3T1Him2rctXKB8Bv14yZLT60Nn%2FRivGGEVgTaFAYPhrHkVFK3vi3F%2B2yUHUMqptKFTlCwmFAMURvXyLuBLulo8esYSGG5B%2BmczrzgCyCRoPYMyyNUd7GWkEYyRyfyIG8ro8ky%2BzF24kunEg5qDJckFlqPE%2FppjE36NVw%2BF%2FvAs2n9vvlWeADhdC8kUdSMohb5xT08EzZaMgqT8jcuLJkSH4ZDbk8HumQlChfjWD%2FFUjhO26xX2%2BisXpS7nztjEea8%2FCoUAZzhJQbruQ7SPKdmGUX8%2F4zLWnHd8ZNZa8pOF1dzOD5KZkqm0GONKkUBrNMXHdRE9D4jMLKUir0GOqUBbFeH%2F%2Bqv%2B1M%2B2aLhBMZS9DpiTvEXNk8hUKkjwjPZsUYHuuDpMJQ7Oe%2FXKoBskB3kmBFlQaq5nTmlWZfuBl0GwElFPC0vW9EfwZNeUL0Gd0XwKoO1q0GVyxZvL0pcJvEbPn6Gwae2zu7AXQzavu%2Ba4kjsL1wUV%2BUjgHO3q3P%2FCGeshXcgfbd86b5KyR4fths%2BboFT6VKQJwFtGIVUFN4FxE%2BoFwpI&X-Amz-Signature=a6964e5ca3b641e2ac23c593125e5345e23446a5b996848b65c7b8340c92c1a8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3NSWOCF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIEeHxknGnPCIqDfcJCAJ%2Fen%2FFjuP1aQlMBoU6pe0njSyAiEAt%2BYQr%2BUYi6AK%2Bdq6u4yeYvRPQWVHw1PNlRPR1IsViagq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDNRNmhuOpMAUvcYX4CrcA6VYx7iZyQLX0K9MrXRh%2BDTdlzepiVLFZ9cotriukC7kZ%2B%2FF4Q%2BPjAF0ejMubU472l%2BqecP8zLwJMHB03s7yvTu%2BUhA1J4IFUgvNb7aHQCRy80CqJiZNl5o1Mozc91Ipdw06iI1Ap4PvgT8H6t3fDYMTa2hAfM6vJzHsMxv5glzzBw02Cebn1jWycKCKB0tSxohPAxACpf02z4xKo%2BMTaEf7PfwHxjj%2FtJQEDJG00RDN1V%2FijL8rHbCzWYSL5RXJfXXrvXazePe2vRINr6I3LOqE%2BL2CyuBx2shb7TG9eLvbWhRRgSq3T1Him2rctXKB8Bv14yZLT60Nn%2FRivGGEVgTaFAYPhrHkVFK3vi3F%2B2yUHUMqptKFTlCwmFAMURvXyLuBLulo8esYSGG5B%2BmczrzgCyCRoPYMyyNUd7GWkEYyRyfyIG8ro8ky%2BzF24kunEg5qDJckFlqPE%2FppjE36NVw%2BF%2FvAs2n9vvlWeADhdC8kUdSMohb5xT08EzZaMgqT8jcuLJkSH4ZDbk8HumQlChfjWD%2FFUjhO26xX2%2BisXpS7nztjEea8%2FCoUAZzhJQbruQ7SPKdmGUX8%2F4zLWnHd8ZNZa8pOF1dzOD5KZkqm0GONKkUBrNMXHdRE9D4jMLKUir0GOqUBbFeH%2F%2Bqv%2B1M%2B2aLhBMZS9DpiTvEXNk8hUKkjwjPZsUYHuuDpMJQ7Oe%2FXKoBskB3kmBFlQaq5nTmlWZfuBl0GwElFPC0vW9EfwZNeUL0Gd0XwKoO1q0GVyxZvL0pcJvEbPn6Gwae2zu7AXQzavu%2Ba4kjsL1wUV%2BUjgHO3q3P%2FCGeshXcgfbd86b5KyR4fths%2BboFT6VKQJwFtGIVUFN4FxE%2BoFwpI&X-Amz-Signature=8afeaa29fd72104c001b1ef3d6a73c704787ef19f31a47946e266216ca0c4bf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YTJUG4E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIA0N4Slv9ul2E7%2FBRVxe9VDrY1ANWI9%2Br78IaY6tNuLsAiABeVZxUP7WZf4YHCcsJBgyUrxaIuvWNPiX7npkaq%2BD%2FCr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIM9U8nqVAbC9Zikq4BKtwDyOMQakMPyyho7vmthvO2a0NdhRpt%2BD8Su2O7dCr0XPz%2BdSSfsrLxbLq6HLMHQAAUFc7c21jHdjqoCeSOK2AVAQ7Wvy7fCKl3kU2DyAegq5TCcWSqdwHKtCnWKp03y6YWF3ks5rb%2B2dSYULDwSgwO0nzSma4mEe7b8SR0QV9qDTIXwFxHnNUnQCX%2FNzBsEXkWl4wsIzt7uqdQ5XL%2BoVxd78TyS5avrbDqbTMM%2BIPaH5Ydb%2BjdM0AgUtbXzUs1Hl3P8iMjTncORocK0DoWKYGvRXiss1YcGhdxDUhvBcPq3JtIEA0UU5EIvTbFHMRHVELNshV8udJZTUryNu6qvCIoZzGP0pb5mhLWLEadTp8E72TYWmeAVb0A6eS7p7d8BNbLtSaYAKM25wKvR80WnTXmEHkxBBjUN5yRjFRxNCeGXmjRo9gq3BisWEMpp5qWK4kkwN1fbwdaJaZ9CS9fs9frVtNwcwa18LxUy05%2BJ733nleYLSHQcd4LHt8wrNdAnw7oY%2FcI4eeiFEYNSQZe%2BuLK4FKVpf7Xz3hBGRBFTb2fBN2tQ1XvDbXE%2BACs0jMf%2BM71IzfXfhOfXjU7RIRzOGHV5QIzKsgvsRtRd1pJ4Am4dibk3i7Yqav%2BZZxUyPQw6ZOKvQY6pgEottNpqhMhQMCMizIg9UuZMYU1%2FK2Z9oyJUovuWyxqIw6qW0i0PzBacoH2lOYi92RqEofwQRHE1fjCougmGynWGzcdOh13%2BVKEzNtTOQ53VnGioM3h4ge%2FKSwVXaack9GmBfdz1Z8cdt1ubk8DlBOepXaAYa9qypvJZviXScq6j5WgIkDh46OXIBmdEQWd3G9yPDih83yOSwsy0iRdaioU0PExC9nS&X-Amz-Signature=edcf69dfb1e0b5058b5e30a6c2d81935881bad8a78177be26644a22d37d203a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IFBHOXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICQxxV%2FVpxrzfgCxbRmf1PReRHJI6tEPmmfbzTnmHXFqAiEA0oNUacbnAFgCRQdcS69MF6hLUWWb3%2BlkX10PnClRicAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPUxKLx5LmMwVSKatyrcA4iDYVP9fUF9eFClmlYi5DOkG%2FrAgOX7W7ldEtYE04UmdK%2FC2c3WO8T6r0ko8s6l3tHfijwBgYBM9Nz70szPnZBRkkhTHAbxbc23KlNKL%2B3kWH7S1wzJq8OIy8L5tQmQTgAD%2F%2FyFBhOYQKkpGmayuxop8DG9N5AzjdNVaKFjQxRBbUSTVIih4y8KsZ9syq7vtN6Kepij1j3RPGpGZAN4EG9LSng6knbmiaX0McZDixdZQPOcaWVKvk9ZEe5i5nMFBvbiRAEjMFcX%2BrdT%2B7IO9XBH7d87ulCpKnVZEnE2noZCcARt4M%2FwjvGLlTmH4%2BWrwoaJTDrhYQGKj5UvbbsxUyp9ZFW7vC6yiNHs4k%2FUyKSgUWPsaGvV1jC2PLEqX7mWW5RBKbJXFcB7pDAQQeU9lNInysiFRVKXZHW9H5bWNsHr7nGC2EC0rFL5j4SMBx0A5JRZo0Deacbc6AL9Mlo63yPYWo%2BWNVGgycsrSeyAtWenoDf%2B5311rKrZXCCvUPw8cTqHym9NjQZIKh4LaWg2CTe%2B9FFZaNs%2BGkMWpd%2BPDeuUfLmV3f3%2FN5Jm4BCJiui1M34MUY5kbeutA8OVgubl1KNYYrZG7uLo9nlJEPruESVI42nXJWPQ%2F4mUOtY7MKaUir0GOqUBWMXXwGJhBLt9mChbIck9PLsynwQTMepfOo7kpWQbfSXtRB1VshQcH%2FACedlq%2FPn8lmiFl5y%2Bz8hYnkLo7NNPjdBiTSYnMb3lPhXv6rxWnJgph1zjXE31PBk9kzA%2FPf4FdxQP7mFcJpU3m%2BGJosFJdQTCnWemZ6psB5Q6%2BlxQrIh48PyhWW%2BRrqY%2BUAw1g%2FuMCLygPGrWatv7WNI4e2DxYocspHyE&X-Amz-Signature=8a9c3b9830d86605d0731d13566e302c60557e5dab67e5dbd484d90960e51c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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