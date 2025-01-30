

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=5d2e6572dfde2c0df3e9855ad938adf4d1470b0e8088745bf1d6be790dac7af5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=83c991c13c9ca220c9f8e44d61e461a5a7316d5f5f352ad24b0f2d5a5957f8d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=ed1a1de5f46e7663b44b9f46291f2e40b97116bb58d561efd145b9e0c9835cc5&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=fb9899b2e4435324872fd22110a8262c570c1112dff9effe02e63c6b18cf1878&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=912302bc7423e8183e7717e88b610096c1f1fc14fcb1cea7632b2397bc0564cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=182a9b44708bedc0e94b65d5839a0360442dccd457fa0c032cee38ab28899f5b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=94fae5fdb893ae77544dcd745cf318823b0a17b053ec636984c4f4512e83d820&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=638bf75dd7d91f71a68c7fbad7bed546db3a3796e952126b285f5a94e642d670&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=7e855c1e6c779760a77d1ab0bcef1b1196dc6d12c20fb814a9b2d10dc149d874&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S7HG2HV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxnxfC%2Bg7HmlLk0HiCSCT7l7iwnqbN3FiqUIvg2V4LvAIgZeH%2BzS%2FfaZqAfGRq2vw6EAzA1%2Fo4zz9HKfgP2h8QWIsqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjIlCcpDHadsBOaJCrcA%2FU8wfoL3wkdIGBI%2FaPYFH5s2Sw3lMCNobqcRzqZfLuwfM0okAzS8Mq4G0DO5t8DgaoikFKZOmzrXnPF61a6gCEejkB1E3R3%2FG0VTarMHjBg0YZSxx72vq%2BkWaNa85nXfInk%2B6UYrezYd1T%2F5NROj%2BB31W5R8BSsB6sM1Rcv8knxKu7W0KMHHoYH0CKEaWStYrvzYUGnwO8kmLcA7aCqyHKpA2hisRQVRo0W5CdrabNuDt2cvu8bZ70iWfat%2F3MP5j4LQKRDy45ydG0Dg3zctvJ0EO9h9NEzCuyHqUbBsnpvCuT2hLLXVshDoM4K5648A2%2BetIZCk90AqB6nAQdFg0NX1FWEHcuzJt4kHCdQ%2BBpjv%2BLY%2BnHHKupfhAvgzroNXgVwiJh4y%2Bqq5Q4pHyQyxjHYvBrIORGHh8hC4ZgwKA%2F01t2LOrM8qUntYx17NABTxP5SBcg0jmSDkoZXA4hGqPzqx70sDiF%2BCZqTuCRZVtvpxL5OwzaJ2AzeG8uidB7nqsdsiZI3J1jMZiGqEKsC4lbyf87PYc6pHlfTnr4dffpRdCazr3pMhvpIOXSXCktVnRIRs0VEOiJ6Y1p3Ws3iQE5WeKvw68VfJvuOtK4tTWo%2Bdys6BRhLrkf1dVGnMMqo7bwGOqUBs7DleOtwnoz8GqoniU9JLMOxQYj0mnKvutgfiiQ5bHwky%2FAJhyTOYbi%2FyXFM8SrcdziLRLRCa2i5Q3aZK3ejyESEj5QHEkOVY4xH0vhsLfx%2BDcpn6c1OGcrIwlBNxudCDKwVqKlxBt%2BZF%2BNgdzm71qscNQgkg5nN2nPPpA4z2d7zBbsGeTNS2Lsgp6fieyQQLNPvv%2F31907SSq75kORkgS%2FbsIQX&X-Amz-Signature=172a8d7453ef83774306906c310343275f4ddce12536982333b2fda7b90b6ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S7HG2HV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxnxfC%2Bg7HmlLk0HiCSCT7l7iwnqbN3FiqUIvg2V4LvAIgZeH%2BzS%2FfaZqAfGRq2vw6EAzA1%2Fo4zz9HKfgP2h8QWIsqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjIlCcpDHadsBOaJCrcA%2FU8wfoL3wkdIGBI%2FaPYFH5s2Sw3lMCNobqcRzqZfLuwfM0okAzS8Mq4G0DO5t8DgaoikFKZOmzrXnPF61a6gCEejkB1E3R3%2FG0VTarMHjBg0YZSxx72vq%2BkWaNa85nXfInk%2B6UYrezYd1T%2F5NROj%2BB31W5R8BSsB6sM1Rcv8knxKu7W0KMHHoYH0CKEaWStYrvzYUGnwO8kmLcA7aCqyHKpA2hisRQVRo0W5CdrabNuDt2cvu8bZ70iWfat%2F3MP5j4LQKRDy45ydG0Dg3zctvJ0EO9h9NEzCuyHqUbBsnpvCuT2hLLXVshDoM4K5648A2%2BetIZCk90AqB6nAQdFg0NX1FWEHcuzJt4kHCdQ%2BBpjv%2BLY%2BnHHKupfhAvgzroNXgVwiJh4y%2Bqq5Q4pHyQyxjHYvBrIORGHh8hC4ZgwKA%2F01t2LOrM8qUntYx17NABTxP5SBcg0jmSDkoZXA4hGqPzqx70sDiF%2BCZqTuCRZVtvpxL5OwzaJ2AzeG8uidB7nqsdsiZI3J1jMZiGqEKsC4lbyf87PYc6pHlfTnr4dffpRdCazr3pMhvpIOXSXCktVnRIRs0VEOiJ6Y1p3Ws3iQE5WeKvw68VfJvuOtK4tTWo%2Bdys6BRhLrkf1dVGnMMqo7bwGOqUBs7DleOtwnoz8GqoniU9JLMOxQYj0mnKvutgfiiQ5bHwky%2FAJhyTOYbi%2FyXFM8SrcdziLRLRCa2i5Q3aZK3ejyESEj5QHEkOVY4xH0vhsLfx%2BDcpn6c1OGcrIwlBNxudCDKwVqKlxBt%2BZF%2BNgdzm71qscNQgkg5nN2nPPpA4z2d7zBbsGeTNS2Lsgp6fieyQQLNPvv%2F31907SSq75kORkgS%2FbsIQX&X-Amz-Signature=6c5aea949a1daf8b18c73422ebe9707f67f76a1e1a5b3d42cb79242b6547c937&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S7HG2HV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxnxfC%2Bg7HmlLk0HiCSCT7l7iwnqbN3FiqUIvg2V4LvAIgZeH%2BzS%2FfaZqAfGRq2vw6EAzA1%2Fo4zz9HKfgP2h8QWIsqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjIlCcpDHadsBOaJCrcA%2FU8wfoL3wkdIGBI%2FaPYFH5s2Sw3lMCNobqcRzqZfLuwfM0okAzS8Mq4G0DO5t8DgaoikFKZOmzrXnPF61a6gCEejkB1E3R3%2FG0VTarMHjBg0YZSxx72vq%2BkWaNa85nXfInk%2B6UYrezYd1T%2F5NROj%2BB31W5R8BSsB6sM1Rcv8knxKu7W0KMHHoYH0CKEaWStYrvzYUGnwO8kmLcA7aCqyHKpA2hisRQVRo0W5CdrabNuDt2cvu8bZ70iWfat%2F3MP5j4LQKRDy45ydG0Dg3zctvJ0EO9h9NEzCuyHqUbBsnpvCuT2hLLXVshDoM4K5648A2%2BetIZCk90AqB6nAQdFg0NX1FWEHcuzJt4kHCdQ%2BBpjv%2BLY%2BnHHKupfhAvgzroNXgVwiJh4y%2Bqq5Q4pHyQyxjHYvBrIORGHh8hC4ZgwKA%2F01t2LOrM8qUntYx17NABTxP5SBcg0jmSDkoZXA4hGqPzqx70sDiF%2BCZqTuCRZVtvpxL5OwzaJ2AzeG8uidB7nqsdsiZI3J1jMZiGqEKsC4lbyf87PYc6pHlfTnr4dffpRdCazr3pMhvpIOXSXCktVnRIRs0VEOiJ6Y1p3Ws3iQE5WeKvw68VfJvuOtK4tTWo%2Bdys6BRhLrkf1dVGnMMqo7bwGOqUBs7DleOtwnoz8GqoniU9JLMOxQYj0mnKvutgfiiQ5bHwky%2FAJhyTOYbi%2FyXFM8SrcdziLRLRCa2i5Q3aZK3ejyESEj5QHEkOVY4xH0vhsLfx%2BDcpn6c1OGcrIwlBNxudCDKwVqKlxBt%2BZF%2BNgdzm71qscNQgkg5nN2nPPpA4z2d7zBbsGeTNS2Lsgp6fieyQQLNPvv%2F31907SSq75kORkgS%2FbsIQX&X-Amz-Signature=3d0401afbc3104b08f0a69f5bcd582f8687434f433722e14b8809ecf81eaae45&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=1f25b628fb50a208040b02e269e8df3eb7fae6d7e312c2c9639b2f3d3f50d4fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=51bdf03686297e13d4ec7d924286f7e3bb895d08d9cc311853c1e64434480b8a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=85339eae2005c84a78b7d6cfa2933f2fb95032e44540259919ef303bf699e974&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=be31c99afcad57e5719ebdd41ef67053dfbc9a4d8a4fda8f7e39a35464861585&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=cd7c97390f12dc65fef4fb5b664e222eec39fcbc534c43a582785b9c1afdcd58&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NSIFMHB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDpcSufow1IzOmpsWwFFSKLAvjkd1UnlV1%2F4CJ4OR%2FjsAiEA8fCHyvuFTP01i7sq60hIwrywrziJeybMTfADmeJR1hgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvJxdPCHM22a4F7SCrcAwoPGHEGoGmRWqK8Yi3k2N8SXsZ7Wjtx79IjEUHtkMtOqE4jNKNL6CQ65Uq9dBr32qT65gS3iseY8nkdthGrcSl90bIz79xivkGVVDdS923gFimjv1iMgNTGaT3FJa0ywBzRGBWKjvA2C1oPAsp%2FW4OhUaNpYxbGKTZ%2BJSgeWQV9iEiZ2yxNFFaCSsgAVqpGKKggAz2%2B5bgMfLf%2FbHUCJame62fqITzDFyUo6UL5c%2FXgk3eN3G1LosxF5z6FvcMCQWeyz1A%2BVto4WghOfUCoIfZ9ceZw2u1RkIidX1W6yFAdKYiJmuhiUML4OLYIrrMKHQ5CqlDePlrlP5kqp9f1eBvy8VGucVjmy8xybkmeqjvUZP0y0FUgxv5cEEMamE3Dli4uL0ge0nnbeFXVzBgI7f25ALr6UWum19uIFsdGoX6Gj5HZwbDMNL6mBjbykuAp2W%2B7kBGkJ3dRyXWBQWh7HWKVnP8r73AFtkK2Tv7uQf1cFAw1Zev5IGTt4tVdT5agud00LXYrJQ3YMbknWqYSCT%2F2E0V4HhF405DHjI4Vvfp%2FOhIZDDUqSEAa3phv56HyZR2EU9YQ0y7%2F0N1Yxm%2FmCHhXSh0c8po6JZA8fb6QUGLkMQ3mEaOzdEekAi12MKyo7bwGOqUBtpkByp5ZhqxRxW0mda2DC3fLJNTuZR%2FYyPU8ipsoDIA%2Buj92n99pAKGfRZFpPFLmoNRNWuYgkT8wovcTy1WKnb%2FThFROuvOhv4AylnN75YFVM053YYMgzA25EnQP7WxgeCm4QS6lYl02TIAkHZ2SwWwyegh9%2FnKdFG65c6HSIohGQSNApWZOqLECVsciGuO4%2B4NHPGoR7y9qZux9i2Jj7HEALzaI&X-Amz-Signature=73ca22146795b1b97c0e8c3143a002caa539d18fc5d35234b7b81c388f0a3ff9&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK25BUTL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCa5hSaBXKcJq5iMwhMgfEOTT9y35uzTl0wUYy9P4MWyQIhAKy6EnJNrjkM9vrIinWKYxEPwU0D7feefizHABTNxs7LKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJkrHrU0Y1LwUrJEIq3AP7NUNyhey%2FB8cCyy6GufyrJGW%2F2XUvUSbmg6tzn0q%2BH5I2LRmUmTgWfgBPP8mdx7uf%2F7FJ7z%2FLpEgrMliOCDHTFSo9kn11m29D38Ij%2FNu%2BjTcsNtj1sjYGWpUkWHN5%2FNRQecusGjMF1edYT5FCYSbewwx%2Bnih971mTpnw4FMecx8LL1avwE4d3g7RXc6VaPJQEyQ%2BRsGQ4N8MT%2Bh0JlB8YtWUJt%2FzmzfkSiA5yuheLQ67DGH%2Fem%2BVf1sAqPBiAy%2FO1NV3BlSzhDBBOfKyjOtPTCqA97sD5SXngTOePLXKlJ3sej9AxWIKKFk%2BIdmUycz9PDDdgY8BSlk%2BGLx1r6tb1XZw8Iu%2FjRr0W5HE9yqW02kpEasr8AppgWl146yDofRTgmEg%2B82J2NHJPsULfSyZfYdjAqT0d08UEa338yINrkR%2Bk25FLstCLKl9IIsICWSGJfhMuk%2Blzk1wq0pjyujkIGjkoCefRHmfaSWDQ1hPNHApAdP5oNeeKisBBoo2oMLFmkuDVfDAmdiJqO%2FibjIa6UOqTInxjaueyUMYZ1K3VI%2FpsFRdXXcuj7iYPRPk69bhIKdx5FhHds0y14YDQ3E%2FfkCf5Hxm6NEc3iMEtPXw7Oh9h4eu39MhbSYoUvjCLqu28BjqkAWJOIdMsbIbyE6QVUKChkJyl15IvJCTtsAQhBsBy7rqA6ZCIQZRY9yemN9hCPQ3Z2OLeBtyAucvL2OEVe3lhhD9DdQoycJFjQ%2BT%2B6CXF9eJToP5oZszY4q8zu9OhkvHzy%2Fa4AOlXLRHsd6hYUh5MkrQsza58HfKcuPa3GYEhwGyp%2FNajQ2IthcsToid%2FvTR%2BvHby%2BA6ro%2BpmpWZViXcAnUp%2FxHT2&X-Amz-Signature=d4288772ed5372caafe82361a4bf0d8bd10161e94748edbad3e3c0fa0b9c7a0e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK25BUTL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCa5hSaBXKcJq5iMwhMgfEOTT9y35uzTl0wUYy9P4MWyQIhAKy6EnJNrjkM9vrIinWKYxEPwU0D7feefizHABTNxs7LKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJkrHrU0Y1LwUrJEIq3AP7NUNyhey%2FB8cCyy6GufyrJGW%2F2XUvUSbmg6tzn0q%2BH5I2LRmUmTgWfgBPP8mdx7uf%2F7FJ7z%2FLpEgrMliOCDHTFSo9kn11m29D38Ij%2FNu%2BjTcsNtj1sjYGWpUkWHN5%2FNRQecusGjMF1edYT5FCYSbewwx%2Bnih971mTpnw4FMecx8LL1avwE4d3g7RXc6VaPJQEyQ%2BRsGQ4N8MT%2Bh0JlB8YtWUJt%2FzmzfkSiA5yuheLQ67DGH%2Fem%2BVf1sAqPBiAy%2FO1NV3BlSzhDBBOfKyjOtPTCqA97sD5SXngTOePLXKlJ3sej9AxWIKKFk%2BIdmUycz9PDDdgY8BSlk%2BGLx1r6tb1XZw8Iu%2FjRr0W5HE9yqW02kpEasr8AppgWl146yDofRTgmEg%2B82J2NHJPsULfSyZfYdjAqT0d08UEa338yINrkR%2Bk25FLstCLKl9IIsICWSGJfhMuk%2Blzk1wq0pjyujkIGjkoCefRHmfaSWDQ1hPNHApAdP5oNeeKisBBoo2oMLFmkuDVfDAmdiJqO%2FibjIa6UOqTInxjaueyUMYZ1K3VI%2FpsFRdXXcuj7iYPRPk69bhIKdx5FhHds0y14YDQ3E%2FfkCf5Hxm6NEc3iMEtPXw7Oh9h4eu39MhbSYoUvjCLqu28BjqkAWJOIdMsbIbyE6QVUKChkJyl15IvJCTtsAQhBsBy7rqA6ZCIQZRY9yemN9hCPQ3Z2OLeBtyAucvL2OEVe3lhhD9DdQoycJFjQ%2BT%2B6CXF9eJToP5oZszY4q8zu9OhkvHzy%2Fa4AOlXLRHsd6hYUh5MkrQsza58HfKcuPa3GYEhwGyp%2FNajQ2IthcsToid%2FvTR%2BvHby%2BA6ro%2BpmpWZViXcAnUp%2FxHT2&X-Amz-Signature=b115d464a78f5f8545d57e4d8ffbe4af9ab9c31fae3875952e93252ecffd8ddb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGRDJENH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzXh3C9sK%2B%2FmJDr4KKnAgYgXriUJjN%2BqrBzSZRLizpzAIhAN0TIspOoDvxnuAs%2FOIDFGith0XR%2BCClIyyoDMyC8cPYKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwap2VwvHk17qhogBUq3AP0nlItP%2B5HSX%2BE3gARAiQd7WpqaleanvYdiYf6nintEB3moMtqsvar3v9n0fmRb96vwn7mPSh%2BcLuLpqzw8uhG2xyF2%2BKcbZPAX2LeNKWXRk%2FF1QZ7LXkK%2F2Oop5GSJwj3LR4LYSiT0%2Bufy3tITBQwknE4ipXl2ce%2FIpHF3F9qQIr3oVZXsi6BgwT1nXNHkElJw%2FpaOn2%2Bp1XW%2FLggj4d7znIqerrgqCKD2HWTqqCFVewgn%2BRmYbDlt7ABmt0ewMDZsuP4t6bPEV%2F0RMC1eSJbISJ5YGGM7f2HJJxm6tlh3FLtyVI29EsDrpvROJwxA5tImeMKtT%2FoIeCK%2FYg5HQllJ%2BZ7FzZfdh6VjUE0hmIgAbdh1vrEk6yHkYMMX7BSYv1CR%2B%2BhZrLVCte5803V9M2tF1R90AFAb%2BhoSzaCA4m03ZCdZQXownBoDzHaBMmROq2ltvpMPhMJhQRkwVWkhiBayP3lZQ2xeJ8e%2BA9aJ2IweTTujbOYzQTFgMC8u9tdhupJ9YTjaGGBrc02Fa3vJdijJp4WHO0z2MRTRDfjyP%2BcErt83jf0NQdHdm9t5g6sU6mwoM6ROba9KycB%2BRnS%2BwzXEdvJxKluWiV440XnJI7V%2FE9th4QOuBiGIsd5XDDRqu28BjqkASPb5JORLIoL77VInz%2Bq%2FezunbJHjMQubM8w7lLkCGW7DfakJqdNgmtixB0pEZHQ8db3qnrFgs1pOdSYotHSC%2FUROi1oxXCXDXXQg2pzaSKUhtdQEcQNsQIugfpJCJJEg4vio7fFhwZF%2BP15Za26pE2zvP0LQghCcTSVmBJGAXggsAoVbBSXOTkIesfBT4P81ztQqx0j6rpA2tZl9TM0dw22QSng&X-Amz-Signature=808cc2b59d40e1533ca9af4ef25fb6d71017f8aa049113bd35975db79e4f21d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFRVNUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOF%2F9aOoRrdoH1XbQ3Avcmjm%2F0KVdnS%2Bc0yCicFFS7%2FwIhANSDT0orgreF47CkSS4aHEIHGM2%2Fc15nfxzBXRZKWzRcKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz1JzoyN4INXTfXusq3ANOBx3UFlQZQQywmnwwjyXB1kb0lVhFOmmZpYzCjl8X0HSSJ1I2KWi2z0jJVVzrwmIpxxkYC7wKEZQcF55TJVxcAV6smoxE7%2BMYZjXEAYqwCKUqUhWFrNyyJckhcO5aMEdgcVo0itHdCxDwCAgvH8cr%2FQzZM8GUfItTB2twaLB5HpZxdQo6z5VYi9hANSnV5B6WyVbzGozhqFlDmOclf3pRj5gK5AOwYusMvuMolQ4CyxKWU5Hfsh4VdNEXN5c38MXwT85E9GmWgSMzDGOA6VXrqloE8C7%2FnBBVLZg7zHHfsJTFS0ZOQf98kP4X4fuE9yelubiPaVfD5aKuTlGSMH7ihqQyGuDFbshSHlQ29L%2FZkuvok3MJBG6VHac%2FMPnfouKy1mQ0H21%2Bq763pElR3fDcrrOLgjQqpWNyrs2c1x3Hw6tgxah5FanhxFVMEuzz2u1%2BxlqWbqDuvS7Uyvg8pD0CBXTlchNmSu3tv5NVVn9YXPwDlW71SgysRNrOJH2wFhMTwxb6JY2wksEB9ysnZSuQ7C4afPWQeIZj482VyGgP14BhBqMXEPyIxqH2l23i4SzqxdqwhxgLMuO3T4VB6guSoxCaMLgXC6gs4yGAxcrvd7D1%2B4IsQKJCZ2pbMzD8p%2B28BjqkAfawTfijYiqXn%2Fc9XRDT6rcVEjkLvTx4TkNSvJa6f08QZYsp76B7IPSsNTehV%2FHfvDh2aUR%2F922vL%2FNE2spDTULMI%2Bb%2Bs0ueenGqMFWSrf3mg3d%2BNnGwoCY62%2BDQl12cnbVALj4vph5uGul27KAJslUvUhibvV3XCyla1gyb3rumfGzHRqQj7zdLCuzEA0BPIMtjOi1UhnQsTnwlIFWxNgsLkfH9&X-Amz-Signature=53c4fac8ea7ad8c207e47aa68802c7f6d1fa8ccc15d17203217519a3a1c75dbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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