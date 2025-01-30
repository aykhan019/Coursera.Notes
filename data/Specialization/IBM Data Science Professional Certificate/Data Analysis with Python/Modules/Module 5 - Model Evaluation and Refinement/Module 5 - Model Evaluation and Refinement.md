

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=250766b893e33d8bb2c09aacda905a01e11cb3c0f2b84a18bfee91fba8a4c905&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=21ce7b5bf928a203dae0785fb6c033a15ee62f25f5694d0a54724f561796e327&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=cec7068e21ca1ec2b99f5f2eca522f5a7d404aa6e4d588808b5ac3129184b5fa&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=867a5131079c5b652ad1a84103e3f405f8474471d71e0f7edce58a8aae328133&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=d80963111a357e86fd96c59d6dbd35430e09225873a14e54ded6ee4a9d6c967a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=96dbac7f6ed4b53a586feb2b8f48685c6d5ea0a7ec8f7c693f73410d3fce844c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=de1b7861704f471ef312cf9b293a73be0f350629b9c86c761f2d35bfacbc6e65&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=682165ae5c3f96bb4e1d03058f5e63f947ec4b1f81d8db28e331dd37cfe2c00e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=533025d77a4dd412e089b9f08cdfb0e01a4e0173648da4b0a2310e755b5768c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647TILLLN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtX2uovjm9FT3SfUGzfVOCpfMnApnLp6jpvkbC4SqWRAiAJBVKBdxMG0zkTL03RZ4oywLspT3abhxBi7X7bJiId1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw1k77fdaVn2SZ4lqKtwDfeqKygpzeKZrgE5zUqW4JYeHaBmKG0C86986aH%2B6RPB9vAdy7msPbRDvaFwYSYh25bJ3olyDTmM7dQSegbFNir3iWw0EgMan%2F6w7tAWwjPJ9WZQ6e4O5xrz6%2BIXabJwLSjL8ohI%2BtIFNSnXK%2B%2F%2BfdPY%2Fn%2BK4bSDl1XKKpTzotpYe98AsfVQPxE4IhIOzWRxt%2F95O1yvUYRNCa9RNIWB5KbkOgArFRYwR%2FlB2klMc0%2FX3AwC7KPuqRVF4P2687BghBVRnwuMyHwvezmOwVq4bYSPWNRZNapml4OdYcYS8aq%2F%2BOiOqpUzQ5t%2FSKny1oO3yjz2oJtYwYWwjR5tWQM4YfNJh3PPIWzuPuLzasNX6ww7VIokVkxWw2F2BFzteaWumdOm1paK2EeBQ6pWLTsdjFI8qOCqUHL85CCJuMRZQ%2B4rgrZnvpCucXMPpGMeUfj0q34%2BrO1BO5zD5dWAJZIwy5bCOwVny1B6nP8qD8UxsNZC6Tki1Az2gBDJUZ0ADRQ9sEYMwYYoZ7pPJgD11KPcDeXAzv6yS%2FdcXUQrCqLosldT16gdysJIXwlx8zamkWg32xy%2FYcFipoAIQW%2FixyV9mL4dVBwgT6ytOA%2FOX6hQPgnMn8Q3Se19cXUHbDrUwgd%2FtvAY6pgG2LiEW7zgtBowDeh0ZeB9skYxtItjcPmYOfPUJYlwaRKLu%2BkUqGUD9RVBkWuppn1o3StvRKpuxj6DwcYcFTQWYQqXTflAU%2B%2FsoDV205081CepUsdq6tz1q%2FXR5pcHyBNOrtrOfjR3qW3dIrQQULsLuWplg%2BPoA5%2BuU7PauF%2FA9CwmEN4GTgdU2qAGrXbVQMjmf0FWfHybJeiRoqYhqT2Eh76mlzlYl&X-Amz-Signature=891cc8f743809612a42040dd28e53d887fc9b4e3617ef825553beefdca9c3b94&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647TILLLN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtX2uovjm9FT3SfUGzfVOCpfMnApnLp6jpvkbC4SqWRAiAJBVKBdxMG0zkTL03RZ4oywLspT3abhxBi7X7bJiId1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw1k77fdaVn2SZ4lqKtwDfeqKygpzeKZrgE5zUqW4JYeHaBmKG0C86986aH%2B6RPB9vAdy7msPbRDvaFwYSYh25bJ3olyDTmM7dQSegbFNir3iWw0EgMan%2F6w7tAWwjPJ9WZQ6e4O5xrz6%2BIXabJwLSjL8ohI%2BtIFNSnXK%2B%2F%2BfdPY%2Fn%2BK4bSDl1XKKpTzotpYe98AsfVQPxE4IhIOzWRxt%2F95O1yvUYRNCa9RNIWB5KbkOgArFRYwR%2FlB2klMc0%2FX3AwC7KPuqRVF4P2687BghBVRnwuMyHwvezmOwVq4bYSPWNRZNapml4OdYcYS8aq%2F%2BOiOqpUzQ5t%2FSKny1oO3yjz2oJtYwYWwjR5tWQM4YfNJh3PPIWzuPuLzasNX6ww7VIokVkxWw2F2BFzteaWumdOm1paK2EeBQ6pWLTsdjFI8qOCqUHL85CCJuMRZQ%2B4rgrZnvpCucXMPpGMeUfj0q34%2BrO1BO5zD5dWAJZIwy5bCOwVny1B6nP8qD8UxsNZC6Tki1Az2gBDJUZ0ADRQ9sEYMwYYoZ7pPJgD11KPcDeXAzv6yS%2FdcXUQrCqLosldT16gdysJIXwlx8zamkWg32xy%2FYcFipoAIQW%2FixyV9mL4dVBwgT6ytOA%2FOX6hQPgnMn8Q3Se19cXUHbDrUwgd%2FtvAY6pgG2LiEW7zgtBowDeh0ZeB9skYxtItjcPmYOfPUJYlwaRKLu%2BkUqGUD9RVBkWuppn1o3StvRKpuxj6DwcYcFTQWYQqXTflAU%2B%2FsoDV205081CepUsdq6tz1q%2FXR5pcHyBNOrtrOfjR3qW3dIrQQULsLuWplg%2BPoA5%2BuU7PauF%2FA9CwmEN4GTgdU2qAGrXbVQMjmf0FWfHybJeiRoqYhqT2Eh76mlzlYl&X-Amz-Signature=ab532b611620d64572dee932295e739b698f1e24f5b3b5a32f6dac93508248cd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647TILLLN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtX2uovjm9FT3SfUGzfVOCpfMnApnLp6jpvkbC4SqWRAiAJBVKBdxMG0zkTL03RZ4oywLspT3abhxBi7X7bJiId1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw1k77fdaVn2SZ4lqKtwDfeqKygpzeKZrgE5zUqW4JYeHaBmKG0C86986aH%2B6RPB9vAdy7msPbRDvaFwYSYh25bJ3olyDTmM7dQSegbFNir3iWw0EgMan%2F6w7tAWwjPJ9WZQ6e4O5xrz6%2BIXabJwLSjL8ohI%2BtIFNSnXK%2B%2F%2BfdPY%2Fn%2BK4bSDl1XKKpTzotpYe98AsfVQPxE4IhIOzWRxt%2F95O1yvUYRNCa9RNIWB5KbkOgArFRYwR%2FlB2klMc0%2FX3AwC7KPuqRVF4P2687BghBVRnwuMyHwvezmOwVq4bYSPWNRZNapml4OdYcYS8aq%2F%2BOiOqpUzQ5t%2FSKny1oO3yjz2oJtYwYWwjR5tWQM4YfNJh3PPIWzuPuLzasNX6ww7VIokVkxWw2F2BFzteaWumdOm1paK2EeBQ6pWLTsdjFI8qOCqUHL85CCJuMRZQ%2B4rgrZnvpCucXMPpGMeUfj0q34%2BrO1BO5zD5dWAJZIwy5bCOwVny1B6nP8qD8UxsNZC6Tki1Az2gBDJUZ0ADRQ9sEYMwYYoZ7pPJgD11KPcDeXAzv6yS%2FdcXUQrCqLosldT16gdysJIXwlx8zamkWg32xy%2FYcFipoAIQW%2FixyV9mL4dVBwgT6ytOA%2FOX6hQPgnMn8Q3Se19cXUHbDrUwgd%2FtvAY6pgG2LiEW7zgtBowDeh0ZeB9skYxtItjcPmYOfPUJYlwaRKLu%2BkUqGUD9RVBkWuppn1o3StvRKpuxj6DwcYcFTQWYQqXTflAU%2B%2FsoDV205081CepUsdq6tz1q%2FXR5pcHyBNOrtrOfjR3qW3dIrQQULsLuWplg%2BPoA5%2BuU7PauF%2FA9CwmEN4GTgdU2qAGrXbVQMjmf0FWfHybJeiRoqYhqT2Eh76mlzlYl&X-Amz-Signature=29f306cdc1c0a405647508bf433de5937f2b5aec1f542f552d8de6204d197bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=1a079af06772d50b3e7777b3e64d439fcd08d472ebe614045d7eec747e2087ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=bbe7553e2ae19c1f9b68526dc514701280fa9ce77b3fb92fb1630f6258cfeb7b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=89236c2803654fa9cb04cee55056648577654d21ea4bf79f79cf825766c084f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=0a24954c59d9223a912a20f5a9b1f556dad7f298b51d07d901ae3860bcf031fd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=2931648ddada5d0a6b01a29765a7ddd4739dfec87862cbb385e529a307154e3e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBE3MZRU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiW7nUGdmORiM1f%2B2qYPMLZcIt8INC7jYEIVhHFx4ggwIhANQ5mYSbJrRyOvEfLanThISzOOp1C1fvpDjZ8%2BssimbNKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwsky8nfcksHOq8q0oq3ANg9m2afjHwv26tbdkUrmMuwa7pfNGvyC935a1ZTu9DzsQHYckr7sOl4cprnesoaGcVLy7E93CDdFxeqm7v%2FfXZGU57CFZzuDaEDDSlBCL0pz3vc4lXS7CHXHbOamAH08g0a9jkTbzhsJoGLJOpLeL34UjgVsl8ecrjl8ofnyC7pyOK6CrRgvG0i4Bl2SIQUhIHBd6m0fDplUR8c3kVy7SukTJN8W1t8lcEWLSmBwgJXPMJIDO0bT5POVTEAumz3S7nzG5lQHX1eWWwwO9qAvT2NTNpO0ssWj%2F%2BlOrKVwbdIT%2FL7RCsWHquvYQQ%2B6dOLdvWXFyfnlGXDDWtnJEIWN9mWpPK29t47%2BHa0GRhIBJ1vakpgLr8nOCMRHpW9TO04Ga1eUBRv95omWfTYl9FCdTsd%2FZX%2BULvIUt4N9CDCDEGscCXrb9NGbdF1NMk%2Bz5AGk%2F%2F1ocalJEKXW%2BHxn%2BJvuUkx%2FxS5MAvuosSzbu%2FzQf9YRevdATynp40puXbb8GwiJbuytYCf4NoYRxRdX0UcjSnqxGya6e9WaoWK42T9aRh1qBTa6UpVW7g0sHC%2BkK6Ewb3DgU4J34K4DsCOAIR8ID0e4Wka0eUWwV%2B88a8wAM8Zka3jAT2f23dHCY7mTDS3u28BjqkAbXUyb5i7Ay8c0ga0GHeB5sAAxZjzavdJudqBcesUwywo4PLBjHHhHzVVIhovoPFWH6vs9fn%2BFORNEyWjDqJn0voP4n3IjgO%2F7Fx%2BZdCfeisc%2BRu4blVJmlhTfbzMqqtCqqOd25xnLZ%2Boiq%2F92utZgRTxCI70HPLHBBUdYMPUEUm%2FKFrGRFjTNhH6wrPRG0FFTmt6L379Mf%2FCg4l2EwFe4sguAfE&X-Amz-Signature=3f752cf4cffa044adc30a786b70560cbfa1a18cac45311465926f0004454adb7&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCG3PGAA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFN32TwlNP5LqJSh%2FRR6%2FJxxHRvHFoiXp8KGI%2B8RuUFHAiEA2v08KyJj5VL2POlQ76uvrE8Yrhww29CQGOL1qmkGQ84qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPaxzrO8dorrKF0QxyrcA2rASgSG%2Fg73Tqoac9qIBjyt2JKYc%2Fj3QWRoDqfWOq8j6KHPqT%2Brjt9z1M%2FNI8ss%2FBKR3r1HVkQcC7hKJ3%2B%2F9nksqYBCthCMtUqP6gjBwTVwIvrwjbMGUl3enqq6yxTfMiIkX1aPm0D%2FTPsp%2B4PGnDT8yAZA9EO8zLv1A6o%2BPbfTbcdYKh9G19xVVp4tWYSMt1CWAC9ygLMU98qNdKo2fhJ0wN4jwcZwWxpa4E%2FHg7NYZu5nQ7StNOg8M1buhEtpvvCkWZ%2FXt3XZFYDGmvf0mg4XkUorLFzNlZzsF%2F%2FScrqRK2BUsbDQK5J7na2xMk0nfBUk%2FegBybGPvYTYQljiGlbvcfpeNyDNa91mYf0Ozo5hhThsoK30jzf4xS2VJjnivZx2j2x3lgnOTpGn%2FozgVbyMf74BqwgQW2fL5m5C4po2cDeyODbpxWfsjy9I4R82IqPTL2tz8xbXWshzDtHnAs6oJ%2BdNNrLdxFX37a%2F5xPXty2xisQ2b7l6uji%2BfGGB8Jy6HKYWbjoLB7A3F6TTEMWGuTur44BxQibOFsfVJWWQD9ECVm7fwjuXv4tg1QtTAjH09dpZhRggRA73rUUr4QQ6UDqzeb6TlrA8Or5Ula1zsttE2C1j0LDWsIY7IMOPe7bwGOqUBoQx2djpJ6QHnkPagHUCXH5AH%2FcGDuotlPhwARQt0B1hQr49%2B%2BoPxbpcLbdGzAD36GXgYTQONPwfykc7qyYwAhYWVMrr8L0L8svIRaa8GuJvPo4TsTdYrKkKj1QzzkjqkAaxmRliDtgkQTT0C50neRDhhMMitpCGZbPqyAShOMmFlMOD9UrsWNdLcOW3ofWe8nzQQv2mbHyoFqPf0Mu8QM2UNkgzt&X-Amz-Signature=a48a08b1b7caba0f323372119cb0eb8e10d77347ff95b5c4806d82df2a9e7c0e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCG3PGAA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFN32TwlNP5LqJSh%2FRR6%2FJxxHRvHFoiXp8KGI%2B8RuUFHAiEA2v08KyJj5VL2POlQ76uvrE8Yrhww29CQGOL1qmkGQ84qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPaxzrO8dorrKF0QxyrcA2rASgSG%2Fg73Tqoac9qIBjyt2JKYc%2Fj3QWRoDqfWOq8j6KHPqT%2Brjt9z1M%2FNI8ss%2FBKR3r1HVkQcC7hKJ3%2B%2F9nksqYBCthCMtUqP6gjBwTVwIvrwjbMGUl3enqq6yxTfMiIkX1aPm0D%2FTPsp%2B4PGnDT8yAZA9EO8zLv1A6o%2BPbfTbcdYKh9G19xVVp4tWYSMt1CWAC9ygLMU98qNdKo2fhJ0wN4jwcZwWxpa4E%2FHg7NYZu5nQ7StNOg8M1buhEtpvvCkWZ%2FXt3XZFYDGmvf0mg4XkUorLFzNlZzsF%2F%2FScrqRK2BUsbDQK5J7na2xMk0nfBUk%2FegBybGPvYTYQljiGlbvcfpeNyDNa91mYf0Ozo5hhThsoK30jzf4xS2VJjnivZx2j2x3lgnOTpGn%2FozgVbyMf74BqwgQW2fL5m5C4po2cDeyODbpxWfsjy9I4R82IqPTL2tz8xbXWshzDtHnAs6oJ%2BdNNrLdxFX37a%2F5xPXty2xisQ2b7l6uji%2BfGGB8Jy6HKYWbjoLB7A3F6TTEMWGuTur44BxQibOFsfVJWWQD9ECVm7fwjuXv4tg1QtTAjH09dpZhRggRA73rUUr4QQ6UDqzeb6TlrA8Or5Ula1zsttE2C1j0LDWsIY7IMOPe7bwGOqUBoQx2djpJ6QHnkPagHUCXH5AH%2FcGDuotlPhwARQt0B1hQr49%2B%2BoPxbpcLbdGzAD36GXgYTQONPwfykc7qyYwAhYWVMrr8L0L8svIRaa8GuJvPo4TsTdYrKkKj1QzzkjqkAaxmRliDtgkQTT0C50neRDhhMMitpCGZbPqyAShOMmFlMOD9UrsWNdLcOW3ofWe8nzQQv2mbHyoFqPf0Mu8QM2UNkgzt&X-Amz-Signature=94cbbfd90a03bacc5f9f4a4955ee2ffb2271e5686759c8c7aea275580034799a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634T2N7YG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMw2E6KKorfm4o8PVOR7YvfvaFjW5cR7kd77JNGrSjxAIhAL6bC9zyNd74J%2BO8ZPwqKs04taIRILbzUCYqGFu4vhItKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzRSS17sPf0Tey%2Fx8Yq3ANGwdtpX7bymQ%2BlsBzcSBiJlL6XWYPRgpX7UzsrhBdHqYPExmXBRHpXTKGZw92vRKcPyFtg%2FmLEGw4C71IMqdGE%2FRR12FTQqE0td4aMb6PFbKnyeGOiqmAJC8xFpshtNrF%2FZ5WX9i%2BVqJGSNUexLad7lE1HQdV8Dr83LiaHOlsSKDcjEl5hALmo2Kci4gD%2FgRj1KHcV25qDafHxoGW%2F2620NOo9oxxQ1kjj34Vheop%2FUceIGZGNrxroBBonlxNw4gbIhDxdUFYyIojjyijALo0WXIJTEE%2Bunfv3bsRtaTE7lDCc4rQe%2FYJqvYd6Wot85gwvmAiujYaU8XGIsHKPzq1Y2Lp0I9%2BzLbOHpxoOVVyWHmv2fjQetqUrIcu6bEtkhrU8VYujLhv5PgAdO3SWC4Av5VAYFccpvXU1rnk6ekgEatQrCa1Rxhb3txhDD8XP0C6FXWaaiEbEJInD0NL14lTgqmajk30LBtcaULZPdHPYcUjWDz77gLHvtO5dIRn%2B3d2GXwgr14xPfiRnt4KHHBidd8gvOorv5RlLhXi0Ap5tNSudfZdmVsBw5zx0h%2BmHVpwUgCSeN%2FrlHA%2FP5dArVyUgLQWtjlC0ts9SemE183XkLifAwn5ft05FuA5SnDCc3%2B28BjqkAeuXI9hIeIFmgSNCcjRXXtqZROx5rZA6Eqc1FNZKKL1DXBWprytV0Jc0X05Fl1igrQ6welQCTjzSYSWqOPlBOWlf6In4ob%2ByHOa3ywTddoNVyMoemVIuTPcqkH9%2FC4TA4z8LzeJe9biEZpMBFJK7s1Dw%2FLmGX2gyq%2B%2FJYnqiR7Xm2mOGvDGhKuPVGt79QdpZbGnYqWmx8bQXXBdf1uCeSaLOufaF&X-Amz-Signature=c5e97bdf508f3ceb962fb4b43c441fed535bbecdeec81fdfb32ff888663af53e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTDOOEXU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDyemASCtqPni3yVlN9LI8tuzXkrZhb7M7Oziok%2BgJAIhAOfvbfOstCLaKV9tYyBjBiXkudibtx0NdB7%2B6CV8KvqjKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ0rgMek3UQi4yFxIq3AMzpDNoKVY5KzMRxfCGsmXyvwN3nFanA2aum%2F%2BkJcnLl38ZlN7uwJ%2BRwyQ8NUQLx69pHCs2p1ZrzdP1IqIrNtiPFjMMVg7yJ43lusypRxRZWCQMuaIIufQInYGwA3OiWQtWzoqMpOaE3CqmAtWRhJb7sa91IqbhcTBOd6IKvC3J9GsKKYGLf5FHwbqZVw0p0XVvE1pc5h%2FsnXEnrVNYZj6YMiGdvfPyG6kaW7rHl7DkQkbj3HKvxmuzSviJ7UPF0M0XBs%2FVg1JYeMhoo3OEiggw6eEncflIV%2F4A5h6SH8QM0tYY0kLwO2RemNEpk4kJrHsMAHH5skdWcr2avRXpK43Gxxp3XrN%2Bz9q%2BAkXeZrWSQU%2Fb%2Fzt5mZHQe8iZ08OZeIlql5mTSHJ0MFX4S18g5i3IUqLKUhBUKYkkANK01hT%2BsajexUpVbq%2FB9hoDNdsq8pFtClcWe6mDRNstI2nkz0oHHJNqBQ%2FXtkspjqONA4zjAaFgy2lN0gSPxnBJY4VVnfRdxoRY5FnhyWccH%2Bmh2hw7erxazBFefsDhbKCnHq7Ep%2FcbdOVclVOJBgn4C8Y2KyEIGjEn6%2BIwASlMxB0dChzOfzwTNubRcKGhhHHsT44vECXS%2BiyDLxTAPDXXIzDO3u28BjqkAVoHiZY0XD%2F7I0b98JwTuYYc%2BC8OH3FiVEmbW8%2FfjVuejAlJsVT8KkFc%2F1MbfK0Y%2BYAz22SsPAmJ%2BybHMYdm1s3CZRG5QloZYwmWsqm4mEjH48ITSCGBhBI8qxJfCYQmqpo6tUN4KEIMyPzU%2F7iWTCPXdKOzvCfU4y01qBs1C9wf5bkPZ91hfk%2BtIdCg%2F%2FB7PWQx129WfjIkXmP6DK4SJAkADxHB&X-Amz-Signature=a517f7a90d817bdfe596d8b93c5f61f951c7905c67c078f0d0c1adb520d3ac42&X-Amz-SignedHeaders=host&x-id=GetObject)
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