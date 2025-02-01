

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=40c0f0eb6172ee52df15c9b3680e16f418d69a4f899f36cdd43aa97144dac904&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=d8d74ccaec89c9e532f081030dedf7750895bb6a86f9fc22d723297463d9ff79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=24162c0f9d9f542f3907a1f9d7e7f5894e94b01ddd9567fe1ce91ee7a89a24f1&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=d5b04b9d64df389e3b734e6332fbb8a5e9db9b7a633bbff55abb81ea1518391e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=216529d4f00780f6c8db19730aa69805f50d1215d8c39ef4f059c34a089efa0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=4c6c6acc6346892d8e56e63983a6444da027fde9a5e00791e063b3a8b4f6d107&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=b49ea260ea6663ed631f59aa8cd53a492a34ea38caae791d43f36397667b791d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=5218afe91c0f6083683eafa58b3207eab0c60d82adf9e334b2f1ca8a5af777e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=be9b1998edeab1f4b66116147db0684552065963395e934204f0b6b8f0f960e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SINAS2S%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2NpM9tSuYzhj0AhfGOnWruS8umArfpGzEGgqfbk85%2BQIhAK9R2fIybSyPAO4JUVpcDqdlKAO%2Bt%2BsQvw7FbzilzsP%2BKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVFInua8SFmAZi6coq3AMvQNMLYKbV4nynfrBeMWl6cu0EZ4v3J8n7FixlE5BLub3Y8UrspV48qmfS%2F85KbXJfXF8LjK0KC%2FHFsrJIInDmAtnIrwF2zPNvUhrTXw3uR%2Fa8cZXsxPXW18Se9dgyDhPanb29NGebWQDu%2Bm04reSBIPqUoyoYdUMGKtRnaW%2FeIkrWTU7G9hZAtijW43cjsyhhIeOl11j9IzKE7sssIqJcSVYgn6Y%2F08OJsisRM3%2BrsuG6w4EjjUfsCVTv9ItxY%2FSJV5ih3uk%2F5YfR8SQv992E0LoJen%2BkQsOKReT5vmy%2Fxd%2BFEHCMFgFf17sTdcYzG6o4i2rA58RkdcuajgAYOfNLjmKsexCS2K8H6e9KQQXVuGesZF4h7dCR%2FrBjrs7AAM4eZqx170ybfnoOImXP3PgN8rovEw61vFa9yE7uJbN2Ykmp7EmYYI3d7Z5p96vIE8JlH%2FyHWB3%2Fjpkq6W0hCyz%2FDwX9dGzI%2FqBjjb5pybXODPRwNig%2F6lToUS7W3eK5XlIoBlEEVgjhz%2Bppza0yp37Sm50c%2BPLnVKac5VT3GgCz8Dja7orROE%2BS86KBKMIADw6%2Fk2Ta3kBfQd13ZibCXlmlPIgq%2BEAr1nkZGDFx7c9Qdaev70wn58dQ38S7mTCpsfq8BjqkAaJg9QeK19vEWB%2FrVYQ3n8gBsDczvKNl5coI63YhOeynBy3aGGDF87Be95sq7hEi9nXrF1qPoHVJ0SltD6BWRyEnnuFn6rwswEDFsiK6caAhqwhgXmt8D5E%2B4QJlIyiRLmpo0Sm6MrHqfkoJy2B7M7BrcUJ9YudNGmww%2F%2FVV%2BijMwOs5EwehEs5Ep5uKQbdO5GEPruU8q6yfKSWii3PGN68PsaRJ&X-Amz-Signature=cc1c686a6ebd5db8efba3c629af281f665ec5f0426e3d1151ecbd5ead3862727&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SINAS2S%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2NpM9tSuYzhj0AhfGOnWruS8umArfpGzEGgqfbk85%2BQIhAK9R2fIybSyPAO4JUVpcDqdlKAO%2Bt%2BsQvw7FbzilzsP%2BKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVFInua8SFmAZi6coq3AMvQNMLYKbV4nynfrBeMWl6cu0EZ4v3J8n7FixlE5BLub3Y8UrspV48qmfS%2F85KbXJfXF8LjK0KC%2FHFsrJIInDmAtnIrwF2zPNvUhrTXw3uR%2Fa8cZXsxPXW18Se9dgyDhPanb29NGebWQDu%2Bm04reSBIPqUoyoYdUMGKtRnaW%2FeIkrWTU7G9hZAtijW43cjsyhhIeOl11j9IzKE7sssIqJcSVYgn6Y%2F08OJsisRM3%2BrsuG6w4EjjUfsCVTv9ItxY%2FSJV5ih3uk%2F5YfR8SQv992E0LoJen%2BkQsOKReT5vmy%2Fxd%2BFEHCMFgFf17sTdcYzG6o4i2rA58RkdcuajgAYOfNLjmKsexCS2K8H6e9KQQXVuGesZF4h7dCR%2FrBjrs7AAM4eZqx170ybfnoOImXP3PgN8rovEw61vFa9yE7uJbN2Ykmp7EmYYI3d7Z5p96vIE8JlH%2FyHWB3%2Fjpkq6W0hCyz%2FDwX9dGzI%2FqBjjb5pybXODPRwNig%2F6lToUS7W3eK5XlIoBlEEVgjhz%2Bppza0yp37Sm50c%2BPLnVKac5VT3GgCz8Dja7orROE%2BS86KBKMIADw6%2Fk2Ta3kBfQd13ZibCXlmlPIgq%2BEAr1nkZGDFx7c9Qdaev70wn58dQ38S7mTCpsfq8BjqkAaJg9QeK19vEWB%2FrVYQ3n8gBsDczvKNl5coI63YhOeynBy3aGGDF87Be95sq7hEi9nXrF1qPoHVJ0SltD6BWRyEnnuFn6rwswEDFsiK6caAhqwhgXmt8D5E%2B4QJlIyiRLmpo0Sm6MrHqfkoJy2B7M7BrcUJ9YudNGmww%2F%2FVV%2BijMwOs5EwehEs5Ep5uKQbdO5GEPruU8q6yfKSWii3PGN68PsaRJ&X-Amz-Signature=d3525be1c9df34e8ea019e9ccc5a54f8a922a661b2c270f3473e970adef3f568&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SINAS2S%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2NpM9tSuYzhj0AhfGOnWruS8umArfpGzEGgqfbk85%2BQIhAK9R2fIybSyPAO4JUVpcDqdlKAO%2Bt%2BsQvw7FbzilzsP%2BKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVFInua8SFmAZi6coq3AMvQNMLYKbV4nynfrBeMWl6cu0EZ4v3J8n7FixlE5BLub3Y8UrspV48qmfS%2F85KbXJfXF8LjK0KC%2FHFsrJIInDmAtnIrwF2zPNvUhrTXw3uR%2Fa8cZXsxPXW18Se9dgyDhPanb29NGebWQDu%2Bm04reSBIPqUoyoYdUMGKtRnaW%2FeIkrWTU7G9hZAtijW43cjsyhhIeOl11j9IzKE7sssIqJcSVYgn6Y%2F08OJsisRM3%2BrsuG6w4EjjUfsCVTv9ItxY%2FSJV5ih3uk%2F5YfR8SQv992E0LoJen%2BkQsOKReT5vmy%2Fxd%2BFEHCMFgFf17sTdcYzG6o4i2rA58RkdcuajgAYOfNLjmKsexCS2K8H6e9KQQXVuGesZF4h7dCR%2FrBjrs7AAM4eZqx170ybfnoOImXP3PgN8rovEw61vFa9yE7uJbN2Ykmp7EmYYI3d7Z5p96vIE8JlH%2FyHWB3%2Fjpkq6W0hCyz%2FDwX9dGzI%2FqBjjb5pybXODPRwNig%2F6lToUS7W3eK5XlIoBlEEVgjhz%2Bppza0yp37Sm50c%2BPLnVKac5VT3GgCz8Dja7orROE%2BS86KBKMIADw6%2Fk2Ta3kBfQd13ZibCXlmlPIgq%2BEAr1nkZGDFx7c9Qdaev70wn58dQ38S7mTCpsfq8BjqkAaJg9QeK19vEWB%2FrVYQ3n8gBsDczvKNl5coI63YhOeynBy3aGGDF87Be95sq7hEi9nXrF1qPoHVJ0SltD6BWRyEnnuFn6rwswEDFsiK6caAhqwhgXmt8D5E%2B4QJlIyiRLmpo0Sm6MrHqfkoJy2B7M7BrcUJ9YudNGmww%2F%2FVV%2BijMwOs5EwehEs5Ep5uKQbdO5GEPruU8q6yfKSWii3PGN68PsaRJ&X-Amz-Signature=a1bbd176c961bed7f2124c6469ad4487eb6689bf2479e48bbdb5bcaca568e409&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=0b784702767f739eac2d35bae31fefe7e96f827a5f5b2ea919ad84ea24c46fea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=f1278d6bd26cf7751ede437d9d59698570ff6a469e5950a8abdd272efb8b35d5&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=3c57e8b6db83772ca02a4b995282b0c1290d8476aa5ee51c87cfb1ebc83df943&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=8b4dca27d5c79e4561bc13c0f8624332896eb1577ed818d311fcbf72db12c896&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=ba489da4bf8910d5e0ae46200b173d2e97a9eb034258aa4a8e08e09af4f33488&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QVV2JEV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8baHqDhXmMVfkst%2BdvUFXKgLqT8xaf5roeIU6BS71kgIhAJlbPIjHQO3zMuaJaNkU3nVdnrSclQVNpNJy9CXjCHf8KogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylawsS971dgBRxJHoq3ANdJ5Ifil1NRrGg%2FPohUbJu7s4OIzG6LZ6KdVC1Hxxz5zES2xPuCFkD1uJn2ud4Mx1aFuIRStw7kDDueTitaAFYLD2%2FgliQECWWBJbyoAEDCdz%2BYMK7bUdeo%2BIhWTCjH%2Fh8EKZ9oaLAW6zLTD9Pv6vR8sNevd1JVwOB8VSER3B%2F8sYfhcnjgYDBLY0tuV2H5Ik5a88vUPPklEEPtogllFtSwtNssgpHjSZk6n%2BXF%2B6QFoNeFqlHJoQE83%2FDqVjU2nRXoc3SBRoTm4n5W1l7ORV323%2Ftw3KMVuKZ17kadLY8Ixt85jM1sjgTQf0cS0jthvVVQGAirzXpAUf%2BzCQ4gCTZ26iS8zkqKV8%2F5lJPxSpu6g1qjlxeVpYd2tdNle06xXQpFqSaYlNVKws2wbGeIgUYUIo6a0lCNHTDlToHM0lipCY7MV0p05hIFNkT86a5OjrYY4v%2FA9nW4wmkmL76BGl3utHrybF0TE5sP4iQhSomrCo%2F0Wita239tCOZDt%2Bglg1odXMpAhl3Tj%2Bjd9fCswSnxMG%2BFNCO34OUWEGmdbgsIORCxcHrMUVrwD%2Fdk3RMDm2R9sbKz5XzVHo1yXO69XtgO5ONXB9ZJ4n341tRX%2FUw%2FFdx5RRl1jS1VHrprzDLsfq8BjqkAUHz51XoSOJQ2ZShNPEyUV3TTaAjkHdEDPyEQmrP%2F9zGK4nLkPJoV2eoWaqqKAZyeFM7A1ycyO2GQpMOzWXX%2Fz7bLuhhZ%2BLyX7Xu%2F8%2BjfxLDO6z6xfszlOh45258GtfQwGZPVe853LkQg7h%2Ffnt9orsWUTvQUI9w4UHgu2z1iXN%2Be3vCwDguA4iCoiYMLx8s6aXpvCCrvFR5iNTo8H%2FFPVpSghtJ&X-Amz-Signature=c0c7e83d3e40f7de9a91d4b2c532c22b825a57aedaca2cc70d1817ee501fd375&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXEBDWCU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGK6CxHD0AOBag97%2FTfqUMvzIHM0k%2FJ%2FgafcCK12tOlgIgKKdybRawG69W3o417awlhJeAejp50agreT1Hh5jFmqYqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4DoHuuSbwiceBW6SrcA77dwQvLJDRJYBBQ8j9Rqc1VSt%2BnjXwOAojAlsdwTE9m91zappVVaWiDW5RrKq0VxYuOW1YLtjzmU2cTeg9H8AtSsNoREJ4XXEL45OExek%2FNdgXmfBrluZczVbNdoBNwHT%2FfkzeqxVjuUZ%2BDi11j2A3JUfSlYHa8esC0qrlLS%2FyreX3REr8ODZfUC2X5%2FFuVXeIznD3KVqRbjRQjBTVZzISy3n6DXNQiQVpU%2F9WyA7vu86vEynHTq2xgUAo9xVh7QxZkQ%2B6iD9gr2esUwhTJN03oDU7Pr5XPV7xm6cdItepcS0xZmkGDXHriIJiC0gCDWcr2sEPi9U3ZmUYcz%2BUH8oAe6bIHZWdY3Cqqxc51pPo46pCmGq%2F4H%2ByRgUu8siCMT2HTWRtKr4Nbg0XzHMm6lAwqQkKTWQZnZH8yzHWx1f29ewB5DC4dwdemoFLtZ2Xh74JfEk1uYOGwd5XVrFNLyFzTZpCFjXn3zaA6op5s5aTpgxPIBCwIsRRPSgUkGCKlBtivy9RPmoYbZiB9x8Y6OdcVl5j6lRp8RCBjKRaeMLg%2B9udG8orgOOrIL9lfaqreYV%2Fix1hvrQAzDUjUJrBGn5WxbQOEI6x59644YYGPtdI6Ck32atUb2b8DyjzlMKmx%2BrwGOqUB6asOiXguuLZqzmtskAct%2FTbkeztkADoaHL0QCVkwgrQfZax%2FmI6Ik6S7Fgyg%2FXq%2FK5APALNRpHyO9cg8yEQ5FczVTrbW6V9h8cjTFUVxHRYXJy3lHMcDcnAN4qKMG4QL%2BICwsdzQyewiUhR%2Br2uBolM%2F5xLsS3ELoI3UZz42iXV0Us1XFKtfmf2NVfm9mE9jzRQUZmcoYuBWHQSKxz3PlIHSSdiI&X-Amz-Signature=f6b020956daa4ba69fcb8146df75d6421a153b4b1634dace758fb1492cc8057b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXEBDWCU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGK6CxHD0AOBag97%2FTfqUMvzIHM0k%2FJ%2FgafcCK12tOlgIgKKdybRawG69W3o417awlhJeAejp50agreT1Hh5jFmqYqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4DoHuuSbwiceBW6SrcA77dwQvLJDRJYBBQ8j9Rqc1VSt%2BnjXwOAojAlsdwTE9m91zappVVaWiDW5RrKq0VxYuOW1YLtjzmU2cTeg9H8AtSsNoREJ4XXEL45OExek%2FNdgXmfBrluZczVbNdoBNwHT%2FfkzeqxVjuUZ%2BDi11j2A3JUfSlYHa8esC0qrlLS%2FyreX3REr8ODZfUC2X5%2FFuVXeIznD3KVqRbjRQjBTVZzISy3n6DXNQiQVpU%2F9WyA7vu86vEynHTq2xgUAo9xVh7QxZkQ%2B6iD9gr2esUwhTJN03oDU7Pr5XPV7xm6cdItepcS0xZmkGDXHriIJiC0gCDWcr2sEPi9U3ZmUYcz%2BUH8oAe6bIHZWdY3Cqqxc51pPo46pCmGq%2F4H%2ByRgUu8siCMT2HTWRtKr4Nbg0XzHMm6lAwqQkKTWQZnZH8yzHWx1f29ewB5DC4dwdemoFLtZ2Xh74JfEk1uYOGwd5XVrFNLyFzTZpCFjXn3zaA6op5s5aTpgxPIBCwIsRRPSgUkGCKlBtivy9RPmoYbZiB9x8Y6OdcVl5j6lRp8RCBjKRaeMLg%2B9udG8orgOOrIL9lfaqreYV%2Fix1hvrQAzDUjUJrBGn5WxbQOEI6x59644YYGPtdI6Ck32atUb2b8DyjzlMKmx%2BrwGOqUB6asOiXguuLZqzmtskAct%2FTbkeztkADoaHL0QCVkwgrQfZax%2FmI6Ik6S7Fgyg%2FXq%2FK5APALNRpHyO9cg8yEQ5FczVTrbW6V9h8cjTFUVxHRYXJy3lHMcDcnAN4qKMG4QL%2BICwsdzQyewiUhR%2Br2uBolM%2F5xLsS3ELoI3UZz42iXV0Us1XFKtfmf2NVfm9mE9jzRQUZmcoYuBWHQSKxz3PlIHSSdiI&X-Amz-Signature=c3ff5304e6ff7298bab79d7fd8a39cd64d7275b4f6db190700b908f160445d13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J5ICARN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBHbkLkHSc5pcGyV1Pd7Bco%2BSY%2FBvR%2BHeF423upwCEyvAiATRNmTMuAWdIzW7QRB62%2BdycbqKVJjX8qYXSjH2j%2BZ0CqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmaKGzBmv7%2Bfd2nJuKtwDpv8gQsLvq%2BF%2Fif%2FqNLO2IcKDaiyVEVujdHaYeByhF9%2F6E5winMAGFiv1QtrtkIYAKiOM2cZRKNnXU8Ug9tHGjTivfq3KBJbKLpQRXs9G8THFC%2FoY7%2B%2FLQZitRTpWOwK2pCdtaGmEAurE38VJv15S3bpyfLFpo9m5S61RWp96IeW%2B3AKRxYvvim26HpvfvKo%2F7G%2FBUbm%2Fggsr4d%2BBOV8mZ0d57POLww4lxzAspE19FXQwxNycrIpV47otMVktXkBxY2h7CpE7AhzqjYZOeM7mzTPPxG7Ow32OJ270VAQPQkO2zMe1u9%2FOhZ1MUB9b5JP5JEGn1kvWNGzQ%2BoXv5BvSE9%2FZANVGBcgHtNiY6q9Hj4oVsKxkBoZVPb%2BgHF1HemuLqnASef1ycnIEX0w9BQMw1TGwJelo0kEtUyayCZuRRFZGOebveEnHGYRoPnEYqiMHRnIJ7sqcbFtEwWN0oH2FNjIoriqvIZC%2FL5y1UGW15Dcqerq8WragTvHkkY93VftFwi8j49mmCFODL%2BGcHdTPQT3owTNScAjiix5CmTLEE%2BRmANP3nwpOArFTM7k0z%2BbbNcttqQjwd3Vs48RG97pQWrQ9j0clMSOcfKNs93afuUPIURmPhUfiV6qdfHEwlLH6vAY6pgF9nQu6z9%2FBSXw93EQA9iNKoJU96ZfC0VT%2B6fhicj9gVZz4uNU3G30xylU2CCzSefhh7iUeISIrLBXSLhVLqykxnqxMsJZ757gTgyKC%2B45CGy1JrwWf7JnWJKQYK5T0C8HZRItcGSsSFimFZSVRX08ZLhdIbZu5lQHwq%2F499V3y58gYmOv2L7E0CulP16kXOsJtQK6boXPKGLLRv4o5UGVig%2F%2FJTd%2BK&X-Amz-Signature=b52f7531672802f87b52648c575d1bd3c03bc278e66945bcc2f07b5cc4666cdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDW6UK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6yJk8vUpTvbOaYvQAg7YdtqASVGGi1eNu0qfzpg4dwIgFWtgR73QytKMAUq7gA9Zf9dildblaiUAaBamTrsJ9K8qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIws35Px5CRrQ9qhrircA1tg1NOq%2BETcEa2Z8G2OBcvU5p8ImlG5ARQ1emrXQdS3m8%2BUFNYALn9FaDldcK5GkqqZoa81KS5jJ6WESwgdVadTzrpgS4TSn%2F3%2F%2BXU136b8i%2Fm7hbWMAI2%2BCV8wRDks%2BvZfh36uefo%2BC4peHdR8eZJ2S92EUpU5xHA1NIy38jCZ08LoRHm%2FH8Y2xSPu%2FYrFNMmbkYjYGiUS0ssO4Yt%2BpF9oBALXbLd4tA2soXIVnllf4FqsDqeGLTUxCHQ3TMQ2ArMqDhER8Y3dVe%2Bw7ozeSHpjmZUUwDIVEDlhtNzFxnt74x0z6sH4uDudLIrJ7O6ce6p9WXTuuPkVWkLL9y59ZFqyndRMfGw6EYU8DUDq%2BdDvbFt8TXqjl883cXioiXzd44OMr%2FTTwGdvQcmJMVivN6MRVDcnC9zalQjdbg%2BbIgDMJ%2BzQ1FduwqMHmOaagRvCVkpnY1zcZPFkg54yCjNZrQlaZInk9JlbQSBBMvxGT64FvZlI%2FD1nVOws4amD8wzER9cVeCUMBCJs3N70UkVdFmfszSs8%2FkRYhk525j71KZRXs0aF3L19bot7aI15%2Bo2JKFnL8LKK0C%2BseDPCbZeMwOPFLg8svgt7t7MmIEMKgGtP78nbUcs%2FkR4WX%2BdtMJ%2Bx%2BrwGOqUBviztJXF4mqN86Itk6RarryXYVRTMTUstBLsqsr2aAd85Yk3PN%2B2FoqI7ldgi5Z4aklK8qB%2B7DfzEDPiVSZFYxhzAEF1vl1WNHxLvXFMCwXcaPs90Azmo4%2FGscvDwqoMtIaW47ZXIDZ%2FFDQprGsTI3qJ%2BlKnQ54veztSXT85oyu4zWDnoBvAaBdUnIbVQkz8RzhO8YwLNs0ZEl8Gkdxmoy%2F4iuca%2F&X-Amz-Signature=adeb4b3ad1d3332e0d8016d63fc83b6c30d39ea2b5d99dd18afb5e9c3b541f44&X-Amz-SignedHeaders=host&x-id=GetObject)
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