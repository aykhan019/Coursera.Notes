

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=1914df69facf6c48011ab6612fc9eb8bb35a31c2f7ad20c9c20b07301e00c6f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=ba0b88e748258bdff2bf7ddc660ea059edf74d8516b855e0e8c67788869ddb76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=8069a9d01f18602a98b8c9491af8755ba1bbd8a354c7b28b819daf0415682118&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=e64532bf71825e12b351c453dcb04b7dbb4eaef0bb638b0eefdb55d3dc7dfa71&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=8c693a37772cd0218a9c300f9790888ce18c011123831ebe558e896d0b31109a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=953fed151e483c536d570e74763b3de2cefdbce036306545e0d81bbdd020ac41&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=d7e523bbdbdb845e445c6b5526e20ef96709c77533dea5442e73ee18cd7641a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=2956bbe632d56a254054d8dcce31fa3b3eb260f9a1bad625348bd48470ed9761&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=492b2abf06176279fa9df30798adca59af67c7ae10f91c956ba5fc8f1ee2e417&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655MODDWH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwCz41y9KoEuB82ap2J0AinYtpF2xekpMUT5nbdRwdPwIgZHWIKTV4VH6tDVoJixgoYO84LCf4dqh%2F3tmbdrplKNUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC7sUee7e2PazlWJuircA1sCPJT5GavTlzCmbEoxdus1KAQUgB64ryo2WD8U%2BhIdr3P%2B0do0XzPHePChjU82JpdxgBagsjNZz7%2FzOM8wboD090n%2Bf4A3mNynNh5bJPfrAgL6cr6ttnu9axGg%2B%2BEfT6SBeXwYjvo9Yq%2BrpmXsmligudPanlt93S7YCsJfq5ZRNZLRxsWG3%2F65KSWREl%2BPdy%2FymImqwWEIdbGRLdtRNlCJE3UTZoUP91GDQyW21W%2Fi7UO6oc0i4fItKBMIxAaWxJtIvnawoB9v31IH4E4dxfgggb09r%2FcYkfAGskwmMuNRIDTCTRQZEEuRSxjqrVOJqIPMp0zWvk4GeGO6HVihGLi72diIC3XQu2lZb4GX1TwWViaCo8fXSV%2FWpFdS981a5pEo56AuRrbuRxNpp3mKyV96eavNoCtDoII3DDXj4Z8nF1ZCPLLnYlyOeCWMLC4PM%2B%2BdIp3TRX8Up57o%2BVpyB37a64p%2FDLDYTvQ0s%2BAagpt6XghB1PkVAfotxWovB7JQVmvPKzhfJroerZfdOk84ItCoiQjppHLNm9WalvYMYsUW%2BTSMzf1o6R8ZLfHLfFZgZNpdlXFUHvDawdFUBcOgpuR4P4Q%2F3%2Bakezbw4Aw3LDUyc9ZPgQVi0cdt17cEMMD49LwGOqUBTnRDoXASiVs6kSK5XslTFiidkTUfRp%2FiHov3weil02SDcnkz0ZzbA07UFiJ9udOboHPK6xsThieEzLITwiWWe2BzJkIcD5UKb%2FLip8tUq44jYqhPjoNVuUV8JNi%2FkypY2P%2BJhDD8VzaAsXU%2F%2FPbXJ9igB%2BCQReny2XlPyitacjAfGG%2FmmW2ia6OejVwiyN%2BPgTMj93Ksix6QtS7PH%2BScZGK3AT5p&X-Amz-Signature=a4a7bc8a8df66f1e79ec117cf7068b277d6129415d144b47da6562f4d5803e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655MODDWH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwCz41y9KoEuB82ap2J0AinYtpF2xekpMUT5nbdRwdPwIgZHWIKTV4VH6tDVoJixgoYO84LCf4dqh%2F3tmbdrplKNUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC7sUee7e2PazlWJuircA1sCPJT5GavTlzCmbEoxdus1KAQUgB64ryo2WD8U%2BhIdr3P%2B0do0XzPHePChjU82JpdxgBagsjNZz7%2FzOM8wboD090n%2Bf4A3mNynNh5bJPfrAgL6cr6ttnu9axGg%2B%2BEfT6SBeXwYjvo9Yq%2BrpmXsmligudPanlt93S7YCsJfq5ZRNZLRxsWG3%2F65KSWREl%2BPdy%2FymImqwWEIdbGRLdtRNlCJE3UTZoUP91GDQyW21W%2Fi7UO6oc0i4fItKBMIxAaWxJtIvnawoB9v31IH4E4dxfgggb09r%2FcYkfAGskwmMuNRIDTCTRQZEEuRSxjqrVOJqIPMp0zWvk4GeGO6HVihGLi72diIC3XQu2lZb4GX1TwWViaCo8fXSV%2FWpFdS981a5pEo56AuRrbuRxNpp3mKyV96eavNoCtDoII3DDXj4Z8nF1ZCPLLnYlyOeCWMLC4PM%2B%2BdIp3TRX8Up57o%2BVpyB37a64p%2FDLDYTvQ0s%2BAagpt6XghB1PkVAfotxWovB7JQVmvPKzhfJroerZfdOk84ItCoiQjppHLNm9WalvYMYsUW%2BTSMzf1o6R8ZLfHLfFZgZNpdlXFUHvDawdFUBcOgpuR4P4Q%2F3%2Bakezbw4Aw3LDUyc9ZPgQVi0cdt17cEMMD49LwGOqUBTnRDoXASiVs6kSK5XslTFiidkTUfRp%2FiHov3weil02SDcnkz0ZzbA07UFiJ9udOboHPK6xsThieEzLITwiWWe2BzJkIcD5UKb%2FLip8tUq44jYqhPjoNVuUV8JNi%2FkypY2P%2BJhDD8VzaAsXU%2F%2FPbXJ9igB%2BCQReny2XlPyitacjAfGG%2FmmW2ia6OejVwiyN%2BPgTMj93Ksix6QtS7PH%2BScZGK3AT5p&X-Amz-Signature=61a0e65c5b07468ac14979b1aeb481d86ba81a96a055679de2c9c3c1f2a88906&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655MODDWH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwCz41y9KoEuB82ap2J0AinYtpF2xekpMUT5nbdRwdPwIgZHWIKTV4VH6tDVoJixgoYO84LCf4dqh%2F3tmbdrplKNUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC7sUee7e2PazlWJuircA1sCPJT5GavTlzCmbEoxdus1KAQUgB64ryo2WD8U%2BhIdr3P%2B0do0XzPHePChjU82JpdxgBagsjNZz7%2FzOM8wboD090n%2Bf4A3mNynNh5bJPfrAgL6cr6ttnu9axGg%2B%2BEfT6SBeXwYjvo9Yq%2BrpmXsmligudPanlt93S7YCsJfq5ZRNZLRxsWG3%2F65KSWREl%2BPdy%2FymImqwWEIdbGRLdtRNlCJE3UTZoUP91GDQyW21W%2Fi7UO6oc0i4fItKBMIxAaWxJtIvnawoB9v31IH4E4dxfgggb09r%2FcYkfAGskwmMuNRIDTCTRQZEEuRSxjqrVOJqIPMp0zWvk4GeGO6HVihGLi72diIC3XQu2lZb4GX1TwWViaCo8fXSV%2FWpFdS981a5pEo56AuRrbuRxNpp3mKyV96eavNoCtDoII3DDXj4Z8nF1ZCPLLnYlyOeCWMLC4PM%2B%2BdIp3TRX8Up57o%2BVpyB37a64p%2FDLDYTvQ0s%2BAagpt6XghB1PkVAfotxWovB7JQVmvPKzhfJroerZfdOk84ItCoiQjppHLNm9WalvYMYsUW%2BTSMzf1o6R8ZLfHLfFZgZNpdlXFUHvDawdFUBcOgpuR4P4Q%2F3%2Bakezbw4Aw3LDUyc9ZPgQVi0cdt17cEMMD49LwGOqUBTnRDoXASiVs6kSK5XslTFiidkTUfRp%2FiHov3weil02SDcnkz0ZzbA07UFiJ9udOboHPK6xsThieEzLITwiWWe2BzJkIcD5UKb%2FLip8tUq44jYqhPjoNVuUV8JNi%2FkypY2P%2BJhDD8VzaAsXU%2F%2FPbXJ9igB%2BCQReny2XlPyitacjAfGG%2FmmW2ia6OejVwiyN%2BPgTMj93Ksix6QtS7PH%2BScZGK3AT5p&X-Amz-Signature=b5cd0efc3cf4363784a4a35fb5176b64849574cf0eac1f42b1fcee624da692e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=b7ae2ba4c79deb81d4fb489f239095b748d04769bd198b059d7854630ba52b71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=aec1ec01d1755c739002155185ffa3e68e190a12814f823adc400fd733198dab&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=83e50eb5762f7209cea3ca5e5626cd8c715a38fe58476199bd9d299748341845&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=f2078079f433bd45560067de083f99d9b8a49a333ce1088662f989f74a1596b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=be4ab5c1cc08e28ac8d1fa508de221fdb22c01a3743a202617f8252558c109a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUAZEIJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHd7Xqefvv4ZE%2F6SFYdVokswyOwAWtbw1wo6KJM9OdLlAiBwPQd5P3qrLcMXCZXAwFa49IRyY1VsRPbLZj465om%2FPCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcPKK2yXNoOO4oHwSKtwDAXh2MyBiCGt5RkUBDoj2ZxQ%2FvgtS4CUFJ0ZdRGv8GybnK1RNecC7wyuiDD%2BkyGfJp578wGbbPxvaRerMJaQWfYpsatLjjiou3teR4mxV8CcUE5aoXIgnhPjkBQcTp6LAxQLEIdUzXwIEfOf6w7ZnonRJT%2F3NZfN%2FW5UQ3WHWigZ32qbfz3jNrjbNkYZOCmnW5i4gnISVJiGeioaAN%2BZCV10yXQo8QfmGDJ0nnP3CQJCGi83YvPTwaaqGEA%2BMUOxBckAZCyyQiSVsn1GdGF7dk5iEZTlg6AxFPX8zA3RiA9fi4Nw8DaP1AKdXO5pVbmwhCe080qjhlXe1djv0Lf%2B7ezohQq0m5PUc5ubdnaKhK%2BgGbFe8SR7gLWKdOllp5Y%2BG5orKpR3lSUS%2BMc1Yy%2Bl42j1LiB8pmxPFB2ZwDpU0mCVgeOK%2FH8jwWClU7cRvKU41aagKNteKDhZI7rfAkSfqG%2Fd6DK9zUTF07xQnknu0TU6W4An3sY%2B1bFN3d182eHyiieZb3INU9kJyCRw8Zn%2BBM7vUuQBMsco7RFY3iJrzu6PRVTzuv2abBfrOHalZiYj%2BULbELvJudwWZUQIP1np6AJW3SPeq4HtOC%2FK53o0dnUtCKEUPVuVZTML8QtAwvvj0vAY6pgHClFefxRxrOGDYFXyFqKSaZGZU4ZiNO0XDTUHyMkrwPll8UEHwJBnlHs0%2FkWFUx6uGqQkjf89FmrdEJQsnRZ3Xp2vRmaaCePjkjoU%2BiWci7aOKIJC4N7wA8lLytZ6G%2F5UIeWY9KBEFJBCuOI5XByMkLVQO6Ew90ikVVnGYJ8xXAMIZDv1LHGyqNdFclMPhe0188bPMLq2NkcO5tBiHonXkZmL7W7b3&X-Amz-Signature=c28f1661b87a7fa6d3a2520a72914fc231a95203a5d331c63536e32f64138c6e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTOPEUVF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH5o1zCYUISQePw6MBGjLhqestPebSWeJCrjk56soefvAiEAjkAPBgY6nrZlfK%2FX2tM4ZcdFTg9cgpQRJQCn4VWidX8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDxsd9%2B%2Bgs%2FMBlY%2ByrcA4dLJlhA7usaUNqDIu58fWKd%2B0BuZE7M7S4x7032fxtUkpf8KHzPUIRulbecJUcLPTMYIeg%2FUxY9aA3zwmFwsO95YjmLFIEqWABzY8jxAFUcjfVegQ1ZIp21ufuKOm2Pm6DUyunV4ac2ecZs%2FdwEG3pyzsac%2BJu4kicvwzKT1ZYw2aXlfsJVUgB1Wsu0aCb%2F%2F%2FrutOoD3BvQGgbXNb0vAb29iSu6ay7FR8bbBYBb0QZCNvRT%2Bu5UJkbJBOXdi2EPcsi6lidI2wFC1KxZqrDnf%2FxBl6tGSDvFAS%2F5nfVh1LihcGNWOD7zLdjiVBxAb164oqgibrA3raOeDUxNw%2BJ2KA9v2oAHQnMykW%2FnZFqz2g%2FBDlsNyYMMBgfu2C7htRzDKMWpJwhsj2zKOILUTJPUdXX20d%2FAmKy1xdbIbW2BIOYJDg7KagH8IsTu94TZe4sTx6Fx0878Eo%2B4Iba3t%2Fkpj23%2FE9QfqIvEjTsmGd2cADFaAGJnwcTxLnBVjz2bOFUDdmcN2TnCPG6z3hKsdilPvh3966A9eb%2F4o8ch4bAk2JtDuKRGAX4xxl%2BQNp8dTGaOQVJrtO8seZzGxYaFhBh8X4XJ9jRI5iK7oRfKGPgURp5PI34Tvc%2FsDcM9AaT7MMrb9LwGOqUB8o7ySSq3NL7ZAY0FP%2FOzI%2By6MmoCk2aXKcWD85Usc2tJxwskLOuGhbfD2kS7ck%2FoqrT38nCuZfdxlYt8zkbn8Wo6TgG1Jg1Uoz%2BWVYayUtULRPm6pl%2FPOkiSsX0VdIV5uvl9R1ijoYFJpe43slxMuNFI7MlyOE2CPGi8120sqafTjRoMNkr6PdKzoRpNu90Ch%2FNENc8x%2BriZ3%2BUWTEVlL%2BpU1Osx&X-Amz-Signature=653248c70bdf5f8b2410aa4f609cab249c23015f1ab90c118dc21239b1a718d7&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTOPEUVF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH5o1zCYUISQePw6MBGjLhqestPebSWeJCrjk56soefvAiEAjkAPBgY6nrZlfK%2FX2tM4ZcdFTg9cgpQRJQCn4VWidX8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDxsd9%2B%2Bgs%2FMBlY%2ByrcA4dLJlhA7usaUNqDIu58fWKd%2B0BuZE7M7S4x7032fxtUkpf8KHzPUIRulbecJUcLPTMYIeg%2FUxY9aA3zwmFwsO95YjmLFIEqWABzY8jxAFUcjfVegQ1ZIp21ufuKOm2Pm6DUyunV4ac2ecZs%2FdwEG3pyzsac%2BJu4kicvwzKT1ZYw2aXlfsJVUgB1Wsu0aCb%2F%2F%2FrutOoD3BvQGgbXNb0vAb29iSu6ay7FR8bbBYBb0QZCNvRT%2Bu5UJkbJBOXdi2EPcsi6lidI2wFC1KxZqrDnf%2FxBl6tGSDvFAS%2F5nfVh1LihcGNWOD7zLdjiVBxAb164oqgibrA3raOeDUxNw%2BJ2KA9v2oAHQnMykW%2FnZFqz2g%2FBDlsNyYMMBgfu2C7htRzDKMWpJwhsj2zKOILUTJPUdXX20d%2FAmKy1xdbIbW2BIOYJDg7KagH8IsTu94TZe4sTx6Fx0878Eo%2B4Iba3t%2Fkpj23%2FE9QfqIvEjTsmGd2cADFaAGJnwcTxLnBVjz2bOFUDdmcN2TnCPG6z3hKsdilPvh3966A9eb%2F4o8ch4bAk2JtDuKRGAX4xxl%2BQNp8dTGaOQVJrtO8seZzGxYaFhBh8X4XJ9jRI5iK7oRfKGPgURp5PI34Tvc%2FsDcM9AaT7MMrb9LwGOqUB8o7ySSq3NL7ZAY0FP%2FOzI%2By6MmoCk2aXKcWD85Usc2tJxwskLOuGhbfD2kS7ck%2FoqrT38nCuZfdxlYt8zkbn8Wo6TgG1Jg1Uoz%2BWVYayUtULRPm6pl%2FPOkiSsX0VdIV5uvl9R1ijoYFJpe43slxMuNFI7MlyOE2CPGi8120sqafTjRoMNkr6PdKzoRpNu90Ch%2FNENc8x%2BriZ3%2BUWTEVlL%2BpU1Osx&X-Amz-Signature=72c728d8085a1005ab3696974511b6f768da4be500ddda8def300b7660f5a1ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNUHN25U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBJPuAV7b4wHG2mGBofUXqGnoCEtfujGHARX5VfU4gWUAiEAv%2BXKpfn%2BO1nzOqqSufJreDsyKST6DQgmUgrTE4KRL8MqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqItVZ1kt0eQlUXOSrcA2l0NGyEL7roJUqnqaRiTlfVQp4m6I5y%2BenrxOfUl0cknZSifDwAKaOSOTHdcAu6OAR8SOFFL4kU33U9QFSBHGvw2jgK2gDL7%2FzGNmmozxHAhVjvTtMWj03RGqG00SuTIjeoSfjaeoiQAlLj9Cpx7DDFnJUjE1dWxmuKbdqJ1uT989%2FtnEKWft%2FcrnlDAsGt52WSDlMO0vxHegdykazRiwYuVCuIXtJs3evXSAmQDkFXpkZh%2FBoRC4x2YOoPSiCzngxxU5ajRblnvPggNBNPu2OVcSLVWx8z0fKN4CLe3bg30qWUK332Int3PrDfvlKUubH2Z%2Ba4ek1SrcSIF8T7g81owNhq3zia2D4A2MqUVzdMutWtt70BJ34Hiw8ET2HP40deTX7YZ0XxntcPLBXsvKHbeZokE%2BjZbxRSFURjf5DVo8X9ZTmFLWd24Gz683%2BDKZsmWzyem6TKfK3zSHkdw0EHo6eRstSQcFxn8tIj5Np0oBATQVYZx9vm0wbM2i2PCbORrA%2B74UTkfIGLajjKAtgkQefEKqtH7Gh2KVqvMFZMkrFm4sIJGzORRHiZOD9HLfe1pEFwThq5kfxHj%2F%2BSeSXadSehW0SErgISPS7xCkvBPdft597g0uhs%2BOx%2FMNbb9LwGOqUBCPDBvNZuthJ6T%2BXmTUPu02hH%2Fqc1%2BzCZpt1MkqfPOklSNf0oYdpy0CXvvPgb4dnR9LtEme7BfOHgDrQ2lA53aoXCufOHTAOgXIj%2BVihO%2FbXqwb9%2BZwd%2BES%2FyAPZRiaaUyMEisxzKuusoQXMl%2Fh2agPVKyc6FBObnKlNNCqdJ2PB4F1j1kO8%2BPTyes1aOvgCJwluuIwBxL0Da0WUJri0828xe%2BcCc&X-Amz-Signature=fe98491a2b6b5c4d8afc1bac32659172058bb8901a7dd900521e85b1ed6fed8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EYIUW7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEg0L3lkSNZPjDCw%2BzerbtSKqGnzhbvp1VplvjjhJCuCAiEAjyfGRr5r5JH5aNrbNFK7EPCXojXxXVU%2BUyH59kHn52IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEOr3A4xJ5knBKRgLSrcAzBqp%2FsiCr1D%2FDroMGv%2FiXh6C0KScUIV0fr4VIvMccPFRYPHKyp2H%2BMuVrwoLFrnqZVIRZMDDsaVOG16f6ng%2BVx1UGuWpjklVOticbGI3nrur8zcZct5waA9RkblJ%2Ft8cIas5BjplfEdXBMfdD0zfUiizLvXpMgrTsU852mx1JJFd7HIwdI7vqIPgAZCCHbucRk3PPD%2B9YLVrR63xsweiCIUsOiuK3kWwSzBXLL5J3SrDWa7PK2mtCKrxJBS7SNiSy0SpKVKiJAlkRb%2BbbHdx6FE%2BdwKt7RuDXjLX2YmTckTnM%2BN4nm3wr2WRdYR2RMnDy5ZZLtCzIuX%2BA8W65lr5H5V2t76qla2PGlE1uhkJPNQg%2BUgX1GqDTWl3Fg59qMivgYaJKaa9JabXm4vDkaTD0YrxToxMQAePyqHPmHh9QR8y2eq1FB5RR4dRnXxDqKMrR%2Bc5AbYl9eQplH%2BDIs5rwqKMVJj4K3RjOO5xKvHHVnxLB37ZfN8Ygjb5iLwDgBHMwvw5HAkg8On0WPJILxNnRzPLZofbIQtfw9m3cStWWrja8ErTW2qCYEtS5mWi%2B7HZBLYlRYZx7uZUMCnHWh8%2FCUUGmePvjy2MBMDX%2BLZ9fnWHjpBsyOGLWmD%2BDcrMJr49LwGOqUBYaVw3SutxwMImAaOq1itOB%2B8oKTpyUVhBhX%2FZYaa4bUPvL1iVJbRV3R1cR5QPIRzC1aWSP9M4NovTbz8X2jcsAMxvlvbxMQe7NRFVz2PLaAfmvRvUVs9ojHiE0cXaOF9SDpzXkNPUsLWIV4bmZi2GBYBuYcFscdGOnyKA1N0zwf7lYKFk2TpX8egHN%2FdzPa9YwvTsrTGk7BhDLtAExVQAWPi0RFu&X-Amz-Signature=c84aa23fe3e7e527654ea9b83867f989b92b5e54dcf1e1b89d2c56b7eccd0650&X-Amz-SignedHeaders=host&x-id=GetObject)
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