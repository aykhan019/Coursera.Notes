

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=cf0f7062e28c98d6a911b26c6d1549ce61b587425ed23d9b90cd42ca41fb601f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=7907ac97a35657b16be87a5de7fc5cd62cfacf53c65d0ee2a52ed78d7abdccdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=b4e01d92cc41af05ced9c6593217c7f79e45bdef6f23304d8a28dea7c6eb8f91&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=63ca361d24d9fbac64ca81412fe078d6aacc4525935b5dff4e0389a6146bd8aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=388f5bc236f35de9ed362897f7257167be4a31171a98cd6c862fcaa06a7f8abe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=fcffa83756fe80586c4c82f8203a558fa35e3660e0b72331563f4ac14f5f6a0d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=8784156072b85878ac4205cd7ad5b30b491aeb1075086f67291ac44645e39bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=162442583424c0b2d1008cb3184e7e5281afd9f5a088912f4ad1bd4cac82d27d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=b587010d1d9a67fc12fff51db322e448a883c588cf6ffb98d6d122b82c495aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZLDWNZU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcugfv1b5qvMgsZw5wZ7hQGP8mHRdN0dZR9QPr%2BnMM0QIhAOKaNdjy%2BM6WSTwOc1eXKNg3OzB29fFe%2Fi%2BfUG%2BuDaOzKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaE5O1APrppaMJh08q3AOGj43bsr64rp6jb5H1X92Q4304MSq7nSHiRK8IeRfIQ7fVVJrIGlwSJ6T6K6ET3l1Lnd%2BZN0Kr45e5U6BxsGO6nH0e4TojfOXKPcrGi6NKQEueCv%2FOj7LXdsRUJ7W%2BMtagGZNb2BSgGIOvqEU4ZENzNh4fvpPAX6%2BRUHfc5RXy2CgukY%2FNDQIaE0dtxyGnuGaDRLkcpiTKFYQR9knBbClIyWJJo%2BU0uFjF0e%2BMXfLwBymRYcsNL1vxrr9Delzo6zg5Y%2Fj0afgiHX7%2B%2B6JqVuhj3FJ0Y043q309PlHQMAioSddM%2FP5uqGGj1u1xCEs0YsL2wVkIscmD1R326MzNeE87m7FKBq3r1ECrwF%2FToJXZOxHnFfHv7sDC1XZ8TtTR08j6fX%2BYEA8C261jy8DL87LZ%2FadSsWrUHYFVi8bM8fLS72ABJDUlJYCFWBWv6IfT6fLfPBW4Sx9MGcFVMyv9akC6feOit8%2BZZitqD3wkUodCjFeytX%2BDm%2FcwL984iSMNzDI5y1gd9nZ2YLYbcctUUeWnTWdmTBlleAsTrGZhLtF7qtldD7sV%2FRO86Y%2FFUqh6DugstybQ1G%2FcMVHEXrawJFY%2FVEEicY%2BqkSBFFqrUxPfa8WQFWzgLDXFRIuLE5TD4iu28BjqkAUaoPb2xI1ZdHTREhTwenby%2FC65T02ZKI3xNXfr1lOMbqkgEp%2BcmWwAdvwYAIECtp3I0By6OlIaD4MiFiZztZXqyxa4b9zPoQoh%2BmcKSH1F7j66GwVocQsJP%2BSBOVErDHYYE45W6aNADQXW585S9juVhT11RvF4E%2BZdrGkbjF828RQLeR9lET2BzUCrHUO21YnH40FbtBkzV4IhotP9h30iSGZUV&X-Amz-Signature=282a1d51efbb9817baca623707d76e8004d179343fb95b7a22fad62294507030&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZLDWNZU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcugfv1b5qvMgsZw5wZ7hQGP8mHRdN0dZR9QPr%2BnMM0QIhAOKaNdjy%2BM6WSTwOc1eXKNg3OzB29fFe%2Fi%2BfUG%2BuDaOzKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaE5O1APrppaMJh08q3AOGj43bsr64rp6jb5H1X92Q4304MSq7nSHiRK8IeRfIQ7fVVJrIGlwSJ6T6K6ET3l1Lnd%2BZN0Kr45e5U6BxsGO6nH0e4TojfOXKPcrGi6NKQEueCv%2FOj7LXdsRUJ7W%2BMtagGZNb2BSgGIOvqEU4ZENzNh4fvpPAX6%2BRUHfc5RXy2CgukY%2FNDQIaE0dtxyGnuGaDRLkcpiTKFYQR9knBbClIyWJJo%2BU0uFjF0e%2BMXfLwBymRYcsNL1vxrr9Delzo6zg5Y%2Fj0afgiHX7%2B%2B6JqVuhj3FJ0Y043q309PlHQMAioSddM%2FP5uqGGj1u1xCEs0YsL2wVkIscmD1R326MzNeE87m7FKBq3r1ECrwF%2FToJXZOxHnFfHv7sDC1XZ8TtTR08j6fX%2BYEA8C261jy8DL87LZ%2FadSsWrUHYFVi8bM8fLS72ABJDUlJYCFWBWv6IfT6fLfPBW4Sx9MGcFVMyv9akC6feOit8%2BZZitqD3wkUodCjFeytX%2BDm%2FcwL984iSMNzDI5y1gd9nZ2YLYbcctUUeWnTWdmTBlleAsTrGZhLtF7qtldD7sV%2FRO86Y%2FFUqh6DugstybQ1G%2FcMVHEXrawJFY%2FVEEicY%2BqkSBFFqrUxPfa8WQFWzgLDXFRIuLE5TD4iu28BjqkAUaoPb2xI1ZdHTREhTwenby%2FC65T02ZKI3xNXfr1lOMbqkgEp%2BcmWwAdvwYAIECtp3I0By6OlIaD4MiFiZztZXqyxa4b9zPoQoh%2BmcKSH1F7j66GwVocQsJP%2BSBOVErDHYYE45W6aNADQXW585S9juVhT11RvF4E%2BZdrGkbjF828RQLeR9lET2BzUCrHUO21YnH40FbtBkzV4IhotP9h30iSGZUV&X-Amz-Signature=256c873926ec888c1a8ba8960cca6d4f03813e896643ebccb58cb31a63433053&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZLDWNZU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcugfv1b5qvMgsZw5wZ7hQGP8mHRdN0dZR9QPr%2BnMM0QIhAOKaNdjy%2BM6WSTwOc1eXKNg3OzB29fFe%2Fi%2BfUG%2BuDaOzKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaE5O1APrppaMJh08q3AOGj43bsr64rp6jb5H1X92Q4304MSq7nSHiRK8IeRfIQ7fVVJrIGlwSJ6T6K6ET3l1Lnd%2BZN0Kr45e5U6BxsGO6nH0e4TojfOXKPcrGi6NKQEueCv%2FOj7LXdsRUJ7W%2BMtagGZNb2BSgGIOvqEU4ZENzNh4fvpPAX6%2BRUHfc5RXy2CgukY%2FNDQIaE0dtxyGnuGaDRLkcpiTKFYQR9knBbClIyWJJo%2BU0uFjF0e%2BMXfLwBymRYcsNL1vxrr9Delzo6zg5Y%2Fj0afgiHX7%2B%2B6JqVuhj3FJ0Y043q309PlHQMAioSddM%2FP5uqGGj1u1xCEs0YsL2wVkIscmD1R326MzNeE87m7FKBq3r1ECrwF%2FToJXZOxHnFfHv7sDC1XZ8TtTR08j6fX%2BYEA8C261jy8DL87LZ%2FadSsWrUHYFVi8bM8fLS72ABJDUlJYCFWBWv6IfT6fLfPBW4Sx9MGcFVMyv9akC6feOit8%2BZZitqD3wkUodCjFeytX%2BDm%2FcwL984iSMNzDI5y1gd9nZ2YLYbcctUUeWnTWdmTBlleAsTrGZhLtF7qtldD7sV%2FRO86Y%2FFUqh6DugstybQ1G%2FcMVHEXrawJFY%2FVEEicY%2BqkSBFFqrUxPfa8WQFWzgLDXFRIuLE5TD4iu28BjqkAUaoPb2xI1ZdHTREhTwenby%2FC65T02ZKI3xNXfr1lOMbqkgEp%2BcmWwAdvwYAIECtp3I0By6OlIaD4MiFiZztZXqyxa4b9zPoQoh%2BmcKSH1F7j66GwVocQsJP%2BSBOVErDHYYE45W6aNADQXW585S9juVhT11RvF4E%2BZdrGkbjF828RQLeR9lET2BzUCrHUO21YnH40FbtBkzV4IhotP9h30iSGZUV&X-Amz-Signature=9b31489a9f99fa7ab108476ec596d9f815e93d881d67325002e62be288267a26&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=d8fa56fa11efb260346a4627a70ded502b1ee9d68e4ab75711cfaae5c1370873&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=d10f0f90bb8937265c582ae195afd62e0d337e028696467d900c2f33a2ed03d9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=2aefb060d736f0f110a6966b29228f27db149e41055679d8bf85b211b335ee11&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=fdc375026410b72d429f9a6e7d337aa0c3ed7daed2fa97508525d73f11016367&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=81dd5613184d9eb9668db97b905f449f9b16fa90acb1861d63e4357e2f06420b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB2FVONQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcGgHvKlc3q10mPQg1lTjf1cRtFlQrnzdoUXSMy9drDgIhAKuNO0DvxZfYe6Ko5ZJS2jLSRLon6PNyjYptwb6SkSFgKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9A%2F2NRPYobVKgymYq3ANLQN6K%2F3oo4cupMFJjmIvgy0QfmGrk4oTEcPiEKpV4qxUlBfQcXXUPX1sErVMZIZ3WrdD%2B78xnuZkYMw0hSKxH7tAWvCtN44KWdhJZYQVOkENfYpJS3jWfmiyJc8s3Ybf3%2FYKy9Q%2BWF07FL7SUEaDGNxhKlnMn97%2FqtenJqyp5ySEmcdC%2BHxpd2RJpE%2BZZ95AYfoRhWs4Hg%2FpyVON%2FBGwKMdKFhcn89ELtKdMDcbK2ncfVe%2FpaqUSpdiJftOvANjwy0L8xe0atyTGewZtIcvlIyCZhItSYeCyR2R2UrFeXyhFmsAOghqZZMF2%2B2t4Y%2B3NaSjdRBV4xIyXftZh4QFS1Nrj9NLChlrHkECl4n%2FUXp6eT%2Bp%2FiXc9BTkmydnv9gF8n35GuGy7BAI3onGzhuGVnCFZqqRJ6Fy6Q68FG%2B00u8M%2BamdZKMHwZlhY6A%2FuJzyHoda1Ob086DYtCHDGjjZWL%2FEJFTbfyUVF%2FEBEir5wPx%2FCqoMK9bLncx2yt9SI2C%2BJO1TyaE1dtMq5iFzTfXkspRZw%2FUn1bLHek3aPsQMPrzAkc13j7nuwsyT3Tnu1tf5zkeAxqqn1kLy2iqDHqcF27jmhGn5kfdBrvzO1xM%2BdGLAPZR%2BKaELUbjnuSOzC9iu28BjqkAYojvlblW5sXqubVKnI2KAmbWoxkjdJ1J8vmbxHnEdmaJUq%2BdD8sutmgvnoX87vjs68jn4lF3W6Lta7QLFI801uBHH%2FLBN8Q9Tt6Wq99mUDmRhI%2BZ222lCbKP9JjQeaISKA7CDY70rGDS84BU93kW%2F%2B9%2B199Wi07GF8fLsJDXwIQdyhqPOLz5kWPKIx0pBnkMrNJwYJ2bZof9Dnm1Gfv7vjS0QtC&X-Amz-Signature=10c61bb494c3452ed4634379296138fff774bf02fcc13c6e00012e82a2c02a3e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBJYSDBO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYjGYB9wFsDktstfphVWCPiR7N5mwd1ayhYzWMxiQ%2FYAiAx%2FmmlJXHsjVJNwPuJ3MvcAcwaWc3GHVhlTFeDaUrbvCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT%2FWMs7cfbZ3XUNMAKtwD2pmOAkl0SYtjWIE0WoC8kfucLJUhXbdKxt3eKC1LUwAEwKPzJLK32FNVguW%2Fl5zBiSYG28IjEpTNJk7XtGQan%2F1k05YtNLCKta2qUOL2GXzK6NJVhNl56Gq0LhjFI8ajV4nyb2ry3qhnlqI3FtYYgEMk6%2FcsvczTnKnxankFz3LwYWXIbUXlAmcfSUprzlOER0%2FLKwHyaKrDiY6f69E5rv%2FRG9N8AaOqjE226K8lbcldn%2Bwu%2FxFAaI%2BB1xO6FTnttuhE0eboVX8gXg5utOQL2QE0asn1D29b84Ry7wPVm5mRXpiQXBaahNQ0HQ1oOj2wTSnFC9ZqJl7FAomZI1vG4IEKZJJJx2pPRct5iVKtckY4Wb12rWBi%2FDSzqmp3uIprCyAtw2NRAK5yqiZdUpEcxhtSTtladPFPowl%2FSHsLfTmkw%2FLAVxljHtfTde7grXjHI1EPKvcg8GHSXw17hkKw1xHYC1O66UhEyWRurk6mNPSHK6kerk0XdsOXBLH3AObPv6thT%2FniKu6PghxQsxg44hEQzldCcgtHzZ8B04283WN8PHwcvPfz%2FGgK6VVmnwVqYwJqgNERqFz0dqdnNbJ9s5Pl5rkhttqaX8LQUI6bKDM0xu1tq8%2FWrMvJO0kwt4rtvAY6pgGA%2F6rqZ1S4n2BLhZUnS846GbGXQu5Ozi4urVWUFTYkOl2CZU5nax0KiEPTIDEcEMt4nN84V3VbJakrqpjLYcfBeiZRq01t1cwBWl9kmZtv11%2FO7T4QEoSPSXxurrUnTTR8nQZ5H%2BV3VlLy400YZjz4F1029w%2BEgWqCNWRMTA9KfI0%2BOGN%2F7DMjnXCCQXL2qVuQLaLt8%2BnlQVhqUOdpYnj5%2F%2B0WG9Z8&X-Amz-Signature=851b2467168670be16cebc76a146c610f3b7b4941f957594264e0f3d2440a943&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBJYSDBO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYjGYB9wFsDktstfphVWCPiR7N5mwd1ayhYzWMxiQ%2FYAiAx%2FmmlJXHsjVJNwPuJ3MvcAcwaWc3GHVhlTFeDaUrbvCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT%2FWMs7cfbZ3XUNMAKtwD2pmOAkl0SYtjWIE0WoC8kfucLJUhXbdKxt3eKC1LUwAEwKPzJLK32FNVguW%2Fl5zBiSYG28IjEpTNJk7XtGQan%2F1k05YtNLCKta2qUOL2GXzK6NJVhNl56Gq0LhjFI8ajV4nyb2ry3qhnlqI3FtYYgEMk6%2FcsvczTnKnxankFz3LwYWXIbUXlAmcfSUprzlOER0%2FLKwHyaKrDiY6f69E5rv%2FRG9N8AaOqjE226K8lbcldn%2Bwu%2FxFAaI%2BB1xO6FTnttuhE0eboVX8gXg5utOQL2QE0asn1D29b84Ry7wPVm5mRXpiQXBaahNQ0HQ1oOj2wTSnFC9ZqJl7FAomZI1vG4IEKZJJJx2pPRct5iVKtckY4Wb12rWBi%2FDSzqmp3uIprCyAtw2NRAK5yqiZdUpEcxhtSTtladPFPowl%2FSHsLfTmkw%2FLAVxljHtfTde7grXjHI1EPKvcg8GHSXw17hkKw1xHYC1O66UhEyWRurk6mNPSHK6kerk0XdsOXBLH3AObPv6thT%2FniKu6PghxQsxg44hEQzldCcgtHzZ8B04283WN8PHwcvPfz%2FGgK6VVmnwVqYwJqgNERqFz0dqdnNbJ9s5Pl5rkhttqaX8LQUI6bKDM0xu1tq8%2FWrMvJO0kwt4rtvAY6pgGA%2F6rqZ1S4n2BLhZUnS846GbGXQu5Ozi4urVWUFTYkOl2CZU5nax0KiEPTIDEcEMt4nN84V3VbJakrqpjLYcfBeiZRq01t1cwBWl9kmZtv11%2FO7T4QEoSPSXxurrUnTTR8nQZ5H%2BV3VlLy400YZjz4F1029w%2BEgWqCNWRMTA9KfI0%2BOGN%2F7DMjnXCCQXL2qVuQLaLt8%2BnlQVhqUOdpYnj5%2F%2B0WG9Z8&X-Amz-Signature=7bcc9d0610d2951e34c7d80dfc17d997ede8ce617e887ed6593a40ca6eddd58a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663APONAT6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjT6l2mIlkP13jY4fN3lJEJ8E02hg%2FBeKYnLhWnCRHiQIgHOZ7uAIZTtmmhP7nd6PSK6sMNr7%2F1u%2F7yYwL%2F%2Byp6HEqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBKqT%2FQveMfEpvW3SyrcA6UFIw8tFQfT5TTlAfWPjytj0nvePBhWaqdhPddQR%2B4cQt%2B%2BVNuu9ttZqC1yMzdnWHm%2BmXSjNxPETFefOxgWJns5hTgtdWyCuyDOl69YgLn13L9IcMSaHaXPb1NmO4WSt9uuMIedyeIAVwUcaXwrfmA6WBk6SZSb7kOk0qSou1MbB7recHiHXkCRe7ab4AieX5be29yMjPFS4z9EFGbsshZjub5Yqwj8RLtGrozAnKT22q9p03tneoiy4ueCu2zOVY0WjtXZ5%2BCPuo549RqkyzAmDKF1xzhT04NYmq03ty5kMcZqlaZpR2NO8rzM8Y3H5DxyRZtkhfepPPueZ6nyX5G40GOkn0K%2BP8Fx%2F2wrlbJqgnSBoMcVpOmJU8LHHS2alDJyVRHz%2BGaXN4a%2FLK6t9MqPzihsukNGh%2FCNO%2F0lldRPwnpCv5L%2B7M5V82074eQ%2FInHRkfxkKgUPUlYE%2FVvQsg4NdScGgpvcqbMUtfPvmTHyo7tPwQhrCuZpcHvjvOCxrRJEgVftOvvjbPPpG33uaB1yeFGLYs0XySyYNGcSkB8jg8mtY0M%2FQ6wMexeqthCRSQ9ei6urU9RK5ceAXO7vZiWvJjNuflNH9riP7INMxi3fB34KM6t843FPViFEMPmK7bwGOqUBIw0jmACfL7LqDlPUCgQJx1L0HUdL%2FaZ%2FM1PeyJgAC3RQjE5%2Bx7yVl890l3KWOj3r1kzkIJpRXXlAr9Ch9oFT42lxlV58mgnEEzKYgr3JLdQqIebLO04AvfNZuqLwF2%2BbwooeIdm0x4XCgmmJm36%2B38km3F6LxsnoFuctgwhSj7CDnDqMvgXXNDy3dMSqmd90Da8Mp8qqC0jBGAQa%2Fayfh%2BsLZAAa&X-Amz-Signature=a77c8bb58a875b489125da6eac30de27b7d6b7d9225cd3d0ea46953d8c06f15c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHG7Q6TI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfXrzcQ%2BOpquxFHJYKWiuZnOPVPreO3dh8LY2O%2FPH5kAiB32e8y%2BqtQs9OWW4WTJIWr7H87ea8LqeRFAETOtE454CqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRL0ezdgED0ZMTTE%2FKtwDcd1WoHM8L31s1mrPaIoqJDnEQ5LfeNs1Ccj%2FjLziXPSSTZfvit6ZP4RKDmv8DGhQhhUXUfueLR0FeMR05%2Fmq6spjWiRVmuXAlENSuuRM0jSOovj7LQ0r9r2oYfnSLIF5gOzqrIcxWtxKtk1ECSFXVC2CfEOPSsuuftxny93kLMaMJ21MnojhrurEpbdn4qluI0RdocgdDwxy8fVh06dfl7zqL%2F9jHvCgM9SJh7842NeV4nCFNAx5nPEWsAhj6sYKWxWYjKPctQNq9IPaZh4iHYWn2u1kS%2B2rZQaRNMAPypyut4lnawnNyinKKA%2FoP2zLWR5X07W%2FpSYP4ZyF%2BuQSUUMZYvuYJAIua3zEcL25PxH7xyY5UZ%2FSl6zfkIh2TuArDviLQazf6XaesvmGMBgPo9XaRMoUN%2B6PbMnGaanLi5v2l5ugs6ziMZOumRWWZxJ9ymLdyaF1lp8HqNmb2bS%2FZFhHvLmhkLOzxL7KXnH0rjJdntMI6LaETY5usOVZvoQ5KYh62PTz6Xz0uj8cXwI9kDbXxGLrm4G3XS4td3s7z113FsRoI0KbVppyCTQvR65%2BAPHVjQRmtPYXQhBQByG%2BmTqJxoUjzOT5skX%2Bhi%2BN6NMQESnpTEvJNB5CMq4w04vtvAY6pgHx8NnMOCI%2B7HT%2B7cmh%2FOG4tczFL7GGCkex%2Bh%2FYk84YNfX1Z2x0T6UgD396RlEKxfIg5njOtGM74kquULx1RT%2FWje8ejQfVbqdKWdUhjI9qY8Gc4V%2FyNFlRbivoC%2FNk9Ral0JotyIv1uxfaBxnnUFNJEWm9PWDqUgLW4FU%2BTB5eHKotSO%2F8b1AtBKSu%2BOkRXKpCaQ6XI4uRX%2B8oVcseSO%2BA6vKMSEo3&X-Amz-Signature=87ed23b529eaab686c1c9d82a113b093cdf7c03e5fd687a91f06a844ffa63515&X-Amz-SignedHeaders=host&x-id=GetObject)
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