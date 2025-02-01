

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=f0e4957e56591bcd19333f7c0c34e92bb4c891b965cbec0b45fccf0601c412d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=86217f8862b7ef020be4221e8b96fca14641f5021904471b871f2b96d73f9b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=366d47498dccf584862abcd5697bd2d23c6cac67f8ef40a064a824829dd0f851&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=023dfa47f91290ae5477dcfd1974ba16b7ad3cce4ccc0c209fc7b2d1154d00d1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=e4d2b4c31ca13cdacb28b7144b23c3ef9546644a9d0d55b56d065118445a7eee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=f6aa83c2263fbd125eb8f6fc5538c7e1e4b4838dc4821a7f379bc27e4572c151&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=d3ceb415f55132d1e5dff610abe74244c90f0db650efaa035588e576afc8419a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=ff6553c9355c34aafff5dae5d34b7b1f3428715a4a46468b965e41283925c08e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=1ed275f9bac5b3e5c9e269fe8d870ee6c78ffd0f46da098d690f432e8a9a8402&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3TSUKJ7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyrpJySzxMyMm2WRnP3gSEwZRtUrqIyQ6iO7SoCrPRgAIhAP%2B%2FYJ%2BVQsiokFNxokY3jqPY3clupmpZhCGjkoJ4DO0oKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu1MvjYzYmz9NbR%2BAq3AMPtUtaOBsWFzs364qmhbHe0A2XXV9MLSyp4Od7zA13Rg29sZhf3r3t6nid4V5tvpSH3Go7FP%2BuhSjclgMpY8JcgdNlInXrtH7rS%2FlXuC0iw5k813vwfpnsJ3ONI9HqYpwXuc4PGtHybtddqBwdwYUtihaG%2B%2FuUFq9%2FuPt5x5B1cevT9DXJdRlyFCpnwATJCHf4Hm8FUKaJK7SptVOcLWd%2BNms3DIQHOedxh35rV%2FVLQqSBfb4r%2ByzHK5ZqliLImXdir2nMA5Plfl6eg4ZRRwI05cjDITKUkIcKAsf%2BHtk3QkSptvKtGg21kOJXbw0QghlZMwlvvybnbcAzJa8P7Wmry7xaassfMpHbyNgn4xDW6rsrFAuKDoncpXaikHF%2Bo6mn7x871itAUQFBwvXM5gQ6FDIInAiXxN5mTyuTFTw4dd7Qt2sEqtqZSu8be6IM7WonkBdXLhyaItBZMMxWs%2BFm0ySeNqcZaWVJBJJaVcobVlsPhBY%2Bx%2FTAcR4VksuFgR6lAzLFezvZ5ZXOlHc9iZxRESKjjk9mXeFkkvFl%2BoOnvC1FW09%2F6GjupqqDWGIjDC7rGCjeWTLZxhNSCDJl49Ib7wB6n3apXUnO3JHQZr8NBIuWjJ3rtZ1m5jXchjDF9vm8BjqkAaItADCXN5YCG5iSpwGOlxgxPkk1119u%2B7I71%2Bb%2FK5NjPKJkjOp0%2FDqgcNJSv%2B%2FInivY5JtFc0tIeU8nNkxYe%2FifXC%2FY9ZTHpeANEsgIMWKNOuqP7W1UihI%2FyzSRHX%2Ff%2BRM1IvzMYdB6ohIpT12lUfwj4X%2BJ8RY1ohCynk5SyhxbwTRm9K4Rdzq9EUlq4bxsSxJvCJ9qmmmJOKeaienH0ngu2cq6&X-Amz-Signature=cb08a719ec04ef96b751b02b3d69f2df2e5dd279ffc0712a41d85f68eabca7cb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3TSUKJ7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyrpJySzxMyMm2WRnP3gSEwZRtUrqIyQ6iO7SoCrPRgAIhAP%2B%2FYJ%2BVQsiokFNxokY3jqPY3clupmpZhCGjkoJ4DO0oKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu1MvjYzYmz9NbR%2BAq3AMPtUtaOBsWFzs364qmhbHe0A2XXV9MLSyp4Od7zA13Rg29sZhf3r3t6nid4V5tvpSH3Go7FP%2BuhSjclgMpY8JcgdNlInXrtH7rS%2FlXuC0iw5k813vwfpnsJ3ONI9HqYpwXuc4PGtHybtddqBwdwYUtihaG%2B%2FuUFq9%2FuPt5x5B1cevT9DXJdRlyFCpnwATJCHf4Hm8FUKaJK7SptVOcLWd%2BNms3DIQHOedxh35rV%2FVLQqSBfb4r%2ByzHK5ZqliLImXdir2nMA5Plfl6eg4ZRRwI05cjDITKUkIcKAsf%2BHtk3QkSptvKtGg21kOJXbw0QghlZMwlvvybnbcAzJa8P7Wmry7xaassfMpHbyNgn4xDW6rsrFAuKDoncpXaikHF%2Bo6mn7x871itAUQFBwvXM5gQ6FDIInAiXxN5mTyuTFTw4dd7Qt2sEqtqZSu8be6IM7WonkBdXLhyaItBZMMxWs%2BFm0ySeNqcZaWVJBJJaVcobVlsPhBY%2Bx%2FTAcR4VksuFgR6lAzLFezvZ5ZXOlHc9iZxRESKjjk9mXeFkkvFl%2BoOnvC1FW09%2F6GjupqqDWGIjDC7rGCjeWTLZxhNSCDJl49Ib7wB6n3apXUnO3JHQZr8NBIuWjJ3rtZ1m5jXchjDF9vm8BjqkAaItADCXN5YCG5iSpwGOlxgxPkk1119u%2B7I71%2Bb%2FK5NjPKJkjOp0%2FDqgcNJSv%2B%2FInivY5JtFc0tIeU8nNkxYe%2FifXC%2FY9ZTHpeANEsgIMWKNOuqP7W1UihI%2FyzSRHX%2Ff%2BRM1IvzMYdB6ohIpT12lUfwj4X%2BJ8RY1ohCynk5SyhxbwTRm9K4Rdzq9EUlq4bxsSxJvCJ9qmmmJOKeaienH0ngu2cq6&X-Amz-Signature=809c48f1aad987559187b4829d18fc583547d02631ee3f5c99ee8eab8a1813a8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3TSUKJ7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyrpJySzxMyMm2WRnP3gSEwZRtUrqIyQ6iO7SoCrPRgAIhAP%2B%2FYJ%2BVQsiokFNxokY3jqPY3clupmpZhCGjkoJ4DO0oKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu1MvjYzYmz9NbR%2BAq3AMPtUtaOBsWFzs364qmhbHe0A2XXV9MLSyp4Od7zA13Rg29sZhf3r3t6nid4V5tvpSH3Go7FP%2BuhSjclgMpY8JcgdNlInXrtH7rS%2FlXuC0iw5k813vwfpnsJ3ONI9HqYpwXuc4PGtHybtddqBwdwYUtihaG%2B%2FuUFq9%2FuPt5x5B1cevT9DXJdRlyFCpnwATJCHf4Hm8FUKaJK7SptVOcLWd%2BNms3DIQHOedxh35rV%2FVLQqSBfb4r%2ByzHK5ZqliLImXdir2nMA5Plfl6eg4ZRRwI05cjDITKUkIcKAsf%2BHtk3QkSptvKtGg21kOJXbw0QghlZMwlvvybnbcAzJa8P7Wmry7xaassfMpHbyNgn4xDW6rsrFAuKDoncpXaikHF%2Bo6mn7x871itAUQFBwvXM5gQ6FDIInAiXxN5mTyuTFTw4dd7Qt2sEqtqZSu8be6IM7WonkBdXLhyaItBZMMxWs%2BFm0ySeNqcZaWVJBJJaVcobVlsPhBY%2Bx%2FTAcR4VksuFgR6lAzLFezvZ5ZXOlHc9iZxRESKjjk9mXeFkkvFl%2BoOnvC1FW09%2F6GjupqqDWGIjDC7rGCjeWTLZxhNSCDJl49Ib7wB6n3apXUnO3JHQZr8NBIuWjJ3rtZ1m5jXchjDF9vm8BjqkAaItADCXN5YCG5iSpwGOlxgxPkk1119u%2B7I71%2Bb%2FK5NjPKJkjOp0%2FDqgcNJSv%2B%2FInivY5JtFc0tIeU8nNkxYe%2FifXC%2FY9ZTHpeANEsgIMWKNOuqP7W1UihI%2FyzSRHX%2Ff%2BRM1IvzMYdB6ohIpT12lUfwj4X%2BJ8RY1ohCynk5SyhxbwTRm9K4Rdzq9EUlq4bxsSxJvCJ9qmmmJOKeaienH0ngu2cq6&X-Amz-Signature=f691af1d92e57f04e64962e5592734edf8e86d6e2f6bb6c1989cb930e8efe61f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=b190a256d0bdc17bfd4e5a3d292ef0cd27eefd37662d04c8b207bccd5f5f2c36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=62d018a45908f353d9bb5f5e5f4ca64950512f8d495f02ab4bb6998a8631e0c7&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=475dec21d4586d4d02af5f71ac9efb408fd855bbc38c3ef5f4da80d83372972c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=5728e4d7a8dd336d628d28ab7b9b7057c5962e27a7651c686486d0bf382cd7d0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=3a9dae404d4041831747dfcb85ec3e1ce78092f9b6be36c5d5e5af723caa9b11&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BAWFH3Y%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHsFdyAAiXTJnw%2Fuaq82Ln%2FDWiAwm7X1jkwyV2cRzm0QIhAPxXEmWJ%2BsWIMxchW1nlIlC75fGDyQLK9KenmLWlJOTdKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5X4TeV5jcY3gA1Msq3AOi4ccXlcuj6jn5gobpRlywNVUdiVbA2V7hv0wSQmwpcRdeAi2mwQsbeDR2yqtsYyuKubmPj5SMjEfMOgGGo8nWIA0i0HQydoV7%2Fw7GM4sMugb8wAIhI5dpyjYNnUrkOSRzYNJzcoxq%2BdLmT6JIeHOC0Ae7VHb1FSN2whLgDNnwK3IWXpt485xy7jzAgM7llJ6v70BJAgAhYtZZEDpyBKH3AjOSYSkO%2FpiYy7IVfYaws8oCRiAhsQpg54gBwuPAmUdAEWScyAQZeWsyZgAhZ5oklTDk2yO%2BfPsBY%2BvO8760LwHEFVziTFcRu7LDAZtye6l5JHKj41n9tDwAdTXI98EBqPkFJh9tFZGL5tLwJuzF4hBYVjl1PfrWYvjJsukLilICaBzaKdOjdxkrFpADgL6kmqi8bcYH7UDW6YH92%2FPa8nCL9NMfETCDSi64PD%2ByQZnVcLqXteuWQc%2BySMXKgahxuM1EoXm74DjvyNp2gYb6SJtTMI3pYNfkTGpZ3XsTuRW11sFxQFgKCRDp%2F8OREeaGr%2Fww6jWPDZwwXPTSFr2kTzBFiiez2Wz3Llcz9dthwUhuNBlS%2FSxERc9BDfMeRmmWTWCH%2Bae7Ea339DxpDRzc19lOjCXs99iubjbryDC89vm8BjqkARjyEiKgazRGbFvzE9oqbSfkRjYIH0DE9omxSDumwkLC8fXQjmfx7dC%2Fwgdgd1gb33FlbzMFsxKulJWhAp%2Bb40d7O1CLL1EnjByxVxR38HYalWH8F6GRg9kkUNE0L7eo0LmwJ8PnIe%2F1cKy3lsghHmY8Vfofbts6s3l788W%2FZ83EvEjLuu2TzSw0E0%2F4iNr8D%2B8ElgKTYME7T5hw9NnUsIkdevIr&X-Amz-Signature=a1166cf47a4028d91268b33224d51c1f606d0be23846df676d4c83691d069b16&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMTSGMXO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4AwFBzv2C9N80CjcbJMdK1XJ6VNFaXotpr5Sa2JW24AiEAkKyUurUESqLYs43IlGWkaLlsxfDg746X%2Bdwsg8X84PsqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeEY1T0VDGbSgfrIyrcA3YvxOUCaIskbckTpwzttWdz0VQJX1fd2NmHHUBu%2BrTp2Wzx7o%2Bu5YcT%2BRR7hiR5HKNzA9KuKbl7hVcxs2xpEZm3ykFPZFpRQ7Is2O%2BGRT8WWZW3KSIxUKzXNzH0yd1fO8cTRGgLRdk7G0XJKLoF09TheC8LNWFOh31gmx8nETtCsInR%2FcfdneYGK20XzceXBRga9gkG8LGlETQIIuph7SBFpax%2FS6rZiYnkfNAud7MtebeOyXgZVryDF9aD6j3ZG%2BQ9SXSkLQ%2BMP1af%2BlPccOWXRUf1kFrq81Z9wL%2Blu8IzjRaUlzRtK6q651G0meI5nZGXnMtz6uIKteVm8RA%2BPw%2Facwpmcthm8nDN0gug0cpHnNttY5CWYiphoLxK3DS00F6QJNJAvKJEDIWjocTCaxfnfOb%2Fq6OddEGIaeDsQpQ8gEuUtI5%2Bh%2FFQdMXI9coT5YpuN9f%2FJlXswtIqGx%2B92x%2Fp2zmfPPKe%2BUED5FEZatyHxTYkQWWJD7zCprvGLYMVUR9YZnT4jn7j1o5UFB7jd0iU2JUecuJNCv62TBE7kE2NJxqQKyIlh93GsgacjwN7ktffF0Bfxwv1D87CLhhOXuZIc%2Bu0WpjhSBsoq1wWoIM1tr4m7iQVxmdZmGZcMNj2%2BbwGOqUBfGvh9X6Nxm%2BVmOPXFVVbmnvoyADWLZfjxeBaLXP1wS7QCmzUoh9uHSc1ckJFC8UWFzpZ4CZVN0vnVkf18X3NJ%2BDkfm7EnhZnXXJrW37mNUI4Icjhlz1eSkL9O3YHDtKS3h%2FVYDUkfhTHxl5UYi9ZItUc%2BuZSFx%2FhNn22uZnfmiHGKLH5Cr1SScVgljw%2FDQ1TnC3aZw7Cql1gNNIIe%2FVdgJrMqPSh&X-Amz-Signature=339d2fe7b18c59dcd3440e67294b5935898b1b31e4009814b565d6de1699ec12&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMTSGMXO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4AwFBzv2C9N80CjcbJMdK1XJ6VNFaXotpr5Sa2JW24AiEAkKyUurUESqLYs43IlGWkaLlsxfDg746X%2Bdwsg8X84PsqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeEY1T0VDGbSgfrIyrcA3YvxOUCaIskbckTpwzttWdz0VQJX1fd2NmHHUBu%2BrTp2Wzx7o%2Bu5YcT%2BRR7hiR5HKNzA9KuKbl7hVcxs2xpEZm3ykFPZFpRQ7Is2O%2BGRT8WWZW3KSIxUKzXNzH0yd1fO8cTRGgLRdk7G0XJKLoF09TheC8LNWFOh31gmx8nETtCsInR%2FcfdneYGK20XzceXBRga9gkG8LGlETQIIuph7SBFpax%2FS6rZiYnkfNAud7MtebeOyXgZVryDF9aD6j3ZG%2BQ9SXSkLQ%2BMP1af%2BlPccOWXRUf1kFrq81Z9wL%2Blu8IzjRaUlzRtK6q651G0meI5nZGXnMtz6uIKteVm8RA%2BPw%2Facwpmcthm8nDN0gug0cpHnNttY5CWYiphoLxK3DS00F6QJNJAvKJEDIWjocTCaxfnfOb%2Fq6OddEGIaeDsQpQ8gEuUtI5%2Bh%2FFQdMXI9coT5YpuN9f%2FJlXswtIqGx%2B92x%2Fp2zmfPPKe%2BUED5FEZatyHxTYkQWWJD7zCprvGLYMVUR9YZnT4jn7j1o5UFB7jd0iU2JUecuJNCv62TBE7kE2NJxqQKyIlh93GsgacjwN7ktffF0Bfxwv1D87CLhhOXuZIc%2Bu0WpjhSBsoq1wWoIM1tr4m7iQVxmdZmGZcMNj2%2BbwGOqUBfGvh9X6Nxm%2BVmOPXFVVbmnvoyADWLZfjxeBaLXP1wS7QCmzUoh9uHSc1ckJFC8UWFzpZ4CZVN0vnVkf18X3NJ%2BDkfm7EnhZnXXJrW37mNUI4Icjhlz1eSkL9O3YHDtKS3h%2FVYDUkfhTHxl5UYi9ZItUc%2BuZSFx%2FhNn22uZnfmiHGKLH5Cr1SScVgljw%2FDQ1TnC3aZw7Cql1gNNIIe%2FVdgJrMqPSh&X-Amz-Signature=3c2f7aec159b27f3bcd62d6a4d7c0a03f18528e4c76541ea476341fe3fb424a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAOPJSVT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUw1ArQWqCWIzx7ems251pFC3YQkzdhOR1sB7uHdjd%2BwIgYPa6UiAnUepkKE5a5kBtm6vhvQuEhiA7%2BYUkk%2B%2BcNQUqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJetg71y1OK00CrbZyrcAyJM7qVK8Qkm6RHn1GwN4AEz3UboEKnltCjdsJglFTwPcb%2Boma8gIR8OkH7qWNVrVvPgNHEKqtsrjIWjz8u7jwul8%2FZr35NsJxSEoRFZG7SCMUH6M9jlw95WRcaBeCAzpcBhrkfRL36UQ5eyWZGs6XV9a9%2FbVIS4HoP8vxWn4GMbVd4hmL7%2B5fNgptDqqxo7qJwJdeWL%2BXLg1%2BFiZQkYyQTDuoUGHQgyEKahXLZQhyeV6jr%2F9HKmFgQuXEet7PAgAeNvBfbJjjrvkWMREQzh%2Fn37JgtFkqw4g%2FYF%2BNpLRJOugzwBceDS%2B6xWrxZc7onXaZex0GR5PNeHuGadz7qPsixNb1%2F9L8tc0GlhCEvF4EDaEYNIA4U28pIrZQvTUC3MLdkM5fnZQEDX27N4HzltUm%2BbUtyh2bR4om9VgfXsMkIxYMuloSmCJcA6tonQBQf8fT4ri2zEuZujWODB4GqzNqqxEscVM3%2Fplwyzee2S5ERwc24tuM2X1DrHeo5Q%2FncLUI6goHcQSfTncxDhZpBhHCz4ICLee5gKlMEoAMoW8UwsbyyEy%2FxFU0MZ21IdCCZjdzS8rN4j087dlPgvfePoCyaSt%2F%2B5Nswd3lTx1VJGCViZU%2BGlKQh1GcMM%2Fwx5MLn2%2BbwGOqUB67ISqztOQ15BGsc1z1zmY3OuHdL0jlVp42R7M%2FIx23K1OSVJiMhsVJgY7o%2FHcBpL1wt2bdTK4YEl2dv%2BiZ6CPmVAS3VS6NXj%2Frjss9TscNrNdvDNvNbvXu9C2J9h3gegjY4C8VQhXljbpoEHsmTWi7OGhmLhOOCXRWOemlwlS1X9CrqDRNdEXj8zllN9pUZCisEwTY0GLuIezy8IVcVMCDTsghjA&X-Amz-Signature=9e7f09e919adde275c5bb34f5515cc9f3e8e6bb116cfc2da0c3795c397f7560c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DY7RDF2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCVZOsNNuXl9J8ZhMo%2FIfHAYu6Ax4Zkx9rqYbWrCM0NgIhAKiCov424HJwH5ZK1%2FMipRJOZGn1gmKMW3v77tJ6%2Bao9KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0LC%2BqgvxF0ksI888q3AN64%2B3PBb%2FWEkzk%2FI%2BrpPA%2F%2BMLg1UbHC5GEE9SAMJTM0frdDBpWSEx5XQPS07C1CLApLPzr9re2XCGLacutoFPZI9FJgisxO22E1%2BiIpB6bsKHK8UGFlu3IAWGrauBLuzACYfVYJSNdpymsrS7lWEfRpgLNSHMVgIG4Pgbq1AGL0HQPE%2F982bhIrkhzV4UgcXdUaJCoMiPh28vHMWoN8cvE2f5vkgrIWCaLCOBcv7Ayoo2u8%2BCZHM3lMZr3J3%2FQHdTKkp2dNbJ0Xk%2B93aQ%2FxzqnjY70uqIN6A4F1rmBE8IMX4a8ZUw0x6lNNguLi9Ja5ISPOXnBXKSMaRdiU6ybGWba63EODbPS9ilupc79F7e6hOHheSmvhcuLV2dBqpF9UzCy3vMN5lfaOZ5MlgKGl5G2KauVeOqazgkoZKvUBprjx8oRDLGHNQffSeXkQBKsVwn4e2mS2%2Flof0COExoXdoue5A6XHBUhWrLjSAskgS6DgVhRFo81Fqv7UMpSC54O1xzUnju3ZEbXsJ9JAJzXfZ4%2BdHw5xv4zJrfKha5T2ZKQBTVxv44%2BMDIGbGGySa01BRuCMwq9i2Ic80ujykCzXU0tge0M8sJI%2B%2BWHLH%2B6WnA9z7FEedUeewLM257%2FOjDO9vm8BjqkAfAUMdkJh%2BnhPZd0JQbtSCpzxyUUvVqgQdAHheFqBpysgwHIjHRjrkZn0NpMoDCX54neBH8STL%2Fy8h0HmZsrAoSv9jua%2F%2Bktsju%2BbSBhpq6fw4p5YNge2B6lS0KCVUhnseN1INpVQsVgS4mtnmTDDpV1JVy7cJDnpiL3oqSzzzX6ydvE2hif5O42SeY9pV2HMqHEaY7TpDRUNukS52fX4ZIuW1B%2B&X-Amz-Signature=5b33e6a4526d0cdf673d371ccfc5f58e686e03424268388241fe30a659f60fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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