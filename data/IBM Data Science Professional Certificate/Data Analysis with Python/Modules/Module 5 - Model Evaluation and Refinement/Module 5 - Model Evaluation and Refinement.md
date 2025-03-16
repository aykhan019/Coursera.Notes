

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=3ce8e5208d37db914f360284ec1e5cc798b853eb65d74c29ef2b7834718eca43&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=5150d2ffe4dd2dd264594926747a00d2df3c14f42ab8432a68e764901e74d7f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=4b7ed50e6a7de14318df2967d9436d9a6766006f0f0e24493471f431e05c6c78&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=c741db71ae31a5117b8b4d9af0190e6c159b3acd7d45396950db12dc6cbe88c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=b52f6c5e142849f6d292942103c3154b685b90b155ca3c833ef2ae17c9b78a43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=1c78909ab277fab041a2d48d018aa87a7f8377a32745ac396deb355963c3c75b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=3ff988ebd087fd1ed1159c34d5adca59a43d8b3109d08f2dd3bffc4963695644&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=abc542f4c1c861bff3d934c9c20c1e07b942a9e9e9b2f97eb99fd0678cd595a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=ce8a713f40591ce6c835939ccd2febc0971a8919135721b59a66556249405a98&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVQ54YH4%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk12D%2BEO2%2BtqPfWDwCVjxOSr%2B8%2FHwVOKz08eoqqNng0AiAt43t22PBP7peAx7kIXeZhwl3OZHnqEUBhC%2BtMDot2NCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMGOQ6mSO79aQ%2Buvk0KtwD97BAPGceTbzgqwntHMCg9DXpd36MkqxGdWJs1Aky8GVmTCfnzZiFmcXaLhLtsLC1eHpoI%2FXHim9hC6cbjSg%2Bnqu%2FO%2ByKFU%2FI1272TUqIMOtQqqLPp2NHbIDegP5wXzLZ0euIHFG%2FhfShKxBK6UR0DKbH02Uc1P4OTadxcYLVeGcIwkAa6jg%2Fb70bmIfAkyS5a2%2B9ICu0bb4GAgkVbCQoTJNWK41cAuP6v%2BkxpYpJxhJ3pG3HS3lWBuDE7gzSaVTLZ9AtTbjVO%2FGtGYYRN62Fr7%2BLxRHc3SRZCa%2ByzG6Qu8gvDDTItdN9OBBMNXWgZRitMqEdbR4bIXhdh2rm2l8uXUxkwz14CP8KuUnvNnjBn1oJxOoUfk5QmH4qzxGaLGOXzUnjH1Ju0%2F2TRCaEsN9VzmJJi5XkJLHzNmYOWBmB4giOBTMros6be9Yw3EZ6%2FdXkI6w%2FZED9IbXht%2BiBCTKfEbduYUYkttpxnC%2Byc6nst39VPxlSxHhEtXXkDoP8IsydDI%2FTip6reXssUyDK58D2Ikdh2%2FrbCkEKdSRqTt6MY37sy0RzDYLVEy6s13kImVpjuEvQZNmpsK4ky%2BBQl1%2B97nSclOs0MVg1D8Rk7hpJ5fWn4YWMHiabZT%2FFCpQwvf%2FXvgY6pgE%2F7t%2Bx38a1GjDtPr%2F69j6CboJ%2F%2B8dajbIwuPW4EA2bd6rotOHeebkR%2F3Z7g6gUyN%2FrxEvn%2B57X0MkZT7JSPRTKipquy%2BGDVdE6UH%2FmHiE%2Fqu46u3eij1UGMwKJF%2BSL%2Bd0rN6a7Bb%2FGoNJi42dRm%2BTII1MFsVm5akpOHW1XPn1wf%2FnGMTsFV9th8t9lundB%2BoKV7V6jsde7eoufxzoQjXWJaUeFeKFP&X-Amz-Signature=dc076b299f02560a766a931b68f0be52ee039ed7c779d56f5b96cc077f634961&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVQ54YH4%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk12D%2BEO2%2BtqPfWDwCVjxOSr%2B8%2FHwVOKz08eoqqNng0AiAt43t22PBP7peAx7kIXeZhwl3OZHnqEUBhC%2BtMDot2NCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMGOQ6mSO79aQ%2Buvk0KtwD97BAPGceTbzgqwntHMCg9DXpd36MkqxGdWJs1Aky8GVmTCfnzZiFmcXaLhLtsLC1eHpoI%2FXHim9hC6cbjSg%2Bnqu%2FO%2ByKFU%2FI1272TUqIMOtQqqLPp2NHbIDegP5wXzLZ0euIHFG%2FhfShKxBK6UR0DKbH02Uc1P4OTadxcYLVeGcIwkAa6jg%2Fb70bmIfAkyS5a2%2B9ICu0bb4GAgkVbCQoTJNWK41cAuP6v%2BkxpYpJxhJ3pG3HS3lWBuDE7gzSaVTLZ9AtTbjVO%2FGtGYYRN62Fr7%2BLxRHc3SRZCa%2ByzG6Qu8gvDDTItdN9OBBMNXWgZRitMqEdbR4bIXhdh2rm2l8uXUxkwz14CP8KuUnvNnjBn1oJxOoUfk5QmH4qzxGaLGOXzUnjH1Ju0%2F2TRCaEsN9VzmJJi5XkJLHzNmYOWBmB4giOBTMros6be9Yw3EZ6%2FdXkI6w%2FZED9IbXht%2BiBCTKfEbduYUYkttpxnC%2Byc6nst39VPxlSxHhEtXXkDoP8IsydDI%2FTip6reXssUyDK58D2Ikdh2%2FrbCkEKdSRqTt6MY37sy0RzDYLVEy6s13kImVpjuEvQZNmpsK4ky%2BBQl1%2B97nSclOs0MVg1D8Rk7hpJ5fWn4YWMHiabZT%2FFCpQwvf%2FXvgY6pgE%2F7t%2Bx38a1GjDtPr%2F69j6CboJ%2F%2B8dajbIwuPW4EA2bd6rotOHeebkR%2F3Z7g6gUyN%2FrxEvn%2B57X0MkZT7JSPRTKipquy%2BGDVdE6UH%2FmHiE%2Fqu46u3eij1UGMwKJF%2BSL%2Bd0rN6a7Bb%2FGoNJi42dRm%2BTII1MFsVm5akpOHW1XPn1wf%2FnGMTsFV9th8t9lundB%2BoKV7V6jsde7eoufxzoQjXWJaUeFeKFP&X-Amz-Signature=546becf1d2871c11bde526da3859f543501ddc3f0c8ec9f3261fe2780a003bd7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVQ54YH4%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk12D%2BEO2%2BtqPfWDwCVjxOSr%2B8%2FHwVOKz08eoqqNng0AiAt43t22PBP7peAx7kIXeZhwl3OZHnqEUBhC%2BtMDot2NCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMGOQ6mSO79aQ%2Buvk0KtwD97BAPGceTbzgqwntHMCg9DXpd36MkqxGdWJs1Aky8GVmTCfnzZiFmcXaLhLtsLC1eHpoI%2FXHim9hC6cbjSg%2Bnqu%2FO%2ByKFU%2FI1272TUqIMOtQqqLPp2NHbIDegP5wXzLZ0euIHFG%2FhfShKxBK6UR0DKbH02Uc1P4OTadxcYLVeGcIwkAa6jg%2Fb70bmIfAkyS5a2%2B9ICu0bb4GAgkVbCQoTJNWK41cAuP6v%2BkxpYpJxhJ3pG3HS3lWBuDE7gzSaVTLZ9AtTbjVO%2FGtGYYRN62Fr7%2BLxRHc3SRZCa%2ByzG6Qu8gvDDTItdN9OBBMNXWgZRitMqEdbR4bIXhdh2rm2l8uXUxkwz14CP8KuUnvNnjBn1oJxOoUfk5QmH4qzxGaLGOXzUnjH1Ju0%2F2TRCaEsN9VzmJJi5XkJLHzNmYOWBmB4giOBTMros6be9Yw3EZ6%2FdXkI6w%2FZED9IbXht%2BiBCTKfEbduYUYkttpxnC%2Byc6nst39VPxlSxHhEtXXkDoP8IsydDI%2FTip6reXssUyDK58D2Ikdh2%2FrbCkEKdSRqTt6MY37sy0RzDYLVEy6s13kImVpjuEvQZNmpsK4ky%2BBQl1%2B97nSclOs0MVg1D8Rk7hpJ5fWn4YWMHiabZT%2FFCpQwvf%2FXvgY6pgE%2F7t%2Bx38a1GjDtPr%2F69j6CboJ%2F%2B8dajbIwuPW4EA2bd6rotOHeebkR%2F3Z7g6gUyN%2FrxEvn%2B57X0MkZT7JSPRTKipquy%2BGDVdE6UH%2FmHiE%2Fqu46u3eij1UGMwKJF%2BSL%2Bd0rN6a7Bb%2FGoNJi42dRm%2BTII1MFsVm5akpOHW1XPn1wf%2FnGMTsFV9th8t9lundB%2BoKV7V6jsde7eoufxzoQjXWJaUeFeKFP&X-Amz-Signature=72e4e21bd9ed363a7499929b4c8b1ff00f1f1644c62148d66684f277f110174a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=dda5d8fab4082b7f1535291dd539374dbaec16212de79cf7a32da46527fe0c12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=93747efb0fb0d8c960c4dc4ce2a327d71a0ec0ff22730c15e3cb33ce31bae573&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=3412aa4ea4a1575b8945249c412dd3fc6017531c0d2f003fe831ca2c0e1d12fa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=9b2ea8d38c40f6ba260095b8349284adb5f36f9f7fcff55abd5c337ce2f945ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=1023c1c3edbe68ce5bde0336342dc077fbf9a51e18a679262965f9a8fa057240&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4D26XB%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6DeXLXaqwX6iSkuzm4wN6Qc8lY7Ghh%2F%2BF2A6wgDfzuAIhALG9h8mxEnhIjM4IPr7eJ3MPaw6l3yVa8aRwkzU2n4DzKv8DCCAQABoMNjM3NDIzMTgzODA1IgxOoWGfG6r5Z2OhvE4q3AP44AejtheKAKZ5u7RJdrCRg4lohJRXaHw6vYOZTedV2LdcRWX38aUCk7uDfLopkcVzNwh57nNbLv68WuWzuPxZhzxwXbTDwEIzDaKkOWsLsRTVwFL5PqMa31ajAuB5qgvqdIJBt80VQPkgRGmVYL09dtm0ccwPXEmLBsYJ8bOoTQY0UVStelWf2YBV4PSvkTs%2BEoAQWZr3uAx%2BRNupCc1JrYejojAhRUTnlomeJ2bOq7%2FrUBFhV9t3TehrTCdhVU9PJNl5f2KsbCXmCraDIiiPy6l%2BDNX%2B6eZMb07yYYmedhBVtGYopeLuMOQNIQvYfPl8QMSn8ilDHJ0cQKqIUgDByXiGO9W26Ji4mCpQtQMNSSmmYrzy75%2BJJ9rd1psmJjqjVOWIRfVw9a3xmCTHUEPhCvk896dkhHfqOFg0XmbdZIplmKc2Z8HT2Lf0KWj6ZBu%2BHFc6%2Bw%2Bfx7cXFeXWl3xHAJB%2Bh3pBiIA91npS2sJQmvw52bHCKSm29WsdTCvaSw5Lzak%2FiicA3hkNihDdlRpydqAXf1KvHd8MBHTCs3t%2FXaq%2F5zKfNqKiisr3ilyyF1V36VfNcAVzVF54pPJwgGyR3SSf4I98T5JiUGF1i7BRvtgE%2FbQT1saT9BUbYzCu%2F9e%2BBjqkAZmDHVDXu8QX7FLe1fJXdOKCDzQB%2F2gl2DgsXuR9UOW7wRVp8ZbAfKqU2lw1pDdKxrebJ9HBRNjmIfPtsM4SpvRr%2BZMtCHKkn6iKpB7S1I2BvFehewNS6cI94FQNINV00FE7Ui0YVy4YVAasakD6YkJhppavlsn8YsMNzDUWwXgmz3ef02NLUGBtIlS1MlY1ZLix1jC0sIT2NjULr1CdePqgANpP&X-Amz-Signature=14a38cc64349ac28c7a3ff31404f5a8f3dddc23ef5fcbf4c0a67d4ac812267f4&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPVSNJUB%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1IxAfklbPaBYZfuCPYIuc2h1J9OtzcGv7nCZN6hA6%2BAiEA%2BvLgjN7TqZ%2FqI6SXuzEJpHVXQom%2FMxbqcwwWoWofshEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDPSxhYzuSxSCy%2BJtxyrcAwm5cfL%2FR6%2F9lJqGV%2By%2B1YFYDMiPeLV5DDW2HrXgeJ1xfuNN0lUReU2sUiHupDbgS7bHcED%2B3tBzuiYbVSt3QlN3uGh5duIiW%2BezrjDofQeqOAHcnfYygCbEL7IJwmHTC8scWyojbsj47qNUW5TEOvbKUtZJrbncnZSvmkkISaMm95Uhl3pzegd%2B45KSTYMwYVjATQChUrNssXxLmIt9KBJjkQBcsAhBWeZe%2BYo9XdmcARA63Bw7xyfAKqhYclG5NHT6tFO5eBUGxiGI8YTQmDTaWD1UC1T0wgYGqtpSMbNW5xrTYeiTxPD0PruP9j9Hfksq2eyZCAvzmolSaIXtHucN93Ukkuqe%2Bc9Km9n47IffEIzCPS82zAeh2L%2BPmRj6U%2FlmRIKZz8RbHFKp6IK%2FVtCzplMRJEeRt%2BPAF%2BaOC9iakd66XtTRRyaH%2FSHLkhHJOaCvcs3QCszqllT0yaHEJfiu2JcLnTVWxubFjWirS6TB8miSLL54Pv%2FdUFjZ3LROhOpPNirWkmjPI6Ww6z3Z4dYJcJE5kEXGhQlnHRwCFZytbVZGLoCYd%2FK%2B788Bbfee5cGreTmqFklENErSGE7S4qusI3c5Yp1ljYX8mMzDL%2FOuppXI7oqVmHnFMr%2FpMLP%2F174GOqUB3X4Q0mhbx5wBXB2iguIGtIy7ZenoMbTXRhjoOBs3gbB7B%2Fwz90BFhyMnAcEXiCX24KgJj8EmrvihbHcJEMKalrHVn4waLIKdsb26SMDeBOV%2Bfdz6eU60ukzqOXT0WEISmfN6piIAS7OQzOkbpzqmtCESBFCUJCbNjeYSicFCXgxGuV3hZfHX95eYaUwWIj24A7iy1KKadUTl1JmMF4KgG37perUL&X-Amz-Signature=3d507d9deeb13b2ed7ff04bb5c7b31450e0b5e0a1bf1630955a608b5b8f92560&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPVSNJUB%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1IxAfklbPaBYZfuCPYIuc2h1J9OtzcGv7nCZN6hA6%2BAiEA%2BvLgjN7TqZ%2FqI6SXuzEJpHVXQom%2FMxbqcwwWoWofshEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDPSxhYzuSxSCy%2BJtxyrcAwm5cfL%2FR6%2F9lJqGV%2By%2B1YFYDMiPeLV5DDW2HrXgeJ1xfuNN0lUReU2sUiHupDbgS7bHcED%2B3tBzuiYbVSt3QlN3uGh5duIiW%2BezrjDofQeqOAHcnfYygCbEL7IJwmHTC8scWyojbsj47qNUW5TEOvbKUtZJrbncnZSvmkkISaMm95Uhl3pzegd%2B45KSTYMwYVjATQChUrNssXxLmIt9KBJjkQBcsAhBWeZe%2BYo9XdmcARA63Bw7xyfAKqhYclG5NHT6tFO5eBUGxiGI8YTQmDTaWD1UC1T0wgYGqtpSMbNW5xrTYeiTxPD0PruP9j9Hfksq2eyZCAvzmolSaIXtHucN93Ukkuqe%2Bc9Km9n47IffEIzCPS82zAeh2L%2BPmRj6U%2FlmRIKZz8RbHFKp6IK%2FVtCzplMRJEeRt%2BPAF%2BaOC9iakd66XtTRRyaH%2FSHLkhHJOaCvcs3QCszqllT0yaHEJfiu2JcLnTVWxubFjWirS6TB8miSLL54Pv%2FdUFjZ3LROhOpPNirWkmjPI6Ww6z3Z4dYJcJE5kEXGhQlnHRwCFZytbVZGLoCYd%2FK%2B788Bbfee5cGreTmqFklENErSGE7S4qusI3c5Yp1ljYX8mMzDL%2FOuppXI7oqVmHnFMr%2FpMLP%2F174GOqUB3X4Q0mhbx5wBXB2iguIGtIy7ZenoMbTXRhjoOBs3gbB7B%2Fwz90BFhyMnAcEXiCX24KgJj8EmrvihbHcJEMKalrHVn4waLIKdsb26SMDeBOV%2Bfdz6eU60ukzqOXT0WEISmfN6piIAS7OQzOkbpzqmtCESBFCUJCbNjeYSicFCXgxGuV3hZfHX95eYaUwWIj24A7iy1KKadUTl1JmMF4KgG37perUL&X-Amz-Signature=87b083f2c512d6e90b584e18d8ebdbcd378de35936fd6749b4dd62f71ac5949a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637BKDBIM%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6lqI5Kj3R9HtphVcOavXfpA7W1YH%2FgkubIvVe6LnVNgIgVRg6i25AgvmWwXTEe2%2FqCSlmV8hAHqZwp5xhCRKEx78q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDKQcAUvZerZbeD%2FX5SrcA5xLJ52%2F8SN1qJmuU9L9Iz5iyKXYdRl8dCrPQdZMqEco%2B0SHa%2B3BIvu518k8TfBYNKhKqM11eSPda4wXaVDwkwWnFgm0kAiZfeNmB1EN7XXg0LzzQ46lz8R1eBB%2BSV94lkuu6fU8RdjetzUc3R4c8WBWkkpI25qot6yY90fQSOktaBXSv4253VzlOAhXLgBwxJTMZ7ksgUQn4yUMSDa%2Fa0n%2Bjz6%2F7p7%2FXQrpjrCoeXSMxtRal9mJGPufZfO9YmFNvGAVq5Qy%2FdfR9Qcp3n49Vy%2FrdYo%2BLb6SBuTjqG5FNM9yo%2FYWY8sMFapX7SFzLfD1kFd9FQMZiumT1UlzJw7hXpa4hWoZkGPQQ4dfoI%2FsLnAqTs8l7xkbjyUIUqaTO3g3pE6RFsmh71SK3AL5y1FaVucimWyx0yMr0%2BksJFT0WKV00uWrwl9hb55xB5LxDv6sRgegVwTI5oNelS7R2p4qv3RecGWaRSs1Is0XxSjNExfr99GjLl5sO516Cl4SVX726Zkve3SiGNO2ZdBLblL%2BVyO94KMDGhex7ZLgNrLnVIyT65c4ArRWW9vdtcGdajGNaXGfTbVxHOBSDepRguusY99NOX2vWKRbcokz00vDRbf3YO6wAVh5AvAfUuSWMJX%2F174GOqUB1E8EUAD%2BBpV9YJUiBANT3EDc%2F5eDsabJULYaduRGm8ep1mqDAxQI77oSX1nx0SXdGeVGue6wGVbT9rADE1xQh5ulFCqRSFUNlGz3RxwzlDu97v3ULUOEvS6VV2uqMXYyC9ACaq%2BAUR%2FeLb%2FLinvCxyZSW%2FePG1iLPf5jEnL5sGQr6lhfrbRda3alVmA2z3IIOhnYALKSQixWJBrowGRSc8Cct2k4&X-Amz-Signature=71b8abf0d31bc2550b26456bb17a854fca939031bd701775e29b7ea0bcebfacb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGUPGMTH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr1H2N4gpV%2B2sYktIY3urvMTqy4Ay6GvGnup4heWc64gIhAIxc%2F9TgzEuiHD4ti1biYjatxRz%2BOj%2FXhJnuVayCa1XwKv8DCCAQABoMNjM3NDIzMTgzODA1IgzmJR6iMk3XGdfGb0Iq3APzs1VPlyZ0poFLiYdUybqljCX5qI%2F7my0YnWNFaf7VdIZ4nDAASjZGDyuAMSxoaZ8WlV%2BzRbjrnyUhfAh0cWfXPnVyGbYH02nxqdy3fNsoR%2Fi1YxwqwhsPV0BLkiMMxHuL2uceLoGtSucBXXRYQ%2Frdi1muzBBxM5g1EJhiT3HGQxZ5n86mvyhl3IpwA3NMfBckoRDzILhDW7lMFxPnogUulUZy%2FpCTvHNdniYG4z9oWNXR9ah9oJ9vD9lwXE5JX%2FXaTlEd0JtDVm84Tw5Q8DgIRaSs87RcvjepZgz0iLsVL88q7n9uau6I0Crwu%2FsDE95o2OhjE%2BnehcnmTZt66opWhhMMT6TAXDYcutg5gjTQRnZUlhNbSeDDNFw95c8n696KSgi5IW8pV5TrJiD9hNRdvI4OD43xArkBR6Inw34z61HbChHcEfHkZbzGHskMqhVHsFFTTtgXb7Bw6EqtueLKPCPmVz3htbIfYGWqSWyjGKOpk4ZPRyQb2eyTPiSbig4W4OSrg4lnAsoSKq6OEl7RXuY1A71FAgvoR494OS2OiZNzZ064VZZHynQmyIp%2BFH1CHej1Mpfaj1QcQ1uvxGSLASGPutGCqaBOpvFBv2aQ3LPdk%2F6nzimuOk2jvzDh%2F9e%2BBjqkAWjPrLQwTrveUmk0srBApBH1nNYCx7BC2dWcUxFh6QzF0fnvQXJhZHfAGmjQokJ%2B2WL84EAZYi1DmS4zfX%2FpD7M1V0ENe7OFBbfhWc1GxzIx78aJN4uW8ij0I7ewKsyOpcY1SbEuoFOv4EFXKA1YUUONk3h16tXMv0NZqrzgf%2B8G8zz8cbaGT9C06e0ycdX3F3Blu9RxDd42M8LC4GvtZEHYW0Tj&X-Amz-Signature=8b858b04f3b0cdad00842235e2e7bc8c98ad738eac7f5b9afe0d63908229f0d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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