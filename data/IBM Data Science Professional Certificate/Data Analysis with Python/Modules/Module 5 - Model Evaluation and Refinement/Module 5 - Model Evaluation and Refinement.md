

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=69dfbe0cb5c29c9b742fb6706ad1fa965e9b65a8c07bdf9c494e094cefce0d17&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=539ad42aaa0c3b8e9e23d8090462eb222701c687ac820c4587680ec9618104b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=5d2f1de7b2888c0133f192c9b035454c1a0c31d850d15cff43ae6ee14db71b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=4c208bdef25961187863ebf8e4f24e0d5608c5d4dbdf2cc5e4d58b82bca6c1b2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=79451fe5783e015cdd492cf8af56b749582f458ccae33cf25117dd56214c74c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=a3d9b0eb5e8924664a35005f57837dfe2102514b2321fa0929369308f9fa6820&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=8600784b8b7c1f1bb805af2341a11a2f12189cdfce83e17ce6409788062bbd41&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=a2746a308f2a70c5732ae1a3cae1cfb26ac2f20f051b10d7d542a4405db9d9ed&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=01b23bc70401d8fc72cfc304f7fc308183b41d53b4a80aed85bf2266caf8506c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4VZMEQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGr4AFFuNOfImZ4ngCn1cm9lE0U511G7TY7fxTPvY9YxAiEAry5onOrsNAJ56oSc0J8xtceFPvsTgp4Uw77Zr%2BOqYRgq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDC8VWjzm9IM4cZKnGircA5zTj7AbaM5wWizdWgdG3nVoLFgVbVyQM2trXqGJLw3ons7sEgeZRnoHrGd75l4V8mQusdybMkTfFIQtwp6zEnkdcq8ZgTA2unOeoJ8isddypSLaBGCCGksJVpnqX658XcE7EXOHCRyFa2MnRewUrKZ8%2BchwTSClXns8kGipXd0ni%2BUvC2xln%2FxER6R71vDdIeAwL%2FNK0sEHePuQZWFtRMoPzSkuztUYy9YBlnJoxyLoIZJiN9MzauQNzSRvSN%2By8Do13O89HTR5wtQKEQ1M2UEkp1ZzcJ14k8IGVvpmqdVOm2RoCsscO1c753aH3D%2BVeY50aIn6zxuKhTjA4GB7l3CAXT9Ol3tRls5EahA36joSrunL%2BQMckHOj7KM1txqLHtNa61pqnuvzkvMom09AWVOirj5WeXWwwAP98wuvDAJTEQO9KkhSKvcnb3dZWWPEdSAa1oU8wP%2F914QBDOFFL9yScrMz7AZhnHU71JfCxV9M5chGXltaNueyobf6kJcpqMn86GmaerwwhErabiwyEKsbD9kAvy%2B56%2B4rl2Ea5I4%2F9xu3S15Rl7cP5RRGqD7XVbRc1XSAIdy1iA3bk7yD%2FiGc6RQPal0TGnqlcZATjlgyB0NjzM%2FDN9ZJk3vrMKyck70GOqUBhNOud2DKKywMMd3pCi9QhS2HMe4c3eyDhwHYdSnvQ%2Fp9B%2BiPgY%2F5tBm39EYvVNGsUkFwW2ItvbdCThFpiG1opc%2FoqaYvBv32ZIP7jmdWEwhYc%2BwEWDnAjeL6Jr%2FsA64NMykhEWbeXOcnf2SNiDygm3UExyniF4GtVUjtVx9wQrlW8dprGRhE7VZEqXb4xhXMwoDgyn5aKYXLlHckYkBzf3CSxGlo&X-Amz-Signature=068780f873a23163583a7586acbb3058c59f032f95a830f07c75d51586c88699&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4VZMEQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGr4AFFuNOfImZ4ngCn1cm9lE0U511G7TY7fxTPvY9YxAiEAry5onOrsNAJ56oSc0J8xtceFPvsTgp4Uw77Zr%2BOqYRgq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDC8VWjzm9IM4cZKnGircA5zTj7AbaM5wWizdWgdG3nVoLFgVbVyQM2trXqGJLw3ons7sEgeZRnoHrGd75l4V8mQusdybMkTfFIQtwp6zEnkdcq8ZgTA2unOeoJ8isddypSLaBGCCGksJVpnqX658XcE7EXOHCRyFa2MnRewUrKZ8%2BchwTSClXns8kGipXd0ni%2BUvC2xln%2FxER6R71vDdIeAwL%2FNK0sEHePuQZWFtRMoPzSkuztUYy9YBlnJoxyLoIZJiN9MzauQNzSRvSN%2By8Do13O89HTR5wtQKEQ1M2UEkp1ZzcJ14k8IGVvpmqdVOm2RoCsscO1c753aH3D%2BVeY50aIn6zxuKhTjA4GB7l3CAXT9Ol3tRls5EahA36joSrunL%2BQMckHOj7KM1txqLHtNa61pqnuvzkvMom09AWVOirj5WeXWwwAP98wuvDAJTEQO9KkhSKvcnb3dZWWPEdSAa1oU8wP%2F914QBDOFFL9yScrMz7AZhnHU71JfCxV9M5chGXltaNueyobf6kJcpqMn86GmaerwwhErabiwyEKsbD9kAvy%2B56%2B4rl2Ea5I4%2F9xu3S15Rl7cP5RRGqD7XVbRc1XSAIdy1iA3bk7yD%2FiGc6RQPal0TGnqlcZATjlgyB0NjzM%2FDN9ZJk3vrMKyck70GOqUBhNOud2DKKywMMd3pCi9QhS2HMe4c3eyDhwHYdSnvQ%2Fp9B%2BiPgY%2F5tBm39EYvVNGsUkFwW2ItvbdCThFpiG1opc%2FoqaYvBv32ZIP7jmdWEwhYc%2BwEWDnAjeL6Jr%2FsA64NMykhEWbeXOcnf2SNiDygm3UExyniF4GtVUjtVx9wQrlW8dprGRhE7VZEqXb4xhXMwoDgyn5aKYXLlHckYkBzf3CSxGlo&X-Amz-Signature=f264d911692c106ac883e2ec89dec13c9a67b9f5f1003033a59adb50fd0d5068&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4VZMEQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGr4AFFuNOfImZ4ngCn1cm9lE0U511G7TY7fxTPvY9YxAiEAry5onOrsNAJ56oSc0J8xtceFPvsTgp4Uw77Zr%2BOqYRgq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDC8VWjzm9IM4cZKnGircA5zTj7AbaM5wWizdWgdG3nVoLFgVbVyQM2trXqGJLw3ons7sEgeZRnoHrGd75l4V8mQusdybMkTfFIQtwp6zEnkdcq8ZgTA2unOeoJ8isddypSLaBGCCGksJVpnqX658XcE7EXOHCRyFa2MnRewUrKZ8%2BchwTSClXns8kGipXd0ni%2BUvC2xln%2FxER6R71vDdIeAwL%2FNK0sEHePuQZWFtRMoPzSkuztUYy9YBlnJoxyLoIZJiN9MzauQNzSRvSN%2By8Do13O89HTR5wtQKEQ1M2UEkp1ZzcJ14k8IGVvpmqdVOm2RoCsscO1c753aH3D%2BVeY50aIn6zxuKhTjA4GB7l3CAXT9Ol3tRls5EahA36joSrunL%2BQMckHOj7KM1txqLHtNa61pqnuvzkvMom09AWVOirj5WeXWwwAP98wuvDAJTEQO9KkhSKvcnb3dZWWPEdSAa1oU8wP%2F914QBDOFFL9yScrMz7AZhnHU71JfCxV9M5chGXltaNueyobf6kJcpqMn86GmaerwwhErabiwyEKsbD9kAvy%2B56%2B4rl2Ea5I4%2F9xu3S15Rl7cP5RRGqD7XVbRc1XSAIdy1iA3bk7yD%2FiGc6RQPal0TGnqlcZATjlgyB0NjzM%2FDN9ZJk3vrMKyck70GOqUBhNOud2DKKywMMd3pCi9QhS2HMe4c3eyDhwHYdSnvQ%2Fp9B%2BiPgY%2F5tBm39EYvVNGsUkFwW2ItvbdCThFpiG1opc%2FoqaYvBv32ZIP7jmdWEwhYc%2BwEWDnAjeL6Jr%2FsA64NMykhEWbeXOcnf2SNiDygm3UExyniF4GtVUjtVx9wQrlW8dprGRhE7VZEqXb4xhXMwoDgyn5aKYXLlHckYkBzf3CSxGlo&X-Amz-Signature=420ce365c9ee03f2d4ba03860c46d58918d399e1fc2bfa6b606bad6f8e93ef62&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=4320e839b8cf83b39aa912df9ba52cdb1664b1b1615503b166b70fb846d3604c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=adcd20d1243c6c7d5020b2bcadd2a438093d534f1ff71e331c508a99cf0ddf8f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=c75c470114fe41d7f83d65f14507fd8a346289f06078048b6e36ac8e1cb96d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=e4c275e08836900008dd3e3b77d10c928e6fe2bacc29ad409707a498cb288d52&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=6049cdb11596d2bf719e30bf02e0b8908c7bc3017fa463790f6fe6d962b3ced2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GB5STNN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCEtj3QKql%2BQp7oJWcTcTn%2BxfHp5p6N3bqWFK1uKeebAwIgEHeHyKbmV5xzA7Gf078AOM8ra8bSdWIC7jOkcQkuVMkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDP49RZ22WZRoFtrU2ircA3XSiQZ%2Fq831yurydn5jNSfVQx0FQHic2DXkYG3tHx0zkSo4AQ6kBsLhmzR40Ed7Lqs2iSob3vBRTRWqCJKZCyKFERabf2M2%2FhH6UTDx1g4ZXbqEhR5Je9xo%2FlRwNd8MEwRQ5Z7UXuUHM5aRxuaYpk7cd1tpGUobhufijROKXK63aMj4NyRmmmFfRu6PtlhuDcnbUuYGc9FjaOjVmoFchtRdKL9SIIbXEbA2DwbmgvVqkjbgZtBBqA7umk2zheAQ3H0bYpmFyyxNbnpQ%2BYN0QC8Kz9Nco2EunBs1iWGiT0RtC7z3PYbPRfkFq7EvKyv5mLQn04yItLWzPEhZN8xEyS8TC5kmEF4b4C3Ip4ueYd1OzXVc18kqgqVZxwBz7z6yBEu5WMaT3JHCBhuCAh8pK9y7%2BIWlzzrfLxjwV2Zieas4gFHVB%2FOQrvBt18sE8WQjNhGXHrIee4hH2i%2FTRV%2BjGrymnJFs%2BLyspCmB5rGrVCG4JXPxrjtlfsHp1SFApLpd9YW3GGidlF1fVcKWvS00Kvx6rz7OTcieMIUj3y6h3zCnGHwJfUjZZ%2B1X2RoC1fLHdA%2BWUOCe7ZqyIxhFW4K8uh2%2FwvxkSKwN7ZGAcwxtHhc8DBflpMdOLjLL2WPNMKyck70GOqUBTIJOvBvEuSQqGGJnWHX1aDV24kLa6V1ELhJ9My%2FT%2BDSHrnk4I70JyrRWuxzZvmB7ylhPIZ1EuLQMZQG1A540nKlmNX%2BaSTGg%2FEAdZp4Cj3lG49Bt3SS7PbhLz9PCSjOZiFO%2FvXvmV%2FK61%2Bc9RJoC5hnqnxCaPUjelGuRiFjCvHdy07yco8q9But1Fm8U6CuMLP3MVxVxgnmAoYABh0iRezkZC0oW&X-Amz-Signature=5d63886cbef002147c9ac42aee65f6d5f7bbbf836edb625b73024024fa8d7d07&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTPBAAS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFfLqfN3lCCdoiitvmXpTH8xaPgIlhC17v5FSeJIdRyrAiEA%2BfWm5wKx7Xu6OUbptu3UmJpPyn83iKplkNFYarqgYUAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDBlVNnq8tsoIIwt%2FYSrcA%2F3RlOuHULh3WZFFmv9tVKzt2a9QMYFuAyRcy3Zv6N1qDb2qY07%2B1DNhGzl0EZmDQkDWr9fSt7bBimjUmgs6qQ8Te27%2Bj6sAAnMnfeoA%2Bl733G7eF%2BTII83k4wUbDdXgLCwVC7ksrrdim0SawX%2F9dOP1cKH5ZVa9EbY8Kxp%2FfK6lvCk%2Fwt%2Fv3ohw3awCoYvM5UHYkQzTO1GYKn8%2B0wG7UMta0y3IxY8%2F%2B%2FSF4Lm5rHZRsvVHgeMeOdDDrWJZFvy6cP7zIvD%2FI8PSL8k93yVHk62jy3uEbntB8R17UulI6vW0DpVJ4B6kNTtyQ0koPaEVIjWkhoFlH7NpwVmqvINdyYszVMh2DVvaM2Sz2Plc39RaAu79eddI%2Bx6ytGRe9BZMUVTNhGz2wlUJEB88eCXCVklRH%2B9%2FqVIt9pBO9j5sRj1ihLw%2FtlrnJM5c65OivHFirYMMi%2BjkcuZZs9Dv%2BaP1oT1rNEjDRKyhuDzXFLXUTjNonlUduQlG6jMlpyixYhhK8G7oethBHcahQ77Ypjk4C%2B8LSGHKZS97rKGPyHLvdZTiAqVKs3YUg2K68yDXHuvbfBHBx2BGLMDQUPJqKLiNLrxwPWZNVrTC%2Ba629Wr4R92Iyr7rRawFX3M0b4nVMKGck70GOqUBPesRELt5ZTlPpFoDhIQ9bVI8ZnVIIqqZblJ%2F5os1TWH%2FstTiSamiHrL3OZv4Z0zEcFqviYNhzC6gY27A%2B%2BkJugvBnPOYAbBnRYa5DtgZb7DwgTO1X92bHHKV4%2FFgKfUgagMiucf6I6G9Tq7ZArohnLaf2Aww8oHiwwnz%2FHh5UegQTuaYyv%2BCrqq%2B4Drb7pO4rYUYwrCw9c6XZHCe4s5bznlA0Lnh&X-Amz-Signature=42860a2ff7761c3a9d3a4f2265d2617f61b559578e84ee96cb862f36d7f9e750&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTPBAAS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFfLqfN3lCCdoiitvmXpTH8xaPgIlhC17v5FSeJIdRyrAiEA%2BfWm5wKx7Xu6OUbptu3UmJpPyn83iKplkNFYarqgYUAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDBlVNnq8tsoIIwt%2FYSrcA%2F3RlOuHULh3WZFFmv9tVKzt2a9QMYFuAyRcy3Zv6N1qDb2qY07%2B1DNhGzl0EZmDQkDWr9fSt7bBimjUmgs6qQ8Te27%2Bj6sAAnMnfeoA%2Bl733G7eF%2BTII83k4wUbDdXgLCwVC7ksrrdim0SawX%2F9dOP1cKH5ZVa9EbY8Kxp%2FfK6lvCk%2Fwt%2Fv3ohw3awCoYvM5UHYkQzTO1GYKn8%2B0wG7UMta0y3IxY8%2F%2B%2FSF4Lm5rHZRsvVHgeMeOdDDrWJZFvy6cP7zIvD%2FI8PSL8k93yVHk62jy3uEbntB8R17UulI6vW0DpVJ4B6kNTtyQ0koPaEVIjWkhoFlH7NpwVmqvINdyYszVMh2DVvaM2Sz2Plc39RaAu79eddI%2Bx6ytGRe9BZMUVTNhGz2wlUJEB88eCXCVklRH%2B9%2FqVIt9pBO9j5sRj1ihLw%2FtlrnJM5c65OivHFirYMMi%2BjkcuZZs9Dv%2BaP1oT1rNEjDRKyhuDzXFLXUTjNonlUduQlG6jMlpyixYhhK8G7oethBHcahQ77Ypjk4C%2B8LSGHKZS97rKGPyHLvdZTiAqVKs3YUg2K68yDXHuvbfBHBx2BGLMDQUPJqKLiNLrxwPWZNVrTC%2Ba629Wr4R92Iyr7rRawFX3M0b4nVMKGck70GOqUBPesRELt5ZTlPpFoDhIQ9bVI8ZnVIIqqZblJ%2F5os1TWH%2FstTiSamiHrL3OZv4Z0zEcFqviYNhzC6gY27A%2B%2BkJugvBnPOYAbBnRYa5DtgZb7DwgTO1X92bHHKV4%2FFgKfUgagMiucf6I6G9Tq7ZArohnLaf2Aww8oHiwwnz%2FHh5UegQTuaYyv%2BCrqq%2B4Drb7pO4rYUYwrCw9c6XZHCe4s5bznlA0Lnh&X-Amz-Signature=b81955b48afdc9a05324b8bd3fa75b0c3382e0ebc6c99200cfd95af6952077fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z3K7HF3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBctkSICQSOD1XHaVsmzLi1yGUGX5JOl7y549Sst45rDAiEA%2F8Qta3TpPXaETAO8UK4dBlFdlW4JeE5EqtRqvip9He8q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDESxDnuYPgASWYkrzCrcA2HZwhWSYJBN0DnRNVkLs9TGbI%2Bmugt20prDtHU8c2chk03%2B%2FyZHY7fThzOf5e9OxIeQ3QPmYLa9K1IWmLXsqyx0uoSACHg07xyv4h%2F%2FdqPCHTVNsH0B58Me%2Fue%2FouF3ECbrII4%2FcJWDnyFOl3FD5gNjcGwr9HNBA7SeX7XOEBViWQYE2mFox501hGmVWatm%2BVxK%2BOzbuZ0fgCkFc14QS89XRFeCbpLuaLteN4eM9wSiTWrquW%2FjV73FT6Ye%2BsfSysBI8LH7TRMiYaQUJGOXft0jkfn44oqvh%2FPQEonIoBTvDNN3eh92RlhlyJUDH6nobUxc7%2BB8ShKPoU%2FDTd%2FoXPjgN0pSpSPD%2FMbAsl1g2T1SyhyduZs2AJLjrBBzECo8NMi1t%2BedX4gwfl9%2BPIG%2B51bZBFDIdnX22fHM2WGsby2J1tYNFS8m%2BgaX6YqI7sIMfHRh7IYbpfRBWzC0BYG2djkIkn1jMHMyWO65AqhPH3OYzq9P3hDtY1iqvumPrKHHZSsCuAbq6WTCkdJB%2BNNegfuxxr0kuaBuhLOOeWBkT%2FoIIpAnbkVEUtGdRkasTo%2FF6CPUKeVHzaKQh9tsoT15yO0Yh3jxxVKdmKtWyuNpZO6XKOX%2BSO8h4UJZf0neMI6ck70GOqUB%2BYa0TQzU1VJk1b0URMvxnD14%2F5PJi5nLJZLdVEM6dzXYpHsWGCWkRasqbm%2Flm0Kl26sOQDGSkk%2FV7r7WNLfUAdCKxRztuRB53FBHEvNQqmypiMcRImvb%2Fl%2FOtq1RPAWY8nV1EGhGOBgC1dxM9CTPl%2BviEdwLyPdO1UaAQS5l2LA06IZ18WKiTqi8tHEyyuyiQhKCCxDG00eSYriPwlqcqFPcN3%2B0&X-Amz-Signature=ffdef756a833ad9bbcb6363eccd6544b082a78294eb86502ae1e9b138d206256&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL6GFQ5W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDW7F8PF923OmfGrpEGp5sJdJsHkBQEKmDN54JCi7ZhvgIgMytgKBwFzfJ6FfKLU8H3JAk9rlkBvewKaaEyPD2daDcq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHgnk1gXEIu3CeSscCrcAz%2B1%2FLCPCefFKwlFtP%2BCgWQkonezprWKp98xUih9yeyYdJjZL1LQHJ%2BP7ikYKBKrCbYTDEHuSk9nM17vy53X3%2FRIsHY0o7n4U47%2FiVc2OEd11CdigVhLP08KkZ5pVID2f8pZxdQ27JMo1sk3rt1T5ljpbbYjvA%2FmCE3riHibgXVcrYuhSuvSPa5hVvKIK2Aralo%2FVXeSUQgvtYOcJUI%2BHgII%2FT9X4TZnAiZeUOpsBTbMVQEWlMAhHgkKynFX%2FBSJFiKhEt6HhtJCfuiIUphSDB7HJpe5XjlyYTs8Z3YcLh90Mj2f0%2B%2BkSswsT0%2BVH9EiKDsHph5sUle3ezXw58F6Tk2g5FEcqBdNsLqldzCRg7G%2B0LeGJrQg9R9ThAa7fliGM7ATaeueMYh%2FRRUcbVss72uMZYHjHZxOUCA%2FCEQodSYWFNlzxPjG3fkT%2F07ka4UEaiGOoljJaMu%2B2kvcdmWYe7zOSYVRF%2FWjxcnnFT%2Fg4rK7bEcNzFp4EgEyLNK94IuCxeSh43Np%2BT0%2Bjca7pl9wU69zqzlnZ%2FF48QN6BAdJ%2F%2BNLcGpy%2Fq5NVzofhRzhxNZlxtzJN%2FT1Pk09%2FjUT7JP%2BqJgap5cf6TwEpEnZ%2FQlL%2BOgWkSKqU3Irm%2FBmpfcSMNKck70GOqUB6htbkPu62J2YzzaDWJV%2BEBV3DCevbRhpx%2FJppNeNxYL2QSVqbkcVVv6KVvXZ9veAPiIoIvJ1I8BSdPgKrSOu3W5mnHQ0fxZqw%2FDJtZOgqSHT3888zqqumyGYUNcqqhupBGU%2BdchwAEsG6Sev0oBGneHXlf0ewrR2RYgbMAhRLjtI5LlBKj47owBKFGmgbwmC2iFgjW0r5OiQxpMJ6YndEKkvRpek&X-Amz-Signature=6584870b58506b11cc9144b37aed211aba56e206b1c65269699ac2a8616de50a&X-Amz-SignedHeaders=host&x-id=GetObject)
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