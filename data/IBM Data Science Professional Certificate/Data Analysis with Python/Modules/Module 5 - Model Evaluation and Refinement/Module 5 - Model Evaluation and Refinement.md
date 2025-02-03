

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=29476592f231e4b4008284d52a1875b95d0f3cd91e2173a4422d0b461d4914bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=1d1deddb524495d7f01a2c99c57090ad197f86eb3b4f237083ff4de560a77802&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=f44bbda278ba97f7ed13c494b13bd93cd78066535022a0f473e6afff2d29aaf0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=86cc2b13a8fe6dcb24c0567ea103ed58222a6da0787e53717ab738d41f5befdd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=f898396f479a2a4ea39b7cba6044598a4b8db000eb3f8e1915b4211db794e3d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=97a98ddff6b568d445033c2948fb08cda2732b7a5ce318ed279501043b5e77ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=29810f99735e6f4e52f12eebb27af9b54a0f4029b8e6594b088b61f5aea77134&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=deaf5e7206f8d8d8fa2381898b9bbf17a3e0cc0b947c823a6edc78d7c23b64d7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=636b1bc168765603b8ac6913d36383d32ca57fd5e7b182ff59a1ad733e5d9df9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUKHSQVR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQCO2E47Tp9F3slU61kmS%2BhhbjRqoW8gTSGmbvBDRzP7%2BgIgAlEguuL62IzGFeROC0I3YVO1ujLhzF5ERsE%2BdC0RFVQq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDAjOBgw%2BLtLTrTJzSyrcA1P0jJSMaFVQz9yEsJb9gDGu6cQTvG3P%2FXtcy%2BrJjrllKsCH3cYKdpuDI3JS8OpmETqZa22btrecMk5t5%2Bozr9bYTq2mrt4qz67CcNH9aFtRSDbXxc2zAc01OP2YjfTTFiU9jjx77ap8VbEy97lsQ5yjq8a5O8NYfBHc0VFh8A9qJjbHt8Uj%2FV2nlQLly%2B1PdRpESUZc6tIxIN2ZVjTRS%2BnAqb1ds0FzjeSqvdqTld1GwXelUy2kpQDU%2FfDBZeoarFcxYZou8Y87VD3qbSSEFnZ3DmTpkUI5Oh4vAyE5jNJrHV3VSJ3HJs0gQ8xt4zh9iE1pQ3xHnFvQei1aecpK5MDZXGjPCokaOTB1xaFwzaCXpRUgAqjza%2BnabvPHiDBkIG5jX9v7%2BGPnfqnvjIer6gkr5eIbbF8x6UrvPvgQ0%2FixpC0HF1pKPFtwDunYiI5e8P4dBWCD5%2Bv0iCZGpV4uBKcE0u5m2GsR%2FGNKp7ThJpNZCW5Z2xI4fFHS7quo4BjCRA1FWwUZWqIH3PJf99VSzNDmFF%2FV35sGYq%2BKZNdK3gQWsUzVZ3lh%2BIvvL%2B6As1hcQKGdS%2Bt2yGdsX3PvgQ%2BeiuV4P5v3wMZztNTzAToshD4CvBKbpFgi30NuQK%2FiMKDmg70GOqUBc33cVdolNYIDrUJixld9ebYD9keW4pI567jCn07UYyKBeNTORlO%2FB%2BvvUE%2Ff4BvE913A9s1QuFZ1NhVh3lMQs3lP40XQgse2sOTjTjXUvF%2BxD4q4sHlzoUTp46oZwTLoXwawamo0Rr3ZfOhXFMvDZGrUe7QjxApfy4YhJJaD%2BPihELgu6zAlpfaHRYUOYMaXRik7OmvR3XzCJ7pkIgoGdkbrCH8z&X-Amz-Signature=d9936c87176c03b8e75d984c9f4a1563bdffd0040147c9290ab5a3136cddc44e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUKHSQVR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQCO2E47Tp9F3slU61kmS%2BhhbjRqoW8gTSGmbvBDRzP7%2BgIgAlEguuL62IzGFeROC0I3YVO1ujLhzF5ERsE%2BdC0RFVQq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDAjOBgw%2BLtLTrTJzSyrcA1P0jJSMaFVQz9yEsJb9gDGu6cQTvG3P%2FXtcy%2BrJjrllKsCH3cYKdpuDI3JS8OpmETqZa22btrecMk5t5%2Bozr9bYTq2mrt4qz67CcNH9aFtRSDbXxc2zAc01OP2YjfTTFiU9jjx77ap8VbEy97lsQ5yjq8a5O8NYfBHc0VFh8A9qJjbHt8Uj%2FV2nlQLly%2B1PdRpESUZc6tIxIN2ZVjTRS%2BnAqb1ds0FzjeSqvdqTld1GwXelUy2kpQDU%2FfDBZeoarFcxYZou8Y87VD3qbSSEFnZ3DmTpkUI5Oh4vAyE5jNJrHV3VSJ3HJs0gQ8xt4zh9iE1pQ3xHnFvQei1aecpK5MDZXGjPCokaOTB1xaFwzaCXpRUgAqjza%2BnabvPHiDBkIG5jX9v7%2BGPnfqnvjIer6gkr5eIbbF8x6UrvPvgQ0%2FixpC0HF1pKPFtwDunYiI5e8P4dBWCD5%2Bv0iCZGpV4uBKcE0u5m2GsR%2FGNKp7ThJpNZCW5Z2xI4fFHS7quo4BjCRA1FWwUZWqIH3PJf99VSzNDmFF%2FV35sGYq%2BKZNdK3gQWsUzVZ3lh%2BIvvL%2B6As1hcQKGdS%2Bt2yGdsX3PvgQ%2BeiuV4P5v3wMZztNTzAToshD4CvBKbpFgi30NuQK%2FiMKDmg70GOqUBc33cVdolNYIDrUJixld9ebYD9keW4pI567jCn07UYyKBeNTORlO%2FB%2BvvUE%2Ff4BvE913A9s1QuFZ1NhVh3lMQs3lP40XQgse2sOTjTjXUvF%2BxD4q4sHlzoUTp46oZwTLoXwawamo0Rr3ZfOhXFMvDZGrUe7QjxApfy4YhJJaD%2BPihELgu6zAlpfaHRYUOYMaXRik7OmvR3XzCJ7pkIgoGdkbrCH8z&X-Amz-Signature=9eb4e66fba435640f0333acfe66f8a0041e6a500e5039990ab12712acb223a53&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUKHSQVR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQCO2E47Tp9F3slU61kmS%2BhhbjRqoW8gTSGmbvBDRzP7%2BgIgAlEguuL62IzGFeROC0I3YVO1ujLhzF5ERsE%2BdC0RFVQq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDAjOBgw%2BLtLTrTJzSyrcA1P0jJSMaFVQz9yEsJb9gDGu6cQTvG3P%2FXtcy%2BrJjrllKsCH3cYKdpuDI3JS8OpmETqZa22btrecMk5t5%2Bozr9bYTq2mrt4qz67CcNH9aFtRSDbXxc2zAc01OP2YjfTTFiU9jjx77ap8VbEy97lsQ5yjq8a5O8NYfBHc0VFh8A9qJjbHt8Uj%2FV2nlQLly%2B1PdRpESUZc6tIxIN2ZVjTRS%2BnAqb1ds0FzjeSqvdqTld1GwXelUy2kpQDU%2FfDBZeoarFcxYZou8Y87VD3qbSSEFnZ3DmTpkUI5Oh4vAyE5jNJrHV3VSJ3HJs0gQ8xt4zh9iE1pQ3xHnFvQei1aecpK5MDZXGjPCokaOTB1xaFwzaCXpRUgAqjza%2BnabvPHiDBkIG5jX9v7%2BGPnfqnvjIer6gkr5eIbbF8x6UrvPvgQ0%2FixpC0HF1pKPFtwDunYiI5e8P4dBWCD5%2Bv0iCZGpV4uBKcE0u5m2GsR%2FGNKp7ThJpNZCW5Z2xI4fFHS7quo4BjCRA1FWwUZWqIH3PJf99VSzNDmFF%2FV35sGYq%2BKZNdK3gQWsUzVZ3lh%2BIvvL%2B6As1hcQKGdS%2Bt2yGdsX3PvgQ%2BeiuV4P5v3wMZztNTzAToshD4CvBKbpFgi30NuQK%2FiMKDmg70GOqUBc33cVdolNYIDrUJixld9ebYD9keW4pI567jCn07UYyKBeNTORlO%2FB%2BvvUE%2Ff4BvE913A9s1QuFZ1NhVh3lMQs3lP40XQgse2sOTjTjXUvF%2BxD4q4sHlzoUTp46oZwTLoXwawamo0Rr3ZfOhXFMvDZGrUe7QjxApfy4YhJJaD%2BPihELgu6zAlpfaHRYUOYMaXRik7OmvR3XzCJ7pkIgoGdkbrCH8z&X-Amz-Signature=42a94a53ccf4c20c694a2d2962b0d55053d7d2ed1029dfd3370a7f45f94ec182&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=1777ffc73d4d667da16060c0ed4af23df40dbe9ae7f30a3742166759cfbda411&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=0ea9a224f77974f052a0ca6d07931d4322ec58c904650bc57ace62d3c53d923c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=3d950bad988d0e00ca127c4af99942fb23c0f0b4329fd72a56e328b09e3d43bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=94edd7cd517a55725d82e9922b580fe5f206249bb96b0ecd5ed4940f75641ffe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=9632b2d87905531c8063f8c15c52c7c49bfb37949106afd711e95be400c501b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LG57EUI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIGJ5LQ%2FY2i%2FgcXiuKyvu%2FFuXJUzSeY5aejFKYcZs5gkkAiEA5RZkxuFmDHPQG0ynwM%2BiNAaGyl%2FhBxIMzrOTAD3rjzAq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDFBNnGUzLatgDCTwPSrcA%2BQ31osYPIEr8gv07ZMF%2BEi4sgRjQ2VmkiRjLaGFh2Eyqj6AhA2ErzQjHqV%2FIwjCiUTXQLnvled%2BHY8xNUh4Ac%2Fv7x4mocTNH6Hxitu82zLx0E3%2BJznKoET7FnxgXCxR1P3ROcFsATuAZc5PURpHgjJ%2FqxCrlf4wmcK3WzNFxq0qXYPB%2FKBIzbCbLX3v2EebRpBSLJJ5T8YSQJP6bul5y3sQklHxZ63ewjc9LpX0%2BfBjp%2F5qovrrLixLyibDOdn9twT683%2BnDtD%2Bs%2FV1rMLjW78adI7I87VwOwZ3543TfciX7BBXjD6qaXMv%2FlyHI%2Fk%2Bp%2FMNas1YKiPjshwtvSWcQdr3DhV5KSctEGJ6x9aTAEiwUfJrLi2XtMf%2Fr1LW1qJ0HPwkjA9WMPbS85uMPoteIOYXXqE3hec5OTWo3NIJWhkEwuuoGl72zphF0Gol21NGSgFjy7dihkhaNI8wESdVZYN%2FnQlfNzFZ635xEt8exSr4UA2DgqfHiUx3XRHxD2Fy2wWB4o7m6HKfXkQBuLuPHwjAmf6UycQLMz8djXjyb0NjH0hsUwzXaki8KO9R5h48tdiE%2FCMhr1ZJNkwRzz1ZAS%2BJRX6pxRXljHMuw2sN6wR7hJr3IfgmJkjTNY9yMNfng70GOqUBxgS29DZB%2FzuBOLGqrTnh3jNVqqRXWZC8lHTtbJGxUmcyaGE6YJeniBlR7dlG3J0OFFCFKK%2B2OJ1dRh8pjyPUS2AJd2PD4ichaJnNgQNaoZE8I8jCUStBeZ48MgoumQvafxtlzEF8n79yfkF%2FPQL9usnFvuAWber0Exu15ZR%2FQxZELGLqL9CeT1QgS781ZdK6HlDbAFtAgHSe221qZCW5UaQpOImf&X-Amz-Signature=cd0c4e8cf1333246104bc805c407381c0e723cbb523fb9ea5762cb0fe7309a63&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LXC7O7B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDPVGH8%2BdT4sBbC5jPzMIr%2BwWy%2BhYazGsk%2Fvffve1WyJQIgJIFGteAVvlya6RX8oUwunwdfY%2BPQKP%2F%2FUpfy9wPAqs4q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDFwYbbzAIE6zNEj4lCrcAxIHf3FCH1G2sEK2xb7PHKYoyUcN6YXOwZyEVqcJ%2Be13VeB7%2Bo%2Bm8GcZsM5efCMRBVtp7BftNymp9Ehyy8KtapyzkHTqPfdRTm%2B7%2F0jgDKAzS5puVnzkYo56nyxbmnzMH%2B5dodnS%2FpA2QLAUFKDjJFxfDz1C%2BDli5ohpbIMBgjO4vRTAfi3JHAlyB1DVFhrh0pnFjOtK1R%2BDIKB%2BzzNjz1rnAb1lg4ecKPcjAHzTHvOHfsolHIxG%2Btu%2Fak4wwyszPJabiu3d%2FaYgSCOeNcPs82EVoCVZ7JU37mGUJ52gKahpz3Farb7GX2W7PzW3HRTloi9Dbppv0liHtPUKBH9%2Bxfy6spfOc%2ForWiMn3DTuHDXl9sO%2By0YMGsgc9V6XH4sFQJ8q8oGuf9K5BBkPeYdX8auGut9JjIXroWMJcie2JJrWEnXlf0gl451ELnHoZkX9l7qQBoajNkAT0xQZqJzphZabAO25eodyNeQBc6VgsBisWPXdkRIbESdmxCatyrFUX%2BsWDwy7ALRRZK4UYMBoKzvCPFNC3nZ80e2R3dMcc6Q7c%2FB5NnqqzFZNQOXbK198ZxTbnBvrz8CEvkLrEjfpKkDwLhokIBhohff1wPVlnI1j2rYlWqjFNEImoJ2UML%2Fmg70GOqUB1zo%2FBEM8PO10f4U%2FltdRiGXFfkco5lOrtVN%2B760MYQpuEoGEcLWsOpznG8ymEhZBS5ApPg97Iu%2FfXF%2FKcqIXnAObmCQQux1XI6KcW%2FY7wnqTgv%2BS9E192vjz7i%2BsBr80DaEmXJYAAmZS1DaWcCbR%2Bu3YoqwJalWtOwlU1Vg3JM0RoEe5aJ%2BIPQjH7DU4Nq3M%2FFWrKwnKHbjgLuSTY1zZbQMihNAz&X-Amz-Signature=a858822cf337ebce879dd4bedc0fe308f4da1a6fcb1951920237bafc8e8b8b10&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LXC7O7B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDPVGH8%2BdT4sBbC5jPzMIr%2BwWy%2BhYazGsk%2Fvffve1WyJQIgJIFGteAVvlya6RX8oUwunwdfY%2BPQKP%2F%2FUpfy9wPAqs4q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDFwYbbzAIE6zNEj4lCrcAxIHf3FCH1G2sEK2xb7PHKYoyUcN6YXOwZyEVqcJ%2Be13VeB7%2Bo%2Bm8GcZsM5efCMRBVtp7BftNymp9Ehyy8KtapyzkHTqPfdRTm%2B7%2F0jgDKAzS5puVnzkYo56nyxbmnzMH%2B5dodnS%2FpA2QLAUFKDjJFxfDz1C%2BDli5ohpbIMBgjO4vRTAfi3JHAlyB1DVFhrh0pnFjOtK1R%2BDIKB%2BzzNjz1rnAb1lg4ecKPcjAHzTHvOHfsolHIxG%2Btu%2Fak4wwyszPJabiu3d%2FaYgSCOeNcPs82EVoCVZ7JU37mGUJ52gKahpz3Farb7GX2W7PzW3HRTloi9Dbppv0liHtPUKBH9%2Bxfy6spfOc%2ForWiMn3DTuHDXl9sO%2By0YMGsgc9V6XH4sFQJ8q8oGuf9K5BBkPeYdX8auGut9JjIXroWMJcie2JJrWEnXlf0gl451ELnHoZkX9l7qQBoajNkAT0xQZqJzphZabAO25eodyNeQBc6VgsBisWPXdkRIbESdmxCatyrFUX%2BsWDwy7ALRRZK4UYMBoKzvCPFNC3nZ80e2R3dMcc6Q7c%2FB5NnqqzFZNQOXbK198ZxTbnBvrz8CEvkLrEjfpKkDwLhokIBhohff1wPVlnI1j2rYlWqjFNEImoJ2UML%2Fmg70GOqUB1zo%2FBEM8PO10f4U%2FltdRiGXFfkco5lOrtVN%2B760MYQpuEoGEcLWsOpznG8ymEhZBS5ApPg97Iu%2FfXF%2FKcqIXnAObmCQQux1XI6KcW%2FY7wnqTgv%2BS9E192vjz7i%2BsBr80DaEmXJYAAmZS1DaWcCbR%2Bu3YoqwJalWtOwlU1Vg3JM0RoEe5aJ%2BIPQjH7DU4Nq3M%2FFWrKwnKHbjgLuSTY1zZbQMihNAz&X-Amz-Signature=bdbf0d4655241d7ea60a46e8e647a1c51a4f6502ce28a3287cbfc319abbf86c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647ELH3X3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIH8yn5dgGfQghhmZ2TqJFuPeKnJVg1UB6NxfyEZdTdkEAiEAj86tse1fJfXXbu3DNWss9VDGWGv1vlH85Jf7uuZU9T0q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDEcW8FPMm2zdfY3jSircA10iS%2FQOyYrA7DApXajj3IaLtQ2iC0Ks1wevDtzvtM9oO7QRUrLWfA%2FdbpyK33ZFdV9d7KjOZd3Auu5gfNcT01oIceV7cDOZXhy7Z%2BBBh2oE7aDtIgbaGC2GLTOQueHLXfHV9HD7W6B49WEhFyjcEQ%2ByP5c4t1LNeCm2gifVWYgukQ6J1HeKK2vr1gAnHhEelncUbcMFUiA%2BTAAjIDQax3V3HzqickWjFmQPak8t3lkAotE9BgXBZ1phAlUbUGvyy3kclM14U45V5N4vTgj1sINSjmOPKLt1MkPh4qoCFFcfgihjSQWyn3rEs0sI53bgALepoYJf%2FapAgVx252n3Ji1ql7%2FeklDKI2siSfCder5ovyQ84d8AvucwkY%2B3t9835w4txQEoDy1DLko%2F%2BIoP25S4KE6uRVEhQ7tE7ULK54ZaW5s%2FFQ%2FxkA6eCEj8Hx%2F9fKHsPvj7ATRpLUn%2B3ByzbGMDwuKyGyksbQgeNwkEATGd%2FvNF9Ct3T58kzsw2Uz97JdvITtiveJGH9N5oL41z%2BgL6Ae%2FFfRe7mqqSMWFIjxhyfSPAqpl%2FznntIr3ERf3MJVkmMAHDX5MB%2BzvcB53OQWc1YRd577svnHkvN3DpP1pdgzJX0%2Fu%2FEBDGlPe1MIHmg70GOqUBc4%2BC5DoikHtV7OQqC%2FQ7MemPxKwNLvq72V5Yx9lg7ESJa02Gsj1LCTW1SNgrOW4hyU8JWrSTPTjJXGXgco8nP0g%2FhBMm4RLLVWHEvGGnz%2F9aPJFpOkSjeg15i2TdoqOJkrr3mA%2FOQ6E%2FXXulNu6fs7hdcG73L8huXxZCEfx5n0JFN%2FUHHwks4Gs69XWxQ3UxEmt%2F5wvNHewx%2BmnuwKLGRkFvmd4r&X-Amz-Signature=b4303674fdbaf82e17e6df43ae839e67372d5637fa79251387d056e0f1ed2887&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5K26AMG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIFAyqMBwr7PxiqDQOV%2F%2Bt2tw3TSQVETD2ZRRBdlSAtc9AiEAwmejz8qJkYqNgWI87IjEA5xCkv20kB5ap5nTyURrZ1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIaqlG3fdCyn0PaOtCrcA3RFcWBl%2FabNWZVZ3RhwBwDHOJ88EmFRWIGhT5eU4muHIHX%2BdVGCiI44uC6NKQvnHpfvo1e72n30xc9U4A2jj8BfWtXx06djc7AEH4qJWppwqxiExwgtdxF2dqaWensbjfdDbHR2of%2Bq2U4Pe030Hg5U%2F4%2BjXa3Vb30iFc3yT4QRhsVJyTCzJ7M5dkPcGwbWBWlR7jbwMlCUZUlFKc7pvdSyG6qshxj63xF2hO7MJ6v59zD5rmrrXusEfpLmW5XhuIXzExAjqciFN4YNV9VPY9NaS0HYctHLwYPzLBLHOmqxgagACdafdzo8zXujTslbeyJ1yCFGLuL3YzxjJ4jI39cZvkoKmFCkIdHMzfaIeSPVQ30RIQAtirDohtAnHa2ZGCjaLeURfMksf%2Fyr%2BrUu52lviihSw8oCOOZdVbyqmP7Zb2JBhLP1sT3NtTkWByyXFIM1oVggxmJilyO1Zv3dUL4OQUaucFMj4KB0fGoLYoP8kktHTIs0E3ezf9IzQMThEsQVEn%2FUoOzdWNmG%2Bk%2F7SnDy8ySy2FO7pD%2FiZHwkyvZV%2BmSGZ1RDMwKTE7bLqv6ZSroRX%2Fno8Ff9ECSDaVWXveG5XcbEqKMC%2FWesoEBDnwreEskkTPhjTns4I%2Bt5MPflg70GOqUBlDbfyIWu8tyQD9PJ%2FcHCnE0VF8csiLEQpHTaQyhN%2BpXb78fCJeobtealfTgRsgvFM2%2Bvl0p9d9%2BHIxYZyfHF%2F60sexAyiDz0LJVHtFCrQuT2F0%2BEW%2B7Qo4WUqfffLJRtVCPv8V6JqfOfcPd%2F%2BmY5PYpVwcuCPYuYON0zGz2BxAHIyPimxrOB%2BrTcEfkqk2g5xZvtuQ2hUpVTJy6JLD%2FqUTltHBPh&X-Amz-Signature=a9e479deb79249d23d6105417189a02cdcf157f98438dfcc2149f39239e33696&X-Amz-SignedHeaders=host&x-id=GetObject)
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