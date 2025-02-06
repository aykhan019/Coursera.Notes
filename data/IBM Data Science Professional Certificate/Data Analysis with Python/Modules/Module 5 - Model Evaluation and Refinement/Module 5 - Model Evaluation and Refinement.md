

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=1f9b61e87c4125de0364fcf4492355ef19a022dd1bc37d7e98f0c4af4c6325b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=2a6bde06a267690df59169e89b5aa0c4307d4d60686ce834bf31ce8228899db0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=d5c4153ed0fab1b35103e1d0a82c738c6fded55191c2569ddee7ac4cbdafeb2d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=39a5414b3438780f036d78e0ad42d8b0ef6c24030ee6233ee9719c7a37a9cee8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=160f948367e004c250044f80b9e368befc6358a38890369e52b96f050743377b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=ffdf849ac6d7e8860eff9905d052c7d56d13af7848e3a9026cce4185ef8596c5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=436d49cf7d436158f0608f572c80cf9e2390b6a426f9aba42027e19ce5d5b5c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=3fcd3c671aa4c16de03ae24a1c2632043fba149b54814b8266358f2fe599d712&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=366b6243b107bb848cf4f55db585c55b7603e7a1a68b2bda076eedcc73cf2c47&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A77U5SP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDSL7YXpcAvi%2FxYan72kTP7FhwOKhcgf%2FbkNS9iBPNyfwIhAMyhQLrcSVtHRuj%2FoQKc9LcCl6%2B7o5QjGqFUe4bXP3%2FwKv8DCFgQABoMNjM3NDIzMTgzODA1IgytIfd%2FJ%2F84%2FVGYVOUq3ANC7j%2FREvBcIXBrayEwzp2zZb5KfNne4yy66OgWgfWOyE8rYewrN0f4DMSuJBWN29yzQNNEvGks%2BvRCf5Lu4JVni3jDzvcFxEMBXOCY8N9TYoWnAdf3umEiz%2FW%2BCcSdC43dIFQZOPNRF7ePYmAt21LGxtkxRO7IqdsuIXE0aC58vKMpTBkGU7mRvLmMxK8su99gOMssJb2EkNT6AF%2FUOVDurNNl3KQgyunps%2FuWgImg8kW3VAhUhJSyZ2dz3sxcjuJxt0RDLKC4uEs7GxcE6%2BDSbnykergJuj5%2F0j8PEjPemFEk0J670aNeRS%2FraGTUPpFo4ecm9lbt%2F1R41tPWeNVDMoMrsqOK2AMxRvBRD0C2pwTjGYgx56%2Fpf2BzmH2AsKf1NuKlIR9pedSsJlWnHKwQHOlBo3nhgCHeMEssRF77BI37cFYJo9TMmClvjxp0APUGoZvBdwCs1uzMS%2BdWqM%2FLOjKUfRwbMET0MRkvhJq6jqmsXJwl2VM1ZIho%2Fpf28lKnMA5qKA9KplgWiC5zE4KMipTfMJzzQtrLRjTjrQGp108SMjELqq9yBgaRRx4e2nmeWgFQc1uxWJGZK6Q764A7sRS1wKUes7hSBbEF39W4GEQm%2Fx4voGgrzjtRljCDtZG9BjqkAT7hlPfx0F54ReT4CDJLI2wH%2BN5I4FTOnJT%2FFZloM%2BGNduOa7zhyo7xW8iNrtuFHnvH%2BRdWuDkNca73XFMxWvrJJ0%2BjnTvip14dq981tMHi3aArplF19E1SvZ77zsWxwzvwrOkcRKcDK1LDn2iMtIGG8wjqaNndnK2noIDSoWPyLNw9VIebtS126Ywu%2F74h6qb5VWX%2B3C3lUv2uWaXGv9bT4z%2Fq2&X-Amz-Signature=0529cb4c53a3e5043352aa070bc8bb4ac9178e630261fb0cf5a36a239f2c2227&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A77U5SP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDSL7YXpcAvi%2FxYan72kTP7FhwOKhcgf%2FbkNS9iBPNyfwIhAMyhQLrcSVtHRuj%2FoQKc9LcCl6%2B7o5QjGqFUe4bXP3%2FwKv8DCFgQABoMNjM3NDIzMTgzODA1IgytIfd%2FJ%2F84%2FVGYVOUq3ANC7j%2FREvBcIXBrayEwzp2zZb5KfNne4yy66OgWgfWOyE8rYewrN0f4DMSuJBWN29yzQNNEvGks%2BvRCf5Lu4JVni3jDzvcFxEMBXOCY8N9TYoWnAdf3umEiz%2FW%2BCcSdC43dIFQZOPNRF7ePYmAt21LGxtkxRO7IqdsuIXE0aC58vKMpTBkGU7mRvLmMxK8su99gOMssJb2EkNT6AF%2FUOVDurNNl3KQgyunps%2FuWgImg8kW3VAhUhJSyZ2dz3sxcjuJxt0RDLKC4uEs7GxcE6%2BDSbnykergJuj5%2F0j8PEjPemFEk0J670aNeRS%2FraGTUPpFo4ecm9lbt%2F1R41tPWeNVDMoMrsqOK2AMxRvBRD0C2pwTjGYgx56%2Fpf2BzmH2AsKf1NuKlIR9pedSsJlWnHKwQHOlBo3nhgCHeMEssRF77BI37cFYJo9TMmClvjxp0APUGoZvBdwCs1uzMS%2BdWqM%2FLOjKUfRwbMET0MRkvhJq6jqmsXJwl2VM1ZIho%2Fpf28lKnMA5qKA9KplgWiC5zE4KMipTfMJzzQtrLRjTjrQGp108SMjELqq9yBgaRRx4e2nmeWgFQc1uxWJGZK6Q764A7sRS1wKUes7hSBbEF39W4GEQm%2Fx4voGgrzjtRljCDtZG9BjqkAT7hlPfx0F54ReT4CDJLI2wH%2BN5I4FTOnJT%2FFZloM%2BGNduOa7zhyo7xW8iNrtuFHnvH%2BRdWuDkNca73XFMxWvrJJ0%2BjnTvip14dq981tMHi3aArplF19E1SvZ77zsWxwzvwrOkcRKcDK1LDn2iMtIGG8wjqaNndnK2noIDSoWPyLNw9VIebtS126Ywu%2F74h6qb5VWX%2B3C3lUv2uWaXGv9bT4z%2Fq2&X-Amz-Signature=b61d9ebbcb07b5cc16a67287ba43520fef38270e3f25210a42a2b1589fc47a96&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A77U5SP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDSL7YXpcAvi%2FxYan72kTP7FhwOKhcgf%2FbkNS9iBPNyfwIhAMyhQLrcSVtHRuj%2FoQKc9LcCl6%2B7o5QjGqFUe4bXP3%2FwKv8DCFgQABoMNjM3NDIzMTgzODA1IgytIfd%2FJ%2F84%2FVGYVOUq3ANC7j%2FREvBcIXBrayEwzp2zZb5KfNne4yy66OgWgfWOyE8rYewrN0f4DMSuJBWN29yzQNNEvGks%2BvRCf5Lu4JVni3jDzvcFxEMBXOCY8N9TYoWnAdf3umEiz%2FW%2BCcSdC43dIFQZOPNRF7ePYmAt21LGxtkxRO7IqdsuIXE0aC58vKMpTBkGU7mRvLmMxK8su99gOMssJb2EkNT6AF%2FUOVDurNNl3KQgyunps%2FuWgImg8kW3VAhUhJSyZ2dz3sxcjuJxt0RDLKC4uEs7GxcE6%2BDSbnykergJuj5%2F0j8PEjPemFEk0J670aNeRS%2FraGTUPpFo4ecm9lbt%2F1R41tPWeNVDMoMrsqOK2AMxRvBRD0C2pwTjGYgx56%2Fpf2BzmH2AsKf1NuKlIR9pedSsJlWnHKwQHOlBo3nhgCHeMEssRF77BI37cFYJo9TMmClvjxp0APUGoZvBdwCs1uzMS%2BdWqM%2FLOjKUfRwbMET0MRkvhJq6jqmsXJwl2VM1ZIho%2Fpf28lKnMA5qKA9KplgWiC5zE4KMipTfMJzzQtrLRjTjrQGp108SMjELqq9yBgaRRx4e2nmeWgFQc1uxWJGZK6Q764A7sRS1wKUes7hSBbEF39W4GEQm%2Fx4voGgrzjtRljCDtZG9BjqkAT7hlPfx0F54ReT4CDJLI2wH%2BN5I4FTOnJT%2FFZloM%2BGNduOa7zhyo7xW8iNrtuFHnvH%2BRdWuDkNca73XFMxWvrJJ0%2BjnTvip14dq981tMHi3aArplF19E1SvZ77zsWxwzvwrOkcRKcDK1LDn2iMtIGG8wjqaNndnK2noIDSoWPyLNw9VIebtS126Ywu%2F74h6qb5VWX%2B3C3lUv2uWaXGv9bT4z%2Fq2&X-Amz-Signature=f26e9fe1e87037cb7341d07be8f7bc0db6e0099aee2c4d507e8efb9aa08f8880&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=0c9416708bbf7f32f843339e8ed123af9c493827e83e2a29de209ebb5eaf3d29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=d69d34b931a3ef7503050ba2c0fca819d9b3454b5442a0fcac4a7151de944822&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=b80a746d35d5a24b16b543c0ee8b95d13ad866e4f66eecbd925c1bbd01bb66fe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=70b4e4d2f4af7b222bb06270cfa772fcdaf3ec77c85cc9de4236ccae246fa7fa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=0ca13057a3aae3273f0ea6d31deb9900d4e8900749d55a961fffc81138859429&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AUM4PL6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIDr2Lfkrjjb2m0M%2F%2BibgxifKrHg9WuRulBF7FwPQEmoJAiAI5N43%2BYdAW7UQeIQ1TH165Ff8y8%2B0kyKHOOus12Vt%2Fyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMtohBIwrTE50dOtXNKtwD5AirUI2IixO6kZ28cf4peHhrcj1DEask7tlN37KYW4KE3glqftEPEonAVHEDyw3kMrequ%2FoGRvovlgll72HrzmEZaq%2Bv2QSM%2FJSeoR%2BPkpThgI7e6WPpCG6Q7gBC7HW9Ww0QTaZrlVi%2FEWx%2FZtGFO0bU1NIn2vF%2Fg72IUYkzvRw1ifLPnD2x8MISaNq785GDDVTtGvCb23Ui5JXoGnMngfj8H3a%2FpnuIMVCu8u7MASwN7UQxGKuYT4T6Q5xbmxW6V4AWPdbMC4i36dZ1TXXYCvCtRC%2Bnxe46li4O2thklPBW7w3mOkmEHxMXVS3cx4p8lROpyDC%2Fei2QQtBFhNMOtzeSsUTAIWniBrJtfbaV1QQN1sO0pVdtFGUh6JsGAMSQY2UtKs%2Bg%2FJn12P%2FjxE%2FDHgmmx1nwuxN7z5%2FiuKaU6GmRKShjrUA2JG8dyQCqPfrmWSE3E8lKzBY7BrOfX64XeVjz9RWaiLrY2c4gx%2FcVmnxZPYaMwmeh1nPUDjyajIx%2FUPsWcVJsftvgGiyeHbJpI%2Ba5gm8Rx4LWfoKNzBEH5TMfGAKpock7wAz%2BUIqfcrSjbrNvhQ5SHQQKOpXzWXjFR%2FFumDL4Xu5Y7MzpRnIswU69eVEyS3LFs9lY93AwzbSRvQY6pgEMX1JbljX6J2dUhK4ddKU%2BnYxO%2Fw%2BfYaPymKyH9tEZtsLRNbYgDcEbpaUO%2FdaiFrDJQVwt14SfpRjg8NtM0uAXQz8eFOWq7pjTtWeRIydrpHzFSQrc%2Bzf0nLGjfLdBNGL3SerNP8uFwEc7INPt4DcCaNLFEC16PNI4rVdMd1AmbEUMFFBfsmD%2FR5n%2FqwjSMWrflAc0JsESjdF63kCXV7CmKWEwSSbp&X-Amz-Signature=1e729862c382bd179bdc746a15ef45eaeec110dda4ee1a0b92fd029689e67765&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKR4CSJI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCzIzq8Club8UqURIYVy%2Bd%2BqnuGEry%2BBbYEhR32F3gwsgIgV%2B7C0ac0H14MxdP%2FOLuQD7uwqa1qQnwydNky703oLBEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDMtHSUs2%2Fze4o%2F1cnSrcA9fLxlBL5mCYaxA1nySsk%2FbaB0qhGiUoY3PmxIikgcFS07ZADBmGF%2FdghAutb9xZ8T3NFsATdbLArIm0w8a%2FKbZUTWVtZhIC4lA4Lfj2KfuJc6mJomZQTYSUB7rHE0%2BtfA5tq3vxVBJtnsKbbU9dFfWMPjkF2dL5JJEBO64ZBsBHkRi%2BOCDFDJwe2eWgOPhdRMp3Jl5WcBFQzufwJVfa%2FXd2Av9P448w7DrraADrvly0a0cNVLIrJvPKnrHtpy2b0vDlieWsUMQR%2Fden9ArAfDfpEqpvpp0jgRp%2Fksp3xFHItt75Ne7sGnYIBeWuQSEzjx6AO4UuWZvYcCq7gqRrNQUSWD96UsH5OoqNkdkKbAMeGaH0LOWlH6M2JrcJGWBqGL7%2Fhb9fc1LycrQRr1yJ1IrXOM71VrqZPLRi39ZhN%2FvaLgjFXE4jbh%2FnOjfvgzATS5IqdQ92rrmqHjCj4wsQfFH8S4%2FmG8mO9I7hMWllYrHr%2FQsiPRsQ0FEzERPxJo8Nenl3ZWvpQRNdS7t0KUFbaZ1WMXdZBKYi9QP2q2am5VMYqj%2BMQR3f58EBr8HOGptQActTQZ9JO1FU%2FxpEVd8YjsnGsD0pcMwU54GO%2BgUTKNWAiI%2FD%2FseL0A3NNvSoMPu0kb0GOqUB%2FFW9%2Fe28%2Fps%2FOdOxjoWil2X7pBM7KbNlFTiBx0oVdoCRl7Ajsa43414B7hCkwWNTknUZposUynmNErkEhjQ2T3IBubbd%2BkGpTrd9%2BQFk3%2FNMaeb%2BIvIU6KsiDqOVW3HdaF1kmA66s4Vf8IojkpE0SgO44ee9n3%2FNeYpA%2FdiXxHwRZ9myruCZFLGwlRooWZr9tyYZilkCmzz0ZCZgn2MdtI13P6VC&X-Amz-Signature=fa888e8cc66ca0268deb64a05ccd8e245ad0245e6fcd23832ace0d568efa453f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKR4CSJI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCzIzq8Club8UqURIYVy%2Bd%2BqnuGEry%2BBbYEhR32F3gwsgIgV%2B7C0ac0H14MxdP%2FOLuQD7uwqa1qQnwydNky703oLBEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDMtHSUs2%2Fze4o%2F1cnSrcA9fLxlBL5mCYaxA1nySsk%2FbaB0qhGiUoY3PmxIikgcFS07ZADBmGF%2FdghAutb9xZ8T3NFsATdbLArIm0w8a%2FKbZUTWVtZhIC4lA4Lfj2KfuJc6mJomZQTYSUB7rHE0%2BtfA5tq3vxVBJtnsKbbU9dFfWMPjkF2dL5JJEBO64ZBsBHkRi%2BOCDFDJwe2eWgOPhdRMp3Jl5WcBFQzufwJVfa%2FXd2Av9P448w7DrraADrvly0a0cNVLIrJvPKnrHtpy2b0vDlieWsUMQR%2Fden9ArAfDfpEqpvpp0jgRp%2Fksp3xFHItt75Ne7sGnYIBeWuQSEzjx6AO4UuWZvYcCq7gqRrNQUSWD96UsH5OoqNkdkKbAMeGaH0LOWlH6M2JrcJGWBqGL7%2Fhb9fc1LycrQRr1yJ1IrXOM71VrqZPLRi39ZhN%2FvaLgjFXE4jbh%2FnOjfvgzATS5IqdQ92rrmqHjCj4wsQfFH8S4%2FmG8mO9I7hMWllYrHr%2FQsiPRsQ0FEzERPxJo8Nenl3ZWvpQRNdS7t0KUFbaZ1WMXdZBKYi9QP2q2am5VMYqj%2BMQR3f58EBr8HOGptQActTQZ9JO1FU%2FxpEVd8YjsnGsD0pcMwU54GO%2BgUTKNWAiI%2FD%2FseL0A3NNvSoMPu0kb0GOqUB%2FFW9%2Fe28%2Fps%2FOdOxjoWil2X7pBM7KbNlFTiBx0oVdoCRl7Ajsa43414B7hCkwWNTknUZposUynmNErkEhjQ2T3IBubbd%2BkGpTrd9%2BQFk3%2FNMaeb%2BIvIU6KsiDqOVW3HdaF1kmA66s4Vf8IojkpE0SgO44ee9n3%2FNeYpA%2FdiXxHwRZ9myruCZFLGwlRooWZr9tyYZilkCmzz0ZCZgn2MdtI13P6VC&X-Amz-Signature=3630499bfc41ee5d16a343efaf9bb9b2e3392e7e533605a6d0767bd11282855f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNWOKTCL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIB7ZQ92Gp6EWSSttHufSUeJF0dkGT9FcW%2FrRwOvsDDBjAiEAzjwW1Cz%2Bg%2F9C%2BHpZwRM3cIdUtFGdkc3Zlqbno8%2FsoFMq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDE42gen39wPwUNdliSrcA7yRp99TXXr4wGAtjJ%2FUog5qUJraTJlpfGmnv0dfcgD%2FuLJQzhAQ1gfTHAvgZWBpId8sn8rcubSOusgyP2GHumcvCqy1tmtkq91GMUBIEv2Xh685mYdDxEi5MXL1Z1P7EbXfRguGBbnh0xz8fh285VuTu2%2B2yjnchBb1s6uFgY1ChD0ApEqcivY25G1or5tdK0kSvxOSL8QL06gIsGpCOOtAmLPJD7pxl%2FvT0wTNHg0p7tSwp5SHjmNEppZPbAa3NsbXaOptpAIipWdBUoULZOQkLRPJgq5P2UGD6PpvCnbdKpWV0rzUHdeuPnUj%2FqcIwaBRVBBnPvZAfR6Ar7Y7iSmFOYlP1ocSkWjPjs7jksdWkJhgIDDjmmlZafQNAEIbl7GP5bhkzlz1cs6bfux9ajIOu4pGXG35fyVPgeXy3lZsvlQnsyaVxNjUyc0Ak5XI4Cabk8%2BL17uRCR5Qc%2B%2BR6fAJhdtzMI5K6eSLfPoEkIb%2FEVPRRHx1zEaM56JOAxhoYMeQeOnwffzzm2I2a8fxaGkC6rIoswOCHjflg1osKshgpIEEWZVmhxKFALaU2FmXwUw88DOGsYyJxvkP4ImeiKKyMKE3FY545CYeyNS4KbnY97sIqpx%2Fnzqg5WAlMOe0kb0GOqUBDBO4hI1knPZfslxhZqsuu%2FyK5JH1q5idy7NtBi8TaQEGTi1mI5ZLWu%2FG6mibnyFYB9ygQJ4SIIh0ocb%2FRqgzXgPuAXGi8s60Ajn8cCA08JYQo2zb08nnBSGjv33GCp84XmCa4lG%2FcxF0YeMkhRTuskPpYrrHNuyESVgG8gzBVbFb3wbW4E39%2Ft%2BacFowIQKOvWeWJ3oIY2QrpVPzrH9tyraIx6j2&X-Amz-Signature=39dd8b6ce4b7feb8acf98d3219b97f47059b20d5950415143ef716afc7cd4f35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GP7LCZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAkX24k1k2yseJCcnufp3fnw%2FJ%2FNOtoQ5FHcSHI3GlDOAiEAqa%2FHUcBWRB5Ye0dsT5wYp3FI0v0bS0NdV20mz%2BzaSDAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDFSCppTYif81lci8nyrcA886OBLF8RB7Z6u8QbZU3O0lCAjYgjV6GpFoP4RXY2Maulv32PeZ0DGFSSZBS4%2Bce%2FPv2ZIe7ZQKeu0G2H%2Fft0ZqFHkUfyiNvcCyZSk9v6suuIh96VFErYEC%2FbxsUa65MLgPutHOueZvq9pHO%2BQkv5QAHTgKhuyr8J74gt%2FkVoFq2iS0LSEqBDCdxvcF%2BBvASjrV7lH%2FPxXsus3w3I9T0Eiu8BsL0maPxx92w5Ag9iKPu2ml%2Ft6jx7P%2FtuOvMvF%2Fq9Xt%2FH46bXttGluwT4CxPiI8hbswawNXYUwuWHFBr9KxvVsj7lMkOZNS3uX3zH4NwCT66aiSX5W7J4vUItE46CFx%2FrsfIQbge%2FMh7rKh3Sfv4LhDsIGgR%2F8bOmNtGZJIMqve3h5YLJiBTcdHApVOZiIjyFrMcQ7zu9diqt5WqSM%2BAY0LTvaRcQP0a76a3PvcvploWSymL0A%2BS6PaEz1qrwIftR4WanXAcfnZL3R3ZwgG0R927K7s306uIPbHFwi1TN3i6d2iA4CmGe7qeeNA52x%2FrXYF5o%2BGU6TWaFSruB8TfFAkm4cG3XBtqV9aDsWUzQzRBEYQ1zLdUvwkJsRnAUjRoxrMiIyPiJLXJokCwNAwo2uagNzpK5NtQqdEMMS2kb0GOqUBxcvzFXhHix58Dj9%2BpmHqcg73K%2FC1nyrHUk2E5ikj%2BCMmNi%2FoCmG3dDe9EZw45rMihsrxZgdxQ3MDgDIJtS4b7bRiT0R%2Fj8ONUh5Ojkw%2FY1dUJ%2Bz5xr6xq2zx8XxhOHo3tGvk4dEDcMrml%2FRZZudcQKUQL17T7uNULKppLgolPjNjvdJgxIYhCTjWD36f8EQJmIIw1CX4%2FaRsk9PEJrOQB9db4MNA&X-Amz-Signature=9c221faf131290e3b354754d8bca0d02923a248307589d10b3986329898bc157&X-Amz-SignedHeaders=host&x-id=GetObject)
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