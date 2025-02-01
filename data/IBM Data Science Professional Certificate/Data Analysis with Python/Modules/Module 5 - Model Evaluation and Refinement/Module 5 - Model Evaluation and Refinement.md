

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=71438edd9545bad0109e7f8094d0accb6cd6b15e2af5f4d17ff944504c292472&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=31f6fe68ab2ccfd28d16d09deb3a7fe3f23750f88ff83f8b5ae39d0e338230d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=da806507e9657480a9b21342babb88e1cbefbb2c1ecddcdac9c440c4a88b44e3&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=a4ecfd8c2d0bdc8b998a2c7f1b0a1faf64a8e2fe23c91797b517aea09f5ab0c9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=cbc5d81e5c8ab67ad8b78a3838b4332c1c2fd6d6812ef2566149959ce5e2a76a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=67c6d5dda43b679bf857dabb9ab39a779490a660fbb2cb2e58bea09fd0aafa3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=a46beadb8a2d42b345c05227c11891617d1e877040758d944bb6d98b7d5973fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=091c9a70e25922a5fe54283b9ef1d70d9e198a64f078624e696dce7c3fecaedb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=eb51223bb584850bbd6472abef603b8de16608ee98e707d856d680ec5fa07a90&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEIXPJ5J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSwv55eqJ1R0saMVTbfCAX46YV6abd2VinFoK2gZdm7gIgKHyFgiY6qbCzttf7vohpSkMylm69YTUKBD0Bu4nVPcIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BDc7BTDnJu2sDqWyrcA0Yz8zQLe%2FNQ4B39o%2FXJ5YQPMKIgoKCHHpOOvtDjZI%2BHTydQLps1j2X0TxaTAVFKT2jQxDYIuFtRcPrLEk33sDH9C7qCEJZ9cZM%2BWFQY1RoQTXcFXZgTWrbIq2oJxvz1FV3gzCEcRIDK41MSeKWvRmXfNZZONZVUB7QkeQeYzSS%2FYmiLGn%2FqbQrctk4%2BXO6WGkXV7syStSGedF5Z9FPrgAEjZ02fRbMt1WeniAiyb6%2BPBLqnkuhY5Nqa6XqsJqj6foNr%2BlU7Xej%2Fpglotfn7YqwtAI1Qc0APx2SOD524E5aPSLl48ZsxPjxzU0AhYSJUVHQDDFk6fwNbM3FfpXh%2FHtrp1wKoMBZa9vOTCr2%2BG1TK9b%2FOXxfC7Jr8PisQ9almGBfHZ%2FmEgxir30QSROF9jErM7LnlfxQxvqQKB0XKl%2Fjso5BrOORsc2kWtD%2BuYF%2BL3e%2BrQUBGCfXVJPWWPO2VOwNCOicBWVdpwLSu22%2FBVoNEvs224nGdeA70XaB0nv3IifXI6y1rdVp%2BXLZAS8rrVZ8AAAKPE%2FQTXmzREHw9zNyhxWP37EyeXhnGhTSZvbk4XxRSuQHdvJayGWjUEapv0ax%2FYUG5FMschp23LxkYAqNP0tioikUEhIhCnufqMOTs9bwGOqUBbuf9NuG0Y0kx2AW%2FU2aiT7CWlIIJkawylzpOvhhI76f80NqW0NbJVWgcdkvRrdjY%2BAZKamq5qA%2Fwg%2BfMWALzLzlOW3D89qgbyZE9HCA5MYCB%2BfVkKbdNv%2FFcRKPV3QdEUOfR5iLvYaLiIyEGj6MfAlIRlq36mC1UT2v%2BogvRpy8ExkahATf%2FD607LIWSg4ZhM5Z2SNt86pogkvafGtjE4c5Posq9&X-Amz-Signature=73a3d93d890732328ceb91980e0560ab9e1e1802ba5f0b5bffac7a3a29cb055c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEIXPJ5J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSwv55eqJ1R0saMVTbfCAX46YV6abd2VinFoK2gZdm7gIgKHyFgiY6qbCzttf7vohpSkMylm69YTUKBD0Bu4nVPcIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BDc7BTDnJu2sDqWyrcA0Yz8zQLe%2FNQ4B39o%2FXJ5YQPMKIgoKCHHpOOvtDjZI%2BHTydQLps1j2X0TxaTAVFKT2jQxDYIuFtRcPrLEk33sDH9C7qCEJZ9cZM%2BWFQY1RoQTXcFXZgTWrbIq2oJxvz1FV3gzCEcRIDK41MSeKWvRmXfNZZONZVUB7QkeQeYzSS%2FYmiLGn%2FqbQrctk4%2BXO6WGkXV7syStSGedF5Z9FPrgAEjZ02fRbMt1WeniAiyb6%2BPBLqnkuhY5Nqa6XqsJqj6foNr%2BlU7Xej%2Fpglotfn7YqwtAI1Qc0APx2SOD524E5aPSLl48ZsxPjxzU0AhYSJUVHQDDFk6fwNbM3FfpXh%2FHtrp1wKoMBZa9vOTCr2%2BG1TK9b%2FOXxfC7Jr8PisQ9almGBfHZ%2FmEgxir30QSROF9jErM7LnlfxQxvqQKB0XKl%2Fjso5BrOORsc2kWtD%2BuYF%2BL3e%2BrQUBGCfXVJPWWPO2VOwNCOicBWVdpwLSu22%2FBVoNEvs224nGdeA70XaB0nv3IifXI6y1rdVp%2BXLZAS8rrVZ8AAAKPE%2FQTXmzREHw9zNyhxWP37EyeXhnGhTSZvbk4XxRSuQHdvJayGWjUEapv0ax%2FYUG5FMschp23LxkYAqNP0tioikUEhIhCnufqMOTs9bwGOqUBbuf9NuG0Y0kx2AW%2FU2aiT7CWlIIJkawylzpOvhhI76f80NqW0NbJVWgcdkvRrdjY%2BAZKamq5qA%2Fwg%2BfMWALzLzlOW3D89qgbyZE9HCA5MYCB%2BfVkKbdNv%2FFcRKPV3QdEUOfR5iLvYaLiIyEGj6MfAlIRlq36mC1UT2v%2BogvRpy8ExkahATf%2FD607LIWSg4ZhM5Z2SNt86pogkvafGtjE4c5Posq9&X-Amz-Signature=901e45b9ac4446d7aca43793d6dc10dbebd56d7d5f94cb1cdab0339aa70b057a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEIXPJ5J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSwv55eqJ1R0saMVTbfCAX46YV6abd2VinFoK2gZdm7gIgKHyFgiY6qbCzttf7vohpSkMylm69YTUKBD0Bu4nVPcIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BDc7BTDnJu2sDqWyrcA0Yz8zQLe%2FNQ4B39o%2FXJ5YQPMKIgoKCHHpOOvtDjZI%2BHTydQLps1j2X0TxaTAVFKT2jQxDYIuFtRcPrLEk33sDH9C7qCEJZ9cZM%2BWFQY1RoQTXcFXZgTWrbIq2oJxvz1FV3gzCEcRIDK41MSeKWvRmXfNZZONZVUB7QkeQeYzSS%2FYmiLGn%2FqbQrctk4%2BXO6WGkXV7syStSGedF5Z9FPrgAEjZ02fRbMt1WeniAiyb6%2BPBLqnkuhY5Nqa6XqsJqj6foNr%2BlU7Xej%2Fpglotfn7YqwtAI1Qc0APx2SOD524E5aPSLl48ZsxPjxzU0AhYSJUVHQDDFk6fwNbM3FfpXh%2FHtrp1wKoMBZa9vOTCr2%2BG1TK9b%2FOXxfC7Jr8PisQ9almGBfHZ%2FmEgxir30QSROF9jErM7LnlfxQxvqQKB0XKl%2Fjso5BrOORsc2kWtD%2BuYF%2BL3e%2BrQUBGCfXVJPWWPO2VOwNCOicBWVdpwLSu22%2FBVoNEvs224nGdeA70XaB0nv3IifXI6y1rdVp%2BXLZAS8rrVZ8AAAKPE%2FQTXmzREHw9zNyhxWP37EyeXhnGhTSZvbk4XxRSuQHdvJayGWjUEapv0ax%2FYUG5FMschp23LxkYAqNP0tioikUEhIhCnufqMOTs9bwGOqUBbuf9NuG0Y0kx2AW%2FU2aiT7CWlIIJkawylzpOvhhI76f80NqW0NbJVWgcdkvRrdjY%2BAZKamq5qA%2Fwg%2BfMWALzLzlOW3D89qgbyZE9HCA5MYCB%2BfVkKbdNv%2FFcRKPV3QdEUOfR5iLvYaLiIyEGj6MfAlIRlq36mC1UT2v%2BogvRpy8ExkahATf%2FD607LIWSg4ZhM5Z2SNt86pogkvafGtjE4c5Posq9&X-Amz-Signature=28cd5dc33fae5512260ddaba598047b64dc099ffe569ba8b89c21ed3acda2533&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=1108941fb330383e24386ab662f33e6c3ff43609573a29b256a2d4eb6f4e51b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=2b1acce2f25000dca09a41b297c4824d89bc3d4f5b3f84b1c27b74f0038936c4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=fa877cd728abea6e903cad4018d87378f1fa7a32ccf80320fbec652e4bc45e95&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=7c34fb0a4eba0b95032a588365f795cb71a8929e094bbd094556aa2ce5d0ce3f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=b0fd0cde04907f1b8367f68215010c83337cde031b457727bf108be44d9f5ae3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVZUYK4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRakImeZkc9U6WU85NK9tz6neohG5Cpx4y4MeTSAKHkAiA%2FKwLYqTcZPDqfDK5uvlKT48VjP3DLj%2BJRpKwMcX3XTiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRAFZxFY3iKhxdCYtKtwD4QV8UW4%2B8jKkat4E92qc3jErYEq1rS6iwfzSJ%2BBmDcwvHw0XOhNdkcLJxw6wdu%2B0Cygb2keL%2FuDVsJY1DkxAvh%2FDUPwxhaRFgNwG23arq8sy6PvYH1mUv0x47W5%2B7LRMWPGA5ul0Stp%2FPp7YHBM70aER%2FgafHED0FVRUBXeXoslpVI7n%2B8ox6C2Cr5r6ej9L114SdXiehPvIfsgdjfjIR%2F9x%2B2jXINOeOhosyZm5EQNfPqanNfXuIquGHVCjsn4Gxnm0XdHrxviLq8Tfs%2F8XRFXRwPlLz8ECOuFQTJVQbqN7%2B9yQZMCRL0tTWItc9BZ8nCL2ZyYi9LnqBSitsy9Aq1S8wvENze%2FLI9X6HaTQSeX%2FyD4gdK%2Fwady17u45fHHWp7X9fn2MBdx82Oz23kMNc7kgqCxsndDUgtowngCwrEnA4fa0JF8%2BvyCe%2FLHUB1FVFlDIqf%2FRG97vc4MSKbNfgF44VAbEi1NbCRXvxhsV00mrep5loe9QgPQxZWZuW%2BvV0t%2B4QBmHDTkL1nuWbe7gsSUdESxpm4iuxasjlG2FU7fqWiGKXGOo%2FbvJNcqaS%2BNt29y5Qr7H7k7E0jUG%2BeyS2ypDCmQe%2FE%2FaJHp2rP1kec00Y46QS9gXI7nvWmMwlez1vAY6pgGphrVsyoF6MuEZMttu39EmqaOKOlSlAxP1TUxTJzAR%2B9oXBTdcGEsHG2Awd5ovYB5uRnA3mgwMbZXORwJ6mmkzBkoHpa3E%2FWrXjqQZm1q%2BxGNbdxZqeGXcekdyDVjkmbrgEylrrUcV6nxa3esQSrm0tZaxF%2BvDgQmOko8fwHk07gNbMiZAxwQFuaI%2FHVAFQkzWTBdAYaOOfvdS8p8vYcGdbhsojk9A&X-Amz-Signature=bcf9d893f03db1737cd7b115c2a10f34ac5e552de566d44110fabcf0f3a596c3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRQCKH6Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXo6pane6Ddm%2F97D2NoXWjNOVlLc9ZmW9iIM652PDxmgIgayCZ4qkqMymYyb%2Bl4YcMWB%2FvZdEacrjaf%2Fdrr5YVoy0qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAx8ThAVX7jCq%2Bx%2BfSrcAyqlpdkmnCsQa%2Fva26H6kRieAn1en4pf57c8v7K7TDtDUvGX728RyxHN4wggNXKjHTBv1JdH5K5FtyicBrZ67q3U%2BZnKj7rnR5%2B8PFwplG%2F2ajYFqjwyOz3SUQQoXjty2Prs8Ooz82aX0lZXbH1VMt1KKD0g%2F%2FkO9mv%2BQthBAODh%2FvluGBslOKJUO16R%2BlGEIXcjrjBQWrlGTS2%2BQJsvUy%2FamOmqinKSTdzDpIv1j1w07dXNRmNyo7sKvzkauBFvmle3DaFeefj0cqT6FM%2F5xuHliFJMQXCTmer82A3iZEsIof%2FJnRrEko5W%2FFcYygXX3QJmQUSAnT1Z3tiA2g13YwBmgse%2F6X8rgZm32ODl5JIyxgjrnqbJt0pr6TA6PczNwyLvsXgu8ysojFdNWYPy2QbMWTygaV4z3SpUTjEX%2BxqBPvClqhnxQ7p1vHIwsknRvafLmlYN2r1GdsQreQCxb5lJ3A0OrK1kpylGh5rwUs6zR0GIATzmnl4AM9EutG4n5MfNDoQc2qN03yipucv0J3lVhohvuhoOA2%2FCZ%2F7qlwJCZFHlxpkaz3GXvuDOxJm28U2zmlxOeyax%2FQu5NPXNXxOv5Tb9HEHBzuq6CrFodE90tmNgIMZ7EXvnQkttMJvs9bwGOqUBz6aZCxapbJkOSHmnJ1YSvUjR58uzHgqDgv1JcXwhkw1YZsQ%2BQASK382XVGlQ7uY9A4uH2DuoFKSKWyzdHY6hVJcJJGrTQpwxyHDQ1edf3LP2z5WAF9reEykA7XAXCeRFJ7QmMbm%2BEwe%2Fzonouc6Zaj1gMNXbt6TVaU7UPZQs7BE8cvzy6MPnvwEuKdBJMKLqXnm%2FivmDUxeGB1hVNYWedQSr5ieT&X-Amz-Signature=3f1bfd21f54477fe1d5def74be06b8f747a85be5afb272ebd326ca3993f13027&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRQCKH6Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXo6pane6Ddm%2F97D2NoXWjNOVlLc9ZmW9iIM652PDxmgIgayCZ4qkqMymYyb%2Bl4YcMWB%2FvZdEacrjaf%2Fdrr5YVoy0qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAx8ThAVX7jCq%2Bx%2BfSrcAyqlpdkmnCsQa%2Fva26H6kRieAn1en4pf57c8v7K7TDtDUvGX728RyxHN4wggNXKjHTBv1JdH5K5FtyicBrZ67q3U%2BZnKj7rnR5%2B8PFwplG%2F2ajYFqjwyOz3SUQQoXjty2Prs8Ooz82aX0lZXbH1VMt1KKD0g%2F%2FkO9mv%2BQthBAODh%2FvluGBslOKJUO16R%2BlGEIXcjrjBQWrlGTS2%2BQJsvUy%2FamOmqinKSTdzDpIv1j1w07dXNRmNyo7sKvzkauBFvmle3DaFeefj0cqT6FM%2F5xuHliFJMQXCTmer82A3iZEsIof%2FJnRrEko5W%2FFcYygXX3QJmQUSAnT1Z3tiA2g13YwBmgse%2F6X8rgZm32ODl5JIyxgjrnqbJt0pr6TA6PczNwyLvsXgu8ysojFdNWYPy2QbMWTygaV4z3SpUTjEX%2BxqBPvClqhnxQ7p1vHIwsknRvafLmlYN2r1GdsQreQCxb5lJ3A0OrK1kpylGh5rwUs6zR0GIATzmnl4AM9EutG4n5MfNDoQc2qN03yipucv0J3lVhohvuhoOA2%2FCZ%2F7qlwJCZFHlxpkaz3GXvuDOxJm28U2zmlxOeyax%2FQu5NPXNXxOv5Tb9HEHBzuq6CrFodE90tmNgIMZ7EXvnQkttMJvs9bwGOqUBz6aZCxapbJkOSHmnJ1YSvUjR58uzHgqDgv1JcXwhkw1YZsQ%2BQASK382XVGlQ7uY9A4uH2DuoFKSKWyzdHY6hVJcJJGrTQpwxyHDQ1edf3LP2z5WAF9reEykA7XAXCeRFJ7QmMbm%2BEwe%2Fzonouc6Zaj1gMNXbt6TVaU7UPZQs7BE8cvzy6MPnvwEuKdBJMKLqXnm%2FivmDUxeGB1hVNYWedQSr5ieT&X-Amz-Signature=46e1798fcc1b5b4206b6a51c4a59c05fd67350ab0d788d1196561dcad61be9cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTDM4NDP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAHR5NjBo%2FvgwV5eDiZ%2FX8y%2B7QSKzLYFPpQ2hLjroBh6AiA834KnYXM%2FXBz6710pg%2BODVyfs02%2BrNdnp%2BgYCmW81dyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU91LgAgnZy4CPtrGKtwDCopjM913Du%2BsLLbx5wvTAvZToHDKiqDBqHfIDchELwef0wBEMnYBGQnVy7%2FRH9U7dGYmvt3IxAYl3r%2BDEEgFxFvREhAHuXmhVtJAfhEqd0dNrzcUhdkbx596aFv6%2Ffx49v0PFssjaY7OoUNdBF9V2eizFX7btBUx6%2BHwjpGJWRHIckaIrjLavDzN4Mp0yx703g%2F0wLKl%2BHk8NY%2Fg9HJ0ffUULVF19jvgvS16zoxTqb%2BS%2F6i8LPP7NOgbj3rNTwt1eayjA6tk1PpkdTR5T3KRwACtrk8YNBRKtBwUmJotPHnVtyMEhaQj73guPIEFhTJwY%2FT6DZAeLSHu%2Bh%2F4XV96DG%2F%2FNDZp9Ww4bOxfMsXX5nOjlqZVMVA8yei4x5824eFbXZD1%2BBd1iYDZrNL99M44Wj9o9YSdilwJMZYLxxu9rpXmO3TAeBYupOtC339y5vNI3wm67MjAW337IM92tYx1V7z35714N9lHXI0rX8PRL5kLEkWWVAQX5wpepE2Io6fsgB8MRoV7Xcjw%2BBjA%2FApnDK3z4IatrWLi%2FGBO5jUBd3Yul1jKDGeAwCQVfumJNALeNpBH9rtfZuNTr1GwhpPWdPL9KSXcj%2F1hu6x8Mlq7vDxDijQaB0L84Q0BeQQwxez1vAY6pgGvtxLZXZ0KOoRMFx0qwN8l1dP%2FZYlxSrwW39QcHmO%2BU0KrM7JaO%2Bu7UpRV5xr1G%2FpRUUuS%2F4NLj2YZueO7Xxm0EWdd9%2FA5XTqSUdjyttJf6Hj07CrXKTd6noluVqJ5mmjm%2BLHcdM8tJDqm0rvuIa1UPfB3gdOGTPb%2Fwcg7Yh8X2R8OMk8XhC4UwQMk639tib6t07SLbj8Z%2FpgmM6bt%2Br0Y0liyJMGu&X-Amz-Signature=7a2133ee5550e89040dc670eb0387f57f9b2423844434f6103f9c5888c8c65d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6MI5VC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoTsdYNqgBbhf4RBKLtEcEtoSP5bE0h626ddmt8BEmZwIhAMoKxcch6ZtTVNHF6%2FOA5Fr0LI04zlhqQwb48XTW9gzXKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKiJ2QeuxAQjn%2FadQq3AMxCZv05GYC378a5dGxIOIkGEHVVJB3nRzwukZ%2BTVfFY69mu3iKMm6ZME5BgALzsefdq%2B78pctca0Lxbh%2BjtrO2OvSc2GGurBE0gvE823TFVibwW05SVVtpQkMlk7659wgDjVL3SmGX2ztGd8nEtuC8NPUc4qRaCJnIjkCubpT2X%2B3e9sRZ0Vz2LrL0o2TlcCQR8IsnWXaOef%2B5Eatxa%2FBNYQtWGKoxru5m57dP4ZqSQraa%2Bt%2Bpc0d5AUFiUOLCfBUUipW1IeURzZSvv89J73LO5i0ASwHQxdk96aw6CcX39fnrjCErSAq0qQCDpv4vakh8L03VIgqeuwNmoFntXuBZ3CkRVhlAKsKptUFu51AIESSjBkIg9%2FTlKibZvlIf%2BeVQpDPzyRUKJtSPTxHQMMmEEft5BvO4%2FChb0bwDsEz2xdCE9TiXwzIRqwEuRbz23V6lT%2BI7hBhx2AUUWfE9wVZtFVbAWfBzbCQB7nmaUzexy7nVuUsbM46vSP8sYyGfAAe%2FCkuNbFAe0w08sCdOQncJGz%2BCkQGGz2DWApoZLMyRj00tVAjgPDMXc8cQVUIDqX7Zw5Q7YRdlDH7AS1MuuJgi0gIRpMbCnQUweK29GOsKOraEbbHETdp8wmWvbjCe7PW8BjqkAfHgp%2BS4jtnqUkIfuBXRp%2BWStZvHs3TB6ilp%2BF1xlk1Q54DS77PNI%2BzH6OQOt1lHrzslFb5kozvcT7WzfgJz8lwMzEueKBMvq6slQe1o6gxZauLvzZ%2Fjom0UpY5FUGlc1fJCIbQoXc0PTwTCIfC39IaDZbvaUyKyZwUAVZi660RJ88t3M7ENz3fWIEWWInjhX90bUEi27eTVew%2FK4KJIAAf0%2Bb3G&X-Amz-Signature=946e4687b3a9e20ddb6f17c0609529888a9edf07669154c8c643a5552368923b&X-Amz-SignedHeaders=host&x-id=GetObject)
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