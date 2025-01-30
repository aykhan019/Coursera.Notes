

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=c13b9fbeac5e68bdcf48c9c5d4b6899b10ce69e289bb22d4fb41f95ea80268d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=c9a3e415fe022239259822169a0fb95bef3d35c397d1b4c8c56217357613aa54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=159a471b6c143d5551a85eff398ac6d1bdc7f9b52a928e1837d02a084390a700&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=c8ac2815fc305ce3fdc074262bc5bcf8063fd5c7a4b433bce2c72d2b51c346e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=587fd9bbfeac93c4929e5b7d47d76805d2b8ec826a148445a6ba167fb95ce6b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=dea7859bd591a576f140fcd04acb9922aea8d166a1a7277d28cddf617fe2e02b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=ce775625fe333d80ac5e1c2ec39699defb330b12f3ed19bf8cb52272d7ad7524&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=ad34e36ce18624693fd3654d1b6d80ae9d40df6101ee20a34545a3b25c92b60b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=df60d5da9268d6c88ecf51946cd725cf9bcb529db1c926413740e3aa4ac295d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZAWWZLL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfW3O%2FIGqWwI8H9N0otPvrg%2F0rKK2lcnDgvKpMDz8UQQIgPqpOQHNm8SjEmKqY%2Fc2BH%2BAvPBNi370IaUHDTCatFusqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8XN%2B42aR6nINRXCrcA9X2ZcwuljplpjWaQbyRxqILzYYcjMevVGFSeAnH5RozD5NnxJE8%2FJbZz%2BvkzAhxei5VPhzUIXPGve73X5ETZ8WXky6oT3G1kQ2Xx638jRGQxExI92quSLU5LeQGbcWKa37SdIgbyl6V9nOywTFJB%2FBLvzkBkmjndoZqOWNZpjfj4SV7zqUpI8QwUFDvRZsAq6327wQRXR3oW6G7PVGuxrg9%2B2%2BG%2F5BqpMESYiVqylHH9MRkIBBvnQ5940yynISuiBaQqaoWpkqkstKHV3Ztqk8BnaqB%2F7smXElGMcnm0M7a%2BNipLB01F%2BjqzAOQbE306ZX1Qmd3STLVbstDa2N%2B%2B8t38HmLbSYDJyiuc7hK4FcdK8MjS%2FsCFZVnGvVXfgt5G2qYO2WCgmqMRsHTjJ0nk3ji3AULHFZbeB3vSnTMoMm7c0%2Bzgg4yHfoc5irlBYFpbhSTLun8x04idk%2F1m%2FgKI2XgYKY%2BZDGOhUTecWr2k2Dg8WgsPy1TrY29sg6JbRUP7LA50YWsOd8BH%2B0nMlM%2FLeDbASKi2f92I%2BqiIscs4XuvztMIEskkiAhXG1qYhF%2F5CzI8C%2Fiyn53yMgJDJLbog7xq4mILVjJpNZQx%2Fx5z%2Bcr4IPDs%2Br6PaoS1DEvbMJOX7rwGOqUBuVFABwEQ7bUjsX7f96P8ekpcIXzVAAcHM%2BaFqe%2BAkX4HACLpa6bj2VR5A%2B12t9HjcCCsL1HYUO8cogu7MOLAZb%2BSCvS%2FeMwUQFTVZYl4Clzxb1syMLfoWepp8iQrlzej1u2pjC9Jcv6I3XE9IBIGC3vyDJgPGktlsYF2YpclJC7sqBd1HZyftbVSlt6k3KMGrgddQ8UXV%2BMX9j9Q1T3zMeQXyl4H&X-Amz-Signature=99cc2ec5654715b499be01b6a6e147c0eae4e8e516009233ba2b66b4500f9a72&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZAWWZLL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfW3O%2FIGqWwI8H9N0otPvrg%2F0rKK2lcnDgvKpMDz8UQQIgPqpOQHNm8SjEmKqY%2Fc2BH%2BAvPBNi370IaUHDTCatFusqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8XN%2B42aR6nINRXCrcA9X2ZcwuljplpjWaQbyRxqILzYYcjMevVGFSeAnH5RozD5NnxJE8%2FJbZz%2BvkzAhxei5VPhzUIXPGve73X5ETZ8WXky6oT3G1kQ2Xx638jRGQxExI92quSLU5LeQGbcWKa37SdIgbyl6V9nOywTFJB%2FBLvzkBkmjndoZqOWNZpjfj4SV7zqUpI8QwUFDvRZsAq6327wQRXR3oW6G7PVGuxrg9%2B2%2BG%2F5BqpMESYiVqylHH9MRkIBBvnQ5940yynISuiBaQqaoWpkqkstKHV3Ztqk8BnaqB%2F7smXElGMcnm0M7a%2BNipLB01F%2BjqzAOQbE306ZX1Qmd3STLVbstDa2N%2B%2B8t38HmLbSYDJyiuc7hK4FcdK8MjS%2FsCFZVnGvVXfgt5G2qYO2WCgmqMRsHTjJ0nk3ji3AULHFZbeB3vSnTMoMm7c0%2Bzgg4yHfoc5irlBYFpbhSTLun8x04idk%2F1m%2FgKI2XgYKY%2BZDGOhUTecWr2k2Dg8WgsPy1TrY29sg6JbRUP7LA50YWsOd8BH%2B0nMlM%2FLeDbASKi2f92I%2BqiIscs4XuvztMIEskkiAhXG1qYhF%2F5CzI8C%2Fiyn53yMgJDJLbog7xq4mILVjJpNZQx%2Fx5z%2Bcr4IPDs%2Br6PaoS1DEvbMJOX7rwGOqUBuVFABwEQ7bUjsX7f96P8ekpcIXzVAAcHM%2BaFqe%2BAkX4HACLpa6bj2VR5A%2B12t9HjcCCsL1HYUO8cogu7MOLAZb%2BSCvS%2FeMwUQFTVZYl4Clzxb1syMLfoWepp8iQrlzej1u2pjC9Jcv6I3XE9IBIGC3vyDJgPGktlsYF2YpclJC7sqBd1HZyftbVSlt6k3KMGrgddQ8UXV%2BMX9j9Q1T3zMeQXyl4H&X-Amz-Signature=357fe0a1d322ff6a9eca55299632e9c4bee0eae0483c80c820b5837f3942f695&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZAWWZLL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfW3O%2FIGqWwI8H9N0otPvrg%2F0rKK2lcnDgvKpMDz8UQQIgPqpOQHNm8SjEmKqY%2Fc2BH%2BAvPBNi370IaUHDTCatFusqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8XN%2B42aR6nINRXCrcA9X2ZcwuljplpjWaQbyRxqILzYYcjMevVGFSeAnH5RozD5NnxJE8%2FJbZz%2BvkzAhxei5VPhzUIXPGve73X5ETZ8WXky6oT3G1kQ2Xx638jRGQxExI92quSLU5LeQGbcWKa37SdIgbyl6V9nOywTFJB%2FBLvzkBkmjndoZqOWNZpjfj4SV7zqUpI8QwUFDvRZsAq6327wQRXR3oW6G7PVGuxrg9%2B2%2BG%2F5BqpMESYiVqylHH9MRkIBBvnQ5940yynISuiBaQqaoWpkqkstKHV3Ztqk8BnaqB%2F7smXElGMcnm0M7a%2BNipLB01F%2BjqzAOQbE306ZX1Qmd3STLVbstDa2N%2B%2B8t38HmLbSYDJyiuc7hK4FcdK8MjS%2FsCFZVnGvVXfgt5G2qYO2WCgmqMRsHTjJ0nk3ji3AULHFZbeB3vSnTMoMm7c0%2Bzgg4yHfoc5irlBYFpbhSTLun8x04idk%2F1m%2FgKI2XgYKY%2BZDGOhUTecWr2k2Dg8WgsPy1TrY29sg6JbRUP7LA50YWsOd8BH%2B0nMlM%2FLeDbASKi2f92I%2BqiIscs4XuvztMIEskkiAhXG1qYhF%2F5CzI8C%2Fiyn53yMgJDJLbog7xq4mILVjJpNZQx%2Fx5z%2Bcr4IPDs%2Br6PaoS1DEvbMJOX7rwGOqUBuVFABwEQ7bUjsX7f96P8ekpcIXzVAAcHM%2BaFqe%2BAkX4HACLpa6bj2VR5A%2B12t9HjcCCsL1HYUO8cogu7MOLAZb%2BSCvS%2FeMwUQFTVZYl4Clzxb1syMLfoWepp8iQrlzej1u2pjC9Jcv6I3XE9IBIGC3vyDJgPGktlsYF2YpclJC7sqBd1HZyftbVSlt6k3KMGrgddQ8UXV%2BMX9j9Q1T3zMeQXyl4H&X-Amz-Signature=2cf65aca8dbdd2efca112e47dff65f564119f06ef253eb73af273c6efa191c6e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=515beff302bcb341e9c035babfd1bcc537ea1deb59bf031c0871c582cb10dea8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=81ebeba6f39d6b1d575f6fa90e77e6a4a9f17c101ca1c4dea3bd3de4dc1a4f19&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=5050739ce326f2a3c4d9327d4754d6db28bf73a8c1e12c8b5d9c093bcbb080a2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=57c6da797ad1d16332956c5ea95eb7dab374d21fcfd181488f3c33591ff8e318&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=a5ea50433fc5c869caf0657aa5bbe1b1b078bd1b01323bda96bb2cfafa84a46c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5VY3H4K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrF2qc3YxVUaKMuR92RPErztIvhDpwB7ecCTIRojMLOgIgHGI7gDTW0Rw7%2BuCC5pFIZMbyutwTfKgqya32e2SfeHEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFGMvSH5SRsMiWfySrcA1gKoRFItuQgF%2BPh3Dm9Tfi18lUxR2kSBs0lwdZ3a7f7Jmj1W1l7WyZKPjWOGDFCGTzIL6tjs0O0cH1KExKp8DSxje16OVcsUOr0trUauROJIVQm7OitZPwF%2FhsNOmvFnP6fKaB%2BhxmaHG79SbXMV7cF4CyzWVZfJB%2Fr2thib07xmefKkAbLaGyUZGjtDk%2FQNFSYGIdJIiBb46Wd5LD2GEA40B7%2BruYvis7ZzGhQKlvqCfrzo4DUI2uvBlHJXkirG1hhQCTXXj8KpjDirkLd6UvqBvqNWcvbXGEr%2FVhi0xMDKU40yX31CcrQFX%2Bb%2BSXOnW%2B7IYQNDo5j7KEhywc7QPR30dQXLLXfR5p07nLlei0lDYNkwZ%2Fw0UKH7CTI8WNRipED8nSCA2ofeVTGEDSts6SCGC9ej1bWswDU0hJClyMeK%2B%2FjQdOPqorxGP2fqhxXiwXFUyen8cvTdkXZcqyJRtdg24saqx9f5OLOqyxNXA1txjUGUaKdD5ctk22U14cqFzTZM7hvX9%2BlUE8hReS1ex6rEPFVXxlmQDBXBkp7mRaGfR%2B%2F3DG1X%2Fq%2BdFON4%2B3KGgBZEhNvjea32267wMaZqjfdcNFfufH7wuYnmIolKniweffpdpdRQ8fuW9VeMP%2BW7rwGOqUB2Sx6URJuM0qDCLjEdrP3C0awg5ko25tox8eFZoWal%2FYKnpWn13n%2B%2BzKjN1elXLfjdwXoAd%2F3dsn2NDT5IhWT2kWm9bt5jKVw%2BOxv0%2FbVQAowDIW%2B8J0g51WxxyHrv2A14XJ7xd4AekzrBi7ipq4hiXTTxsEA%2FyBoftibN3aBU66Yyw6YVY%2BZjxfYUJkHQn86MX0YDv47mp5vfkdxgt6SbTAfKqck&X-Amz-Signature=2f6c6cf3587dd6760cf0e302374b623d62dc008462e7ced1ed8012a2e56ba4ee&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665KYZ6BY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCkRd0122CS4PLnbDIS8YM8gcajgtnjmyzBzoiYejn5gIgWnylMCyVrB6vq1yyanCFRRscGapRrLo%2Fr%2BryzE1bB4oqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoSWyAs%2FS%2BuUyOpeircA%2BRiWuHQx3ZRCVaGK%2FgDP4N3Ys7dSE0wcuHD8bDC2f5VKaEwv8S0bticl66vij%2Bw7tuiXnGiljv%2BU6bPvvGciM5QKnTnsEskQcU1C1nyMQnaUng1xvzQ4Hf50flUiudgFxIvX9fWERbYjqTOGFVkYtd6z8oVlxChnix4jsmOCxC%2BEnQHrzwAvD1PYLI8tvPFx5QvGMyW44RoMLW82qK6IamarsGRJReE08Ooou8jfDU1rbUL7IYYrVmMO%2FeBIbGd5fTXo1xV0VwTz8lrBGYJSHmSN79wY5RYi82dVGbTXKSNQNwQ3nTAdGxjYcQfqQRmOPQ%2F4%2B%2FPQF4Utfj52W21V3qcLVfIGQNcVEa7i2YRQiHfWueiLVlJxhAJ37UbePYxnLk7k0ypd%2FHpQpyGjzr0Le9HZQwz3BVwKJJeSn2LF985rn4Hr0haydwvRy83z0aLYP%2BvBLvP8bi2%2Boydr7LQHRZlxn8pouXdeCFAVO6EjCNLZJXIUsbLe6P3JrCDMHbg0YZneRC5kHmJBXjbdMRyQwGn7sGPelTd9J2Vxe30LAxxQaQ89e6GNQoDyXIziS0WUCipj%2ByeYAYj%2B9FFS6z2a2smTRiaL%2BKp2RN9IsLgIiiIT%2B2HNGj%2B4s3Wd4fOMLGX7rwGOqUBmwgjkmlBVUmY2442ef3IdvB%2BVGcY2oTcCMgf1g1DAwkFrNJdg5kC5cUA8wo3EfE1oibJXLuClW4MwYig%2BSWx%2Fh2D935Mf%2BuiXdTp%2FLS%2Bl62%2FinB0Z966zeXTcNvie7mzY142QBZap521dGKMmtvbWtp%2BtzdVLBh%2Fqqqp0IzIgC60mze8sqW8e0m2FaYn1wKgYiz%2BUtiPh4F6Qco%2BmuBje56BmxH9&X-Amz-Signature=ec0d986919e040a4a3a65ca3052fb2f49885405e1486e4f2ada1ae2ed1661578&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665KYZ6BY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCkRd0122CS4PLnbDIS8YM8gcajgtnjmyzBzoiYejn5gIgWnylMCyVrB6vq1yyanCFRRscGapRrLo%2Fr%2BryzE1bB4oqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoSWyAs%2FS%2BuUyOpeircA%2BRiWuHQx3ZRCVaGK%2FgDP4N3Ys7dSE0wcuHD8bDC2f5VKaEwv8S0bticl66vij%2Bw7tuiXnGiljv%2BU6bPvvGciM5QKnTnsEskQcU1C1nyMQnaUng1xvzQ4Hf50flUiudgFxIvX9fWERbYjqTOGFVkYtd6z8oVlxChnix4jsmOCxC%2BEnQHrzwAvD1PYLI8tvPFx5QvGMyW44RoMLW82qK6IamarsGRJReE08Ooou8jfDU1rbUL7IYYrVmMO%2FeBIbGd5fTXo1xV0VwTz8lrBGYJSHmSN79wY5RYi82dVGbTXKSNQNwQ3nTAdGxjYcQfqQRmOPQ%2F4%2B%2FPQF4Utfj52W21V3qcLVfIGQNcVEa7i2YRQiHfWueiLVlJxhAJ37UbePYxnLk7k0ypd%2FHpQpyGjzr0Le9HZQwz3BVwKJJeSn2LF985rn4Hr0haydwvRy83z0aLYP%2BvBLvP8bi2%2Boydr7LQHRZlxn8pouXdeCFAVO6EjCNLZJXIUsbLe6P3JrCDMHbg0YZneRC5kHmJBXjbdMRyQwGn7sGPelTd9J2Vxe30LAxxQaQ89e6GNQoDyXIziS0WUCipj%2ByeYAYj%2B9FFS6z2a2smTRiaL%2BKp2RN9IsLgIiiIT%2B2HNGj%2B4s3Wd4fOMLGX7rwGOqUBmwgjkmlBVUmY2442ef3IdvB%2BVGcY2oTcCMgf1g1DAwkFrNJdg5kC5cUA8wo3EfE1oibJXLuClW4MwYig%2BSWx%2Fh2D935Mf%2BuiXdTp%2FLS%2Bl62%2FinB0Z966zeXTcNvie7mzY142QBZap521dGKMmtvbWtp%2BtzdVLBh%2Fqqqp0IzIgC60mze8sqW8e0m2FaYn1wKgYiz%2BUtiPh4F6Qco%2BmuBje56BmxH9&X-Amz-Signature=2cf8e3a1723de81e189d6eb512bb59dacef585fa0aa76daebd98b626bc543a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTM535UR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2BiXpuk5ZhVDBrDfHu%2FBjGPgDRFMlv3F0%2F7if%2Ff2zGuAiBFIAfNqMjZFHc9TajcdhzdQkSscmODKWfgxyELsE%2BnuSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNE%2BnABYzKiJVuNYiKtwDcirIYPQ%2Fbjl1oI4Jm2C4ibkZUshMNsZBHF7PGZlt4tXKn0OkiT8TmdQhFwxTQDi619IBlwJXgoUc1eu4AYUreYr7o54nDtX9zrqv9hi7%2FmKgAlIu0UqIQwteTPQWhCa%2BhENGDt9UBPHJyTcMZuTceP%2FkpjclVIv8eD84NQdKAzmtLH%2F4fXcmc6kPDYPB42jmWD%2FGQmpNMpPsZQcFfG8BnZJjt011dSqlzgHMNGEIPDcEL8JphbGQZKUt4%2FK5tWJvMF0a0Tg1ItCXSdhjPM%2Bi3wzMayQQz0lOB2fYss8J4cLgvkNwxwtfWrCdlsMYiQnTbcmlBmxjSH0dOsJbkpiVEQjyQb13%2BiHIjWeC%2BiAk2p9CAODYzHq3spR6u1NHBQ5h9KgVyVA%2FvPmyEJ%2FF9H8a3h6oM0pcXW8WHHlqkaYDHJ55kjmX2HAYfLURdiWSB2LLjVsD7T2qqgxPd4%2FrhqbC9uqiGox2uTJB4RlGqCXOx4Jfg37KVOi%2BM2pX9JM3N2xQtmFb9XKu36lmUswe2SaV7TcMD7wm9fIaWXpfxyEICk%2FfUoeP9XmAFeWX5E3nfgM%2BHNdcytMiGkn8LdkpXvN%2FK406P2b%2FClMEj6LQr%2FlZn8y8vRovnMORTTT8BuowgJjuvAY6pgEdrLrv7KauxgfOj9hGLLm3hZIM49Sr0jNyk2RpBmy75jhc7PCdUZLn2ZmINhpx%2BabHc%2Ba9LiIeoRoeNvrk6FO0sUfhI7am0LG%2Fprmt%2B7QSSVGFMygK%2FXp9hF74gNNoAF2I499dpB9VlXoHdbdQPpjllIKRHi6BsNVxZXLaaMBP4MW%2BIJnk%2FLV%2F9kQZxDRVDA1hrZegj6zLUFZh5DHCo%2BuDO%2FlU85V7&X-Amz-Signature=a0c91aed4e2ea9f0b5668d5874a317e13bb0e9843c6163a5b5543bb4e5678036&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=5e2d7a9fe53b3ae2113e841efe229561e5e9c47b8b36141cd3883a2879329f15&X-Amz-SignedHeaders=host&x-id=GetObject)
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