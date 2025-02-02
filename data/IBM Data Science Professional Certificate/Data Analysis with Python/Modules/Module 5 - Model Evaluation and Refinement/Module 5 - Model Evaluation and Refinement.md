

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=14b5f6edd5d1fbd0693c0acd3f5b4928aa6a8c2b86d890abbfedf66ed2908bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=7a15c78ff3dc40f8b0ea056a62718f70b5e59dfc298f343269e0f970451ef950&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=083f9891a7fc50651ce30502da2f1df0d004d86995cedeee6e765024ee511f25&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=b18438542bc6812fad9534f3cc1ec279e5507475c70f7845cd2d348f4e1805d5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=58ff3a92e885015d55b64c7d056cd58f051ac8c9f50184e030ee6dd0d9c6da22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=8443fd3723f3eca3c423f35578c410bd279d17f1ff4cef65196fe1ed780809a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=6e182636a1480a46c32551c19dc3a53d84b61ffca52f3369e904b78eb1f58ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=f84f14d0c11a0fdd63a9dca3578d21566829bef81f9624595c1364efacf83053&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=1ba4107b84a9773e9a4fc5182bcfdac5ebcd1c7ec408722b1966fea1b2f7b083&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T2BRYGC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7tDrd9Y36LstOz%2BHOZQsk5A8C0YzsqnW4qGcMVQBiNgIhAMqHGxAMnGsZ5%2BQqsspXeIzB3SBHU0%2Bv1Q9z2Z0f6g9yKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhM0bJj%2BnVFxGQtuQq3APbXChxy1exsDi%2BLz15gJthT%2BOxdWMDgnRBBCgqivcY9Fo%2BNCZge479dq0TxBrWFHpBoXKpisCc72s2SKQyGANpMVAAEDxaSAPqputpmIfe0yaRTdxQ%2BzZkaPdBFjyzRg74iKsX%2FwhfVdIQpZpnh9A0C%2FFn73tjP59MhSkqzf0KnY2YVYhaLkGdVgp3Lrp6cL10Gp65zP%2BEKNKBYolsvhmbs34kOSk1lU%2B%2Bs6tx5vT%2Bip8DYch4KlOZZCTWrvsGMkdkZBxxFxHpkfmkEcF%2FBjHsRiOpI7kbEIleKuz5ZlNcELMfsgEYAQVzsfhIl5A4eCz%2FZTp5UBy58bUpEJAALySDGsyifV12TKG%2B%2B5uK%2Bluq6b2yFe6N6gg2hZc8InhRoEwDnL0bkwXWx6dK5KBqG%2BESEhsWrj939uUjbdC9%2FUKjo7zJXjEqQIH3AU5ngcVx6KdpgOMBFCKDfpyn2qz%2BFMUoDkh7tP6bPx9J5%2FMkv4ycPTrVXgVKuHxetwKfzEjbdOBUt0wpSvqkU9uPWz2X3MyXLtANIKqxBYgk9%2BGtgODVYcfnI%2FT5vNMb2ass6Bp0qhEiiuRMv5QtqWe5zEgP4%2FHhWFqTope5qiMv%2F6NdsPbLFDQSFUmNDtJ61R%2BpVTD7nvu8BjqkAWlnkThY%2FacYSHALC3xYatXh3Z5KHdXBvfxc2X%2FndVSI2WkVc8T6vb8Hxj1tBw68EAIpJK6uQ2%2FqcrcLWIbVyaVxq7AfMMlI2gm8upn37oaUPpjpiP0P6l%2Bb6G8DVyhDlaYZtk%2BMGA6U1kVPyM8hJmMlxjQyjHzqbrz0VPCVuT%2F%2FRPoFwv3QX4L48O8jaw522yL%2F2Txgb7WD0ZtkaeA2p5aFzJdT&X-Amz-Signature=caf8528317444ea57941f58bbe663b72e0c73102a2bdbdf998c3ff319190b6c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T2BRYGC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7tDrd9Y36LstOz%2BHOZQsk5A8C0YzsqnW4qGcMVQBiNgIhAMqHGxAMnGsZ5%2BQqsspXeIzB3SBHU0%2Bv1Q9z2Z0f6g9yKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhM0bJj%2BnVFxGQtuQq3APbXChxy1exsDi%2BLz15gJthT%2BOxdWMDgnRBBCgqivcY9Fo%2BNCZge479dq0TxBrWFHpBoXKpisCc72s2SKQyGANpMVAAEDxaSAPqputpmIfe0yaRTdxQ%2BzZkaPdBFjyzRg74iKsX%2FwhfVdIQpZpnh9A0C%2FFn73tjP59MhSkqzf0KnY2YVYhaLkGdVgp3Lrp6cL10Gp65zP%2BEKNKBYolsvhmbs34kOSk1lU%2B%2Bs6tx5vT%2Bip8DYch4KlOZZCTWrvsGMkdkZBxxFxHpkfmkEcF%2FBjHsRiOpI7kbEIleKuz5ZlNcELMfsgEYAQVzsfhIl5A4eCz%2FZTp5UBy58bUpEJAALySDGsyifV12TKG%2B%2B5uK%2Bluq6b2yFe6N6gg2hZc8InhRoEwDnL0bkwXWx6dK5KBqG%2BESEhsWrj939uUjbdC9%2FUKjo7zJXjEqQIH3AU5ngcVx6KdpgOMBFCKDfpyn2qz%2BFMUoDkh7tP6bPx9J5%2FMkv4ycPTrVXgVKuHxetwKfzEjbdOBUt0wpSvqkU9uPWz2X3MyXLtANIKqxBYgk9%2BGtgODVYcfnI%2FT5vNMb2ass6Bp0qhEiiuRMv5QtqWe5zEgP4%2FHhWFqTope5qiMv%2F6NdsPbLFDQSFUmNDtJ61R%2BpVTD7nvu8BjqkAWlnkThY%2FacYSHALC3xYatXh3Z5KHdXBvfxc2X%2FndVSI2WkVc8T6vb8Hxj1tBw68EAIpJK6uQ2%2FqcrcLWIbVyaVxq7AfMMlI2gm8upn37oaUPpjpiP0P6l%2Bb6G8DVyhDlaYZtk%2BMGA6U1kVPyM8hJmMlxjQyjHzqbrz0VPCVuT%2F%2FRPoFwv3QX4L48O8jaw522yL%2F2Txgb7WD0ZtkaeA2p5aFzJdT&X-Amz-Signature=acfea7db4bee3dd22f46bdcb190b495d59318f99ac590eb7006133350cb0630b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T2BRYGC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7tDrd9Y36LstOz%2BHOZQsk5A8C0YzsqnW4qGcMVQBiNgIhAMqHGxAMnGsZ5%2BQqsspXeIzB3SBHU0%2Bv1Q9z2Z0f6g9yKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhM0bJj%2BnVFxGQtuQq3APbXChxy1exsDi%2BLz15gJthT%2BOxdWMDgnRBBCgqivcY9Fo%2BNCZge479dq0TxBrWFHpBoXKpisCc72s2SKQyGANpMVAAEDxaSAPqputpmIfe0yaRTdxQ%2BzZkaPdBFjyzRg74iKsX%2FwhfVdIQpZpnh9A0C%2FFn73tjP59MhSkqzf0KnY2YVYhaLkGdVgp3Lrp6cL10Gp65zP%2BEKNKBYolsvhmbs34kOSk1lU%2B%2Bs6tx5vT%2Bip8DYch4KlOZZCTWrvsGMkdkZBxxFxHpkfmkEcF%2FBjHsRiOpI7kbEIleKuz5ZlNcELMfsgEYAQVzsfhIl5A4eCz%2FZTp5UBy58bUpEJAALySDGsyifV12TKG%2B%2B5uK%2Bluq6b2yFe6N6gg2hZc8InhRoEwDnL0bkwXWx6dK5KBqG%2BESEhsWrj939uUjbdC9%2FUKjo7zJXjEqQIH3AU5ngcVx6KdpgOMBFCKDfpyn2qz%2BFMUoDkh7tP6bPx9J5%2FMkv4ycPTrVXgVKuHxetwKfzEjbdOBUt0wpSvqkU9uPWz2X3MyXLtANIKqxBYgk9%2BGtgODVYcfnI%2FT5vNMb2ass6Bp0qhEiiuRMv5QtqWe5zEgP4%2FHhWFqTope5qiMv%2F6NdsPbLFDQSFUmNDtJ61R%2BpVTD7nvu8BjqkAWlnkThY%2FacYSHALC3xYatXh3Z5KHdXBvfxc2X%2FndVSI2WkVc8T6vb8Hxj1tBw68EAIpJK6uQ2%2FqcrcLWIbVyaVxq7AfMMlI2gm8upn37oaUPpjpiP0P6l%2Bb6G8DVyhDlaYZtk%2BMGA6U1kVPyM8hJmMlxjQyjHzqbrz0VPCVuT%2F%2FRPoFwv3QX4L48O8jaw522yL%2F2Txgb7WD0ZtkaeA2p5aFzJdT&X-Amz-Signature=797139fca5f18754aa098e03200b35ccf9d5ad40ee2da0c88b766e53b9a8fded&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=c30db3f2b2a21686a51b4242091638a7fd795e59eea9920d0f9043c52aa05285&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=da44b431f0b199ef149c3ccbd5f2df9b0250468af484b71d1c2f8a5d6994822d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=128d46633a3da3c21267976a5bad3851b4107032aad9252c7302f3959baaec1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=0ba7f658e03e0e40b4a724b77bcf2d75964ccdf4e9ecfdbecdd8f911f0ca9714&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=ec602370d7c8713a9adbd4615796fdd92408e8f38f142c52bc0d4fcd54c50ef3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VK4FOMN4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg9vX8JS9JWTXyJEWpQBfA11XcH7Heyu1WquojFwHd6QIhAKrmJbpgC9YHmQdomRbchGxiW6SGtQsQUJpjqJTerJsTKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5go58Rc8CByyY7W4q3APtvjdPm1%2FcpVH6NLKLrzPFP4cl8ylq9t2UqYjy5Zgrv%2FI0qbJmkDr8Xu9GcWXPESn7rHttBW%2BqMEDiMcZiF7x8TFPYA1lZrOKNdstHcBtPhfItPLplDZft1Su7nzfkAaXqYpCT8hfpXrJStJsDzqfZoW%2BNyD82DM2VhmbdVjy0IchNDJEC6cXxyB%2BVOGeA38G8F3r7SNYHt5rLGOavW2PNQQrLozl3zt55ojoZbHZHvyddwmjaiQKlKa%2BjpBpD4iiRbVSpd2%2FzDEBrQ2qX8pbgU7DWOPYsCY%2BOr0%2FtoJNk%2F0O2453QD1R%2FBquFmFGS%2B7VpRv1svGNNXCYGdaewFkSPZGGQewvntYt0mIZTLknPDze6M2LG28cwZY8LiL03lj76uQvZYhW0sm5sTEP3KDa4VG2xfeWtna9mvMovQlL0PMflYrc1ffUSsxWrYircj%2BB6LTxbQIO2wXlOg87QOiyqbRvhzexyYQ1TeY2Uvy9lDf0P7oXZE8D1zsfzfwsaJiDiofBiAQAT8TPkyM5fsqb9M5tVVJt4HkyQ%2B2qguZTbjcVL5L640BMX%2F25UrQW8h3pq42Oe5isW45Y67pq72GU%2BGVSX8dqRML1OXl4YKMvbqHVD8q%2B17jMF0pBGQjCqn%2Fu8BjqkAcIBnglkSHThHNPbLQW5tCQQxfBzk%2FVeNG%2Fhnls9LYckgYXtAjaT8pGcO3C9f7Fr%2BrvCZ3hfJ2IFXDOLlGs6jWe1u7nzX1UMjWWZtmem6voJhRshQCZzQEwQGHQ3Jr2XJbK3wY8UIkUreZV0FmMO%2BXifkMxpfHIyA2MNY7E0gLC%2BtNl3ZqMXfD3O9TcSisQZ5S%2BP7Dq33qJzNaAhBzmnsqdB0rpP&X-Amz-Signature=71822be3ec1c62a026cc82b067e146970ab9700b7b7eaecb4be8956638d109c0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655JNORXS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLGLUReMYuPSYbhd8uZEAJtc3nmnyrr3XkTPow7SZz7gIgHqdSNnS5OXyath98WenLG7lHuQC18T9TGk5Voy2KXVcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlBzeJ6Vxn%2FM4CCJyrcA%2Bzqim6Kuua%2BlgRoUYez%2BvFfI%2FFnBpA0iaB4vx3InEwyI%2BIKQY8RkHquonf%2BucP2OWA%2F%2FMJvVwcJB%2F5fevYMaKs2C%2B1gHz7XCW3uv3variscnEOErCrJmoAuT4auNI41F7IA%2FsKzm%2FhvBj7PGy9085yUVAvL8ZZ9Cu9QKPQln9FEop2GtG%2F%2FmcJ72GE8X2pC8Fr2Qikxp1rjWkwDAht8Uzxj3depwoJfHhtmd7qtYLDjGS9JBq8i68vKDUeYRWMgl2CJ49HB2ciA6uUl7Rh7Zm6opS7b75dm%2BRDSebIxNpSfcivkFZPUeIEbvtaxX6%2Bgv06ZNGZdL58ye8R77ey3UBw5zyejD0oPnZhLlkeFzpNmMS%2FahWBa%2Byt9bJb0ZvXslGJ4zfZaHoDsPucIp%2BG99snkrZSxFXc%2BKe4ibORayKBf8tuFQmqrtI47eM3g05fOd%2FvHCrcOvaXIMxLhQ%2Fbl5w0GwIggRz74lmlh7C0fnkVapzdT86eYo7zqZ76EhGWO157CXw0ChSQpHNmY%2ByC6WD6Vw5Rg%2F9YBio91BOgywwWMuhrgimDglmfzMhf7vVzschZB4t8kj6v5%2B2y8TEPHDlveiueXKQBvA4vwD5Tkj2CcxNWqiWVAGVHl%2FiSiMPqe%2B7wGOqUBdkA0mVXb52qw8M0IG0pCsB4OyETDMuXYwCCDK3jbSahy5Mb633Q34Kr2IUFugGcQJDu6fl1tVKckaCCChBiBwwsSU9Uues1IuZbifTJ%2BXz7mWVIMw8TC%2BqJB0HM%2FGTNp8vmHim2dPvj%2F8H1A6VCWN2cApYCj%2F0dFM23CNv5mLEYFGEKu9C7rQpI%2FK%2FjX3TFwj%2F5yup1dcPg%2BIGf%2FGv6zNEL1T83h&X-Amz-Signature=4031bc2238bf69a7670f47a890877808f754b525bf396cde220f5e2d761539b9&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655JNORXS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLGLUReMYuPSYbhd8uZEAJtc3nmnyrr3XkTPow7SZz7gIgHqdSNnS5OXyath98WenLG7lHuQC18T9TGk5Voy2KXVcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlBzeJ6Vxn%2FM4CCJyrcA%2Bzqim6Kuua%2BlgRoUYez%2BvFfI%2FFnBpA0iaB4vx3InEwyI%2BIKQY8RkHquonf%2BucP2OWA%2F%2FMJvVwcJB%2F5fevYMaKs2C%2B1gHz7XCW3uv3variscnEOErCrJmoAuT4auNI41F7IA%2FsKzm%2FhvBj7PGy9085yUVAvL8ZZ9Cu9QKPQln9FEop2GtG%2F%2FmcJ72GE8X2pC8Fr2Qikxp1rjWkwDAht8Uzxj3depwoJfHhtmd7qtYLDjGS9JBq8i68vKDUeYRWMgl2CJ49HB2ciA6uUl7Rh7Zm6opS7b75dm%2BRDSebIxNpSfcivkFZPUeIEbvtaxX6%2Bgv06ZNGZdL58ye8R77ey3UBw5zyejD0oPnZhLlkeFzpNmMS%2FahWBa%2Byt9bJb0ZvXslGJ4zfZaHoDsPucIp%2BG99snkrZSxFXc%2BKe4ibORayKBf8tuFQmqrtI47eM3g05fOd%2FvHCrcOvaXIMxLhQ%2Fbl5w0GwIggRz74lmlh7C0fnkVapzdT86eYo7zqZ76EhGWO157CXw0ChSQpHNmY%2ByC6WD6Vw5Rg%2F9YBio91BOgywwWMuhrgimDglmfzMhf7vVzschZB4t8kj6v5%2B2y8TEPHDlveiueXKQBvA4vwD5Tkj2CcxNWqiWVAGVHl%2FiSiMPqe%2B7wGOqUBdkA0mVXb52qw8M0IG0pCsB4OyETDMuXYwCCDK3jbSahy5Mb633Q34Kr2IUFugGcQJDu6fl1tVKckaCCChBiBwwsSU9Uues1IuZbifTJ%2BXz7mWVIMw8TC%2BqJB0HM%2FGTNp8vmHim2dPvj%2F8H1A6VCWN2cApYCj%2F0dFM23CNv5mLEYFGEKu9C7rQpI%2FK%2FjX3TFwj%2F5yup1dcPg%2BIGf%2FGv6zNEL1T83h&X-Amz-Signature=0322de9c7b70a9a623cdd2ce2e2065ae47636be0f45273f77d7eff424366d3d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JUWRPYR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxSwWFqw8NHpIaMZdojySqKmR%2BFCmJ50V2pQnfXdh5bAiEA%2Bj9%2BsV6qV0%2BjqdWITZgp%2FSx7HqIbNOxOm4cO%2FXc%2F0RcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDITBNc%2FYHUpmXDN5XircA1P%2FA%2BU33hLMF64r6Tx%2Bxe3PaxjERAioxZ5r346YuLYzHTgsl01u6IXdbHIoPgiWZuwzPIbKZXSgws4Ar0rEGSg9r%2F77E0mRpblpnNpkWGnmbVW%2FRn8gCDCr5204MiBEldM%2BvTv8KXLOWROYeMh%2BtOeT9vQiF7UQdcDELOHthsC1eB6%2FcSWdjeVKsK3NZ1bp5SWBQD%2FCLoWcfFrC%2BbaByGrzSnvKmS9nLAPJ%2FS7SBhaJEVI9NxFnLrxOV%2FT8JzS0qpRs2iaeJj8jHAeADGLD%2B5jG25mFDEp%2F5DeLYgG1AjO6fCt%2BucLmjNV9i7F4ZjJIQncf%2FcTN1uUhBFTKYxUiHqv3t%2BHzwXMoAfJkjjpec%2BZ%2BglDEyoC7SYUy5Viaa7bWqjhdtWK3d65JXACevjrsxFH2cghRShNSlRp3VIdZXmmMIqE95YSaQsDzHgF6W51WecrqwQzhAtSHSFjjCh9Z3wgiua%2Ft8fx0xeqvFhNBhCQRYv%2BOx2%2BH0ok%2FO54JG9bBdr%2BjjCg7gexBDFFvuuCBJNV47oyuv4LuQtUgo9gGsMaT85JEVzjNaBFUQ9tA8KchiWRUsWIKYKEkt7IuX%2F2wVqd5HuRY5BXX8tg8Nczfu2nruEoWKL7Lp1fgzcN2MKif%2B7wGOqUBGP%2BaxSz8CNX5soqHCE%2FBnD8Dl78Sz0096xQM2h%2ByF%2BSkaXXv426UPtgVKsdXJUv1RFvHnWaA1tcXK9IJ5%2Fbe2aJXhSZ3HVH4Sj4Omz6QKGHb5feCYfSNgO9wtlxrzQO8t3YupJ3CRkBD%2F8o4CyCfidyf430%2ByOjZ0oxVoLnMoGpJuvdZBCLv1c%2BF%2Fj8vlK%2B1z4VmSHKsmDtBzVpbVHYoBRTE%2FusY&X-Amz-Signature=703c6207e5dd9c2ffbea7cd20f0366156cf958781779aa306a2b1fcef6b81fca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUUEJZM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEM3k%2BWULIsufOUsZSLkbi%2F7GCZW4PJVT7V8nMK%2BPFp%2BAiEAyNG%2FfuBJCDcyE5DDS1PasG2VgcZwrwucXdin4B1Ui%2FAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGdhcvfeI5yQ2zsAircA2Af02TudEPw2Pq3PSbbEB31Aq0yP%2FXZ5Ra3FtXODqwiCTp9OteFnTAl9XZq8LBDqd9pdx2qiqOoUx529c1hQLeHS8yK%2FZyZvIIc%2F8pv4xmQBUn%2BbYFPb%2BnIzh7vzvpYvh3rVrNsFrIKgLFUEXILlSZG4x4NdPbVWmdqtsw2bBfVVvwLbI7uRAYiz2nnvor%2BmUUbbvDX9uRgPX%2FOtBjd5UibrjZNIL17vSsH1hFUmdt19ku5CJV4oynurMGZpsjEDzsX0Z%2Bsg953Gcc%2FOTcF2lcPzfH6HHSnv1tyDZsMRmLfT7junJIO5seNmMAAkxlTDg4uCfBs6ykW9YezO27O1vXJtqj31TzQVjNWHCMlWsUSONyMssKcgH7U7%2FRoY558aZb3rfudacPV%2FI5bW7U8xgfrjotOGi0CZvWmq4NbJBXMTs1uAlbLIDhqfScA7ADBH9RQrdy32AJMUBjv20qOFNmdy1fCY2KqUvrtsTmV4RUJabfrVaPShvQ2zLHsB%2BDb6HblVst5hPzlvnduvthF9MXbn8DlLbFyYjPaljsIXzXd4lv2mLVn06j8X44%2BEO7yTUY7Jx2cc6kUsDuy1svRlBFe3YKjxkPGsd5JV6DIeJ3VvfWr86pICoz5I%2Bu6MI%2Bf%2B7wGOqUBiKS6wQ%2FyEk2q2B%2BsOKCNrSpSCZgjUjoDNn7pqK%2FC4VeDM6%2BkKtKfHjC67d88otPQlnZuFoU6Vej%2BU71A0DYxkB9Av6S8sNY4lXa8Jpif9J4GzGlL1qcdYph1f05Js0aUWKOQtY%2BL97eBliKSWJRBKhVCu%2FBvXSkGhfkSTvzRYMMfTHh2%2BsiRB3oSqCojYDQGUx6ZL8zuUywmqEqHkzrdvXazIa1L&X-Amz-Signature=214c748a583643d178fe129834b3b4871637b044dbe6f2effdd7f7d0f41b5834&X-Amz-SignedHeaders=host&x-id=GetObject)
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