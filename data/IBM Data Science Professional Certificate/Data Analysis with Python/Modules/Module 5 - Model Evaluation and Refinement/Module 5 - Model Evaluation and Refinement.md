

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=66da4e1a3444bf8989215562ef60677e9f7cb6b6178104d3a06348c63955014f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=ca141c8737e98f340e7b7a926e823c9e4d2e43e993df8b0a496cf2c705c699b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=f9228f626deebc9f2c4b9942d0989f4fc8a7dc7212b5f73163799019c09c6424&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=c78d533ef074adabbed0d6674325aadf19f41757e0745727553886713ab17a4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=9b1a9ff600962a3dfb618272ada8ddc0bd06bb775d8e9025acd64b4370148c75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=78f81e8d0be797b000bc1c7e4e65c59c04fcd1baf507ec35f520c10c8b7eb497&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=60abd595e3a234593ff59c661eaf92f96ed1ba34aa445ef5039951775c406229&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=b8d18cb352d05eab3203de3063db5b3680682990a8863f3e67dc206098303786&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=9ba8b5b8b6cba955d6e2924751afc1e92de43e9b1c61848b369f9d24660d2c39&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XACJUF6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBkrTTjBtmDsJ1PZUrEQ5vjOkKn8tLdaAvGF2Xg4tyTAAiEAh%2B44dxsAQw%2F2hzc9j1Nv4kxCTo0AjPE5BrRXEnPYNW0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDEPVj6wZiVJAASVobCrcAwA4cO32g8DF4e%2F%2BNsTYsoMXdveaJMNhNnLx9R3MMCjG5klohQ6Rze7sATUMmWUvRgPbendA3mJo37LJJCEtDWDTqYsLk45DaL4eyujumbVmIRZ1fTg6rWSmTdp1wc59Yj47hPvemWnKue5INCGu8Z5jf7ytQdu0Nzb51DgqWqI3knSHyyyPozZ2cm5QWoN9qgWDiUKY94cFqV6CmnluszM5SR53%2ByufUFgSpAbfzCZyx3NDM2snUx0Q2Jy7fXamO1WKRCGYg38OtI%2B3iYc7TxYNISiKlekotL0h0eNinEcMbtI%2B8%2Bwx%2FQEsoJt7pT6B3YQ2VsVoPj8Hk2t939fLvAudxDSFvIHk2thVXUxfUDxhlgqjTFm3FNanWVg9xIr9G0m0%2Ba45RLjlOLiulz6eICb%2FlORqe%2Boe3iJQrbAsxQrgdHMyVxITP56BEyCGZXCngcKytH2YqDqWaZ1APrxLt3RzjDmcB43JbSIhA%2BJ0p%2BAZ0Oh78lPV741zscjSsgOIrqXHH8Q4WJ4oEkVO%2BAczXcF%2BfxDGf15KieBiLUVrlDCTZsIUz2sqaAvSZnzsjBD%2BJilmi%2FQATdwkTnrhwkZiQRJOb8hlqZqQQKoI9fDQfYaX6o41aXgKuOt%2B6MWWMMOps74GOqUBrIVWbW6F8vag2J5p7djublD3N5I5FC7LPydUi3rGEK2wMuMyMoX6ZFjwl1SF8PiI6ycl4biDPKO1z9InNGPhvCXEhmg4XLulcsBXHz81sP2xJ5BeFgdekYRpra2RxeFG0vkSC9HbY3caJ2%2BQfhnOhEpEw2CbC7TYIDbce16hLwsvYlTJ1SLkSvhS8ndemlaX467yc%2B5LACy3f6ABvVtO31g1m41V&X-Amz-Signature=ef0e6f9adfefcd79bb93c86465aa969997dff39e79d96d105a3e4f0c82408264&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XACJUF6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBkrTTjBtmDsJ1PZUrEQ5vjOkKn8tLdaAvGF2Xg4tyTAAiEAh%2B44dxsAQw%2F2hzc9j1Nv4kxCTo0AjPE5BrRXEnPYNW0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDEPVj6wZiVJAASVobCrcAwA4cO32g8DF4e%2F%2BNsTYsoMXdveaJMNhNnLx9R3MMCjG5klohQ6Rze7sATUMmWUvRgPbendA3mJo37LJJCEtDWDTqYsLk45DaL4eyujumbVmIRZ1fTg6rWSmTdp1wc59Yj47hPvemWnKue5INCGu8Z5jf7ytQdu0Nzb51DgqWqI3knSHyyyPozZ2cm5QWoN9qgWDiUKY94cFqV6CmnluszM5SR53%2ByufUFgSpAbfzCZyx3NDM2snUx0Q2Jy7fXamO1WKRCGYg38OtI%2B3iYc7TxYNISiKlekotL0h0eNinEcMbtI%2B8%2Bwx%2FQEsoJt7pT6B3YQ2VsVoPj8Hk2t939fLvAudxDSFvIHk2thVXUxfUDxhlgqjTFm3FNanWVg9xIr9G0m0%2Ba45RLjlOLiulz6eICb%2FlORqe%2Boe3iJQrbAsxQrgdHMyVxITP56BEyCGZXCngcKytH2YqDqWaZ1APrxLt3RzjDmcB43JbSIhA%2BJ0p%2BAZ0Oh78lPV741zscjSsgOIrqXHH8Q4WJ4oEkVO%2BAczXcF%2BfxDGf15KieBiLUVrlDCTZsIUz2sqaAvSZnzsjBD%2BJilmi%2FQATdwkTnrhwkZiQRJOb8hlqZqQQKoI9fDQfYaX6o41aXgKuOt%2B6MWWMMOps74GOqUBrIVWbW6F8vag2J5p7djublD3N5I5FC7LPydUi3rGEK2wMuMyMoX6ZFjwl1SF8PiI6ycl4biDPKO1z9InNGPhvCXEhmg4XLulcsBXHz81sP2xJ5BeFgdekYRpra2RxeFG0vkSC9HbY3caJ2%2BQfhnOhEpEw2CbC7TYIDbce16hLwsvYlTJ1SLkSvhS8ndemlaX467yc%2B5LACy3f6ABvVtO31g1m41V&X-Amz-Signature=6f1303cab98845d0a5249b7d6eb239b786cc63bdeb0a14ca58a5ccf960b89e8f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XACJUF6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBkrTTjBtmDsJ1PZUrEQ5vjOkKn8tLdaAvGF2Xg4tyTAAiEAh%2B44dxsAQw%2F2hzc9j1Nv4kxCTo0AjPE5BrRXEnPYNW0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDEPVj6wZiVJAASVobCrcAwA4cO32g8DF4e%2F%2BNsTYsoMXdveaJMNhNnLx9R3MMCjG5klohQ6Rze7sATUMmWUvRgPbendA3mJo37LJJCEtDWDTqYsLk45DaL4eyujumbVmIRZ1fTg6rWSmTdp1wc59Yj47hPvemWnKue5INCGu8Z5jf7ytQdu0Nzb51DgqWqI3knSHyyyPozZ2cm5QWoN9qgWDiUKY94cFqV6CmnluszM5SR53%2ByufUFgSpAbfzCZyx3NDM2snUx0Q2Jy7fXamO1WKRCGYg38OtI%2B3iYc7TxYNISiKlekotL0h0eNinEcMbtI%2B8%2Bwx%2FQEsoJt7pT6B3YQ2VsVoPj8Hk2t939fLvAudxDSFvIHk2thVXUxfUDxhlgqjTFm3FNanWVg9xIr9G0m0%2Ba45RLjlOLiulz6eICb%2FlORqe%2Boe3iJQrbAsxQrgdHMyVxITP56BEyCGZXCngcKytH2YqDqWaZ1APrxLt3RzjDmcB43JbSIhA%2BJ0p%2BAZ0Oh78lPV741zscjSsgOIrqXHH8Q4WJ4oEkVO%2BAczXcF%2BfxDGf15KieBiLUVrlDCTZsIUz2sqaAvSZnzsjBD%2BJilmi%2FQATdwkTnrhwkZiQRJOb8hlqZqQQKoI9fDQfYaX6o41aXgKuOt%2B6MWWMMOps74GOqUBrIVWbW6F8vag2J5p7djublD3N5I5FC7LPydUi3rGEK2wMuMyMoX6ZFjwl1SF8PiI6ycl4biDPKO1z9InNGPhvCXEhmg4XLulcsBXHz81sP2xJ5BeFgdekYRpra2RxeFG0vkSC9HbY3caJ2%2BQfhnOhEpEw2CbC7TYIDbce16hLwsvYlTJ1SLkSvhS8ndemlaX467yc%2B5LACy3f6ABvVtO31g1m41V&X-Amz-Signature=d46566b24199b0b7ee4f16c4f9e9c48d75f001b46d9fe1fb083459b397549146&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=a1dfebdfbf4fbf0c73ad715ed3fadebcc68c9d09d1330a568a00c503b04b10e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=d70f774aad4edf53870216a94b53b88044f9dcf9d579abd31799220020bc7ed8&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=b888dd048d630d0632cce7d17f097ae96aa73f443b43d0a1465d4aa439683d2e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=2a2e33b6e9a6c7f6a7710c251680b96022ce160a2d4a67f4eea1cecd14573bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=2feb67d68976050ee2d341561817f55ef41dbe41968924a48fa45ac57f18d6ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJBFNX2B%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIA6qZwJT9%2FGluIPhizoasKeZ0qJ635MKA%2BIMNXpyByS8AiEAwC4cXVhDfhYU%2B5elWxMbCuRRui9%2BdKxzaKUsnU0%2FURcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDHcr3slc69RI7GmU0CrcA5aKnadbEMyCUC%2BmO%2F%2FLNvcunGIozPgCJGS2VQHKARTlJ9hTi76z5nFN7nvpp6YEYR0GIX0AwnTk3r4%2FaaYZ4H17RCRzFmL6o4sR5jU1STvsMJkhKNIzXDkD%2FgNUssjQ%2FIY9uQ%2F4LEqDEQgHK%2BTIeNPhSDLplrrLTdZrbdvKPu3TJld5GX9A4ajLveQQR79YxC6rFKut0rZEgrGJCVnarzSHmHVb2pSBNz65qVR0TrqZlKPvAAcpYYaS0PXJU%2FLGwZO%2BGAFtTXW4dVU0OC3YG%2FHYSd%2BW%2FJxa%2FB69yKjkjPrGXmN6rK1UOz5%2B19dve6pZStKdI3cMZImOiGcx91dRjFOYpclsaKz7gBYSCnuumegTsVxkW40h6R0Kq%2FCc3rm0QPiPs4NHY2qBuUPsf6w%2BSbfLb0uYVA1tYMGB0XJUbBhUj%2Fx6o8kWWtbIAgc6wRRHcVFy3i6nY6o%2FxgUy5HPxgfLF1zZ9Whv177E%2FX%2FEMIZCeQYJYX48FmRBPQP3%2FLPC%2BCFgXVfJI2mUZahLSgcg%2FBc7bjmcgDmwc4V1XtMnOi7EOFu6gaF3DZoYcPu2%2FScy0CAsYwzVDFpwpRqoLgpi%2BL3IMTmP3j7unQ0KAf9FO0a%2F4%2B5sy6LBKJxNb7bjGMOCps74GOqUB%2BHsboVpOW5ojOc6fo0ArbcRlrmd9zLUzwTYVquwWEYn6V%2FOwRt454Pytww66MnVuC83iKw2ab0drBin%2FQve1kT9UxWeHxp8rAJFdHLCOSMeyl1rS%2B7CvmMKltip2txfToAPJaFueNDon0C3jhW9d3HIv92oSwUOUzqO0VGkJ6bNrjAfhbUA0vRGEN36C9EPlITXtRAha17JoIGrRfYsEXqhjJ6uq&X-Amz-Signature=4bc7a88b91382eceb240995011d73dca8d48450ddab1c79d69ebb828ecad8c3c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX53Z2GQ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCdYIeMJQJ4q1XPfR8OIMk%2Fc9Fu3BvTGZ1EWf9wcpE8XQIhAIt9rDhxkdDBNXNpH%2FdRYTIziD5%2Bmbg2sVLKOIvasj9rKv8DCGkQABoMNjM3NDIzMTgzODA1IgwLJ%2B9J3xD6rNxHdgwq3APp%2FzyWHtfB90a%2F1qH5ESzbcxI6PY%2BTDji5jF6XBvKdoirUkPztoBONBHNrGqbCxKy00r1lVGUou55mPTjdaXewky0KQUlmy8VY%2BfPKmBjWAS6WV2y8vMi%2BfVDGtJnY3skfw%2FPPMluB%2FTuxCC571p8CekUVYIZCSJAhv4r8JZ%2BL3hi3vYJcZ7H9kwvll%2F4ls4Gg%2FzQ5etGyvSzc6aGf%2BsPWO3vY8Kt4Ml%2B38ce7xoVe4I8SOymJORz8oLFB297QqyDJHJ6fl5ndcF7%2F7uBpInCbOd1Mu9YYX6s%2B%2Fp%2BtPMsXZmDgkc9NBlgj08OhqAp1iFCkF0dxHAn7r5ffiGPF9O7NoRmFwc24KHy%2FbrkrLk9bfXW2H3VNUaR07kCfDmqQRhPKulrk3gsC8au%2FNajee4S7eDufKZcWFtFS3orRFb54LzLrYyJLitKQMgb3TUyFUwmbryAJRJVYnLqCZSLJJhfy63rHXojGyTwFPqDCZrqRT%2FRHXNP2grA20ExlenrjM1kGLAGkZqCCsAgYVa6AFFpWCFM3Z7owiGXwSzu9dZhyf5Sj7CqAXXTbKvfsp1dfjnfrSqvcX6AgKTsg%2FkBN2HFwjAL7IukIChcLWhga2kPQIJob2qvPDB4K%2BIKYtTDkqbO%2BBjqkAYS7rYL%2B7jRSHXr1dv55EH4%2FdS3KQk2MmD3KPPBRtqm4xrHh%2BUSFpYdp5GSotHEk0ZCpnA4XiSfGQpiy9yoNNxo6ZgisxlGJrLQ0euU6lR463YD8jJb7u2CCzHNDMUQBrSRTsqQkupGndIBFRHOWI%2Fp4NqMrQSR8MsqlHEbiOSiDJr%2BLo7WvaC5FUUdvunYFQDzHr14BVkrus9d9ZiNIPf3cMYpl&X-Amz-Signature=97759ab95b97b3f1080c6367eb51149179e7163c33cca8fc2961ba50e9f0bce2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX53Z2GQ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCdYIeMJQJ4q1XPfR8OIMk%2Fc9Fu3BvTGZ1EWf9wcpE8XQIhAIt9rDhxkdDBNXNpH%2FdRYTIziD5%2Bmbg2sVLKOIvasj9rKv8DCGkQABoMNjM3NDIzMTgzODA1IgwLJ%2B9J3xD6rNxHdgwq3APp%2FzyWHtfB90a%2F1qH5ESzbcxI6PY%2BTDji5jF6XBvKdoirUkPztoBONBHNrGqbCxKy00r1lVGUou55mPTjdaXewky0KQUlmy8VY%2BfPKmBjWAS6WV2y8vMi%2BfVDGtJnY3skfw%2FPPMluB%2FTuxCC571p8CekUVYIZCSJAhv4r8JZ%2BL3hi3vYJcZ7H9kwvll%2F4ls4Gg%2FzQ5etGyvSzc6aGf%2BsPWO3vY8Kt4Ml%2B38ce7xoVe4I8SOymJORz8oLFB297QqyDJHJ6fl5ndcF7%2F7uBpInCbOd1Mu9YYX6s%2B%2Fp%2BtPMsXZmDgkc9NBlgj08OhqAp1iFCkF0dxHAn7r5ffiGPF9O7NoRmFwc24KHy%2FbrkrLk9bfXW2H3VNUaR07kCfDmqQRhPKulrk3gsC8au%2FNajee4S7eDufKZcWFtFS3orRFb54LzLrYyJLitKQMgb3TUyFUwmbryAJRJVYnLqCZSLJJhfy63rHXojGyTwFPqDCZrqRT%2FRHXNP2grA20ExlenrjM1kGLAGkZqCCsAgYVa6AFFpWCFM3Z7owiGXwSzu9dZhyf5Sj7CqAXXTbKvfsp1dfjnfrSqvcX6AgKTsg%2FkBN2HFwjAL7IukIChcLWhga2kPQIJob2qvPDB4K%2BIKYtTDkqbO%2BBjqkAYS7rYL%2B7jRSHXr1dv55EH4%2FdS3KQk2MmD3KPPBRtqm4xrHh%2BUSFpYdp5GSotHEk0ZCpnA4XiSfGQpiy9yoNNxo6ZgisxlGJrLQ0euU6lR463YD8jJb7u2CCzHNDMUQBrSRTsqQkupGndIBFRHOWI%2Fp4NqMrQSR8MsqlHEbiOSiDJr%2BLo7WvaC5FUUdvunYFQDzHr14BVkrus9d9ZiNIPf3cMYpl&X-Amz-Signature=742021e8f910fd4a2a105bc11dd23ac120890e3df0e12ee44ae43663573edbd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZLHG6X%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCICsuApqKhQH93UN5n7XsJsR8FjSGSvsRg84cQR%2FEOxl5AiBoiXO9Y31SgNytnkNUrTX56KPVMmVaY2VgjT8ul9o6myr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMzwc14yq0gUja6vX7KtwDMMzszjWSDmV5Mo7Z%2FWEt%2FXvXAOZw1WTJDhm8suajxq0Mrqn3IE7eoiFZgPFAYZTz1L30u%2BAftrY2Ljanaa%2BhMdRKV7loQcy3eWhlA1TytnBB6JclsoA2G%2F6g0EmwE2FD0CrzRxL%2Bdw4ay1CHvJKVpfxpiJ8b5vCfYGKpCgny%2FgB0FTFzJvAXx0o4JcX6zgVvW62sgcsL0bLOuG%2BLi9Wa5BV37AbuXTeCS0%2BBSk5QFcD4xcvSPn4ZvUsuD3l4jCayupM4huNz1B0vKDRTGTtb5YksBqFRuDwgxyme8F0A8smWUqEUXEd6wwENazNsyvsmS3C9s7cNcUsFkLNjD3%2BYm%2FH9CJnj28tvLYAtgRJhURWAY13cT2JxRnrGEa7oKfCTzEaNlwmYke3hrSI5TyqkJ4RRaW09iXq3x%2BUhQHkG3DjOnSOK7gS7DBsDSsWP8cRGi4LlYduC8O27uSqVdjesy6Kbh6FtwHJySheHHKWoBX041uASTUtOZn%2FEg6o8haj8oXIZpj%2FP2cYslvlyTPCICWWOoRWTScpPKvoNpq6RcxRvXOEHFlZQFeJjnqv4xMU03vIXbRIrygt3Io9ER7ZD0%2BWWaoeFIGn2QgU4Eis2tFLu5Ecz0ShcpfxwKcMw7amzvgY6pgHxCefmt0mU%2B5fnKA8pP2VL4CNoKCSgDLDDNFkF3g7IKdIS2wz4d0fZOdfXHaGfz3lnPIQrlOa6hzT5oCl4hBkNaxHsVpTTIANO%2FcJVM7PMF1iX2n01Xi21kXBNs%2Fyr00gMFKNxRMvsdhuSLYyETrK7CAyXTh6ZLafKU4NTyPuYaOwfG52ntZDLzyC2HNeZPGbYNF%2FvD8D1DZ7OfDay4qcryPinCxtZ&X-Amz-Signature=5d2aa2462ee28a32f6ec3c952eb0b17a5e827e153059e5a0a33ff085e82884eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FJZN3WD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIE38ur048x%2FJg%2FmG%2F5on9%2FkJcbxHBSwFb7U5cjunzbyFAiBt2sVLs78LKVuLuIxs%2BwsKG5IqO8CkOvMxnSa25ORa%2BCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMxWY5ds3SWGjb6L5EKtwDEaUXyjbkjVm1ICkHf9OpRbkFgI1uQXtwIVUUK2G08D9%2B1d3ql8i4NCshDFCBKydyu4C818nro16ptnpwt2RSxUf5FvKhagWP3PCgY5Ov1c0N4phTymO6vXRApFV4Vbm80vMTB94ARGvNBeG0%2FSon9QB2n1BRpWKVJ5Y5Z2uRXvNG5iaEure86eTgkyLJ1vhC1c4iwjNR8VYBRus8eLpzeDkWz7HTfIVwQrPVQrpIwFKa7rpBOrju8e0mf%2BrYi0AKXIS%2B7VDygsSXH5ERmWF%2Bru8%2BpHkrwF%2BTq2jg9COpROdGr58mPEH2pJagHkJLqJtLJSlTS26koL7Nc3eBUdWU9xROnLkxh6K6h%2BoSbK7FYrWOVdWBTcRblyR1ZRaf372pteXrvb7%2FyCMehU%2Fs%2BGEBmZcNPeMj4ilyLZo%2FKX1O4UvoZ1jz8iLlMrqr5XZsElMKUqodJOEzigZArCHRfcS0lUvCIR48EKMkgevt0M1gIOs%2B2bH%2BlSJ07Tg4jKM7fUBRLfjkbRPK0qwb0ilPMU69QYALnY%2FkTxc8jcS%2FX%2Bn8%2B81CQsuYLCeCD31eRmmjbC3%2BsCa%2FT1S5KQy4t7bpUrliCmUuI1NxTZOW2b%2FkIoyiWjIQk7eqjYXeoFlYz9Yw4qmzvgY6pgGBTj2LEb5HoW8ot24kWPZtrDOfBBSvhbJVfsS4J99hN2znKIWRlm30tUYMgppdE5wR3LkDGH4CJzcJ%2BZQPxOhk5tfRftIz6GCBBPS7ueJMCNhdTKm6%2FUILO2aC2hb1W1k2EEhKeP6rxPlgFgJqnRimWCWp5%2B%2FIKbpF8X9r81XauRLqC9GLKctQW9Cv%2FY%2F19HiRA4Ss4C8fwNyqp1030OgZ4hFE4erP&X-Amz-Signature=413e40adbaa02804de5365867137e6e43792ce8030e7b0767d8031b54540df95&X-Amz-SignedHeaders=host&x-id=GetObject)
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