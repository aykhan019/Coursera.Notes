

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=de1ce5c8a833407729ad3364d761bac10c3b4adb56a5ae19f43b0125a5d501db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=f2e62b19ff682152a01d3c0704d58eb9aee95b584d344ccdaeff75d3d00573ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=af89ab01533d563cdefbe1e52d8930d4eb6a038a2d81f79868ae90439291dff2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=35c8465ad75b7f06683f8ee8e0b9b05fd0e920f495e38d834678d47dd6cb8f60&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=08574824dc47646b567af716bdbcf09e00d5c5399e4958b5a6cac01bfb1fc6ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=8db8c28b6ca88d337792d349e02ea608d939335a8cddb805c3992497be442665&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=87a02e4c25d7480f040b951c924ab8d088fac994394eeb0b02eaa7f348af5f15&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=10a2c5493269ef100dcbd0139f3f3ac9978d42f00f73fa3dfcdb84ad6d75d052&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=c7d702b4164e74d0d8f3a6936a1cd96e51852f7c2e37e7d0c0bfb4a580c98825&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=0a2c158ca0aca52b439404554dd45947d1943f66e72657366d39927dc23ebcd8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=fd8b2c2c2ece1a25d1b7592d9726c819a36aa3d50e6f89ab2c3526c2e055194f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=88d85f78a4a0c51fade6d8e1a135449052f4bded55cccf22d64b96adc2968422&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=d684e0a28ed11858a221d7357e22382ffe8bde3ac533f77cc4eeb3885a017a94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=fef6c8631d64a2362f7e469f0f40d1f34d85cbb962614b5bbf031d25c43796c0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=247360b120f2e6c68c1dac5a040e073094587dbb758813a5039988659d877f64&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=1170d23c82f1ed50795c574e096bb0a5046ad3652111c13567c9e9d34d02d391&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=42e7e5aa68a5a48a2ed6d74967c2f4c4b155376e711e5ec53d68df88404eedec&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMCRBKO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCWgpcc%2FtymmdRpCEANfqPXmKpojWot3ruCe0MKlqRK%2FQIhAOgZD4%2B45bjT4e1up2y9KMmrCHtgmQwfbL%2BYZ%2FVJxv6aKv8DCFoQABoMNjM3NDIzMTgzODA1IgwLVyfGODoLGQG%2BKegq3AO9HQDqHWFQW6kx72ZhQqB52x7yVtC8olf3JNP4TYXVW3Xf3hXZ8W3%2BHtNqx6i6Q4GQzdiL9Qb1o247Gjshn2lUvRUSOyNhlKjFQT8av2mHn%2FVg7O9zHSYmjOcgQAATT%2BeXqAjLqoCxUSjZlq0wUn%2BWeHw%2FIIBo3yHlJNz0svIcjIXKBb9EKGsznieq4Z7imuoSYnmHC7KRoT9cDM7wIK1pHN8%2Bdtvku%2BwKM%2Ft3ICoKQodwYoQmCw0Dwd3zknLsdFlkg2c491OvQLS8irXqs3yy7eciRAhtAMkcvPMfMtZCYpRGWbY8vgys%2BlBoPmRYvVMsx5GcAIUAGDo8TPc5v6%2BsQflMdEYMIKNu1Dbc%2BN2ymG%2B47dcaVb%2Fvek5kfrR7B28M0q%2F2jy%2BtltBWnWDzj9vMh5ediyxl0klnbfLjjqPBqLQ2AF4hn78CUX1iyeju4uEtaMgUP%2B%2F%2FUgvVs5zg8MvEuGNXiw2UDnL7QcANsoWVtLDNTd9Hg8Ifmr9Ee2NOGETe8K6BdHrHJdzOOLcbJ5jrSQ3VMmioOCF5WgOgdk2lUzCmg9ZkZsr53NeoEickp4uLqh1T1n7WBAeEGIwcVqRE0wcQYvrkT%2FubE%2BTIXrWXkVOgOk5bYdCMEu9i3TDk7JG9BjqkAUS0UFJS0MNaYSp%2FfuOjLCuq9M2o3T7IJznQCDNqcI9wA%2Fq3awwk%2BykW46U12t9OIeS9vvryPu0ZCBbIxwzAdNkZWro7LLfcq1pT%2FVaecgzU6bb7QI6shiWQxXYZ1IvFt%2F%2FipMtm%2B1SKNBIeNBnMIMAtPrv6I8dUq0Aq%2F10DLe4BFetxQWFamciQj2NOQ%2FqGnP0wllBALPe50SHeS8m%2FHobJlfPm&X-Amz-Signature=4d9970d3b507c05797da4b8fabce5afdf1b45b8732d98835bd394af91b97b006&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7U3AOEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCfAxuqz3JBWDdvRFHIzsa7enduXsEvO%2B6%2BuVPWWGOw6gIgIoJE2UNEjSma%2FVOLNzPPyaJ1sl15PVXX9FZ1yMv%2BMk4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDPZ5yW14Qj2E3LqEdircA6oFL6anyDQfrkHtjsg6%2FR5GBKU1a65yXc%2BIFDp81cbOgFGYouPjc0BBfmsP1MkpvgNciVQLQ1CsDAEGf7CorUbLqJeLOUtas10TAPbfw%2Fni9aJc75jJerbEtZ%2FcGtLy5naBFcikPd9s3mMHqV%2BRH3tZId2ITbMu%2BcSnQF9Zf%2FgmzGRV7w2yXdOSkBcicW9F9MtWqGu87k6wphkWh7mL%2FoMHf3CsZIczoyi1FpoqGsydrsRKJ1ZrapYmrALsyHl29dXltMaf6WNuHhibQIXlPOC3JK8O68C5DEQKo5rgR0z3shOwwmHb9dZ8cWPQQ4pBA3K1Q4p5RXnWOi6cJwnt7Zni8wGaFN9b73Zz10p0OsUJd4MhzMGaESGzo9U5JoApawXuJzcg3V9VXgisUZBfJEgG2BrAe%2FsErxTQAGW3gETuJzSyHNHdnuwYWry2290bM5qBX15OLhFmr0hjMjgXUHOfNmZBC8XH2d%2Fm1ziNVcBcM5RFE8In8j1LrS3fVZYbeGQU5QbyZcIdwwthdQwCQOeAhe62p0kzRGN6ZHPoqzsS%2BdlpsmoepSfF7LpnUAMueTZzL8XcmOFjIOw7o3Ce0v7ikZZhppf6lhjvNKSnSLem6Tsjmne6uVtkRqYiMK3skb0GOqUBf4YG2jI09zSe85NRidj2r3lHoJQ9ZPaEvntk%2Fhzw63lgv8HwxQvJL5jc7DkD9Z%2FChSBB1Vxrd%2BDf2PbSmKgLR2wl7465Bx1T5rXF7BCyHBxbZzYWmGiTZhR8NDOtssN0Z7W2kRrIsyW7b4OoHCV%2B15a7E479K%2BsP91vbDSmFfOCVdDJHKkXu1%2Bnqy%2FsnOsLL65NRc%2BgCaOU3uuoYsJazpODAMRo9&X-Amz-Signature=ad9391a66e52e3a8647a888da68f936cb9e5a2a5be3ebd1301d76105c87987ac&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7U3AOEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCfAxuqz3JBWDdvRFHIzsa7enduXsEvO%2B6%2BuVPWWGOw6gIgIoJE2UNEjSma%2FVOLNzPPyaJ1sl15PVXX9FZ1yMv%2BMk4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDPZ5yW14Qj2E3LqEdircA6oFL6anyDQfrkHtjsg6%2FR5GBKU1a65yXc%2BIFDp81cbOgFGYouPjc0BBfmsP1MkpvgNciVQLQ1CsDAEGf7CorUbLqJeLOUtas10TAPbfw%2Fni9aJc75jJerbEtZ%2FcGtLy5naBFcikPd9s3mMHqV%2BRH3tZId2ITbMu%2BcSnQF9Zf%2FgmzGRV7w2yXdOSkBcicW9F9MtWqGu87k6wphkWh7mL%2FoMHf3CsZIczoyi1FpoqGsydrsRKJ1ZrapYmrALsyHl29dXltMaf6WNuHhibQIXlPOC3JK8O68C5DEQKo5rgR0z3shOwwmHb9dZ8cWPQQ4pBA3K1Q4p5RXnWOi6cJwnt7Zni8wGaFN9b73Zz10p0OsUJd4MhzMGaESGzo9U5JoApawXuJzcg3V9VXgisUZBfJEgG2BrAe%2FsErxTQAGW3gETuJzSyHNHdnuwYWry2290bM5qBX15OLhFmr0hjMjgXUHOfNmZBC8XH2d%2Fm1ziNVcBcM5RFE8In8j1LrS3fVZYbeGQU5QbyZcIdwwthdQwCQOeAhe62p0kzRGN6ZHPoqzsS%2BdlpsmoepSfF7LpnUAMueTZzL8XcmOFjIOw7o3Ce0v7ikZZhppf6lhjvNKSnSLem6Tsjmne6uVtkRqYiMK3skb0GOqUBf4YG2jI09zSe85NRidj2r3lHoJQ9ZPaEvntk%2Fhzw63lgv8HwxQvJL5jc7DkD9Z%2FChSBB1Vxrd%2BDf2PbSmKgLR2wl7465Bx1T5rXF7BCyHBxbZzYWmGiTZhR8NDOtssN0Z7W2kRrIsyW7b4OoHCV%2B15a7E479K%2BsP91vbDSmFfOCVdDJHKkXu1%2Bnqy%2FsnOsLL65NRc%2BgCaOU3uuoYsJazpODAMRo9&X-Amz-Signature=72dea5d5e0b2647c94ddb4fbed2c1ceba6a632320ac302df7e4ab30449fa4720&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYOPTLEZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDcHmTlqicZivfxbDaAmoRtZrY%2B1dcDMDRYajEbA6n3VwIgHdtrUcJwQLKmbleZ5Bz5BbxKTnBplnsu1jiLuUF700cq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDAvt0hkEqpk1iLttMircA%2BRqFGPIYFe7K%2BRNf6eyQU1z3tysNiAg4aaHlhuXX3h%2BtktOgryv%2B2HfpLvjK%2Frbzkvxm4ZkG8VPuko38L8fky5ZG7nDeJdc9CDBRXhS7bfGWAje0G2hG0ommsYN5f%2FluftOs5BlnVLU3hWoJwiRI1P7c4TWpS4FqRCGS2rh%2BspCfMNyKkklkjGZIT62jcGUqVG0rtG3Mg5N5fF9Mvz7IsIa9ZcRp%2FWP61zD8C07CqEMWlPFNrf5zWykZkQli%2FUQX1GvzHWIFS4wA3UuvKrCkwR9Rud4W1YggQkPF9vDV25uePdtKncUDOjLvPdQGg6E25pzmZc35D34G5YR1J71hprtjCOAqZblrFUSBkW0AwLMFn3wI0jqLadv%2BFP2ADCesIg7IdM3kcEr4ndWJgJQwxa5OZyVQE8n66WNFRPSeqtplbJfJnqWGeEny7bI2r3TWURsnNthYzIHDKChFnwLJN3vHVD157%2Bx3UCAozYnALEaxT6kCASZgLjbyLs3MbSdTsSOA73JJ1pqw37zp5SNDVZQEeW3OaiJJDSP%2FJGFHXrjlqyICQGSoRU14D9%2Fse5eWVlA%2BZK8KFn32tjE7i6CyHE0I%2FCAqqSCFhIjwzGoxzUpZkMoC09N%2FV7cbwE7MIrskb0GOqUBT%2B6tyNxl8pz9ao2vzGD8baKjJscg76%2FgRue0T48qgaMhi72gsBo5NILwaHojax9OpcSiBOw2%2Ftw0Nw%2BsXA29OqdHXR6ZQH58zFOPkHtqGBOnFxz3Fso9gkTAUtpPtUPSQ7UmQ%2B7N%2BLt2%2BhoKyckj4YC2IgmPkdQObn8LTZBWLomAdTFr9px%2BVfQrDgBsIkm%2BpMpl7qqEYwq5ZyvXqV6696cgfvHo&X-Amz-Signature=bcb94c0d86739abad5af77586707c9bbf5c046464028e4dfc72d3adb4c698e86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKR4NCS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGbsQDO%2BZVEKpmp9LdTb9tSSZrJ7OFYEtEI34DfhsuP3AiBd6Eut5FJWeGiO4ls5to0gyapNdtxGvCjZA4Eg1tLuiir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlSlnBE1p2cAKSIEJKtwDwFwn8LDV9iNBQ0LQe%2BKRjaSyHYFTR%2FiNNTYeZlnwM61JvxJtx47GRVjGI%2BBZZisUlFsZOe%2FEBOwVs4mcT2pyrUcXsbxbCQR3n8i5bK0rGSOZLkK%2FBtJh%2FkFHuiUk3qI0sXrR9nGXzqBNrQxjNiuOqXy3MEu%2BZIwRfSyvR1Pso%2FzYymxfCSvI7i6CWYdOoRNJGa06jX7c9sxN%2BEKUb03DlTMpWgjeFwaldJKdOAB4SFnJ3k0Ia4wjIUYM9jYtFb7LuJBdvQWq%2FX%2FG2LarKaetCU2g7LDxe7mV8RZL1PGx4eJY2WLr9nk89zOEjWudK2g1mNFoxa5TbOC9BrGpSIZV41r8GZFtBLumUCUmGv00e7W5OBwq4Jpr9ZJ5FI%2FhnQVuXe%2BCec2ay3xyxzBHDqrtdj2FeSLbWTq7UFk1qut37HSO%2FLHPo%2FUB82jN0wv%2BCxtNirqiIrG2WY%2BXkUeB1oqY919h2wV5k6m97oAqYYnuLhjDnZbVfo0W%2Fkfhwghf3t6B15g1aHWhnlYWubyDVh0wj2omVAVFehhgBCe0%2FaycS2WF0N9G4j7dGsPFDjVeRz4Kz3vTIVtrLq%2BAMZey5W7RlUV6%2BI28g%2BddTSEyVTMvApnhBxnluzBHlC8i%2FBcws%2ByRvQY6pgFweB392RhaE2QMQSq%2FzK0hcBO%2B4PByhcKYuCXz4xJfU1SpZjaOzIk%2F2aymJqOoQVvtoPfyA6y9yRuf4mo6gXQlqXrSisDZmsv%2FzN9E9SH0S9rAveJYkKEkyoEPx8VqtVWJtsTKp7DR6McjjUmVQXc3rhn5lNJJ5piDukG4Qn1QeMjzPlhPDdbDENXCGOBNFUwvz80KFwz%2F418wSVckzRh5BIJwd4P5&X-Amz-Signature=6a696189a0438b2abe0e0316f188dbbc7fd85dbf3867bc3e22166ffb3f47cd89&X-Amz-SignedHeaders=host&x-id=GetObject)
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