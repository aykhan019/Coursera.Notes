

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=cb36dc559a0e3ccfe745521e7c2090cc1e04f0f6a2b7eef7ad269818018cc3cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=58e6e24d094b085dc0f9c6eec7027fc6120de0bdbd51acfd6170485d0e85458a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=b9140477f0120f4476731b971208466ad331cd1ec865703753d1903ccce2ba69&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=8cce5c75bb80c0e54918aef0d87bcf5b1bc501072d95a409bc131a4eaa61f658&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=bf10d22d3edf2d861cc76a23857d9599661440259275c78ff926f87158c7406c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=e15c3aef5ee1a3e62d584cad88da819f97e062ad39768db28bfc84358de90d64&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=4ad75ed76aa3ff955e124c86e768e536130208a2fa716cc86b244052d5656033&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=5354f2654b021feeaaf07e1ef0665cf4265ad6a5d3b51d4f28282ff515a5316a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=ede964333084ab598bb87d57c22cb5de380b1c2a7340aed6615a7e2b7ca7f553&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636Q4ZAPA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLEFSbmpiKiYA4lgVaxwGglWhA%2Fs1n46pgFVfVL2LJ%2FQIhAMe%2F0xvjFoNyOZFvsg3oKXJPWgNuHvJue%2F%2BYzOzKt6LsKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBrZhotcdTUcC4jAsq3AMuQxlOWy9hv5p6IQ7jlTBxMa6%2FaVah9zYEmTBAUXtQFVXP8cA6s82AIfxjcIgyS7qx7nSl2LUCG1u1szXOhSwQAqFLFYdwgXNMYVIij95TIT4wVY84XpebJgTeGcZXmqxKJH%2FvnFgYUf0maHzvKTT7zX26z45oYuzz738GFoY9WSSmI40hwBRKgK1vhQSyueq8ROe%2BhuNvjrE0xhw%2FNG4meMw6NjPF68R4AjDCARKpvKaNR%2F5DAKP3URje7p1qRdNbQ7m4t8lEuK4MjyfpdO2E5bpe9DMPDbNPWXUoSAAEZlNVslo%2FvIdrv5v6z1e60vka1VFG%2BYLxaqQPxOY%2BpdUY%2BpnEfQ3bp%2B98EPYFdAx5HdfzKhwirRSkKYFFLrMuKrpRcn9agH90zql3N6%2F9BPt6zQUThzyEnxGZDSyonWJ8RyUG09EzirNvzdjfeELwQ6dlTYZskAjzx3dza6GJw%2BbPJi1sgxgNkc5ruZJLknN63h%2FBnK5J%2BKZtzF3%2FyvuZak12LVORTw12h3GZi04xyXBXCZscB4z%2FFlXErtiwe8I1vzLAFBiusRTK3LrwV9IhRBStfWmFnkBqsUkL1fEivLPAntff41tXFg4FTdre0v3mtCCv%2F7ygQzqBJv51%2BzCppPe8BjqkAZCFUFghHlDFgwzAImEiV%2Fgnhu0l4OHXaNyTSuB5RuyTEal%2FVVylV9ltKi%2F59C60QZ3pnDlCNIVICR7nIvUCF82AWhCO5%2FGBE3TKWlt7cxnvRsmtxMOxTiMJiznJRXMeeXV2bybO8chlVarmtK83lUpuXgqM27qnksaFKRPRQFC9RqNnQR9eGut4oEYA570lm%2F0GsPzTGF3yWqJO6K77HUpUlRSE&X-Amz-Signature=54f7af460aaa16240376b51b22f45c825b6f7e601956d40738ad0c80f188c32a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636Q4ZAPA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLEFSbmpiKiYA4lgVaxwGglWhA%2Fs1n46pgFVfVL2LJ%2FQIhAMe%2F0xvjFoNyOZFvsg3oKXJPWgNuHvJue%2F%2BYzOzKt6LsKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBrZhotcdTUcC4jAsq3AMuQxlOWy9hv5p6IQ7jlTBxMa6%2FaVah9zYEmTBAUXtQFVXP8cA6s82AIfxjcIgyS7qx7nSl2LUCG1u1szXOhSwQAqFLFYdwgXNMYVIij95TIT4wVY84XpebJgTeGcZXmqxKJH%2FvnFgYUf0maHzvKTT7zX26z45oYuzz738GFoY9WSSmI40hwBRKgK1vhQSyueq8ROe%2BhuNvjrE0xhw%2FNG4meMw6NjPF68R4AjDCARKpvKaNR%2F5DAKP3URje7p1qRdNbQ7m4t8lEuK4MjyfpdO2E5bpe9DMPDbNPWXUoSAAEZlNVslo%2FvIdrv5v6z1e60vka1VFG%2BYLxaqQPxOY%2BpdUY%2BpnEfQ3bp%2B98EPYFdAx5HdfzKhwirRSkKYFFLrMuKrpRcn9agH90zql3N6%2F9BPt6zQUThzyEnxGZDSyonWJ8RyUG09EzirNvzdjfeELwQ6dlTYZskAjzx3dza6GJw%2BbPJi1sgxgNkc5ruZJLknN63h%2FBnK5J%2BKZtzF3%2FyvuZak12LVORTw12h3GZi04xyXBXCZscB4z%2FFlXErtiwe8I1vzLAFBiusRTK3LrwV9IhRBStfWmFnkBqsUkL1fEivLPAntff41tXFg4FTdre0v3mtCCv%2F7ygQzqBJv51%2BzCppPe8BjqkAZCFUFghHlDFgwzAImEiV%2Fgnhu0l4OHXaNyTSuB5RuyTEal%2FVVylV9ltKi%2F59C60QZ3pnDlCNIVICR7nIvUCF82AWhCO5%2FGBE3TKWlt7cxnvRsmtxMOxTiMJiznJRXMeeXV2bybO8chlVarmtK83lUpuXgqM27qnksaFKRPRQFC9RqNnQR9eGut4oEYA570lm%2F0GsPzTGF3yWqJO6K77HUpUlRSE&X-Amz-Signature=0889dac1c293c622dd22d76591828e4dd6f46d37afadd60b3d33b6e21725da3a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636Q4ZAPA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLEFSbmpiKiYA4lgVaxwGglWhA%2Fs1n46pgFVfVL2LJ%2FQIhAMe%2F0xvjFoNyOZFvsg3oKXJPWgNuHvJue%2F%2BYzOzKt6LsKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBrZhotcdTUcC4jAsq3AMuQxlOWy9hv5p6IQ7jlTBxMa6%2FaVah9zYEmTBAUXtQFVXP8cA6s82AIfxjcIgyS7qx7nSl2LUCG1u1szXOhSwQAqFLFYdwgXNMYVIij95TIT4wVY84XpebJgTeGcZXmqxKJH%2FvnFgYUf0maHzvKTT7zX26z45oYuzz738GFoY9WSSmI40hwBRKgK1vhQSyueq8ROe%2BhuNvjrE0xhw%2FNG4meMw6NjPF68R4AjDCARKpvKaNR%2F5DAKP3URje7p1qRdNbQ7m4t8lEuK4MjyfpdO2E5bpe9DMPDbNPWXUoSAAEZlNVslo%2FvIdrv5v6z1e60vka1VFG%2BYLxaqQPxOY%2BpdUY%2BpnEfQ3bp%2B98EPYFdAx5HdfzKhwirRSkKYFFLrMuKrpRcn9agH90zql3N6%2F9BPt6zQUThzyEnxGZDSyonWJ8RyUG09EzirNvzdjfeELwQ6dlTYZskAjzx3dza6GJw%2BbPJi1sgxgNkc5ruZJLknN63h%2FBnK5J%2BKZtzF3%2FyvuZak12LVORTw12h3GZi04xyXBXCZscB4z%2FFlXErtiwe8I1vzLAFBiusRTK3LrwV9IhRBStfWmFnkBqsUkL1fEivLPAntff41tXFg4FTdre0v3mtCCv%2F7ygQzqBJv51%2BzCppPe8BjqkAZCFUFghHlDFgwzAImEiV%2Fgnhu0l4OHXaNyTSuB5RuyTEal%2FVVylV9ltKi%2F59C60QZ3pnDlCNIVICR7nIvUCF82AWhCO5%2FGBE3TKWlt7cxnvRsmtxMOxTiMJiznJRXMeeXV2bybO8chlVarmtK83lUpuXgqM27qnksaFKRPRQFC9RqNnQR9eGut4oEYA570lm%2F0GsPzTGF3yWqJO6K77HUpUlRSE&X-Amz-Signature=4505ab3a4a95cc4cf40fcf0c7ed66bd4c646cdcdb0ab04371d4f76cbcbe38d75&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=377199a3d83b4104c979d59cedf243d1ae07efdbc927293a27af6e2018b6ffb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=288774a0f2ac434dd14e1c27ac15f47276bf35f10953320abb3b80331a4eb134&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=42b6446e9c147a0fae5bb309a933d4ce92e30cd2c72a390f285d02aa4df603b9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=395b82d7960242f9c650a72483e2de6c9450278186e8bd9a044139a94bb1f4bb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=7b518bbd28c6ed43d56b0d5c720cd56c2bfd402eeaeddb91e93a64b54deaacdf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644KHUKNP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBEchxTW2F0R1hhTotz0684mRViCdLvYJqYQXLVSFmZ6AiEAq%2FpB9BRVZPfUPJeBFRyOWPv5n%2FkDz9DFNfOSFP0TMxgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOa95C9zc%2FIVwM%2BkeCrcA0rPi1kkY%2BZoxgM9UpOMV5F7t%2B%2BzP0nwPuIhD8t2kdINyeRKWHKCPKNMffuucR%2F1LlIQ%2F5dX2vdTKum8KRe0yRop3hyxE8buDfCZ%2BFt6jlUafy%2BhUILAHDRX%2B3hRHEsi%2BZeUJUWuYNvlWr3Qd0gzcGNArmxsJXLrqnyXnL7H%2FuXCFPVNlFr7ZE8LN55087XRmLo7cRzCNRPfmubIZYKAE7hAJgiKSnNPd2LQrIXWyzsN8NPwQbB8n3i6vtprn0gtG6KeKBcecl%2FvDrqS2marPrkbAl9oToGA8uXrc5jko7OeXG4SiT99%2FZ2xhsFtFkz7D5%2B4OLCQvOSELkGCNlK6c7rZfqtSvChtzEIR9i8eoLmD8MJDZ0M%2Fa86fr7FnnUGKjCPeNXIfxKOQchuUiTyEI%2FDePARn8%2Fsb%2BF6ha3r4j4Iknto4HCV1Uy7KTtWciUotTd%2Buwxv%2BDyw4Hgv%2BC54VKKQn1AJ%2FYDSuARwVLFdgrPPsLRv1mQkl2pf5hJvySGq4YVGziEOt9OSmtbjPEPtNCY3jf6wyN0f6c9%2Fu3GTeRtqDKFKLdQa4W0B5hf9jnX%2BdUkjahg7ZnJeAa3TwtkR6nruIxDM6cEAj6W0cOX6z5YtEkIzlZe4KDjJwpm7xMKuk97wGOqUBMlUf2CIZpQ8D48dbYLpiDRF5MIm8TjqNZX%2BVrGYjimWjXfLHsvsQL2H9RwIhF3hrwZsB5aywRCkcIJMqA34V2tNjVsKUnjxlU7watNldMFPJJcBXxJj13kF2WHd3Izr00Qf066od3j%2BaoNSRI60NNaBF06B23Tb7QUw9D5aflM0F1dM80ck49xRXUAW%2BSl4W5ru41UGm9p5fKrjK9anPt7mfx%2FE6&X-Amz-Signature=4c93d5375fda98cbf35b89a84a612432e5eca6ffa088242c2af6da1ff67d536c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EMS6ZPV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtGTbyQH017DfO%2BhHPkIGokR5rVzjMpvCnA9fw8Z5vlAiAzyVkFXBfqP0j6GacZ8dypA41C%2BXjhOGUSyVMSIWPE3SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sfRKyL%2Fe7E2Ia6mKtwDSlotOOVYb6SHhJ7l59xIn6MhP0FgVvz98YUSkSHgB%2BlmwEBUUXdTvBRUkGUh%2FN1TG1UbK3hy792mAZCwuCcRaGjLYnn9CSu8%2BNqcHwx8Rtw1535fFJLfnRe7IgNRJnnbymDbMWXiXJc4imU75JdW%2BNWeoA4ciR5dN1pgSN7%2F1uU03lIoHv1MUUegBKUHBJVwBm1Uqh6S6eLlX%2F8ZjdmTIPruDcKXEZcC2qC0QxwrShxvXyN15k%2FCI0NFZPTbL%2B3UpJJNtcRjY%2FoJTEf%2FAqbgZjq5FO%2Fi1W8iaXcH19E%2FaEDmse90uk%2FpEv2sIgYLQFV8EyY6AS6eQYEdqNf%2B9mNv5gnpMnUnI16BS8BIT8qo7nHRgKPhS2PrNBbOCJF5KzMtNPzvz0FFEGlC0vyeHM3CWRahgnoq4xJgBvHoVg0m8gzQrOdIXXPUe%2FZNWqKyw6IgOGEcSbRlT%2BoetRMUDh8XZWZJBHoaBgo7BkB2eNdWG8cs9lRXJpytUhUCDdfi%2FOgm9Kz6VLs8Gz29ZgMJiIRRDErkVgrwI3FucPcAG5HVPCIax2D98JjELQk9MTsl3CyDcJF7JnzIoIr1mc8Fq4RYBQSK4h%2FeqMKO36M0j7LuW0%2B%2BMYtxtH0Wi4RGGn0w96T3vAY6pgGARg3WhukFZIDcKmdiC1r5p2tPrpLa7Cac75QiD5296pElQrcaMfmmGdvpDjPFH17AQ5hQz7IQiVA21fAnxQsmbHWSsjRqWcTU1RB70rRloFZuv0unha53P00%2F0uw5Q%2F79JzRlmkpHhtknbZbcaBUUF7X%2FleNXCQbUBZiI1wvy8ajV8VHHfvL6glzijeqSIK9%2BzhyyrBEzrz%2FHA1M253JulqnPAdzE&X-Amz-Signature=ebd1b0d91b99c562128087413966ed9963363f571f85bce7f852128b5c54d78e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EMS6ZPV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtGTbyQH017DfO%2BhHPkIGokR5rVzjMpvCnA9fw8Z5vlAiAzyVkFXBfqP0j6GacZ8dypA41C%2BXjhOGUSyVMSIWPE3SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sfRKyL%2Fe7E2Ia6mKtwDSlotOOVYb6SHhJ7l59xIn6MhP0FgVvz98YUSkSHgB%2BlmwEBUUXdTvBRUkGUh%2FN1TG1UbK3hy792mAZCwuCcRaGjLYnn9CSu8%2BNqcHwx8Rtw1535fFJLfnRe7IgNRJnnbymDbMWXiXJc4imU75JdW%2BNWeoA4ciR5dN1pgSN7%2F1uU03lIoHv1MUUegBKUHBJVwBm1Uqh6S6eLlX%2F8ZjdmTIPruDcKXEZcC2qC0QxwrShxvXyN15k%2FCI0NFZPTbL%2B3UpJJNtcRjY%2FoJTEf%2FAqbgZjq5FO%2Fi1W8iaXcH19E%2FaEDmse90uk%2FpEv2sIgYLQFV8EyY6AS6eQYEdqNf%2B9mNv5gnpMnUnI16BS8BIT8qo7nHRgKPhS2PrNBbOCJF5KzMtNPzvz0FFEGlC0vyeHM3CWRahgnoq4xJgBvHoVg0m8gzQrOdIXXPUe%2FZNWqKyw6IgOGEcSbRlT%2BoetRMUDh8XZWZJBHoaBgo7BkB2eNdWG8cs9lRXJpytUhUCDdfi%2FOgm9Kz6VLs8Gz29ZgMJiIRRDErkVgrwI3FucPcAG5HVPCIax2D98JjELQk9MTsl3CyDcJF7JnzIoIr1mc8Fq4RYBQSK4h%2FeqMKO36M0j7LuW0%2B%2BMYtxtH0Wi4RGGn0w96T3vAY6pgGARg3WhukFZIDcKmdiC1r5p2tPrpLa7Cac75QiD5296pElQrcaMfmmGdvpDjPFH17AQ5hQz7IQiVA21fAnxQsmbHWSsjRqWcTU1RB70rRloFZuv0unha53P00%2F0uw5Q%2F79JzRlmkpHhtknbZbcaBUUF7X%2FleNXCQbUBZiI1wvy8ajV8VHHfvL6glzijeqSIK9%2BzhyyrBEzrz%2FHA1M253JulqnPAdzE&X-Amz-Signature=417ab62983854f5de0550a0252f7eb907ede55bfffaff0c8539c31d72d266e10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQQZOW46%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAj7g9aiQF844KS5ID7iTO4r1QckShy7cyWIAZi74U3AIgZs8fgxx2Dze1rYkQDOkDZ60oInBGyohmUt0wOrlvnc8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKWEiDzPiqTs85R8yrcA%2BZ9gQOmoE4%2FKsEPdYUzl3E8Fzhpu64xe8dcG9wIbIsUoM2snoVlR%2B%2Ba84V67o0KsdyK0seahWso6qY6Z%2Bg%2BWMRtyd4qVpVy9aXNAYPRC%2BBwNu8NgNIvQY14RkKhA9Xq8l5JbP7xXyrq%2BsaUhhEaKr%2Friuo3iAvhIX426g0tS%2BsMWu1UGeTVgsgSTS4EOe5duBz%2BHAHQCqPdNby7mHjZ3LRaCKd7aq0%2BxJdF%2FZ3h0eQ1oPbdFz77OZfYd2E1kL8cEB79cUVJu6Q2OYrkBnvh0bI0gkckQQRiTocgdbTMGz5bHwDn%2Bp4iFSqXTZIiXlAHKFffAkBes5ndpDLc8lYELEJ5qFfOFrpwARKKP%2BzbAlFDokEdFaXHxOWwXsDsE%2FnnyXZgCjX9tZgAL8dYOrSK7ol3eQvw3n02Mkpgx2J6GOq6NoMIUhnlWWsPJEiiMYF5MT43XZW9voEfH9aEUTjPoHIUZXkfQkRTzjb3rRqGHyP1HXN%2BdwaoOqnLDE4diXzObw5aHqmLkRit15c38VK%2BvY%2FPdOesFrGPzhksPNa9qDCq1E%2BBYMvuk2IHxTZW4EFcd926pq6vTK%2FJGFXI5rcvsrOgbUOM%2BpO9%2B7YuVJROMxgEiHN4JDWgoJ53%2B8hAMKCl97wGOqUBOm%2FpTVAokEOz84OlBGUXhIHOc4u9hhnn6nkloL%2BIik%2BrMwsIMgYB4e%2BXO10K2uRskwwVwznQHFRVItffqyEOmLZ93FocRyA3HgQHKijUWYavvMUFs%2FX90O0gdSSxBoLx9nr1aaJT4O3v2YUW16gMmKBG3mv1h3FnKnwmv%2BVpcnK%2Bq6QNw0SxIN8yK1i%2BGXLtsxxS7%2B5kQbiEIOH2nt9y2NKssIeg&X-Amz-Signature=6767edba30a0283eaeba3a81f95464a1d5561a8214659f0e56deb5043b45749e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMIDGRP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP4acQvrwgPWc6mvIpWE3NJofZfX8nREU%2FAHd8utxFuAiEAg6QdDjBAQPC7nc3FCx%2FrYhDZnYUslwpo0WBT3QMpBDkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdYusFIuSvA6qRY6yrcA1olOQeVnhlb3GbeqSXHBcoX0TXVQc7GnAKla0AHmmfkKEMHO%2BTR8Reib7DJEumvGSa3%2FHanqiMfEs4xtXoFwVXwvPo4LIEOxi7SLQ%2FCP6ji4x1muD0X9562L%2F36gF2YOuc3%2BQbSyy5dL8AsTuA5oLzyiqpFHDXl%2BbPTKMAj%2BoNZsR%2B1xxMExdPyp9k%2BGleTd3TSBj6Z1zVM8QJUmbtNQGm%2FWKXrr6niRfPQFmbY0LduJ9sQYCMVfWXZWTJLTNgbfvmkGe014k02EHBqIzG6%2BlDnF2aSCzPW4TXVlc3XbxTzHSPunmkOO28v8BeBXtbAv3xTmizNkKKWhFHdZrtZQqizwR7EcT16OilzBzeRjyPk24NAiEBz5vrF8IXGuL%2BK6HQO%2Fd5M71U4ztOQ61WrStROn2vzzwba8wdnz5e3C22xe%2FwAxfxS1wC458BY44URhCospdwTYkXv6YXPT7Q90XoNsN7jZi8bUzPRTfE8ABOEPn4NQhUlOF6jOSAW7VonevXOV%2BogRbbAjxLZiTp5wTJF3YbTfckxHWMzC5ztxRZocm%2Ba%2Bv6ax9aha3jRYAkOnFVciAY4WAWgvMXgel1%2BssKFwFAe0VfE2nFPHqe1oIENmP9WOfy3VDX6u3saMOik97wGOqUBHZdq9m0A%2FzV2EtgCvEMf8rC8gm98pmf7uZ4MNj%2Br6JkPrfFkVRHyCsqcZ713OusYYO98ba%2Fjq%2BM1x%2BjI7tLSaq8iv1SEOM5nuxgBeyoO8xJl1NFYQKReA3153cXz446uyN3%2BPNME3O87ayA3W9uc9TVSPrX1EwjfmkmunyVEZenMRRp0iVSC5iPu3v%2BrW7rzEXpn0Qba8WbVEl2YuXwzzEl0Bkvh&X-Amz-Signature=88119915589014b06def28f46c3cadff02936fbaf002dcd243be4b292b401eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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