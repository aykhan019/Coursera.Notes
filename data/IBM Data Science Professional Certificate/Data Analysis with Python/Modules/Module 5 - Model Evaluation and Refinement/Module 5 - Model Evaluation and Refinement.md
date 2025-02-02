

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=5eee368d86e1bca472cfbdc479800ceb0ffb8356052b084821aeb329d32dfa0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=3d6763bef5a4df82026985aca8fef03f6a379870bbdd7713fd2d5d551bc581b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=9ce4eb9311fdabe053e7dbe53347c0eecde63266b68359fbd932aee120fd7c46&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=2c76c3bb5f0e06ae46f2c597667aeffafa493dd0a9643f56125002aaa6d40c16&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=48224787f34930246f6f1c10a6382144f2dd58021b441ec0a9263b69fb096d3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=a1760abcfe7b6fa6d83f85038bfcb60d8eb4ab5ea1199e965fa0c32392f020dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=fc7eb046eabd8da2f95862c52feb75dcc4f550e78f372d69f1530a6e8cf7a34b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=ddd21f7bbf4b0931cb2dd18802078e168c438b0adc7874a3f865abc69d50abbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=d059e0c4f9f074ca1ba846de9939b15af71d07066cfba0a95a37f1e2ea422ef2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5O3JVTK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDej0DI9R0WPVgXDqeHXJn6XVHQFZFosUWCgplxctlnNQIgKFRPjMEQRLEIia%2Bj8Nz0vlKG%2BnepyIQq8cuM7F8kRuUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGua4FUa%2FQ%2BTfk2kSyrcA79oL7BpXkne8hWlruXdggvS50z%2FG1htleYV5qGiG%2BfVYtoTguQoiUCrDamEHFfOHYjOy%2FggnctyLCduMthweLK6AeAfLvqbz1L%2Fowl1CDKTVYnC5CeLbi%2BHCWirkyJjc%2FGeQV33t3%2BUgo%2Bd3fPiZnARG1P%2BEPvl2iSdIkUml62TdoTdnrRdGvk%2FIHBmrsnjg9MC9Qp9apxPBNQak2PiwnKhv3rHolrzpQEzIlGm%2BiXqBhUESBA2yBlzRFtAYsz41nFIBCHifEUSEvLiunxULQfJfbdmoAl%2F4eVsDjxb%2BisSGt3s94LKJx8XYpDGKAx9WUocqkDZ4sgqsFWcOaJtHAGeq1UXlLBeR4CddnZHhNmH8%2FDTKL0Twy6uVWSMrQZc3O74RTFp0MCk7DcCwqWsDgUDR1aMaQzxyrq67a2x4Ll1AGjB7XF4aA%2FgSxngrd4%2BWxGh85OMRA41Dxs5fmf0D3IeVrjJBn3qgm9BskX%2FGPqX2Uq%2FuTlJn51SATHWbKbBCXjBLVBZ6NmCuoPPEzhQkz54Mf5y9pp76WE8JY%2BHMOt2WyVcns8jE0dHdoYa52zkqLoJfb2dYDypFsmWZwxvz7LwTwb9cKRgPj7fg7B%2FVFCgMQL3R%2BGErWclqf9jMLzk%2FrwGOqUBTxVfpCPVx60dSGyOFfRtbQZD6XYa8TkXAbJyOr3pljlrUdojpzmtiR28x1FbqKTtDLxi3xjMWnWaXrYYHC5%2FmZGm49YNaQ4YK5SilxZ38ahdO8STMpElvotXf50GQP5rTxUsqIMPm6aLot9oeN4skIcUCHqDMckPvNljR8BZ4mmeoDp00yHl8YhIxFTXK4roq0jR1SEi4%2FzbWPjDoxVPC9BHsXO5&X-Amz-Signature=8db2c6836c2a20beeaf42fb7c2bb2200522bf70a047fbeb35797ddb1d2c4f01b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5O3JVTK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDej0DI9R0WPVgXDqeHXJn6XVHQFZFosUWCgplxctlnNQIgKFRPjMEQRLEIia%2Bj8Nz0vlKG%2BnepyIQq8cuM7F8kRuUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGua4FUa%2FQ%2BTfk2kSyrcA79oL7BpXkne8hWlruXdggvS50z%2FG1htleYV5qGiG%2BfVYtoTguQoiUCrDamEHFfOHYjOy%2FggnctyLCduMthweLK6AeAfLvqbz1L%2Fowl1CDKTVYnC5CeLbi%2BHCWirkyJjc%2FGeQV33t3%2BUgo%2Bd3fPiZnARG1P%2BEPvl2iSdIkUml62TdoTdnrRdGvk%2FIHBmrsnjg9MC9Qp9apxPBNQak2PiwnKhv3rHolrzpQEzIlGm%2BiXqBhUESBA2yBlzRFtAYsz41nFIBCHifEUSEvLiunxULQfJfbdmoAl%2F4eVsDjxb%2BisSGt3s94LKJx8XYpDGKAx9WUocqkDZ4sgqsFWcOaJtHAGeq1UXlLBeR4CddnZHhNmH8%2FDTKL0Twy6uVWSMrQZc3O74RTFp0MCk7DcCwqWsDgUDR1aMaQzxyrq67a2x4Ll1AGjB7XF4aA%2FgSxngrd4%2BWxGh85OMRA41Dxs5fmf0D3IeVrjJBn3qgm9BskX%2FGPqX2Uq%2FuTlJn51SATHWbKbBCXjBLVBZ6NmCuoPPEzhQkz54Mf5y9pp76WE8JY%2BHMOt2WyVcns8jE0dHdoYa52zkqLoJfb2dYDypFsmWZwxvz7LwTwb9cKRgPj7fg7B%2FVFCgMQL3R%2BGErWclqf9jMLzk%2FrwGOqUBTxVfpCPVx60dSGyOFfRtbQZD6XYa8TkXAbJyOr3pljlrUdojpzmtiR28x1FbqKTtDLxi3xjMWnWaXrYYHC5%2FmZGm49YNaQ4YK5SilxZ38ahdO8STMpElvotXf50GQP5rTxUsqIMPm6aLot9oeN4skIcUCHqDMckPvNljR8BZ4mmeoDp00yHl8YhIxFTXK4roq0jR1SEi4%2FzbWPjDoxVPC9BHsXO5&X-Amz-Signature=b9b73ab657c3808bd6c652753369a3fb7c80b6ea2e1d33f046f96912c3959afd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5O3JVTK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDej0DI9R0WPVgXDqeHXJn6XVHQFZFosUWCgplxctlnNQIgKFRPjMEQRLEIia%2Bj8Nz0vlKG%2BnepyIQq8cuM7F8kRuUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGua4FUa%2FQ%2BTfk2kSyrcA79oL7BpXkne8hWlruXdggvS50z%2FG1htleYV5qGiG%2BfVYtoTguQoiUCrDamEHFfOHYjOy%2FggnctyLCduMthweLK6AeAfLvqbz1L%2Fowl1CDKTVYnC5CeLbi%2BHCWirkyJjc%2FGeQV33t3%2BUgo%2Bd3fPiZnARG1P%2BEPvl2iSdIkUml62TdoTdnrRdGvk%2FIHBmrsnjg9MC9Qp9apxPBNQak2PiwnKhv3rHolrzpQEzIlGm%2BiXqBhUESBA2yBlzRFtAYsz41nFIBCHifEUSEvLiunxULQfJfbdmoAl%2F4eVsDjxb%2BisSGt3s94LKJx8XYpDGKAx9WUocqkDZ4sgqsFWcOaJtHAGeq1UXlLBeR4CddnZHhNmH8%2FDTKL0Twy6uVWSMrQZc3O74RTFp0MCk7DcCwqWsDgUDR1aMaQzxyrq67a2x4Ll1AGjB7XF4aA%2FgSxngrd4%2BWxGh85OMRA41Dxs5fmf0D3IeVrjJBn3qgm9BskX%2FGPqX2Uq%2FuTlJn51SATHWbKbBCXjBLVBZ6NmCuoPPEzhQkz54Mf5y9pp76WE8JY%2BHMOt2WyVcns8jE0dHdoYa52zkqLoJfb2dYDypFsmWZwxvz7LwTwb9cKRgPj7fg7B%2FVFCgMQL3R%2BGErWclqf9jMLzk%2FrwGOqUBTxVfpCPVx60dSGyOFfRtbQZD6XYa8TkXAbJyOr3pljlrUdojpzmtiR28x1FbqKTtDLxi3xjMWnWaXrYYHC5%2FmZGm49YNaQ4YK5SilxZ38ahdO8STMpElvotXf50GQP5rTxUsqIMPm6aLot9oeN4skIcUCHqDMckPvNljR8BZ4mmeoDp00yHl8YhIxFTXK4roq0jR1SEi4%2FzbWPjDoxVPC9BHsXO5&X-Amz-Signature=74082355ac74af3073c4448da66ee70add527275accddf0af04d165ac26fe39d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=b8afed3ac9f6d9ecd4c96ed9d0357204eda76ce825bfa21458165993af2a8621&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=45e0161eeebdfbd71dbe00114aabb3ff46f68985bfaa934167629737b5e1251d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=50fa5f7e64a8bd1e02edf1e85cab7d9ca5b08b736c5125ae6c3a0a7491b7278b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=d7c359293c27d9b91ffe85ad19d451d00a43e48905c7f59fd001238a40d518b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=3fc64137dc1706465de62a41358459313aa4ce22979b952f5b1e2992174fd0a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPRQIZ2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHn3O8GG0zqvgJb1RMtfJufaEUDDO236l4lqDHgBCWNEAiEAvfr8DqXzdFqxnMsWUjE1LjX0oohXQ5hkUKkyUux2w3AqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2B3PFPgfDtvmJhi%2BircA%2BR8jcIihZL350UFuFDBlB4VOyLB4AfGvdZN8T7zdKcKwSwu0N4IBgboPEL1shpBxcvw6eOKdPix8zTuaIOHc1ZF1%2Ba46dJ21oPu2gbdKl67jW246eqXFA6QettA7E6syMcZWRY4XlqnfRgXyulI9WsFd3zPaY2BUlfI%2FVA3sAmY%2FUB0g9hYYJJ5%2F27HyP38k0Gz0hiDPnb28DRJNEGdt3Vu%2FRdRuvmCovW2RSIa45NA4h3sSLt9KpQEcfCRTMWSh6toLHt7hlyxAVsJ0xEwbFEJI3eguCZ6BL0%2FhKeEu4NTbqDzDzfc3toWUknDbj%2BwA7%2Fhk3ByOdRye47%2FaYhzDlEUsUthIC7n3d2tjQ0YiqjYfOsEpAltHilSzJ3CxHL%2BlJnxSiW%2FetEjE55yltyyFByov5zOO3zx9hfuj0t%2BKDUO0AStqWI6ELQFxkc75etMr5K4NCMYPomscGRp7nZWIVSSjyfql9OVobbDmg%2FjPfEPNbEb2aOg2YyeZcTxHEDfZWDCi%2FUxVFF%2Fs7pYesO9RD1v6ZlyNRwvxwhdHGVK2JrWlkPO98M51SqG7OaM%2F26XuvYnHyG3s2dBpCgOoAvbwy%2BzdPfHaNRi0Rebw5mgZSlVp9VWsC6SCSjGoObQMNDd%2FrwGOqUBem%2FzdNQ0VmgKKf6etnth%2FVRiBAfd3orBBv6ybGOfgjzkCNHczeIw%2FEH%2BXnvb%2FB9ql6H51gU37jMuWw%2F0lLUAsszK%2B5xtuAXOqODrFppHM0zYMzPSsulBPKqYg5G%2BmppBLC%2FMU%2Bgjx1xBGoueExoY0D1ZPs5gHbwq%2BaY%2FXvocA7pEmgCDkD2vUNdeBEzSMKAe8OOY%2Bd1D%2B8ZOomJLaMZr5oq31W0h&X-Amz-Signature=e833d57a099d4dff30abbeeea73347bc0c1df5d54917258007385c48fb1b80f2&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3C6T44B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7RiOqVyIYe5yrsv7bAoSOqMycRt1xbsWOB0SzXkjmjwIgHShEhu2YMM%2BIqqVvn5H8JrFOAenOuGiIgHN%2BGGNw67gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvApkXNlHcC9NlzSircA7p8PNIuUGUzcFjFezp3wzrd%2FijPQUTxpF%2BAH88df2jG5eMJGslPrp9g4nEvm6n49I4mkqJyooN00l57TTf7b36ZvHbL7dKFlNeEQ2hehV2FSv%2FsgMBxnDTiqq6gxDG%2F%2BUreIApteGWjCz%2BZDzS%2BY3ssUrsRJ9k2v2CxByAy6IXXaN7zKUEv%2FUcv1CNGRQWoLp74JTTYasEYoCphpsZbwNzeudjKrzLPkDwtSUDL1drja%2BynLi1Pq4zwl5f6YYhO2vWmdyp%2B6NyoKCNRyfQrN9wlJM23q1Vt01euuGvOjcNq6Ao6hcGGfD6wqvg4s%2BKED1q3%2Fwu08DCh3YpzstIv7oP%2FuPzRV5Tw7OBe3mLk0cA7jjb2ZWSs7lLZq9kjgI6AEly%2FUxYo6qw8U9sM77Zvx6sRBOf67NgT2AMkaPXMPtAeN3slB7YeMll%2BpAdFMivgkeMTdY5GpP9XmZbmc0V4gvmYXcwpYbezxH1UN2%2BVXv2uJudQt0NB0o%2BVMV6PCPEQ%2BThv26KmIntm2ePTTZaW%2FvE8ClkrCP3SMIXBqcn5tV%2BRQz0GJ6Y2in37kjmiHUP1RGKwCWz23mXW%2BNUxketv0Hdc3KLt8vSdH80OTZjuj%2B6lE8cZaVWlI5a54F3jMMfb%2FrwGOqUBbzafDuu36mIwNiCHeqDXWmUN0ib6DnLCEvq4F%2FNYAOWrQ9Pk2j8yP8tCXx4V%2Fe8vKB5u4aBmYqEYUM9C4THrybtLXEaYkkNjvQ7YtzhVURK4dw1GV2pZxpJxPQOiDzYbvFZ4GnGYzlq1qon5%2BvHpq%2BTlHuyS%2BJr%2FduFukXpTCwapUiMmVw9l8KYrK43VAIVs1gZ6mC6z270XDUtSB%2FrAQA4NJoGP&X-Amz-Signature=35bdc886a69dfeb1827d46492a4f9fb335fb6ecda27009a749b86785ff7fcfdf&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3C6T44B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7RiOqVyIYe5yrsv7bAoSOqMycRt1xbsWOB0SzXkjmjwIgHShEhu2YMM%2BIqqVvn5H8JrFOAenOuGiIgHN%2BGGNw67gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvApkXNlHcC9NlzSircA7p8PNIuUGUzcFjFezp3wzrd%2FijPQUTxpF%2BAH88df2jG5eMJGslPrp9g4nEvm6n49I4mkqJyooN00l57TTf7b36ZvHbL7dKFlNeEQ2hehV2FSv%2FsgMBxnDTiqq6gxDG%2F%2BUreIApteGWjCz%2BZDzS%2BY3ssUrsRJ9k2v2CxByAy6IXXaN7zKUEv%2FUcv1CNGRQWoLp74JTTYasEYoCphpsZbwNzeudjKrzLPkDwtSUDL1drja%2BynLi1Pq4zwl5f6YYhO2vWmdyp%2B6NyoKCNRyfQrN9wlJM23q1Vt01euuGvOjcNq6Ao6hcGGfD6wqvg4s%2BKED1q3%2Fwu08DCh3YpzstIv7oP%2FuPzRV5Tw7OBe3mLk0cA7jjb2ZWSs7lLZq9kjgI6AEly%2FUxYo6qw8U9sM77Zvx6sRBOf67NgT2AMkaPXMPtAeN3slB7YeMll%2BpAdFMivgkeMTdY5GpP9XmZbmc0V4gvmYXcwpYbezxH1UN2%2BVXv2uJudQt0NB0o%2BVMV6PCPEQ%2BThv26KmIntm2ePTTZaW%2FvE8ClkrCP3SMIXBqcn5tV%2BRQz0GJ6Y2in37kjmiHUP1RGKwCWz23mXW%2BNUxketv0Hdc3KLt8vSdH80OTZjuj%2B6lE8cZaVWlI5a54F3jMMfb%2FrwGOqUBbzafDuu36mIwNiCHeqDXWmUN0ib6DnLCEvq4F%2FNYAOWrQ9Pk2j8yP8tCXx4V%2Fe8vKB5u4aBmYqEYUM9C4THrybtLXEaYkkNjvQ7YtzhVURK4dw1GV2pZxpJxPQOiDzYbvFZ4GnGYzlq1qon5%2BvHpq%2BTlHuyS%2BJr%2FduFukXpTCwapUiMmVw9l8KYrK43VAIVs1gZ6mC6z270XDUtSB%2FrAQA4NJoGP&X-Amz-Signature=c92d1948fad57dc9b6ba6856201f02b5d0320d4452e67bba29cbe469048f4e79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EGSEFP3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6sMscTJYI8f9hTEiRdoGMZAHD4MrdKkg%2BFAiXSh2H8AiB9LV%2Fpmh8VsnKKHE3TLIxCf4a9zw2ZPdNtU1xuVcPjzCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTh6eiKEOFiJAwpBAKtwDrwFhzvHAFz%2B62BzY%2Br2RK5BFlsaJ4Em36Frk89i9YIm7WlTX%2FKJIeQHoFUUFZqY8ozo8A%2FzMkvUgxuRgmlyxVMUu1l%2Bs9r4yQXKoXbfnWcJ5B8xLLkoiObaUvv7%2BP979vT15KJT%2F%2F%2B8LuftQpkR5uRz651f%2BAPZPJyzXfc7i8vXbpbY8KpOARmAr24Nx8t42HmiahAWPWA85Zr8QdKhrxkkOXzeBCnd2OITiGFAjdky8RpDq%2B5eTl1ziy9pzOwdzMuthWYyeLLCCwb9Hc6eT%2Fd5ILmqb9fBo%2FHrHMHa9YB5zw3PLGKp7yjPV4N%2FBgtxyPaKAsplUoxnEkw4zH2FLryUHRPZCoIV%2FJm5gPEwLHcQZ%2F1g3S%2BPPQfJ3y77Z7IVKKsoxllwVLQof3v3QOEWpY3XA4pHN5diXUXNh0LegcptatKYwZOxmKCMk3%2BEwRdm7Aw3pY6hG9QT8IA3iTUs1WTYF3kzOupnc4F26jj0KnbyU3PIeRcIOn%2FADRXCkiQpBHM4bdpGui2v32NTESgl9v%2FGWpRWFACc11Ps886TZpFL%2B7gUcklQ376KBj%2F%2F7yoDe7WLMdLO9fA7XpkFPQx%2FSVBAocTuGlbGM%2B2iwAkOIHvTNtRWOL%2BGXBOmAHYkwx9v%2BvAY6pgG0fwZYq%2FPnwJgl6kTAPY%2FOarCaH8fBYMHQQ%2F4%2BTg7sAboWjlcP4yxZzudFUdbyUMSAUihEVPWV%2FZeO4%2Bh07jVDZm3bcuWSVPXhSsA4iFF6bomcI3GFo%2FXrnwEmWB%2F4m47WobQAUcq3qsWNSoWsheOzFxpA8Ideo2UaOLhqlp3Ysu%2Bk3yoZQKNCo0H09Sm8p1VGdJfRVUe68amc4thNcVTM%2FxOysTzK&X-Amz-Signature=871861e0dab0cc8d8d96a588dd5ef88445727309b3507090f15a0ce1cf65a768&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYW6Q4D4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJmSbmJga4yCicGEFLcz9AfF7dPQJAk%2BDeccEtTiqHUwIgK%2FCWo%2FW6rYor9L0C7%2BS1s7Kuh8Ka134fFc9NnT1X3oEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FUEF5z5IrATi5lDCrcA%2BOrDgbYepiikxrWzxYOTGncAC2GWok9ZMJfvhN8YXbtvhrXB%2F8Jd6NVSJ9rOHT4Kvlg86ICQ7VzTCspivz0h2ZzDIT2eOP3H5bVtKaTrMgoGaiKpeCkR3qnZGW11Gur7xSmuA%2FwxDEuGLbF81fpAE2Yj2AuWgiVyt9l2CU74FpDXQE31YMsYMa0CB1RG9IgkmOWJDqDqH5sjmQVxBlYQbscijiPGT2oaiGagE3uUd3kQNAh4USS%2Ba3XNku7AOkzmEH74Od3c5DkTcOrmzmjaoeowl9h1NinolM%2B2Eqvjt%2BR9j6BRH5B03j3NuPwoP%2FDGCdy4DlbSyCQnslv4GB66ZADADKBXeNHNjllrpCPjBD5djZrdT8U5DcOC7Qt8jDYT5LftX%2FbVTryiQ23mwQSxhPj%2BITJnDY2zUE5uG6dzlqNbjEp2MwiSRQQxgNwKXhJhURyUrbZcN0Vqv6s4dHtmVV7kTshs6JdRSoaFSQfb4AsN6qPrR%2B3IyzuTjB5Z8ABT7tGk7Qxtmh3ZQteB9p50grP49zP%2BvE3Zaw5CXcAhfvhmq0sMOKIZkuIWsE8atNKehWzeTCUZ1O0COS4BGwpTAbJ0%2BA3rWHQrvs9FuK23zKK1w6bO79myzgH9%2Bq8MIPS%2FrwGOqUB%2BSlCrnkkEPuXZKjqv6sFwwc0dEHXARCOZczazq5l1mMRVUKBuvZ4AVud6J%2FlAidgvM6tJL1l1NPyBOYpXLtcglmy%2FKqAXVBYI%2BGDeeEmYTTNW1Ss1t%2FbuvaTAAtl5LaKDHgXJOhZRVTd0ecWd5E6fBxMkPUfjhfwwJEucpnsW8sajbsxp0qp%2FAzb0U1uyrkgcWD7Kw%2BACpZ4dD07pnRhq%2FQ6%2BD%2Fd&X-Amz-Signature=446633b0907c9528cde2f545a0d3e59694ba07151adfdfd5075cbd7c7015ba8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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