

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=d3f87c7e866c16708e2e97cee5621d241b635e799a4ec73f9a27d9dc6aa394b1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=eecc926e4b80d6ca39e57e14ea4b0ef8a50f9446819e5e27ae1606d3604a8b97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=bfd371d5616fc1d232323cff40c553b24d17eb0364ceb26c3ca024dec6f5799d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=ca61f7ff2e47cac68d24cc603b9bedda1d5dc0a42d045e4f3cbb7afb3c398042&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=8e377241ef13291f21615636b532a3d73051d7263a160f68333771b01b2132bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=88660a1758ce44404b7798f29d50ee585f01a21a3e2fdbdfc195acf52e79d4cd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=e9da56fabe3201e38d1a408be97187f99dde7c4abb4d8b85d7ed4ebc51d2c32f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=73be99be9d38378b74bf54306afc3d2168cef7ca8001c255bfe96a1e0cc37c79&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=69a3e55dbadeee4626ca34abd7c050021f094100f03aeeb2e6372a249bbe1b14&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3ES4FPV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr7lLGl6%2FOEbj17AQNEKZBALhJXJUhMdYPKrePDFIOYwIgM%2FOCv%2BnmFghhwUI6nZ5ea4hDd9%2FFCtxKvNE9A%2FpnzGMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOUVcotymOmmnqzt2yrcA4xUan6x9jTOy20LhqHPwhomcjMbSwytJB4hJSWZQk939GImZz4ff%2FhJvX8fgpjMiMb2cgMsIRwXxJI0es0VZ%2Bd95OHJJz%2FSYlUjqNw0v8hekMuwLql9N7Zr0uDE4qGxqKok5%2BQMV9lpWdyJbDfk0UqVWhWluF17vYsokEAJ6ET6UVCsTCgfLc77M38jekb3CVUz6uzVnbIYghOxjfDpafEKnx%2FkGEJwnTSb1yKne2zV%2FjgbSx1jr9%2BlKR8mSn7OVb1fjPJN9Biis4rAG%2F0TnL%2FOKW2U0Ww5TQjJPu%2B6Kx%2BOBS28PSiJBK8A9C9BT%2BAs63vupHCnPP02%2BpXsfvgb5ZJdwpWV6FIYDnVIkMy4CvW2btTfBQjRUxHkc9uuBpylnyB2Emo6hUW6srzRrRq0%2FgJ2opAkQAzc9BYlBnbqs0woExLWbEwulZ8IYhHXzmUl1Nyg3TPMhDutqiDerAaZwMSAO2thaMIwBOlMD1J2NjFf41yVOE2t2AQHSHVga%2BxInFfEpPXGPwMURezS3tx%2F%2BDwUyiW%2FX5SmaL4ifePrQ7oiM5UHjhk3wYxj9WW8%2BL3F4Wk5J4qCnW0IVYy74VnUBp%2BuM9gIqg24e20W4Xo%2FbxLyZvM1ddZ6iZI8G5C0MKfk%2F7wGOqUBoK1ueMI5p8%2B%2FnbolCoUWNFux7IXXy71xJhIm9s5OaNnxQkezLJXuVoSEi0nFPGvaBfgqz%2BFGTHwUWLiZWu668F%2Fw5mg0YJq4ViPZI2eCpv62biXQIQ1KUWD4i5KCAI5I%2BAV%2FFuymqb4jJScIfMvQpo3v3mgW%2FLNakc%2Fu3eGUf3mihe59%2FsGbdUhJZDminR2Gn1k6aiqPKMjWixa2QhPy1IaiXYt8&X-Amz-Signature=7abeb6b5a0dd5cd6a4b040cf2555e646244ef561c6fbac61f0e3dc1a193374c2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3ES4FPV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr7lLGl6%2FOEbj17AQNEKZBALhJXJUhMdYPKrePDFIOYwIgM%2FOCv%2BnmFghhwUI6nZ5ea4hDd9%2FFCtxKvNE9A%2FpnzGMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOUVcotymOmmnqzt2yrcA4xUan6x9jTOy20LhqHPwhomcjMbSwytJB4hJSWZQk939GImZz4ff%2FhJvX8fgpjMiMb2cgMsIRwXxJI0es0VZ%2Bd95OHJJz%2FSYlUjqNw0v8hekMuwLql9N7Zr0uDE4qGxqKok5%2BQMV9lpWdyJbDfk0UqVWhWluF17vYsokEAJ6ET6UVCsTCgfLc77M38jekb3CVUz6uzVnbIYghOxjfDpafEKnx%2FkGEJwnTSb1yKne2zV%2FjgbSx1jr9%2BlKR8mSn7OVb1fjPJN9Biis4rAG%2F0TnL%2FOKW2U0Ww5TQjJPu%2B6Kx%2BOBS28PSiJBK8A9C9BT%2BAs63vupHCnPP02%2BpXsfvgb5ZJdwpWV6FIYDnVIkMy4CvW2btTfBQjRUxHkc9uuBpylnyB2Emo6hUW6srzRrRq0%2FgJ2opAkQAzc9BYlBnbqs0woExLWbEwulZ8IYhHXzmUl1Nyg3TPMhDutqiDerAaZwMSAO2thaMIwBOlMD1J2NjFf41yVOE2t2AQHSHVga%2BxInFfEpPXGPwMURezS3tx%2F%2BDwUyiW%2FX5SmaL4ifePrQ7oiM5UHjhk3wYxj9WW8%2BL3F4Wk5J4qCnW0IVYy74VnUBp%2BuM9gIqg24e20W4Xo%2FbxLyZvM1ddZ6iZI8G5C0MKfk%2F7wGOqUBoK1ueMI5p8%2B%2FnbolCoUWNFux7IXXy71xJhIm9s5OaNnxQkezLJXuVoSEi0nFPGvaBfgqz%2BFGTHwUWLiZWu668F%2Fw5mg0YJq4ViPZI2eCpv62biXQIQ1KUWD4i5KCAI5I%2BAV%2FFuymqb4jJScIfMvQpo3v3mgW%2FLNakc%2Fu3eGUf3mihe59%2FsGbdUhJZDminR2Gn1k6aiqPKMjWixa2QhPy1IaiXYt8&X-Amz-Signature=ed21db7a09d0c456b13e17a007204b79036fe348c0b7f3dbd068c6cf84668e74&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3ES4FPV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr7lLGl6%2FOEbj17AQNEKZBALhJXJUhMdYPKrePDFIOYwIgM%2FOCv%2BnmFghhwUI6nZ5ea4hDd9%2FFCtxKvNE9A%2FpnzGMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOUVcotymOmmnqzt2yrcA4xUan6x9jTOy20LhqHPwhomcjMbSwytJB4hJSWZQk939GImZz4ff%2FhJvX8fgpjMiMb2cgMsIRwXxJI0es0VZ%2Bd95OHJJz%2FSYlUjqNw0v8hekMuwLql9N7Zr0uDE4qGxqKok5%2BQMV9lpWdyJbDfk0UqVWhWluF17vYsokEAJ6ET6UVCsTCgfLc77M38jekb3CVUz6uzVnbIYghOxjfDpafEKnx%2FkGEJwnTSb1yKne2zV%2FjgbSx1jr9%2BlKR8mSn7OVb1fjPJN9Biis4rAG%2F0TnL%2FOKW2U0Ww5TQjJPu%2B6Kx%2BOBS28PSiJBK8A9C9BT%2BAs63vupHCnPP02%2BpXsfvgb5ZJdwpWV6FIYDnVIkMy4CvW2btTfBQjRUxHkc9uuBpylnyB2Emo6hUW6srzRrRq0%2FgJ2opAkQAzc9BYlBnbqs0woExLWbEwulZ8IYhHXzmUl1Nyg3TPMhDutqiDerAaZwMSAO2thaMIwBOlMD1J2NjFf41yVOE2t2AQHSHVga%2BxInFfEpPXGPwMURezS3tx%2F%2BDwUyiW%2FX5SmaL4ifePrQ7oiM5UHjhk3wYxj9WW8%2BL3F4Wk5J4qCnW0IVYy74VnUBp%2BuM9gIqg24e20W4Xo%2FbxLyZvM1ddZ6iZI8G5C0MKfk%2F7wGOqUBoK1ueMI5p8%2B%2FnbolCoUWNFux7IXXy71xJhIm9s5OaNnxQkezLJXuVoSEi0nFPGvaBfgqz%2BFGTHwUWLiZWu668F%2Fw5mg0YJq4ViPZI2eCpv62biXQIQ1KUWD4i5KCAI5I%2BAV%2FFuymqb4jJScIfMvQpo3v3mgW%2FLNakc%2Fu3eGUf3mihe59%2FsGbdUhJZDminR2Gn1k6aiqPKMjWixa2QhPy1IaiXYt8&X-Amz-Signature=e9d9b7bb73c963106c3cc72ec0e7c72223b8ef185ba073867b78bea0e615c338&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=c840b03eba41955f0e34c7aeaa0f9bf16cc6f4ad3205a3bac84674d6cad68f26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=ea8c86b1ea9cd0ca2fdf112fab5ef363df55f1c9edc667299956d5cf2947fbc4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=2c4785d5f899309a1f1f16ca1efe4305d4fd4f4696cc675222e222dd1f70cc0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=3b73a036e0cc83125368151c533b0fe49bc4aa89f4889eb1cdf95401fd455fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=00b531c166fd6de4fde4d97720bd88a4f0fb33c1181a45cd3c45554170334e2c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OTUR4ZI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNIJFR%2F%2FBDzUTpSnWzAlkT5BPMJ4bDbQe%2BFS4Nku%2Bs6AiBblLb7Ritwjqkt1jAM2sf%2BLms7%2FO8uWMOietonacDnNCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuY2afv4ZDiwirhq9KtwDwWfHiQCHKTBwR53OAU2Qpod04zPq5cOeG0f5SR%2BUUVL0NFHRQDKJw55mTC42%2FbIg5W0Mbnr6cW0Epu2vRgSBs8YXsxZqYVHgR980PsD%2FbDuUq9PKf0rVgsnQCNammuPKzzdcHAfZ8EYpJHdql%2Foi7zbDAPfQ1wX7F42F1goqQc5WsN%2BInePsxUXX9rBcZztUp3cvyfy8pazCwTuErznd%2Bp%2FLJL7HUKJYeg%2B9EjhoigyJihuQKZ8QFcrZdqhQhKibWh3CkAG%2BHN4qJgUmVcEf3tv%2FkMwARENqAXR527aVegXzCjCB1GJUGfiya0nk%2FeEdpHDKD1p1pKugR4Y59L%2BRAHhINL%2F9lljUrwpE4Ghf%2FEce%2FdAWvGs64OtBC4LnVTcQ8hp64WxmdNFAD2X6C%2BCJIkSnQ7p9vRJuja39nRwYk7Dh%2FJF4Kniw5HJcHU20ID7v9VEyJdr6Fnhi78ZkhPBRyoRss%2BMyU%2BDaO%2FI9jfdaMzvAFIKvQBo7w%2FWJYgk6ue2y9S3QhjngnqaAGMA4TtJUSF9c0B3XBYy3wkLKHvZWm8dC0Bwwlv%2FK0WTYNh6efwBv%2BbOlyiCqbOUWNzkT5HWWTsUyPVxv5C5FbzHyQ7r4a%2BuW2HgRMPTmQPi%2BY48wp%2BT%2FvAY6pgGsfk9By4IpHATs6z3RrJZ3bsBN9TMbmcDjUPfBxDhdykw2SKZl%2Fdpak6Ohu8zCER2%2BYLxJEL0CFgIGiqJ%2BL6tDLPH4h78Aev7zWkLgYXH8%2BY5gtz%2B0Cwy3IzPU0HXJsoBFHSkTmtUbg2nvommBwCtor9170vxm5TI8LITmwbkYR%2BgOaLz1S8JSM%2FFvn1hwezcWqyBSEEWJ7VlsIIFSOSQ%2Bm5bipvsP&X-Amz-Signature=e8d781b52d0247ea11c48860d4a445087a5f89253852e98db387bc435322847f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXRGDDLN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfYeVP3pugOwKqghJ4vOgmzwX3BW4ZOBoFLOfViXgE6wIhAK3fYiqi0DmcEqasSXVzDaAFKRIEb2CuB7HfXxzhxatEKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6mvLWIxzgbtbZxCIq3APhx5fgBUQiJ9JxY10FQOAmd1v1qXJBhNIb3hw2wLPMoV4uYeFHcHWSImkzbwl%2FKkTdEZZRMX98Nsj%2FTjMPGN%2BxBziTWRNcF3gdviHCfySIt5w4IQ6v9EbBOVOGSbkmcUOi3fGm2Bdmvph7RDoqhi2qtk6YQi4rGCByTS9KG%2FAUJdFRLKodgCHb7pNyPQ5TRNfqWJcE39k%2BvBHv1LE%2BmKWNNFsDCRHy%2BiA69LQtbNNHaZgugogDmN7ybrkAg%2BVGWPfmHnFGOaFk1F4%2FBcrcmguyFBQiShyqx5IxJ6w1FdMaZgkZ5p5FIt9srApgsSgB6fHyVinkQOcg68LPQq57QDAeiUyCyPeoqQztzmv1OZfa55mEm7L%2Ba3z7o3pfFcM9mGEWZGqa%2BkaCehIqfCsM7DewRlmE9PjNJE2%2B4zIYgmHYdf%2Fu8UydhciI99qYjULRRGVqkfD5IjDaxe7neOiImJsEB8VnSdZWqcAihh4bIwp%2FJvuXsMNLV4gxfWWdEAK8M5uJZUaV1%2FWp2n%2FQN7NM7ijf%2Fj9nNPi5fuXId%2BzdtKgMF%2B%2FubQBTMWdOiygCqEgCQnIWpRkBnGjOMtgY7u1YWbMqv9DxjDcozqT1AymEuL44HttCNeNdnCPSzVM1EDCu5P%2B8BjqkAYxlcwd38sF0itxgYF616fUQCIhQbnXseBx%2Bw7vbx6xQ6dD2HEe1RJwxyftBbRj0HmJ%2FyzG%2F4GH8Z3uX1olwMIj72DxmL%2BnR6%2Bsqi7ywBmwLTFbaXQPvyFzCI8jofiNbHxW80J3N3X2XNjE%2B%2F5P1KX5iTe0e5pi5f3rGIaH3Z%2FamXwNMSE56%2B4vfAJm6DU00q54MGGElCjjPNBb5YXq6sI9FmKdL&X-Amz-Signature=a9c41d7a494c56c93d8e3843c8c393f59bc3bcd7a543666b9085d7f05b114333&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXRGDDLN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfYeVP3pugOwKqghJ4vOgmzwX3BW4ZOBoFLOfViXgE6wIhAK3fYiqi0DmcEqasSXVzDaAFKRIEb2CuB7HfXxzhxatEKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6mvLWIxzgbtbZxCIq3APhx5fgBUQiJ9JxY10FQOAmd1v1qXJBhNIb3hw2wLPMoV4uYeFHcHWSImkzbwl%2FKkTdEZZRMX98Nsj%2FTjMPGN%2BxBziTWRNcF3gdviHCfySIt5w4IQ6v9EbBOVOGSbkmcUOi3fGm2Bdmvph7RDoqhi2qtk6YQi4rGCByTS9KG%2FAUJdFRLKodgCHb7pNyPQ5TRNfqWJcE39k%2BvBHv1LE%2BmKWNNFsDCRHy%2BiA69LQtbNNHaZgugogDmN7ybrkAg%2BVGWPfmHnFGOaFk1F4%2FBcrcmguyFBQiShyqx5IxJ6w1FdMaZgkZ5p5FIt9srApgsSgB6fHyVinkQOcg68LPQq57QDAeiUyCyPeoqQztzmv1OZfa55mEm7L%2Ba3z7o3pfFcM9mGEWZGqa%2BkaCehIqfCsM7DewRlmE9PjNJE2%2B4zIYgmHYdf%2Fu8UydhciI99qYjULRRGVqkfD5IjDaxe7neOiImJsEB8VnSdZWqcAihh4bIwp%2FJvuXsMNLV4gxfWWdEAK8M5uJZUaV1%2FWp2n%2FQN7NM7ijf%2Fj9nNPi5fuXId%2BzdtKgMF%2B%2FubQBTMWdOiygCqEgCQnIWpRkBnGjOMtgY7u1YWbMqv9DxjDcozqT1AymEuL44HttCNeNdnCPSzVM1EDCu5P%2B8BjqkAYxlcwd38sF0itxgYF616fUQCIhQbnXseBx%2Bw7vbx6xQ6dD2HEe1RJwxyftBbRj0HmJ%2FyzG%2F4GH8Z3uX1olwMIj72DxmL%2BnR6%2Bsqi7ywBmwLTFbaXQPvyFzCI8jofiNbHxW80J3N3X2XNjE%2B%2F5P1KX5iTe0e5pi5f3rGIaH3Z%2FamXwNMSE56%2B4vfAJm6DU00q54MGGElCjjPNBb5YXq6sI9FmKdL&X-Amz-Signature=738e9a64bc7408bc5e3c2a674d6fc1a67e62882b6bd41698510823af58264f9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5DNTZIK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4o09Gt3kY8pzUx6Wzdg0pZo477ABiOwNqRUgSPZ6EAiEA0E2mvb3NkFJDHkB%2FxJplodz2F5AQ%2B1mydRa3QucyrHMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNs%2BQki114E86TUSbSrcA9nevlIEVMNbpsEsln%2BCmPYLeLjoxV3KIg%2BEoqr1addz5oc%2BKuXEETomN6Bb98OhmJ%2BHsoybjaXghISPFmdc8UabFaJpJ%2FxtVX57IISLpuM5mEaEYFL5Rcu3kjsW%2FykU%2FxAMYwmETlPeBmjEFUnFbBJfG01zXWvNsQ5VoIoXotZJoP71XsEK5EK4FPsaSRtS3JGElXgNr6LO1Rw7%2Buk1x3gvvcqVE%2F%2BI92efUqJyum0Sftf4%2B5XsfrnntMwPXq3gFmdixmbHGssFGkratJ2rqxoawYs3mND8WnnN7EQSjHsdCEfoyMVdy24qYSCNHwAe4JDCJuHOPHNG8Gb%2BOy6f1WPzzCVceEJoPpu4ToVoicM9GGv4WhC3kpT5p6HcNj197i2hpAUi1DHlBPYcfmgQTMWDXTGzHXRWvNkbWd81VS1XfsV3rLBiQU9p%2Bahmi4gFLzPL1kqXJJXNY%2BMcG7QUp9VxmdB%2F40n6wPV0lUQxqvSzaY3063c2ik6ud39ZyEnOxfLZmcWvX0Hhx9rtKsIT2MXFdgJIU5xUqsgOF1xdXXr6%2F%2B1Z8IHlfD0sets7nfWYE0WSVDxY0u%2BhdLnp9y6UQWgTvtKR8Wc6tMml32GpYDBMok6qkXrXEU2Yf20KMI%2Fl%2F7wGOqUBGdcVkVm%2B90J1QnknoWhrnrsazVoA6DNV3kmiE%2F%2FGh5m62103G4oUYzfgUdGUWqo2pi1cmCQ7LNitTwsPCLwgjWN%2FGinlUKDLWaVIvRQuYtavA980V0wpuWK6xv6Vw1AXlhPvvODD5tAU3qEO67FUleY0tFsnXP9JM%2B%2BzvF%2BFRWyHiiJlQopE0SPl8kiAl2CcA7lspuUEni2hyob6GC1ptWe26ayN&X-Amz-Signature=4f86caa364ebe7efe8c447f4ae565741b6da451c20b88e7cabe8859abd7d24c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3YX2DT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6qjmie%2Fkrrdv2Ht15NT63V7fdBxSR88o%2FXZCErGZlnAiBEDdzsmFgEbQ7Q3b6cZqQvar1%2FqflETIhJfRHFNMakeyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZFCnC2KcVPsDOX7KtwDAJ8zuVlNXNJTvF%2FOMT8XJnMHwBkTDfZyBc2vu%2FTLO2%2BVToqg9rfOKmscN7J%2BXxCGi0g3FxTL3AU1zqAhHV6ivRhFhJHfVvkSKTcxJGkxf9yiguw8f4l7HXFBDs9b44rKR8GQ%2B2TzUtEDfZhQ5XvNAn0NozfJ%2B9BKiVXQV5oJZcj9tPIIQWooMjkj%2FHg3iyFhkMNLId%2B53dXf9JZD0PUOAjavSl8Fe9nYB2oO%2BMi9oEF6oOItoz6ZiGdCKRdQnsry%2FV5L%2F05q3qB9YtKO2unfb7rtIirh3oiWx7LZ7iksnUcXM7TN0kWa5t0gnKIbGPKPQCMrAQ1E2DbewM%2FIm4u7JXC8J3QvSCYxJyA7ac5aQVi0Ec4G4DLqcAdZ0JZaWev1U%2FkzIdGqgqfE2nKzDT%2FvIHoblG%2Ff%2BwCMFe7uHCcEcO1xhEbMhmMbIuqb%2FkIGHmv%2F8B9AZHLCLl01RTePj8zBV3JBUso%2F8HJuP1muEcr8LL%2FX4EXjAbd%2BqHp3sDcJdWStTHENQyI0AKk%2BT2UPkcAWTDWuBLU7r%2BqTy0vfjD28IMalUtZw95Pyg%2FvMCClfTrhxgZs%2FAF%2FzO6BU8cvv9qMn%2FnT1wA3S95p17sPi9L%2B2rz%2FZs4gNNnJLzC%2BDI8MwkOX%2FvAY6pgGqN3t28BakDu7n%2BZv1cDoYEC%2FOhoG6LyJ78HIQdbaBqPPCZU49z3a0VUaxDQA2c3kv9i79DOO6GlWBTtJxER9mmYXHTzIBjT%2FqQTzavwwJf9zjARHvesgNRjBSoOH1L8F%2F6Jh%2B2Y3XhgE%2FTrF3McudiRS178fCGeIDNOULJkox55TMRMrEh2yDirluu53vwvXHxsHQNccZsOBZWK%2FGfpejGe9pamrQ&X-Amz-Signature=71873fa534e01f4bbe35c6abd11e9a64bcd1b6fbbfbb012a9e51979547f1edd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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