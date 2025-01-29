

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=9553c1d9900baa4d4eb8dbfda109d10fd262971e8e8a8c12debe57599cac2f4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=6c4cd9e8be075a10200d5583bf86a88c67adfe37868b3f80feab54a5eac99bcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=3565f7148b7bb176c0d955f1761be806a29a055032615c07c11c603bd603432a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=ec5c37ffe00a171964bf5d1ad81eedd369cf6eb98f778f74d3c3de2e744cba79&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=8f07275531c99704997dbc2a0e2104c0fa914409722d55540abc9c60b365c77c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=07b032bf16f19d1e2d032a1c4568d4cf593cd74e928903949700500e125fc417&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=f8633a0b32e787f800b5739256485f7d7b051396d7126b5e9da39ee26ac5a4fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=bde1942f1dab69c93c4a3cfb16fdc1b455845d88c8abd947ec84b7a8ddb3abf1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=1fbb5fc837fdeaa8fc0e91f5f0db445f9c0a338a6930b254451b4772b7a29550&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYKWZSQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh09HmpJYlQqEGMM3r7d2pjDBS5lnMU2O82zelZviscAiBfTIRQ8HfyrJMWkSLw8YWBNDb7JwpslNm2q%2BXahjdXJSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7vNxdU3uoKWmt9tgKtwD20TsBvax0ja4ID2AOAVAM%2BbkwyC1d7ouiUMfofkYv%2B39bLxv%2BkoBo4KD9iFia9WdVYX7ZIZIjsSdn4WXVUZ4c1SDTkYPxjSGp2At3g41n7Wem93Gx%2FN5DoAs%2FRD6uAW4K637pVuRay%2FVPfwNe%2Fe6vlINAZI9YQpZymcToWJkk6lUoitnzmgPwqdtyOUdPLcxWxWm1RkFUPAjP6A0gQC6Y7FRMFYYWywxT6SCnnuHYUoKwH4zFuzsanxi7%2BRZLGWT8iowYH9cjdyskq8iL%2B%2FT8zSqDcDkXt3XbmKyVNb0LrClqkKWWeCzO%2B0cVsQZ25MGyrokBJIPe8Ajo%2BmSVQzhSvtN9P6cLD2i6880t7IRkQ7lSomFhjtE8YUgzKsTaloeOe0sD%2FAt9XSmGRv8oY9HpA3vmTDz90BP3qrrGizbmnTVMb842gqKhvVCbYYf3wZeNZ9jQal97AvMdh%2BpVwHrAz3lZKPf3j9240cAFz91RLDy6LsEMP%2FjrrB35njLydubjhqEd3urti64UF%2By5aS6tkziEAwjwy5tT4pdxyKheLtPYzGQmgNUxR0As9m8ZW2wsnl%2BrifseYVnXqrnKSAE8kOv88FkWqDqnYHU1tUP0ZGq3YJr%2FscRMcfxoycw6MXqvAY6pgH2aSicYaDVtVqsfjq1Sf34exeQTbga91Llo3mTblU%2FIDGPdTYDQPVs4KQ13AjU41LbEn4Op%2FaB1U4UEnSM8g5%2FeE0CZUcYTTrAuvpogF%2BlYeu1RRagvCmjfjEZL6upcAP57SbfGv1jVXJxG7BpuRHI3vzLChWHjAYR9amHF5Z3aytwV7FGc7aARaUWUqwvNRTE%2FrwooZPv2yXa2ZovtRwbfWRcBBkp&X-Amz-Signature=e8e8680602eb56e2d18a0fcba3e45d968295a1ab0170a15580e5b133de4606be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYKWZSQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh09HmpJYlQqEGMM3r7d2pjDBS5lnMU2O82zelZviscAiBfTIRQ8HfyrJMWkSLw8YWBNDb7JwpslNm2q%2BXahjdXJSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7vNxdU3uoKWmt9tgKtwD20TsBvax0ja4ID2AOAVAM%2BbkwyC1d7ouiUMfofkYv%2B39bLxv%2BkoBo4KD9iFia9WdVYX7ZIZIjsSdn4WXVUZ4c1SDTkYPxjSGp2At3g41n7Wem93Gx%2FN5DoAs%2FRD6uAW4K637pVuRay%2FVPfwNe%2Fe6vlINAZI9YQpZymcToWJkk6lUoitnzmgPwqdtyOUdPLcxWxWm1RkFUPAjP6A0gQC6Y7FRMFYYWywxT6SCnnuHYUoKwH4zFuzsanxi7%2BRZLGWT8iowYH9cjdyskq8iL%2B%2FT8zSqDcDkXt3XbmKyVNb0LrClqkKWWeCzO%2B0cVsQZ25MGyrokBJIPe8Ajo%2BmSVQzhSvtN9P6cLD2i6880t7IRkQ7lSomFhjtE8YUgzKsTaloeOe0sD%2FAt9XSmGRv8oY9HpA3vmTDz90BP3qrrGizbmnTVMb842gqKhvVCbYYf3wZeNZ9jQal97AvMdh%2BpVwHrAz3lZKPf3j9240cAFz91RLDy6LsEMP%2FjrrB35njLydubjhqEd3urti64UF%2By5aS6tkziEAwjwy5tT4pdxyKheLtPYzGQmgNUxR0As9m8ZW2wsnl%2BrifseYVnXqrnKSAE8kOv88FkWqDqnYHU1tUP0ZGq3YJr%2FscRMcfxoycw6MXqvAY6pgH2aSicYaDVtVqsfjq1Sf34exeQTbga91Llo3mTblU%2FIDGPdTYDQPVs4KQ13AjU41LbEn4Op%2FaB1U4UEnSM8g5%2FeE0CZUcYTTrAuvpogF%2BlYeu1RRagvCmjfjEZL6upcAP57SbfGv1jVXJxG7BpuRHI3vzLChWHjAYR9amHF5Z3aytwV7FGc7aARaUWUqwvNRTE%2FrwooZPv2yXa2ZovtRwbfWRcBBkp&X-Amz-Signature=835087afada59700bfb3df6512e38a3f2b662cfa47b2eb044d7e0481aab91154&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYKWZSQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh09HmpJYlQqEGMM3r7d2pjDBS5lnMU2O82zelZviscAiBfTIRQ8HfyrJMWkSLw8YWBNDb7JwpslNm2q%2BXahjdXJSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7vNxdU3uoKWmt9tgKtwD20TsBvax0ja4ID2AOAVAM%2BbkwyC1d7ouiUMfofkYv%2B39bLxv%2BkoBo4KD9iFia9WdVYX7ZIZIjsSdn4WXVUZ4c1SDTkYPxjSGp2At3g41n7Wem93Gx%2FN5DoAs%2FRD6uAW4K637pVuRay%2FVPfwNe%2Fe6vlINAZI9YQpZymcToWJkk6lUoitnzmgPwqdtyOUdPLcxWxWm1RkFUPAjP6A0gQC6Y7FRMFYYWywxT6SCnnuHYUoKwH4zFuzsanxi7%2BRZLGWT8iowYH9cjdyskq8iL%2B%2FT8zSqDcDkXt3XbmKyVNb0LrClqkKWWeCzO%2B0cVsQZ25MGyrokBJIPe8Ajo%2BmSVQzhSvtN9P6cLD2i6880t7IRkQ7lSomFhjtE8YUgzKsTaloeOe0sD%2FAt9XSmGRv8oY9HpA3vmTDz90BP3qrrGizbmnTVMb842gqKhvVCbYYf3wZeNZ9jQal97AvMdh%2BpVwHrAz3lZKPf3j9240cAFz91RLDy6LsEMP%2FjrrB35njLydubjhqEd3urti64UF%2By5aS6tkziEAwjwy5tT4pdxyKheLtPYzGQmgNUxR0As9m8ZW2wsnl%2BrifseYVnXqrnKSAE8kOv88FkWqDqnYHU1tUP0ZGq3YJr%2FscRMcfxoycw6MXqvAY6pgH2aSicYaDVtVqsfjq1Sf34exeQTbga91Llo3mTblU%2FIDGPdTYDQPVs4KQ13AjU41LbEn4Op%2FaB1U4UEnSM8g5%2FeE0CZUcYTTrAuvpogF%2BlYeu1RRagvCmjfjEZL6upcAP57SbfGv1jVXJxG7BpuRHI3vzLChWHjAYR9amHF5Z3aytwV7FGc7aARaUWUqwvNRTE%2FrwooZPv2yXa2ZovtRwbfWRcBBkp&X-Amz-Signature=a010c1b867ac62c87b3bf8159ae1bc781f5f1651e0b893314a277d653f4a93da&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=e45719181a9e71c93bc100c9b4f53b4d33556a575d6314b1cb4c0279118c246a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=8a1c4ec592d20a82bfa35e9ffbac2eb59d5be0f32fff414388749efe4342c371&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=6ac0e3e72857b1eb31bd828bed8ef1e5df7c47e235f36affee35e2248cb494dc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=f35c54d27301612455a2b10c39a1b8675eae979065c54607eb1f1d78d832410b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=670186bfd70526347be3e3ac9a350a80fcb4c32b9b9738f2c116702a06d3e383&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVL2C2YH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FrItHJuwzRLED7Acqab5GIwxurz1ZKOnxCG%2Bw1ft1NQIgNOtaim%2B3UyHUndKLTdgCP4ldtdZ9wY3Yte5aoVO2YMEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOcN%2FzTIna4GTjSofyrcA%2BXHW0H6a2rXrMpaCsiDVJh7nSQPMNXl219EmwphmjUZJhNP1Nkk8tXpwUk3YCEnhHGGo%2FLWtJfDer29tDNPc5bq%2FFr8dByJQ8LQl3F%2FlmGFTTCQoWk8se15OJmsOC57F18nWW%2F0w3Ma8Xk1lu5UX28dunmEyTf28rR5%2BPXSJV7%2B6V2rPdKuy39fQAKbEsVNumNbLnB0DBmhi0H2%2BUlLtu5sx2ZNYsUE4JxRCF3IcNx6H52iSpMz%2BFmtVfAITX1H266xl1ILQODljdQYeD9xklucBzJGQkoL993OBDLToxwXW0%2B8di9cl70I4S4pe2xLqM1cyiAzmegCIqX5jR80mVkIqYksdgi0p5qsJo9Fx4I7ywjnbfmgZi7%2BiShd3bC2nGxSuBA00g5n0U7tPFnNYg4ZWcEgBOYUKKJU8yw6VODUZE1gUhbr062O0E2SkDXQCpn2cHy%2Bn7nNoDAUSJY0rpOD519GhSWtAAxD2T00Iq77lNIQ5wxEoVadmOcdDguS1vSo2kaknG7lpBBEwX6D6phsmGKMw8sp69kc5CIbpQiSMlg0ESOSUhO6w4ih2QMc9jwFL2dGJO0Nn6vVdGNZmZ1G3Gp1RvbBNP3a%2B4fHVeEvkvnc%2FTSnX3%2B%2BAwS8MLnF6rwGOqUBI1ZKRRSClxW73dc02meVA43AVgYx9%2F6aerXxW2KMa0LCQ0WituZEG0SN61CEWiw9wL220UyEWicqlvW7XLafyiLD3wfVf88l9SrIzQYiqzd0AIIXvO8IjDBh%2BfEm0y8NZJlZK8u7bHrFl8uFvIfHBlg4m3QLWsHB%2F0JZoyeMjHsSSq6pwNa8%2FtpPBEhG45EmOwZW3l2cdD4vhm9XJwUyzLeKYt%2FT&X-Amz-Signature=9ac9787ffb7d0efb10d66dd6849f4564471d691eb4208f71bc6e5e39fd8a7e67&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWTL3JXY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOnP7xo3mDFM0BaqlepyuN9yWtFSS7pSHjZO5AlvgUXAiB0%2Bsc3Z%2BTMhClbLYS9QLWgEbbl9WijCYGEWgHqxZdDTSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BG7tSdmsPlkyQ0W4KtwD%2BiFqHnQXPQQ2ByjirnCyHNbBow3LaB4FDg5p52QkD84er%2FXhaGQGhL2TypQCHiQjcf0cPc1%2FNrllZPmiavQ9z4bWaOFLV4b%2BkKVkGnLZL6tjg2ONPw01Dn1ZPyw4jFXk1jHdKnVzlYKR8lGOCAVHDpEEA8tekdDLO731brb8mVZ16F4PnCR6To9iK5kyGc0XhaN1hsjgBDmV1RrrmeLOL08hBAw7lllZiEEYjLKsvAVEjaIiFf0aL6RrMj1ZHaJKU9PEd8xN9lx4koraSLwI7zCFDJQ8wRNiAUfu7XAnmWA%2BOBpoSKUn6M1GLtanTv%2FwXPBRfD%2B0pPH8qVwddx0fMw%2FZr4UxiLczqekj2Ot018md5kCHXSS8DbAx%2FdQ5Vnz7jubocMIoy%2BRXfX48Iyy6KLmfVpFOBrw5D6uEI71cfonj%2Fyv8IDsRPnnUIs21fKlvflToU0kSbnyZhKLeCpi3GYczxiavQKj%2FF2o3S7lYgfKH6l59RTj6e9CJBlHKKhhulF1JqOnOLRaYT%2FOXTL%2FaPz%2FcopuQAzlx2NJ8kFQqjT9XPJVX4NZG6tslx49EOnB3BpaXD8z3JI4tFze%2BixOz1n6HcGo2SuTqOjPMis6NMFRwnNR%2BtvqhhyxjfAMw3MXqvAY6pgEXtfk8wqHcFhttHsHrb%2FiL6QTShqSvGGe3FFJsfmXIi26VLNOGJPPUIvfiZ2%2Bi5vlpCTv%2BNfhIq2yV8%2BaVzBg639B%2BnZJ2MHsPL4aB8t%2F4QL%2BZJ0e4%2BwYs71MMEBJcwzz0GZG2hL1PFuHnFvSrGs%2BaF1QYe5PkjZk8SP7O%2BF6cbkk2nXKjfGFqYNsru6tiK%2BoKiQ7cZd93GFkZFqNCVLgQAH3wndAd&X-Amz-Signature=c35ebd3a7d27cd452ddc5e92e2631c5d324ea0798bfc104533d9e43c008e2545&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWTL3JXY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOnP7xo3mDFM0BaqlepyuN9yWtFSS7pSHjZO5AlvgUXAiB0%2Bsc3Z%2BTMhClbLYS9QLWgEbbl9WijCYGEWgHqxZdDTSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BG7tSdmsPlkyQ0W4KtwD%2BiFqHnQXPQQ2ByjirnCyHNbBow3LaB4FDg5p52QkD84er%2FXhaGQGhL2TypQCHiQjcf0cPc1%2FNrllZPmiavQ9z4bWaOFLV4b%2BkKVkGnLZL6tjg2ONPw01Dn1ZPyw4jFXk1jHdKnVzlYKR8lGOCAVHDpEEA8tekdDLO731brb8mVZ16F4PnCR6To9iK5kyGc0XhaN1hsjgBDmV1RrrmeLOL08hBAw7lllZiEEYjLKsvAVEjaIiFf0aL6RrMj1ZHaJKU9PEd8xN9lx4koraSLwI7zCFDJQ8wRNiAUfu7XAnmWA%2BOBpoSKUn6M1GLtanTv%2FwXPBRfD%2B0pPH8qVwddx0fMw%2FZr4UxiLczqekj2Ot018md5kCHXSS8DbAx%2FdQ5Vnz7jubocMIoy%2BRXfX48Iyy6KLmfVpFOBrw5D6uEI71cfonj%2Fyv8IDsRPnnUIs21fKlvflToU0kSbnyZhKLeCpi3GYczxiavQKj%2FF2o3S7lYgfKH6l59RTj6e9CJBlHKKhhulF1JqOnOLRaYT%2FOXTL%2FaPz%2FcopuQAzlx2NJ8kFQqjT9XPJVX4NZG6tslx49EOnB3BpaXD8z3JI4tFze%2BixOz1n6HcGo2SuTqOjPMis6NMFRwnNR%2BtvqhhyxjfAMw3MXqvAY6pgEXtfk8wqHcFhttHsHrb%2FiL6QTShqSvGGe3FFJsfmXIi26VLNOGJPPUIvfiZ2%2Bi5vlpCTv%2BNfhIq2yV8%2BaVzBg639B%2BnZJ2MHsPL4aB8t%2F4QL%2BZJ0e4%2BwYs71MMEBJcwzz0GZG2hL1PFuHnFvSrGs%2BaF1QYe5PkjZk8SP7O%2BF6cbkk2nXKjfGFqYNsru6tiK%2BoKiQ7cZd93GFkZFqNCVLgQAH3wndAd&X-Amz-Signature=b63ee7feddd457adc38938f57e4bdd04fb4244adaec9b9ef590b71261e1d8bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SXBE57S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBesu4Wz3JHicm%2BP0PuZHuSUeijVFJcMXpBVra9fl5TBAiBrIFT8qoQB8g%2BjyYZyEit1t9WkhJl3MWtxYmH2U9d45yqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuiBA2r18uq%2BDQHlLKtwD7mjb8SPzmQOUnHHNMhtfu2NOUAMgA5FxYi55Y14lkiXT79zSQT0jc2wmX%2BL98ZU2PvZUk%2BGd3KKZlHlfxQOyCH485QjbcUaVy2VDAw6QUIFLR%2BAlHC%2FbU3IJUM0OLPm%2FmmwhVUSM%2FYvf7JmvLExKlTV3dTJtWY%2FprstLpd%2FM7jleCZ9icJU%2FpTBB4MkWvqsIJ9j8GVAQar9wLJ122VqA7MhqsFISS95tIc2ErZPpKQzphzzDm9V05DhUzKJEW0XpNSsuvne3rXUVRtFwYqAkN9h7pHZ0VSatCSbk8FnV5bIv9EQyqMHrif73DleuPgNWnlcgvULcAPTneg8YBpcFWZM80u1I8MpWP%2FFbUaUEomukEgIm8aCi1Dhw%2Bi78XsC5%2FqRKZSYIJUWJBgvZ5BK%2FtJ3GPDc6T5SvZBaoqyBwLjN5WC0GCzAWx5wdLDxvHxgZeo22jps60UF6kuQrACmPYqlWKkSMVzfCiU24VGV486c5ifJcqUNWMKUWjcMCLxaGqy58UWasWgfE74DLThA2dve2FagVORcanMA%2BiCE02Fnywib2721DUCEDYv176eNbNYvI6IAtnPCpuFSpaXS0Kgtfw5Z%2BNTBIBfwMtqNvtpY04JJoRYN9QTal%2FikwkcbqvAY6pgHjok9aC8YI4OzynNVarxZavNDYGy4et840RsJWLTd%2Fd2A4GszItvdqoYIVYQ%2F4yrr1at3vFSNma0HtrS0PoIY0JMDvIBHjAfS1L6cZ9h2RMIET5jcfkq2k3jX4DF9H03O5ZcQXKJXZ5PvLF3O%2B10cJuU8zRj2LweCezU0XynJRfY3LDk4%2F3Zc39JLg%2Bn1e1x5a7ApvkwG%2BMBSU5K%2BtNzUgupIkzSPv&X-Amz-Signature=e9341817207c8dbf936dd34e5c86f5b4ae011ee5080e6ca59df28f7e712ebbef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IBPAIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXL7cCpOyQG3%2B%2F2dSxiZautwwJuxPg7Lq7uekHmO%2BN8AiEAhZ7gGe%2FGl1aRvnAcnRAvZxc%2F9kDVpY6KSjD%2BVUTxYOkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpENMoalbJhbZHKcyrcA2kFfa8FXRRMCA0YjpChmqviqSbljb5YoQl%2FjK9Ig8YAeWPeJOXxrN30xRHifZRa2SS%2F7rIEwH9OVHx0aTy4sw%2B2D99fEM6KxJDL41TaevaCZolLrHtGTs%2FvjymyzQTZivVTsHsK5BH23ll9LssuORm49rI17vVxRFV67AzQmVqWKK2cB9lA85BJMDJAJpruWzqTHxNVzthT3vPlz%2BWgafDnVcU24hBWVnASzDfA0bazg%2BXX7k5w%2FYb36WiJwfWDNhDbmVY%2BY2ARXKNuujMMzDs%2FO49hIzUw1HLVmec3TbTDr1GHZTLSKTWKL6uggIQ9Zvd%2FByBrScLat8NyKp8lB1qS7Mz9%2F2ky%2Fl1SyVAmBqojZ9ZnM9W7Ovz1%2BdB%2BEw2WsEZmNZvlrIk6BC3dxe4Oa92YQ6EshX8Q354ZlktHNNBSC4zZMxdKeXjNjoI3NxVQhKWghUfRFZC%2FIgl1RPYvcFEW7fDE4h7AnWG%2FloyG8i4kf7KLLzPhKu1tMTCNJJhbU1UMqjeomXb%2FtlwfHLHnoby15SAlCzBGdOd36DOAEopHQLG3uPZNhyAs1GxEvESktoVTYbz6WL2pl9fR1Zs%2BW7GwpkEr%2BMoGlPUCMZkIYb13Rrh1OgncKcB6soOVMKTG6rwGOqUBTAoIbRmGQ%2FD%2BJxg6pehUYMLRZtRSf2ATjNfaG4aFL3mdcAR7dcyQ7pI5cY39BMJHg5L%2BcnVD1vXauidFuVILuzUXOeiC1B%2Bi9jvZXCJVOc47rUbS6eFRQRlcWRVrtKCL20mbyMrPU0h%2FoIhUG2inSx3vYVol2W1wYvst1GUJTF0sur7SCcExsA%2B4kQK1ka%2B%2FoJ6TopDSHqfaxSVF87xPUzoHlrB%2B&X-Amz-Signature=d343091e1f90c0f8905c589c934e533fc27dd570830dec83704c9eebbfa8a243&X-Amz-SignedHeaders=host&x-id=GetObject)
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