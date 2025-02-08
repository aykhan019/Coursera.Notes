

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=00a1cbfe2f8a8b317a8a59f50a39a004c4514bb24da8436f6e7cdf6277bd81d8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=84b7ce3c9f2eb491835d7b771ee21981ea46220a33e31c4b90ed86c988ab1909&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=aec3b7f22e70a001c12bbd62e48c9c106eb6c2df2bd83bbd57ee1202c1906c95&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=602da62c3bf2747bdbc3116ab8d68c7cef5256ca032f1f31f339187b1c3236b2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=aa93e5dd97c10083bbca6cb0f4650a11d58aa0499f62d9b213c5bed341d8a1e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=edce445b91945caa56456468ff97e76d1ce2b6bc753d6a233f0a540cfa0ce66c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=4fc3fcbd5501e40f057b38b2fd2271cb1894d55de421499639498456bebbb7d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=d202b56447081be03cdda91795496cff6fc3e45c3402cc348d3c04d25c89c4d3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=c8f0d3eadbbb33a0a23b6299cc55f1467a97640d3607f155947906d443393db6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KICJQMB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIBxuaHp%2BQoD4DiDxp5Y9gKTIH0RRCR9RkfYg1xtIhNxZAiEAz6gm9D5wSbrF1wJscTDDLK3uSoiWm5Fdi%2Bw92VfsuUUqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfGTnkenzL3nYSU9ircA0YyuHNvLQ3O1Yh39NDj3xWghEhcDARMW2U6scjrco7vzmCR2bnoUauAHSfcEYgsRyBxKOt%2FfHdwIFfDDY6RDbotv13h2n%2BKaqCwk6W6eIZb33byxIbStjXIClUvvwoQm1HLRx%2BnLLcERiYLMZEqlgb8Nk0wWGAeW92KwKmJThrKBNj7rURO81KfMdhehwblD2gnDXtwBR6Iyulm8llDRBPZMXD1xVZF1ZzqYyOwVEhVOwztz%2F1jBXBV6Bt5ztGuTAt9I1oD6Q2cyJehw%2BYsjOl663W9dKTp2zrRwBivyYnpp%2F1c3cw7NpRNoF7EyytTwSa0W55KC28hNboT5DUciquJdwuvTLZYPjy%2FFz1Q%2BrGA%2F6TJEtUdqupLO90551RB41Q%2F%2Fr1bZ6KuXD3NxsMK7tete%2BMjm2r4EnVzJyBlx%2FcWEZEpUoK1wWtMMTuTsPl96A0kcgDkzoq4%2FRYH9lDUiFquK2Wglupn9sZMRJbRJNNgqq5GHSfNsC0maKxTnWNfHhQDxpvra5zaLMA0WPd1yRo%2FMsI4cTEX5QgeS1A82FeBKSlfvgC4hSkwulWJOrzRkTIcVFqZeRwuePuuLV9Lgc2dBREeQwOVCHnqooCj%2BHH4csAgWzjk1aAOQ%2BWlMNCOnL0GOqUBSZTFYS0%2FBvBhLNWpnEDaoveQfCDyYH4MFRdasrof5Wd6vXO5E4%2FGHVMAEehPMUwoiNGeeb4DwJFHZbrTN0cafjnT1CMqTtyC6PoMPw9fhOC0Aj9sSFsKq%2Ff%2BBUY2oJVJALvjdHrL0fLv65I%2BomgRONNteVDh0JuToNBcMhfm1dSVZ9jp2xsCSGWmkIaYwq2EC%2F40dlE4DNnEOqxmY3nlxZWUg0Gg&X-Amz-Signature=901fca1efe1df2bcfc2d25cf797a892bf972821e391cb5f67797a66f12ea56a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KICJQMB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIBxuaHp%2BQoD4DiDxp5Y9gKTIH0RRCR9RkfYg1xtIhNxZAiEAz6gm9D5wSbrF1wJscTDDLK3uSoiWm5Fdi%2Bw92VfsuUUqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfGTnkenzL3nYSU9ircA0YyuHNvLQ3O1Yh39NDj3xWghEhcDARMW2U6scjrco7vzmCR2bnoUauAHSfcEYgsRyBxKOt%2FfHdwIFfDDY6RDbotv13h2n%2BKaqCwk6W6eIZb33byxIbStjXIClUvvwoQm1HLRx%2BnLLcERiYLMZEqlgb8Nk0wWGAeW92KwKmJThrKBNj7rURO81KfMdhehwblD2gnDXtwBR6Iyulm8llDRBPZMXD1xVZF1ZzqYyOwVEhVOwztz%2F1jBXBV6Bt5ztGuTAt9I1oD6Q2cyJehw%2BYsjOl663W9dKTp2zrRwBivyYnpp%2F1c3cw7NpRNoF7EyytTwSa0W55KC28hNboT5DUciquJdwuvTLZYPjy%2FFz1Q%2BrGA%2F6TJEtUdqupLO90551RB41Q%2F%2Fr1bZ6KuXD3NxsMK7tete%2BMjm2r4EnVzJyBlx%2FcWEZEpUoK1wWtMMTuTsPl96A0kcgDkzoq4%2FRYH9lDUiFquK2Wglupn9sZMRJbRJNNgqq5GHSfNsC0maKxTnWNfHhQDxpvra5zaLMA0WPd1yRo%2FMsI4cTEX5QgeS1A82FeBKSlfvgC4hSkwulWJOrzRkTIcVFqZeRwuePuuLV9Lgc2dBREeQwOVCHnqooCj%2BHH4csAgWzjk1aAOQ%2BWlMNCOnL0GOqUBSZTFYS0%2FBvBhLNWpnEDaoveQfCDyYH4MFRdasrof5Wd6vXO5E4%2FGHVMAEehPMUwoiNGeeb4DwJFHZbrTN0cafjnT1CMqTtyC6PoMPw9fhOC0Aj9sSFsKq%2Ff%2BBUY2oJVJALvjdHrL0fLv65I%2BomgRONNteVDh0JuToNBcMhfm1dSVZ9jp2xsCSGWmkIaYwq2EC%2F40dlE4DNnEOqxmY3nlxZWUg0Gg&X-Amz-Signature=b6b039a3ef78b8221c635d5674009f42a0a442667d2ad5e70d849fd6e86f5508&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KICJQMB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIBxuaHp%2BQoD4DiDxp5Y9gKTIH0RRCR9RkfYg1xtIhNxZAiEAz6gm9D5wSbrF1wJscTDDLK3uSoiWm5Fdi%2Bw92VfsuUUqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfGTnkenzL3nYSU9ircA0YyuHNvLQ3O1Yh39NDj3xWghEhcDARMW2U6scjrco7vzmCR2bnoUauAHSfcEYgsRyBxKOt%2FfHdwIFfDDY6RDbotv13h2n%2BKaqCwk6W6eIZb33byxIbStjXIClUvvwoQm1HLRx%2BnLLcERiYLMZEqlgb8Nk0wWGAeW92KwKmJThrKBNj7rURO81KfMdhehwblD2gnDXtwBR6Iyulm8llDRBPZMXD1xVZF1ZzqYyOwVEhVOwztz%2F1jBXBV6Bt5ztGuTAt9I1oD6Q2cyJehw%2BYsjOl663W9dKTp2zrRwBivyYnpp%2F1c3cw7NpRNoF7EyytTwSa0W55KC28hNboT5DUciquJdwuvTLZYPjy%2FFz1Q%2BrGA%2F6TJEtUdqupLO90551RB41Q%2F%2Fr1bZ6KuXD3NxsMK7tete%2BMjm2r4EnVzJyBlx%2FcWEZEpUoK1wWtMMTuTsPl96A0kcgDkzoq4%2FRYH9lDUiFquK2Wglupn9sZMRJbRJNNgqq5GHSfNsC0maKxTnWNfHhQDxpvra5zaLMA0WPd1yRo%2FMsI4cTEX5QgeS1A82FeBKSlfvgC4hSkwulWJOrzRkTIcVFqZeRwuePuuLV9Lgc2dBREeQwOVCHnqooCj%2BHH4csAgWzjk1aAOQ%2BWlMNCOnL0GOqUBSZTFYS0%2FBvBhLNWpnEDaoveQfCDyYH4MFRdasrof5Wd6vXO5E4%2FGHVMAEehPMUwoiNGeeb4DwJFHZbrTN0cafjnT1CMqTtyC6PoMPw9fhOC0Aj9sSFsKq%2Ff%2BBUY2oJVJALvjdHrL0fLv65I%2BomgRONNteVDh0JuToNBcMhfm1dSVZ9jp2xsCSGWmkIaYwq2EC%2F40dlE4DNnEOqxmY3nlxZWUg0Gg&X-Amz-Signature=41084fbd8062c5d2b922511d55f361b6fc283a7cbebefbfdbf8dc929dbf36950&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=e8f5ed5c7afbca2354479081387aa2543bb43a687bac5a5268fb42866ec32d34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=e1da12bc0e3cb15fa1b7d22839c1ba6b132a42f5fce08d4a7a56d8c0e82cac56&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=f25e207d4b8adde0574bbf9893ca7e438fc056572c4522c11f24cc1d47a8186a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=2235bae7551825142b2f3453d6d62a2715dd9e1141f11f1f94015c6b9c648561&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=d4484dde64e2878fa03b2afa44f559a850737573bc5ae3cb2dd4c2ab4b5f6f41&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULALID2H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCdx3yGqoFfFXgwedxjY6mPeVrzBis0WX3q0BWS4uhKgwIhANdpwXD9lctP%2Bk94NgWSYxWJ1slzgSqFlw8Sw0zMsT53KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJb5UaZbd53oxd82Aq3ANx384QRRR1nWd9PGJUDG0UrW%2FSzGZoJeBED6qGOZrHhQ2Uz2MMAOTrtbdYauZ7dApgdJ9vz7gC%2B1bEq%2FUmjDmM%2F70%2Bd8fb%2FOObLNi8k3OTRj2kqcQxYahzyqQJAOS%2FIA3VGa0ZMlHEzIcv9Oo%2FF8yu9ed9eqc9EGQ%2FnM1Rq59UN1r7MHJ0jGPi0v%2BEY%2FV%2Bmvyw3Wj%2FxmGcNXr9t5gn%2B17%2BjVsAyCpzkQfUB%2F%2FLnGNa5ef1a3PfMU%2FtTaq8Jwcjw2vq%2FCynt1UN841hKjrDXORO6YzK4%2F46BMqTFDXJHjwtshQliTqjDjssW9cgjUcjkdtLN%2BnkM03TMJjEXHwd%2FRdt8bGQ6%2Fe%2BYsKvWniLwNoxBiCnL7C%2BrmO5HW4UhVzgAv%2FCwNkhJQoTQNdaK0tR5A3eDa36pMBtACu5KXXuuXM2c%2BtWNrNCSALlTRsPhTGRNQDQOKpyqTwqhlMEmC61PNNBAaSC3GjdcjJXatchVptEaED9mHbKqg1wz5X6QTr%2FiD3URE1bUvDk1yNhyhpVkhXYuLm%2BCVv104KISbh6uY%2BshlmpmDbAtraBTALwm%2Bz5GoO45X%2FHjzATsKcH%2F45uRPukoaVaqO3tkq1whPekKOrGV6IUIpQ4dTGoUBzOPDCBjpy9BjqkAV%2F6dtQaXa8ytz%2BMDmU3i%2FVkPfb4jZ6Z7RHhdVIxcPcl6I7nnII0tEtATbCbGCxJsgcqmBdbTOFXOdmdDwMWX6XIZ9x09%2FujCMd3ggeLk3DI4bZmVQtZZ6F7Kk8hswUuWCslRQ%2BhAku2eXkCW1ETUStJYsZ43qLktrEFmTGiUEg9YVvaraH2Zp2pYA9twjizFI2KexTXb6IJ9lbo94mHdtM%2BIaMj&X-Amz-Signature=0febf5093ebdf3ca6b852af51ca02d16b57f0fbc45af95ff8ecd0140c56d93ac&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=825ab4d30578a868c4cd7eff8eeee137a5ad5c2018e849be93fa3e11977a8e2e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=e040e11ddf0ff365ab3c8d392ec7441f7a3ffb3134910c3eed96348ca54ee115&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZSRUEHS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCMlnA1pIAKw9pZf%2Bqwdw5Rnhi4P%2FfCKULHOL7pzd6OJwIhAJs%2BKOSxwA5GAflXEAnCqEod9y0gQ4MUfk7BT1Kz8naFKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLv1cp9XcdX%2BzCZk8q3AMEJh%2Fr2Y0wPBV5x5U9v%2B2uK%2BS2uQzGY0%2FWEuBM9AywV0ODnYfKkHpb21fflnau4zRvXP%2BNh6GFUhjNyLzk35m5C2axLHjNrmVKvydiQAg%2BJAF7TAplnxEPbo6qvBHxt7w9SW4VJm33ipHbPRto7X1ceWpgS%2FsxoHk0EzSOpGjStu4pvfvfGT9z%2BmYQc%2BSL8S%2Bzbi2lCYW4cgjZvxygyk%2FAYfRWTxycWj5poJYl0zeZBiTnMT0%2FINDHoj8aF4EdUboTRlIxZwTd4sMM%2BeabyrPgs9pr3fo70XEDLZv62xUgcifklJLPfLskeymKAWB%2FfYKtj597DMGhwXOjaKfK5LAoO6atwxAyyv94ku0Rgs%2B%2BKKZXNgbhgA5tr1ttwJYt%2FOZakgjomZgGck%2Ffridhca6jlfW8AyVoZnF48KYQJCc9iSjCcLZc4dWPrOC%2BJ8j6eK4%2FL1XSTOoXFKfE5t82g0Luqpds%2FP7AeOi7c5vZKP5JxCG197VCnmNcWqE1wuL0YssuBHj9GGOsnveUVGdDHqVFNYCFSn1wGf2XbBVvCm53qYObcZtYPfO0ZS1NhVhl96HmQ3NPxUMWC50wMzZ8OtIlkhqRG0UdJOuH%2F8sIrAIGiwUIh7SZB7hOgd5m9TCtjpy9BjqkASaowIROGC1E8qLXxur4tJdQ6JvQzLKIjivaPfLeZ11b8iH1wOd3BDiSLwzm64LgN5S%2B2NUdI74DFb0Es5%2FZKsu0E4eBpGpKeWaXY%2F6ilC9duo9rKq7LmJeHUr%2FdQxAZSrm48Kf1wFgGKlSi40rQKUjs%2BJK0cVvyVNF04EoXS5i7zmBbqAom2WUnb2VOwzdfyOTLF6gLeBlx%2BV3X8LxnI7NUXXia&X-Amz-Signature=fb74be53d905f0145edd441f9f9d90a2e42dbdbf5e56c33925c5d2fd3dcdcd4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22VAFNF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDQs75VgfgRTGlCmDrI0L7G8%2BuDwKSgVJDW%2FcJQkLSjnwIhAKIqYJQPtCU5N9vZ5Qbls5RX%2B8Vk7oUrjIB%2BCGSPHRLdKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc5Vp%2BQdQTp7rFtWgq3ANJ6Z6HatRC0kcHCUzGiDvojwzflQnMIPM6JRQRhQsiae0Trnhfun2bkCZ7zukwuDmifcLjzGP6RBxh%2FFmqPVNYtw%2BNwUmx%2FXLXjYALXtNm%2BA%2FYZZplLDJAFNXzXwC7WYw9HXHhVRKqhucWbusVJABdt%2BTiZ719f781iffAY3Fa4Sgy4UcjbFSna5x%2F9Ui8HSwPvhrpOjxsAYlt8Qbwp2UU77fAW%2BbnAJCFXiOljPRcnUDkp0zsz30hSToEZMwkwnNCN3zPC%2Bxe4V6R07HlCmm0EVjZlIdmmEopJMGbmug%2Fxwbi66wsPq4aWget1QiYRfiwtydM%2Br8VslqkKCJa5TrFhtQA37VKVZ5UACrmFKjqq%2BPKqZFqaIzA3gtL4TqrEl1HYL%2FqjB7VFkH2uLl7T%2B%2FCTNQpQblF4n0sCz8Ls8D08xx87RrkR8fuWy%2BlzXUG6jRpgnCINs8d4XPx7JhegPt9trxUsHklSiPjoILaQlHGOdBkikV4ETwEiDRGm4ALdRg72g0rVDTz0sxAMAAhQGD82%2FixzohbZphpnwhlLQRFT4MQ11sKJb1QUBAqpEIjPwIoAjkSeqwq89s6XK94TzYsr9otyQCeIu3aOgUYSJZlxfu6Kr427tzfq2XdAjDrjZy9BjqkATCIEGswjAOxY1tMrGDTyr6Iwp%2BBLvCeK6kx%2F7RoMHqBIm0IWBcD8dhnCH1OIulkvGsacGsDcyIEsRCBFytPTTwradqTaa3zTp6JWov11XQaUuZosn%2F%2BDwT2MaKdqCrXMoP1hW6sadV%2FfSsaKoN%2BZfLUCcaMPXsG87vYaJ9N4Fku%2F%2FWnxDrnSz8s16MeXDeSoqPjy77K6eTph0%2BCT7V5xZF6l3yO&X-Amz-Signature=5817e942d1a820f6f6ac7bb2a07365bf792e41819b44ddf7b531e62beac9d4ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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