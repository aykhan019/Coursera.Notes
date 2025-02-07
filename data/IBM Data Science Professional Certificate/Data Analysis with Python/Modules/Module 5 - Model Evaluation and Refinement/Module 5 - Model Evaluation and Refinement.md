

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=088d4f3ce979e71c5c049093e59a8ca9c5874c49edd3aad0c6ad850f476c3260&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=0a9d590420e871328955d85a2b69ad4f94a6f66ec2783bd9c8fe9bb12e84d8df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=96f49e9db285b6669ebe59e89d0b2ec17d1ce1ac415a981c6022eb27132c839b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=ab2684f9ff84e07ad5e69270dfe0e8222038a65131925e5f24b62b7f473bf86a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=1e3a6e33ea4dba38d977b3606e8ac950cb33d5082b0bc9d755962e33b64c444b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=cdf7a84e4d66ac9b7a028eb4512d26fdb814d7c5d28eba307156ef22008a95cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=e83feac98c976a1943ae8cc2b0670da3bb4e9ead093936581c1825a4919b4425&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=963a90375e9eacc788adf81ea5a3cac5a0cdca2b3c3b1120fbdb9411060c5485&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=232459d0d3818874da0520b469ea8a338f39837ef953cd36eb7ae26b1801e9b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KTJL5UY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEKhVDZf04x4f1%2B1TswNLCgOu%2B3VKiUQDp9ySfPWXzqcAiEA7cklX%2B2d1vVItVKeUah%2BaTav%2BwOeM4tPr2YFHlO3g54q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOfSegV2ew6Kdmv5sircA%2Fl2Cw8q4qft1ivoCmlRQON7SGgtqs4hpDqJDRM43j08lk02fpxyk%2BNo47Jf7VQZE8bWXdJvyWVDcH6BrhbW3HQRe7LO46uoYaAWJSweeDu56RPvlXPWiJ4e%2F4HuyZgg2be5objx3DA7vo2V07zXpe50EIhanhMaB92FcjNDlEKBZ3gM9Wv5isc0vjEOnspACwvbdrE6c7VqZcJkO46uUxCb%2BzYHl1evMqBPHtFNyYyNs6UPWXOebyDtGkkOoBOZVkQZU7UavpEnHhKtY7UxdDAovns9m3A0lEwwZXSpC1tuuOZ%2FpGVIhHbA4%2FJOVymXhef1ktEHdi831u3yi8jfQAVjtWIcQPeGIy0sP4GZXt99cQ2bV5ShUAN6jkZu4XyaBcYnOKpdTKT0bkTCYEPkUHFOvu51raiqvUwIH%2FmkXmpYlgh%2FGF1Xs1B0%2FH1K%2FNDQtLX%2F5zwgM9v%2FiRbeatZnxRlpdbKFrL1UjJo3xziGBCz6tuiTbrvlvUgmueV2%2F%2FZntkfpkeROAtkAmXllb95wEpdvGepg2TyduqqZBBxGCRK6czciCfj8YX75H%2BWck%2FFVM7sRy1JJ6yxZ%2B8o1MM5tnvMilvF%2BaukXAOHh4Jc1PPpVEHyMzBBcKFCC0cmPMPT5lr0GOqUBIU6uzyPIsRILzp1SAqUd6CWJtZNzIHQ9SgXLbw5atcyEzuThUzgHvoimZA5swJHKjjWa%2BDJDCFk2UgblS7tCn15kxpIvKWxpLUrbdXRjScasThRlg7K76fl0XVFi6pTbgoMm23VQINL2XtLu0YM%2FwS9%2FKgrXvKBnoj7XAjUVA%2BGOLSZroPxoLDiNdoTOExWw%2BJSzI4S7%2BM3meM7mHNKHdBy%2Fe6Ul&X-Amz-Signature=a9fc050281fe5f1fa32282a5f6e9f29c4b04d8265c80feba0ca8d40b6a4ae594&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KTJL5UY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEKhVDZf04x4f1%2B1TswNLCgOu%2B3VKiUQDp9ySfPWXzqcAiEA7cklX%2B2d1vVItVKeUah%2BaTav%2BwOeM4tPr2YFHlO3g54q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOfSegV2ew6Kdmv5sircA%2Fl2Cw8q4qft1ivoCmlRQON7SGgtqs4hpDqJDRM43j08lk02fpxyk%2BNo47Jf7VQZE8bWXdJvyWVDcH6BrhbW3HQRe7LO46uoYaAWJSweeDu56RPvlXPWiJ4e%2F4HuyZgg2be5objx3DA7vo2V07zXpe50EIhanhMaB92FcjNDlEKBZ3gM9Wv5isc0vjEOnspACwvbdrE6c7VqZcJkO46uUxCb%2BzYHl1evMqBPHtFNyYyNs6UPWXOebyDtGkkOoBOZVkQZU7UavpEnHhKtY7UxdDAovns9m3A0lEwwZXSpC1tuuOZ%2FpGVIhHbA4%2FJOVymXhef1ktEHdi831u3yi8jfQAVjtWIcQPeGIy0sP4GZXt99cQ2bV5ShUAN6jkZu4XyaBcYnOKpdTKT0bkTCYEPkUHFOvu51raiqvUwIH%2FmkXmpYlgh%2FGF1Xs1B0%2FH1K%2FNDQtLX%2F5zwgM9v%2FiRbeatZnxRlpdbKFrL1UjJo3xziGBCz6tuiTbrvlvUgmueV2%2F%2FZntkfpkeROAtkAmXllb95wEpdvGepg2TyduqqZBBxGCRK6czciCfj8YX75H%2BWck%2FFVM7sRy1JJ6yxZ%2B8o1MM5tnvMilvF%2BaukXAOHh4Jc1PPpVEHyMzBBcKFCC0cmPMPT5lr0GOqUBIU6uzyPIsRILzp1SAqUd6CWJtZNzIHQ9SgXLbw5atcyEzuThUzgHvoimZA5swJHKjjWa%2BDJDCFk2UgblS7tCn15kxpIvKWxpLUrbdXRjScasThRlg7K76fl0XVFi6pTbgoMm23VQINL2XtLu0YM%2FwS9%2FKgrXvKBnoj7XAjUVA%2BGOLSZroPxoLDiNdoTOExWw%2BJSzI4S7%2BM3meM7mHNKHdBy%2Fe6Ul&X-Amz-Signature=28cfd0ae47616e51106ed1ca50a26e97fbd8ddac0c96f49781fb66538104e94c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KTJL5UY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEKhVDZf04x4f1%2B1TswNLCgOu%2B3VKiUQDp9ySfPWXzqcAiEA7cklX%2B2d1vVItVKeUah%2BaTav%2BwOeM4tPr2YFHlO3g54q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOfSegV2ew6Kdmv5sircA%2Fl2Cw8q4qft1ivoCmlRQON7SGgtqs4hpDqJDRM43j08lk02fpxyk%2BNo47Jf7VQZE8bWXdJvyWVDcH6BrhbW3HQRe7LO46uoYaAWJSweeDu56RPvlXPWiJ4e%2F4HuyZgg2be5objx3DA7vo2V07zXpe50EIhanhMaB92FcjNDlEKBZ3gM9Wv5isc0vjEOnspACwvbdrE6c7VqZcJkO46uUxCb%2BzYHl1evMqBPHtFNyYyNs6UPWXOebyDtGkkOoBOZVkQZU7UavpEnHhKtY7UxdDAovns9m3A0lEwwZXSpC1tuuOZ%2FpGVIhHbA4%2FJOVymXhef1ktEHdi831u3yi8jfQAVjtWIcQPeGIy0sP4GZXt99cQ2bV5ShUAN6jkZu4XyaBcYnOKpdTKT0bkTCYEPkUHFOvu51raiqvUwIH%2FmkXmpYlgh%2FGF1Xs1B0%2FH1K%2FNDQtLX%2F5zwgM9v%2FiRbeatZnxRlpdbKFrL1UjJo3xziGBCz6tuiTbrvlvUgmueV2%2F%2FZntkfpkeROAtkAmXllb95wEpdvGepg2TyduqqZBBxGCRK6czciCfj8YX75H%2BWck%2FFVM7sRy1JJ6yxZ%2B8o1MM5tnvMilvF%2BaukXAOHh4Jc1PPpVEHyMzBBcKFCC0cmPMPT5lr0GOqUBIU6uzyPIsRILzp1SAqUd6CWJtZNzIHQ9SgXLbw5atcyEzuThUzgHvoimZA5swJHKjjWa%2BDJDCFk2UgblS7tCn15kxpIvKWxpLUrbdXRjScasThRlg7K76fl0XVFi6pTbgoMm23VQINL2XtLu0YM%2FwS9%2FKgrXvKBnoj7XAjUVA%2BGOLSZroPxoLDiNdoTOExWw%2BJSzI4S7%2BM3meM7mHNKHdBy%2Fe6Ul&X-Amz-Signature=0aeb6ffaaab3368da2d90397e90378eca5f97adaaa19dcad11673ea182120406&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=d6df4b23563a08dd339167fd696ecd90e9595f95be7650a11cf07ef5f4ebb2a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=7fce29e1ec42e474fab6813359f54da2647c11edaace839ea4f3de4fc0e5dd51&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=81d9c15c491398210eb8c642f9d7804237aae2b45888909e20224b631228ddb3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=cfa312451c500f40ed7ec84831557aef818e958aefc6aa2a8b692ce49d172aa1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=b325ce5a8bae7ab31922ab6913a7e868ef24cedc3a34bd03140ac92c626f0a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY3XFODT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwiC1M5KJK0YiJiOQtMGoFQV5A2tc90Sj%2BjV83v0gFyAIgU1UX8gTZwa%2FySpRUtGZs0IGBdYKk7AiuAhjpv1wX6gcq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDP03JKXi1cDAZ62YoCrcA%2BUk4DdVKbV%2BF%2FSqNmzwS80FWsd06oZydCuddcrQkJA%2FdSi3OkeAmQANBCsBhM%2FjBAQgfvD0%2FCi7trzd%2BV0%2F4RvloKWju%2F1Crn%2FhuOw0GEnlAbZDqN5w9fllo587omn6t0l2e1lYmroTjD3MZh5p2dcHvsuYhR7JnTWLGkDoEZKcAl1XYErGBoMY7I4zOsMTj%2FfZdA%2FZO1CEA5nY72faeU%2BbbgXNI2Gkn%2Br35Tl23GdpWuPaymBsd6wsAeEwC%2BDt5bvCe0KCBNMWAsRfZaR%2FxEiPQp3%2BMtb840ubHln9K25ngBvOhUJqnEw4HPwthUmBAy%2B7CRcOh7p6IqVRLBKI%2FIdcwundKvQosXgo1gGIHJSptwqG84MBR82D62RulDW7EGl9yAAGNzJv7GGCvQEH68Ui0AqdIOxLRpiuNLMK5cz3V7c6up12E5xSloeHd9rSmwiSwQKv1TvVXnWcBSrFOSLwZbGnHnFtUV4O0GXiaKWcgYcFIrKrRGZv4YNx%2FxE4AAOjEXX0GvVzrr1seV7jkHw0fYdKqE0XTcJKVm0y5yPy4fsZjgh3BbAIyQ1vCUY10S37s6jMvCvV15RR3ZnwS1vgT%2F2cIS7PnBXt8o37tUUqXmeyLtEWPMURGvUKMP35lr0GOqUBLcnyOAQGR%2BXKUlTY%2BbXhWx4fC1N%2FcNSWmOZyDj0ToIC8PNdYI8EBeQ9rZPWBo27VKpihaHEMapFQMaEf6iJWZy%2Fzx74Dfo%2BtFQlFvvmlLDo4umJp%2F9WXrTIPu0GOErldrCTfBpvUeCGDk4%2BSNKqhAGdDOI4ivwpnDOcnLGAuBYwLkIsTM80Wst%2F4xkZvSCVVnIKUnikCoi1HYTYqKyCWVaMhAoE9&X-Amz-Signature=b729c23ad24870eb72f1d107a65be484801d43584b113aff12b90d04c72c3ec1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOKNXPBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDeICvFDluN%2Bp9%2FYv8OsbzQ%2BhIMUe1pyE7XW2KJR1gVfgIhAIbSxg0H5o%2F4YS5ay2MF%2FoPfy805RncTjc9qFJR41FalKv8DCHEQABoMNjM3NDIzMTgzODA1Igy%2Bx24NgPyeh3us9XYq3AP1kdlz111xzdeEIJiHy2d6IwMy9VFEgbgCdFRlDmZiIIdn6o62qNeCizfvk9czuML8CiD7roN14Ii9FlZgRBL5bPDf4TiPQOVZy%2BSzgqwbRC2LpPeB1ztBIwOvZffO%2B5lex4pZczzpKoeQ7lODUoUYF01tjBfBpXcnhIK1N6Rz%2FBGSuE2JKB31hm3oCjF1mldfprB60nMuTvAjixjipew1T14UQBTeQnrQFD7vtz8vPepGE%2BpfxIHYT8PU7kHV63CJOqTi4ffjJ3Gdt9Y2h8w2aZKS2Yc2M4mnLO8%2FXLaZQlNO1ViOFaPTcy9sJyTWzWaB5DOWPRBaHEFYYrPtdeK6864Z%2Fv5kpLJnoWCcb6%2F9vcjIK9jsqHGmGJTjwfQDf%2BZiDs0CHtvQOIp%2BZ4Xu4%2Bg9BcU71yq0s%2F%2Fv0rrbKW07GLuqJ8ZbLtj%2F29esWw1ceE0uRjnJW4N162C6SmX2enjYVTZ%2FeXHHI7j4tX4u1jhaEvUKdZE2HE5oD%2BD1gRscrIHk%2BgGmaLJXfqy3dYYTsaEmQRujd8IjuxeJnAlj8zcjhI8iRxmr2h3nPu%2FRuD2PJ%2FTQBR4OQHgju40kVneTwS9npt1arCVifBOLlL6S9PswsTQmLlVBXLObOl9QbTCA%2Bpa9BjqkARji2%2B5gIQE4ohN2vyeFfxlxVhG8BouJ%2FPMK5rlUxV3jnpXx%2F%2F4gG4QACdpIvifuOrH6f71DeSO%2FZ4Fb9hngLhuy93OWukpXOdrQ3cRvfszrUq2cdKxyripU%2FEeizTIWCOKnbuut3c3vPjJZ0EZCZPWuOGwCb6%2F7ZTXK2Z%2BRzgcwyrGY2%2Fk3A7Uwic5B6aN8QJFcXn2YU7iqIGqP1iMqI5x3i3bH&X-Amz-Signature=84252cce2575b24b273bf1733f093d1ca12f2c16e707a36b8a4e3c11194f2991&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOKNXPBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDeICvFDluN%2Bp9%2FYv8OsbzQ%2BhIMUe1pyE7XW2KJR1gVfgIhAIbSxg0H5o%2F4YS5ay2MF%2FoPfy805RncTjc9qFJR41FalKv8DCHEQABoMNjM3NDIzMTgzODA1Igy%2Bx24NgPyeh3us9XYq3AP1kdlz111xzdeEIJiHy2d6IwMy9VFEgbgCdFRlDmZiIIdn6o62qNeCizfvk9czuML8CiD7roN14Ii9FlZgRBL5bPDf4TiPQOVZy%2BSzgqwbRC2LpPeB1ztBIwOvZffO%2B5lex4pZczzpKoeQ7lODUoUYF01tjBfBpXcnhIK1N6Rz%2FBGSuE2JKB31hm3oCjF1mldfprB60nMuTvAjixjipew1T14UQBTeQnrQFD7vtz8vPepGE%2BpfxIHYT8PU7kHV63CJOqTi4ffjJ3Gdt9Y2h8w2aZKS2Yc2M4mnLO8%2FXLaZQlNO1ViOFaPTcy9sJyTWzWaB5DOWPRBaHEFYYrPtdeK6864Z%2Fv5kpLJnoWCcb6%2F9vcjIK9jsqHGmGJTjwfQDf%2BZiDs0CHtvQOIp%2BZ4Xu4%2Bg9BcU71yq0s%2F%2Fv0rrbKW07GLuqJ8ZbLtj%2F29esWw1ceE0uRjnJW4N162C6SmX2enjYVTZ%2FeXHHI7j4tX4u1jhaEvUKdZE2HE5oD%2BD1gRscrIHk%2BgGmaLJXfqy3dYYTsaEmQRujd8IjuxeJnAlj8zcjhI8iRxmr2h3nPu%2FRuD2PJ%2FTQBR4OQHgju40kVneTwS9npt1arCVifBOLlL6S9PswsTQmLlVBXLObOl9QbTCA%2Bpa9BjqkARji2%2B5gIQE4ohN2vyeFfxlxVhG8BouJ%2FPMK5rlUxV3jnpXx%2F%2F4gG4QACdpIvifuOrH6f71DeSO%2FZ4Fb9hngLhuy93OWukpXOdrQ3cRvfszrUq2cdKxyripU%2FEeizTIWCOKnbuut3c3vPjJZ0EZCZPWuOGwCb6%2F7ZTXK2Z%2BRzgcwyrGY2%2Fk3A7Uwic5B6aN8QJFcXn2YU7iqIGqP1iMqI5x3i3bH&X-Amz-Signature=45d060ba13d46b7718e4eaa719f2ef0ca4b27e6c7f5bdbf9d392b952b660a61e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ACDIICW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCOz2vKD0AGEWv3s2U%2Fx4uSqHxlYDL%2Fa49YawUuT84%2BBwIhAM7QHDbt2QhRawoiKbPjHSZzfe8k7DAiNMNlE4CAZcUFKv8DCHEQABoMNjM3NDIzMTgzODA1IgzjFinexn6vMQyfjZMq3ANhlLv8bUZsA9YgrgRCrOLQwGeR63UC%2Fa0ENmCRcP%2FRvfCtSFuXl1vzEw4fjLVEuDNBm76rcZjQveS01o8AgWQGoJYqF6U5iefdZWZiy8PNWUpAXbxys4LmtIQRFmLiNTKbk9d1VL0UzYJAMioSYQ2M67RcK9jok6qEc4OnmGUB4iXOKKwxDeFo%2F2gb7rK%2Fm8GY2r8L5TmKmE%2BMFmpmUE8lPvXbhVTpuwvMCP6TVsjcffkkYiYW90HMXzyrUL1V08rW6wrcmDAP3Kj0V0BapdxpjL48UCi8gELiRb%2FM4pG4UvNciGYDRi%2FrQ3zV3%2BoKXv%2B%2FZwfcYkrk7PYfqMziIoJTgNrKVYHg%2F9YQo5nNzvb%2B78RiMG6GqO8iCJ8hCPH%2ButAP%2Fa3CjJk7oaCEyL%2FAUhh1il%2FXs9FmVrL0LDO8elnl9u2uGPKhrVeWyZ6H7Rx9d%2Fek9NAQZ%2BhL3StIEn2gWUXOpPwGVWHLBXEJvulDGsvvcdp%2BC0k7HwEYmBj2XzMDs8sPcPGmv8kCu56pZ9swaEkuhyQfN%2Fq9mPwNU%2FCVLMHwpBPLtzLax%2Bzhrtgbchw9drLHjJTGpUG5HH09%2FhkpwsnudC6Am4XQTUfZzFuCOn%2F4%2BUigmOZ0gQfRGJ0bYTCR%2Bpa9BjqkAV36qKExRlOpCVMtrEYUd4Iy2jVCDt7IbocRQAM%2FrRWDh%2BbgrdW5V4gMU2dhUXrTLhRlUxhs%2BnpbBU%2BIh3XMu0PoGbM46visKO6PaDsnj%2BmZsoJkgdYjZDsfg3mvArE8wmsHwkzxJOLvTNmz%2BWwGMYAMYqp8PkR%2B2%2FUO5HrRBbK8CvyrF3kNQlHZd3mRBr5MDr2XAlzr%2FBX9uBw9sAzknDBASj2L&X-Amz-Signature=2539eb008bcbc6fd6ade88216e3cab0445ecd9b71d726e9f9e7c483b9cbd8924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WM74IY6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHX9vgJefuafB%2Bi8fvH4IVLez4%2BcTESi94i%2BwdP8mxFiAiA%2BiZ1He5SjFvc0KPahAfRwwxEnzMjvJQ6RO8qvD9gZMSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3bjymJSSjv0x09BbKtwD%2BbBtmC6r7D3VDrjCsvXOiysL2zBVSFO29%2BbLE4pXRetP5%2FwEts%2FE4h%2BupqD65JzajET3sRa4NqKTltyishYyn68pHDckYdxMZ%2F8MDcSAWUeCISEhI3nmVWQnlYVAQgKEw4H734w5sl9CVuJCOJr%2BD4R7vzglffe7xOUTkUdMNX7%2BYx%2BlsHs%2BgZQ90ulF4yUiq81vz%2FlMvxmzT5lM%2FyZDIkPMsEPrfAgUBSFNRSUd9DOyJkgjhVNMQj6Exo66JmMgKZyYn75a2cipFK3pLEtUQKb6n4nRUqR%2BqeXu85DLOsNOBg0kDsTQvRhc0I7yb5W3XJQDaGSuF9E%2FexQ8v%2BluwFsHBxltxmVtEUUssSHanr6hHqQXPZIz76aq7HBqPFbsPPzdusyOm4l5xT6VR3mNMwNozit7xfZ6qNyNBEsO1fI5JLqzkA%2B9kTW2JPyXmaQrVoRHSN46wTaOQCuFE4b%2FZDqlizVeiXq5u900AIk9IQFoBy25aeb0Iz6X2H19Nl9hOFyRyuYKYUgLTcRRgYuhKoSITuH0M%2B6ItS%2BkNEA7oANaGnKYVdgImV3VAkRd6DGk4jlygRMJO0jx3Zz%2Fwv0tl87WJkuVwRwXiI90jvAvHwtscbYicMmzRx11I94w7%2FqWvQY6pgEEaMKHuv7%2Fm1AoC1cfebtbdLb9%2FrAboADfZHBBRWwx8wyoHDDQKijv6KAhEyRnUHbiTHw6B25eSJp5irnIQy9%2B6Ysa905v1q%2FWa3gBCLJgo%2F5DqBNU%2FXWXH3Gv3dts%2BCADn56bfjeRjIQikOEXeyKkCB3uHhiGanuiXxR5szALzOZvH6A9y9O2hrLXsM0SxMM9mFVXblC%2F%2FRjbkX3beLv1IIMoxE%2BF&X-Amz-Signature=01661d093fc5943793ba3f13cf5be060b92655f62df72ef77bf55611282a6b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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