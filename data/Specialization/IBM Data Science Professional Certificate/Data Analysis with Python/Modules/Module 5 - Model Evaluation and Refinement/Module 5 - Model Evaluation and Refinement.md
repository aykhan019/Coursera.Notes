

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=20bc4058e9fcf07860b1b8092bc82171f91dc0577d042d615b14044dc1792f62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=c096b3b93b3c02646407ba445e7acdd2ea1bc871cdee328d4076a0ccceea520b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=f7ed5ca39bbda0caf1c08254051ede49409f130d21107d1907eddf5f9a6767f2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=65a2253c4b2eb744eb6b5324913c210c3d13e03590410334f1c063324508d1e3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=65b8ec05b704e3b872ec2e0e63dee92cb18ef6c1613109fcfba2244caa38cc30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=6ea391e54bab6cde3bbddd9b779332e31a75b5a1437729993dada79dbad8f1cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=a57f955a20a515486a6fc8ca5c3758805e2b88fec679fa15f21bef6492db827d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=8105e73077ab019f8f890fce54ab0924f7e43f002a36a7932276689569546966&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=f4698feb1a8150ff71eeea475c1317a03253c0e4d0b67475305e6c6079fcd6a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZPVI4JU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3ma%2B1JTzU8cFPMNMJ4DJXuAZA9%2F8%2Ffi6EHb%2FuHw7NQIgOhAaZZKFwHFCWt2Ml%2FBoWExVYK3hw%2F1QedKDL%2FYIJDIqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1tUxmh9KlJPwVWOSrcAwcW2wRb1JD%2FmS4yEly%2BlyCS9mV%2BeH5nBxEPVWk7Qek%2FLqreI35%2BcFgDbQ9VSu53cd2sBAx4DSBy97kX9QZ6STMAwDuT6rK85Tab5Si6TKFDyabFhcg9BCzNzkW1dmw1hAablPGFjzxPRRSkN52akHeArow7oh1uliersAZnN83rwzSgmAYnGNV54Xdf9SBaiiB7%2FqNbLSpHohA5XSi78og2APQlrcSfz4jkVXIOrrAZ9ed7AlZKAhYOyuOoA%2Fesel4Lk%2BoAFicjgUYjzzEpRIPx57LDDhe0cm5kgT8e21%2FD8LT9luPsT1BtL4NHK7fdxxPKYGlN%2F6nVADgkoyPhTSRrk3VG9Ji9o4cZE46tq6niJJNMcSeom4%2BVkACYwuYrfucLcshsS7KK4nlbPFFyt6M4bOb1DPjnGZuGm9W26R7m4MnC7LcobwFSzxtU495a%2Fl1OmEYcijgXCL%2Ff4k%2FUF0anvAESoKZpoJ6c37gwK10XscrGMLWU8baAkL67RLpkLNG5Srht8ImCW%2FGKqGZxaVAlaI0JJwLZMvLSOQhpR0vz3JSlAni0FzKeU0e0EDU0D3iezq8HruSddCmceDNpMMvOin9wQ%2BzJq54m8GVN%2F%2B2CPho8NWJ3g7OASgGOMPDg77wGOqUBlOfe3cgHZTo5UYWF%2Bm9B5dmbPACtcHiQuWKdruTdPvfIqvgLa0E6R6bWh6R9XeYZUkXaTnHAUXCZEQFbXmxKG3D23%2BmaWONaL%2BDCPmC1mLpecxGryM2gp%2FWvSbwlHD8FwXlc75v0dRlToCe8Aqa%2F8TW338UyUNQh7AOEbHGWnEo5%2FgYwmtF2c0b4Z3cDK0wUVPNb6io8fp9YDocNJPTsryA02P%2Bb&X-Amz-Signature=efbbb6a20aa9e44689c707f2dc7a5a4fa925a3774344bfc5f6f8fa0d16865247&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZPVI4JU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3ma%2B1JTzU8cFPMNMJ4DJXuAZA9%2F8%2Ffi6EHb%2FuHw7NQIgOhAaZZKFwHFCWt2Ml%2FBoWExVYK3hw%2F1QedKDL%2FYIJDIqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1tUxmh9KlJPwVWOSrcAwcW2wRb1JD%2FmS4yEly%2BlyCS9mV%2BeH5nBxEPVWk7Qek%2FLqreI35%2BcFgDbQ9VSu53cd2sBAx4DSBy97kX9QZ6STMAwDuT6rK85Tab5Si6TKFDyabFhcg9BCzNzkW1dmw1hAablPGFjzxPRRSkN52akHeArow7oh1uliersAZnN83rwzSgmAYnGNV54Xdf9SBaiiB7%2FqNbLSpHohA5XSi78og2APQlrcSfz4jkVXIOrrAZ9ed7AlZKAhYOyuOoA%2Fesel4Lk%2BoAFicjgUYjzzEpRIPx57LDDhe0cm5kgT8e21%2FD8LT9luPsT1BtL4NHK7fdxxPKYGlN%2F6nVADgkoyPhTSRrk3VG9Ji9o4cZE46tq6niJJNMcSeom4%2BVkACYwuYrfucLcshsS7KK4nlbPFFyt6M4bOb1DPjnGZuGm9W26R7m4MnC7LcobwFSzxtU495a%2Fl1OmEYcijgXCL%2Ff4k%2FUF0anvAESoKZpoJ6c37gwK10XscrGMLWU8baAkL67RLpkLNG5Srht8ImCW%2FGKqGZxaVAlaI0JJwLZMvLSOQhpR0vz3JSlAni0FzKeU0e0EDU0D3iezq8HruSddCmceDNpMMvOin9wQ%2BzJq54m8GVN%2F%2B2CPho8NWJ3g7OASgGOMPDg77wGOqUBlOfe3cgHZTo5UYWF%2Bm9B5dmbPACtcHiQuWKdruTdPvfIqvgLa0E6R6bWh6R9XeYZUkXaTnHAUXCZEQFbXmxKG3D23%2BmaWONaL%2BDCPmC1mLpecxGryM2gp%2FWvSbwlHD8FwXlc75v0dRlToCe8Aqa%2F8TW338UyUNQh7AOEbHGWnEo5%2FgYwmtF2c0b4Z3cDK0wUVPNb6io8fp9YDocNJPTsryA02P%2Bb&X-Amz-Signature=20e26bcd7053cd84d47ff209e30037b1201aa57539118fc6dbad038ec5850c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZPVI4JU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3ma%2B1JTzU8cFPMNMJ4DJXuAZA9%2F8%2Ffi6EHb%2FuHw7NQIgOhAaZZKFwHFCWt2Ml%2FBoWExVYK3hw%2F1QedKDL%2FYIJDIqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1tUxmh9KlJPwVWOSrcAwcW2wRb1JD%2FmS4yEly%2BlyCS9mV%2BeH5nBxEPVWk7Qek%2FLqreI35%2BcFgDbQ9VSu53cd2sBAx4DSBy97kX9QZ6STMAwDuT6rK85Tab5Si6TKFDyabFhcg9BCzNzkW1dmw1hAablPGFjzxPRRSkN52akHeArow7oh1uliersAZnN83rwzSgmAYnGNV54Xdf9SBaiiB7%2FqNbLSpHohA5XSi78og2APQlrcSfz4jkVXIOrrAZ9ed7AlZKAhYOyuOoA%2Fesel4Lk%2BoAFicjgUYjzzEpRIPx57LDDhe0cm5kgT8e21%2FD8LT9luPsT1BtL4NHK7fdxxPKYGlN%2F6nVADgkoyPhTSRrk3VG9Ji9o4cZE46tq6niJJNMcSeom4%2BVkACYwuYrfucLcshsS7KK4nlbPFFyt6M4bOb1DPjnGZuGm9W26R7m4MnC7LcobwFSzxtU495a%2Fl1OmEYcijgXCL%2Ff4k%2FUF0anvAESoKZpoJ6c37gwK10XscrGMLWU8baAkL67RLpkLNG5Srht8ImCW%2FGKqGZxaVAlaI0JJwLZMvLSOQhpR0vz3JSlAni0FzKeU0e0EDU0D3iezq8HruSddCmceDNpMMvOin9wQ%2BzJq54m8GVN%2F%2B2CPho8NWJ3g7OASgGOMPDg77wGOqUBlOfe3cgHZTo5UYWF%2Bm9B5dmbPACtcHiQuWKdruTdPvfIqvgLa0E6R6bWh6R9XeYZUkXaTnHAUXCZEQFbXmxKG3D23%2BmaWONaL%2BDCPmC1mLpecxGryM2gp%2FWvSbwlHD8FwXlc75v0dRlToCe8Aqa%2F8TW338UyUNQh7AOEbHGWnEo5%2FgYwmtF2c0b4Z3cDK0wUVPNb6io8fp9YDocNJPTsryA02P%2Bb&X-Amz-Signature=f459be5e2eeac61e45a3dfa407cbb142827c702f46dd1137e8829732ea063dec&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=cf83e13270aabefaa3c8e70db83703c8747303e279101067e6815d1b290fd939&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=eeb23556d16db63009d1baae793f72617319d7ec680d3c092153a778f112af14&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=517f2ff703bb2305c934753d40dfa3c69fec80099284b5abe602352180ee7582&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=27dd3b6a58de37a65f8e858666dd8d7a16e0e9ab37cc91a1977d1d27bd2a90b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=157257cfb4eeff48d97d9c8e77d2082ab35baf0b2bef4f27f09ae8eee128306a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPATSGF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqKk0Ft7QZcB1dKKVIC80voUFGbgRrrGfD%2BctP3JsBVgIgQjR2c7QvtD1Hw0Fgp8V3NP6DZdU4r3l3gSAYphdPV%2BAqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsbFJ1TJSKbbQFacircA1DGgBwBLW6krbWJrZke%2FAO7%2BeZwMphGlWJ8jVIoVDlbymVUrx8qItRY3vHXaxsdmagE64pR75PtTziAXX774f9KxCsGQ8TUR9pOC59oeNwC9HBUBY5sqYTswy%2F%2FTZ7HkcCCcQbOezAiIwCXz8VNCkJJw29m1z%2BXFhv0wLE6%2BAb70%2FcnNchqOzbd%2FQ3oAOrOK89Y3bQPi3euwoMjAZPg6GvYI8jqRQqFziCgZw%2BV6zpSgucAoq%2BpgIgGvmCzombWNrRhCZAyjj0WBDXzKr5fS%2BTY3wqAHHNm6C5UbVIrrcjh3TZ%2BA06VzFeKnH5Ng0Rdc%2FHMdSB6kYKR1TUYzFdY5NHx4ARU9ksMnkV6WgjDxbDgrqumFcM096CSdpCz4CGOoNfcp7zD91met1GNVPwNyizqatxVAMqxpQ4%2F8LDDcNRIAuBvvMjks6zaMgqzG6bqq5GwpgJneS0B8JyAkkE5rLvEvYm5zt1HgYpX1%2FQT6Awn7EJwse8edL9VFI%2B5fixwk3nMnwYfaB8UvST5IJwUdCnd1zzoQk7muEL%2BlGSjb5lZQ36AdfWECWlfQCBs72DAUEHV%2B%2Bc9XkDMqGv0TlWwotOxzuUF5FE5A7mTQmsSzXFAOQTmysD%2FxLlEvs0uMKTh77wGOqUB0KtafcfXQ6N%2BywqYfQcmsAbRmQK1P3iWEbGu9dIlyZ8XPTUnxcSSC4judPfBeB%2BGf7my%2FWtfrDfyHYHbATeBhtq89ihWMtSPuWp3ZIfWPWcslz0QDvS04dT7xxvdyNgD8BF2p2qJgUk%2FiGxkrMIaYTspxfNULE0MfGupXcrNtc%2BaoRc4cSj%2Bctw1%2Byq7WGkKfcAycu9QaHMmurAuXjKl4dNgBbAI&X-Amz-Signature=3ae61a147fc7c9a267fe227707eb4ccae23e2df0f46a60a9aa126903aed748e2&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OOQSI7D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BLSZL8lFrnRpXh3jdgZi5MNgpNNNZ6HMV6%2BsTH9DPAiEAiLzjpDVPbL2RrRi7XeLHkocKBx4j9SiYVYbXxmyz%2Bu0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQxU%2F42kVkT5UhW2yrcA6pcKJVZk%2BBiYSsSEbxQtjUi%2F%2FhwwJkn3ulHXYKTku0IdCiS5un2pKtlRNq5sy3KeoWYQyL54FQPxGyygPHeJ%2B3pknFh9PHtjDM94euhZz81Bp4WT9TC6VoXgqInqxBoaLhC0B6vmt4izu9wJTSPnJQ7LxwuTgBTClvRkSu%2FhhJgM6LKMHAaqDQrZHxYVX7l3qQTgqeqhCIUTit6wykwdMJF3bNogiDP0SAuK%2FGbT78jxP4UUdM6No4RrLeQB%2BhQwBtkaImsfoqh2z7JPoKbEZ8MPB7GQ0AIQxVPT%2B4YrHrxuLmuFI%2FbzW4bEJ3Nx4CUJFn2fwXRUK6uEId%2FlfjOi3VqKw4Su%2Fzo%2BaRlzFvHC9emjlyOixshQO9T%2B7fQkGiFTxD0LyCYTwKhHhDR%2F2KaGOe2kUXcBSLnPovHSRQ6UD%2BDrhQkkB4i0mo4PH30P7O4i%2B0lX0I%2FhaaCcH9GjKZtYeVJee7S3nUdgEQf%2Bt9KcX6yMAuaCHlrtQKYa4f1KotGBF15mfc72U3Ai01P%2FxVnOtJl%2BCz3F%2F9K5JMBX3zyZLKVYK00BHnzx3D5Rf0Z4po3q1F0cJIprc%2F9TRULrL6R0UOakM0vid2%2FU6Em2gqb%2Brkxw7%2FpscobhQq4UXeMMIvh77wGOqUBUiDwPjjUdcg6Q2Y%2BlQdwcA0vuCiOcSFeC1yj56jVFwrO5ulBEoEjnsNGdg5pD9g4IjUMWsT0kqgwhTFyEBAj6g53w7AAE4lXwFJEvd2XnaXG9A1wAaVFbSflB2lNdxvo7sHB5Yo5zWxX6csLvKFXDiWNVPsIRzYDeIosRJYQRK2vx9xbX%2FrhNx28yIGdjSFLeoqcqDNswKr6dRHuzTBAc0DMGpQp&X-Amz-Signature=ab86bfb431348964878adffc59986478f2d1d738875f33b1e5528199b3006558&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OOQSI7D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BLSZL8lFrnRpXh3jdgZi5MNgpNNNZ6HMV6%2BsTH9DPAiEAiLzjpDVPbL2RrRi7XeLHkocKBx4j9SiYVYbXxmyz%2Bu0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQxU%2F42kVkT5UhW2yrcA6pcKJVZk%2BBiYSsSEbxQtjUi%2F%2FhwwJkn3ulHXYKTku0IdCiS5un2pKtlRNq5sy3KeoWYQyL54FQPxGyygPHeJ%2B3pknFh9PHtjDM94euhZz81Bp4WT9TC6VoXgqInqxBoaLhC0B6vmt4izu9wJTSPnJQ7LxwuTgBTClvRkSu%2FhhJgM6LKMHAaqDQrZHxYVX7l3qQTgqeqhCIUTit6wykwdMJF3bNogiDP0SAuK%2FGbT78jxP4UUdM6No4RrLeQB%2BhQwBtkaImsfoqh2z7JPoKbEZ8MPB7GQ0AIQxVPT%2B4YrHrxuLmuFI%2FbzW4bEJ3Nx4CUJFn2fwXRUK6uEId%2FlfjOi3VqKw4Su%2Fzo%2BaRlzFvHC9emjlyOixshQO9T%2B7fQkGiFTxD0LyCYTwKhHhDR%2F2KaGOe2kUXcBSLnPovHSRQ6UD%2BDrhQkkB4i0mo4PH30P7O4i%2B0lX0I%2FhaaCcH9GjKZtYeVJee7S3nUdgEQf%2Bt9KcX6yMAuaCHlrtQKYa4f1KotGBF15mfc72U3Ai01P%2FxVnOtJl%2BCz3F%2F9K5JMBX3zyZLKVYK00BHnzx3D5Rf0Z4po3q1F0cJIprc%2F9TRULrL6R0UOakM0vid2%2FU6Em2gqb%2Brkxw7%2FpscobhQq4UXeMMIvh77wGOqUBUiDwPjjUdcg6Q2Y%2BlQdwcA0vuCiOcSFeC1yj56jVFwrO5ulBEoEjnsNGdg5pD9g4IjUMWsT0kqgwhTFyEBAj6g53w7AAE4lXwFJEvd2XnaXG9A1wAaVFbSflB2lNdxvo7sHB5Yo5zWxX6csLvKFXDiWNVPsIRzYDeIosRJYQRK2vx9xbX%2FrhNx28yIGdjSFLeoqcqDNswKr6dRHuzTBAc0DMGpQp&X-Amz-Signature=3c8fa9a70728ae2bb54c035e75a26984ddcf0b0bdf60638307c066813daf50aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UJJWSWM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA5LCOWTrQwnJ9RLP%2B3xElAl7aZfemNYTNQ6KyR7LbJvAiAQhdsZ1cByxtA4k%2FqzjDcEm3evlqPz9B5xWlgSMhioQCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6QwGZt0xvA5LuTxGKtwDK6aT0w27rAuw3cSHBj0j5ZLrJBO8KtqvaqnenaR05Gw6fU8xa5iSKxpuimbt7%2FDWobjSGkzbCv%2FxKRRp1MGAZGkhIS7WWcsgZRocasWF44cJymUqWwh5qnx8FQKG%2BdF%2Bc1lw%2FzTOqYAKSZKIUy%2FGLvfXb5Rfi9vADajVibR1p2p7Ao6VcMmS2WT14IrgRMNs9CrADoIFsDZ%2FZd0jSHc4nVQqI3BiXqufjXtu%2FrVdv1be%2B%2FVNU%2BKV%2FmVSjwswiMqRaehexXUO%2BJgs6orIN%2F5rm8O2PGcfUNCyUS2BZNeoGtYEkqVbJYWsbL1rMOD6e2OVaTPOZevmrSx73gUGk098edsov2olb%2BpikymKQrXvL%2BCnUHnWgMJz9IAun3uJlTcyBiDscXZVpQAOpMxC6fGT2erqy0VPbB9h3xwiT45DT8fT5Ufw7DFs5%2FxznKn8ouiPZWSNf5GSpUDuS7a3eWR1eIcghKp%2FF9tWHeAaxfKbv7Ia8YpKzhKMwmjg4maspGWNr4i3Ppc6vMjQjBQnKVR%2FVaRIR56UdMOZUK8qRI8ndyLv6e8eCs2aQWk77g%2BoWTU76qJMr494BxFTkWAaU47d04xytXpJ7FG%2BR77tQQ%2BPaAbfaMzIPGmj9%2FPJVkQwvOHvvAY6pgEh8vgnK1y6RaJ0uNwSWSXjQoJRejMR6LKS1H17K1RMAImiJ75g9VpLPvDaNM1Zk7%2Bldkn4Vw%2BFlL%2B2ldg%2FhZETjx%2BpMnyM4Vbzfw%2FGKKdJYpf50dRcFnawrJTFH5%2FnuVD%2FkhyA1XvUfcWlMyRfDrRySaR23xfpEyBf8BYpN2nGEI6iz0jki%2BLHcH4Jw7du0W%2BpUS%2BmMd4jDqs%2B3gAdRVGyCq9tKrH2&X-Amz-Signature=0bc1488e51d8d9307fc575292604150c1933f76792469ad7dc58ffb95c4694c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZO623K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKfUZwZRmoa%2BCYgn5YeKUj6QczxYl%2B9gpqJjSaDOpXxwIgA7glFnfRpkMnLWwFLP4vOLcDD2d%2Bat6Fdmq9Aa9BP%2B0qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZSruBTDINHWNXA6ircA%2FeLoIR%2Fz4xNQV1v8UWXhnjeSKe24mfcHwdiyaNTYSS4oi9hXdQViUjwJvkPBD6sPYaKd87JnifuRXjMuotQx9K%2BYGP0z3YWr9dMkcaFLUW57yljkmkIoXrqzW3u4xHR5HqxC7peomKkhI6omwR7hZlY6gTOOMh5xjqQZ7XEvArRJO%2B6mzGv1P5BwFnfye8gdSzqpeXX5kepDgpep008D1TNz9nVh%2FtuNsT6rS49hZJbayKZ%2FHehg3jk1fMwKw9NhdQ9ZRIFiCojGcj72E1jRWdD5ghstiOY7H0u9VMPSO8rYdmmfmHg1uV9akJSwiqAOZhGQ1i2KOlpDHz32L3XNFvfOaHHcE%2FVEiPJVsf6DOB4wYf0PnaKL7w%2FNPjXEi2oPXihxAH3Q%2F47h3TwbKnlr4pSB4CxlPtXEdLetlw%2Fy%2FBBwgeg3HvihP9ktLES2eqC176bq4L7LpDWWFZwN%2B0ym9L6gsnDva73mRnBuuxlkFI356Rv17ZoVp3Pg1Z%2BJpLoD%2FYZg%2BjFVF9hAansb9CWsddmjcIEIF5QmIJz3uzgfjW7sQwkmw3%2FQWXsIGcR2mEdelQsyjv%2BQiyV9uT2v%2ByTmd0%2BVQkfhsOR939Rx3bN0nKwjmR7eLeIvh30ZwWWMMbh77wGOqUBp5BILp0yYWiea1bTrc5ztTIV%2BPz%2BPtv%2Bpt%2FYG%2BMQjFqaJWgCnJkfODQVqysJXBlQ%2FCyxqHjpzcFpvQHByQ4vo3lJtQJtU86L%2BCcgT4jLsm0CMZpcxEwJODhzX6Ax%2FfmCYGcKErmLEAOvnWaKNtqoPZuyY3cOyj1s%2B2ElR29td3Q3dKCy2rrCkEePT1t268%2FZGH1xOtBDUgEN2PxbHsbaSBcckSP%2B&X-Amz-Signature=999477f9c720daaa58392fe78ec2455a7f37c49f4dab00a3e540a3a80dfd80b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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