

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=32fed4e259d97fb5f1bd675d14df9f0894be250e2364863deffafc56cb3abb14&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=714c3bfd47fbf4f106e79a2a43a58683032895363b7433de54b4b1c2367dad2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=0d8e6a4da870838174af740e88018c52b3153ad1270e749f23df399387d40b94&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=2797817ecee5565fc4b7b46866e38dfb8d813a6a02f84953eaae27e69fd0050c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=93fccd61d319bee190e6ea942226e6f432fc489bca33f56e93f6b73fa398b463&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=27c873e3ff2ffc349eae9063508a72fcd036af61993603ad1b4d7d3c2f7446f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=6f8471c1a689b0403c0c95921c3cf035ab90341653c2b58583071114603d5c18&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=c87c76bfb61fadc2522f816ad6438089e961d86ecf4629427627576c7ce61635&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=149c741551e1aa9a779b15ac50d9cefbd16395531b20480b5ccd4061678fc2e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVK4YXU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCb0KvFP7l7xqsPyb2fGhOTg7wMxYhOEAzVzhMEVaGvUQIhAKzETQgMIc0uMEdZOZAS3nSHXh1bDFwj9GFYNim1ZXUBKv8DCDMQABoMNjM3NDIzMTgzODA1IgzEHu1seuwvI3Gg4uMq3AMUWHNaomjZTi%2BJQ5CEiTgAPEU9sXMjmBlAiHphWr8ikkNmMeDN%2BceBG%2Fdar5%2BfETTNUePHiVOYryldP1T%2BAbB6i6D5Mfuo8NX0HrpX3zB8pwdatZcRPPfpSRP56p9nw%2B%2B8sOtJnaLinw2OdxQOmcjLa8XJAsWhyveOiSE%2BfnRgq2xO8ZDhdU75xqlWM3mzd%2BAni9f3Kz%2BQH2EfEjidyM5bsz3q%2FEoZbc%2BS%2Bz15DZCxNvDIyBGrMLrC3bFyC5dLqFMSdGk%2Fep7z%2BmEpu7g%2Fb9epNehUyuKsPkiBxOj409usmnj2N9MoA2oFnAxYwEwGHo%2BZJOxobp28PJkFRB3n6J29mZYg141McTB4zCAOhr3cMEnGsf1%2F84CQnNAelSbnX4DZrxTDFdENQlxWmk65eT7DkNLxW8CXuuB92yy%2F33QRAmQZBONwRPsr%2BV3FPGyS%2B%2BWaotfo0JjKLprm5nz2CxQLB4hrmvjNB6XpYej9KY38qv3b3fo9C4aFWhOaOYB7e%2F8iRUlyqs8cQbXUfHBLTqqA3CnOEeaJQZTDNrDAIm6vumtbM1krHGEMAumV8utJYP6jWUyVs4GivlXYebtvpWzM0gvjiHU0heCaVcZhc7bJz2XicYE1s7O01RKo7jDaoIm9BjqkAcgPmh2TWbzePJ1w1DXXxVYW1GdM7uZ2cUDarjwgKlxm%2FOyikxXa6ZWJYmoTDWParOYNpFJI%2Bo2VexSOfLwXP0fdbIXzFlLWHeIsREL83qIs71yprangn7e1UHbWT5NHYPEENdJ4tuttezWb2ig%2B7NK7Dv8yVs6pTqdPuFYbtunpVRfRgkPBPDwLUhYmaRZ6len0EwGFmPgWqhMaCQ%2FKz%2Fl%2BApOS&X-Amz-Signature=ed18c2bc32ef5c1137e00bf762a98ce2eda45e58e2587d431e05406cf53f5444&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVK4YXU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCb0KvFP7l7xqsPyb2fGhOTg7wMxYhOEAzVzhMEVaGvUQIhAKzETQgMIc0uMEdZOZAS3nSHXh1bDFwj9GFYNim1ZXUBKv8DCDMQABoMNjM3NDIzMTgzODA1IgzEHu1seuwvI3Gg4uMq3AMUWHNaomjZTi%2BJQ5CEiTgAPEU9sXMjmBlAiHphWr8ikkNmMeDN%2BceBG%2Fdar5%2BfETTNUePHiVOYryldP1T%2BAbB6i6D5Mfuo8NX0HrpX3zB8pwdatZcRPPfpSRP56p9nw%2B%2B8sOtJnaLinw2OdxQOmcjLa8XJAsWhyveOiSE%2BfnRgq2xO8ZDhdU75xqlWM3mzd%2BAni9f3Kz%2BQH2EfEjidyM5bsz3q%2FEoZbc%2BS%2Bz15DZCxNvDIyBGrMLrC3bFyC5dLqFMSdGk%2Fep7z%2BmEpu7g%2Fb9epNehUyuKsPkiBxOj409usmnj2N9MoA2oFnAxYwEwGHo%2BZJOxobp28PJkFRB3n6J29mZYg141McTB4zCAOhr3cMEnGsf1%2F84CQnNAelSbnX4DZrxTDFdENQlxWmk65eT7DkNLxW8CXuuB92yy%2F33QRAmQZBONwRPsr%2BV3FPGyS%2B%2BWaotfo0JjKLprm5nz2CxQLB4hrmvjNB6XpYej9KY38qv3b3fo9C4aFWhOaOYB7e%2F8iRUlyqs8cQbXUfHBLTqqA3CnOEeaJQZTDNrDAIm6vumtbM1krHGEMAumV8utJYP6jWUyVs4GivlXYebtvpWzM0gvjiHU0heCaVcZhc7bJz2XicYE1s7O01RKo7jDaoIm9BjqkAcgPmh2TWbzePJ1w1DXXxVYW1GdM7uZ2cUDarjwgKlxm%2FOyikxXa6ZWJYmoTDWParOYNpFJI%2Bo2VexSOfLwXP0fdbIXzFlLWHeIsREL83qIs71yprangn7e1UHbWT5NHYPEENdJ4tuttezWb2ig%2B7NK7Dv8yVs6pTqdPuFYbtunpVRfRgkPBPDwLUhYmaRZ6len0EwGFmPgWqhMaCQ%2FKz%2Fl%2BApOS&X-Amz-Signature=a64ff43cb4774d2a8de2c8fcaba986d866c2ded6a36452aea9d6768e43b3b6c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVK4YXU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCb0KvFP7l7xqsPyb2fGhOTg7wMxYhOEAzVzhMEVaGvUQIhAKzETQgMIc0uMEdZOZAS3nSHXh1bDFwj9GFYNim1ZXUBKv8DCDMQABoMNjM3NDIzMTgzODA1IgzEHu1seuwvI3Gg4uMq3AMUWHNaomjZTi%2BJQ5CEiTgAPEU9sXMjmBlAiHphWr8ikkNmMeDN%2BceBG%2Fdar5%2BfETTNUePHiVOYryldP1T%2BAbB6i6D5Mfuo8NX0HrpX3zB8pwdatZcRPPfpSRP56p9nw%2B%2B8sOtJnaLinw2OdxQOmcjLa8XJAsWhyveOiSE%2BfnRgq2xO8ZDhdU75xqlWM3mzd%2BAni9f3Kz%2BQH2EfEjidyM5bsz3q%2FEoZbc%2BS%2Bz15DZCxNvDIyBGrMLrC3bFyC5dLqFMSdGk%2Fep7z%2BmEpu7g%2Fb9epNehUyuKsPkiBxOj409usmnj2N9MoA2oFnAxYwEwGHo%2BZJOxobp28PJkFRB3n6J29mZYg141McTB4zCAOhr3cMEnGsf1%2F84CQnNAelSbnX4DZrxTDFdENQlxWmk65eT7DkNLxW8CXuuB92yy%2F33QRAmQZBONwRPsr%2BV3FPGyS%2B%2BWaotfo0JjKLprm5nz2CxQLB4hrmvjNB6XpYej9KY38qv3b3fo9C4aFWhOaOYB7e%2F8iRUlyqs8cQbXUfHBLTqqA3CnOEeaJQZTDNrDAIm6vumtbM1krHGEMAumV8utJYP6jWUyVs4GivlXYebtvpWzM0gvjiHU0heCaVcZhc7bJz2XicYE1s7O01RKo7jDaoIm9BjqkAcgPmh2TWbzePJ1w1DXXxVYW1GdM7uZ2cUDarjwgKlxm%2FOyikxXa6ZWJYmoTDWParOYNpFJI%2Bo2VexSOfLwXP0fdbIXzFlLWHeIsREL83qIs71yprangn7e1UHbWT5NHYPEENdJ4tuttezWb2ig%2B7NK7Dv8yVs6pTqdPuFYbtunpVRfRgkPBPDwLUhYmaRZ6len0EwGFmPgWqhMaCQ%2FKz%2Fl%2BApOS&X-Amz-Signature=0df2242ac4f46b71beca20b062dcac0cf6d7c170dc7b36e32e647e4ae680f878&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=1b20eb1efb15be914a330219488acb1d8fa3c5ce19a6bdea0950fb2906db0a74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=c973cfa7936fc9cbc5b1fb833e7ac59cf8cc966d868c091f294b96b53f776b99&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=bc59452e775a08d87a0f1f91befa5cb43b35a406a11057005b6464ae600dcf46&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=b9df865093ef88d37330c1f82e68f90f30dca3bb908cbf09b46d411d312d984f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=6251a047eedb8cd7a3625f1f722aa68e4e0b59ee77c1288f80d619fcfb316273&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V77KDVUF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDu8rUfDdGBGLwGSWtv3%2BkHgGgJjBdtMmhNhiJeiwY%2FVQIhAIo7U9Z33Q4c%2BBSYT8FDIuZVH7nFVELzXTtaq%2BodDBE%2FKv8DCDMQABoMNjM3NDIzMTgzODA1IgwtqMD7a318vIEOwiIq3AM%2B0I%2Ff99q1jYCVpamhnBkFylKiilITS%2Bxdehax%2BZmHlo3wEWpME5ZHChNWTkqeJ8Cr9HteSTDnSHLWFKTfqAK5Te08kVdBAQh8niZyg1jWndB0EyMH8NY8LJoES%2B11yd7MNp3qyx0GaTw5orLaZkGPwEKSKERg%2F5U0mk74noLAkZtlLSVXtgy%2BrGHF4MWvqYzRcr%2FRTXMvDwjB8OPRpbQlbHwqC0uNf%2FSIAEiye9GomB8aMoIxxm8bUswbpxAyvARXO7rDkyCsMIzrJZx1BYRViC1kz%2BBMcNKX6%2FWOnejYlywAT3wl6y8wSENDNPYI%2BZSHxd9wCrAL05jaghwTCfCX6%2BvLdBj4RyICB%2FgOEXy35qau4Glu2%2BeLAkNgbxBm7wvJVi2HPKdleIX0zH9qz3dNHpC8reQ6kfGld8BHm%2F%2F61PPCXtfSontMF7byVSOREp%2FUqMECRIi1L1SXbJ7xCLIjkTw%2BC4fsgvPN%2BpJvWwimoS4gwINnAP6ICtJ%2BoEYSzTl5ZYfO8mcVFrO9hhHzEViTWZUvPfdrlM%2FgP0HHJR8Ux37mLKA5R7suUy9W3T7omEAGTg276WapSMX2GdKIq2Cqc2rgqTtgmnsAdDQ%2FNJ7LyXFbRkv9vafe151WezC2oYm9BjqkAX0WuYU0qYafShReYr3tV0vbrvir4JeG2in83TDLsNSa7U41%2FN1kmflBra9UU7XgQeSdMr46En16LoDD4gmwC%2BDexn74ZmzBaadvyOpkRFZ9S3SqDZlwR0T9aRsKXU8TUH1D7ibjx%2BUzQxXTfe0RbwlSNhR3xD8EqmC9yywEcLK4oZmLMHVOFPVuy6r0BR3fDakCi%2Fmh6FDNliqRPs3oIkzOzkND&X-Amz-Signature=219bea914c4152821a104d03c005e6b474f166dc8dc8bd43df186cb4b180b85d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVK4YXU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCb0KvFP7l7xqsPyb2fGhOTg7wMxYhOEAzVzhMEVaGvUQIhAKzETQgMIc0uMEdZOZAS3nSHXh1bDFwj9GFYNim1ZXUBKv8DCDMQABoMNjM3NDIzMTgzODA1IgzEHu1seuwvI3Gg4uMq3AMUWHNaomjZTi%2BJQ5CEiTgAPEU9sXMjmBlAiHphWr8ikkNmMeDN%2BceBG%2Fdar5%2BfETTNUePHiVOYryldP1T%2BAbB6i6D5Mfuo8NX0HrpX3zB8pwdatZcRPPfpSRP56p9nw%2B%2B8sOtJnaLinw2OdxQOmcjLa8XJAsWhyveOiSE%2BfnRgq2xO8ZDhdU75xqlWM3mzd%2BAni9f3Kz%2BQH2EfEjidyM5bsz3q%2FEoZbc%2BS%2Bz15DZCxNvDIyBGrMLrC3bFyC5dLqFMSdGk%2Fep7z%2BmEpu7g%2Fb9epNehUyuKsPkiBxOj409usmnj2N9MoA2oFnAxYwEwGHo%2BZJOxobp28PJkFRB3n6J29mZYg141McTB4zCAOhr3cMEnGsf1%2F84CQnNAelSbnX4DZrxTDFdENQlxWmk65eT7DkNLxW8CXuuB92yy%2F33QRAmQZBONwRPsr%2BV3FPGyS%2B%2BWaotfo0JjKLprm5nz2CxQLB4hrmvjNB6XpYej9KY38qv3b3fo9C4aFWhOaOYB7e%2F8iRUlyqs8cQbXUfHBLTqqA3CnOEeaJQZTDNrDAIm6vumtbM1krHGEMAumV8utJYP6jWUyVs4GivlXYebtvpWzM0gvjiHU0heCaVcZhc7bJz2XicYE1s7O01RKo7jDaoIm9BjqkAcgPmh2TWbzePJ1w1DXXxVYW1GdM7uZ2cUDarjwgKlxm%2FOyikxXa6ZWJYmoTDWParOYNpFJI%2Bo2VexSOfLwXP0fdbIXzFlLWHeIsREL83qIs71yprangn7e1UHbWT5NHYPEENdJ4tuttezWb2ig%2B7NK7Dv8yVs6pTqdPuFYbtunpVRfRgkPBPDwLUhYmaRZ6len0EwGFmPgWqhMaCQ%2FKz%2Fl%2BApOS&X-Amz-Signature=a1b8c5281f3b2e21c3e9b6c83a337e5312dfef0b3b3f56f716fde48097d2b662&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFVK4YXU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCb0KvFP7l7xqsPyb2fGhOTg7wMxYhOEAzVzhMEVaGvUQIhAKzETQgMIc0uMEdZOZAS3nSHXh1bDFwj9GFYNim1ZXUBKv8DCDMQABoMNjM3NDIzMTgzODA1IgzEHu1seuwvI3Gg4uMq3AMUWHNaomjZTi%2BJQ5CEiTgAPEU9sXMjmBlAiHphWr8ikkNmMeDN%2BceBG%2Fdar5%2BfETTNUePHiVOYryldP1T%2BAbB6i6D5Mfuo8NX0HrpX3zB8pwdatZcRPPfpSRP56p9nw%2B%2B8sOtJnaLinw2OdxQOmcjLa8XJAsWhyveOiSE%2BfnRgq2xO8ZDhdU75xqlWM3mzd%2BAni9f3Kz%2BQH2EfEjidyM5bsz3q%2FEoZbc%2BS%2Bz15DZCxNvDIyBGrMLrC3bFyC5dLqFMSdGk%2Fep7z%2BmEpu7g%2Fb9epNehUyuKsPkiBxOj409usmnj2N9MoA2oFnAxYwEwGHo%2BZJOxobp28PJkFRB3n6J29mZYg141McTB4zCAOhr3cMEnGsf1%2F84CQnNAelSbnX4DZrxTDFdENQlxWmk65eT7DkNLxW8CXuuB92yy%2F33QRAmQZBONwRPsr%2BV3FPGyS%2B%2BWaotfo0JjKLprm5nz2CxQLB4hrmvjNB6XpYej9KY38qv3b3fo9C4aFWhOaOYB7e%2F8iRUlyqs8cQbXUfHBLTqqA3CnOEeaJQZTDNrDAIm6vumtbM1krHGEMAumV8utJYP6jWUyVs4GivlXYebtvpWzM0gvjiHU0heCaVcZhc7bJz2XicYE1s7O01RKo7jDaoIm9BjqkAcgPmh2TWbzePJ1w1DXXxVYW1GdM7uZ2cUDarjwgKlxm%2FOyikxXa6ZWJYmoTDWParOYNpFJI%2Bo2VexSOfLwXP0fdbIXzFlLWHeIsREL83qIs71yprangn7e1UHbWT5NHYPEENdJ4tuttezWb2ig%2B7NK7Dv8yVs6pTqdPuFYbtunpVRfRgkPBPDwLUhYmaRZ6len0EwGFmPgWqhMaCQ%2FKz%2Fl%2BApOS&X-Amz-Signature=53cfb06e4c6c1d0f9691f568a83e937c642ed397fc02843df7d8583e4cb27900&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MAMM2E2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICkE5URchf1JkqLq6Vha9Pj7v5WPDVvSQpJaNzD3uzpZAiAqmugGepo3vhu3hg%2FJrF13akNCHVhL13W3rqH0C5mUmyr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIM7UVfmShcagFKJiQoKtwDDFn2pM9h0LHeMljbOjRypYds78mrBJNDLFD%2Fn4Sq97Nywx2%2FScB8yomNqaltP4XPa1UCWNAepGJC0OfJgUf%2FRdZXfVjUXCo1VQnCsMX8uHBEa2jhtt3PJ%2BobfzIkaNgP%2BLZL7ncjV%2BSL7xeB4Y3X01uUhTNC0mBIz56cAGgk0tkitDCIFKCPSQTPR8Gp3fpUpVhyw4zNkjwoNfKTpzlYKYEp6MAdGkEG2SGt9AyCbpx%2BRSHjKeWd2CckiHzu2R55QXtdJHn1SQmdn6dI3uL8qgGz41ofibsxHaM3fNpPtGmFRgJAqHCRIFwIvunC8NvL9MRK%2FBsnBZ9rGaYu4bTnCji3dWpxOXSYDYyHVy9Uxte%2ByLtlQoymdrJmhp2d1BPEyOTbVm%2B5eSVXB7fQjO6jdhS9BlhcpkdJB9ZTc1KF8%2BmY2Zq%2FzObcU3gMa7Hg7CeQyYrEUZfrWR5f64Q4Lj8jIQb10PL5s0eqtdEsEzM8w7UYah47JeI0xc7ot1fcw2NCUFd7w6fBtdx3Pdt6%2Bn9QIz0FKvqs%2F0OzcN2YHhvhQ1lDDO5Ko7FHz5FhZS9RMZsdSokbJO2oN1z1vnpJsjwXDJsShCkf1q6Xlju86em5PNf5m1gw%2FOhwYk6MyoUwzqKJvQY6pgHFBYgvSBQXuJQPk8cWTnje3HYNND4%2B3cprM1HS5zqzxyrFloL3Cm%2FVWnh6dUOOmiBGvreZNC1qjTEmp%2FdxUIStIKvaSn4x9%2F2JKuGUxUI4MJd4zWxu6WwaXLBxlYKXRiXTX39hznD3gOXwnJtpWzUcsc5GNt627zS8FitJXhWbzfSJqhrJlgUDnFUJi7E9jENh%2B35D5q%2FUC8bmmsllqA0HY2k3z9Uu&X-Amz-Signature=c163ce598b7ad94ca5fb8d8c83ee64c00de50b16178f61a6730ed23c72afd551&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OB7534E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRa92tVnjJqc3kHumVudkVBqSXUzYKPl%2FBOdv0vGGimQIgPnLybT2aWQFoTY1i7dBcCS8hrmkuwGJuiHlrxDUxuvQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI2gkyNeAh0jJ0TwiircA2TkY4ntNXXzOrtw3r6F0pstNko5FCTSMBa2raoNmywB8Gy20pnuysMYBRXhTWlSVpQzsOD95F4XQjuMRzgm2sS2aKgWNC1g%2BBE4Ioq904S70AKtyzzYkxiXWNX6c1KVDaAvKM6mchQ916g3Z4KvQScgjpZ6NJWjXvNI1C5P4qE5T5TUdLsiyuX%2Bu%2Bwl2OMKRcwgv%2Bf3OHz3%2BmxwiCvk%2FZ%2F7f8T8m83gTK1ZhBY8FkYN6Wjpn%2BiI4DYf%2BpORM3ICf3veqwLFbE8goQ%2BZ5i24z8pg6F5mWuNa5hEkhJlXV%2FB84wLGZJxCjquqK890g0%2BRHIUSOv2o7tY%2Fc0ebD41kdsvvCuiYTMTozWqrfOyRiqCTAPALbndrKGOgjmXyO4yw8yJxNDQic7oZXm5jCOAW%2BFhBFLJxLzggHnAqixeejEfHgq%2Bl5mzkilmF0DZhHyHWl0vkzefCPE8GdlJbKqmXXU854JPVAmwUhORd%2FRD9NR1SgfDu6P7vbEJv35WwyIDBvyoffzT4C60b5W3LrE1R0lDsYscXDnl31xEQJVoxipbrb2tPsd2AtqI9kDg3YFy4BINcFVKuXuwy9HB2sprVUFsQrdrPAnIcLHX3NWU7%2Bgalq80OUL0rfj7tstDpMPqgib0GOqUBU39D0V8275XgyfSZEuIf2s3mw3gydUuhZOVcGIsDYTJ%2BWSUGK1LF1OUfXiCKK9NFJwMN1CEy87l038XTlvsxwaqFak1pyoCxzghI1jejwtm3uuaHN%2Bhfdltiu6LoMIg5zuWd%2FrgtBG5hVPUQhTB7bfEjawLhSo4Dnh%2FdbphNXSYaJRxyIyG%2B7uE1eiGi57Ptc1pKilxixhEwqD%2BSor%2FLbyMF8lNu&X-Amz-Signature=36276c57b2b750548541ec04fc8ca0f262e49e59939ece31731ce367ce2d235e&X-Amz-SignedHeaders=host&x-id=GetObject)
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