

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=8c51c91cf36f2449a0474916934a13a0c441d82361e0817101492f894cdc6a79&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=1081b31f7c8b159c081fe97dd6411d62b8dcbf1f808aa72b5249e5e30c14b511&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=73d6861364ad0c55ed4cc1e179c10c21440e1feda19de74d530e962b8501e79e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=599cb4a4a110e79edde3fc301870e9327cb19f1dbd46e82894cb591ae51e60a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=068257b7cee82856507d2b0ad4e3df42fe42cff2dd7c609952d75741510be80c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=75b3d82190812840429592d8ae2f35b4c6fceb4d9bf242f19b2120ecb4731f71&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=f25ad616420b357f3881e75d8e397a347eed7617ab37249d15fe603e45b5d047&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=8c29a745bc4deef295fc283f98ddfc3d62b43641c816ffb5292763f84e3ae17f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=2e57bce22e64bd63ecbb9fa79e58a57c7d91b22a89c5bc2d94cf666569531ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HHCFRGW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBxeyNeQEaDU3NvoqFVwcWrbemaOGGK1g1Z8cmbwkdj%2BAiEAwkV6liJZY7YhrxWmyTPJn6fsBX1vi3QLwLGwne7Of9wq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDALgIpEayc4efOREwSrcAwxBLIziaV3UKw%2FdYgbsN9SUrVVOVlOBELcHSQq%2Fy0nn3G1zMSBPKrK4Yv%2B6nV74NLx4dVm59oGNEfgnx%2BuBUQ2sO83S2YKYz33fYNEzFy3BelSVdfqO6CVWHlA%2BAOXlUfxEU1ZGHDFgxulI7OEF0rhNW23TQXj6dolNKR0j5mORWBql4SgV2%2B%2BIojZKr3DFvPUtXYA3sQS2R89Bx4qD4uh3DIzfCY%2FL69HIqZD9qX5DXUl%2Booeog%2FZdOqq2KB4EBMHKJ%2BaxXbTRkdW%2BfPTMBMfqUNDsG1LLqI3s5%2BxjbFJW59DEMTpMLvSy8NRLyj0OlgG%2BU7TE31QoICBj%2ByC5kNzaL8KbZb5UIHsoEh1KjvcbFx%2FITShZH2tn08EoC%2BHeWv8Jl7OSYDZbvKINH86OqI3Czw2xamuwrzJx8lV3RYMDFkTJ9XzL3nzq0zWdIoL6U9FnFYCdUf35%2F5HVbGHW8Z9aU6cd7YpKzDBto5GNhaN7PEKOR2V%2BSwFrFSCMfv2AkP4YNP0Bp%2BrCMx8AbbFcLGO9dQiXGC7pGTKHQ%2FvmiuuacYTh1AXuYBj9wlKh%2BvI8BwknwFFkDniPzYnxOZddoesqGKKTczOZqBurDrTx2WGGSIc5H8CMZqGlJbAlMJrNir0GOqUB70vji5LZMZyfKtvdUi8JDVWL0P48AE0CrC5xrnBtvPmGer9B6NIz%2BLd1zNO7uvNRo2i37ol%2B9IRnDijKHrygRXxgHDFOiGC7y%2BQeSamSGhWW0cgc08Bvp6dyxYD%2Fd6WDi9ZT%2BqAjLl8Xq0xClI2VsjaoxNemJreISLc9HIZ5zUdlsuUTl8tvZ5iOlOKFHOs5IRGgaJYj%2FQhn8Yd0y8iIm8PPXewm&X-Amz-Signature=a4c40ba8ea96327299e5d700eca5722b837fc969a4a0a2bbe269da5ee2c1c0b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HHCFRGW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBxeyNeQEaDU3NvoqFVwcWrbemaOGGK1g1Z8cmbwkdj%2BAiEAwkV6liJZY7YhrxWmyTPJn6fsBX1vi3QLwLGwne7Of9wq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDALgIpEayc4efOREwSrcAwxBLIziaV3UKw%2FdYgbsN9SUrVVOVlOBELcHSQq%2Fy0nn3G1zMSBPKrK4Yv%2B6nV74NLx4dVm59oGNEfgnx%2BuBUQ2sO83S2YKYz33fYNEzFy3BelSVdfqO6CVWHlA%2BAOXlUfxEU1ZGHDFgxulI7OEF0rhNW23TQXj6dolNKR0j5mORWBql4SgV2%2B%2BIojZKr3DFvPUtXYA3sQS2R89Bx4qD4uh3DIzfCY%2FL69HIqZD9qX5DXUl%2Booeog%2FZdOqq2KB4EBMHKJ%2BaxXbTRkdW%2BfPTMBMfqUNDsG1LLqI3s5%2BxjbFJW59DEMTpMLvSy8NRLyj0OlgG%2BU7TE31QoICBj%2ByC5kNzaL8KbZb5UIHsoEh1KjvcbFx%2FITShZH2tn08EoC%2BHeWv8Jl7OSYDZbvKINH86OqI3Czw2xamuwrzJx8lV3RYMDFkTJ9XzL3nzq0zWdIoL6U9FnFYCdUf35%2F5HVbGHW8Z9aU6cd7YpKzDBto5GNhaN7PEKOR2V%2BSwFrFSCMfv2AkP4YNP0Bp%2BrCMx8AbbFcLGO9dQiXGC7pGTKHQ%2FvmiuuacYTh1AXuYBj9wlKh%2BvI8BwknwFFkDniPzYnxOZddoesqGKKTczOZqBurDrTx2WGGSIc5H8CMZqGlJbAlMJrNir0GOqUB70vji5LZMZyfKtvdUi8JDVWL0P48AE0CrC5xrnBtvPmGer9B6NIz%2BLd1zNO7uvNRo2i37ol%2B9IRnDijKHrygRXxgHDFOiGC7y%2BQeSamSGhWW0cgc08Bvp6dyxYD%2Fd6WDi9ZT%2BqAjLl8Xq0xClI2VsjaoxNemJreISLc9HIZ5zUdlsuUTl8tvZ5iOlOKFHOs5IRGgaJYj%2FQhn8Yd0y8iIm8PPXewm&X-Amz-Signature=e0f193839a064c6d49f1e04957e2061f1e3156d5d7dd7fedd26e903091af5ebd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HHCFRGW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBxeyNeQEaDU3NvoqFVwcWrbemaOGGK1g1Z8cmbwkdj%2BAiEAwkV6liJZY7YhrxWmyTPJn6fsBX1vi3QLwLGwne7Of9wq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDALgIpEayc4efOREwSrcAwxBLIziaV3UKw%2FdYgbsN9SUrVVOVlOBELcHSQq%2Fy0nn3G1zMSBPKrK4Yv%2B6nV74NLx4dVm59oGNEfgnx%2BuBUQ2sO83S2YKYz33fYNEzFy3BelSVdfqO6CVWHlA%2BAOXlUfxEU1ZGHDFgxulI7OEF0rhNW23TQXj6dolNKR0j5mORWBql4SgV2%2B%2BIojZKr3DFvPUtXYA3sQS2R89Bx4qD4uh3DIzfCY%2FL69HIqZD9qX5DXUl%2Booeog%2FZdOqq2KB4EBMHKJ%2BaxXbTRkdW%2BfPTMBMfqUNDsG1LLqI3s5%2BxjbFJW59DEMTpMLvSy8NRLyj0OlgG%2BU7TE31QoICBj%2ByC5kNzaL8KbZb5UIHsoEh1KjvcbFx%2FITShZH2tn08EoC%2BHeWv8Jl7OSYDZbvKINH86OqI3Czw2xamuwrzJx8lV3RYMDFkTJ9XzL3nzq0zWdIoL6U9FnFYCdUf35%2F5HVbGHW8Z9aU6cd7YpKzDBto5GNhaN7PEKOR2V%2BSwFrFSCMfv2AkP4YNP0Bp%2BrCMx8AbbFcLGO9dQiXGC7pGTKHQ%2FvmiuuacYTh1AXuYBj9wlKh%2BvI8BwknwFFkDniPzYnxOZddoesqGKKTczOZqBurDrTx2WGGSIc5H8CMZqGlJbAlMJrNir0GOqUB70vji5LZMZyfKtvdUi8JDVWL0P48AE0CrC5xrnBtvPmGer9B6NIz%2BLd1zNO7uvNRo2i37ol%2B9IRnDijKHrygRXxgHDFOiGC7y%2BQeSamSGhWW0cgc08Bvp6dyxYD%2Fd6WDi9ZT%2BqAjLl8Xq0xClI2VsjaoxNemJreISLc9HIZ5zUdlsuUTl8tvZ5iOlOKFHOs5IRGgaJYj%2FQhn8Yd0y8iIm8PPXewm&X-Amz-Signature=0df799eba1e91d1920aaccb813b870d21976bac9f25c7d279bf6908616147f2d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=a0e49399eae2f77a892fe7c5fdc4feb9322d2b14946cf033d1818f36047b7931&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=4db0b83626aa77ce9f808cd9bc6695718076940f7820286fb0fcdda55c300621&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=8cfbd03e1d10854a4789dabd76f9b4619cbbe5fe38ea3861e6194d72d516f3ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=59724feeb713a6beae935daa81c0589b49f17fb66abd338088955fe81fbf2607&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=9b7ea896271ae5b53ac44870491f298aebfdea6f2ba38defa18cb12a6cd60dec&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5VDJZWS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDAPzI6zggaxWMJ2c%2Bf9MIe4bWQq2xr6o1fUrOgKt%2Fj0QIgVF9Q8KTeXZNaTRaRh7RcA9ndqirSDzyIU4JS%2BX7yt4Mq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDOlKCmN5ryFCW184cSrcAyOs9HC6n1qpBXr2fxAbo3jijx20%2FJ0rDRAn6NPXcz2AaK6jHyUL%2BrdY9AupTYHs5pHUtHjvgxz3aCPJOwJ25LXgOHcJYg8AVqV%2BZac45Bj%2BmkkNXR3O6vPIZvnDosVZaJKOKJ5AukbAkcV9JZ91mFXYRzUQH2dmUN9lsACAV8Nc7l3Z7s%2F0M%2BZHEo8hFGsTR6maZDyu65nWeqQGM%2BqOvGM9Mv6tKaI08fSV9OQ9%2FUYjnSg3YwzEfnK78oibSiWZIVWSq870T6cykHKGDHpNHCjgF04HAVP1Ar9vIJqQD9wfLHf%2FKAOVIjwrs9vDQ0JnIjm5ZSmypT35qb%2BB0C772m41JS1EvwDcUm0LEALjQmSHgNKYeIuAjgLYMe4Cp5t48SVGh%2B1L5RYUdrsEhVuUa1YWj0MvhZsjDfpjyEKYUGMr1pXV2tdsaIif3hJ6YKXtZdJUhor8GeUxaEjfpRKIfwBhohlLdm8jMcKn2YZVrQRqNbfj2XCCMnDuNnoZfEbHz0kaVmYly2t3bWfII5Wdu4M%2BonqXj%2Fs%2FpkOc3HuKDq2YIRuuCE2iyp88sV9kau3aLqyyIZLogCpm1W%2F%2FXLHnmv2t2aqccuf%2B3oaUUQBn8at%2FfBcW9Jpama5OK1tRMKHNir0GOqUBIb1%2BILDK1tQD3VSzpGjjoXeFRZ8WMf%2B5EzCAJJmYeRxVeMcYBsaM6kmM1oEhob%2Fjxj2gd0Nfq2kooRPB3wx9wdXUKiB4NkTEjPT1KhT46wjLeADpmjaHsjOTcppPJYtt0Cli76paXDxdrfjvqJq%2FZYTZo%2BJm7DpRlIK9jJdkCVaok54TPVazE5AqWYbQHt2llkKGKwfh5FGlaRBkCFH6hD7EZVdt&X-Amz-Signature=6142bd705764d4be26b581140c58ef77838c0cc2a1fa3a7528cd58cfc636a3be&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WYDOEJT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDGxPuYBvfvDSSKqX%2Ffw4lcdGk%2Fs9sBG%2FQvg6Y4NhKhSgIhANySJZypadzbsUVp3FuKd%2FwOw0A4QYqbjPptfBSa%2Fqb8Kv8DCDkQABoMNjM3NDIzMTgzODA1IgwsO5gpwqLE7WfGiQMq3AO7A6FDh%2F%2B5pIc%2FKruEBQo5tPfsN8YGJSRvOYC4TzTxAGzNgZnxcfHFkKdzOXzeEFMxNndAQzseb9ail0wayg7kvyy3ihehzX5DgDnih51vkOjekr9MKBIrHgJwACte0eVWmlc%2FumuNt1fjmngDPkYeUJEEVJf5v7znZ6k6JS%2B74X8CMfgDEfAHcmQ27eEOy11j2HxOSETJerId4743vmcu4K5rezhi1GpnVyapJT3mrmb6J1s2ja9hPcGJPhDyeakhzqhMz0qr%2BYI0AaKkyk9r%2Bly5r2K9jiRbaps%2Ftcs2bVKdTG75FBsKbwylxMtCrIekoh6aSOyKK%2FqPKv%2FEkVtE1VxTlAfMXNlFSAO5MVyesVJdf22pr4OX7h2KMPXsAe5r3GFamPUDWaC5Uq1Np7SGYWvBJgrWdKih%2BHayyqh7k6nSD9w3JcAH0bSEoNrDMa9AplPX4l%2B9yoLuvtcbq4kdaz0mPMNjtOcaLp%2B7m7b2GDTi%2BLhxWONtsngYi50%2BP5sJeyKzzFHfB1cux5bHgttQPpKzu5gmY0Us6Swafvk%2BlnV7%2FehcdEeS696vbSv24Rd5bmaul9HCx8exPHNiBh0dbdXa8klWC7sKJvMLG7aFPlSOeAAwjyB08ys1%2FTDWzYq9BjqkAa%2F3KkpzKyTuqYoTfpnhTUablZHdrHwqQ5DFLXTKkkgp92LyJ97x7iBr5RsmJsKbunnoL4ygM4AYAffSCSmuElgC7OTTRa4F9C9NKE1I9Hre6Sr4poRnJedv%2Bhv77pUTKmYnv4PhZyodBddDRG4GU2Utd6ZMoz9RFMoPUqm2%2FQfkBic3JbykPE3VM4t3ZO5ftF8V6uiLesqMm5ORQKaJFFQoBM0a&X-Amz-Signature=95ea2c7b82df80f40bb9f5551843affdc1ac0206068c507a77e5d3d25bb50bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WYDOEJT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDGxPuYBvfvDSSKqX%2Ffw4lcdGk%2Fs9sBG%2FQvg6Y4NhKhSgIhANySJZypadzbsUVp3FuKd%2FwOw0A4QYqbjPptfBSa%2Fqb8Kv8DCDkQABoMNjM3NDIzMTgzODA1IgwsO5gpwqLE7WfGiQMq3AO7A6FDh%2F%2B5pIc%2FKruEBQo5tPfsN8YGJSRvOYC4TzTxAGzNgZnxcfHFkKdzOXzeEFMxNndAQzseb9ail0wayg7kvyy3ihehzX5DgDnih51vkOjekr9MKBIrHgJwACte0eVWmlc%2FumuNt1fjmngDPkYeUJEEVJf5v7znZ6k6JS%2B74X8CMfgDEfAHcmQ27eEOy11j2HxOSETJerId4743vmcu4K5rezhi1GpnVyapJT3mrmb6J1s2ja9hPcGJPhDyeakhzqhMz0qr%2BYI0AaKkyk9r%2Bly5r2K9jiRbaps%2Ftcs2bVKdTG75FBsKbwylxMtCrIekoh6aSOyKK%2FqPKv%2FEkVtE1VxTlAfMXNlFSAO5MVyesVJdf22pr4OX7h2KMPXsAe5r3GFamPUDWaC5Uq1Np7SGYWvBJgrWdKih%2BHayyqh7k6nSD9w3JcAH0bSEoNrDMa9AplPX4l%2B9yoLuvtcbq4kdaz0mPMNjtOcaLp%2B7m7b2GDTi%2BLhxWONtsngYi50%2BP5sJeyKzzFHfB1cux5bHgttQPpKzu5gmY0Us6Swafvk%2BlnV7%2FehcdEeS696vbSv24Rd5bmaul9HCx8exPHNiBh0dbdXa8klWC7sKJvMLG7aFPlSOeAAwjyB08ys1%2FTDWzYq9BjqkAa%2F3KkpzKyTuqYoTfpnhTUablZHdrHwqQ5DFLXTKkkgp92LyJ97x7iBr5RsmJsKbunnoL4ygM4AYAffSCSmuElgC7OTTRa4F9C9NKE1I9Hre6Sr4poRnJedv%2Bhv77pUTKmYnv4PhZyodBddDRG4GU2Utd6ZMoz9RFMoPUqm2%2FQfkBic3JbykPE3VM4t3ZO5ftF8V6uiLesqMm5ORQKaJFFQoBM0a&X-Amz-Signature=a4efb49e7ce60790a7baec7992fcbdeb7eb1e7834596a959c414cb9a948bc3cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDPOV5QR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDJ0VINqNxS5YFQ4lnOPUsMt4HJO57X3Ks9uH5rDU3Z5AIhAJswpCtKVTEIPJ3S%2F1bMeZ3MX5IKLBelzKSee2NkFPmAKv8DCDkQABoMNjM3NDIzMTgzODA1IgzdgAyg9Iy24iq%2FiqIq3AMTgSha%2BFiqwQKSHby36p2S7RxIONCTLJ%2Bs1BRiqjrhF2g%2BubXIK9%2BO%2FIym8jLi0N13HSQgzgKaL3caDd%2FZrgs6HaC1qnDmHrN9PxO6DVTlnK0qLSjzZJdW6%2BFOlpWdKyqj233ekceo1JGS1gw4vqWqaPndrllUrzihs8t6w%2BTDrce%2BRPpCWh2ejxGf%2FkPBy2ImB9IcZq7bcezNgxEoZfVTyf0iMVM%2BC9bjb6FD5RzbKWtbjuEqqVk09mfIz4uaRAYpL1dm7i%2B4fZqEoOPHjqWjx%2BsEsGTX9cj0Yxmk6xWcyeJeKMtOzLqsaLGuDDV2A8LRaartBHa9A%2FWrM87wDBkNe6fLoJ0eErE3nXG2Uoi6bVKnKO9%2BGbONoQ6sPrKAJHvE1rQdEj8gq10sKrmFrAFWDpk%2BKwK3bFND1t4MglLv4zVvT8drtCn0FUQwjK5sSG%2Fo3zPz7qXJHENjm8jZ6nB5JmONr1BaoxG5ypDjcD7G8oM%2Ft93Lh1X4anZlvplJ3tmHC0r5SXndh5QQYHMyuemmXhIrVpupzqeuFX9Xd5dbxEN8eBa39Dr71Lwf%2FQuK82XpW%2FwK5a7SN%2F72BGijwf0Ff6CDOhSiweRnBWpcx9HFi9AgzV1erR08cdDGSDD7zIq9BjqkAfwizeLhFEjKsVulxv8PTdFRcY1LQvvql7szw5rUvCQ1CGd0cXi7QJVs3BDuQ1L6R379caRvMVLMgMONInp22miIauNdZiJu6c7hufZHfcCTnKULpxwvpfjl8rfRq%2BjFCEipzfSPteob%2Bln%2FIrx61DNPenLo9PGUcP8wsUTOe6NxXeHlpG56ZPxovlro9toMOCaJQujk5NS27CqPV0%2F1qe38GkOE&X-Amz-Signature=117e6f1b19024e2271cac89bd7cf672a4d3e2005ee1e745956b7261e459343f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG657N24%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9ySBCtJWMA3PUpU6vb52V57%2FoFAG3IXVE7Vy5aIHIJQIhAI0vcEhAsQVcPUbdsjbTitiVIjzmHdF5pkk1ph0AFcBtKv8DCDkQABoMNjM3NDIzMTgzODA1IgwoLxTQI2OG1B228Bwq3AM4vDw6kBD5oo13luoDUPxVfjdaXkbnWfyOp1%2BczMDYK8ajGrQvgvCTO8ZTFkaT4uS9q%2FCjEYxkQkgPANtm6GpJM4gGWgsvA5hZbFJe4FdS6kQpXH3WUMH%2FcWHagSG0KrC%2Bw9L1JBnGcC8X7CGJapsHY3lR%2FRGNsi2OBPqKv7O7PHfZG19HtGl8zCc4IMhMGNtrBCSM76nz%2BThrc3U5L142i%2BCgTNP6i%2BIgpVqlq%2FKTQ%2FBbpgTPkR3J56Ga0qlCJ9OaPBH26X4iVDjFVP80HKVZsV5vcX3WnyY3v4x%2BJFb01mBKRUgzwqDfIXfE1FgrNSUagUaUMIN1IQQtKoDmoNLEdV2D7eDOx6YUHtuzCnofu00sRncroXMNOOMzCtpuZW7PzZNJHJDebza6OYxCLtXf0YSYpGJHT8aAhEYeIb7eoPZKqwx%2B15BtQIoB%2BEDOnuaru9CvUefUMJjPeHFSeKQbdmTXhofkdNjpdUhtig44gY5tgzTupCPLriWKGaHt4XLJzrVnGbPNP%2F82PM%2FYq1wMSNkYZqDZR%2BcqcX3IQsn1wgwm7Lnf2BgFsBFJtHho8mxGylvo8tYAhBYIf1ASE00Y6BGwbjQ8OxR0jW%2BBmSWqbeI2VOq8UcbCVuz91TDVzYq9BjqkAaApfFlpDWTYDxM%2FCMq8C1bGr7RUBr1BYAfh%2BUiAY8fzz2Q8VoYxtfgVPLfmQoRaY7%2FHxw52S%2B1nDaX%2F8YzpyqZMD27z3iLMGEHbQRzVy30j5ZK6MWUVmL0xI%2F8xHTJsODHR%2FPN4hX%2FrvVeKY79JaTZTLNIQ3VSjmXhqtiQ75mSTvSmYDVs65moo25HsQdHd9BMdBpeUuiwjYDULI%2FS0we9jHWt4&X-Amz-Signature=59508734cd3eaf8e514145f9a0a3410fef0650cd86215cbea4d8eaf5a3760e9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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