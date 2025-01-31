

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=87c54d5461fc79610e0bfb8aecdd9f6735a026f19732339f6cae7c0449ec8807&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=987641d1d96f90c777d0acfd3b6de044a0138d74af76432a46c7d80ce1d88c46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=7700e34b8408b699f5c9dce77d83ca300fa1dfda4fc4d8d02203d90ce6eb9ce0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=ef888267aad10885bec6fbd383041d1888f4ad2044d23968ecb611825d37cda1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=6291ce53e5dff70295db66505d9e1d8cde9e40d706d43a4132dea0519c6abe2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=947e0e339b813d6c2cb450d7a9a1fcd4649a6dce83179617b6fcb0968f12afa9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=df2076220f392260ed31c61eff77e0eb415b243bfaa1ff28894f217836199dcc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=0ff42af8b6166a8b014620e57c079c268bf2c82cec7412dbc3b49ecf1180de72&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=9f646173d208b477b93af718d16ef4dd63591df1cac1d1164d3f780d52316f51&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=42efd1d14db123def034278fc4a918a18e3910eea88527f988b2ae6e4d6409fe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=1dcccc899168332298c1cfe280328ac7899b63d52901cfbb50a41544c8fdbbc6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=9d4e14479598c59db55c2d079156417b443f537dde90eedff61074616337ae9f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=44428af8c72ca6abb058d6e91dda17d6075a38f61736d9bfb76d939b0eb60ef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=c234a4bc1452b9ea2af0c975ed86518882e2b6c277094914f44599c96936a9f5&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=954b0db6dce93c6e37639f42e497f05baf3ef17758e41a8b8714a9466c075efe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=14b28e2d5d6f5561264a6ee4677ea80a57a44b72dfbd69279efa6809dd1bb9d1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=222701d795182c1cdbe3245b7401587248717414e1451de9c6c21589caa91f09&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GPLMKXW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoMU9XOnB5sEi3lDAaAyItuHEGKReqhQP6aQGvftHj1QIgaQ7g6CXJ8bm1XeZiI9FAu90hAke%2FtIUM9244gON5zrcqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK0IAQypzSWc3YcrBSrcA%2F5Ey9vunTcE89xzs8Xyv1ourWvsoUqW%2Fd05Quhrpbi903Bp9Ha0r8eVMEv86DQgnH79R3%2BQ5%2Bi3XOqtGeHuqnRtRPeMhpGNSHTruecAO8GlyvdDqAFdkGdW9ZInHlLLHavzo0KdtTSR87Cz7vrL2rkLgg190HsZYtC0akw92gLDooHhH%2F9fpKSht2q24d8Mz0rt82n0T%2Br4WcX%2FFhFb8koduQdAoaKlnMKoVURKeAf9ikwqr6smQ%2FuqHoHGPqZI6jaaa7nl5OiHUWpwEnCTwy425D%2Byz29TM06j7WoWTquGaw2Ao6LZorYXxnT251CKBwxNkzURG7Ugl6WsKeOTKvn0MVWMtFAOxGfQbqyvMKW4T9rDZ92%2Flo2sZ%2FT%2BzmIIbe2QpbjDeKecJpmk7yFVC7%2Bw%2BEcCkrCXlhvlMT2toDrs6x%2BKJof0FIjI8tkurB98yEneLjpGGOmIxXTbbvhkDI7OI0vGf39a9iVIMrGxyFsg808%2B5YNW0L%2FONPmTOe2oZAkl7cBkTERhds6KxVQQaZTdNzdjNEH%2FzBkYSJk54rGvYtSI9AkF7Ahgk7hSUQ54xtUFGCDynZruABiebj0vpE5gUHtTDUJTWup7Z%2F8n7dUJn%2FkPsGn3X0SHEhQ7MJ6U9bwGOqUBxb3OFHnbORQVSBu5ONy6hb5NFOQxUqPuGrZc2MW9p1xLKVD5cJD94MnXdshk9Od367sXMycv%2F5yLo0tPtAf%2FAC%2Fhj1b%2FOR2GisNE%2FmT1xzLNuexQV3lZerW8wBCd1LWja6DA%2F8WakpQAOtOHUmTj%2FCXaO0WhAjpktslvp%2FsueDNs1OL%2FlFJedRSN9uGlffGDY1PobsdYvwelnAjBzXrD%2B16RUzIU&X-Amz-Signature=315abd7714785886cd6fb3d71b8097debde392057ea2b6a824013f593a3591e1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL7TDPUU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEZPtkKRZXJrrQLZxlXQQbjx1ir%2Bwn6QfdGmsv%2Bgj60AIgbDWVzKSHdV5WiJXDy%2FK9vCeL63VSvwMy0uuKgfscsYEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOAv%2BasY8i6bbFUpgyrcA0lLAS6VMPuoAt3DCN3J5Metc%2BnQfS01%2BNQrBXGMIfhI94dFNf72hAyIHmmJ0A0e%2Bke%2BiljofayVE7g5Ns6m0HQ7qdP7jKDlVpi50oal75rSUZpdq1BA5IV9VhPH1WlIpGvdf1rNbL0CzeBoOZHJ0mTb7pKA9ztembyJy2WcHZY2ohYLjNeMlsZGRPLJSy32EFdOzkQ8ErCEttpKgKIq98cLLB06K8qMQ2TdjDxOa7hk0Qhy59wWFF5F950ircyCa9eSXpHh%2FgjUP4WVS3nzRyJHupDREJsi3MLplsJO5KcZF%2BWKV3yw%2Bw8hBAbT1y%2BRrmwuIzE%2BCPsGnjvk5XwlyhIVf%2BTB%2B44NUVRZ9Uae6OHNExQtX1gE8ZquJiZRhWCtqwrz8EDfnRlZinzeyZx14daE3zdUb%2F0eqinWGsvviX8fl%2BqSANW%2FCuSuKAEHSAcYQJ8B9D7K3%2B4tZ%2Bnc8Kp%2B4WJAzXdiDS1Kvkw5OQOw3ivceukjSJOZDxX%2BsHunuryXl0dZzCABLEQSIqlAdjaLmgyWeczt5PCykhcT6H2PoUoiT0KgCi%2BUQIwZX9qwXiZCwwXwnLdcrJ9TSMA610o3Oj5GK9sqvS2rTYN%2BS%2FHhwAllBqNaCzkFyv5C4a4gMIKV9bwGOqUB%2FvhKyHt%2FAdhTlDBhKGEy%2BUXlNXQYJ%2B7XNTRCbp32S7SswievXfQvcVUyEkt8MpL9CpIfd4%2BfQujM3q9BId1Bm81duvSLduNzjiSYWn5Bg5mbAWx3ZIzdYuwwEzBxmAqvJ%2F5JkaUHtOfA5I0mS542LTZGZXP0sUFwsPuxdFLpv%2BprSJxOTFAp4XXz4wwVYAA8qZ1qAZe2UiIbRsAyajaVZ%2BoW9MM%2F&X-Amz-Signature=e10fa9f673751dfe4ff43ebc1248f99b50458bcb701d3cc07523e44119197016&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL7TDPUU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEZPtkKRZXJrrQLZxlXQQbjx1ir%2Bwn6QfdGmsv%2Bgj60AIgbDWVzKSHdV5WiJXDy%2FK9vCeL63VSvwMy0uuKgfscsYEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOAv%2BasY8i6bbFUpgyrcA0lLAS6VMPuoAt3DCN3J5Metc%2BnQfS01%2BNQrBXGMIfhI94dFNf72hAyIHmmJ0A0e%2Bke%2BiljofayVE7g5Ns6m0HQ7qdP7jKDlVpi50oal75rSUZpdq1BA5IV9VhPH1WlIpGvdf1rNbL0CzeBoOZHJ0mTb7pKA9ztembyJy2WcHZY2ohYLjNeMlsZGRPLJSy32EFdOzkQ8ErCEttpKgKIq98cLLB06K8qMQ2TdjDxOa7hk0Qhy59wWFF5F950ircyCa9eSXpHh%2FgjUP4WVS3nzRyJHupDREJsi3MLplsJO5KcZF%2BWKV3yw%2Bw8hBAbT1y%2BRrmwuIzE%2BCPsGnjvk5XwlyhIVf%2BTB%2B44NUVRZ9Uae6OHNExQtX1gE8ZquJiZRhWCtqwrz8EDfnRlZinzeyZx14daE3zdUb%2F0eqinWGsvviX8fl%2BqSANW%2FCuSuKAEHSAcYQJ8B9D7K3%2B4tZ%2Bnc8Kp%2B4WJAzXdiDS1Kvkw5OQOw3ivceukjSJOZDxX%2BsHunuryXl0dZzCABLEQSIqlAdjaLmgyWeczt5PCykhcT6H2PoUoiT0KgCi%2BUQIwZX9qwXiZCwwXwnLdcrJ9TSMA610o3Oj5GK9sqvS2rTYN%2BS%2FHhwAllBqNaCzkFyv5C4a4gMIKV9bwGOqUB%2FvhKyHt%2FAdhTlDBhKGEy%2BUXlNXQYJ%2B7XNTRCbp32S7SswievXfQvcVUyEkt8MpL9CpIfd4%2BfQujM3q9BId1Bm81duvSLduNzjiSYWn5Bg5mbAWx3ZIzdYuwwEzBxmAqvJ%2F5JkaUHtOfA5I0mS542LTZGZXP0sUFwsPuxdFLpv%2BprSJxOTFAp4XXz4wwVYAA8qZ1qAZe2UiIbRsAyajaVZ%2BoW9MM%2F&X-Amz-Signature=819b152402830a2bbd1e26e98e78a2a67323e8101edbbbda4e6c06b9ad5e3152&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR4DMR2R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcpxG72GejC%2B9FVfHIi8%2BQQqiGahvOUaQL8GY0LWQreAIgSpUUNJxPLzTfBYmsUN0H1F3kUU%2BL97wj1YlURCF47DEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGOiIY7yZg9WWJVEgCrcAwy7VUFoPqHQbKmbT5Pz7YSCJAydX6SoFHUk%2BBmn7J8ZqYcV8zFgMrO5UvYaMXVWv60tqp8kVZfdKOtrQn8yrLYZfIDh1biS6FUTNRSs2LoPzj3Mh3xiyZfrjh9VFV7QDqGvqltx2a4qX8uSjXTtyWBx2PrIEE4enAy3qWrwh8xVKCsoGPQSfnjtmVYc336hjJ6kvw%2B3vGSvCbZF7DNfViwJ9tKBk%2Bl%2BLmwIkoEE59v5CDNEAAT9Z0%2Fcmn0PAx3F%2BR2md9vbQpiCeCc64W%2Bsr%2F8kbq5HJCddxMaJoJnrHLbsu5lqtaX%2F%2FDsl6eh8K8GDkfuyZMWzMidVdi6pOsMs5SKuQ1jRritKJ3egWinJUBrLyM%2B6YphG9i41BTT0yCT6oiqMOsJgn4qn3OjAxbMgeoACP3%2FC682ws9kDTAOfyBNi4NbaDHL9iJGQSr27Lu8IFX5D3QHNQS7BUPiLKXufLiur01wPlCDDjbeI491%2BiV7k3z9c7ZFA8bFbg37Zwaml%2FirJAr36wQ%2BINRl1XSoEnMC9cJp2ohU34xv%2FdIXrG2PdRtTE5AFeustrslna5ds0EyvLBjpQ86Ebuj1UZ5XuKoGHNgmTCPcwgZi38HkSy9qCnHBQaJlqgl1KSmw%2FMO2T9bwGOqUBAP2FLbaywx0V%2B1%2BaiDQmtRIZRipjuDAMriWJib29Qa3lDsc5VkhMaxNk9iGlR%2BvPaFgFtOiUWC5n8QQvEf0mIeGWfj%2FAs3Xa3kJB6GcbAbcrZwWNrEUlUVTeoX%2FsgF91X8CpNcOrQdnURuO3DivlYr3bfPKIf%2FIrSzG1Z4YzZnZLLhkup2EdAQ79s%2BeH%2F8EMyb3m4KKlrQg8Go4MwHnaEWHqar0P&X-Amz-Signature=2841b433e25d2b7b8187dbe3ffe8aa286e6b156e6a6e352c69bfe846c8b3691d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVHWMKY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMoHjKPlrJYwlMAJlQLAmvFSGMJSHUirJaKsul2Sk6PQIgByR8anMf4wBSxNiA9pCGwGvnTOJnmmbBRJPZoUqlH3oqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQLLKCca31J3bSuOCrcA9lbrvkFwrRW9SjVwTXgh0B6Sa3tS4jVaZcYMTMSZ6gFAMgPfxtuffTZSkAOyKCzMyOYrVmLItjPiFHsS2c34ut9yOuh6nvv6ziTtN9v7ayl%2BInZ4xD3qZ2VAk0iOrYOH%2BawWuOhuCKv%2F3uR64O7N3vF8p04WryMVDM0pL33IJcxuQFI5p%2BOuZciyf%2FwKqPcYcmJEskbFKxsJX8sQc2FaEYgbnsXrdgcKBsAdLf0AdI7E8%2Fd81UUHjcGHvxdjdIIzvSaivL0XjgffuYjIIB1yEnf0FEjDdysIamWFgugWDjLtqzkqmh%2Fg6Tk2aJOEU7EhZ83onSS14FLuO%2Bw%2Fwji0gmI3Yh1I85KxlwMmB8NuEyKNUidycgwi3Oz1mASdHXcb3v5JHpvaqc03zBPj8EiiIlire7OJdvY8vGoiKO2KgWgWqbihlHpnSAZ2aGQG7Memh3esK%2BUzUVrpgpnhgClZ81Cq68VLVTn16RyLC0as1cc4ahAJvZy1bwoR4DwJrDP5jAfX8aEfEV04l5laW7npFJF7x8P2LjQwecEfIkD3bv5wCguHG9A3w6JBvP4oODsqEJBZ2%2F8Ko%2BBfeuzYexNSzhA%2BiecTBx3TwsvDfN2DeoHR6FcwB%2FHxS1aSRMfMO%2BT9bwGOqUBRtv2UwNFGbKiN8axLW6V8vE6zxNMHYTDkt9FyWFUUUUwlRkWID5iAMId6EGL6aD3fuRNhTxrUflbVOesPIXgU30LU8egjmYJPXtKNRdts9K78LmFYvkwKDH%2Fx%2FkTBPTrbyrGDXJ993w%2FFPJVxqjFBzB0fGlNchJ8q%2BQioyspfcXi%2BxZTsMyXcsSY1aSMXd%2FBQWlHdL2B71mHNV162Ukodf8waX1y&X-Amz-Signature=ed19b8b1e4a8a5fec81d599b40918f072ca88968d98a4b63ea20535719a6f165&X-Amz-SignedHeaders=host&x-id=GetObject)
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