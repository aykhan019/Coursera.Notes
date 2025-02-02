

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=b21868f3e7a2e58d72db3c0126f7c9e0f5d3acda06268a4aebc1134754e00995&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=64a7ac526201165e92c5af319df04c9ccf472771105d4efe396442efe9812157&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=755e57430d44e49ca57dc4087252e86286e847fd8bd8d220a7bb9a6cc69ce128&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=c3baf7868421185fe518d0a9e639f34256605d77d4aebbfecbdc470be85b83e5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=de59675db7eb798e7abf5a960cb17d27993d9c4623989925e3bc4d99f1ddd81a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=b93df40d65af6131196596d5138a3cab0afcf1552ba881250b230070bb1bb3dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=fc05cdb61db8b52f39caee8aa11aac0569692f944b62154014e79c62d0cb7b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=a1a0c052b7ff10bb619150738e2daa2c47d7a5a8dc41574a39bd142c5790bb85&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=f9542ab68da13fef25374d735d12d03137921f97d6c9288eb02e8561f616809e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLWXT2X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIENF5PBfNVGUntTP1QizZAir%2FYbNxhg7vIMJQznzAolxAiEAiYICloUuHtPtIDgMMAGtRNNjWIarQBFs2gJb0HP%2BXgIqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMFMYuN0kgmj7G8UyrcA%2BoSpuYs5EPatJeaGSoCIha%2BIKrvttrsdF0hOwqeE3bfZXLNFT6toxd7fCUc9GWrNhaC5uivK%2Byws8fVykxpRdu2PVZUhkOQp8Gu9rrX11I1KlsnDuhAhNh8wxybTJ7JDv6Q1RYnElX1bBZFey8vpBaN7DRxyANCUqEh%2BPFI4zFyH80AgwJJx17a94legZOcyqSmYM%2FUhemBxtc07mn55Ynt9pG7hW%2FTXBD21ytwdqS%2FrkBusJrXKdKfAY3geJjTO4dAE2jhtl%2BntY6K8Wk636o%2B0IMEueorGqiXFi3qsGxN1Cdbt7QdLS%2FQJX6kf5hPzWxSDTi85AcuziToI2EHe457KPcvRDYD5t%2FGO4URO5565VwWXX8FlbkHOu%2FmVuAXwlOLTS91W%2BDmEe3vFODTOzvYOQddw1nYId6vlfbFFV1IGk0LWqAvuWUyNldL2bdqGWfJTz8ww14T6RMsTkmWgAuXkldXNFQ0O4OiLMkSnkUdQLihSuZrWhwAOnmP%2BV0qvAJsvxJPsQ9fSYier2s0sJmfwvhQYPANocD%2FPcG8axjOldW%2BuTnPfQtOkVzai4EaJVO8cJM5ObTFf9ICnYqx%2FlH%2BY1casIK4TcCugh98CIwZbJpcS%2BsdZ6%2Ft3SWAMOq6%2B7wGOqUBJLVUMDL7uaptYTpYIEA1OlvdzsW%2FG3CwvtdH6gmhp1TbzVzZnEfjz42ZqIVB8DaCW3uSm5N29axCO4rIe7fZjdqDz1pVr8DpBrMQXpGqzavDiHcQfUs6IuNdMiUvwSJIvt88S6Yzs5yaFg1EjGQIsKp9XhGd9XPBljsYhecIM4jLmOS%2FLZ5MY%2FF%2FeR3vdEQUtVjcyoH%2B9qnQk4mMEkcGg3HrkaVX&X-Amz-Signature=26b681c711f969f34e9cbb86ca8b084ccf32a87ae1a26726215f0e2a2648abc9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLWXT2X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIENF5PBfNVGUntTP1QizZAir%2FYbNxhg7vIMJQznzAolxAiEAiYICloUuHtPtIDgMMAGtRNNjWIarQBFs2gJb0HP%2BXgIqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMFMYuN0kgmj7G8UyrcA%2BoSpuYs5EPatJeaGSoCIha%2BIKrvttrsdF0hOwqeE3bfZXLNFT6toxd7fCUc9GWrNhaC5uivK%2Byws8fVykxpRdu2PVZUhkOQp8Gu9rrX11I1KlsnDuhAhNh8wxybTJ7JDv6Q1RYnElX1bBZFey8vpBaN7DRxyANCUqEh%2BPFI4zFyH80AgwJJx17a94legZOcyqSmYM%2FUhemBxtc07mn55Ynt9pG7hW%2FTXBD21ytwdqS%2FrkBusJrXKdKfAY3geJjTO4dAE2jhtl%2BntY6K8Wk636o%2B0IMEueorGqiXFi3qsGxN1Cdbt7QdLS%2FQJX6kf5hPzWxSDTi85AcuziToI2EHe457KPcvRDYD5t%2FGO4URO5565VwWXX8FlbkHOu%2FmVuAXwlOLTS91W%2BDmEe3vFODTOzvYOQddw1nYId6vlfbFFV1IGk0LWqAvuWUyNldL2bdqGWfJTz8ww14T6RMsTkmWgAuXkldXNFQ0O4OiLMkSnkUdQLihSuZrWhwAOnmP%2BV0qvAJsvxJPsQ9fSYier2s0sJmfwvhQYPANocD%2FPcG8axjOldW%2BuTnPfQtOkVzai4EaJVO8cJM5ObTFf9ICnYqx%2FlH%2BY1casIK4TcCugh98CIwZbJpcS%2BsdZ6%2Ft3SWAMOq6%2B7wGOqUBJLVUMDL7uaptYTpYIEA1OlvdzsW%2FG3CwvtdH6gmhp1TbzVzZnEfjz42ZqIVB8DaCW3uSm5N29axCO4rIe7fZjdqDz1pVr8DpBrMQXpGqzavDiHcQfUs6IuNdMiUvwSJIvt88S6Yzs5yaFg1EjGQIsKp9XhGd9XPBljsYhecIM4jLmOS%2FLZ5MY%2FF%2FeR3vdEQUtVjcyoH%2B9qnQk4mMEkcGg3HrkaVX&X-Amz-Signature=46991686c0f2cd715189879856b1183853ebf3b38e2534d6541ba4b3260b05b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLWXT2X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIENF5PBfNVGUntTP1QizZAir%2FYbNxhg7vIMJQznzAolxAiEAiYICloUuHtPtIDgMMAGtRNNjWIarQBFs2gJb0HP%2BXgIqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMFMYuN0kgmj7G8UyrcA%2BoSpuYs5EPatJeaGSoCIha%2BIKrvttrsdF0hOwqeE3bfZXLNFT6toxd7fCUc9GWrNhaC5uivK%2Byws8fVykxpRdu2PVZUhkOQp8Gu9rrX11I1KlsnDuhAhNh8wxybTJ7JDv6Q1RYnElX1bBZFey8vpBaN7DRxyANCUqEh%2BPFI4zFyH80AgwJJx17a94legZOcyqSmYM%2FUhemBxtc07mn55Ynt9pG7hW%2FTXBD21ytwdqS%2FrkBusJrXKdKfAY3geJjTO4dAE2jhtl%2BntY6K8Wk636o%2B0IMEueorGqiXFi3qsGxN1Cdbt7QdLS%2FQJX6kf5hPzWxSDTi85AcuziToI2EHe457KPcvRDYD5t%2FGO4URO5565VwWXX8FlbkHOu%2FmVuAXwlOLTS91W%2BDmEe3vFODTOzvYOQddw1nYId6vlfbFFV1IGk0LWqAvuWUyNldL2bdqGWfJTz8ww14T6RMsTkmWgAuXkldXNFQ0O4OiLMkSnkUdQLihSuZrWhwAOnmP%2BV0qvAJsvxJPsQ9fSYier2s0sJmfwvhQYPANocD%2FPcG8axjOldW%2BuTnPfQtOkVzai4EaJVO8cJM5ObTFf9ICnYqx%2FlH%2BY1casIK4TcCugh98CIwZbJpcS%2BsdZ6%2Ft3SWAMOq6%2B7wGOqUBJLVUMDL7uaptYTpYIEA1OlvdzsW%2FG3CwvtdH6gmhp1TbzVzZnEfjz42ZqIVB8DaCW3uSm5N29axCO4rIe7fZjdqDz1pVr8DpBrMQXpGqzavDiHcQfUs6IuNdMiUvwSJIvt88S6Yzs5yaFg1EjGQIsKp9XhGd9XPBljsYhecIM4jLmOS%2FLZ5MY%2FF%2FeR3vdEQUtVjcyoH%2B9qnQk4mMEkcGg3HrkaVX&X-Amz-Signature=d08815482711116baf65b2a94e278a8005964b116daf89c9123a3b8ad810d44c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=8549d43088141993c7565285dfd0b0776a85d3cf5ae979858092b1b670d82b49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=3f38d3be6fc98f1f6862711ac67c8295bbbf862725dc724f57870cb205d62cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=468cd1529e4a747e4bbcf701b46e66b5fe37901218a0ba4a9ab559c17800fe54&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=d128291dcca8a4d03b1b087c9a9e807773aa40c72fdd96f878834904b80ceaab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=7342621cbfb20ad5b3898a0b3ad1488e3209e2d3f896ac847c4438f625fffb8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VERZOY4N%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLUH8MdAI3W4gXMPsz8bGIZYYuIcBsMnSGw%2BpGwdoVBgIgSdgmiAqeBv4lwEPrFCbYzXx0qymJ9kK3vKF8cofiQ0IqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2Fad5JgLXOc3y7MlSrcA8bNX1QpvLP1PhaJfcFLFqUST11wSFE%2FXzVSxhWlKzjgHIOwEAP0%2Bx33bVSq5pishXe3JBT9%2FTvupdmwaL8qM1g4y49o2VHbCy%2FULJ92e57TLspW0Z%2F%2BOURIXrWWEH%2FlPa07z57MNXOirZ9%2BmhBMOkc2RFjuQY1FPxkHj4tIUh1fUuKnUJzQpU2j39olc3bE4Q2VRrqcjvj8Vpn8KgzkgnXT7SM8ft93WBMZg1qKM0xuU4%2ByYY3Nq%2FhhEotD89WnZ2%2F%2FBqC4pAe5fDNySdhXlqmX9vxdV9T6cWQ0V7F0PYP8XUg94dL2OIRRs%2F1xzn42kCg4HaqqsjTIjhi9NzZ3lLSsWiVBO%2BhTFOzwA8M0dfqEtQjHML5AwkuIOkZmjzKl4iStritrt5jNod5MorIloOpuzwJtuqkPMlBMzQxMiyn01x4y9Mo7%2BHHC6fqxV2%2FP%2BEM%2BahlVNlMPibzPItnZZ9K6ofvhOwoRPyQmgGyluVMx6fTMp1LqDcXyiLeF9lysvu8AtwfXO3UGTiL2Gr4%2FU4YlkPItBo%2FwIiwxVviS6TAn4Gi45vapb0gjRIhZg5oryrxT0iS8I4cRmF13qdiNhUKk%2FtnD8wz1FfUZf1OTzxMqKFawbNXicCq99BRxMNO6%2B7wGOqUBsGuj%2BBOP0H%2BlXxiEIR4VtGmwGN4XCBGkt211iK1G3URLeP7xqZ9ea6qICxiJuUGHFO7M7CS5%2BNpDFKhWM%2FES8aUQa0%2FUaeldht1St%2FHQTN6LtJBcS5%2FdYapHHt0mwe31YOm%2FCJRNfKQ9m%2FAJW%2FiwQnoAsswunz03iVsNR4m%2FLNPQDmPnc%2Bv3ehJxluwoHGKQIb30HKteNSR3ZTVdHuIHZlaQJHCQ&X-Amz-Signature=6736195a090da6598422d8c96e6810fc88a16d632bc92769b4b85fe921df4f4d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666CMYRJU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEVJAZnscK%2FA388lT%2FmQCrtJ23eehfD5iZYQWzlXqBksAiBX18OA3BNZUPnsUYuM9RQTZLHysIK3FPx8tRzcBmv6vyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdBVqAmGf8aWQ4%2FcvKtwDPJ6IUWTHLBXoPV76GAcThbCx5%2Bo8JEVOYi%2FfUJEbLwyjlmoCo8gfNh%2BR6gEzPvWQHpiiYNn3gzVavUwWTRzxz%2BwIoFECATwzqukqIALimjzDw%2BDRH2vH02NrFKnSmTHipaSzbKlnHtVN6Fv3JdvzySZMr%2FqArWO83skk0HhClSYnaqvXcRDB5AvNxU4gvWWWDo86oYTHbDPWyF46kN%2FGqZ20jYsHp7XdLLfh7iE9S51yk8ka5h6mCg%2FZK7U6Kw5C%2FE4PYbvNO4tkNR0DdyYRzAIisnUozE9jDjjfpjf9Ni7ThE8bqbFzDhkt4I6rqESDuFAxAfmuiKmcrzJSsAZqULZhvh9ehiwDOniAhfgOGoTPWqLUc%2BXiSRu9Ks7vOqS%2FPlS2w224RZyGKUeLRfBYAqD52J6BeveIGKPwp%2BWHyZDLiN%2BMGjpSFEuYoJM7dHqB70Q1FDXodKrnZmphEsVVLQ8IGcDkqo5Lw4kjc0r4en%2FqFfvoFMpBTiMyuK6GYSrTv1KuJCDNR0V%2FbiqxdrOyPtCE04Anl4Erk89TjlRI62J7p63EaJYz8AxJQO28rt1JPPVxwiAzeqQWJOMpzAJS82IfNw80k2KiEZQyX9u2VnJFUAml5ppMtJsla30w57r7vAY6pgFSX9ueyTW%2BEZDPDDFV0aeddwzBSpxQe%2BbmqzlBsYel6WABnMW2LHXQY4XY9CcVmJ%2F7z4JpZ6hTH4HC54PZAKSiBuELl%2BvpGRLw9hwZCnUSTdqrkRBaN6uvlrXgJq9ZNz1S3OlUlAL5oy7XrdBBSltIjGfB9twXMV3DRAWd9RNN5dcfX4Uzwiovle339MPsFiPPFUGuhJQQWZm38L2ZT%2FJ1Xfnzr%2Fex&X-Amz-Signature=ff675112b2782bbe84d81e2234f2a61ec9e2e39d0bc541718a5eaf2c2ee1f887&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666CMYRJU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEVJAZnscK%2FA388lT%2FmQCrtJ23eehfD5iZYQWzlXqBksAiBX18OA3BNZUPnsUYuM9RQTZLHysIK3FPx8tRzcBmv6vyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdBVqAmGf8aWQ4%2FcvKtwDPJ6IUWTHLBXoPV76GAcThbCx5%2Bo8JEVOYi%2FfUJEbLwyjlmoCo8gfNh%2BR6gEzPvWQHpiiYNn3gzVavUwWTRzxz%2BwIoFECATwzqukqIALimjzDw%2BDRH2vH02NrFKnSmTHipaSzbKlnHtVN6Fv3JdvzySZMr%2FqArWO83skk0HhClSYnaqvXcRDB5AvNxU4gvWWWDo86oYTHbDPWyF46kN%2FGqZ20jYsHp7XdLLfh7iE9S51yk8ka5h6mCg%2FZK7U6Kw5C%2FE4PYbvNO4tkNR0DdyYRzAIisnUozE9jDjjfpjf9Ni7ThE8bqbFzDhkt4I6rqESDuFAxAfmuiKmcrzJSsAZqULZhvh9ehiwDOniAhfgOGoTPWqLUc%2BXiSRu9Ks7vOqS%2FPlS2w224RZyGKUeLRfBYAqD52J6BeveIGKPwp%2BWHyZDLiN%2BMGjpSFEuYoJM7dHqB70Q1FDXodKrnZmphEsVVLQ8IGcDkqo5Lw4kjc0r4en%2FqFfvoFMpBTiMyuK6GYSrTv1KuJCDNR0V%2FbiqxdrOyPtCE04Anl4Erk89TjlRI62J7p63EaJYz8AxJQO28rt1JPPVxwiAzeqQWJOMpzAJS82IfNw80k2KiEZQyX9u2VnJFUAml5ppMtJsla30w57r7vAY6pgFSX9ueyTW%2BEZDPDDFV0aeddwzBSpxQe%2BbmqzlBsYel6WABnMW2LHXQY4XY9CcVmJ%2F7z4JpZ6hTH4HC54PZAKSiBuELl%2BvpGRLw9hwZCnUSTdqrkRBaN6uvlrXgJq9ZNz1S3OlUlAL5oy7XrdBBSltIjGfB9twXMV3DRAWd9RNN5dcfX4Uzwiovle339MPsFiPPFUGuhJQQWZm38L2ZT%2FJ1Xfnzr%2Fex&X-Amz-Signature=27bf6ac34e6e52a8fc0ed306d0543b0e6f5c06a663f735560768373b3bd8aa53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIKZQ5Y4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXhr0YceXOS0ZPBr7%2FIcR4l4LENIN3LhJOu3htV%2FGAmgIgFLbi7T1obLdY4tb8GpaBnSfNyW3MuUvwpwjc3TmqOpUqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK3zXCCevVbxXIBIiyrcA17VayHp0zP0K2d4fnAU8iXOmc6jHVhE7xczEjgSRkoR73QKLPedaa3KllyRzn0zGjQTVTbfDCRWAE36x%2BKV2zmxpRyBy3JerdgEf8USZnmv4HeUz4iFmKYzsj3Sfcphl6dqSyid3O71iTpHr8D1Y2SGShEaowvbNkQGH4o1XVH%2FTSA1ulEs%2BHWxENvW8DzXOjegxTjQz2NAc4i7fastsrssODQW7Qn%2FK4EodhpOM%2F%2FpbXKacfbeNdxFaDi%2BqPEQA8%2FIGcGEG1VC4UPmupPKrthD87SdoGsQ0AlihVX2a5YDAZw1lk6yHMHDPNxsHdSKB2eMYk9Y9qk3CJxrd7z3ydPosN1LVZIhRL2TK0zDv67mR0mrowFyYCIXN5ZRbl2jRLjLKzAKN4AgDmIm%2B0%2BcWZ2eTWqivg0b9U13kfrcGtng6EVZNL8WBAEC6EDYPVcNSs4dqPrVJLwH3O1xSJ289C03kUJAXUN8c%2BzEqShrYgG7WtlxhukdNIY2m2HKh6rP9QwNE4E628LULU%2B4chWovsG2WHG3re4h69lUkI1tY9sg4oi8rIsYxfbzIPg4TV3tUSj1a7tpL96ds%2BM3p5dSyt%2FmV82mhGvCkM73iS4vT7cLbJwEZaAhBoTtL8NfMMu6%2B7wGOqUBwlBDUT4bqiaaWEJYxDj6Pe%2B2h6jb9btatcjmZV7Qn7rOcIWuRGwTIeZsI5g%2FL1ejNv0rR7z6KDEO1AmIElySXnsvMOmw55ukmcLxwTsMsFjgKh7s6BuXVNnibKK32DlsHX8KCbTPOujvYG3LPKEbZOgaYD4vzc%2BtZI1OVgfNdH%2FQgCxADIwZ2XJlIMO%2Fu9KmTg0978bKvgxEX3ZQWu7bTbmalNEH&X-Amz-Signature=c559e87f7d041b282bcb6ed8940b1cdea48eef2bf5ab7ad19764a88dca29e7a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSU7BR6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcO1BA7QPmtkNeSNHxqvWk25jFUqlgdlD5hVIl6WA5QgIgSZe36FsQ18SoYn0gg4GUnKK%2BIp8aovdnwAWgZvq5%2FXcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL04h%2FyLmThu%2FiZWYSrcA6YSia44nS%2B0B0KIhYpSfx0oWcIlhXoG1NyTHCsbN6i8GztTPO4r5%2BsXNKFynjbutINZES4UM6hjP99NUFu%2FUPfPx2namwAxAljStrPfsVmU6y38LLEriBo2gQ4jzlYLUtm6pp9%2FgdfVdmFUil1fHexfzVmb5JYGEl1F5qeTn28qhAAUcE0fuo2xpLm333t7O9V577CiPH9qeFmrLQN2XisNJ84TD7CCtyyQsBJSgfYDeax03vvhC8pm%2BjLbJVUTV8Ir8fOegYPZi3dTIfBfNkevCrns337FF25ilc9oGsQ44OQcewj4M0XKtXlqdCu0EqdmTTSlQ9TTEKC5ZI8NNau59IDH4eyXXyubxZkNw5g4KevIddro3Ko0D3zLTw5D13W2n5kmnwwD1JuPWx%2Bp%2FRlSlUuSRomqNx%2B82jMqb9X88dsP1cjmuI0ElyL7h4Nmdv3X8u2fAkdxGy%2BK9pZrHnakfLmnsmdPVcJ8JiYLlCfq61HnTbh9%2B6mzX1%2Flwv%2F3wGXshl1lD%2BqPy2r7Wn6THHe4D6LGEcUVHs8IiXeZkYU9zi4NIoaaVVJ9mV1FdXkpi0TyuR1jwikPQSyRfpYEOp2cHgeDHKAuzb59wdqFYxNKMkipjOYgMIPwTQEBMPO6%2B7wGOqUB%2FWKpGjAObSAFxeHV706MqHVmufzH6aKq9f6DpBVfXDArCpNqFzWhGJodideEtJsBqAikbv5IU5FRtxwgh1apGuCgQ6jcqbJIHbpXMCiSQrRbYhMeFTNu82E1h9GeCCR6hmNtmvxXVFdi7zpmK5%2B5pjENXJAZ8LEXRZOIKADrk92u31ELJXG4EWFEOeq4XfjgzP0XMhC8lfjF7VkXuht2VRqGu08W&X-Amz-Signature=e39c452f92755de57b29bb70f5e1da4b14a225cad4a479c3cd572c88fc0645b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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