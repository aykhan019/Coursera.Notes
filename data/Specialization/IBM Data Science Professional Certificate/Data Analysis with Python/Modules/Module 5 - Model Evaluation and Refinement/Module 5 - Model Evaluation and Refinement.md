

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=27e741cd3f2e5c8cb33960152d64d1d7e32882c9ba2f2519d27983d627445dd7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=8520c91f561134af380c286526ea4608571dd7a18eb006c22c4e550e2e6d03ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=28fa022700e12375e34defc85688cff1959f9850ee52091df03baddcc5193cfd&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=327eb41e9c317fab04fa56b678e4b7dfcfe6ebffbd3d3b927340c21d470fddf2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=d5c4e3e5e38c876a3613a802489951cea834ec395e1a80ebb79103e74050656b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=6ca1662c12f92c613fc20e4fb36956b4a5bbf4c681f59045c864171d8fe34925&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=bb1d31c1cf309849fa6ad3d601e7ed1daa3eaaa7ee93f34505c4d93884f9150c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=523060a897b9036285aa4323eee78de8280d2a12d1f2e31c7980207d62b40dab&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=d8fd2a7935370ac5b92ea0fafb45e0be9b67dcce12f982405d5da3d34e0b8b3c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSBHMEVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdVQK2fum7LYTBkkIV6LOiTh4cv2oZf59zhssf2fm1wQIgP9rLhEBZkUCmAvOLV4hj2s0dFVN%2BUBFS245uVbOmkvIqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGztEZP4SPyUeKwkvircA4gEmSSf3w2bHm59DiqoUo%2B%2FMa%2B8xyhLbGiqMD8qHCwZOcjDdMIls8LIQ8SmQuJnZZlm%2FPp6H77kjrjchNprnjGPCqu4z30PdPXjrYb%2FYXX5OHmKxM%2Bx479%2B74sxIoPhXgE%2F6Tm9miXn8pSflMsXf7NWmo5zcXriT4XyWSHqr5prA4Bnawk1YDctfQSqhneQrYZ8%2Fow2eonXtTQ2y0OZ%2F8Nq%2BqhI4KeXzG2Jn4varyF8qlk97jEP9OvltbafONG0amB%2FNihi20RXVbTqWJcK9e8s%2Bml03u5PVSCWqQJVdm8Z2noEPsA1XQYCFJHbcP2QqWwocFS15vXU0KLdKo1YytHmJDsNrT2peNrIEhGPO%2BLo4hYUac6wMOrkrbMgEZ5lUwm7ks8G10RWdgHTuKQXd0IxdZlFSTWwC8pIjvAHB2f2LAXIe8G43eE7e0JzHMd4RM%2F%2FpWE%2FwaJpGpRxsFXgY7ITeOoHpGo6VeoFGh0QGoJNOjB9lA%2BtAOHxLCqJ5uejyjSWC2wt%2FQ5LRAMEN9Z60zs71QTG3d%2BUKyN9qmdRRF6GAldQ%2F7ZEsPZgHqtCygJEysjv%2B3f%2FgVBLWbkPn1k4yLA7FFKnLyup1mDm9GG%2F62SXZA4iVQg8SqSekVx6MOL877wGOqUBERlwvrA2X%2Bh%2BJbkLrfsooIHcTO0UPx%2BUdU4oaX3ieoXE6OMguaX%2FA0v3P6JP9lCB1OXLN1b1mPKta7dV5Pv0fB34sjb%2FavrM9v2UHMQBFzTkmb%2BbfkKOuQtdRtfN1mRe2r9UAs6Fnpl3MqSpA%2B4TDz%2FKJXvlDgU1q0WaJjmpuvmk6jYlrhNrXs7KWbq0hkVW7CY5BRe%2FtcBEvU4CrUm%2FLQUkvwxo&X-Amz-Signature=30d93ac334d22852aa42053cb29614912a81834678cdffb1c9fe3deccc1da61a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSBHMEVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdVQK2fum7LYTBkkIV6LOiTh4cv2oZf59zhssf2fm1wQIgP9rLhEBZkUCmAvOLV4hj2s0dFVN%2BUBFS245uVbOmkvIqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGztEZP4SPyUeKwkvircA4gEmSSf3w2bHm59DiqoUo%2B%2FMa%2B8xyhLbGiqMD8qHCwZOcjDdMIls8LIQ8SmQuJnZZlm%2FPp6H77kjrjchNprnjGPCqu4z30PdPXjrYb%2FYXX5OHmKxM%2Bx479%2B74sxIoPhXgE%2F6Tm9miXn8pSflMsXf7NWmo5zcXriT4XyWSHqr5prA4Bnawk1YDctfQSqhneQrYZ8%2Fow2eonXtTQ2y0OZ%2F8Nq%2BqhI4KeXzG2Jn4varyF8qlk97jEP9OvltbafONG0amB%2FNihi20RXVbTqWJcK9e8s%2Bml03u5PVSCWqQJVdm8Z2noEPsA1XQYCFJHbcP2QqWwocFS15vXU0KLdKo1YytHmJDsNrT2peNrIEhGPO%2BLo4hYUac6wMOrkrbMgEZ5lUwm7ks8G10RWdgHTuKQXd0IxdZlFSTWwC8pIjvAHB2f2LAXIe8G43eE7e0JzHMd4RM%2F%2FpWE%2FwaJpGpRxsFXgY7ITeOoHpGo6VeoFGh0QGoJNOjB9lA%2BtAOHxLCqJ5uejyjSWC2wt%2FQ5LRAMEN9Z60zs71QTG3d%2BUKyN9qmdRRF6GAldQ%2F7ZEsPZgHqtCygJEysjv%2B3f%2FgVBLWbkPn1k4yLA7FFKnLyup1mDm9GG%2F62SXZA4iVQg8SqSekVx6MOL877wGOqUBERlwvrA2X%2Bh%2BJbkLrfsooIHcTO0UPx%2BUdU4oaX3ieoXE6OMguaX%2FA0v3P6JP9lCB1OXLN1b1mPKta7dV5Pv0fB34sjb%2FavrM9v2UHMQBFzTkmb%2BbfkKOuQtdRtfN1mRe2r9UAs6Fnpl3MqSpA%2B4TDz%2FKJXvlDgU1q0WaJjmpuvmk6jYlrhNrXs7KWbq0hkVW7CY5BRe%2FtcBEvU4CrUm%2FLQUkvwxo&X-Amz-Signature=14b5e192c5a8e2988181ebe622fed20cddbdfcc5c5b9d728f6ee0caa8ad876a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSBHMEVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdVQK2fum7LYTBkkIV6LOiTh4cv2oZf59zhssf2fm1wQIgP9rLhEBZkUCmAvOLV4hj2s0dFVN%2BUBFS245uVbOmkvIqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGztEZP4SPyUeKwkvircA4gEmSSf3w2bHm59DiqoUo%2B%2FMa%2B8xyhLbGiqMD8qHCwZOcjDdMIls8LIQ8SmQuJnZZlm%2FPp6H77kjrjchNprnjGPCqu4z30PdPXjrYb%2FYXX5OHmKxM%2Bx479%2B74sxIoPhXgE%2F6Tm9miXn8pSflMsXf7NWmo5zcXriT4XyWSHqr5prA4Bnawk1YDctfQSqhneQrYZ8%2Fow2eonXtTQ2y0OZ%2F8Nq%2BqhI4KeXzG2Jn4varyF8qlk97jEP9OvltbafONG0amB%2FNihi20RXVbTqWJcK9e8s%2Bml03u5PVSCWqQJVdm8Z2noEPsA1XQYCFJHbcP2QqWwocFS15vXU0KLdKo1YytHmJDsNrT2peNrIEhGPO%2BLo4hYUac6wMOrkrbMgEZ5lUwm7ks8G10RWdgHTuKQXd0IxdZlFSTWwC8pIjvAHB2f2LAXIe8G43eE7e0JzHMd4RM%2F%2FpWE%2FwaJpGpRxsFXgY7ITeOoHpGo6VeoFGh0QGoJNOjB9lA%2BtAOHxLCqJ5uejyjSWC2wt%2FQ5LRAMEN9Z60zs71QTG3d%2BUKyN9qmdRRF6GAldQ%2F7ZEsPZgHqtCygJEysjv%2B3f%2FgVBLWbkPn1k4yLA7FFKnLyup1mDm9GG%2F62SXZA4iVQg8SqSekVx6MOL877wGOqUBERlwvrA2X%2Bh%2BJbkLrfsooIHcTO0UPx%2BUdU4oaX3ieoXE6OMguaX%2FA0v3P6JP9lCB1OXLN1b1mPKta7dV5Pv0fB34sjb%2FavrM9v2UHMQBFzTkmb%2BbfkKOuQtdRtfN1mRe2r9UAs6Fnpl3MqSpA%2B4TDz%2FKJXvlDgU1q0WaJjmpuvmk6jYlrhNrXs7KWbq0hkVW7CY5BRe%2FtcBEvU4CrUm%2FLQUkvwxo&X-Amz-Signature=f0e35791435e01fd26a5354d4dcd7a6519ce66e8f7c249f49a2f611f5e45a1a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=7fcb0245f5bfbfb57f0a2c133e9d89e6dcc088a8ec7f4146e6033ed343c5f88f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=f53234000262eb2770a02768b53fd79f593d5874e9b0d3eb83111246b652fa3a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=ec6d6136400030c00bc1d7323889421ce0e7564fcf5de7981fef79bd4a77539d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=490cfaaf1bb7572bf92e0d68fd695d9278654ed31e13c48620baaf6fa474a283&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=88448b1fb981b89641d3fe6c4fd6623172dc8376bbdb5cefd6c4aaf47fa4fbf1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V266KC3T%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa031M%2Fgmtjrq4iab2YAHovu0sxDQl7oPdWK3CBkU3wgIgAwFo%2Ba%2F%2B3jsp0rNnFOwR5CCTvnr6ohganij5LyQhUEYqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHnLyavs2TCtqMEKircA5nSRj2C1cVfKONNSdNQIh3b6mtb8DVD%2BpzWfSxReybLmm0bNKjUotCudAO%2FxTh4BTo8pOG%2B50eOl%2B8ortNaMcN5yFHUfRXLKOk8ecdt%2Fd9DMha%2BP2zcwabRuMFCRXBHaWot9nE%2B9FouMvHqu2Wr9g9V4aIlwWSfrTDRYGK5KFMMHZ%2F0dzq7p51Mj5D3VJXBoypPhEcqP2HiwGaMwgFsIRWu%2Bii3iWguAE7wlxrvdyA6u3XGCJel%2FVYhfiw0r37y7WptXlNAagk5WVh7Cr8cwHrVoLQO%2BvirL5tPZfHbOEJ5GWVT%2BQfsaL1I3vC9kgkyd6deTNOVOZqmBBfquj6qMiRljUsBN67XxV%2BB%2BxC6fyAl44xlWgFsNXEohyyOw%2BWvP5%2FwiWW8o6JEN64eFmqEokdXFdcAW0UvdBzxk%2FRMDZAcvC58P%2FuHlBwyRYeMzPhPW3k7LtY11ig4Bc%2BUsql8GWgVV1cCM0iW6svJvYp1SBbp%2BSnQZ%2BYXJTeeMBGdmtclHTsI%2F65CBDpq328bFPj4D9zkOP6SS3kC84ju4X%2FBXtX%2FDJP0y4MxxNvpXFxbq9fCAgP8lXjGmN9nnOq4xvSo%2FECQO96HhBdBc0Fci%2FQGx7W4%2BYGQMBejRtrc8qLYMKz977wGOqUBvh5%2FbBE0A1rnq3F1q2Bys2wa2r1nNykx%2Bdw9r%2FCj%2FSRNWHjS7VFTBN3JLwlWiod8YvgzKt3z6C69eHsdQN18XlOH%2FL2ypzpikXzTFFQxp9SxJDsUXiV85cMgWIs0CNFF7aot6EmrgjkhmxfEua2NyKX57D%2Fqg7aL8qy3rVcL5SqRdO1aJ0LSAtrjTAgKV5plj1bDMfZbL4cNPJ%2BVF1MT9VLt%2Buhm&X-Amz-Signature=dc501977c8e32cb0df68574d61f43e045b560201c3f7d57be5afccf8f6242ba1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I7WXRHD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBXewd3uKqKWcwfMmvHZJr6vVlSXfvoRGUlkI7ysQ1YPAiEA%2Fz53Lzup2u716u%2BRDEIsE1NEizK80c3gWxIniNbH5Y0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbJWOJwjCHkbG7UUircA6oLlraBD8v6LgO7F%2Brw649ttaBugZdFbmpW0mrygz9WGQdbQn4IVesVWoVfdEXITZpKk0FZfAPCc2%2BUqx7IlJ%2BZBPnjBgLWtC1JMudnia9Ly373T1doUV7IW%2BFfT0PElSVLqxHnX%2BAaW3jbRgRWIbZVzfRScgnlfLENfr%2F5zM2rS35urfsoGSAK5Q4cBz%2FMzfmr9Nh6eJjwpK9S5M349%2FhKmQ3jzQhu8f4T8QZOpEt6MZcSnTl3Uqb4JdGRw%2FdkQVO%2FRrd0BE4Of9yNnJlBITah5Asxm%2BjgJs9779373Oy3Y%2BlKXsw3jleEEbnsDBexxxv%2BT5EhgEysqFa%2Bo6t4CJQBRHJL1SOm82yz5u98FK6t%2Fv1E4HQ95lzHahTyitnvnlCAl%2BKP4D7ktyJpbF4heYPhLEItXcEYSLnF8HGysGaH%2F7imoN8Ms%2Fhz4iMdbF6uXfVRGl%2Bzzr3I0uYGk0w6R4j00n7d8tcbkOqWm%2B%2BK6GbAUIogCERSWD6MaBLK4HPKzKUS3Jb1o9vZROBx4q%2Ba9ka59dNf%2BIFWurrjvt83UZm9zQOEE8T%2B6VI%2Fwx5xkvPRlDc2BBzO3v2IHdXA9P1XM28VnyQtvPn1lpgaH7tXpU3mO0cGd%2F%2FEYbkzTkSRMP7877wGOqUBNrcu2VSt0FV2YJZPQgWRcknLcwcfZOr%2BPAouq9miukzyZquLL8XeIAoUfC%2FIo91tNlxgkKzJ0mhkBGtQvWslaREW5C2xam0KM%2FsVLNnHqyJJgHXe863GdBF0ENRfpzehW5%2Fc6UINmCy6ti%2F6pPYeCY6s5uRcU5nZejvwQpH0q91AL493j2vrPYcdvcOCU80CzXkkd81bSDzMvzi1xti4DrZmuo0C&X-Amz-Signature=4be17152e4556dd3e26e11f2caf674d7367618c818e4cf443098f10b24369829&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I7WXRHD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBXewd3uKqKWcwfMmvHZJr6vVlSXfvoRGUlkI7ysQ1YPAiEA%2Fz53Lzup2u716u%2BRDEIsE1NEizK80c3gWxIniNbH5Y0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbJWOJwjCHkbG7UUircA6oLlraBD8v6LgO7F%2Brw649ttaBugZdFbmpW0mrygz9WGQdbQn4IVesVWoVfdEXITZpKk0FZfAPCc2%2BUqx7IlJ%2BZBPnjBgLWtC1JMudnia9Ly373T1doUV7IW%2BFfT0PElSVLqxHnX%2BAaW3jbRgRWIbZVzfRScgnlfLENfr%2F5zM2rS35urfsoGSAK5Q4cBz%2FMzfmr9Nh6eJjwpK9S5M349%2FhKmQ3jzQhu8f4T8QZOpEt6MZcSnTl3Uqb4JdGRw%2FdkQVO%2FRrd0BE4Of9yNnJlBITah5Asxm%2BjgJs9779373Oy3Y%2BlKXsw3jleEEbnsDBexxxv%2BT5EhgEysqFa%2Bo6t4CJQBRHJL1SOm82yz5u98FK6t%2Fv1E4HQ95lzHahTyitnvnlCAl%2BKP4D7ktyJpbF4heYPhLEItXcEYSLnF8HGysGaH%2F7imoN8Ms%2Fhz4iMdbF6uXfVRGl%2Bzzr3I0uYGk0w6R4j00n7d8tcbkOqWm%2B%2BK6GbAUIogCERSWD6MaBLK4HPKzKUS3Jb1o9vZROBx4q%2Ba9ka59dNf%2BIFWurrjvt83UZm9zQOEE8T%2B6VI%2Fwx5xkvPRlDc2BBzO3v2IHdXA9P1XM28VnyQtvPn1lpgaH7tXpU3mO0cGd%2F%2FEYbkzTkSRMP7877wGOqUBNrcu2VSt0FV2YJZPQgWRcknLcwcfZOr%2BPAouq9miukzyZquLL8XeIAoUfC%2FIo91tNlxgkKzJ0mhkBGtQvWslaREW5C2xam0KM%2FsVLNnHqyJJgHXe863GdBF0ENRfpzehW5%2Fc6UINmCy6ti%2F6pPYeCY6s5uRcU5nZejvwQpH0q91AL493j2vrPYcdvcOCU80CzXkkd81bSDzMvzi1xti4DrZmuo0C&X-Amz-Signature=36d139ded8ea2fba83206d3b71e101d9cfb883365b7968f66efcdef13c503c14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZUAVILD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlWmrmcgjM7nYLIGTqLua%2BorMAPj8alC1CR%2F6jDChCVQIgYtLPEVQaIKPUO2AmyM0Rqj%2FRlaOYKx5py7KpDQSzfTUqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjsBqveG8nonKM%2BJCrcA2mKVPimCa4hcmGydRjeC4tl1uSQJMSdyKnf%2FUxBzsRzesYdVGPwX0eB%2FIkZ03TIGgs%2B4m2qe2WET1DKcIKfRsSb%2FzEC02LZM3ZruIRCx5Aeny1MW89vPVBL%2FmE0%2B7gdIo9NR%2BX3C8Ne3U%2B%2FiMYACcqts9Llud%2B1XjSndXiHe%2Bu%2Fb1AX5EbfZHp5xeA7ujqJQ4YBSLVqEqeV1qq3OA%2FnQa%2BK4rjd1DMZf20GOEeGHwYb8OTsSXEzqD4me%2FiCg0Jb%2FBt9wMnAIHam1%2Bm%2Bgfw2jFePdMHptdk84AlGNWrEZB%2BAG3IGVUj7fqgXSFVOZas4JqMqvXTR2weTamcUFbrGewIO8XOX%2F7gWZd8tM%2Bc9FSYAeAM1Pr5jAYOxdovR0tmsDHdEnlxfJe46FCz0QK1Vn2FOojaSDXi7F3F2%2FVTzm8WXBVnlJEVXov9hGnsDqDQCjPiOBzU6UG%2FxF1k1IoHfWQrxGxLAFeZi2TRwF07ljwq5GbzMoBN6AVwXmMuvpAv6tEwaooI7%2FsS7pYB2To2ewvMU1laChW2CAnS3YumZjnO7Mcdv5xjL0BseWqEh1EsQaZ40oT14Rq5kwDW22%2F%2F4UrCUU1k%2FeK84wHSn2NmXQ70k6NPaaTqZbLj7FC5nMJr977wGOqUBliSKe76%2BPBYpmtE6GVZeq5CGWcB1Z3j4SXjUz41%2F01cvK%2FBPQ1%2FO0%2BxH1pCzz0i1%2BdxzwOR9N6pD5ZWt55EJvq1DlvTELGg2r2VgWVvsvzLOPf6cCmQ%2Fr3TlfU2o4AL8lnqN68nm8s1eAT%2Bkeobpypu4kPpmyZ2i8OP5g4xOge6rjqPcdwrBvWMV6bVVoaNjg62bGs4LnwpjbI5o17KLd%2B7%2FchPy&X-Amz-Signature=187e6a43aef505cff7d1c009b3cbc31e7d439097589c777aaaafcf6e379930c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTGB5TF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID72%2BoFT%2BIfYt%2BlL5nPXGuAoWjiN0NampiY%2B7FgCxt7XAiAn9QKQGLtO707KYGIDKqVMD72zXaHfdFSKO1k83hs2TyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWnS9gCCN%2BYAsj7T%2FKtwDzoKD9kpZDJdqgNKF7ZM2n0vDJjGZZ%2BOhYWqkqJJ0VV2eiBvxgeN8MPA8ta8EsJs0OzemmWJ8ESEWa69WG4bnto8W4Kzu2Bqed1FNvRQsPJC%2BV%2BwX4mp%2FL4b25JNiPmwBja%2BbSSGx%2FfDeAZBP6CbPyV4z3QnhKVmlxCPy8AAkvJSK9heKYPRuo73Czs08P6AaedznDEWNZd%2BVWon0ilXWGrq8sgtpAyaKs5hbeQUr5r6oCHeoQV7X4Fe2yMARpjwYHHlJYQQ6jL6fmHPimZD6%2Fj4ypvhzBbJh3pfXAclTridpPVafPzTN%2For25xqIG5%2BIPIatOO6a6Gfn%2FWLX9aWf4WP8BG2J5tFpr7RWMWdRdIqBhv9Ff0c1U6t1c%2Fbe4sOsZlPQIvQ7MeBaluV1bhbd5b5tvgi9RJAvf8ObDbgdEWJ0jOhswF%2BDF0hqJ70DKmQSqggddE6gEkeCgcEfxqqNNhVLd0zsxucusDvYRp5WcF8VYGT8Bjy9weUK0iFvonrlcMO5uNE6rZPCkeK3in2NRCRVZiOwPNgeU0vyJNRBBMTR1TSKCp4tqWFb75XA98E55Bx4DYnRXpvYkS1UEH3VphU6WtkkZf4LdBuasMHsFSO7biQxYEwsjSa8T6Uwgf3vvAY6pgGiJQzji%2F5XPbD1AtpWjznuI2g9%2FAL%2BIiRMa%2F%2Fwe0QlsuwFjrpq1megbFrbdgSkHfPe5O6xgq4aJwIFphdzUNBjXIoRpN45XMGQsPFOcBRVGWF9rR23hTFyUZV%2BWbheNNyMqKKAqt9b0tIwbm%2BBKFChIM%2Bnda4g040XvHUvLwat8wG8410xIFlZ7t7SjxNbB7Slbc3rfinjuri5JOl%2B%2FTWseODZE%2Bl8&X-Amz-Signature=56721fe8efcb20dc0d3b48496e23bd1f31029c4787d7b50e836fd670872d64a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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