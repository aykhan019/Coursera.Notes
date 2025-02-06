

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=6eac1a5a9affccd6f24b74405453fdfdf09168431f5738bd9d8382e49883a841&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=083f838acd2a478ef70cbc7651edaa26f4b8ff1ffc6ae6bd198fb829b8963aea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=1ff3eff340f47ce1b154d668720a6d7516ec0d569dd90ad816d11561f3151a0e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=1de8846397204876dee3a0adbadecda27c26456f34d5ac830c6c33f920b8c51a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=c85bf2af8073171f54d5c4f5aca0d4d73d65f17a0e6229edc428b8e5f1f2895f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=7426e21f6e5dc14709145981b3aa6e99e8d6fc56e2136ccbd9c844d50ea4725f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=16ff2ac847ae4392b2827728a583f0c832b5bdff4eea772b2779ad8ddd184cd4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=97e5dfeb4721bbf6048de35a14f009cae097e4a38d2c79035981917744e5b4ff&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=8fe10ec2095ad849af273e86c3143aa2dd883eb7b5dadd34b68d07c467221bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVDBNNTA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQD3awMPyA4c7FdlFwZr0%2FcO8BifDoq8RxPjHmaKP%2Fh4gAIgbaFczM8CiYnqnGq4DuBMc%2F5N5P4Lu0HJk5wQqwB8xxcq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDGugdC1xMzNKgRhiICrcA3TGKwXlDZuKQ61EfhOoE%2FK6rtxQISW%2BKpKiK6aED%2BqVQtfkokykRMdv%2BXLbjs2mQTieRRCebmVCsA0Fxoke5bQred6X7F2vOFZE4DZRAYMUDq3PE64iNQ3x0EKJDXmQqcKyiPmDjVRsj8XOsRsf7bAklcAMuYzgNj3UJF4U1LtgR0sAKBLDKuUrSKDRTGA0plJAln7mS9A4cEs228cvFzbQmM%2Fl2XzfXtxIjD074did4b2gLJvF9MutZTDbYgafNh0YqnrZ1UPNrK1xqMTNOwQbS1R3ZAAk0lD8Vm8LfC3hp0CZ953iP8mYrFoekCBUVeCKuZ6d%2FKRaZW8Slzj%2BqDLDlXuqeni5F4n6riRR1Wetjlhm%2BW9JWITkD5wCVmHg4mLL7NwkjmPt%2Bm7cdHegnoxov5OY1vn%2FsaeRdmlGj2B%2FdCeEji926PnqY1HPoFgs0riUfyfPT7s6pUlnh56TkTXw1Q32OHVk23i4vmo%2FbINYTJmbqfDwXrloXkX0Jw6Alwgzqy1xQeOGIRWDt5n2xZwvaAsM%2FYSz3zBVgzpMrZaluQvaLQWyYt6DewgQs4NCLtiJruznOc3QNCPw%2BfjVmEA8l8F721pxSEr5hfKOlYIR9zdUp5UsgqlK0g8lMIb8kL0GOqUBKe6UWwHv8zADznMEbxecSCWJL4C5OHefEDTtAtKeK4Ho6J9HZ9CEHO%2BYuXf58xzC%2BF0HWElxRCNL0dglNxFSP9Dds2WytSPLlQPzEhScTPmE8EWtHqVIj0LKv6LbMmuiDvjw4KKjo3SbbD93HrO55wjh08ETMJbytvff8qPnPGseiDSO1eFbBdHqAs9M4d7qcjLGSiT3c3o5S14yHe%2Fb0R%2FcJnuZ&X-Amz-Signature=b5e488575df2912c156a1fc7b02e449c852d5323c1d0dcbe7cdb163acc91a2c4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVDBNNTA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQD3awMPyA4c7FdlFwZr0%2FcO8BifDoq8RxPjHmaKP%2Fh4gAIgbaFczM8CiYnqnGq4DuBMc%2F5N5P4Lu0HJk5wQqwB8xxcq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDGugdC1xMzNKgRhiICrcA3TGKwXlDZuKQ61EfhOoE%2FK6rtxQISW%2BKpKiK6aED%2BqVQtfkokykRMdv%2BXLbjs2mQTieRRCebmVCsA0Fxoke5bQred6X7F2vOFZE4DZRAYMUDq3PE64iNQ3x0EKJDXmQqcKyiPmDjVRsj8XOsRsf7bAklcAMuYzgNj3UJF4U1LtgR0sAKBLDKuUrSKDRTGA0plJAln7mS9A4cEs228cvFzbQmM%2Fl2XzfXtxIjD074did4b2gLJvF9MutZTDbYgafNh0YqnrZ1UPNrK1xqMTNOwQbS1R3ZAAk0lD8Vm8LfC3hp0CZ953iP8mYrFoekCBUVeCKuZ6d%2FKRaZW8Slzj%2BqDLDlXuqeni5F4n6riRR1Wetjlhm%2BW9JWITkD5wCVmHg4mLL7NwkjmPt%2Bm7cdHegnoxov5OY1vn%2FsaeRdmlGj2B%2FdCeEji926PnqY1HPoFgs0riUfyfPT7s6pUlnh56TkTXw1Q32OHVk23i4vmo%2FbINYTJmbqfDwXrloXkX0Jw6Alwgzqy1xQeOGIRWDt5n2xZwvaAsM%2FYSz3zBVgzpMrZaluQvaLQWyYt6DewgQs4NCLtiJruznOc3QNCPw%2BfjVmEA8l8F721pxSEr5hfKOlYIR9zdUp5UsgqlK0g8lMIb8kL0GOqUBKe6UWwHv8zADznMEbxecSCWJL4C5OHefEDTtAtKeK4Ho6J9HZ9CEHO%2BYuXf58xzC%2BF0HWElxRCNL0dglNxFSP9Dds2WytSPLlQPzEhScTPmE8EWtHqVIj0LKv6LbMmuiDvjw4KKjo3SbbD93HrO55wjh08ETMJbytvff8qPnPGseiDSO1eFbBdHqAs9M4d7qcjLGSiT3c3o5S14yHe%2Fb0R%2FcJnuZ&X-Amz-Signature=34475211729d0575e7d73ecb08f2a49b3c85394e45db216dc884bb729a070a09&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVDBNNTA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQD3awMPyA4c7FdlFwZr0%2FcO8BifDoq8RxPjHmaKP%2Fh4gAIgbaFczM8CiYnqnGq4DuBMc%2F5N5P4Lu0HJk5wQqwB8xxcq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDGugdC1xMzNKgRhiICrcA3TGKwXlDZuKQ61EfhOoE%2FK6rtxQISW%2BKpKiK6aED%2BqVQtfkokykRMdv%2BXLbjs2mQTieRRCebmVCsA0Fxoke5bQred6X7F2vOFZE4DZRAYMUDq3PE64iNQ3x0EKJDXmQqcKyiPmDjVRsj8XOsRsf7bAklcAMuYzgNj3UJF4U1LtgR0sAKBLDKuUrSKDRTGA0plJAln7mS9A4cEs228cvFzbQmM%2Fl2XzfXtxIjD074did4b2gLJvF9MutZTDbYgafNh0YqnrZ1UPNrK1xqMTNOwQbS1R3ZAAk0lD8Vm8LfC3hp0CZ953iP8mYrFoekCBUVeCKuZ6d%2FKRaZW8Slzj%2BqDLDlXuqeni5F4n6riRR1Wetjlhm%2BW9JWITkD5wCVmHg4mLL7NwkjmPt%2Bm7cdHegnoxov5OY1vn%2FsaeRdmlGj2B%2FdCeEji926PnqY1HPoFgs0riUfyfPT7s6pUlnh56TkTXw1Q32OHVk23i4vmo%2FbINYTJmbqfDwXrloXkX0Jw6Alwgzqy1xQeOGIRWDt5n2xZwvaAsM%2FYSz3zBVgzpMrZaluQvaLQWyYt6DewgQs4NCLtiJruznOc3QNCPw%2BfjVmEA8l8F721pxSEr5hfKOlYIR9zdUp5UsgqlK0g8lMIb8kL0GOqUBKe6UWwHv8zADznMEbxecSCWJL4C5OHefEDTtAtKeK4Ho6J9HZ9CEHO%2BYuXf58xzC%2BF0HWElxRCNL0dglNxFSP9Dds2WytSPLlQPzEhScTPmE8EWtHqVIj0LKv6LbMmuiDvjw4KKjo3SbbD93HrO55wjh08ETMJbytvff8qPnPGseiDSO1eFbBdHqAs9M4d7qcjLGSiT3c3o5S14yHe%2Fb0R%2FcJnuZ&X-Amz-Signature=2cb3c4809f0786a0a985feb5267c224391fed2ba04749cef59a7fae1095b32b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=50aff1523dd44a61f7cee85f8ce67347e192cf28b5056c9d55f3036b6a8f1003&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=c5a43cc2133cbff4bb0b564c6c8eb7fa6846cb373ce9ac4b8791547ac3531ac2&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=382e1838da30277713655000a9e6057b1294dad2fbbc39bbccecf1dd678b9cd2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=d70933db48c82d32c7dbc5412b2dabf34e9f785bb09920e38862af6f9b4c94aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=2b42d0a449775ee45b07a7fb372695714a92b8fcfb18c4c0af67786c6a86796b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R343LIME%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQCIxxKw4RBsVPSmD5%2BSL1yjATPj%2FZBrMOjYCEiWicmBOgIgI8GRQj5fnTGepP2BVOcL7ikbA6V9c4YcNIDFFUcZXsoq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPJoQOeeBLTioD8BDCrcA7eO4eIIRbuBf54nnt8BsXMwSNayZzWG8auDwLtgPcUSp0F%2BTyOh5OOE7%2Bb3mqHvdAc73vT6CfEu368BWQ0PwwWWtbIGP71%2BYUogXmVdjHz%2BPOFUK4Ao%2BELcm5ClZ%2FBIYv0dkeRNMKcm3PbB9IyQw5VSsCxdveP4REh0dDngxF8bnZqe3WpNIme2WrWhtDJQpqpSNS2T9By37VZFScDlVN2TqkiVLqn7%2BmTbHfa%2F9v5gSfWGo0NyFVonIUCzZotFnq3wf8Gc7SoSEcTS8uli5F9zMqrl58Tq2SYvdS05lheFbQ%2B4ZlmManV6VBdjdYxABB6D9ZAJYk12NGOwXV3hFyMb8OHqx4fPf0VqANaNxLWa25vpyFCchDOmJc%2BnXj%2Fkki%2FJhF7EQQ%2FK8D3aJM8i%2ByTuYbQs9njWKkSpKdYqIzECpkUrdAHe0AJJ26G5AFRywPtea7dt1n%2FPf16TLcdF4lAFdssh7PgwD5QtpxlRNtqK1eiZ4t7nUwpk8BkPudljVuenKcMWcg1pev5MXZaERNYvQE%2F62CDKb2irBgLE52MuZQg7AcZr8Dnxpcvg2X2lkOAh%2FD02idOBhcadl3MPNP9v4JbB2lL0xGdBwmvxAl%2BE4dIhSuIKbXv4N5BEMO37kL0GOqUBCshYva1zkmyO7wBj0hDQDGTxjP2Z1aKSB8ufPH9owkkp%2B9rFkmQ2DTZYBvD%2Fc7ycTsYr2Ta1fSWLvaiFx8rsiwyrSNSK%2Fs38R%2BQxksLCZg64eHXrMtZnoKx38ArUodzCbkIuvlcYS9RVO7mwZQXWcCZqBQPR5EVmhezQAnCHq2FmcX%2FaiPpSElGW0BrAREWzp0Y6JmyL6qo5ER0cdZQ4ItAvsRKF&X-Amz-Signature=806241714744e61ff0033164a893dbb73b95bd08b9347f2a8b718b392a5c05ac&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF222DOR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQCV2%2FkEIydA3w7jioUskWWt3qluLoFxAMyWXgZzjPEFPAIhAOAqE6m%2Fy%2Fn8YqZMbgeehepNU9n5Q0EGMmIaIbb3TJreKv8DCFYQABoMNjM3NDIzMTgzODA1IgzmY%2BR330TJEoC4RxIq3AN0RtAbqEOrgeg8svQ1sVsjrLhrIFgf8y4QJVwcZySAJLGgnMXHlnROJUtwfL61KRJJEWkiA7qeG1wz2SPBWD8jykja0NTxldX5hB8biKn0qVdb1L6L22OPumFyr0opzhwVuf9zZduuq7UvcAjsJx5ceCJaE3rrTxRigQzDurfGeoY5MFcc9npDelG0L15b0UV%2FztvA6leThEkGPbWgWXgS0C%2FvEScYUMBfAjIflfaajXSGy9VsP3d%2Bw%2F8pU1hVnl6sF2OdRTGfSaV%2BdVE5gHLBRA2JZtoLT2ir9VIV8DRY54243Xgr80rghJN554IMcbjSJn6a85%2Bv7l5MhgILpOpGdx1Ejk%2BkZeKP6TytJQR8aiw6yydU4LxUfDRz%2FpmQDLtNAA4Z6bPfyrHe6MZA4U8fD%2FnyVdaokRuZk%2FhxgSiqa7KCh2yDm4CtdmRwhYNqMGCq%2BygDSRS2INwQOiRz7C1vwr3N%2BXpZ3nl3hyskxix94FZWQ9CoXV%2Bd9H6QMrWoCHBRppJ0%2Fj5VKmSgtYZFJ9AIe5Gei54%2FtkF5NuYUvJW0%2F7biwdlvsSmtXzJCNQvhvj3uPQJqDvjJYbggWt%2FJERvLzDE9fWueh%2FwVHv2yP4THX%2BDZ7%2F3ZnDf%2F7TYPwzDw%2B5C9BjqkAZTiRszucf8s80VeuuhVIuRny0JxfMTbMfMjkDDelqIoZQozitHbYCqWJ4HY2dvBDUd4xKSKpfvYuEixwOozD5ivi2eh2ohehLDOJtSEx0En3%2FcA9%2Bzsl1ruw7ElSGz5p5mQc%2F52kHShx4WNTqK4FV6W%2BtMKwaVUB9Pfjn%2F3TT9%2B6oXf%2FMllPhgN01yyObFPKi668wtchQwhsmKp%2F5eSO4Qn8hmB&X-Amz-Signature=614612282a30ad49d2efabd347783aa00e2db1a2c601aa33cda443029a423eab&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF222DOR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQCV2%2FkEIydA3w7jioUskWWt3qluLoFxAMyWXgZzjPEFPAIhAOAqE6m%2Fy%2Fn8YqZMbgeehepNU9n5Q0EGMmIaIbb3TJreKv8DCFYQABoMNjM3NDIzMTgzODA1IgzmY%2BR330TJEoC4RxIq3AN0RtAbqEOrgeg8svQ1sVsjrLhrIFgf8y4QJVwcZySAJLGgnMXHlnROJUtwfL61KRJJEWkiA7qeG1wz2SPBWD8jykja0NTxldX5hB8biKn0qVdb1L6L22OPumFyr0opzhwVuf9zZduuq7UvcAjsJx5ceCJaE3rrTxRigQzDurfGeoY5MFcc9npDelG0L15b0UV%2FztvA6leThEkGPbWgWXgS0C%2FvEScYUMBfAjIflfaajXSGy9VsP3d%2Bw%2F8pU1hVnl6sF2OdRTGfSaV%2BdVE5gHLBRA2JZtoLT2ir9VIV8DRY54243Xgr80rghJN554IMcbjSJn6a85%2Bv7l5MhgILpOpGdx1Ejk%2BkZeKP6TytJQR8aiw6yydU4LxUfDRz%2FpmQDLtNAA4Z6bPfyrHe6MZA4U8fD%2FnyVdaokRuZk%2FhxgSiqa7KCh2yDm4CtdmRwhYNqMGCq%2BygDSRS2INwQOiRz7C1vwr3N%2BXpZ3nl3hyskxix94FZWQ9CoXV%2Bd9H6QMrWoCHBRppJ0%2Fj5VKmSgtYZFJ9AIe5Gei54%2FtkF5NuYUvJW0%2F7biwdlvsSmtXzJCNQvhvj3uPQJqDvjJYbggWt%2FJERvLzDE9fWueh%2FwVHv2yP4THX%2BDZ7%2F3ZnDf%2F7TYPwzDw%2B5C9BjqkAZTiRszucf8s80VeuuhVIuRny0JxfMTbMfMjkDDelqIoZQozitHbYCqWJ4HY2dvBDUd4xKSKpfvYuEixwOozD5ivi2eh2ohehLDOJtSEx0En3%2FcA9%2Bzsl1ruw7ElSGz5p5mQc%2F52kHShx4WNTqK4FV6W%2BtMKwaVUB9Pfjn%2F3TT9%2B6oXf%2FMllPhgN01yyObFPKi668wtchQwhsmKp%2F5eSO4Qn8hmB&X-Amz-Signature=905eb5c022cf5ba44c1c7f92455330023ede8f23ec2964f91d42c5ed5c13185d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZWJXUKS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEKaZ%2F7tvS0Ltsi%2B3gMwy%2FjWly%2FiNHzlpDrfiR0xXSKhAiEAhcagh3ZOSob50LfbyEGJJJEJ879cqoNqD5Y6zWMx4cMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPV9DMTbqoPY%2FFk2AyrcA2X0NdS6DWqTw%2Ba1Z6WiWdorHb5GgDb8UvpM4tfs6EaFty9NI5ux9F3gYTE%2BzNedG9%2FUv5PXF6YENjeh2w0yypPCkGIBanzaEslavKiB57ah%2FTFH7b%2F2yjC8oJy6rDF%2FCOd5O%2B4KJBKe9zOTCfBVo3CDJDxG6BLk3BHyoSnQuOL3zq%2FiJvbwY9hZNSz%2FBtU3rmqC6t0phM7LX1uIPDe3tg8ml%2BL3VUE4hK5wN1ZUu3dMijVFXCnt8o31q%2B36QxIWrbYFjqAqfabN2WNWYs5A8s5IdUGLlwtSl44IFXe1Ocfv5MYN9iEi%2BK4hh65flkInkpLPxUOnLc89eYDvOWNGIkj%2Fgj15i4Zo956v2x%2FE9dkIMbHr%2F8VtGoLUMPTxBOQf0EaH45aYmZDbg4WqhlO1v8PMmGAU%2Fl3jrINqcbGo3OwcHd8r%2BuIlv04psbKPQfa270%2Fe%2Bv5IyE6peCG7bieQVjqqkzHamPl8%2FRMFI6sXBdLB%2FRBfT0a3aDt56LyJJ91aCSHrgg4APMlW3Ba5X4%2Bc4U0keEoshYL%2Ba6%2BDdSA2oldk3bDJQdxveueQOy11KiEm2c4249%2BgVXQIJkcmfx8rTJZLE2kY7c7bC1coSoxeuFf78hG1MOcTWopMbhBrMJD8kL0GOqUB5n3i39OwcZI6QFvBTDSMdVuAZzkVsTcjZ934cLPAJIqElUDdEPqxojDMbPfKv%2BdrjC1qkOgeq8DTZOpDIQqrex19ruL%2BTX3bZLwIGXh8psImF%2BY68agyjCdZVgbVsSI9iVBfgImcvx9aVbFWGSJZLuQjcVNYM7PtqrYxIjEgWi2ZgOs3elS3auB0GNEXHCSHzxV%2BYRI%2F2%2FtxpiaStvpBGTFBe6py&X-Amz-Signature=749b148a2986eba5edf3f13e85ff4af831e9d2f4782a89bc15827845cd9df141&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FGKF3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFHr7RbOM7w7XBHpSBh3WtdGz71upwTqEeyRHB5u%2BorwAiAkH4d3ERCTNY2es5NRjvHUT783Kq24to0OLEh5DxerCyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM16NL7YKYdrEaV%2FNgKtwDUwuw5l7cZTdLtgrshG2yWHVxJkQPdMfqv1StgU63m98JmImndjrQT%2BA3bE5Z%2BWQzLOc71H4%2FDdkON4gLfidnqXhtlpJw89crIuxt2FL%2F%2F140%2BYTM4fVQtWYJ1Kpvt6jXF3HkaR9xHzYEZ%2FdyfMvuEShURVghz1m%2BPXvCQ0Gn6OqVk8ReI0E1hnXNpcKcYcnOFHCuj5Tlh8Tv09CKRLF5GWzsARjMvb3qiNZM18%2FxMW%2BwtYvzFlefNoywSkNwblfA6EEisNccRYJQA8jarTd%2FzABLU5WYwOfZ04x%2Fgxi4QQ7lBBEDdAhQLP7zf1GQd9qHxHrLcHrkhS3xkce03ul2ByZNTF8NWCCarf%2F9nBLMiY2GCt3peZQAULBo1jBq8hKRAp9lPJQr1MtULLekEE5t9N7Ur9iRtOWT1im8jRSbrY28BaMKERkfLHZk8RROzQybZ3qPqW0tAIVITDc%2BTESAazNVYgQy1q0vUdfcWgoNVTLl%2Bu8rCpg1LUAzpRsnrGakJ1Z9%2BGK5WUaaPf%2FdsMaMKAfW78ARv2U3iWuf%2Bb2qEPZje4bWW%2FXUYZ%2BGP1R8WL8DrCf5pEZOp89xllR9E5CycdASF0pPChhjDfT%2BkeqLzCVFZ4Okb49Xr2TDAsIw%2BfuQvQY6pgG%2Fdh8j2d16QBO7iWtnPw1qftBikHJFXxMdIs8tBdNaz%2F20SYjXuliBmfIDNhw5ITeb5bo08DXUHs3J9IDsF4jvElaHRMUoppfBdOOWYa5RA4raQKSQubyResoFaDIApOgC4djbrN2AGBKK03zL2RSl3ig0uWpr%2FBaL36puNfo%2B8aEZ0F9OMfbAsD1bbG%2BweCm07%2FCGvCMLKrIobd52xt7Ekq%2Fc2Ov5&X-Amz-Signature=918d13682108f5c3a4736376ecc9b692f629325eb7dd7caadf02872f2b579eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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