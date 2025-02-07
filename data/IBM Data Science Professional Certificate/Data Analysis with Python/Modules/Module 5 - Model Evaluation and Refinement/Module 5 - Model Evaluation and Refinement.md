

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=3285d93fbd7512c0f9e5c1789c76bb4c05ab3fcba4020db02dfe19e38753769f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=1e931dbce6104396ae3c7e444802bc7c8cc5134d2753fd3788970973d5fa1c33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=22e19890f06642bff09286e00939b18bcd3837e25e6606280d17bc2e3a0ccaa7&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=72a277dc7b4015dd2df840e707ea65feda8650904f500d93597d0cff0c32d13c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=faf5cc302892c42e25797b82c72772a5fdf283bc67d52c1e526ba511dd089486&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=fcbab634535819b3b0f5b2123c5f051e21c9c74cd00691096812335e1395feb2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=1b786dbe74992277968a5638d80130aa93c3bf6ff8bfd53f7f36ee541a29ea93&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=077651580e22fbaf47defa85b538d6da1adc70125028a2f7c945f9f4709f835c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=b7872fdcda95327a87395737491690ac22facd25a66b819e1a2f6384de247e80&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFV57XC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIEB0EzUUanvyqcDDjq7ZRwJzZIS713Cbrrl1c3mQ%2FQMeAiAvFFSPDNwnvQKzuS2FjJnK6suFU5ih816nmLw5cXdCOSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMEGQ6yeuY57%2F8aYK6KtwD1Glz4MXizA2Wv0p3ddeZAzYlrTqct6Gf8JC3UxeQCwzAY2qmwgeUVD12Xr6Gplk9%2BLwMMgJUJF2tB5anw8iYyehirodz6DK0pyqerVNs%2BsVr%2Fx%2BCR7%2BgIrjmMBqeCH9CRbfeMMjrKT1PEeuQ5l3eH0xV5VXrIPMy57QuaBksurmy1K9Zl1DV2SPUjHsX1JnR3fBu9ULmMyWSVVdCMXdORbXKWhwND%2BGs8iUxDCtiRuamoKuzfUh0giUHwtlHciklXLwjLaKfBDtks36aIxinAKGdI719n11C%2B5u2aRU3xYcLVm2RXVe2RXP9%2BMeZVeZgjtskDTIbogabRaqVThgvNHqOVdhoOFRMscinlAGbfDWlqXqfgKdRLL3uGiIlkUvm0KxnDQytdxeMIcEn%2BoAYpGPh05xjKxVtfK3D%2F9CRadOvn2aIcj4yhaWuKFu1Tj8ipZ1%2FbQeHkSGcn%2Fmmd5YEM%2FcZ7Vh8%2BhOqCxPgo%2B5Z0PN0vnIF4YhjMD9KM%2BJuBf0xTTxl0LmARZFRidQRmCuo4s9ONmx%2B89lqCUV9uoWtkXjm5XZ8D%2Fwe9k3Re1XaUGxRxU4ovgwe27ya3RFNE%2FKiTY1lctMIV7HrbpIJq4qpxviEObWjeN2ccxWvquQwrNKZvQY6pgGMZyeB46RS6QdYEZZ%2FCHjI%2BzAWcOSqL6xVnZfGO%2FbjEvtTrTlSa0sFc1sYu%2FJYszj1T22vYQNlob6wiIr%2B59c3qdLRLAvi2pfUrOZ6ADs1860gz43yo44l0gV3uN5WxA6cQdlufqxpFbT9tw5I9ZqQbm%2FhvMGSI9tu7HkFWSPkrnhbYdkWQqeOvOa3VUt1%2F4WfseEE8TdFvgoFJD90I9KQHefxVLnh&X-Amz-Signature=ce69b3ca711f4fabc98f5842a2748a9d24de5e80b2caba586775790b5c5f9e3f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFV57XC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIEB0EzUUanvyqcDDjq7ZRwJzZIS713Cbrrl1c3mQ%2FQMeAiAvFFSPDNwnvQKzuS2FjJnK6suFU5ih816nmLw5cXdCOSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMEGQ6yeuY57%2F8aYK6KtwD1Glz4MXizA2Wv0p3ddeZAzYlrTqct6Gf8JC3UxeQCwzAY2qmwgeUVD12Xr6Gplk9%2BLwMMgJUJF2tB5anw8iYyehirodz6DK0pyqerVNs%2BsVr%2Fx%2BCR7%2BgIrjmMBqeCH9CRbfeMMjrKT1PEeuQ5l3eH0xV5VXrIPMy57QuaBksurmy1K9Zl1DV2SPUjHsX1JnR3fBu9ULmMyWSVVdCMXdORbXKWhwND%2BGs8iUxDCtiRuamoKuzfUh0giUHwtlHciklXLwjLaKfBDtks36aIxinAKGdI719n11C%2B5u2aRU3xYcLVm2RXVe2RXP9%2BMeZVeZgjtskDTIbogabRaqVThgvNHqOVdhoOFRMscinlAGbfDWlqXqfgKdRLL3uGiIlkUvm0KxnDQytdxeMIcEn%2BoAYpGPh05xjKxVtfK3D%2F9CRadOvn2aIcj4yhaWuKFu1Tj8ipZ1%2FbQeHkSGcn%2Fmmd5YEM%2FcZ7Vh8%2BhOqCxPgo%2B5Z0PN0vnIF4YhjMD9KM%2BJuBf0xTTxl0LmARZFRidQRmCuo4s9ONmx%2B89lqCUV9uoWtkXjm5XZ8D%2Fwe9k3Re1XaUGxRxU4ovgwe27ya3RFNE%2FKiTY1lctMIV7HrbpIJq4qpxviEObWjeN2ccxWvquQwrNKZvQY6pgGMZyeB46RS6QdYEZZ%2FCHjI%2BzAWcOSqL6xVnZfGO%2FbjEvtTrTlSa0sFc1sYu%2FJYszj1T22vYQNlob6wiIr%2B59c3qdLRLAvi2pfUrOZ6ADs1860gz43yo44l0gV3uN5WxA6cQdlufqxpFbT9tw5I9ZqQbm%2FhvMGSI9tu7HkFWSPkrnhbYdkWQqeOvOa3VUt1%2F4WfseEE8TdFvgoFJD90I9KQHefxVLnh&X-Amz-Signature=cfad21bfb82b7703f24278824ee97d0058371cad60a1f36451d4bba70fb9904b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFV57XC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIEB0EzUUanvyqcDDjq7ZRwJzZIS713Cbrrl1c3mQ%2FQMeAiAvFFSPDNwnvQKzuS2FjJnK6suFU5ih816nmLw5cXdCOSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMEGQ6yeuY57%2F8aYK6KtwD1Glz4MXizA2Wv0p3ddeZAzYlrTqct6Gf8JC3UxeQCwzAY2qmwgeUVD12Xr6Gplk9%2BLwMMgJUJF2tB5anw8iYyehirodz6DK0pyqerVNs%2BsVr%2Fx%2BCR7%2BgIrjmMBqeCH9CRbfeMMjrKT1PEeuQ5l3eH0xV5VXrIPMy57QuaBksurmy1K9Zl1DV2SPUjHsX1JnR3fBu9ULmMyWSVVdCMXdORbXKWhwND%2BGs8iUxDCtiRuamoKuzfUh0giUHwtlHciklXLwjLaKfBDtks36aIxinAKGdI719n11C%2B5u2aRU3xYcLVm2RXVe2RXP9%2BMeZVeZgjtskDTIbogabRaqVThgvNHqOVdhoOFRMscinlAGbfDWlqXqfgKdRLL3uGiIlkUvm0KxnDQytdxeMIcEn%2BoAYpGPh05xjKxVtfK3D%2F9CRadOvn2aIcj4yhaWuKFu1Tj8ipZ1%2FbQeHkSGcn%2Fmmd5YEM%2FcZ7Vh8%2BhOqCxPgo%2B5Z0PN0vnIF4YhjMD9KM%2BJuBf0xTTxl0LmARZFRidQRmCuo4s9ONmx%2B89lqCUV9uoWtkXjm5XZ8D%2Fwe9k3Re1XaUGxRxU4ovgwe27ya3RFNE%2FKiTY1lctMIV7HrbpIJq4qpxviEObWjeN2ccxWvquQwrNKZvQY6pgGMZyeB46RS6QdYEZZ%2FCHjI%2BzAWcOSqL6xVnZfGO%2FbjEvtTrTlSa0sFc1sYu%2FJYszj1T22vYQNlob6wiIr%2B59c3qdLRLAvi2pfUrOZ6ADs1860gz43yo44l0gV3uN5WxA6cQdlufqxpFbT9tw5I9ZqQbm%2FhvMGSI9tu7HkFWSPkrnhbYdkWQqeOvOa3VUt1%2F4WfseEE8TdFvgoFJD90I9KQHefxVLnh&X-Amz-Signature=335a105d88061e1ae144778ec769bd05ddee08e05d7d0de15af6239248cc52bb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=b62cea13b118de84984859a2468aaa063c21e0d58ed6beced2343a1c80b936fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=4e9150ab18c463c9369aef85796683d4da07e62edbe28aae79526afc99c1b255&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=120795e8121fec77e6698e072cc06b2afe15f53ef6667dfbd36ac500890be53c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=c98d2388a6145329413305f56d2840738d73570980aa7e51046863ca357b62c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=f1ed1769c50b55a0e5efb67010ebaf26eb0339595358eb85c19fdb9091d7e7cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIEJH6Q2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFSLa4o6QhNH8Xpiu1LuhtShcnGrLZ8U%2Bw9dn2Jsied9AiAY8kZgi2YsKAwl2haOgCqx1oNcEYXinuO%2B%2FOH4uy9npyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMRodRYGbrJ3IYERbvKtwDaokGeJcmlZGYAi2pOJwGaNFbR8JPJN9U%2Bxx7kF3335ij9FuOXBB%2F7gsXGMDsvZ%2FrzcusvvdGrpQT38tKIOhy2mNbzk%2B7tsdaIXXUpQyiyeX2ZD84oML%2BjCxPrOnYBBBriQq96brrWtN%2F7NUe4HvlMRIP%2FxeLB0Eom7nJKB3MDB5%2FVJaYbbw5Bf27Mm8BXSxkXcQI8%2BT6B2FG7nXdHS8b%2BbfwyWySDc8rNEa8g1PgW4UiVsMOXPlK4WcmhV%2BnLIWH4PmxrrwMIfktScTkkEcubeYfWY0NFfdRaRSGfQAZaOPGzl5zLL8YBKAOALTMeI1HTVdOEqDcFAy57i190gqYCoj1zYCy92KV%2FTa%2BDXoX44icBnyUKdEedvz7TUBMXanDYsZoTLholQXpKa2m%2BP62o2YEk0N9oHOPDlIvZ9JzAmpKBsgvi1tuU%2FfSTQaR9h2%2F9JM9f9UKCdGMhDZrgrwr0%2BbsSErcysHwfD5jHU4%2BPxgoruQhNjhRODYC9K55ZzO2qfk%2BlFvB%2BS6I0cD7gZxH4XEx2%2Bh4JDtbrLAi1N4gwO%2FRRjKyNZ%2FSad%2BvYHbu1qmiXygmg2Hujck8KwZZHxyyXeZMZB%2F5X7nt7sSPHZsuXRVebK3Sw5uVCXaI6TYw6dKZvQY6pgH%2F9CAeTeJyig754mg38iFUFhlCWlZGJQIAf9S6uPkQUEG9OhGdxUl4wjEIYDpVHrPmMvDlvPHynspptc7TBYaiWJ2oNL%2B42vMoPd%2BvACMD4hU96WXXlKvhFDTGSybc5AAmRHc04PmYoKQmv67ezLm0YfXldxkAQBfN%2FZPNQT%2BGE2%2BN1LpFc7GdhMfrWYrZPK%2FptkGmj8F9Lqd8FHAEwjcd%2BF5wQOER&X-Amz-Signature=b1da2705bd7494f1715cddfee9040e0c570fe46563daf6e74c0b29fa7a08be61&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4G46ME%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD1a9XsLWTRxPCUsWV722ry2F9%2F%2Fyqptlc527sSg0g6qwIhAMTX8d5IvuYtj%2Fnb3WYhPndjrtBS7v5S1JbOAfRjewnQKv8DCHwQABoMNjM3NDIzMTgzODA1IgzxCJuYkFrUugE3mHsq3AOiB8bTKigdbr1xscieqwIRsJ3VHjRo0oajiBy9%2Bx9HeP%2Bc1A%2BQ9Hc3lygu41vyqRdqY9tGEME7KSk3im9lUQrafn4fAeChRoHPfVItEssWFpAkKaZO25NwZfTOd4UAGNcpmd31K9q0bFGayaohEigDfMwbDu2Yf3erfuai9ahjRHNyYzNkyfHP905pxQs8%2BE0Ml3jUFOQ6TjDNUeX1Ie9oVjY2j7uPX6HjpEmCjdsjxT9OKxBe5AdJX%2BHTeKX%2Bo1kej1y7qZLf7rLo%2F96ajA8u3l26erXdu2RRmKMkYcoy30azqCiH4ReLgJuy48Mb5N5%2B8jXxEcm2Wt%2FUljdZ%2BBlZeSARfoyzN2PxfaJShKBQ3PQAd7fuNPuna%2FJHYhMojyJpy9nNRkCzxWFgiz4lXay94Pf4KuBbvQ160%2FbKTyJHOINV8Qoa6BJTz%2FM4VDM1GmKNzDarZQ6Tguj%2F%2B7jlY3hH5cVE69h%2F6XOkfChZOxY8eeR7jXl8CrPvGR13HEeLU7UbCGAfM20%2BBiAjtPr3g1ozTKau2iJ9SCJ1tEperLECSU4ox3lmO%2FjRTDejUvQd2BMtuVNCNsOvfiwFClbWRZ63wzgiHVmrAa%2ByXE4%2BJf%2FTl5lyXmXInon%2BUdTD1zDHtZm9BjqkAW2BhJ5hePViqYwZL75x%2BdORGa9gaQt1W3zqY5lDt58ioJhF1MLFHeQc1DFVGxqU8XaSCpg38Gbo9SgEyZHcZGZVrs9WpjnZ606bz7PDdUUyhWh%2FM7eSCuS4EGefVJrOXRXCHc3o6ZNCEp5iWOy8%2B5dpRo1VhTNTRKsa1KEvw1ZE6xzGCH8A1duneOrloz7beT778ZYp2FCeYmi%2F1c7seVSacNPc&X-Amz-Signature=0c8f02cba627ac1ac1821d454ab1683c4dcb9becf22371bacab1d026759b0c33&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4G46ME%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD1a9XsLWTRxPCUsWV722ry2F9%2F%2Fyqptlc527sSg0g6qwIhAMTX8d5IvuYtj%2Fnb3WYhPndjrtBS7v5S1JbOAfRjewnQKv8DCHwQABoMNjM3NDIzMTgzODA1IgzxCJuYkFrUugE3mHsq3AOiB8bTKigdbr1xscieqwIRsJ3VHjRo0oajiBy9%2Bx9HeP%2Bc1A%2BQ9Hc3lygu41vyqRdqY9tGEME7KSk3im9lUQrafn4fAeChRoHPfVItEssWFpAkKaZO25NwZfTOd4UAGNcpmd31K9q0bFGayaohEigDfMwbDu2Yf3erfuai9ahjRHNyYzNkyfHP905pxQs8%2BE0Ml3jUFOQ6TjDNUeX1Ie9oVjY2j7uPX6HjpEmCjdsjxT9OKxBe5AdJX%2BHTeKX%2Bo1kej1y7qZLf7rLo%2F96ajA8u3l26erXdu2RRmKMkYcoy30azqCiH4ReLgJuy48Mb5N5%2B8jXxEcm2Wt%2FUljdZ%2BBlZeSARfoyzN2PxfaJShKBQ3PQAd7fuNPuna%2FJHYhMojyJpy9nNRkCzxWFgiz4lXay94Pf4KuBbvQ160%2FbKTyJHOINV8Qoa6BJTz%2FM4VDM1GmKNzDarZQ6Tguj%2F%2B7jlY3hH5cVE69h%2F6XOkfChZOxY8eeR7jXl8CrPvGR13HEeLU7UbCGAfM20%2BBiAjtPr3g1ozTKau2iJ9SCJ1tEperLECSU4ox3lmO%2FjRTDejUvQd2BMtuVNCNsOvfiwFClbWRZ63wzgiHVmrAa%2ByXE4%2BJf%2FTl5lyXmXInon%2BUdTD1zDHtZm9BjqkAW2BhJ5hePViqYwZL75x%2BdORGa9gaQt1W3zqY5lDt58ioJhF1MLFHeQc1DFVGxqU8XaSCpg38Gbo9SgEyZHcZGZVrs9WpjnZ606bz7PDdUUyhWh%2FM7eSCuS4EGefVJrOXRXCHc3o6ZNCEp5iWOy8%2B5dpRo1VhTNTRKsa1KEvw1ZE6xzGCH8A1duneOrloz7beT778ZYp2FCeYmi%2F1c7seVSacNPc&X-Amz-Signature=bc8389045971387d2a94f5dcffcc748813c02006b4eaba1ed9eb28f2e283e3da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PEG47VR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIGhnVuFLilYR2GSqlMdnGgKJ42HYy2UTeyPGhqD%2BUEZ9AiEAiwtuWUaQsO%2BqovbVi1qAcZsF0pyrHbXoGLhPSMjhsEMq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIolpRfWOZdDuRuF4CrcAzGzD%2B6lJR6RmMlzZHvmoqYZKVhZ5ixKKY1HWwfDurl4yNL3Qtaok9Po7jc6jYt5K8f6Y%2BMXvIAFiS5a18LbOvGOKfElRrOe50W%2F5muyptICqRVq5SRvcf9aasYoFkp40NYJ6v1ExBwv0c%2Bw9AjjR1GsHyaOUbLKHyDIHVAJ3UwlAKYGy%2BqNZt2NAlseVz8s%2BG86YRkXrigchkREIdWMi1YKAxAOUVN0rpIKiFTlS%2BhVmAjxLA8povcBJVCKJx2ptj4s6EWHXnx30nhDeqONypBMinR3GzIntRcpYH4mUSnf1KmU%2B4HZcGHoCUj02Ho1TPz%2FCmDviQK0GxhQVVz1TAIObt8fWBI8Asp6HbFfMGS4uQ%2B%2BGoURqCal%2FHMvaG12vXS%2FER4hloIcW%2Fg8KF0Q1aSN8xXUbWcTiUrY2ayhm37qhjVaG0r9kJRwfjCda6PbsXY5UxhCk2j2AXx9a%2Bmb5YYVVUXTPqEUfI4fURBG8EKXXTxm7ubpHmiGPwrb%2F3LbNrTdG9OyGvFRjsN1rwzwVXp6F%2BnI%2FPgDrGNjXlTPQx3re3PImdYm0zGpZ0rw5utthUuPDSgEg37B2AoVw%2BzFl%2BgR1GnUVVRQLtb97P6XeNs7YIsTp9T5hTfKaqv3MJnTmb0GOqUBhOlVxPGS9S%2BsfWbO2K9cBXN0vSDurOJA95m1TzjuhQ%2FAC3OeleZn2s1wCGSd3VQ%2BdyihENhB6CQ9djtmUCxGMyaalnuK%2BSs87tWjFtjb23h3zbcHXYWMjB9abbTbsA6RJa7q%2BMSmtb%2FfQ3Icm8hW6pV63PSeFfIyQgffoDrDy2pXtkGdGTsPeoUjr7sCR6hohkWo4kacBXKXLOK%2FHTyBhWKxffUx&X-Amz-Signature=d404261ecafa075a75f6446cc3c99e3a8a978ccdc7e20659fcf952cf281e3ae1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG4AMFO5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQClRne0YD5LS2a9D98nXUTbcLIt%2F8St7AGVD8Lm9ka97gIgGJoHh3LufNUtGkWKZfKEJQhn8eX6%2BLyi%2Fb63uUpZTGQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLGeXb9jMGjQdcVGgSrcA7Uxr8QurN4Z6tBpyRCLgRy2W1SEtAiWCRuRTdisXg89aqglI12yteRY1vSXjHQ8L0A%2BQwKRrETYuyvfHuyVDNHAK7NfbJLD8keLkWidnfO4MuG%2FjjwjXkSxMTXHYmg8d8v9%2B1admv86qXDTNCIC0v2Gbmpn0X8kykSFN3CbmwcTlQiFiVyZ56wcyRVYOPs2DY5X2MFbOwN2LwU0WO%2FXD0KJapZwuwHCsxHX7Mw3MruyIg5S2rQ9LLELYFc6nRk4KC9d3%2BuGcXuPk%2B9ZEKKCTlv2g%2BO8LeTIurV4CigJEz4iGF5kLfxFBL%2BhkzBtOkrJ519CiL7PxodNZ63Fs8UuxT%2BJcgwcvzjwC2Emb0N8AW14YFA%2FqCUE0SdY3J9InUL%2BSkmgUwEmLurqvosVKuGcTuo2zqzRnW%2B1B8gIcGYqQeC0vI4ghZYn9lRJN9Y4AnMvxWi%2F3RIpajx3FFFgq6hLQxWv4Se0dkeprX%2FPe72I2W%2Bnj2AbFtAPgMd0WKqBmb8TbB64NEHZNTPiau99mWaPIyUvlajdYQH5YbqDbhTQSGqiP1Vb5jCowoAdsK2NDKxrqIfijQPNQuZf0N5E3cdeo9fc6UL6UUKlMtJuIve9BCo37i1307kQw53jVuT7MLXSmb0GOqUBQSrah3XNPQ4bzFzjSBnHXohQ%2Foi6EiYP%2BKncOMsjkj5qSRApT%2B48pYyus9n3Kk6KscKeguZsMk%2BmGVSwpz6HtVk%2F4qCnngBDkBi0DN5fig3OIA1%2B08EXKHTVf7pHNlPBDnoF4g0Zl2PvEsyPs19WeoixpGZYxLyODt7UuNdVDIbCxCIJJGp9Fc39ZrACkPZw4tZMiKQuJw%2B76BKsYN%2FH5cPSoCtB&X-Amz-Signature=71d03fee50ac0f182df31f0866da8b858e1dd8d3ab92a805af8d61cadf913b39&X-Amz-SignedHeaders=host&x-id=GetObject)
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