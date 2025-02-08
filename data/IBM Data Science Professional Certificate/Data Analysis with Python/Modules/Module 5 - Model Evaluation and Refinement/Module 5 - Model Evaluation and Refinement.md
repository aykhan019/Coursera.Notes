

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=db14dabf1a99438d23a51f15b71ac86986ebad57bab9d7f440a055208abb00d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=75d0e0b5051161fc86fa16da3732f4ef2b0e4075a9e796cf71110e1eddebdae1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=d0916b4f7f4a2f03895240cc49dbb94c8c32426a020b9da9966a807746e29d1c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=0aa0b81d81e18f5cf9d0a2fc09cfc4e5d57f3517a5687e3c1e9885d127338b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=c51953e58e098417829e526ae07befbe732b67b0f73f559b23c201b21f31223a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=1133207ceaa7329d208b783e357fd9f3bc0d9ebe66122080eb45fc9d13a5c9e1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=05944dcdac4b546c3896fc87d2e0cfe51e3103ce6d17beafa24f4635a10cbd7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=812e980523919a30ff26fccc28ea11837ddd92160f44901fb72309e46096da33&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=d1d960567a67d773a733647a97b19c586d26d7d22b882e0c8c8b309a8d0e4a4a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPEGDGP7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCICUsQPzcZgVjNT%2BTODhobFQW0OCkN2o84I308sYcUbPoAiEA4zsveqMuK%2Fv6BbKd5Wckvd4vgaEYOWs3ruWrOC1S0aQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqSm77ZadUvxGSYRCrcA5PWhYZ9MMlQi2Cys46tcvjMfUZbvifaIjHLkcBmBKnFXeo4STjFB%2FUaslKKQQZ2TVm5zWwSMEZx2ZBEmhPcAtwwH8mOfa76lauENarG6vmKeSKQXeLmnd8Qg238Rf8U6d9wU58BItELk0WC0cr4UPg618evq35EZD5MKsQz0TzHK9Iy39wtVkFob4Z0gun99cn55%2FlanxQqFcX1JpqrSmtZSGRJvs9k1UEyIkvlJgp9YkSustesO5QVrvcwX4MWhRZhix7HkxVQHBgF3kp4%2BcsdQ0VXPaY2UiMZ7XkgCtzsPUq7oPaZ7PQ7TeeQgr41OD3foedeWppCycNIPcK69c3vw6k9dbgIXmHhQ7o0xx4%2FLCXw29hKjYstbeBM89WvigmPjMa3Krgfsk9p2ZauJ5t%2F6xxOkBG5GhikUxip6fkScZjLdysFrJ8dTNGP%2BpxFDFNUUZPfEkfvyj0LNXncKW3%2FxwhK4SVJVLivRfyQ0v7V0SvGe3xb4%2F%2BQnJvGF0tp4eNfFgdtCMa%2FaRt342bFBvHUFLac3TqznRlASLoLi9KnK8BcMTFlDnVrWJHdLGUiOE561%2FcTeEw39%2FJm%2FoJ%2Bbq5vqYZigSDcS0RSfnYFQy4BQbYbyXQb7lxVgDc1MK2OnL0GOqUBtypMV7Z6opK2ak2wH4dK1fFvNk%2BOU96FSnmlLwSgty6K7l2wAwdNZi0dFw3I0s8mTdqnUo1UNtNdxBQHLgXeTj4Ls%2BU9gNjd60KzQjXMizluxmpK1XVwQ%2Bzin9TRM0wkwb10kLwj7OO0O65HQ%2FkUrtm3OfjishEcBRWGbiiYH515AHX9Cd3S5dM6L%2F0XfOVpQurOFAbxPE0DEgpF114KFkhXdiru&X-Amz-Signature=91ccedfde2598a127a526cfe9aaa7b49d9356f4dda31c5b984d973e53f8a5392&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPEGDGP7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCICUsQPzcZgVjNT%2BTODhobFQW0OCkN2o84I308sYcUbPoAiEA4zsveqMuK%2Fv6BbKd5Wckvd4vgaEYOWs3ruWrOC1S0aQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqSm77ZadUvxGSYRCrcA5PWhYZ9MMlQi2Cys46tcvjMfUZbvifaIjHLkcBmBKnFXeo4STjFB%2FUaslKKQQZ2TVm5zWwSMEZx2ZBEmhPcAtwwH8mOfa76lauENarG6vmKeSKQXeLmnd8Qg238Rf8U6d9wU58BItELk0WC0cr4UPg618evq35EZD5MKsQz0TzHK9Iy39wtVkFob4Z0gun99cn55%2FlanxQqFcX1JpqrSmtZSGRJvs9k1UEyIkvlJgp9YkSustesO5QVrvcwX4MWhRZhix7HkxVQHBgF3kp4%2BcsdQ0VXPaY2UiMZ7XkgCtzsPUq7oPaZ7PQ7TeeQgr41OD3foedeWppCycNIPcK69c3vw6k9dbgIXmHhQ7o0xx4%2FLCXw29hKjYstbeBM89WvigmPjMa3Krgfsk9p2ZauJ5t%2F6xxOkBG5GhikUxip6fkScZjLdysFrJ8dTNGP%2BpxFDFNUUZPfEkfvyj0LNXncKW3%2FxwhK4SVJVLivRfyQ0v7V0SvGe3xb4%2F%2BQnJvGF0tp4eNfFgdtCMa%2FaRt342bFBvHUFLac3TqznRlASLoLi9KnK8BcMTFlDnVrWJHdLGUiOE561%2FcTeEw39%2FJm%2FoJ%2Bbq5vqYZigSDcS0RSfnYFQy4BQbYbyXQb7lxVgDc1MK2OnL0GOqUBtypMV7Z6opK2ak2wH4dK1fFvNk%2BOU96FSnmlLwSgty6K7l2wAwdNZi0dFw3I0s8mTdqnUo1UNtNdxBQHLgXeTj4Ls%2BU9gNjd60KzQjXMizluxmpK1XVwQ%2Bzin9TRM0wkwb10kLwj7OO0O65HQ%2FkUrtm3OfjishEcBRWGbiiYH515AHX9Cd3S5dM6L%2F0XfOVpQurOFAbxPE0DEgpF114KFkhXdiru&X-Amz-Signature=136b30f765e4ac5e32f24ce08c93acad9305a688306a316dfa228c30d4fb0576&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPEGDGP7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCICUsQPzcZgVjNT%2BTODhobFQW0OCkN2o84I308sYcUbPoAiEA4zsveqMuK%2Fv6BbKd5Wckvd4vgaEYOWs3ruWrOC1S0aQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqSm77ZadUvxGSYRCrcA5PWhYZ9MMlQi2Cys46tcvjMfUZbvifaIjHLkcBmBKnFXeo4STjFB%2FUaslKKQQZ2TVm5zWwSMEZx2ZBEmhPcAtwwH8mOfa76lauENarG6vmKeSKQXeLmnd8Qg238Rf8U6d9wU58BItELk0WC0cr4UPg618evq35EZD5MKsQz0TzHK9Iy39wtVkFob4Z0gun99cn55%2FlanxQqFcX1JpqrSmtZSGRJvs9k1UEyIkvlJgp9YkSustesO5QVrvcwX4MWhRZhix7HkxVQHBgF3kp4%2BcsdQ0VXPaY2UiMZ7XkgCtzsPUq7oPaZ7PQ7TeeQgr41OD3foedeWppCycNIPcK69c3vw6k9dbgIXmHhQ7o0xx4%2FLCXw29hKjYstbeBM89WvigmPjMa3Krgfsk9p2ZauJ5t%2F6xxOkBG5GhikUxip6fkScZjLdysFrJ8dTNGP%2BpxFDFNUUZPfEkfvyj0LNXncKW3%2FxwhK4SVJVLivRfyQ0v7V0SvGe3xb4%2F%2BQnJvGF0tp4eNfFgdtCMa%2FaRt342bFBvHUFLac3TqznRlASLoLi9KnK8BcMTFlDnVrWJHdLGUiOE561%2FcTeEw39%2FJm%2FoJ%2Bbq5vqYZigSDcS0RSfnYFQy4BQbYbyXQb7lxVgDc1MK2OnL0GOqUBtypMV7Z6opK2ak2wH4dK1fFvNk%2BOU96FSnmlLwSgty6K7l2wAwdNZi0dFw3I0s8mTdqnUo1UNtNdxBQHLgXeTj4Ls%2BU9gNjd60KzQjXMizluxmpK1XVwQ%2Bzin9TRM0wkwb10kLwj7OO0O65HQ%2FkUrtm3OfjishEcBRWGbiiYH515AHX9Cd3S5dM6L%2F0XfOVpQurOFAbxPE0DEgpF114KFkhXdiru&X-Amz-Signature=534372c32275e5a7e2e06ffe33f95d22c744928d1ab0131163ab21a6e3688a86&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=6ec2bc435cf5eeb2530e26a88aab5f9c0fc7e3d09d2be2041354ab98e25a6c84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=ef0ce0c763356c09a2ded880bd580d346161d7b5b25fbabe51382ce569c3e461&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=eb30f516d8dac464b79d9cc75995c1b8ef0553032e8a8956cc8b9ee0b4fb9566&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=95b0128386fca44b91b263afe2a77405fe6d74aecc83c325ce5ad2549149b57c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=395dd63f386fb4db83c79809bcb5354d4d1b7b96b382819909ac2a671d021f58&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGGWDT6O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCLQusJX4G3vVvVt0EA%2FMqGuEL5Io7f%2F0FsxEubdz2n6AIgQ1U5UpudsvCrmCUtQLFRmh1BP%2BnGkILnLNGZTAi78RQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnixNT2L%2BHm9njNfSrcAyPt%2B6UCZwCN9E1T5GOhQ8CrYqo3LtSfSYHmmXD4LnAmck1FMjWn2DI5rjECEgvKFjpFFi3AuQx%2BlNzwUeMqA%2BEUdvQzB8R5Sah9UepmGwIH1beriidA1hIjlaoNKIu97jlJLBVm5VYRdDdvshAIejUyGR6OXxo0HbpwI%2Fvj1tAWNvK5BtcrF5x%2Bq5vOwtBNUIwiusXeC4voa1PhzhgDD3JaynrbYXvmO%2B9kdPaLBOAdQyRc7uRevEJIsGTQBuISctjebKaCJCTKTfitOsP5eCzGz6hi1NlJO%2FBWVj1z%2BFDv4F4eA%2FhCOP%2BNFriOYXT8AasSczb9GafBPYHugqibZinWLU1rnrlgtaw9OPGqggH2MUsLr%2B4rcEcIWUM%2Fiegc9kHZ4%2Fouhm5sv2Z4UCjwdUj8M2%2Fc%2B%2Fv8hUQuKexuNCZYoHjBh4kOVhOoebd7NLgSdgQ0cAd%2Ft1YYqJwNAiUy9AJQ1tACqdJ0%2F10AkR76i0pmljUpPBAAss1t7ETd%2FQTiRxT5CGIMQrnEDDMvoZLIjVjsWk56JACbKX9Vih4qIZbd9EzSVJZYhsEa2lesBXnH2UG44mVTXwcAYYCEvZDxr8nB5XUBQjWrKjoSINNdIERRqA%2Fy73nME29XAoObMIuOnL0GOqUBMOEdS3KZPW02dCLl%2BSImkByUiRQSnV2vT5RJmsQfDKV2kbHg9Ymh%2BUUFZ%2FKgSTBZ8Tknvg138Ske%2FDSVjSeH4myr3hp2D%2FntsRaeqv2tpjqQhj9KwY%2F7817NgFUqEaCqiDKMesLsrL6txfGPJjO4SJlaCBGQdFJ%2BQLTseSjJFHy%2FiLDul4r8BR0kw6EYpgax135EACuw88zzHD8AdxS8h%2F56JpUy&X-Amz-Signature=5e96e53bb186abfa113228666f9f72915b976e1588833ceca4e6d5fa433bfd98&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YK7N5FB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCgWvC3vx6R7ZF08eOAhBFXtnf1qfCGHO6Q886GIUaV4QIhAL%2Bug2puxsYQwHyxVQ6kC3R6JuAOOmzMXQ6749nWE2buKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy4m5Ofk1qmGaXxRgq3AMVgrphiVDdjK0ZJCEOPagloGdLIMuo5JFuNhFmT14caym9zIjSCM6TpmHBWfOlxcC0imjfVYCEiVmzBjZ4rUTUbxFu8Fj3bv9MBf2lhSP6UkorbF2zhuFNKqcrtaQVqJeA7cxU4Roco4NQvFK%2BVUoCZl%2BmlLF%2BhDyOPjUBs3D2gqg0ffM%2FeRXEcyAv321Uf18uo0fzaE8rMHlEJ1XHwtxsSN%2FAvAuAlb6XDUPa%2FUc14rwPOt3GJQn2TCXYFJ9WZWc51osGuowKwvCz%2B%2FOc%2BjSKAsvPvx8%2B1Qs7CMDYW82HxbrPwpRw5xi3L461l4NHwTQuSD6p3TOsHsG%2BTTec%2BwT9Z5bgjAXXF1sgppIFLGKndXqJRKghc1%2Bvm%2FGNHTB9%2BhOFkp%2Ffxw%2Fb6F8HA%2BkfMzybzFh6VID%2FV%2B0kStGAEF%2BcMXMaa4dFH%2F0k5JS1uKuorIpXpYMttBv2YRnsgalODGWJHxLWqcyf%2BUTSt47gYHIU8OB9wC7GKxNDOyA6bVBir2MpQ5Y0V2r7QfqRS%2BTI%2F2JHBGCI9SZHoyoiX2Zk179wMKzFd2aK5%2Bc%2F9zaWkK0jntE3p8szsWgt4r68LFmVvEeKsHeqhtj%2BB0IDjYgEQ5C3H%2BZPccb%2Bowce5aY3PzDsjZy9BjqkAW88MTVwucInVrEJsuNCok7rtd790HgovXpGSdSd0m5SmzUcNExsy3kbe1KyjNj7Dj%2BrcVXSLyk%2BFFvWnxNiKXP%2F8l16tg5Ae%2BCEx7jN4Zg9qk7e5Elf7Wuh6jAsTjO8TbBZsNLU1QEUp1oqwxZmMv3vtyeld5NfiCwaEIfLZG7RLG8I4sifeFxgsuRvVaWKAgGL3bLUullfgqvMoz9nQoqlziaA&X-Amz-Signature=f66d86767f8e2bf057d12157abfa845bd5eb090b6ed0d89cfbbfdce75dd2444c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YK7N5FB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCgWvC3vx6R7ZF08eOAhBFXtnf1qfCGHO6Q886GIUaV4QIhAL%2Bug2puxsYQwHyxVQ6kC3R6JuAOOmzMXQ6749nWE2buKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy4m5Ofk1qmGaXxRgq3AMVgrphiVDdjK0ZJCEOPagloGdLIMuo5JFuNhFmT14caym9zIjSCM6TpmHBWfOlxcC0imjfVYCEiVmzBjZ4rUTUbxFu8Fj3bv9MBf2lhSP6UkorbF2zhuFNKqcrtaQVqJeA7cxU4Roco4NQvFK%2BVUoCZl%2BmlLF%2BhDyOPjUBs3D2gqg0ffM%2FeRXEcyAv321Uf18uo0fzaE8rMHlEJ1XHwtxsSN%2FAvAuAlb6XDUPa%2FUc14rwPOt3GJQn2TCXYFJ9WZWc51osGuowKwvCz%2B%2FOc%2BjSKAsvPvx8%2B1Qs7CMDYW82HxbrPwpRw5xi3L461l4NHwTQuSD6p3TOsHsG%2BTTec%2BwT9Z5bgjAXXF1sgppIFLGKndXqJRKghc1%2Bvm%2FGNHTB9%2BhOFkp%2Ffxw%2Fb6F8HA%2BkfMzybzFh6VID%2FV%2B0kStGAEF%2BcMXMaa4dFH%2F0k5JS1uKuorIpXpYMttBv2YRnsgalODGWJHxLWqcyf%2BUTSt47gYHIU8OB9wC7GKxNDOyA6bVBir2MpQ5Y0V2r7QfqRS%2BTI%2F2JHBGCI9SZHoyoiX2Zk179wMKzFd2aK5%2Bc%2F9zaWkK0jntE3p8szsWgt4r68LFmVvEeKsHeqhtj%2BB0IDjYgEQ5C3H%2BZPccb%2Bowce5aY3PzDsjZy9BjqkAW88MTVwucInVrEJsuNCok7rtd790HgovXpGSdSd0m5SmzUcNExsy3kbe1KyjNj7Dj%2BrcVXSLyk%2BFFvWnxNiKXP%2F8l16tg5Ae%2BCEx7jN4Zg9qk7e5Elf7Wuh6jAsTjO8TbBZsNLU1QEUp1oqwxZmMv3vtyeld5NfiCwaEIfLZG7RLG8I4sifeFxgsuRvVaWKAgGL3bLUullfgqvMoz9nQoqlziaA&X-Amz-Signature=e947aae188fce2d0bd8d4f6c4b9eb10113d2637d4b440280d0992cb68faf1d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466774S4YYK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDo1ojaAw3y01POuGbKJow0O63FZpwrIKAsGZuCsn5G7QIgfqbP7DjFHjBEF7O%2BHxRDIRsEUyQp0r4le%2FxnPgD3BisqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOf1ksn65CXr9InaYSrcAyYTDMt6uLW2AdvkXic2P%2FmLbSh8uv8rgl%2Fk5q7tMXj71epVmQ1P8dUfzoowDi9C4mdzVpwQAp30f0tdh7Nsbt15sk4hWu%2BfUYC%2BFGYxh8n%2Bfim7OaTKer3B09mnvzj5bpBhhx4x8jJIU%2FXEHmtRaUopWscOW9RjGxmf9AJ9JrA2KI7uNsOur0T71SoXqPOdIGwXsUKzCMuoXGni9hvsROCsOY4HsaRnEEJ%2BSUoUD4Od6xT0eiacSv%2FX9g7JjpgcTvuf2hlVQ9vNQPEKnLtV1%2BnmEqyTcx%2FoOW%2BML7nwoIK3nUgpnZvYAH329LwfbQJ7rgZ4Jt1esG56qgnxrr5f9UFMe6io%2F5Nurk1RKXGpFQhvnPRjVxTFcKEuUe%2FvtBeOH4r53gA2jXX%2FvcNM1IOhxPrLgGYYI5U7RHLqw1PW7DFl7WM%2B1rBdxkLiJIGgobkd0yz9lIidFdhuiftG6knOuer6JBYN%2FlVgtvaw8LBLQp4%2FhJKq7EYvkYswq9X%2FUfCbVYO1Zg%2FopIQXssRTi5UAzgYGR8TlTAxYZ8YgwmFwmmE2iC8OTAFY5q6szvyvKvWhdhLvqnlKsa11fNYSjRaW6CpUqMM0%2B4pQ92g%2Fsc%2FqsrwNes0L3ex2Itqga1UQMMSOnL0GOqUBABb21drF8gLgmKJTCArsG61%2FUlHZvE2lMexOSwmOpTylsWxaBHL39ua8okwGXN0WEbtEuj%2Ff7ZgWflWxkvSCuti5nfE4G0WilVcVjNHIUZKhTmd%2B3xfyITwcJa%2BFxBJqwRyReZbBo7KvI7U5CAPSFR2CKXOl6F%2Fxv8dxQ5DYiJn9N8FYuARtJYkXGo%2B7A1U%2BjWyh%2B6aQGROdg4L5Q9x%2BQJdbvi0l&X-Amz-Signature=b19f270a28ab29664aacbd63a83b3ca90843bcc6b5e1073b6b66d881725f0b7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2GROYBP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCAdlSUBB4JHHHH66apQmu0Dm3xRuSM%2BWdruessNiHHeAIgXND%2FbzpwJs9HlrifD32QJPWvfVCB988OE5IrHXeuUkMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTs%2Fm9nBN38lOuJ6SrcA%2FM7U68zyFWvStumERFD%2FQGNM1xjcFjXkbFj4Z4XmVPF%2FAoQ%2FJeOE%2FOma9s0pK5cWT4EE75Xmw7d1D4NtoOIGrzONUsXuTsadSEWo221Muh6pp4w4L%2FylCGU%2BvLtyf8w9J1hIdp3UHpalrY8mfSaPgfbry6KAHPv6hMLsaQbxPk4Y1x9EYM6dYLVp71%2FxRPb9S97RNupsmeoggW5h%2BQ0Owx5C%2FE63ElhoU6nwrt5MrVNtW2t2Wfh%2BCCgoAas7c57KbByKIdCXfgZNjgSV2lz4HhXY3EXo3O3EMva3wZlIGyYzT6A6r4uPidtCLmvtCFZjo98R6KF2%2B26VlwSPeTXK1LpOulhBOQ24cI3gKunGrrKiOKKGxtER0GhpS46S6T4ChMUv32S0CnNL2Xu7P1ZW2bHJxUbBipU2eeoN4NG9iVqOowIkAKHQd5B%2BZnmJBzZxTHBTP2LltYKQwhUu%2F9POoEo3ydO27sEJgrca672tHzqIS0YDqR%2BXNq1dzhCOMebm3MAmQEgaAI3Zh%2FKhJSmbigQAmzV4qWPc%2BlVHYq6PY6DWWZqSzNI%2FlnP415hP%2FUi82j%2FLHXVj4RBL4e6%2BsB%2B0vbz668cje%2FVkTpprUS%2F2op%2B7kir5f%2B5Ae8HYIpLMImOnL0GOqUBK50SfBcC5u9PDCQ9WlbiCKDNTk2QJcDg%2Fxck62Qxt7Gi3Pv4ZpSo63gWVxMe5anYvb6FWdz5hJJydmQJBRqo%2BDySKlIJq3192dQrPOsI3YWYT%2F3iU3NJvC8yiyEamoBQh5cxo5rp5lcsw7G8pqYOQ8mZwtwnka2dp68O8250AMpX3%2FjYVZzi3oimrq0aZzJaNPlgdXfU1ULMR%2BXi6KwGX%2FI11nod&X-Amz-Signature=c8bd33739dd666f3b36b45f0ed2ae8a0d503f4353f7076e1a7f7389b282921eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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