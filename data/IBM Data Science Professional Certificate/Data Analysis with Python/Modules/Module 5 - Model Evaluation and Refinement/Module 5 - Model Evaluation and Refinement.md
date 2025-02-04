

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=e90b250112fc6e1fa3d53f781cf875c43588e08d98b0ecc0ba957b58b9e54af5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=ded4928dd60055eb401d6a4e3af1575e2aff3f72cd218c57810da73900a3cabe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=494f60b398597514efd46e59747b399e8fa02d8c2ab3eb7af0fa6f233dd95b06&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=297a7f005784301a88e15d77a55aec192baf6680196d420fba819c6e2b0c0dac&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=1686b89ad7d91f6f4a24e8c634cbc0f4e561f063c74ebe4c8f7a259388696acc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=6c9abe4c3c86176587d6d2dc44fce78a85085479eed2a2a9800e70cf422836c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=d378b7c65722cc14aa85a2300a88d41c23ad7719019bb2eebe6ecdacdec70369&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=6011410aac820ae45f81db9721232f420b878e3986dcaa09a4638e8c38674c6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=4c31b63fef554ae21f35da3e737d2813a76cf9d20cbae908071d2ab39dafb27a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHCO3HP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCx7kk6j7%2FweW5ODkcCYPBgWXSX2mUPynh3KW%2BfF6n4nQIhAKrGrxAwqXhA9rR7IlXPwfAA4wwJ56zFyHLBWwPNK3%2FZKv8DCCQQABoMNjM3NDIzMTgzODA1Igwe6J3hzsZ57CflpLoq3AOqefgdMB3UyKxuZVOCzYUCF%2BICh0hVxpkwT2bek%2B%2FyRfZ3wbrlAZwterPA2l%2Be%2FXE8tnrmkn2t%2FYpFDcMw%2Fr270lxmCyt6qQZEcRsOb8k5TNtHh6svYbMh8wyVIUkrzTaLe4Gc6pDqpDdgi9y1%2Fdha%2Bjsv3kxrXbISAzMMoCOL%2FCJ6VT6GIskE2Sr1gjAtxBGqW65jS3mFxUhA%2F%2F76TbRO15IszwJ6kxNwxCbpzC6pMxOwq2HliJGA%2FivVU%2Bjcxv83qCWt73vhkU1nPtoljSfGqtNhCvMMazKmEZVaZHx2XLtfNXpDCabiua1UY9k%2BWIsx%2F%2BgV%2FJMz1RlMa3qwIngManjnAt%2BQBzmDv%2FMwEk%2FDIHkUD34Q44Zb3wO703UW3A0vpuTZzrV%2BGsTdd7GJFVlnEOdZgXrwaRiC7XMiqY0l3yAcEK%2BwE0P8hab9nyoGBzAUxHUJm0eXNefhgKZ3WeFS5bPgC%2FfPjcjJhtV1fzFDkU5EHrTtzEhoHy%2F7qxT5MBFRE2cs8pEPOBZ%2FeuAhqRBzTLZsf0fUFQnkUzqAYo71VQG7JbStIlVHSGlOusDDBthDf9V0IWfoQo27nSNrEFJnpQi67bNjS55TjUb1qh%2BkKidxsdiEpMl9FeXRNzDvhIa9BjqkAeHGHgbwdLGsLXVXE3zh7hw00xgKs5Vo4wITYeFR3%2F7hgCZtGR3NyCUxrRTwxggEr2CS7JP72D%2FUMeXEHBk3NyNlTqm7o0vdZAelFLRzMt%2FgIa3uzXMFSQgc8lvXY%2F%2BJ5Xhh1cle79g62cNtqMl6Gqr0zKCyCRMyv%2FYLxN3sYYN0Sr3mvz6SRPbElXZajqRUHqwIywvSLXxoEY6BQym4tdOL3E2Q&X-Amz-Signature=9cbf61444f888f6c60749be38c9fc750e77d1dd94c421241da81114eac5881dd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHCO3HP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCx7kk6j7%2FweW5ODkcCYPBgWXSX2mUPynh3KW%2BfF6n4nQIhAKrGrxAwqXhA9rR7IlXPwfAA4wwJ56zFyHLBWwPNK3%2FZKv8DCCQQABoMNjM3NDIzMTgzODA1Igwe6J3hzsZ57CflpLoq3AOqefgdMB3UyKxuZVOCzYUCF%2BICh0hVxpkwT2bek%2B%2FyRfZ3wbrlAZwterPA2l%2Be%2FXE8tnrmkn2t%2FYpFDcMw%2Fr270lxmCyt6qQZEcRsOb8k5TNtHh6svYbMh8wyVIUkrzTaLe4Gc6pDqpDdgi9y1%2Fdha%2Bjsv3kxrXbISAzMMoCOL%2FCJ6VT6GIskE2Sr1gjAtxBGqW65jS3mFxUhA%2F%2F76TbRO15IszwJ6kxNwxCbpzC6pMxOwq2HliJGA%2FivVU%2Bjcxv83qCWt73vhkU1nPtoljSfGqtNhCvMMazKmEZVaZHx2XLtfNXpDCabiua1UY9k%2BWIsx%2F%2BgV%2FJMz1RlMa3qwIngManjnAt%2BQBzmDv%2FMwEk%2FDIHkUD34Q44Zb3wO703UW3A0vpuTZzrV%2BGsTdd7GJFVlnEOdZgXrwaRiC7XMiqY0l3yAcEK%2BwE0P8hab9nyoGBzAUxHUJm0eXNefhgKZ3WeFS5bPgC%2FfPjcjJhtV1fzFDkU5EHrTtzEhoHy%2F7qxT5MBFRE2cs8pEPOBZ%2FeuAhqRBzTLZsf0fUFQnkUzqAYo71VQG7JbStIlVHSGlOusDDBthDf9V0IWfoQo27nSNrEFJnpQi67bNjS55TjUb1qh%2BkKidxsdiEpMl9FeXRNzDvhIa9BjqkAeHGHgbwdLGsLXVXE3zh7hw00xgKs5Vo4wITYeFR3%2F7hgCZtGR3NyCUxrRTwxggEr2CS7JP72D%2FUMeXEHBk3NyNlTqm7o0vdZAelFLRzMt%2FgIa3uzXMFSQgc8lvXY%2F%2BJ5Xhh1cle79g62cNtqMl6Gqr0zKCyCRMyv%2FYLxN3sYYN0Sr3mvz6SRPbElXZajqRUHqwIywvSLXxoEY6BQym4tdOL3E2Q&X-Amz-Signature=394db5fcee0a570bb61f8e2d3336ca1c74689f450a08035a59aa3d72f1bc65ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRHCO3HP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCx7kk6j7%2FweW5ODkcCYPBgWXSX2mUPynh3KW%2BfF6n4nQIhAKrGrxAwqXhA9rR7IlXPwfAA4wwJ56zFyHLBWwPNK3%2FZKv8DCCQQABoMNjM3NDIzMTgzODA1Igwe6J3hzsZ57CflpLoq3AOqefgdMB3UyKxuZVOCzYUCF%2BICh0hVxpkwT2bek%2B%2FyRfZ3wbrlAZwterPA2l%2Be%2FXE8tnrmkn2t%2FYpFDcMw%2Fr270lxmCyt6qQZEcRsOb8k5TNtHh6svYbMh8wyVIUkrzTaLe4Gc6pDqpDdgi9y1%2Fdha%2Bjsv3kxrXbISAzMMoCOL%2FCJ6VT6GIskE2Sr1gjAtxBGqW65jS3mFxUhA%2F%2F76TbRO15IszwJ6kxNwxCbpzC6pMxOwq2HliJGA%2FivVU%2Bjcxv83qCWt73vhkU1nPtoljSfGqtNhCvMMazKmEZVaZHx2XLtfNXpDCabiua1UY9k%2BWIsx%2F%2BgV%2FJMz1RlMa3qwIngManjnAt%2BQBzmDv%2FMwEk%2FDIHkUD34Q44Zb3wO703UW3A0vpuTZzrV%2BGsTdd7GJFVlnEOdZgXrwaRiC7XMiqY0l3yAcEK%2BwE0P8hab9nyoGBzAUxHUJm0eXNefhgKZ3WeFS5bPgC%2FfPjcjJhtV1fzFDkU5EHrTtzEhoHy%2F7qxT5MBFRE2cs8pEPOBZ%2FeuAhqRBzTLZsf0fUFQnkUzqAYo71VQG7JbStIlVHSGlOusDDBthDf9V0IWfoQo27nSNrEFJnpQi67bNjS55TjUb1qh%2BkKidxsdiEpMl9FeXRNzDvhIa9BjqkAeHGHgbwdLGsLXVXE3zh7hw00xgKs5Vo4wITYeFR3%2F7hgCZtGR3NyCUxrRTwxggEr2CS7JP72D%2FUMeXEHBk3NyNlTqm7o0vdZAelFLRzMt%2FgIa3uzXMFSQgc8lvXY%2F%2BJ5Xhh1cle79g62cNtqMl6Gqr0zKCyCRMyv%2FYLxN3sYYN0Sr3mvz6SRPbElXZajqRUHqwIywvSLXxoEY6BQym4tdOL3E2Q&X-Amz-Signature=36a04715f1d9025ca7e24acb6787e20ad3b33b562d0a0ec6a181a030e5996764&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=40916427673293997a21843ee7045aaf1904f609d0306a9a2af101a04d6c2fc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=d22d1b477e2294ee9bc044165ce7ca6a3db2a4e4f3ba238f542526fd14fc82fe&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=1f1c846cc801ecc23461efaecec9e68d36b8cb9dcf7cb45bdf9d3bffc9735536&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=c6c9ead0b53b534a2aedf47f348bf0498d1ae4414d6b72c5435f1e0b9db805db&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=4ac988b0c9bc62be7ec0a0d7c5b6390110e5341bd4d0d9c51d880bb7794fb38c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RMSENJU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQCTPrDKROfTVOIR1bBHvdYah46cHC5Fe9Z0b3hiz3bqiAIgYLUcs1eE3vz%2FJWEQlejrys0vTkNeM8MLLfig3uri1e8q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDJFzOcfNmniZ8qeWAircAw%2Btd7E3LF7vDe54l7C0XOpWQffbxtVnVO6DD6ylJh5agEufqG1VJ6x7sAKg4%2F801zVdEzvf0jJzIyIGw7rOHR0bRku7Gz39OCVyniNeMR4%2FtzUK56W0oGj0nbeMw%2BKzbrgjqq5uXKsjYtVdVR3barEbWwbmrEOPn8rGw1n0IozDSXzeIfqyTGWKqHgvTQKRHgfWa1ikaG1lQ4mkBVLkq0yA4mlVExyE2sU6wtFwRXTMtzEWHKtrCSUoh2oppQmciWFZI3b0AVsJhvY1UQ38qrKTTPim3BVdUg1lv%2B8KV7uPs6j%2F%2BgHxak8kSz90RlFwhO4pbUtcYP9fHWRmhsWPjHZejRhK4%2Bb%2BsBPDD4axSakShqo1T9EmSGe29dA8Y8P%2BbUVTn1ls4j1fc4z89h4YFC9g5OFC4eLBG%2FXXjG0R0k8GXFLOLjfIxhh8iQSTPLUXQV9%2FCQzVFrx1dcWAUeyJD7zUXCjO2Pq93FstzHwXiJ8bmxLGTwvjQHK7Pp%2FkupsGXIj77ti4lOYOnSIcdgQqZi4nIPkeLMY%2BLTGFas8LZaDgMvpiPgWB7gkhxNll1yP%2FCtMiVDAPB4kpjziyzHALVnCKMYefLc1YVHRvZnVcB7c6RZ8W9lkLHdCOlyKBMLqFhr0GOqUBK56383XsnxrNvYh4jbwsgpr%2BQmNP36tNKXghw2NWFB%2BPCk5mWuUnuJCVWqhzxh2Cyox3kAEtsn432QkSBRHK2StZNVxmVVb8JrFjzrkWvdqQE5739eQDpG8JJOzKXMNEVgYzJAOBCIMGtl9j%2FmROpgX2SqIusmrlttyeo%2FMNBna11uIpULW%2FPVXiw1ouOUOb2%2FyoPL1qQOt9E5vMMTJP1CGGPUuk&X-Amz-Signature=8dbb48b4265c7c76cdaca058064b5de98c9a7e8a4f193d06de4d2e62a72705ac&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632LKLMEA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCSidq%2BuTNIrMGIWGC9yIRxaedlkuxg8id%2BzS3EvCaFNAIhAOig80i6GRsk4wnIwTgcsrARxxEZeRwkV1Zicj6mL3JsKv8DCCQQABoMNjM3NDIzMTgzODA1Igyu%2FjpTHj35iWlfNFkq3AOLx9w5ruUduDoRRuuaqOMoVEYTJiM3pfEtPHAY%2FHAK7lccI4%2BANPQiZAfNHCOQanYoHx4aB5d%2F%2Fn87e%2FcoITdubLgDpTRvH8bRgEcv8slbmQIV6XDPblXr7tPkD0%2FD7dqPJ2hztBoaVrJTc2X1u42MgmGtn1xMK6uIn3k5lyIUOgj35ptde8hz6nWtlb3sLK%2ByM0xubNoRS89YjvkONkvTKIkxK2jtofQ9sDtEed5hM%2BaojguFdpOlA3e8d8EdjeYQZM7EjlR2t4Ag61WNHI%2FnGoRPRjBZ0Wl0jtSVp3ZII7av0RjdrG78sY3%2Byaq%2BFWRN3ntuqB8gShQnoKmBAWopYDna5aGzsaQgDARO8Cv6D61vhQxEr%2FOuxJsySLRXXTHxU7aKUZwTR20xfhwlF0TbQ88xtWwdwh8ewkhpc%2FtttVLSomW6GRJJQCs0Oi8Jam1ue0HdVYXrp8R9%2Fx%2BNJescs4979EnjoF33pA%2Fqa%2BqyKus8ZBXKTCzIykYkYT6FOFXuqoWOr1GLmFUAUOnCR04NNLw2HCPVW1HaAqEMG5471UZxvA6gUo9qLMpHsEw2icLpeI1qrD2Z7M0p%2BPMxrqnPXtzcocdvO7SDxaeCN0Z9B9UPyYUoewMQ6tvMizCUhYa9BjqkAYT1HgryqFWLU%2BL6Ro507NXxJ2twK5ZdQhHbAD362KGVnI9sUEg1f0CTiI7DEJIlbuTaMPcxLDRpHvKqvyebvIsvcDrPXDns%2B4UDx9rNECMtjts%2BSpwcvnOzp4K86EtIkYX8QY3a%2BfXWzh9pTXmGBhB%2FtWqL6wN1CLkOIjnm6h4ADp0wa6tVtgkH3v3mJ3ziy0zF7hGeGJf6BFKR76yue4e0blzd&X-Amz-Signature=6a8b71e67df0f8733a7276fc851bb6baafec552c7b1e31f1c19cd06c46b17a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632LKLMEA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCSidq%2BuTNIrMGIWGC9yIRxaedlkuxg8id%2BzS3EvCaFNAIhAOig80i6GRsk4wnIwTgcsrARxxEZeRwkV1Zicj6mL3JsKv8DCCQQABoMNjM3NDIzMTgzODA1Igyu%2FjpTHj35iWlfNFkq3AOLx9w5ruUduDoRRuuaqOMoVEYTJiM3pfEtPHAY%2FHAK7lccI4%2BANPQiZAfNHCOQanYoHx4aB5d%2F%2Fn87e%2FcoITdubLgDpTRvH8bRgEcv8slbmQIV6XDPblXr7tPkD0%2FD7dqPJ2hztBoaVrJTc2X1u42MgmGtn1xMK6uIn3k5lyIUOgj35ptde8hz6nWtlb3sLK%2ByM0xubNoRS89YjvkONkvTKIkxK2jtofQ9sDtEed5hM%2BaojguFdpOlA3e8d8EdjeYQZM7EjlR2t4Ag61WNHI%2FnGoRPRjBZ0Wl0jtSVp3ZII7av0RjdrG78sY3%2Byaq%2BFWRN3ntuqB8gShQnoKmBAWopYDna5aGzsaQgDARO8Cv6D61vhQxEr%2FOuxJsySLRXXTHxU7aKUZwTR20xfhwlF0TbQ88xtWwdwh8ewkhpc%2FtttVLSomW6GRJJQCs0Oi8Jam1ue0HdVYXrp8R9%2Fx%2BNJescs4979EnjoF33pA%2Fqa%2BqyKus8ZBXKTCzIykYkYT6FOFXuqoWOr1GLmFUAUOnCR04NNLw2HCPVW1HaAqEMG5471UZxvA6gUo9qLMpHsEw2icLpeI1qrD2Z7M0p%2BPMxrqnPXtzcocdvO7SDxaeCN0Z9B9UPyYUoewMQ6tvMizCUhYa9BjqkAYT1HgryqFWLU%2BL6Ro507NXxJ2twK5ZdQhHbAD362KGVnI9sUEg1f0CTiI7DEJIlbuTaMPcxLDRpHvKqvyebvIsvcDrPXDns%2B4UDx9rNECMtjts%2BSpwcvnOzp4K86EtIkYX8QY3a%2BfXWzh9pTXmGBhB%2FtWqL6wN1CLkOIjnm6h4ADp0wa6tVtgkH3v3mJ3ziy0zF7hGeGJf6BFKR76yue4e0blzd&X-Amz-Signature=8e377a22b18810ae5b2b4c491af0c6e917358e232934ab0597954012c06298eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NN66MTN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDzsEZTdnTDV2KuQtGKbE1hMpiUsLzIB%2BhSe2RnuZU%2FPQIgEnKZFYeNfrr6zz10tChIJlU9koi0dtr5K2jKeZ9Q41cq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLhqbNtx747SKcgZMyrcA3917gaGDTIzCkTVe5%2Fc9HNBVfuySySMsiqytxvh2LlPo7Y3h2F9UvDCFks8aMbcLEli6tIczdfsuY2qSRZIMj3Jmu5ME8NGlCMWMwKzCQPpL8jGGByjPhhx5hct7oj3TxaaZNtW21%2BFkxb6TIcSb8q6YZrRQ2C8%2Blzbal3o5xSti8AtYEHWF0fstP9OU%2Btz6Wp3V6Ja5aOBIwIh8dEA98K4oyjJShJmZF6q69oKptpWCnrvWJWiKGxwYRC93pEPz4EBMVIFSoKx23NA%2F%2ByYZRh8%2BsVgz3TUReLQYdtCq%2FtHl7sASwWNwvVS%2FsOzYah1ocCFLoh8hxDLGUcDQrtmwKLNGcaG8iExsFSLR5CPCyvuKm%2FwdXBeUt6mKo4HwJyMIahzq2%2FX7c2R0BFxM8K2w9aEcBR1fl8kV06UV7mKFy8UWd5h%2BjR5eBTUGjbN%2FEoQb9pEgUCMYFSZJ74JSnfwI6CxgsiW4LmcJ5Mvla18oAmITafxQYfmzLcmwDs4cc5OkgnbA8MvsFKdpckPDgb1h8BWK08et3hINuaoYbRRqCAuOn2BVDSJJr5mi3W65CYqJHsT48CKNVFlywEodgHHiRuVO3wYy3OFXWJ4b7P4wa%2FJGRnfAGqYItnehheCMIyFhr0GOqUByas9Onn2mefUy8fHTuNWFiKVXMVoCb4A1XD36%2Bhz5Iz7Okd1jklzbWAgZMBrC%2FIBYTUc9Dxn3DVgy0cJs9tkeRM27p9Pxpoc6QQ3rIHhkkgzB8lQTygcrjU7MpDjNqoeQxjPb%2F8DkD%2FM%2FWrMzETAFRqFzzd4QnEl9ULba4jq%2FGUBOuSdgO8T8tQBn5xiZUaoIg1sxFJzdx%2BjXbIuccQTHJmi3dMm&X-Amz-Signature=2ef83b28e917b1e3557c2ae86bbeacc0e283604613770c4e68ad5bbb54356089&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VESY5FDD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIDjF5drBnCK9mWST4%2BEjIujJ1Ikt8a7aJR%2BU%2BXbcdOe8AiEA5WaiC37iEiKeJ41dJn%2BnWSHxEuIeAxD5ntUtACzJlLQq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHo5vLFWPg4UPDDyEyrcA2FM5BqVuzFZxRXt8lfvvnjC0DGYalqNNjNOVwk9eL8742WGFMtffGXUzM0Riwr6fS0LobCZFn5FGb55UomH3OxziMYpOE2vzMSi29c87tqXHkq%2B00yBUCdaZUnja4YXhXwUgZWjZ8qIKs40sY1dy%2BjSHXzk3l5M8qA2fmKt4Mj8VI1Ot9dXL6Vc8ZO3tejB04kKTwpgVwpQaSkAiRT%2Fm3oUMo%2FfXTWjqkQ2%2BngW7eDNAoLAty9nQ3Hq%2FdoCQa%2Fzi2lSHJslRWDfyxURY2%2F%2BExNpMORkSaqNqCdnYpNHxOjmmrUtKeXrEXpLJ%2FQsdhUNzLwYKGSF9k2KMZEdvI%2FO82YJpFAyff6K6RNonVj%2FbcAWniLc1qTxHCJyozBa0%2F2ef%2Fv3C1EPCGFUTEyxX3OPeEuQa7%2B8HRilYH5akkm8wbycgKXdxbYMPPAG50tHcz2naJ2oD0PBMDYwgoEwV1%2FTz%2FPEvd0iLpuieEcH6c4%2FOTccqUJEgx2XkgjOucgFfDq19YaUC3a3Q1aMm1uaWXjXuZNF97Z8VyXt37XgUnPTjvJmsAtusCJdP9yuZ4PSvD0FFYSwbRAwBBFBCe4FJ7H7hpFC%2FrPkJxYXC5W%2BetxncgQ16TYBzahvmfhZSsFhMLiFhr0GOqUBuv4DOT60SNTG3VszbrASCByifJ%2BjsKnWCFf%2BBR273d7w1fATvv7hsAldIMFgg%2F5BYhw%2Fz1Dyd63yLxoqL%2F1TQF0DWLieyy6OVBxaRZ8VZJkkianfBvr7iQD2m92XZvWYf%2Ft%2FATAR9Tpo2rbWI0FRo7rzTtKrXvxNtcTX1MIV0S7FKTDWtuiyE3F1wzwjWrtCfMsjjEDJCQp4koHwL7c9Os4tSJwC&X-Amz-Signature=5e8b29c8806f913b24eed6cecc4ef23216acfcf828b5547def41b10b0f4ff057&X-Amz-SignedHeaders=host&x-id=GetObject)
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