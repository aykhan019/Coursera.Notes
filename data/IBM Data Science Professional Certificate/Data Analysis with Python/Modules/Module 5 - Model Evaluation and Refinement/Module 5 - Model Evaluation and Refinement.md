

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=0416261218f76814168345693a5c4540abb9c43ca301cac6b3bac2b65e5263e4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=2172c9c7376a493f4f78a12972cf4aa15254a73ae6055bb05231f76b3a79cd9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=aa167c2509fa58ef34dac002899724884801bfff0088e18a59d0f09ffff7f7d4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=5c23ca19568da150d602240110082f6d810ed2f78475d6bc48d9a9904f2225ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=0e8b87ffb024cdfe1f33d684f92a0ed09619a37d67cbd13ea477cbaaebfb8918&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=5e957fc0683065e6f49adeb713eeebbd12f65930d4f18c9dfafe43a3d3c9dd84&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=6802ee161e44018428ad83d8491218b8f1fd34d932f03715b94a342abe7ecc7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=6e0084cfa9409bacc473c3360b38bf45102de6688dac372a4ff06e89b090d080&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=10a95586f80ec3c099ea2da8814c3410703168c65b5e6884af0ca53a3e711509&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMG57RTD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaG%2BjG%2FKbEqrXOZzzI1PjRlp0caTtccqVfmuGyAWaDSAiAQGk%2FIhnMqsoUCKlfE4olwk%2BJR9qdpH%2FXbkislG%2FUtsir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMYpOIVMBGKsWdO%2Bt4KtwD0Okq6fxPyuOCRIV0rO61csXnzOJsqs8mXlHioZ%2B%2Bj2%2BCDVdbCtrwdIsIqBmzsbQJN3NZqKBmgbFOcRX7V5z5OZmBP%2BrIlRaOZ4lHi4P6tDbu1b2o4ZJiUrJKHguC9mwUemIJNNOymd%2FjT9EKVyYWy2BycmWxKXtOoA3Kea2D6yXNcHv5SYAhnvTL%2FXFh%2F%2Ba8c%2F5iR%2BBdiQxJ%2BFyXBrAALFT%2BFZXy1p61UbRjPInOp03nMYFi9Qajjd1CAPbuMBryZWOPVSHSAo1Xc1zCDgxjYlxzzyXD38xrT86R9QfiW%2BuhqEo0N9NlihL87bq0mAeTcF85IA6uqPPZSasjozUfF%2FxXW%2BnpM7H27%2FZUc1GsNE1HYVdd0Ve9M5k0GiPYxSW%2BU5hT8L0WT8Qm1uN9hZAYkUEUhZKWaJzg7J4RVnI%2F6jEPTpa9CHG%2BKlF6nipoCkTZYXvZtp3%2B8SW7U%2FI3Yvoswfa%2BNBEsdfD6d93rN%2B19L92Kq8a51o6RbQy6U1W5uLv6k%2F7GMKWlIeO668n%2F4hlY4KGEH4axPlITKErNdiI9dhMeevKGvr32TJEGTea4xT0Bj6fYGqvPlGzw2mWoO143ZVtDNqyUh%2B0u4m0B7vDEnPPR60MHyPfCgP1LAUcwovOBvQY6pgEPQSHrhCASxSp5Os7o6E6%2BgYB7Cg0zl1KdFfUP1q0LpEny%2FqKl7MZVIBM2ZGjguzLHI8Iq0An0XUllQ5g3UjCKPiSx638D7axLe8SuVrOChDapLZVtpLUgaaAHQLN7dk%2FqyDTWicAIzoatDdpBb%2Fun%2BaNySlJ%2FK90DxKjDTMBbYBgAsX9ayubHK8kPuqwVNfuOrQlg2xP2VoSp4Ovdl%2F7%2BIp%2Bs3JXX&X-Amz-Signature=6556897078b11e3ff6e82a46c037db47b21ef0692db4a6331f1ab9431524032b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMG57RTD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaG%2BjG%2FKbEqrXOZzzI1PjRlp0caTtccqVfmuGyAWaDSAiAQGk%2FIhnMqsoUCKlfE4olwk%2BJR9qdpH%2FXbkislG%2FUtsir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMYpOIVMBGKsWdO%2Bt4KtwD0Okq6fxPyuOCRIV0rO61csXnzOJsqs8mXlHioZ%2B%2Bj2%2BCDVdbCtrwdIsIqBmzsbQJN3NZqKBmgbFOcRX7V5z5OZmBP%2BrIlRaOZ4lHi4P6tDbu1b2o4ZJiUrJKHguC9mwUemIJNNOymd%2FjT9EKVyYWy2BycmWxKXtOoA3Kea2D6yXNcHv5SYAhnvTL%2FXFh%2F%2Ba8c%2F5iR%2BBdiQxJ%2BFyXBrAALFT%2BFZXy1p61UbRjPInOp03nMYFi9Qajjd1CAPbuMBryZWOPVSHSAo1Xc1zCDgxjYlxzzyXD38xrT86R9QfiW%2BuhqEo0N9NlihL87bq0mAeTcF85IA6uqPPZSasjozUfF%2FxXW%2BnpM7H27%2FZUc1GsNE1HYVdd0Ve9M5k0GiPYxSW%2BU5hT8L0WT8Qm1uN9hZAYkUEUhZKWaJzg7J4RVnI%2F6jEPTpa9CHG%2BKlF6nipoCkTZYXvZtp3%2B8SW7U%2FI3Yvoswfa%2BNBEsdfD6d93rN%2B19L92Kq8a51o6RbQy6U1W5uLv6k%2F7GMKWlIeO668n%2F4hlY4KGEH4axPlITKErNdiI9dhMeevKGvr32TJEGTea4xT0Bj6fYGqvPlGzw2mWoO143ZVtDNqyUh%2B0u4m0B7vDEnPPR60MHyPfCgP1LAUcwovOBvQY6pgEPQSHrhCASxSp5Os7o6E6%2BgYB7Cg0zl1KdFfUP1q0LpEny%2FqKl7MZVIBM2ZGjguzLHI8Iq0An0XUllQ5g3UjCKPiSx638D7axLe8SuVrOChDapLZVtpLUgaaAHQLN7dk%2FqyDTWicAIzoatDdpBb%2Fun%2BaNySlJ%2FK90DxKjDTMBbYBgAsX9ayubHK8kPuqwVNfuOrQlg2xP2VoSp4Ovdl%2F7%2BIp%2Bs3JXX&X-Amz-Signature=2eb2c9feb359ce8bc7d7d18b2c8589caccd0866ef1e68894d7eac672bb5b6be1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMG57RTD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaG%2BjG%2FKbEqrXOZzzI1PjRlp0caTtccqVfmuGyAWaDSAiAQGk%2FIhnMqsoUCKlfE4olwk%2BJR9qdpH%2FXbkislG%2FUtsir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMYpOIVMBGKsWdO%2Bt4KtwD0Okq6fxPyuOCRIV0rO61csXnzOJsqs8mXlHioZ%2B%2Bj2%2BCDVdbCtrwdIsIqBmzsbQJN3NZqKBmgbFOcRX7V5z5OZmBP%2BrIlRaOZ4lHi4P6tDbu1b2o4ZJiUrJKHguC9mwUemIJNNOymd%2FjT9EKVyYWy2BycmWxKXtOoA3Kea2D6yXNcHv5SYAhnvTL%2FXFh%2F%2Ba8c%2F5iR%2BBdiQxJ%2BFyXBrAALFT%2BFZXy1p61UbRjPInOp03nMYFi9Qajjd1CAPbuMBryZWOPVSHSAo1Xc1zCDgxjYlxzzyXD38xrT86R9QfiW%2BuhqEo0N9NlihL87bq0mAeTcF85IA6uqPPZSasjozUfF%2FxXW%2BnpM7H27%2FZUc1GsNE1HYVdd0Ve9M5k0GiPYxSW%2BU5hT8L0WT8Qm1uN9hZAYkUEUhZKWaJzg7J4RVnI%2F6jEPTpa9CHG%2BKlF6nipoCkTZYXvZtp3%2B8SW7U%2FI3Yvoswfa%2BNBEsdfD6d93rN%2B19L92Kq8a51o6RbQy6U1W5uLv6k%2F7GMKWlIeO668n%2F4hlY4KGEH4axPlITKErNdiI9dhMeevKGvr32TJEGTea4xT0Bj6fYGqvPlGzw2mWoO143ZVtDNqyUh%2B0u4m0B7vDEnPPR60MHyPfCgP1LAUcwovOBvQY6pgEPQSHrhCASxSp5Os7o6E6%2BgYB7Cg0zl1KdFfUP1q0LpEny%2FqKl7MZVIBM2ZGjguzLHI8Iq0An0XUllQ5g3UjCKPiSx638D7axLe8SuVrOChDapLZVtpLUgaaAHQLN7dk%2FqyDTWicAIzoatDdpBb%2Fun%2BaNySlJ%2FK90DxKjDTMBbYBgAsX9ayubHK8kPuqwVNfuOrQlg2xP2VoSp4Ovdl%2F7%2BIp%2Bs3JXX&X-Amz-Signature=5b560e8e0903677aec70e2dda1a43675ff9663dce699f5314447ff8db3631e59&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=a29044e8356bee4aca093ee9b6674f16da3f6d8e91981242abf166cc0507b7fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=2a59b24b46d4ca048a4c14166c6952976fd3e8f2bf822415ff5731d1dca0fd4b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=8f33adbe724c77cd246ba612b32fc42fb9060fc2d43646b44947c9abe16607c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=a6415ffe4708430513f252847df23e24aa058d0dff6e0de22d44dfbf38fc781b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=6bd9c8816d7896fca4c8d0f35a09eaa0602a6ae95bc9efe02e187754b44e40d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCYRXVJ2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCR%2BYc%2BrtLSxs4lf3FK5kU1GX7nUMRGPTWW9Fo9kz27xAIgazj3ySwjQ5YDJePBSFytPMX1TeO3gQ3SAknvUIYq9LMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLcRHTL5zfReE2WKNSrcA%2BwFLQSpg2sh1FqKgmz7NjZ%2Fin4E0zrs50CJKJusvZWyZ7lA8Z5CNDk5u1LTmwnNR0gqtStbBCI6emyXv9UWFmPzRJaqrFEE3j1PjILqRp6PW%2Fe5IDdZt2vWHETN8BgDMZCM1quJDPuzzXuPMXvIYdyfY2IFm6HEYRgKQKNysvqRvDf0bHD%2Bf8RV2yXXf5fmIOeZiRzKLhIL2JLcahNJM%2FqC%2F5roH2NX7i%2BnC6ciaZaiMHylfpEi6tLTM813sGod0uBY3lWcNvHjl%2BimI3hLkspEJ%2F1ViC0S%2FIZ4z08oGhkoqY98iFx6JVAZnBxU4jZ2Ix2zWo%2BwOjhC13S%2BE7Eashr7mZ1LnuiGCV1lBc%2BlIB8mNddkHqdOg8CqcZFsufkwTAUKL2JMUgt2L5Bx8zeYIv4gHLaJzKxWHbdJxUrs8f87%2Bz0YtnrxN%2BUcRMxwDX4GtxFFdGyq%2FPXmTNI8gwXrp6uRjuFBweCoo4C2N0PxPf1gNt%2F4V6e17zAQy41EPebe541UM%2B2dLRguHTFrPO%2B3ewvq1V6Jp3S9hid4AQCbblxBPj7rZGn4xxEuoq4z%2FULHJTg%2BJueY1pEBLa0ry6mPSXXwZckaDR8v1v%2BaJqpDNtNyrQyeBicVmfAou8uiMLHzgb0GOqUBW1zV7hqDYWKNiF9C1%2FWaxSc3M9Ika9rSyVdfq98%2B7GVCwDygxYNmz1ZYG0bUFOg0mdQcv6y5zQsKitL%2F77xCYkAahXFQeNWQl8emVxW8UR2ppIiupwhh8I8GDzMJ0TwL%2BpcGCv%2BoPfhhKGGS%2FXHX8EB6DkV4Uu16mbsODSIL7Eb1ZsJ5LmFyULKtrGqsBUEpHCM%2FR1tYQoYJNBzgAj5ZBaR1A5KF&X-Amz-Signature=e5db34550528fd99bebb52b962069eb816c0f5de5a6f14b74d43ed4681e4a0f8&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOWXJWQS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHEEoIneJqMPPktUZcxEcf%2FPk%2BmfX1qPT%2FM19JdAGy%2FYAiBzRW4y%2B%2Bcw5GwfwYGiKoD7OqztuZqUC6hKAJT48d8FkCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMZNWGxrOm%2BPJxf4mcKtwD2irg%2FxImyGQ0GHV7tNP2FOP2Ly0MmdaoMVMiF6tUViV4bF3MiPkfuaw6a3Tv1ZSQWlE9VapWnugATQq2VdDlclJBAAou1J0B%2FZW2%2BSmndbKr6bsEO1BPj4%2BtA7KuqjifWk3YW2o93RVOb9hNszWAEdA4Cv0UI%2BiA3qU%2F%2BA8lrsLkegmGElzruNVea5r1jaVgKX%2BMZAGE%2F5v8ffVJQ%2FFuLIwFqFTf8h7XJcmQOgkIf6negqWC2dq9SvFdyo3EA%2Bg90iJ%2FUnMeJo%2F%2FF5u%2B2K5UP3kyfPmgoU7TintYYUuCZb8keMsAne12C%2BMv4cQpyszQkZjni6dnPzxQ7vkoFHacyfX5Rck%2FslLN23lI%2BVMlsZwgnRcnKUHjXor6%2BoXHW2j%2BMHyoGE0ta5fqPW2tcVkbYKAOIoIM%2FVNCDwXrmYl3gxbq9xF1dOFfa1hFEMeOEpmIxlsyriz%2FS8iFAExjOfV9v3cuw9PVgaMsShfSo4SL%2FqitsDHZHcfwb3N0%2BEipcK9dCVGzE1yPwHshjg3ErwCW7v2w7yAfysBEJ2RNLk1yWEuoimPVy1uYrmZ4AWFYpndnL4Osc7UocVHI5li6dAX6Br4r5P4bHqHpjCxAjOg16l05b65wIMaVKsBlM0wwiPOBvQY6pgFh%2BQijKWvxysou8oYmWnEvjS%2FH4NoHzNei5DE%2BkLmv4lw8wRMzEN38W90968a22tMhfppyCLBBfiPe0ejEZk9vNbB5vCEVWVle2wd45OOX%2BQIYKrrTBDwCI8fIm7f0SjSvZLyTpfVMKBRkznWXTxCIm%2BX0GS0woynO%2F2bwG3Eq0QVpndmeAf59mEpSGIyCMUvV4BPP1gLFf4OfkJBgQAeua7I%2FwK7e&X-Amz-Signature=47ac10428ce724d6fe5e4527fd743736012ad7498eebf03ba48c2b3fa7266af3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOWXJWQS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHEEoIneJqMPPktUZcxEcf%2FPk%2BmfX1qPT%2FM19JdAGy%2FYAiBzRW4y%2B%2Bcw5GwfwYGiKoD7OqztuZqUC6hKAJT48d8FkCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMZNWGxrOm%2BPJxf4mcKtwD2irg%2FxImyGQ0GHV7tNP2FOP2Ly0MmdaoMVMiF6tUViV4bF3MiPkfuaw6a3Tv1ZSQWlE9VapWnugATQq2VdDlclJBAAou1J0B%2FZW2%2BSmndbKr6bsEO1BPj4%2BtA7KuqjifWk3YW2o93RVOb9hNszWAEdA4Cv0UI%2BiA3qU%2F%2BA8lrsLkegmGElzruNVea5r1jaVgKX%2BMZAGE%2F5v8ffVJQ%2FFuLIwFqFTf8h7XJcmQOgkIf6negqWC2dq9SvFdyo3EA%2Bg90iJ%2FUnMeJo%2F%2FF5u%2B2K5UP3kyfPmgoU7TintYYUuCZb8keMsAne12C%2BMv4cQpyszQkZjni6dnPzxQ7vkoFHacyfX5Rck%2FslLN23lI%2BVMlsZwgnRcnKUHjXor6%2BoXHW2j%2BMHyoGE0ta5fqPW2tcVkbYKAOIoIM%2FVNCDwXrmYl3gxbq9xF1dOFfa1hFEMeOEpmIxlsyriz%2FS8iFAExjOfV9v3cuw9PVgaMsShfSo4SL%2FqitsDHZHcfwb3N0%2BEipcK9dCVGzE1yPwHshjg3ErwCW7v2w7yAfysBEJ2RNLk1yWEuoimPVy1uYrmZ4AWFYpndnL4Osc7UocVHI5li6dAX6Br4r5P4bHqHpjCxAjOg16l05b65wIMaVKsBlM0wwiPOBvQY6pgFh%2BQijKWvxysou8oYmWnEvjS%2FH4NoHzNei5DE%2BkLmv4lw8wRMzEN38W90968a22tMhfppyCLBBfiPe0ejEZk9vNbB5vCEVWVle2wd45OOX%2BQIYKrrTBDwCI8fIm7f0SjSvZLyTpfVMKBRkznWXTxCIm%2BX0GS0woynO%2F2bwG3Eq0QVpndmeAf59mEpSGIyCMUvV4BPP1gLFf4OfkJBgQAeua7I%2FwK7e&X-Amz-Signature=09a26af1f02bc8a5b6a86635cc573114c0f537155f129e1bf7d88d0348e83dfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIA3RWU2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm8IYsfuFjpf6sCPVemOFVhBh4JTYzgob3bCZQfq228AIhAOKlZCFeUuxoRq%2BTXVPcQTdj%2B3GGiw3X76oRv9WPES2tKv8DCBEQABoMNjM3NDIzMTgzODA1IgyXM3UVSezZYpHJBa4q3AP%2F1dr0g0vAFMnwi8OhOKJJAuRCEHEfZ5Sru0MRNhDz7KGHEIh1vhmkEgvtrl75K6D1hfe%2BA6CtQ2rmW41bDMOKFnJm6ZX5SNh2QRDNKqEfqDm4cSlpp65UJ9hlW%2FqBDAr7TZgBvQgG%2BJ81uBHFO4Z%2BTFsr60pGpwbuGuAQnpcKe4gKgFIZoraG4q0ayolf%2FKJhD2r6lTP84O%2FcYzrVuhPAJMecu7kxZmOUc%2B3TPG20jhJApMsggBU7UbbwcToGvmikfRu9X1nXA15Brt603BWyk%2BkB%2BljwgJ3dS25mYpx7I65ydGze9Z88GiB5vWQdOrgtz%2BzyucUQZOW0LRbyN666yffeDeLctX7wHstndClbzshFlf2aQrAy2AwercK6%2B5OI5f2zXHQmSBQqE3e7U10opuV5OUEAI3PGr%2BDsbiE50qevorv9iw61TXL9KiL5af3sQwRsyVZ4ieFkWoL09Rl2LLam9H0Ex7pLs%2FXYx4J7HyLbTT5c4Irp1V2Ld40YofhmkEnPlalkhPYp9nm0jpCr5%2Bso5aAF46xcAOiHhc3D8LAxUrYyv2zoUxxynLkVJwRSa52xj54uTL9Jzdzmt82OOTZ5SYiPWhB4M8154OFkOIC7ZHQB%2BShi9yEkCDDw8oG9BjqkAWqCwc05j7Fzz0ApFW8w5cMXa7u%2FBIs0tGAIJGSyNHDxT258iE1TFX%2BDy77SGjSphg8FfIF7X47N3%2FPt6blELLHNwET43Zv8YyqCdPDwgGkMCWjkN0O7RpbvAew9DgFZIhB%2BbuwGPBGPm1tUpsASb%2BTUKzCk3leXnY3Cv36loWH136nxNmgwJ2cbTD45jPic3xqpFGQ3T%2FBXErCtxumJQYlCw6Yj&X-Amz-Signature=230d4b4a59dd78026b6407eec8b4187f3d1892af5419a88d4801256fb9c48912&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5NX5DA6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVik0v18SNEfSieA1QM2YqgonR1rpSa9FoMVMPeKxlaAiEAt17k7pKliACDVwpCJ2gFfgY7pwXg3S3fwPc1Qw96Ljgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIjYav6LNSm9%2FK6gPCrcA4kDt0dniddm6xKEYI5ZXlK6jwdLXJ4C%2BTmWiPmu25UaZqW69oxdo%2BJNrGeKjeu6ilcuOyoEYSjRqnWUcEQ5x4d78MuYcQ%2FxdLPBIlpujTYdR2%2FTCpIs%2BiZ1w8xtrCgp6EE%2Fv5hKOPwdeOKCWp7XZMDAQAhf4jgdzfik6UE6L2z2UO6RJYOZCEHvrbIrsLvbioo7Cp5F9Hge5iad2Bz6FHcssxKXL4qlyEqfRmLDxeKuZBVAq8%2Fwqx2SZ9rNAUiKxc39d0Ht5yCMyix%2FimJhTQKWHLa%2Fa5eznQDEzrHH3h%2FLxMACta4N28bibL9ShGRQxMyDwVra9kU0hxG%2BiJ3Mwu%2Ftk0PCFjWx0yq6KIj2ai9%2Bz2QGilvX3qw%2FyMusySyw0PRUEQkEZRDJN9qh3BakI%2Bhw3bDbaGmzgh7G84UL3xGeZeSndbPvhrVqp4SB8nvu6oYgk2aNpfYhvhmxamikCbLQ6KyHpEz5OGDhhiR7L0K7oVBSNh7fDwLGap1j9x4LWGcvnUkIQMoE9fuQsLxWYSyh8TyLScKWEdYThOJPpMv1CpzyLROyTcjzJEfYScRjuzHBHGoAOiXCfs%2BgdzK%2FrMbt02ZsIHo8JUaFF2To58pe69yqUhOOTorO5aGGMIH0gb0GOqUB7%2Bl8PXUk%2Fdga9ABUqWGDIXWrb1k2Shyr6H%2BsbkXj2YSm9f70V2jyK5%2FxFm6W5ZrL1BPwmd1ABROGi8NpUlBxrdPEKGQ52kHMFw6XVDalFCAtp%2BHOEvcWQU4%2FGntrlvB21Xnh7YQJTItlUj%2FRrrfX0BqCR8EeNwS8eeBCkMvBVdBioznx9HzizSz5hJNH%2Ba5HyKVHIUC0mvl4BWa2w8S3qpxYaU02&X-Amz-Signature=909a25d668916a067c49913cae753f4fbdeb80e97b53c049fa22a69ed6bc1b0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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