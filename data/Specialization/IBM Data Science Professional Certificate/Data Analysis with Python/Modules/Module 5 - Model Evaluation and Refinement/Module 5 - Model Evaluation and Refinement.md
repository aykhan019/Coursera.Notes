

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=709c444c7088ae07cd2b8c46c57b494828dbc533f028b2b445b39f54fc8a3848&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=8e53ecc0261d07e5368f8c09e0d9286cd563e5e2edf707d01a0d3f69c3de67cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=e2a26767960ec6d58818939c0aca329fe413786d3d8700d97b97236b6737ad57&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=9e9dda0f93620b0ae551fb8a0232eb8cf5b2c4cbd623a501d7857bf19c2f5a10&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=9cd28e9574cf60cc66976260d2181ed8e9bcfd135ae41779f4a66504ec54cdd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=d6d7535fad74fa8f5f8a1e551a71304f379b3477d9e30f57e5da562e57793b6c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=7437ba23087f2bd44c7bf7be35c144778e6caf209804d0a21e632934b9a64a23&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=e8537b884744a78c9176cce58fc3708baa69a451eadfed46ca6ecd2cb7622f11&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=60d3ba1d1e8937c469279bc1dc696d5c9a18fe112918d2e507e0e5484a27a0cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGJ6TWL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiBB51EYAFGdw%2FQH5PYMAQvoUd0MxUKv8qhUsavFfijAiEAm6v9GFHqCiUtjV5%2B1K6S6jy0osge%2F9mfG%2FE1u3GYnnEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlEBXF9zyFqOas8zircA1krnaZghLA6hMS7wui9HlGYl95j761osZkYsJSHWHrAlls8Wo0ZUhN4Y5ahECfBc5bSG6VrWNUF%2BvORw4O8vsZFGSLxzxjfkXUCFx5Y3rq4lfYTRnkdtb5eq3gjS2%2FkzT%2Fiq319CGsVFMGwdnRcwresr42JN0ZzSZDpsJE9L8cehQMcT6WFrQL%2BIddAf%2FkWdkLFFicCsULi4WIqPQIw%2F0%2Bcf7wzTOuRVoDZYraebofA9nlJV7JzDT0M6t5wJekUFLRO4OG75rVg0pZmnPAi6ZnpVpVorMsMqNUjwzcUCowOXJ6DK%2Bh2bDhN8TOcj3YSd61Ryl6TzRN8cLsYcTqGm%2FCTKr2bLUgPH%2FW5RUZTqnZcOgSRodiYPcCHNMPKy%2BwT9VffKRkBuTjh4T14ZRgK5BkzQh0U4RWWZ68pRXpCxvOeD4innPje4j11O%2Fnkpje7m62rN9Jt9h%2B8l7bOJRoZQ%2Ba0eNYiqobEYx9B9Z91206xi%2FNyRimANXd3ugeJ6Z5fJc4CTJrQg8EDaIPbyKJXC%2FLa1NnJ9MmdF4eDWe3kZmIdrFhg8PuQklrnwpZ17ERPsxLrjkMfosWLgHaYr7lVDDeJ%2BCztCNch8aNZxq8CyfES5PZAoiKi3TA4gh1%2FMODQ8LwGOqUBobQ5mFFWbBxmjort05sdoaLeNd4gQdSfbJfZxjVud6ZmLS%2FgoW0FrAjPs8YnHhBPL3tBycfecbhTXG64XBhtfOpZddUtj8BsBForXw5NdsUlX3RfxCf8wym15dd%2BO7GHZMMiMt1lk7jHfW5ExsfXCtexx5CwCMuNLGSN%2BqdHDQqCK74r3xKELhk5dmiT0uqGC9CWYcsDAARgvuFDU35vCJjAwY9O&X-Amz-Signature=aa4bc4afdd6e1f278f58b17944ede3b8ebe45a58b27210d991f38487ebb5d7dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGJ6TWL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiBB51EYAFGdw%2FQH5PYMAQvoUd0MxUKv8qhUsavFfijAiEAm6v9GFHqCiUtjV5%2B1K6S6jy0osge%2F9mfG%2FE1u3GYnnEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlEBXF9zyFqOas8zircA1krnaZghLA6hMS7wui9HlGYl95j761osZkYsJSHWHrAlls8Wo0ZUhN4Y5ahECfBc5bSG6VrWNUF%2BvORw4O8vsZFGSLxzxjfkXUCFx5Y3rq4lfYTRnkdtb5eq3gjS2%2FkzT%2Fiq319CGsVFMGwdnRcwresr42JN0ZzSZDpsJE9L8cehQMcT6WFrQL%2BIddAf%2FkWdkLFFicCsULi4WIqPQIw%2F0%2Bcf7wzTOuRVoDZYraebofA9nlJV7JzDT0M6t5wJekUFLRO4OG75rVg0pZmnPAi6ZnpVpVorMsMqNUjwzcUCowOXJ6DK%2Bh2bDhN8TOcj3YSd61Ryl6TzRN8cLsYcTqGm%2FCTKr2bLUgPH%2FW5RUZTqnZcOgSRodiYPcCHNMPKy%2BwT9VffKRkBuTjh4T14ZRgK5BkzQh0U4RWWZ68pRXpCxvOeD4innPje4j11O%2Fnkpje7m62rN9Jt9h%2B8l7bOJRoZQ%2Ba0eNYiqobEYx9B9Z91206xi%2FNyRimANXd3ugeJ6Z5fJc4CTJrQg8EDaIPbyKJXC%2FLa1NnJ9MmdF4eDWe3kZmIdrFhg8PuQklrnwpZ17ERPsxLrjkMfosWLgHaYr7lVDDeJ%2BCztCNch8aNZxq8CyfES5PZAoiKi3TA4gh1%2FMODQ8LwGOqUBobQ5mFFWbBxmjort05sdoaLeNd4gQdSfbJfZxjVud6ZmLS%2FgoW0FrAjPs8YnHhBPL3tBycfecbhTXG64XBhtfOpZddUtj8BsBForXw5NdsUlX3RfxCf8wym15dd%2BO7GHZMMiMt1lk7jHfW5ExsfXCtexx5CwCMuNLGSN%2BqdHDQqCK74r3xKELhk5dmiT0uqGC9CWYcsDAARgvuFDU35vCJjAwY9O&X-Amz-Signature=ff8e0272598ae78de21797c9beae82c8ba5d0ef40bc69037f9549277f1064ee6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGJ6TWL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiBB51EYAFGdw%2FQH5PYMAQvoUd0MxUKv8qhUsavFfijAiEAm6v9GFHqCiUtjV5%2B1K6S6jy0osge%2F9mfG%2FE1u3GYnnEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlEBXF9zyFqOas8zircA1krnaZghLA6hMS7wui9HlGYl95j761osZkYsJSHWHrAlls8Wo0ZUhN4Y5ahECfBc5bSG6VrWNUF%2BvORw4O8vsZFGSLxzxjfkXUCFx5Y3rq4lfYTRnkdtb5eq3gjS2%2FkzT%2Fiq319CGsVFMGwdnRcwresr42JN0ZzSZDpsJE9L8cehQMcT6WFrQL%2BIddAf%2FkWdkLFFicCsULi4WIqPQIw%2F0%2Bcf7wzTOuRVoDZYraebofA9nlJV7JzDT0M6t5wJekUFLRO4OG75rVg0pZmnPAi6ZnpVpVorMsMqNUjwzcUCowOXJ6DK%2Bh2bDhN8TOcj3YSd61Ryl6TzRN8cLsYcTqGm%2FCTKr2bLUgPH%2FW5RUZTqnZcOgSRodiYPcCHNMPKy%2BwT9VffKRkBuTjh4T14ZRgK5BkzQh0U4RWWZ68pRXpCxvOeD4innPje4j11O%2Fnkpje7m62rN9Jt9h%2B8l7bOJRoZQ%2Ba0eNYiqobEYx9B9Z91206xi%2FNyRimANXd3ugeJ6Z5fJc4CTJrQg8EDaIPbyKJXC%2FLa1NnJ9MmdF4eDWe3kZmIdrFhg8PuQklrnwpZ17ERPsxLrjkMfosWLgHaYr7lVDDeJ%2BCztCNch8aNZxq8CyfES5PZAoiKi3TA4gh1%2FMODQ8LwGOqUBobQ5mFFWbBxmjort05sdoaLeNd4gQdSfbJfZxjVud6ZmLS%2FgoW0FrAjPs8YnHhBPL3tBycfecbhTXG64XBhtfOpZddUtj8BsBForXw5NdsUlX3RfxCf8wym15dd%2BO7GHZMMiMt1lk7jHfW5ExsfXCtexx5CwCMuNLGSN%2BqdHDQqCK74r3xKELhk5dmiT0uqGC9CWYcsDAARgvuFDU35vCJjAwY9O&X-Amz-Signature=e492af93c69be71646d6f4b488f9f9e56e8a5141570997861d9d1ad61f3e0dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=667e4fc9e57d3f3b1adae67c458acf17b28981e540f36356e31296a6e3e3128b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=21c98fac85283b4fe5bc3b14b9e01ebce8662855bddbabc0b179cab2d37f04aa&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=3e92b4b6ceca97b3e36334ac5512263342406b9f73cd03a1d64d5dba24ed4f47&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=f3a1ec66b9b4783b3f4181e78a99add0b4163f701e7668d9a8fce49e9e4dcd00&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=f64af7a1c0155c53e2335fb5ceca22265891a5623733fb29f144ebace3168e8f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJS2UREX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCizLYH2uR3zstilIamQBgcjaKlDHGCW6kC4fYLsgKpcAIgGKuoIYDA5uUCN7Iy9Z4ifShV%2BALRluDn7GNcOnTcrEMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCuhcMQoUjwb3tl7SrcA3Ziuyz8EF6jC%2Fb28LGrPnOOAc9cUvQnIGtHXJrO6HMIoJIZOrdL8DRo72fHOEBBFVZRmr1EAPLqbV%2FYHmeyilfi1Fogm%2BeFZJzCDN%2B77RCFzQAhOG4R18fSvN22i3cuX%2BsWFplb5dQ3ReLZm2mfqT4%2FMzj9D%2BR9m5FKUVkmIEDh9wPlzTgpjWQK2QwlcJY7isv8n2Tc8HiQTbv9xxdAGicY1sX5tBFHfB%2FekWNG4Qr%2FsmEaWNWWmcVRZ39ZK21uQKHSII%2BAMeZwA6t8l4u9tlWnGCgaiurVEcnErM9g8ca9nbXRm5hx9aQo%2Fw6yWx3fkJHjrjDsixd4Kq%2BrqRok33YBoSUv1MmYJJdQOhr7blEIj6v%2FruZ0MQaOgq99DtTCcCdXpRK91RyBjjOn7PsNPNMC%2BmK6nm58l4NGln%2BgC3RVmxx%2Bkqm%2ByEQjaspvHfoNaqYSHqn02xvhbGmDvXeOcavym0lWFQzZ6%2Fjli9T5iQXRzm6iGc1%2B3tIPDfUi6cefC%2FmsRi43RvBf%2BgTM84tLHdwf6sysLYANgePb5dB2wvm8wbu1VtV1dzVqD%2BpImWGJ8ApLpp8Oyx%2FSotg%2BCN1I075%2FQDYnLUDFDtcT7n7yH17ANeEPUnhgZeujUvedMJnQ8LwGOqUBBUYdGDFxXEL%2BN8bOXyBrhbT0LEkgNnGPF6V%2FbA3Tui4AB63y%2BC%2BjLrIf1d%2FR4Bxhp5k5Fg5O8DQLEdKdtIQrCp8I%2FVimDlzqlYjdelmTXLrZpmTxwCPYfie4FlV6bc1CNZQFyh%2F3LpqyY5IvvlP0%2FIo1%2Bz%2BSnnZSroPBQ8NjXb8pAQ%2BEuqWDjxnIIHu0qA3LK2E1MCyGUx%2FfPHhu5bFGRnxBPRR2&X-Amz-Signature=4a03b28f3da6d356ac2cb5d4e4230465f728ebceb70c63620d16ec49664f8203&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TLPDMBP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeVm1gSaO9uYTJD7PKr2ulNVv0c9UawBEvGX7eG%2BS1XgIgKUJMkPPQuSdtOPXt%2FFFiBmyvBk8Onn0fzT8chsRqhOYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF6l0XdBv%2B4KKToY2yrcAxSb1tJcW9eOQKOEik4qnpWAp1Lj7fBAMUYSH8dh5ewi%2BzQ%2FkLybueb1mw08Dcd8sLtVraXf2QmqdQFpntr4x7dGqCK5yXTxkUS9ycGdP81KRd6ccjNL2gz2mknZ2MKn%2FMiNSuz1%2BhM5jddfsukvicsSKATgX%2Bb3wUaOISVf%2BpIJ0nIlVYkYkQ3k9R%2Bq3Q8og6O1YsahV%2BokvRKSdHBhGiVgOLoQ3iOw2SrejFjStE2x7Nk19HVV63PuiNdi1N9R9wyyL6daCqD2VbI8LEp%2Bp8tpXx3Geqyic90VeTbUfL38Q0MtsQBjqtR%2BhLtcMg1slZ%2Btg3olALGLTR01DcD1U3DEzEGRHua97HgXrzFC2bdNTteU7J37kRnbdrhHrHlqYlcK0kc3aHZM%2Bpa4OnNUYO59S5Ewp0YQSRTqCl4%2FhG6NX6Exqztfe%2F1czALiCYQF%2BeiQJcmxjleQeNYJPMICKr%2B3Un6oRI6iDUCG7Nre9xiY4%2BRuQiyiacgPkwQGTiOJbBHC4K%2FqTeMsu4LOrjt2o9ZOxKxRUwnu9GBJYqgHfPdRbywShz6Cmj0OlJ8Jg4n4TKv23p9X04UdP9lAEQca6S4KbeExuxPdajmN30nE7OaNXyPvmLwR2X7tl5dwMMPQ8LwGOqUBSY3u1vJV6RW4gretKN7eTFYw%2BC9NqcmP4K5cAdqEmUh5TRk%2Bcsk3q1rRvBNpiquPyNJL6AJrUZvkuVwkitTeeRMqftW2W%2Bn5IC9MNrI%2FwF5bPfuZPxWpVk8blPtdOYmNDAPHOBbK%2FubXxM3to8col64alD8LbF9HaO05DwvuWN%2FSjj9xgJ9aT3%2FHWCAAs0oGw9GHPHvRM7qoDFr%2BBvrGApjv0CcO&X-Amz-Signature=1e52db1bb51d7163aa00318943b68e3d82d75850a0297b780f7810a69d7f2dde&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TLPDMBP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeVm1gSaO9uYTJD7PKr2ulNVv0c9UawBEvGX7eG%2BS1XgIgKUJMkPPQuSdtOPXt%2FFFiBmyvBk8Onn0fzT8chsRqhOYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF6l0XdBv%2B4KKToY2yrcAxSb1tJcW9eOQKOEik4qnpWAp1Lj7fBAMUYSH8dh5ewi%2BzQ%2FkLybueb1mw08Dcd8sLtVraXf2QmqdQFpntr4x7dGqCK5yXTxkUS9ycGdP81KRd6ccjNL2gz2mknZ2MKn%2FMiNSuz1%2BhM5jddfsukvicsSKATgX%2Bb3wUaOISVf%2BpIJ0nIlVYkYkQ3k9R%2Bq3Q8og6O1YsahV%2BokvRKSdHBhGiVgOLoQ3iOw2SrejFjStE2x7Nk19HVV63PuiNdi1N9R9wyyL6daCqD2VbI8LEp%2Bp8tpXx3Geqyic90VeTbUfL38Q0MtsQBjqtR%2BhLtcMg1slZ%2Btg3olALGLTR01DcD1U3DEzEGRHua97HgXrzFC2bdNTteU7J37kRnbdrhHrHlqYlcK0kc3aHZM%2Bpa4OnNUYO59S5Ewp0YQSRTqCl4%2FhG6NX6Exqztfe%2F1czALiCYQF%2BeiQJcmxjleQeNYJPMICKr%2B3Un6oRI6iDUCG7Nre9xiY4%2BRuQiyiacgPkwQGTiOJbBHC4K%2FqTeMsu4LOrjt2o9ZOxKxRUwnu9GBJYqgHfPdRbywShz6Cmj0OlJ8Jg4n4TKv23p9X04UdP9lAEQca6S4KbeExuxPdajmN30nE7OaNXyPvmLwR2X7tl5dwMMPQ8LwGOqUBSY3u1vJV6RW4gretKN7eTFYw%2BC9NqcmP4K5cAdqEmUh5TRk%2Bcsk3q1rRvBNpiquPyNJL6AJrUZvkuVwkitTeeRMqftW2W%2Bn5IC9MNrI%2FwF5bPfuZPxWpVk8blPtdOYmNDAPHOBbK%2FubXxM3to8col64alD8LbF9HaO05DwvuWN%2FSjj9xgJ9aT3%2FHWCAAs0oGw9GHPHvRM7qoDFr%2BBvrGApjv0CcO&X-Amz-Signature=e547e9f724e345f339d99a4ef5b0aea6a452e02f59a67679a90f21a079a279e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646T3RDI3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCljvUhbwKme7lF46%2FQwrZJdwJAs3N%2F%2Fg8stfKn8%2BzJagIhAOaQJIdPy0GQm4s4slm%2ByKznVyevoLsEaegkj05EsKEUKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4SaEoLhJiZ4VLF%2FEq3APevbSi%2FVDpjU0UCaGs0Iki2bH0Gm5O7hJIdy5Fu81W9%2FyP%2F6a%2BVYH7ipT3IG1JY0s5mV3MUUkLyDORT5VWhg%2BdIjXOcY8oie88Fp86Te46TihB1EYOmXJvZmeMGtwOnHjppPH7pNQc5e107YNYG2IEfY%2B20kuLTGunjLBdcXiN29LaC9nQrr6SDVL4cdF05kEqdFgBtGkOdyevY0MtS%2B%2Bv7cICxsPlvaJ7IDDHxIYX2DaCIQgki%2BK%2BUn4wJRY3FCH4jkxS3qTTHSMre1Ttdtmpog%2BFHOpzVMVo0J2M%2BgSr7slKR2V8yJWcdxpe00BwLmqa3u%2FLo31WiQSqgqwPEIBFMVFfIIJjweVmd2jRu9AW4JJdMlDGYYQXkoJcSgl6Oipmd6zrouhIlpLFuR2Axfhuy9ygUMc9PNpjoSsdD1nfTkx1mhiscaDrB7%2BLCXFRJoN%2FK1VLtjVvvbNhhNng9r%2BvQ3kVVIqvusizxhfs%2B%2FUGMTcg2HOyXm9N6%2BOwuFazco1OnGR3ak03L%2FKnqSN%2FKl7G7XZwMQSzP44o4j9wWRoLueIu0AOmXOZUE9OSq7Ezar46YXKMx4y4Dc3%2BqoVYsHBBLA4yYj%2FVB3TC47Cc0g5GeJoRzbutcB%2BNK5TnkjDV0PC8BjqkARQmKk4m0gg7t9NwHmN8oKk9ULclL6X0LZP49D%2BXDhWZpX08t1q2D%2FCO8n31DXw1QG2t0kL22HIStfcdKxd%2Fbl7ospSjcoV1V7qExqYnW3WmB7n05Hj5QzNOa1xdXPfkv%2BwxwUgXX0tqmluvj6ilBlF4%2FhyZ81IjmawWBGbDTLg3nP%2FVm4P%2BgmEPurhBXpgW6MDMkWYL2qbwC74Ce%2FJzqH20HMMr&X-Amz-Signature=0cc7e99162482d803357b07828213852adbc1be156d6e4f7eb85bf523e612f64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=eed037ebd95076f3adeac3285a46d9ca7bf75aec983ab6dad2f6e08ad991a42b&X-Amz-SignedHeaders=host&x-id=GetObject)
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