

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=a7c034d4d8d3c220a7b18725786de92d3a2ec044d6dd432731ef8174565e4e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=2baace37903594530acac82ffbf84627d4884f224267f1d278f968e550015047&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=367de54951b75b503ccb92429720723f9647364d93a9e4b1d99117a455ebf0b6&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=6d43dce3551850d075786a96d2acc64273bc7d31067a1ab5ec0e78d69613b743&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=f07a3c349203d17ad3ade77166612e258b0f20bdfb5046c38bf9aa0b448216ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=b21e2c8b5df89e193232a1d1f6725911737d1f2289b8912a6dcabbeddc34f675&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=ece28ff223dd7c6dfb5dae7734663929b48aa47e1a29b1fbc4f276d29215f47c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=8f449eec771c2f5a0ac9f414176cc204bea9c0e59d137adfd655b1fadda4d2f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=8a1ab5f65271ffff3fe5149e1a6b0cfbb4549ad85b5417257aeccb3a4e217c86&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SLAKK6W%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQzDQEjhMm23EDD8mIhz8xGvE6l1JtVUK3T66TFg7eXAiAMp4XY2znSE0C6%2FFL94cWqYwqnGPHfZ%2Bo%2Bnre9MHpJ4yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq0xBcxdkGjmKbAW5KtwDbcUnrRKG61NhvqnPwWrTvsMhq0N1vPjCkiOWjtV7UeluJLeOxVsboLNJrxlu2IeFiUnAnXK8i4XD9zCTq1aObtMoJXZgnGZrNgy7S14jqROuA%2FzF1NQht4xLwR2WzUcot8r4lmNw4qrlGtByfW7ZAdU10ZnJwlOIessqm%2Bfejg7aQlE5GCI%2FYJGhkHaGfw45C1Qm7Lzsr7efCFnyV1pwYdU3e8TGwZTLqdysIIZVJ86j0dl78qPoHqqTkQSbvoUpxx7huPMuo2clz8FS1K%2FbwTtlwK6rifYmoDt3PwqZefOqGkZUpY6rpnYIVUZ4HnqylM4PMpQ8IFH%2B%2Fjv1S5MrVa1UwaAe1KSQC7z3ATQwY8cVLdykvfILmb8St5NBav1yp4bFihvCkaT6OyG95eFvClfwkJWJwzwagQeXnjBGfh3MdmfstPj5qIc%2Btll7MGpgG4cVZuKH38HN6JafC%2FWX0nHcU%2FWNtRJ7zfF2rUKbPQd4MkWE7WjcFmIBugkKfkFKOJHrRf1U%2FFgNecT0yeMrK6Anu4Rlcan1RY0aqWKVl6mrNn%2BW9qT570LvrwEBr%2B8%2B1ki4dzq1D%2BefLHEYfWpcsZspmIW%2Bvi5dHgQyPs7%2BavrnDZxOcgsGxB8Qmpsw6t3%2BvAY6pgEQ6q%2FTkuMnlrLYbny7f8rzr9fOBiw3ImZyX%2FugsOTg7CnjZJRbo2upkGcT7b7UlYGYDE1F%2Bf8CZXwSUvKnHGs9wo3de74LbRLgEXtnrhF%2B7Yp5uWk62%2B5E4O57OoLAzSkV3elgd3ju14a2mIsT90O86iE8kn3Ej4qsz0CHDjZ2gp%2FmSAcz2p6124Od4ChUaOJphZT0qTiv085qhE%2FWzm5auu0nbTzB&X-Amz-Signature=def2a5a4ca990468aefd2467f0d46eb976cccc00b4de1cbb290939537418eace&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SLAKK6W%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQzDQEjhMm23EDD8mIhz8xGvE6l1JtVUK3T66TFg7eXAiAMp4XY2znSE0C6%2FFL94cWqYwqnGPHfZ%2Bo%2Bnre9MHpJ4yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq0xBcxdkGjmKbAW5KtwDbcUnrRKG61NhvqnPwWrTvsMhq0N1vPjCkiOWjtV7UeluJLeOxVsboLNJrxlu2IeFiUnAnXK8i4XD9zCTq1aObtMoJXZgnGZrNgy7S14jqROuA%2FzF1NQht4xLwR2WzUcot8r4lmNw4qrlGtByfW7ZAdU10ZnJwlOIessqm%2Bfejg7aQlE5GCI%2FYJGhkHaGfw45C1Qm7Lzsr7efCFnyV1pwYdU3e8TGwZTLqdysIIZVJ86j0dl78qPoHqqTkQSbvoUpxx7huPMuo2clz8FS1K%2FbwTtlwK6rifYmoDt3PwqZefOqGkZUpY6rpnYIVUZ4HnqylM4PMpQ8IFH%2B%2Fjv1S5MrVa1UwaAe1KSQC7z3ATQwY8cVLdykvfILmb8St5NBav1yp4bFihvCkaT6OyG95eFvClfwkJWJwzwagQeXnjBGfh3MdmfstPj5qIc%2Btll7MGpgG4cVZuKH38HN6JafC%2FWX0nHcU%2FWNtRJ7zfF2rUKbPQd4MkWE7WjcFmIBugkKfkFKOJHrRf1U%2FFgNecT0yeMrK6Anu4Rlcan1RY0aqWKVl6mrNn%2BW9qT570LvrwEBr%2B8%2B1ki4dzq1D%2BefLHEYfWpcsZspmIW%2Bvi5dHgQyPs7%2BavrnDZxOcgsGxB8Qmpsw6t3%2BvAY6pgEQ6q%2FTkuMnlrLYbny7f8rzr9fOBiw3ImZyX%2FugsOTg7CnjZJRbo2upkGcT7b7UlYGYDE1F%2Bf8CZXwSUvKnHGs9wo3de74LbRLgEXtnrhF%2B7Yp5uWk62%2B5E4O57OoLAzSkV3elgd3ju14a2mIsT90O86iE8kn3Ej4qsz0CHDjZ2gp%2FmSAcz2p6124Od4ChUaOJphZT0qTiv085qhE%2FWzm5auu0nbTzB&X-Amz-Signature=f2d3146153df5a2de40f1c52a5b789e6ce43eb119e0c1a0b134a90383b1e9f8c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SLAKK6W%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQzDQEjhMm23EDD8mIhz8xGvE6l1JtVUK3T66TFg7eXAiAMp4XY2znSE0C6%2FFL94cWqYwqnGPHfZ%2Bo%2Bnre9MHpJ4yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq0xBcxdkGjmKbAW5KtwDbcUnrRKG61NhvqnPwWrTvsMhq0N1vPjCkiOWjtV7UeluJLeOxVsboLNJrxlu2IeFiUnAnXK8i4XD9zCTq1aObtMoJXZgnGZrNgy7S14jqROuA%2FzF1NQht4xLwR2WzUcot8r4lmNw4qrlGtByfW7ZAdU10ZnJwlOIessqm%2Bfejg7aQlE5GCI%2FYJGhkHaGfw45C1Qm7Lzsr7efCFnyV1pwYdU3e8TGwZTLqdysIIZVJ86j0dl78qPoHqqTkQSbvoUpxx7huPMuo2clz8FS1K%2FbwTtlwK6rifYmoDt3PwqZefOqGkZUpY6rpnYIVUZ4HnqylM4PMpQ8IFH%2B%2Fjv1S5MrVa1UwaAe1KSQC7z3ATQwY8cVLdykvfILmb8St5NBav1yp4bFihvCkaT6OyG95eFvClfwkJWJwzwagQeXnjBGfh3MdmfstPj5qIc%2Btll7MGpgG4cVZuKH38HN6JafC%2FWX0nHcU%2FWNtRJ7zfF2rUKbPQd4MkWE7WjcFmIBugkKfkFKOJHrRf1U%2FFgNecT0yeMrK6Anu4Rlcan1RY0aqWKVl6mrNn%2BW9qT570LvrwEBr%2B8%2B1ki4dzq1D%2BefLHEYfWpcsZspmIW%2Bvi5dHgQyPs7%2BavrnDZxOcgsGxB8Qmpsw6t3%2BvAY6pgEQ6q%2FTkuMnlrLYbny7f8rzr9fOBiw3ImZyX%2FugsOTg7CnjZJRbo2upkGcT7b7UlYGYDE1F%2Bf8CZXwSUvKnHGs9wo3de74LbRLgEXtnrhF%2B7Yp5uWk62%2B5E4O57OoLAzSkV3elgd3ju14a2mIsT90O86iE8kn3Ej4qsz0CHDjZ2gp%2FmSAcz2p6124Od4ChUaOJphZT0qTiv085qhE%2FWzm5auu0nbTzB&X-Amz-Signature=db0ef1f5e7421cd0a4d520abd4818247135c8fc9901ef6636df649010e642ba7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=1baa2f708c874ce3b59e9cbd9c8a91dc7ebdf26aa1662e1c7e86d87d86064e7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=ecc5f104034b213609229d61da0f9ed6e9ac18446b055b30b99974aa3c84804c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=a7211503c63309f4b72359f59e780759b967cc1c8ba574469bd4e418eafbc41f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=d7ca887f5b6608daa8f04b932bdd0893c903ea7d984f1fac8f1a6ea30e518db9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=6a560fa51a8a73ff4878ae2f44211976778925f83175aaef08fe1275d30d1c86&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y3VSOJ2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEyhlnQra2NvkDUhisC3w3oTrHd55zez8fUHsT1g9iroAiAFdtcuh6UYSnp%2BPltF8I0nAkXvSZPENnbK%2FX%2Bu85nUXiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDHirEqKxX%2BtM4DDgKtwDpXRnDn9EJckOtsxMx85nHD3pq9HJBGYmkBN4BeFYUlefKGP8fyd18clvcxg7NFsYxbDj70QXq%2F4ZoWIYmyauQ2ejZgoQp6vEEXdy3Ir73VCz80lQAiVOT8rxSC0C8ZOUh20NznBfvrbzlve%2FkWHmT1MTqc8OnfIpVxfFUq5gtANEHSoC6Y5RdwZa2mh3VMHiaggERCHIlXybBQgIMkWwwSTSF6WBUFgNWa1KSduarK6Bcd1Z0MZzxW4vqsi6ENhPK%2B1pwVS3t2fC49ai0IGd7sQLjOcueldCbhYLKFP6t9uJT%2BNPH27%2FK%2FXvFZgbFhquE4inSYxN3j1%2FQS0YGN7T8mwW1Y%2BQx60yrDb9mXX2Wm7huSg5sgr17pEonlraPaVKHBGU44k5UpCV9wN0TRB9nqLtdSJ55tWCetYD%2BowV97Y0%2FQmqPZYAp9sBqWVq1jMPod6H0gvPHbNMkAUa5Bl%2Fkg0SOIL7ts95zjB8tTzqJnoQjDN1WUPwZSrIAuJl%2BtlO2MJHH7oIStKU%2FYvEqzK4fWP21zKLcRaQhR9kXdT1i0uaKuYMUEvoqIJgVv4%2BAOP2Ni6yB0hmO6CbVgwEgFLLCQRWlo4RxaMLII%2Bv5KJTBMZzJQ%2FHWlwgVRk3r2Uwotv%2BvAY6pgGEQifmhbit2dDugwHxzo4H64S0rYMnzTP6R1Zp3%2BoOJBdjmH2JTT0sW6PT7sIm0IRoeQMR%2F8ijmY2MpZPNRw6SvxfWZDWfcrnIQQx7IUwvJKC0roZNyDOhxSUd0It96%2F%2B9JCU26ewJ%2BSOgKEgfPtuG00aReL9N25waswW%2BpCY6c7Kl2OnhiRjBWhpZXlzhyjMS5Bk4ZrVEsr0POGEEJGl5WUN1uWn%2B&X-Amz-Signature=0a13dd40772c433144c76cdc35f9fa184acfd487f48238713eef45f784a9ae3c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DTCWO6P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDXrxrLh0HzYHjb1AENKAp9RHS8uPDK4KgTACXwtXuuAiBQDD5MQvmJrpM6utCi9jS50lLfEazOrksjFQyQjxOi8yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw3saPkqCGQBDyM5GKtwDOFVnI8y%2FrDvVJzYjRWphjWyvuWeESoQb38Apz7ySg5dDE6wVzkh5q01fw6AIeEw6QzOH6DSf6SU0%2FKvH5RjDalPFXQXBylT5t34A13JU2xY73yRiTLcwRuAMD0CYx5LKqenSa8CTDC%2F5ybvWUJhJ89xWwB7ilS%2FgJwJKTv8oiI0tFTubSLYfY6xy8zBNR%2Fzvr4p3kn4R4yOpQXX96pJ6zmpN0jkGEoth4QPCAD3kCF7EVasYTf8ALqWX%2Fr1%2BEeKNLBcS0NYWcUMjoQXrSqbHhlkrZdh%2BJcfPkByaQFVuTeEQPYDUkIhfK%2B%2Fa8Ouk8o4A%2BQThOb9SvghdHsoHLfsOva78RHr%2FfX9F6BCWVA32o3WWXBbnmHxjy6nDsg4b0SI9UvJz6YTBnIFvnB9W%2FVNEEDRRsR62A6UCMQtGF%2BpBmSVQdgzrpC4dA%2F6WGmkWI1d1p%2B3EHqV%2FwmAZWD80EAJDf1LLCbJu3zrjPcHVqQojuTjrWFOnmbmQ3VcFsDyiNzdg8sT9Sx7X9%2BYOfk6LcaPKolXRQxwSLM8UMtcs6PvAzvV9AtUDnjYJUcPcT2sGPTtM5LM5I79a9eU172OEvuf%2Bhzm1%2BnZUrtsGuuYqxaa4nztxSe4MdPEIdT%2FBEGAw%2FOP%2BvAY6pgHjj%2FI62RWSyG5Tmv8vZvA8vRoG4eiQvumvGmx%2B0WVMaP%2BV24BunSYHXWz5VksWK7hrlzkdQWG8HbGojLl58o8ulfFKqirfOp7D0HfpQp8PbPU12XZ%2B3vZ5%2FL7NkfrZvvxGNQovTfCCAoq6NYKVMf7m8u4TcDpXFArkNn7lMPUlyZFjrEbPUgOT2D0li8af%2BZdTgwfB99%2FHe7jFzt8hz%2BBB9QXmf1M%2F&X-Amz-Signature=571d71eec19f4417252195c5b703b6bc7455f2e682ee6eab0db474620d479b18&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DTCWO6P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDXrxrLh0HzYHjb1AENKAp9RHS8uPDK4KgTACXwtXuuAiBQDD5MQvmJrpM6utCi9jS50lLfEazOrksjFQyQjxOi8yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw3saPkqCGQBDyM5GKtwDOFVnI8y%2FrDvVJzYjRWphjWyvuWeESoQb38Apz7ySg5dDE6wVzkh5q01fw6AIeEw6QzOH6DSf6SU0%2FKvH5RjDalPFXQXBylT5t34A13JU2xY73yRiTLcwRuAMD0CYx5LKqenSa8CTDC%2F5ybvWUJhJ89xWwB7ilS%2FgJwJKTv8oiI0tFTubSLYfY6xy8zBNR%2Fzvr4p3kn4R4yOpQXX96pJ6zmpN0jkGEoth4QPCAD3kCF7EVasYTf8ALqWX%2Fr1%2BEeKNLBcS0NYWcUMjoQXrSqbHhlkrZdh%2BJcfPkByaQFVuTeEQPYDUkIhfK%2B%2Fa8Ouk8o4A%2BQThOb9SvghdHsoHLfsOva78RHr%2FfX9F6BCWVA32o3WWXBbnmHxjy6nDsg4b0SI9UvJz6YTBnIFvnB9W%2FVNEEDRRsR62A6UCMQtGF%2BpBmSVQdgzrpC4dA%2F6WGmkWI1d1p%2B3EHqV%2FwmAZWD80EAJDf1LLCbJu3zrjPcHVqQojuTjrWFOnmbmQ3VcFsDyiNzdg8sT9Sx7X9%2BYOfk6LcaPKolXRQxwSLM8UMtcs6PvAzvV9AtUDnjYJUcPcT2sGPTtM5LM5I79a9eU172OEvuf%2Bhzm1%2BnZUrtsGuuYqxaa4nztxSe4MdPEIdT%2FBEGAw%2FOP%2BvAY6pgHjj%2FI62RWSyG5Tmv8vZvA8vRoG4eiQvumvGmx%2B0WVMaP%2BV24BunSYHXWz5VksWK7hrlzkdQWG8HbGojLl58o8ulfFKqirfOp7D0HfpQp8PbPU12XZ%2B3vZ5%2FL7NkfrZvvxGNQovTfCCAoq6NYKVMf7m8u4TcDpXFArkNn7lMPUlyZFjrEbPUgOT2D0li8af%2BZdTgwfB99%2FHe7jFzt8hz%2BBB9QXmf1M%2F&X-Amz-Signature=7b226bcbba47fd6181cafe7147ed3bed82b11e63e845dda0ae0361df1fa10802&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTVKTATS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdmDpyXD%2FY0JI584A3CGvDkKebFgTOv6m5lj3FW%2BIocAiBuHnixJ7HdoH7JAPruuq6zXG6z43uqY3MsQ2mV4cagjiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7HerE9HvN1Bhku3bKtwD1NoUZPnVLpMwtmnR6Rt5Ep4MlN%2BBRf91EYiy5HMi8Cz%2B90H%2F%2FsKtgX37u2Jf1pfa5%2F60V7POaM4PaQAj%2FE8qicnLorWRjYOce%2BXTFs2NAwVMh8a%2BAl2Rcw%2BXKZLA%2FKdf2nvZ5mzNwgYqXGnjm0X%2BxMUM%2BRpBS0GATneLhNlCxFks1w8RtWYXxwfpjaCc%2BN%2BTKZ9LyHuvtD2wQugAp%2FP8AxvHiUHpuqo6Q2p7xf7nNf3kGq4nO5FMlh2oPdguwpcTj%2F3MNNueaBHxUgzTAEJ%2F9uCv4flyeYkpMyb7YCZLPcLULJg2ZD9hIpuFGocs3TdQXZloTSQhud%2F6su4Gu43Iqi414F8Y7a5W4jvG8eClLMh4Mh4B1rMZVAQqQxSqdmdC1H3EwA0VU36JXYme6qaklBOQljujWCFlTQpIb3RIXkeU8U2D7tLJ%2FsjDZDiBs2qzcZ5kjv6cx6UUxn%2FhkGsXGBZSVN63k7gvmYpW3FtiwhCNm1beMJqMOazGzF2jPDl%2BYEs18QLEUTHxIFr1%2BJ%2BDrkNJ0h2iV82QFbM9MFcNgk319q%2BwNnpS9rHFKQs9iJYXHyhsLMDpK8Y9xGaQRZS9Jk2Iut9kwGxreIXdsf3%2BkD798NkJZlg6ll1dnvEwk%2Bb%2BvAY6pgGioplkQa%2BBoTolPP8KsIbMOiJ%2FvPIkHHKNjS3fGuxK1UJ4qy4olMHohwFiybeWQqvPj7TX2czuNJoH%2B%2FMMQdLzjhzmxYzvKOPcyx7CZr1ES%2FzCvu1OdKWPdAHxraAw9ErejXvGcZefO8AoafxLgl753Ha6uBi0UIC2UoH5EoTMHU1W3ehTZONnjQs2NGClaT1XetTdIU9Zj8L3ixa%2BYXz1brbC7CYy&X-Amz-Signature=9ad8fc41dfca8cf49006843178b300f9e4d7849c16d54ca6a5a2309b614c67d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRD7VUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAll9UxBozUHetwDaQDfO06n0a%2FTmUBS0u4YYem2w5mfAiEAjv2lvBvD94EN%2F%2FaYxj8aZOWHvYiLl5zOGyGs8HuqeDoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0RyluTxOA%2FNMF2SrcA1vNSmp8seDTIlEa7CkGb9pESm%2BVGzd8ZO5bElo9mKKH%2B7R16vz2MkyWYigMjJoAXcISEKO28di7mgnp2xRvBmBWIm7OJAGJZY4DFXHwT3KXG1ZNb9FsZ2eNp7beyg2ZzhIxacrpi6Yf9kthJNhFaQm57k3pZlH6t7Rlb12hEDrgoQDBN5j4muaVqBm%2FIp49rqVuB25YdTk21%2FFaP5JXseAWgO%2FFtjl%2F4BtBN2sQXyc0jIbojtAM%2BDSCpy0HG%2FIzBb5l3fd44Vop2APLOVD6m9ugY%2FM9rT3LA%2BuCbF0qUulodiV%2Fh9CJqaiqwC8WwAm%2BWzOzgLAN6c2hOjsVBlkRi7DqUB2EQE4Kg5Ffi1q917Oq4mC9JtIb5%2F6qsU3PAZkQlCFek5aAgf0VX50Rku1HLeFP8iJggUnUHY5LWVpG6zqqa0zXJcOJTCsJ4bARvXwJm1mrDl73FtThC%2BqYplOjZ3eHMklnh%2FkK%2FogYBoHuzeAdrfOWCLW9k3l2Agy7QLzvkROW1EiI5WrFC0wyceZrYZg14uaJuUvZ3T1bzV9fNxI%2BzKy%2BSBoWzf87SZL57TXl%2FrZXhJNZ8VHPd5ul1ibyxFk6An%2BdNGWDlssL586kP%2F2T4StFXEuNv74uNJKMMN7b%2FrwGOqUBm8QZL%2BZZqQT9nvKov2RqP0JNlJ0OOks4qpZt%2FaFQXGBL4q8jXaP42xsM%2FzygAqSQIrU196zgibcziL3z3fRMB5CfhCtu2kqM82%2FZaLLJVQQ6KkcoyLyUcdjZ0t%2BeVPhUAHtQ1J%2BBCXNTISY9jeMCYPVHMnLqxyNSXE56z%2BT132GyIwLA4NEw5Mvc6bIbQmWHrNnPBRopNaNRS8fu0Y3rNJC5ns6R&X-Amz-Signature=9b759ade7d435c06c17f146840889a5a1ca5ae7fda2b96d29385ffa5fb3ae85d&X-Amz-SignedHeaders=host&x-id=GetObject)
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