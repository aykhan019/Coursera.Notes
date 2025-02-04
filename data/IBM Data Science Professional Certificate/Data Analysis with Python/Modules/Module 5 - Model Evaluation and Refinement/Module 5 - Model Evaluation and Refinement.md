

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=633adcc1a1fcbd5dd20325c0b054ef75efa0ae53a41819107fd7faf425601303&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=725e20bfc5cac9a76e650498adf32b06e968a62064c845a2f496a2f2bf385d62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=adce022b1bc3d71cc01d141dccdd9327156a849b55845f72dc5c2205e9a1abcd&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=db036d8200edd89f00a8390ca0d2de2839e11f31b91bd9038498dcb00a600c9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=5395564ef0ce33e479106d30c273041507edf8be76fc8e6636762f11f3ea2970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=a643516f20f0e70f74af5e6bb66245e445c1541a136bdc0320f226e186d01988&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=f6437cb5a3fb51b168b31990a84948ba0b2d79acb96fd04899f2c0b4b8087dfa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=1289790429491d32c4bfbd2e76d0fcb71bc13d283194ae20977ab3cee82aa64f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=2083662a8a5fb9bcf72a027f4cea0c020588a17c546aa0a0433119ba9fe52e8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNF2WMVR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD4A8nEKZP%2BU6Iud%2BXJ%2BHwuxDRpERHRE8kHqaQLGyWBQAIhAI6uvUiPjmcCIHK%2FH%2BhlCozxi8WLD88JHQCOXhGjBIN6Kv8DCCYQABoMNjM3NDIzMTgzODA1Igx3X8u5BqYLNGvOW4gq3ANDctw%2BTZgBq3afzj5Gcg9vr5XnORb2jZxcLHtgEI4VvfCuy%2BO9mtSv2F2wTDMZ4%2Fm5XnDCSAek7t7SeXSlGcXHInvDr6KVCJR8OPrwJXpRStoRirIqjxDoYU5PPBzu95%2BKzMzFkrWTZOVOxX65bpE2aswx6XL2wDP8IhybnKl3tXUYaR1rhOTYIDawhGmJHbQr7b4Hb%2BG0T9ve7iZsUrB0L1X440aeZhqiL663sBz1uuNU9LaJyg7pNplnPUYjxxNbuVZiVOSGOd3wYGSVHFt%2FF0tKl6Twbth6ngzbxnTrHO%2Byhn3%2BwUK0cXsADvldk9qzu3kWIccsqNF50HY5AYFeVDultXSDmc7yMxDxHZYEpAhLVc2LTHNCY5gsl3qG3aG9myJTx2JNBJnxnWDHgelPbIQ2ROlNrTbXN9AWF2XEHK2WWjQI5JpDIEwFc3ti2K8ZLQbA5tLrf2wkEFcapH3Blen0jCj%2FVRnOUaK%2FBD%2FlI%2BdBpZhvt38A368jsc8%2FqaVtR%2Bugu7GX2xUTXgpYnogOqv8ua7dWTZefbxAE1ex136EzmREVM8Pl0EN%2Bm7iJc57156AO8B2Yf5oy72zjtVGbvFRA2IAznvPM15zFRBSjEqdKWBdSJU9bm2R41zDRvoa9BjqkAfQQJ6JbdlbFIpqjyxSeg5QmJco%2FEiPYPtMejtbgC5ftGbZazQDbLyduIj0n3Ie0rgPyxeIlQ0TgnR5kH8lI1k05iaaIPlfCcp1eM5RdM85xsTwVXViCTsPQvkAmJKklt3zy0%2FNLdKyV%2BwLna1s0T%2Fxqk1Ob2lykGz4y0oqvkGTTgwo1Lsn4H7ISCPNMfDWt%2BG%2FWqTYE%2FqB8PCdm%2F6FvHrXKATs6&X-Amz-Signature=03b64879fd35e3384d565eb0b2c81a645dc6f142ec0085cbca3763d95d7b502c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNF2WMVR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD4A8nEKZP%2BU6Iud%2BXJ%2BHwuxDRpERHRE8kHqaQLGyWBQAIhAI6uvUiPjmcCIHK%2FH%2BhlCozxi8WLD88JHQCOXhGjBIN6Kv8DCCYQABoMNjM3NDIzMTgzODA1Igx3X8u5BqYLNGvOW4gq3ANDctw%2BTZgBq3afzj5Gcg9vr5XnORb2jZxcLHtgEI4VvfCuy%2BO9mtSv2F2wTDMZ4%2Fm5XnDCSAek7t7SeXSlGcXHInvDr6KVCJR8OPrwJXpRStoRirIqjxDoYU5PPBzu95%2BKzMzFkrWTZOVOxX65bpE2aswx6XL2wDP8IhybnKl3tXUYaR1rhOTYIDawhGmJHbQr7b4Hb%2BG0T9ve7iZsUrB0L1X440aeZhqiL663sBz1uuNU9LaJyg7pNplnPUYjxxNbuVZiVOSGOd3wYGSVHFt%2FF0tKl6Twbth6ngzbxnTrHO%2Byhn3%2BwUK0cXsADvldk9qzu3kWIccsqNF50HY5AYFeVDultXSDmc7yMxDxHZYEpAhLVc2LTHNCY5gsl3qG3aG9myJTx2JNBJnxnWDHgelPbIQ2ROlNrTbXN9AWF2XEHK2WWjQI5JpDIEwFc3ti2K8ZLQbA5tLrf2wkEFcapH3Blen0jCj%2FVRnOUaK%2FBD%2FlI%2BdBpZhvt38A368jsc8%2FqaVtR%2Bugu7GX2xUTXgpYnogOqv8ua7dWTZefbxAE1ex136EzmREVM8Pl0EN%2Bm7iJc57156AO8B2Yf5oy72zjtVGbvFRA2IAznvPM15zFRBSjEqdKWBdSJU9bm2R41zDRvoa9BjqkAfQQJ6JbdlbFIpqjyxSeg5QmJco%2FEiPYPtMejtbgC5ftGbZazQDbLyduIj0n3Ie0rgPyxeIlQ0TgnR5kH8lI1k05iaaIPlfCcp1eM5RdM85xsTwVXViCTsPQvkAmJKklt3zy0%2FNLdKyV%2BwLna1s0T%2Fxqk1Ob2lykGz4y0oqvkGTTgwo1Lsn4H7ISCPNMfDWt%2BG%2FWqTYE%2FqB8PCdm%2F6FvHrXKATs6&X-Amz-Signature=303f500d7ecd940b0902adc3e80cba0390069cbbdcb338ed9f42b37d62be5555&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNF2WMVR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD4A8nEKZP%2BU6Iud%2BXJ%2BHwuxDRpERHRE8kHqaQLGyWBQAIhAI6uvUiPjmcCIHK%2FH%2BhlCozxi8WLD88JHQCOXhGjBIN6Kv8DCCYQABoMNjM3NDIzMTgzODA1Igx3X8u5BqYLNGvOW4gq3ANDctw%2BTZgBq3afzj5Gcg9vr5XnORb2jZxcLHtgEI4VvfCuy%2BO9mtSv2F2wTDMZ4%2Fm5XnDCSAek7t7SeXSlGcXHInvDr6KVCJR8OPrwJXpRStoRirIqjxDoYU5PPBzu95%2BKzMzFkrWTZOVOxX65bpE2aswx6XL2wDP8IhybnKl3tXUYaR1rhOTYIDawhGmJHbQr7b4Hb%2BG0T9ve7iZsUrB0L1X440aeZhqiL663sBz1uuNU9LaJyg7pNplnPUYjxxNbuVZiVOSGOd3wYGSVHFt%2FF0tKl6Twbth6ngzbxnTrHO%2Byhn3%2BwUK0cXsADvldk9qzu3kWIccsqNF50HY5AYFeVDultXSDmc7yMxDxHZYEpAhLVc2LTHNCY5gsl3qG3aG9myJTx2JNBJnxnWDHgelPbIQ2ROlNrTbXN9AWF2XEHK2WWjQI5JpDIEwFc3ti2K8ZLQbA5tLrf2wkEFcapH3Blen0jCj%2FVRnOUaK%2FBD%2FlI%2BdBpZhvt38A368jsc8%2FqaVtR%2Bugu7GX2xUTXgpYnogOqv8ua7dWTZefbxAE1ex136EzmREVM8Pl0EN%2Bm7iJc57156AO8B2Yf5oy72zjtVGbvFRA2IAznvPM15zFRBSjEqdKWBdSJU9bm2R41zDRvoa9BjqkAfQQJ6JbdlbFIpqjyxSeg5QmJco%2FEiPYPtMejtbgC5ftGbZazQDbLyduIj0n3Ie0rgPyxeIlQ0TgnR5kH8lI1k05iaaIPlfCcp1eM5RdM85xsTwVXViCTsPQvkAmJKklt3zy0%2FNLdKyV%2BwLna1s0T%2Fxqk1Ob2lykGz4y0oqvkGTTgwo1Lsn4H7ISCPNMfDWt%2BG%2FWqTYE%2FqB8PCdm%2F6FvHrXKATs6&X-Amz-Signature=c877dcea0af0e8f5027b67068b0d9b34ae3db91ef90d7d02d9dda38a7a0632b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=f792de3766930bd827bd6c3910c049decbfb39fdc11a56dcaa7700e086bdc845&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=d396b91568d71d7964b6eb418421b83f9460003408f9e3f7c829897169ce5ba5&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=9806c72661f6ad16c407bed31fc238981e55d7d75067e5354bf49bb6301f2983&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=7b8a2adb7e08387358de894795a3ef9bb7d68032aa7303aacf1406c77f7dfd1b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=2a31566d340128254ffe396547eddebcf9939a11729571459294115d95d168c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YYVZKLC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIDZJelWHJ3YvEbLT3b3J4qhKJWDsAqGWjxIzd4WwJS3JAiAXlaeR5xEquUKWnj0g5Z77%2FkXS4Ab4TmDqL5i5TZxdgyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMNbuFhEEa7oTgtFs%2BKtwDoVQFSW0QGW%2F3nYeYdRWUBg2WdOVWoAawSIIwkCIREkd40q5LR9Ks0n7w4tuhnBx7jnvzyobD1mhZTq7gowfVEt1bv2y0K%2FhQnZ%2FuzM%2BF0oYseB%2B6txrE3yQUS8x%2F7QWubUboJbOEaVLSdRAzfbr2H8JBnxpl9bAgn8rXRWVMKFapxsZRAgqlLB1PL3VHfamP16EoZR1hzUCU8IEOLo%2F1rIchD6I%2FnFSS%2BW%2BwPg6kTsEkBuNJs0o8rRSY2fWgnzPLvrQ8AcAf6pBLFMtVSq3icjYtLkBI2Y2SzcclfphGohgxM%2FqUXlP%2FUOI3AqTdoPXN0OHPLcieealduPuvCiR2C6fgUgyJYG6nTLE0aapiX2dQabq33xQKM1EL3QbxPAc%2BoyF%2F23eI4frP4sxetYRwQNCMT4ruqehqvtTRG7OVpScBm9OHeApg5WW2bl1WIVWSFskPv49ejpeT6uZI1ILcTzgA6VVXkmV4tH2onRSt%2BtACkd5xdRq7PzgwegowhbzWZJrBVqgqrHZUyXFJwyMG7iGEjRAwp0a7pN0PzqRGbSewJWT05Z8vVixNysGNyKnN1h2n2XpX7cj4NAtWrYk1KxlmaphZeWT1K4Q9MSypSpyziQyKg5enBy%2FY1UYw%2B76GvQY6pgHfJq%2FX022K7aHdytOfwrnSPWIS8fnq%2BAIuGjDSyP2OivmfR4skxTUbB1VH6GAkKSMgP9j3C5uKtrosziCQviaPh0dX8Nbm7ZwN81iOuQMZML%2BrHhZWGLhk39bnel0iyKLCGdzO26MZGhgNlER2Vb9paNZJ33IwIy1CZFNGPglzdQUfXsCw9yfat7FUA%2B6qyXNJaD%2B%2FyuimrZQMr1K9ppceLUcqCZju&X-Amz-Signature=633363b91131a4a1722b0095168071614325f1b93cd8491798340c7f42904c12&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2IQIV4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCcYcdG5X%2B3Nc2TQtZ7sjimkhWU0%2BND0ASQaTk9HACqkQIhANBpviQpgT7i8DGuxmxLQqaAw2VZhiJoVvdex9iKTIj1Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxknRjs8N9Qn%2BmPOhYq3APfXorTlHHVGsZgk5Pm8wZ7HjgakLnKhW%2Fh51iLO%2B6BphRK7tXPUR5%2BBXbstSqeNTlgGaXBdS0GRqC02i8nRF6nY%2BgHxjzclz30XQqpBPr72YEnltfSu8ofud2BSpgMxBBMcjvbYO3sOFZhOrhHRQ9%2BR4mD1l0zKcLizil3l9WQywTRmb3%2F6Qs6EGGZE9GkVWpWHFmmtKZ%2FU%2F7oA94fiQ8ys57T0rY6%2FEFooBnPGjCmQpEy%2BKz%2FqNA6k%2Fvkjv0kB%2B3C4fRCRjQ%2BqfD%2BBC5KDD2aBYhmCXRY6Jhp2o%2F5mhawiAFxIUqRO3yk%2Bzs0s1G%2FR1V8yWj%2F6LYR5%2Fmc8JPuCrUMmVJR%2BuPFdF%2BszQRwRn%2BlsDPo67y6ZD7mwqLXHFrlpNuZOMWBWAMKs8ghhtOkSPeBJ%2Fj01TT2BkrEuQ2hZVbBIyUlbIgQtGYf37GtlDL0LuDDS%2BPsZmhmdAPddTVhUtjIUiKzJ%2Flnuflh4twLviuTxWunbF%2FFs5QdXOIAyz9sg3FCEis1k%2BMFaYu52VTWS7kyK1J%2B3Rx8p9ajg9405WeXTWJ7Hh%2FmyzUDbIx4RVAwp3Olx%2F2vnNGWTTp09zEBY1HiLeoNapw%2BXJ%2BBnGzEgQrDtqjjF20eNmLXpp%2BahDDPvoa9BjqkATUpn1JpIdR9Gx5HBKQqDbSJez4pazam%2BEVbIc05gYqzSHjRoCCgviYYhpk9T8ycTnuJJtkNyrZSK0%2FG3Z1QsFbyA2%2F1xfa80z7P0HGbCpDEN9KoFkRmKYGr1m3imGZLCIaQ8q4KV5YorT7Q7Jqp8wUOaUqOtH5TUloWgyNQA83OXxqab1%2BtIoRDPxWKUS85kfAsRiaiFDmPCLOWZMscGuxeJKjQ&X-Amz-Signature=22b197f4924c521af2b6a0099cb45f78e9df35805192f29f90a109c7d741849b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2IQIV4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCcYcdG5X%2B3Nc2TQtZ7sjimkhWU0%2BND0ASQaTk9HACqkQIhANBpviQpgT7i8DGuxmxLQqaAw2VZhiJoVvdex9iKTIj1Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxknRjs8N9Qn%2BmPOhYq3APfXorTlHHVGsZgk5Pm8wZ7HjgakLnKhW%2Fh51iLO%2B6BphRK7tXPUR5%2BBXbstSqeNTlgGaXBdS0GRqC02i8nRF6nY%2BgHxjzclz30XQqpBPr72YEnltfSu8ofud2BSpgMxBBMcjvbYO3sOFZhOrhHRQ9%2BR4mD1l0zKcLizil3l9WQywTRmb3%2F6Qs6EGGZE9GkVWpWHFmmtKZ%2FU%2F7oA94fiQ8ys57T0rY6%2FEFooBnPGjCmQpEy%2BKz%2FqNA6k%2Fvkjv0kB%2B3C4fRCRjQ%2BqfD%2BBC5KDD2aBYhmCXRY6Jhp2o%2F5mhawiAFxIUqRO3yk%2Bzs0s1G%2FR1V8yWj%2F6LYR5%2Fmc8JPuCrUMmVJR%2BuPFdF%2BszQRwRn%2BlsDPo67y6ZD7mwqLXHFrlpNuZOMWBWAMKs8ghhtOkSPeBJ%2Fj01TT2BkrEuQ2hZVbBIyUlbIgQtGYf37GtlDL0LuDDS%2BPsZmhmdAPddTVhUtjIUiKzJ%2Flnuflh4twLviuTxWunbF%2FFs5QdXOIAyz9sg3FCEis1k%2BMFaYu52VTWS7kyK1J%2B3Rx8p9ajg9405WeXTWJ7Hh%2FmyzUDbIx4RVAwp3Olx%2F2vnNGWTTp09zEBY1HiLeoNapw%2BXJ%2BBnGzEgQrDtqjjF20eNmLXpp%2BahDDPvoa9BjqkATUpn1JpIdR9Gx5HBKQqDbSJez4pazam%2BEVbIc05gYqzSHjRoCCgviYYhpk9T8ycTnuJJtkNyrZSK0%2FG3Z1QsFbyA2%2F1xfa80z7P0HGbCpDEN9KoFkRmKYGr1m3imGZLCIaQ8q4KV5YorT7Q7Jqp8wUOaUqOtH5TUloWgyNQA83OXxqab1%2BtIoRDPxWKUS85kfAsRiaiFDmPCLOWZMscGuxeJKjQ&X-Amz-Signature=2d4a4a797f0e571aee303f3d8d5fd1538ed36949e213bdc8f8786486d59e37b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DQNALWF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCFB3p2mg48sCyLtyLvnkqjomqBWaChxNbyhM1DY%2FQqJwIgQsGVQPhXWl2m1LbvlgBcyRq4sqwOL5g2kP%2FGTroIfsgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGKvAjOucRB7pRLJdCrcAyeXEC8%2BJPL9VPw6z0Zz2xTzkxOWMqnRlBv43KBFQmletlJy2AxWXTqUqayROCHlvBVGEQEU6zlnLD8IFXdMs0N7pxhEGgBLbG2x8zdUiRe72KLIcJuW7ULwIKiutSpvamWg8G6zTUPiuC39FNkPKbji%2Fcv9IHpAE0NYWGvRNOX4gwClA0%2FNQ0TwPLp6uOcw3Hdj8U3iW1jGzglogmJU4wo1DFFzDBvJe2WX9%2BraqvrrISMXxPEu16%2FrOm84zyWOGz3Je6Gb9umBfBCVXuVgUtdMutZOlGHX2v2IOCKGyPCSO8yMsELMZ4yCocGtQWkcU59sX99A%2FpDhKBoPJik42IHC2MfwEnVdiHWsmQRK3dyC%2F%2BnxXMa3C%2BJjZUKWKxVel9DXxbnbSlgqwOc4f4%2FtYAY5Tk4%2BoIe5K%2BAX7XuPL0G61Bq61g69GZ1lS8meDnmOQabXSiB5J9AIiGUNgPXxXjMfJUZedjvwKPyoCQYei4%2BNx6TRyzz5YLHvLf%2BCNFfGAVIDcPS057nRiJYW21ktvzDQ06PmOvUSbrMBU8txIvqUVaKSGUDrMYBm%2B53EKcTTqWerq%2F5LwP94VsqOLxq4Eo33LC9qwgu5XOo8Es1QuP0cPxQuFk%2BlVVhKA258MLG%2Bhr0GOqUBMBWFyFK8B2exD8pzufpqmDSaKegj6jozTq94fEfGHHTH%2Fq1LP7c%2FThDqutvtQjZA%2BzPVeQmXZpVnULOLS%2FTUVJwzlZkiOqOYCqk4EPuCNHVos0VCCGczUVUmsJSxtp9UKkX7r99MBUWk2G3%2BzR9eIFa%2Bw0U4NxvYcXNCJn6eYs8ORiTKINZj%2FNfKcqHab55%2FhDoNNIMhofkiAhiel1Z0fqbToRUS&X-Amz-Signature=2768e9bc20c411afe42ce8258d8a41cbbe6d7f9fb5e22a5fd9419aedbb57890d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEUGFRA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDE4BkX33Ta9ApA%2F0B0r3YJ0QAFCi0rWnqdzd3VVPkF%2BAIgG6qnYRfzZm5dEOWkUsMq5UsKQdpAZdzXvP8q6VSi%2Fp0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCf6dBSbKUxgBUj7IircA1Pk%2BuJ9QlCrbhnTXIV8K7uDT04vDhXH%2B1%2FvMPknTQXXFFYgOtItrgEFsethmHlAvXTdmwNK5f%2FWQVujW5Iv%2FbtMj0Hp8jVVCy05e8YavH6fzcBLwDv72l8AIDA6jmV%2BDurZ2NxpsMExZa4EPbXJ%2BpCtspOSc03c%2BSi%2FyI5WsYhXyHuLXZhiklQsJFWTms6M1E%2FrkK2al2aLvQ7VWcmcdGWp0wv3Ii3it9qgLp2uj96Aq%2FrSZzvFkaqm%2FBP2vay5JQHNfKZzqwgM2o%2BxnPk5NHIKmhgXcwA8lDi3dG0HgUeK7Mz%2Fjv29gsBpzXxz%2BUF%2Fw5LQ1o8HIe%2BEZLEUnk%2FJ2eCwp80S552HT9PcLQE%2FUqo9ff6yszPTXLg3Oh1WyCWvIwfBpreS2tM8kuhXerj86p59M1c2q2CNzn2Fj8Z%2BXMwlMlb%2FYyk7Yy7QGh5NQtXDhNf6lGd09R2CC8830pJS6rzvQY5GXmYjjD1eKIXS6k6Jv2zCHB5dmvnTOj4RD9xBAUBSzU6YH%2B3QO5DJ1rrW4bPwEEgEZuh3XrB4SlTl1HvQTbrHEdD38blWbJUc4cjwgYtmXbGFLPLBunz9EsqHJ9itNEh6M4z5fw4NMcZnh8nWr%2FDwds9NBeRjH27AMOa%2Bhr0GOqUBzelehqXU%2Fn24%2FrWUAmSPinsj33ty7JwvVIliORVg1QcTId9hrIEw4AIMbXrjBgoe0bo9VxlzfNvd7Bu3CHAffw7a2SfrISm47acrbqONUCIHD41zekhR%2BgiwwmwoIFUAN66%2BY6W1uwBQL1tLdXAUkQJyGv%2F0b0qH9RQbjJaTzrbtxb5l4wOoL%2BPxokoWTaDWOX%2Bw8DU2S3SPh%2F1qGf3Zk5NASF%2Fd&X-Amz-Signature=cd17db77f5fc0f2cade2601441661a80032bead4b37b5e0d77d897789033d292&X-Amz-SignedHeaders=host&x-id=GetObject)
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