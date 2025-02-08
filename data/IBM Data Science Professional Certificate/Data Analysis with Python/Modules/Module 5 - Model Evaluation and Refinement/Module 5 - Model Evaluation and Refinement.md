

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=610b18b0b7d3448efb7833d44ab6d810f0e768b99cf85362e8a2756f06804e36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=f46b51483e9924098183c4f451eeb234115c167037097b0f4b230a3ea24a3e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=3edbf5f2529c0bc4cae0c4c5f502b180aedebb0769050c11cf8587dc92067331&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=6d1f0294fadb2ce636e95c341f55cd68bb8143829416cdbd161525cb6ce7231a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=7ecf0257483297940db3e33123b545e50ef385fd98c3df79833680ed4c1ea1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=95f7992efe0a310eb80ebb0e7326e0689d2384123a43613d305175120e72a65f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=0ef3a74400bf05785535f6e61be82c5bb40bcbc70bcdc884e2c3718d35d12fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=2223efedc48c3c06471a29bacf42a2f31d340d512e1299bd9f724c0e651b5f86&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=4fe7d5da1b1119a949001066ba2b706bc20518dad5b04c93d200746d6413e4af&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMJ5XL6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDX4dm4tEJP%2Bvd3CxEpvBAz6jp3J4wPErWzICPZqR1cKAIgZmkOOWyXKy0OJQRiqZS80AeBbEzZ87Ap7kTSOd44xoQqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBPT8a8Uwp01m2KHnyrcA%2BKzY44%2FNTUchTnJOOOd67RXATWHYWvxhhailVKO3dnINFKn%2BwJ2XZCMm7hZZr7CfGDjXPtf5%2BqXoFxf3drSWhxdOwwq53Y8QdDkxg1H%2FKInlixWadJUVcfYA%2Ffg8uGeSI%2FnBfkk3jajK%2FNRAJZJyqAd8JzXyC8gyNfCqlTzQmsngBXIPqEaJ04PnyGt%2Blg5alvU7ZHpuL%2BVsu5QfSUwV69xHaHxHdiMBeRT%2B0C7xcFKuKIMMKgpK%2BupxVqEKUZotLXwwzkVL00gb5nvNdheLg1VSemN3nysXnyrkbsgyvAlVUoxFOJfAxuloCR05L%2B9uMpGQAzRnL776TjKqiRaUOkGS9OMke%2B4%2F6xjqLWnEnfomKUwy2LZd3AEFNWuOK0232y6cWoKbnCIWLTs1C436w%2BiFykQuluZyDzrHZ4art%2FaZ5sOpKa04G7YkWZOb%2FVKg%2Bl1KZsNzzDiQiQTkN4o7YxB3LI5wxggVTe2m7q3s5uhp3ndmF1wCsNVGlLp%2BCd77H%2BW15OxcK83hZsjzmTeZ2jSl3U%2BX7jRP1T6I4LNTLk3D9ph8j%2BJdggs1z4U2wL%2BctQ5NGGcaktEbfflCKs1iEzB94IT2qsbBU%2BeGdSLSuhRYGYEsJI24%2Bs2ON1VMKmym70GOqUBZlQ0luOnVh6BLCphLsVsw%2BxB3gqc9mVbe6IMSmlIv7fji%2BOn6L8ykrNJo2qVkL3Ob%2FEeBW6NUG4JLGoMTVDUwlx2omUO6OthIIoB4egGztcbOAspR7%2F93MKRsr3ovGWjZnuOwXDiXBXvQ%2FU2%2BU39vB936DAsG6dG3PgKmCczbDJnZo79qvZjaF3nQYMI7mFfAyzVVEAzgyM0gS9Z4ZdcFMVuLRAE&X-Amz-Signature=6f868727027370895efa9e8219cf201f660066cd313e4239278c8766579394c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMJ5XL6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDX4dm4tEJP%2Bvd3CxEpvBAz6jp3J4wPErWzICPZqR1cKAIgZmkOOWyXKy0OJQRiqZS80AeBbEzZ87Ap7kTSOd44xoQqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBPT8a8Uwp01m2KHnyrcA%2BKzY44%2FNTUchTnJOOOd67RXATWHYWvxhhailVKO3dnINFKn%2BwJ2XZCMm7hZZr7CfGDjXPtf5%2BqXoFxf3drSWhxdOwwq53Y8QdDkxg1H%2FKInlixWadJUVcfYA%2Ffg8uGeSI%2FnBfkk3jajK%2FNRAJZJyqAd8JzXyC8gyNfCqlTzQmsngBXIPqEaJ04PnyGt%2Blg5alvU7ZHpuL%2BVsu5QfSUwV69xHaHxHdiMBeRT%2B0C7xcFKuKIMMKgpK%2BupxVqEKUZotLXwwzkVL00gb5nvNdheLg1VSemN3nysXnyrkbsgyvAlVUoxFOJfAxuloCR05L%2B9uMpGQAzRnL776TjKqiRaUOkGS9OMke%2B4%2F6xjqLWnEnfomKUwy2LZd3AEFNWuOK0232y6cWoKbnCIWLTs1C436w%2BiFykQuluZyDzrHZ4art%2FaZ5sOpKa04G7YkWZOb%2FVKg%2Bl1KZsNzzDiQiQTkN4o7YxB3LI5wxggVTe2m7q3s5uhp3ndmF1wCsNVGlLp%2BCd77H%2BW15OxcK83hZsjzmTeZ2jSl3U%2BX7jRP1T6I4LNTLk3D9ph8j%2BJdggs1z4U2wL%2BctQ5NGGcaktEbfflCKs1iEzB94IT2qsbBU%2BeGdSLSuhRYGYEsJI24%2Bs2ON1VMKmym70GOqUBZlQ0luOnVh6BLCphLsVsw%2BxB3gqc9mVbe6IMSmlIv7fji%2BOn6L8ykrNJo2qVkL3Ob%2FEeBW6NUG4JLGoMTVDUwlx2omUO6OthIIoB4egGztcbOAspR7%2F93MKRsr3ovGWjZnuOwXDiXBXvQ%2FU2%2BU39vB936DAsG6dG3PgKmCczbDJnZo79qvZjaF3nQYMI7mFfAyzVVEAzgyM0gS9Z4ZdcFMVuLRAE&X-Amz-Signature=004c820335ce8584c82cd4594a2ca83bfcf632b3c62ed811bbb081b746b48c85&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMJ5XL6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDX4dm4tEJP%2Bvd3CxEpvBAz6jp3J4wPErWzICPZqR1cKAIgZmkOOWyXKy0OJQRiqZS80AeBbEzZ87Ap7kTSOd44xoQqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBPT8a8Uwp01m2KHnyrcA%2BKzY44%2FNTUchTnJOOOd67RXATWHYWvxhhailVKO3dnINFKn%2BwJ2XZCMm7hZZr7CfGDjXPtf5%2BqXoFxf3drSWhxdOwwq53Y8QdDkxg1H%2FKInlixWadJUVcfYA%2Ffg8uGeSI%2FnBfkk3jajK%2FNRAJZJyqAd8JzXyC8gyNfCqlTzQmsngBXIPqEaJ04PnyGt%2Blg5alvU7ZHpuL%2BVsu5QfSUwV69xHaHxHdiMBeRT%2B0C7xcFKuKIMMKgpK%2BupxVqEKUZotLXwwzkVL00gb5nvNdheLg1VSemN3nysXnyrkbsgyvAlVUoxFOJfAxuloCR05L%2B9uMpGQAzRnL776TjKqiRaUOkGS9OMke%2B4%2F6xjqLWnEnfomKUwy2LZd3AEFNWuOK0232y6cWoKbnCIWLTs1C436w%2BiFykQuluZyDzrHZ4art%2FaZ5sOpKa04G7YkWZOb%2FVKg%2Bl1KZsNzzDiQiQTkN4o7YxB3LI5wxggVTe2m7q3s5uhp3ndmF1wCsNVGlLp%2BCd77H%2BW15OxcK83hZsjzmTeZ2jSl3U%2BX7jRP1T6I4LNTLk3D9ph8j%2BJdggs1z4U2wL%2BctQ5NGGcaktEbfflCKs1iEzB94IT2qsbBU%2BeGdSLSuhRYGYEsJI24%2Bs2ON1VMKmym70GOqUBZlQ0luOnVh6BLCphLsVsw%2BxB3gqc9mVbe6IMSmlIv7fji%2BOn6L8ykrNJo2qVkL3Ob%2FEeBW6NUG4JLGoMTVDUwlx2omUO6OthIIoB4egGztcbOAspR7%2F93MKRsr3ovGWjZnuOwXDiXBXvQ%2FU2%2BU39vB936DAsG6dG3PgKmCczbDJnZo79qvZjaF3nQYMI7mFfAyzVVEAzgyM0gS9Z4ZdcFMVuLRAE&X-Amz-Signature=bbf6ce0a6e022ec559025cf4d924c8b6d648d94dc92b7311e17f9aa00fe6eb35&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=73e539664fa00075d00f7bc52193852538d3ac1420cc9097eef3f7129b5be5f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=96bd9f8fdf8188eb4693910d691440a8222dba64cdcd97ba411c5cc179b19302&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=da168fa665d77ef81255759986828567eeda0c0a5578968523930b1fbd4da33f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=3510bd13bb9221aa546814244a208ce16b4c6797a73be6bc8facbe9335ed0532&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=e008e58cabaf9f97d074a829a933e549b0d8c8f6e394735a5d3eb7ba307a43b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQBX7MH2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDz77SXbFudQFvoDOFDD%2Buq7prnYtIrCZZXNIsQRCw5rwIhAP65OsumH4YJ0hYPR2sgEihgne%2F55REdItF2r6OfIhAYKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FkZ2CPhfBsTEvv6Aq3AP49u5jb55wFZflzPj%2B8iHYqJPDW3eTK4WfdqpQv0gOaNORviHYcOxW7KQP0GrPdkfGnA%2Fy%2B15Ur73E%2FAeA2cAJByfhM9l22M0FG5GP3hKWDQ0A0t4y8Q9LTmRrNvV61kAjbr%2FsJZ8ImsWvklMkRdJqgU6RtX7UIp4cuIi4E3GyZ4nhLKmbf0XC60UqUFhzxZUTxpkmQeShPMKW5gs5IYkad5XTmY8Ai5da60L1JPD0oVPl6lCf1M22kMFwGyD89TKlL2zoeKPxsiYSL5kaBLIBkjA4fu96W99cOhYXu0v20UoMWCV6PKx4oa%2BO9%2BAWh6oQ2Kk0v3fuUCJfpenLA8urUrBPICqXHkKyYP6NGvB8apyf85bKfWTA%2Bcl2v32N3cNRQocZeDVSnexvJeLo%2B9Th%2F2pm0hnoLfJrVdBGKBdouPGSm7HrBMk0fsD8ek0RwOFyIftN4BvN8nyKLQyB3BHOOC7Dox86DpE9rZFcrsbfL4qD4xU7twddI8lN%2F8sfSL2Z45Qwa0yfwSXZZz1Td%2BskJeH1CqMeYEteF1%2FBpcYzuPZll%2Bh9Ii8HODIy7IK9T02OK10EiA%2BlHKobPApdySw7RjbaSa7sizhhmpe0M8%2B8K%2FAw%2F%2BXRHsE0sBFUdzCQs5u9BjqkAYujzKlbc5UPOjLij2t%2FuIAj3aBWpI9RfWgSAnn8lZePIUk04g8KMrpZBvlTsAe51zxsF7678pFA1SNvjkeq1Ldiivmopi4cBORXCIZXpI1D8yBuRBt24LBLAktu2Erq1mWsz1DwKsGDMJCFbRH9cPbP3ndly4eWfPJviXnwhgLG%2Biq%2F6m%2FsIxr6WnT8QrUkJILbPtlr5q3ga6FZvLpY2Q4XcPuh&X-Amz-Signature=9a4eb1e38f0153a271b6dc7dcaf08be7bba31b5de04b083ccd40c823e121fdfe&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPKECXKG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCKsLKOkn25T0OcGaORcM0sTsqlC%2BDbTCwPc66zZbojxgIhAOkiNvetYmUhTEFToCMo%2B1JjhMjR2QcgkkahWUm5IPJEKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjubsCHiJz4rBJBOgq3AN8g7vuq6%2B078yGAfd8HrRJg1i9YNi4I%2FzG6htj7L2zW9wndqpzlAQq5VbvkHiyh6Lw3TZyNehNrkkfV2yXYjIKQLjgsCWhkdNTtfbdQi7uVDocuox%2Bsovm2J4ck1bD8EB4UJNiFwoPVy9jW79y0q%2BMkRD5CC%2Bp%2FajYGlRnKYPpT8w44K4B3NVWjWH9s0eBwGGEFf8hSM5uHg%2FeQ3AG6SEA3vYyga%2B4fyESeTnczPD%2FEkvZ%2FXscLXm4%2BxjMLr3wAcAyV%2F9AM8sZhVttnnHqDWCm5QhacTHA8etWhSmb2mEr99SU1T3f7SSuoPshl0AxbyIWqIcn43RYYjr7LXVmElJhULAkYHDwrdWFwXEGacKLx8COs3BqNJr%2BQA30ZE5Gl%2FtRRSqI5%2BOHscGCknq5nulXH%2B5IPIna9U3RJgZpiI3A3ZJWrkGmCePV1FNuGUCJJCHTEZS8GQQyJUm6Z0x%2B1CdwgkPP9j1yO5EnD9T3J%2BX47Z98%2BhaNcpburzegJFbneKdI5fKnAHlozIUYlCkCl2qO44lVDZH6mGbiJR0%2F1TMdYNhz2L4rt4BYtv6VpRRHGaHOS811hOKMefCI978rrc2HfsWvExGQ0%2FA7%2FVNNL4V7u5DoxX5hMl3zDUnnQTCSs5u9BjqkAYfjwjGDFThFO25ssL%2FLlZPOGq%2FJ07lAet57PsGRrJA%2BaTBnVifh8qS%2FTg088KjYKYZ5ZL79mYcEdl4%2FByiG9MIPp6PwWQgC2Ae%2Bl9%2FSmaFyMu3hFxZpNNwOTJ2RKfAMFvhUBP9zgvcfEJ8VWcB2fGehAnPT2gG0Iy5l2wBEICtAfcE9GDEmOFkB1xkKg71ImkZS32thoAiEwT4k%2B2xNh5pT5Loe&X-Amz-Signature=163ca1c39606fbf946b96382763422acb7a305f31a507127f4b2de37dd3a050b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPKECXKG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCKsLKOkn25T0OcGaORcM0sTsqlC%2BDbTCwPc66zZbojxgIhAOkiNvetYmUhTEFToCMo%2B1JjhMjR2QcgkkahWUm5IPJEKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjubsCHiJz4rBJBOgq3AN8g7vuq6%2B078yGAfd8HrRJg1i9YNi4I%2FzG6htj7L2zW9wndqpzlAQq5VbvkHiyh6Lw3TZyNehNrkkfV2yXYjIKQLjgsCWhkdNTtfbdQi7uVDocuox%2Bsovm2J4ck1bD8EB4UJNiFwoPVy9jW79y0q%2BMkRD5CC%2Bp%2FajYGlRnKYPpT8w44K4B3NVWjWH9s0eBwGGEFf8hSM5uHg%2FeQ3AG6SEA3vYyga%2B4fyESeTnczPD%2FEkvZ%2FXscLXm4%2BxjMLr3wAcAyV%2F9AM8sZhVttnnHqDWCm5QhacTHA8etWhSmb2mEr99SU1T3f7SSuoPshl0AxbyIWqIcn43RYYjr7LXVmElJhULAkYHDwrdWFwXEGacKLx8COs3BqNJr%2BQA30ZE5Gl%2FtRRSqI5%2BOHscGCknq5nulXH%2B5IPIna9U3RJgZpiI3A3ZJWrkGmCePV1FNuGUCJJCHTEZS8GQQyJUm6Z0x%2B1CdwgkPP9j1yO5EnD9T3J%2BX47Z98%2BhaNcpburzegJFbneKdI5fKnAHlozIUYlCkCl2qO44lVDZH6mGbiJR0%2F1TMdYNhz2L4rt4BYtv6VpRRHGaHOS811hOKMefCI978rrc2HfsWvExGQ0%2FA7%2FVNNL4V7u5DoxX5hMl3zDUnnQTCSs5u9BjqkAYfjwjGDFThFO25ssL%2FLlZPOGq%2FJ07lAet57PsGRrJA%2BaTBnVifh8qS%2FTg088KjYKYZ5ZL79mYcEdl4%2FByiG9MIPp6PwWQgC2Ae%2Bl9%2FSmaFyMu3hFxZpNNwOTJ2RKfAMFvhUBP9zgvcfEJ8VWcB2fGehAnPT2gG0Iy5l2wBEICtAfcE9GDEmOFkB1xkKg71ImkZS32thoAiEwT4k%2B2xNh5pT5Loe&X-Amz-Signature=27ff6f32c77a727d4a785e27c028c9254ff2cdb731cc0a36d1d3ed3ee817ac44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642EGM6MX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIAES6OZjJ17UldlxvWh%2BCFL3%2FPQWVJNd0v53psd5Fwv%2FAiEA4kr0Iq%2Fvzy%2F9ruS1UuN2d5INelqAuATG%2FOrvKWoiRx8qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM6uSfNDajkeNdTUKCrcA9dhBG27MvEkr%2FAozAqZ1uFUXKxcs2v8PvR3ceJCZZVUoGRV%2BJqTSMnG0kk9um8cBkX6xVfF014b9TmStCYkpDjnbglFBJjPoRKg5Zowu1%2BlQdBasFmiKJp6vB26F23KJqoSYIRX2HEtkCiGoHLLzd7roKiCPNMbNAMIdjtuBMmioX%2FU%2BuRQ1t9%2FhSc33I6U06kLhwjNVNlXNEAaKL0%2BVFAZ3q81W70xcnRVIKGJhrSowkILV8FbNAO7BJapq%2Fa%2FS6%2FEhbI3i9KZJdkaeb9AwP8PqWsJQ7yG8jFavBjLGBzjSj9SNeNzH6j8ZJwuf%2B2TW1fgeoX4kD5vsjmJmh7qfjyCKsC7kaC58ksnjNbS7xbZmsXfxmoZ3jJ6iZv5V3UtZAjaPLHeg0hXRqKz7iVwLzaSVvc9LyjHOkq5P1fDhMVAxFRNmtlojX6AqmDW731fG8oKJCBd2gK5g9F%2Ba%2BTw9i3tcYxXuxBWXUeazbKpequppTbr0Ho89m%2FyTNj6qXLCtbe5gSTSLMJifBYeFhQ%2FHrpHV6GMGNt3jm71i8cjxPn%2FTaxmOJUcXIPrddehClcERlLT7JzNLSaYI3hbZv7Mv%2FV17JW5QG3wTcYg1gAet45Dntsp9O4k0UPrmpMSMKiym70GOqUBSW%2Fhv%2FCi3hPa%2BjVVtG58jWNYAa4NWRA7X3%2FS%2FqcVjmCqEo%2Fw9Prm11oIBt4Bi%2Bb23UuxSEnOQ5%2BdhjQ4%2FsO115XHA5qVZNczslBAcXnb7Dmd0VuqpHR41raZouXR1adGdkU13mnpM8QioAH0JXjZCaqFzkJGGr%2B%2Bzg5LB8gdw2rbHsYasGM8LU%2B%2F4ySClGjhMrFNzUxbUPCY2UIHn5FnlK1vcT7z&X-Amz-Signature=4e0bb9d2ee6f93dd47c33adc3ecda0d0d50b887049e034a6e51c3b57eaceec07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PQZKZAV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDZpv6cMWT%2FljdhjijMgT7hrREc%2FQ9JMKuAPqP%2Fb7GoMgIgUeox03zn0%2FKIh1jCWdDVYNFpxKDR7UW3umoREgcrFbkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuhAVVaFlbR2qBG1CrcA04D4EtMaQXdCfYbJXWxaDG2%2B0zesbt%2ByhDpQgaCwAAApvRqJ2g7RXgcK%2Bik4JuzBy5n764nYRVzgXYosBk4ebaDGplPXDa%2B4yRCbNzM2AnQFMI3nHKAOmyOMUmFgEyn8CLsRmkYoMDh%2F1oqUDXFk%2BL1c916xNZmjvwG%2B7fHnje7dlNy7wmTY0FsGSG%2BIjpjZimyBId934KLw3HTqOV9ME7KBqxWSFmtALEilE9cB17dT8DeiCAZvmeWE9bvw2X%2FFZ3Z4hkibe4bddt4M5zCjUEbVK%2Ff%2FUIzAtxQLoChdhjQlwvZOBFmOHcdbcuxjAhpl23KOReQErxaLOb%2BQa9nqpBk2vS7ysSshaP6%2B2T%2BOxm0emweQKkpkOk5LF1A8FTmexTeaxz481ZKMS5%2BymNb0VE3N1zqrWiu9pJxnDdfm7SFE%2B2taYA9Ljoei%2Ba4FiubEru3Xrz22wvy7ePPimm2ffFGm4OQxcmrwmQ5F%2ByFyUSBRjk7pIqMiZ53UBkjBPfP%2FfopJITStb33JFzpfPdNGYG4AqzHpOUZUeMaas%2F1pbJogpG5q2K11r5kXOoSQK%2BModxWCMeJGH100ScT%2Fb2vwazuKKGRCevfbAjXRCfnqAPGj4zasl40it%2FGq6r6MJGym70GOqUBClci50Y%2FsikdrvVMz4Q1jvMafvtJBHCm8mlaWMy6vEEkrrEm4QZlLjyT9Tf%2BLSvAEEaKCA4EstZEFhS5W16m%2B%2FLXyop47ELHI8vXRGQZIwPFI6jcRhhzmoPOX5auBsuhR1UImQBNZMUSl0e44Nnm%2FwpPgHoFXb2xOOdcEtB9i41CmlsH7Ubi5BM4b6acDueM%2F6XrISwZhaHwCV85L3Q%2FlhxrSUC0&X-Amz-Signature=e38d871d15137990deb79b9045bfdc983bc11170b2bedaadaea9e4403b4ae196&X-Amz-SignedHeaders=host&x-id=GetObject)
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