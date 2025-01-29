

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=d7b57d8dd3f5d383b6cd184833d874f4fa36b5fb36c628d988d83161c3111947&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=51da1388f4948624fe4d471ef6ac734b1e6d3a45c450922eb5f26979cce18246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=f11dea0ada9aad203403fdc4a67b73e27d344d561410d510039ae63d42942061&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=0f176831c40cc583c83ac9da50976ec03eeae654613cdce69837dd5141a432cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=0af1f6dc15c0746a8ecb3b39dd532de1f4c47129db4668f2f8cd1bed3779c8ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=b3d91c40e6a2f2498935374a3238a261e2b23e304db516a92a5d571c6ba2205a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=c4ad4262a519fcb26bff7f9a5d1403058449fe829c9a819a7af3be4ad9fb2935&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=14d33e1a0038a10ece5f9af0d33728707c58f37ca8ff302a7a139be9e1b9811b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=1f6786d3c382f93c003e98029cccc3838480d6d2220cdbdb9df29af9ef0a5e55&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42PXIZB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCePbFKPD4rTMX3xpQrYsSQn4%2BGhNNEXkT1ylID12ifFAIgE8ThX7tafXxVuHisiAzJG4zKb6%2FmxcRL63FboSdw1jYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPESgAdSht86LEZYzircA2Iykz5e%2B%2BBqzyDeD%2Fnr0hfm%2B1Gh79cSxLxw7LuKUMxwW2P8Z9tNJ8tzUCK6WVqiLkLemQoook6YBflQesgcNxoksNhOyYnVOliGz3HRfoKOmQPziEDctMyMqWbLnDt%2Bx0RBt%2FLvpxDYVGygNRv0Ns7OINn%2BPIY5XnHnBsKWmjFp%2Ffrptv6sazP13Bz2O01SmhXP2yDfyP7S2bWgz6IzSbgzlj2Tet01oeqpYY%2FR508vtFW1VLLyJPgwZ3CSnJeKJp1DuPt83515p%2FdVT1A4EIZlG44g8xa6BayG6gZlMKWhe1y%2FOUG7Mo3HSP8Bl4H9kUJf8Bq6qcZtOIr2qAOLEypXIN90EF1UsecvyP4gIrTQENKpPqGB7LzlaX6KyfiwrySBihZtcIWIC36FXeU1bMAwUnYjhrkB8x1sapF9pAKqLWTV%2FJ5Fa7bjPuiSSyKgSa2lIQSk6V0j43%2FCHxHAZ1z0DrS6unrcfYKGYm8IZ7d2CQtxodmz38d6AgM18wmDblgYgnzjSK6XETOBmPOe1a6gBe4kuom8ytRVpG%2F54tO4YjnIAjHynFJBmIXbZIQbbhjhES0XNtzJx2JyxsC5uwYsHJkm0KKomEOJirfdI8PF7oMkLASnsXBFm2DuMNS65rwGOqUB1ufZf6xYrbbsAXvoGyj%2BdqYF6ydYHjvhbOt2KSgam5pGHJummu2cwqBSNdrWBUYxnIM9jMq47vrIvNHoby4peSNqPWT7sNtVtjgPuGwfpQb%2F%2BHe7q1xlgDRXeP%2FTeA9qGLF8wpwLVYpoLV%2FFbuYIw0Bscmz0W0WfmFQW6x%2FoD6eQNc1Gbasd7ZBBlG6G28grvOeGVlDSYfOV8LAjPE6ypuXCo3jb&X-Amz-Signature=7a94c4a9fda115b71ebefea9eadd0c7859a13245523df7b96600fb77dc49b445&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42PXIZB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCePbFKPD4rTMX3xpQrYsSQn4%2BGhNNEXkT1ylID12ifFAIgE8ThX7tafXxVuHisiAzJG4zKb6%2FmxcRL63FboSdw1jYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPESgAdSht86LEZYzircA2Iykz5e%2B%2BBqzyDeD%2Fnr0hfm%2B1Gh79cSxLxw7LuKUMxwW2P8Z9tNJ8tzUCK6WVqiLkLemQoook6YBflQesgcNxoksNhOyYnVOliGz3HRfoKOmQPziEDctMyMqWbLnDt%2Bx0RBt%2FLvpxDYVGygNRv0Ns7OINn%2BPIY5XnHnBsKWmjFp%2Ffrptv6sazP13Bz2O01SmhXP2yDfyP7S2bWgz6IzSbgzlj2Tet01oeqpYY%2FR508vtFW1VLLyJPgwZ3CSnJeKJp1DuPt83515p%2FdVT1A4EIZlG44g8xa6BayG6gZlMKWhe1y%2FOUG7Mo3HSP8Bl4H9kUJf8Bq6qcZtOIr2qAOLEypXIN90EF1UsecvyP4gIrTQENKpPqGB7LzlaX6KyfiwrySBihZtcIWIC36FXeU1bMAwUnYjhrkB8x1sapF9pAKqLWTV%2FJ5Fa7bjPuiSSyKgSa2lIQSk6V0j43%2FCHxHAZ1z0DrS6unrcfYKGYm8IZ7d2CQtxodmz38d6AgM18wmDblgYgnzjSK6XETOBmPOe1a6gBe4kuom8ytRVpG%2F54tO4YjnIAjHynFJBmIXbZIQbbhjhES0XNtzJx2JyxsC5uwYsHJkm0KKomEOJirfdI8PF7oMkLASnsXBFm2DuMNS65rwGOqUB1ufZf6xYrbbsAXvoGyj%2BdqYF6ydYHjvhbOt2KSgam5pGHJummu2cwqBSNdrWBUYxnIM9jMq47vrIvNHoby4peSNqPWT7sNtVtjgPuGwfpQb%2F%2BHe7q1xlgDRXeP%2FTeA9qGLF8wpwLVYpoLV%2FFbuYIw0Bscmz0W0WfmFQW6x%2FoD6eQNc1Gbasd7ZBBlG6G28grvOeGVlDSYfOV8LAjPE6ypuXCo3jb&X-Amz-Signature=c9b53408a85b8f28ff772f505374b387ee5f75ca6a4c1afee296f9c85d1a152c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42PXIZB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCePbFKPD4rTMX3xpQrYsSQn4%2BGhNNEXkT1ylID12ifFAIgE8ThX7tafXxVuHisiAzJG4zKb6%2FmxcRL63FboSdw1jYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPESgAdSht86LEZYzircA2Iykz5e%2B%2BBqzyDeD%2Fnr0hfm%2B1Gh79cSxLxw7LuKUMxwW2P8Z9tNJ8tzUCK6WVqiLkLemQoook6YBflQesgcNxoksNhOyYnVOliGz3HRfoKOmQPziEDctMyMqWbLnDt%2Bx0RBt%2FLvpxDYVGygNRv0Ns7OINn%2BPIY5XnHnBsKWmjFp%2Ffrptv6sazP13Bz2O01SmhXP2yDfyP7S2bWgz6IzSbgzlj2Tet01oeqpYY%2FR508vtFW1VLLyJPgwZ3CSnJeKJp1DuPt83515p%2FdVT1A4EIZlG44g8xa6BayG6gZlMKWhe1y%2FOUG7Mo3HSP8Bl4H9kUJf8Bq6qcZtOIr2qAOLEypXIN90EF1UsecvyP4gIrTQENKpPqGB7LzlaX6KyfiwrySBihZtcIWIC36FXeU1bMAwUnYjhrkB8x1sapF9pAKqLWTV%2FJ5Fa7bjPuiSSyKgSa2lIQSk6V0j43%2FCHxHAZ1z0DrS6unrcfYKGYm8IZ7d2CQtxodmz38d6AgM18wmDblgYgnzjSK6XETOBmPOe1a6gBe4kuom8ytRVpG%2F54tO4YjnIAjHynFJBmIXbZIQbbhjhES0XNtzJx2JyxsC5uwYsHJkm0KKomEOJirfdI8PF7oMkLASnsXBFm2DuMNS65rwGOqUB1ufZf6xYrbbsAXvoGyj%2BdqYF6ydYHjvhbOt2KSgam5pGHJummu2cwqBSNdrWBUYxnIM9jMq47vrIvNHoby4peSNqPWT7sNtVtjgPuGwfpQb%2F%2BHe7q1xlgDRXeP%2FTeA9qGLF8wpwLVYpoLV%2FFbuYIw0Bscmz0W0WfmFQW6x%2FoD6eQNc1Gbasd7ZBBlG6G28grvOeGVlDSYfOV8LAjPE6ypuXCo3jb&X-Amz-Signature=d163c650328c59a97e199f49d16a2ea78dee12842f9ca11d58195ca3218e4191&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=b02f97f3c9462a0b5ccfc3b9e249dcbca65e484e09dddc47e0f4c49d5ab70847&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=790bed90e69883327b4c00968680c0bf4811526540512b38e5ea21fba80d1450&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=4788749bedf456de35b8132658ca8db976ddb24adb938b48ab595fb798cfcc88&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=ce336129daca44da436703c81e157d48b6e06f152b0543e25f6858890e332a1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=e3608043fcc1259610f90ed2d138113d734b638603751dbec364f152bca1b2a5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGPIRHYZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDu4j9Ms2lrFmqj%2BXo2wLxQxVfWeQp6798rd%2FdJNA0ThAiBA%2BW7w5r8JcKCBIphzxBsBxqoH7nUSGFdxlpXhPZYEYyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCP0DlSou122J0ZHRKtwDxSKZJxL5fL%2BJGgPxROquKDDvU5Dv8ieCFfraDNuy9nAxTyH%2FZmQJiQbNOlJk%2F1zIs8r5VpZqDwGyBrHI6IAiWukaxCdSePc3936HPtKYsxTI8kJItX9bvaMPM%2FnoVM2piYcZzuiO9JClzO5WVpomIom%2BopNvPX7macYLk%2FLwTSCPAW7IjBFnwDOHtHpzHyFloMFIgtIoNFzuKifsJ4JSu56EkZDGVuxdl%2BTbX5g6vjaX%2BFw76EPR3JAfX25lbc9oRIIY3VabRSFcGlpviYhF1Y2ifiMFCABV28fQpdjLHro9aH8Nt6h%2BXzfvONycB4wUyhX4ZIKsL9ESSUACm0Xl5tkxKpcZh50Tv049fwBQUMpS%2BH307rUcSwWF6hKuoCeuKjInDrRMijGZryVM1OsWsTOjtNnkYJ1sw3VXKoyvdImOf2%2B31gO76UIFV%2Fd5FN0Sa6o0RybdiXykhk6xaCXUfa2k9llC7APsugnn2QAvycxaRZpJ%2Bha49S1DmJpogyq4%2FMHMEyobFCL5X6twcbrcxUoXc8tVEjJLu0A3QzaUQ9a%2BUu5JCA%2FMn%2FN0snZmnicwnyD1ZHjqwX6la%2Fn%2BLsZiAXxFUmrZHSTq29C9xc4DbSMrhRkx8oWytm3t%2F50wmrvmvAY6pgHs%2FGzLpBzXW0faTIMo5z0AOTsHnKlzBfTStUD7AOI%2FKOtKxrPZml%2BLnOe6W%2BRUrofMwcglbJi2eD7xpqER4C2qRNTEIp%2BHqlmFsA5iiA4oSW3ojLpSaI9fYPU%2Fe7krq%2FzzFP878E37%2BmYHuQkzodSQ6P0Yl%2BXfK9Tyk8DJ5K5tykq56QnPeHtCMNvuYmAuTS3SvNmE3WhU1gID34Ij9UI%2Bmy1gfW7M&X-Amz-Signature=b7e3626b1e1aaf635139bd04265e990ee515bb15751649c9505d088e74bca9e1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4GT2L7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH9M5AXcPUieDIlZXOt2bIpE6GDRzsNO2ncf6CLqDnweAiEAlD2IHAyzYSPXRoAHGP6hDWzF%2FldsTlhpNWFo%2FEpcBRIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5vdXgLpZGHxhs84yrcA0XMzU5L2A0W7W7AILj%2FNx36k7204l%2BDImucDvYfS6zw1pRBDOftHh8LATBB0TrYP4G8gsH3xdAXzzy%2B5vHSBWSHH8SKw9btCjZg0h61cUIsVDuMPHDYJdHJgYGA06BKH7RkXN2mZZqwxY9npzlcFC4AQFeAOIfrJ5SOrc9WMmEaFRZuvaTxMNaXXGQq5eqK9%2B%2Fzgr%2BTWDQCazOdamJnV%2BAI%2B2Ph9m47IkxZQbwEsp9X0QL0knLqvBl3HEdC6fLHPbc6SiUxj3hrYxkYaSuGATqHgMVunHE1Y139n7HDBtKo3eGSkxxJzMIzSWkKp8eSY5J80zaQAeI8A6jMriArhQn9f%2Bfy8SOGBdUtIQWVxXBpErEj%2FJ%2FIzK0nrdg%2BdAKamEXLTSDeAtV0wFBQ8hJkD7xRkmqKdbn%2BcSfekl6y7C2%2BqNk6PHpp7C5sexWdHfCqhjQa%2BFjHcKa39dsAYZPY%2F24EVNPix1nOGPZwhQAnH2f5jHB2jD4%2FRtDQQsyLEeSTwFsDJF8HLncYy7qi%2BZONvzYJWS2%2Bg%2B7URPhyXKIOmOR7nmkPy33e1%2FIPBAX76tWQEsrdqlB33WJ%2B41GTRp6z5UUh1G7oGP4err97ZenUkaaqYfN%2F7BjSXOwhSxNeMIe75rwGOqUB03on0i%2FApeoUOb2SPiFUEiE2s0TbAIJDvukriJGkGbDvNGfNVi0jNwGHo5FUk%2FayvwOQ0vgN7PnFEfTY4H3BxS1jc0wMwa5t%2B3G1uvENuw0AAIe2dCg3Om7pshV86nF8Dm%2BYjTDUyMu0JrPr%2B8y7Oo54HafZmtlTFuXv805xSa3knBcnRD%2BevpDbzJ98zLYeTPlVdZXf3nhbkT1qdIZj625RfX8u&X-Amz-Signature=2586b8408d784e8d2eaab9e5e3c3fd6b895f085df14185a3ab3031c21eda86a5&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4GT2L7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH9M5AXcPUieDIlZXOt2bIpE6GDRzsNO2ncf6CLqDnweAiEAlD2IHAyzYSPXRoAHGP6hDWzF%2FldsTlhpNWFo%2FEpcBRIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5vdXgLpZGHxhs84yrcA0XMzU5L2A0W7W7AILj%2FNx36k7204l%2BDImucDvYfS6zw1pRBDOftHh8LATBB0TrYP4G8gsH3xdAXzzy%2B5vHSBWSHH8SKw9btCjZg0h61cUIsVDuMPHDYJdHJgYGA06BKH7RkXN2mZZqwxY9npzlcFC4AQFeAOIfrJ5SOrc9WMmEaFRZuvaTxMNaXXGQq5eqK9%2B%2Fzgr%2BTWDQCazOdamJnV%2BAI%2B2Ph9m47IkxZQbwEsp9X0QL0knLqvBl3HEdC6fLHPbc6SiUxj3hrYxkYaSuGATqHgMVunHE1Y139n7HDBtKo3eGSkxxJzMIzSWkKp8eSY5J80zaQAeI8A6jMriArhQn9f%2Bfy8SOGBdUtIQWVxXBpErEj%2FJ%2FIzK0nrdg%2BdAKamEXLTSDeAtV0wFBQ8hJkD7xRkmqKdbn%2BcSfekl6y7C2%2BqNk6PHpp7C5sexWdHfCqhjQa%2BFjHcKa39dsAYZPY%2F24EVNPix1nOGPZwhQAnH2f5jHB2jD4%2FRtDQQsyLEeSTwFsDJF8HLncYy7qi%2BZONvzYJWS2%2Bg%2B7URPhyXKIOmOR7nmkPy33e1%2FIPBAX76tWQEsrdqlB33WJ%2B41GTRp6z5UUh1G7oGP4err97ZenUkaaqYfN%2F7BjSXOwhSxNeMIe75rwGOqUB03on0i%2FApeoUOb2SPiFUEiE2s0TbAIJDvukriJGkGbDvNGfNVi0jNwGHo5FUk%2FayvwOQ0vgN7PnFEfTY4H3BxS1jc0wMwa5t%2B3G1uvENuw0AAIe2dCg3Om7pshV86nF8Dm%2BYjTDUyMu0JrPr%2B8y7Oo54HafZmtlTFuXv805xSa3knBcnRD%2BevpDbzJ98zLYeTPlVdZXf3nhbkT1qdIZj625RfX8u&X-Amz-Signature=9d69fcf5e233a9d996787b00703f75706cdd4cc04c8fdefbc75931762b2c5f0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FT4Q52J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCbWG9yfJ2CiUFhcCw0DXwaPccjJr81uN2l1YDYKeonTQIhAK2SCG6OrGFcrbP%2FI4NiVtUN6fL7kvb8pXSFZwcrPQmnKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BU0q7ahiGor9LNnUq3AP%2FeH5jSdfYOQgCaPq269qL1FOKNCCu1%2BcB7zBXOS%2BA3YtgP02vb3S%2FJZby7P%2BZc6s8YjPmkj%2BbAdafy%2BPeLQV7vqrNbdgns98NDEWWNo8Yx%2FRDvprWZDKVV5OvzXsy9chocRrCkfTJkswO0hE2ht5nRekmwnH0G7qZrW85mBfZUF5omt2HkMcjPeLEwdSxfuEabDYACemKVLusZ%2F0Mpi3USwiqr3pwWSvHyT2kR1hHOj5LpDGJoMNtoVOMqmKy6VK9Uz8VD1x%2Bq7zufw3tRFKhalcIigtnaoeerOKkKFUdIAp3hxztpy1yA8On3S2zmAjo9PcoOsgwmgiA7weXW2XaBoZoUEqk%2BPsp%2FNxlF%2FTuUB74KSbJ3dr6msiSZMITexv8G4BWSVz9yl7mmdUlrfELJk0prKV7VPutz6sc4l2qpLhLmSUxKrLWsRGDiczFzs9ufjJk58GAYxkrwzA8R2rw3cc2ViBOsM0LTaAch7Ak7Dtzz%2FyblrdWjljJ8Dla2Ciillg1V6OSd3u43icroGD2DmHECJRAaIUdKPt0fGaqEbR3KRQyTSvUf4Hub938gsDb1JGwasV6JcfgXYrvkylMmFxX5yThORL193w8Nd4sJJCr9glBKJ7HXsaxnTDuuua8BjqkAexnYviJGZyDYtFWWFN4m70scjkwdQxYtNAl3Q%2B7REKoRcwYo4603GQ9%2FQBxyHhVNo8BDNRp%2BAYMXeq08fHzux4%2FXtmALbJWU%2FU7JVVtuubb8ekYWN3IcS5cJSiQ0MrwqY00cz80DCjyxkh8Xfjjcg7x9hGpHh0rNbvPE1wMjfLXMR349%2FDW6adul7R0qhhdTH0YwIEbgZb9H%2BdwahD1gR2AlYcw&X-Amz-Signature=6ec73de019393554f46723adc8c66bf7754db2ce72e844f0bae1e5feae490556&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466443VTRTD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCrtIiL4%2FQglM4yPKPSYCVUVoPEezMfdiQRmTHw0HxYFwIgHaVQFLDNh23SSEQzwtf%2Bm1SYdneCa3R371fzhIuUTzYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhnTxlvgaX4FNAiLircAxEsIsRZEvB4pB378jTUlHjGyFpzzTUm61KdmeZPEbKexj2iC6RiAPY4iejwxOD5XoC5xQy%2BJxbtjCDHBzz5ZAOlRnWJrLaVLglF%2BXBTQEq40jToX1EfixZjVptTZEwpiYrv2jGwFWlbrSLD7Yn4mitcHZbkQIF2LmWCGHCdrGyPggBa6u6vYjtbTrXziXgwbQDEVFyKiJ20j8cipUytoFQuDT4EsnwHft7BvbFyNRFSjWU8eiTY1pvDLt22F0Clpif0SWcULt9cFJHKjl4teyyFKYRg5BGi0M75oKbOttEMmXLsoHJbk%2BtHzZXDpAvH6%2Fd7dG%2F41K10wwG%2B98J8e%2BMBfsHNRDgtUc%2Boxj884DzuCyUsnFbs%2FxV8MXS42R%2BwS%2B3iUeXqeupxsyPuDlsext2po1KvN%2BDuw4Ad1XDtcp3xmB8O5l4VDS5IbpYadML86w93nhPnrsZBmnFJItGTAfodTw1ZEx4gA2hbetVkbU0UAYbbTTptEM2VLXLgq2guYJF3Ps7SU6b4YBNpNiGD5BG%2BYvVC3v9Mya%2B4LufdbjLltGiFRN7FyoMffB92LgmOHAy4g%2F3F95niFPx%2FIcGzrXStafMF0oeutn8n%2B2VU40x9XZbd4T0JydJ0ryiAMKK75rwGOqUBQOA%2Fy8jwZvdiD7pq8uxHvq3MTLUmv4bNltsuffPYMVRl0my48kqiXIG8t6qYHg%2Fro5OVadabPsV1LYibfc0W3rNW2qGE0NH08sFqNs1VqGmtnK3jfsu0x9h5NhLY7lu2YrflCNrl%2B5MbLzj9Flxm2f3W3nEua2gjRVxANkJDJazDGPluH1dXvDwPc4INFsQuA7OwQl8XzXCFceICBwZzbMyiKzbl&X-Amz-Signature=3d42ca628f29aafd8b346233d8819f2e17793321a8ad0cbf9040bab589e898e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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