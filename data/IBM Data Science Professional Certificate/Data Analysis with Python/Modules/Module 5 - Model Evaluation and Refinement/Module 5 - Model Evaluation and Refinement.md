

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=e9b82400639b85b156298e88480fc8fe04c87892885b2c6aff9f6f04db9e8b1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=9995e97a83eaf6fc71a65e327cad6d50e8fe076d1483cda00abd6ec7c8148df6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=fd82998cf5bce93f20a52bde59c2f0a917dfd6b9a06832bf5c7efaf2a49a0175&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=8f2331f827b23e6a8c150e78e04a66d86d39876d32d03ac58813cfa5795e7d78&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=711f6c7df955444947083e547eef3b80a900072e58ff83ba115c1a6488856b6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=f38a578f58f87cf7998db64a91ec39fb03428344898d4b6be2570d5e0beb0e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=926ac20485a5900954fa8fb74cbf4246dfafdf5d38c995e9971b95875e8d786b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=98886ffc0a39b6940bdaf328f3bd27ba965e75520974ff2ad7310456e2bd54b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=f90caad32c73ccd5cedf7b3d79eeda7da1a41a977f6253e5a32831acc75e2fd0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PE7ALDE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAstCQZ9gL58w8MO6kLNM4n4xqwek%2BBfVfp6nJNWEEE6AiEAu%2FssbVg2mx8PKpRrt6gtZo6YCSz6x19RKkoME4XgFkIqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCNzHnJQM9VhxV2HrSrcA6YtIbordGLFJ6LgmFCOXf6wQCquqda%2BtDTM8Q1FbyGoUhOlTPGfrdFcKsKzFJ24lelc21BkfxFdN%2BRXs1qT%2B3tgS1veANx68TK5tC87WQ8K4jSvN26KA98inJnK2y2JLdWTSE9d638OKzZvUVaMwnlvvQN21XjQCWkRm0%2BqQp8zEl87GDWP9sNn7kQ8fajrUuvA7JTOTRJx8rbpcsENDYy0%2BP3fwR3GuTDUNxcEoApivB5jBQgFBG%2Fgh2Cbsb1eLbMPTOMOkzbGoRS3JVczzKYPACvYz%2FvHtKSfVvDdLe9CiVdKJMNtMXINYwvrEwELliikK4glSYIR5aSxphZYhoidBmP1LcuOviH5WxEt%2FX%2FJ9YyA0hSzCe05lbzbvLdecVlRYV76hblhFsm4Nt2dD0Ew9t7N0GxXlIdjYZapYCQqThLo3Avu74mwss%2B%2BwNTL2CGeMjrwOEY7JQQsf8VRJEsr%2F6MNBcRIicxHC8eawUcqAC%2BvFAn90F9Y8gQOpIG2AM%2B6pdUV6XHliekqymkJvjdZ2dmeW6ijZLxVihBF4YIxV3pGAxsAwuFSQqw4Pz2XC%2FiK7sGaRZC8CsSLkZd%2BDqFQVPOgItAR0hmQAIuuQJZ8hyvl%2B4gLMWZiemo1MOa%2F%2BLwGOqUBJH%2FN8FFaiNQMebuDUoD%2BukjGxHqWYdjRx0HE33FAi1L42YrYVPPb0C2HwaG982cCGE9qpHJJrztGfXCgmbERqrLx3e5TxOPc06kqOpG7zyyYrpfUg0YXO9FWStZ%2B%2B2GWCrtrkVX0U0UYGTH%2BVkeRW3Z1FWhifDOpEIJgBHXDfACm4XekIb%2BADyt5sOXE%2FMHlN5FN3N1jtYiizUd1n%2BuXbOTrBmNm&X-Amz-Signature=12ceacb72df9032613fc696a67f73d698acf94a42359eed5f206bf31dff51a77&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PE7ALDE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAstCQZ9gL58w8MO6kLNM4n4xqwek%2BBfVfp6nJNWEEE6AiEAu%2FssbVg2mx8PKpRrt6gtZo6YCSz6x19RKkoME4XgFkIqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCNzHnJQM9VhxV2HrSrcA6YtIbordGLFJ6LgmFCOXf6wQCquqda%2BtDTM8Q1FbyGoUhOlTPGfrdFcKsKzFJ24lelc21BkfxFdN%2BRXs1qT%2B3tgS1veANx68TK5tC87WQ8K4jSvN26KA98inJnK2y2JLdWTSE9d638OKzZvUVaMwnlvvQN21XjQCWkRm0%2BqQp8zEl87GDWP9sNn7kQ8fajrUuvA7JTOTRJx8rbpcsENDYy0%2BP3fwR3GuTDUNxcEoApivB5jBQgFBG%2Fgh2Cbsb1eLbMPTOMOkzbGoRS3JVczzKYPACvYz%2FvHtKSfVvDdLe9CiVdKJMNtMXINYwvrEwELliikK4glSYIR5aSxphZYhoidBmP1LcuOviH5WxEt%2FX%2FJ9YyA0hSzCe05lbzbvLdecVlRYV76hblhFsm4Nt2dD0Ew9t7N0GxXlIdjYZapYCQqThLo3Avu74mwss%2B%2BwNTL2CGeMjrwOEY7JQQsf8VRJEsr%2F6MNBcRIicxHC8eawUcqAC%2BvFAn90F9Y8gQOpIG2AM%2B6pdUV6XHliekqymkJvjdZ2dmeW6ijZLxVihBF4YIxV3pGAxsAwuFSQqw4Pz2XC%2FiK7sGaRZC8CsSLkZd%2BDqFQVPOgItAR0hmQAIuuQJZ8hyvl%2B4gLMWZiemo1MOa%2F%2BLwGOqUBJH%2FN8FFaiNQMebuDUoD%2BukjGxHqWYdjRx0HE33FAi1L42YrYVPPb0C2HwaG982cCGE9qpHJJrztGfXCgmbERqrLx3e5TxOPc06kqOpG7zyyYrpfUg0YXO9FWStZ%2B%2B2GWCrtrkVX0U0UYGTH%2BVkeRW3Z1FWhifDOpEIJgBHXDfACm4XekIb%2BADyt5sOXE%2FMHlN5FN3N1jtYiizUd1n%2BuXbOTrBmNm&X-Amz-Signature=f87dd4e54d9c618713607d9340eff0cddca71f05d0c33dd3d1ce5aefbc3a2959&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PE7ALDE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAstCQZ9gL58w8MO6kLNM4n4xqwek%2BBfVfp6nJNWEEE6AiEAu%2FssbVg2mx8PKpRrt6gtZo6YCSz6x19RKkoME4XgFkIqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCNzHnJQM9VhxV2HrSrcA6YtIbordGLFJ6LgmFCOXf6wQCquqda%2BtDTM8Q1FbyGoUhOlTPGfrdFcKsKzFJ24lelc21BkfxFdN%2BRXs1qT%2B3tgS1veANx68TK5tC87WQ8K4jSvN26KA98inJnK2y2JLdWTSE9d638OKzZvUVaMwnlvvQN21XjQCWkRm0%2BqQp8zEl87GDWP9sNn7kQ8fajrUuvA7JTOTRJx8rbpcsENDYy0%2BP3fwR3GuTDUNxcEoApivB5jBQgFBG%2Fgh2Cbsb1eLbMPTOMOkzbGoRS3JVczzKYPACvYz%2FvHtKSfVvDdLe9CiVdKJMNtMXINYwvrEwELliikK4glSYIR5aSxphZYhoidBmP1LcuOviH5WxEt%2FX%2FJ9YyA0hSzCe05lbzbvLdecVlRYV76hblhFsm4Nt2dD0Ew9t7N0GxXlIdjYZapYCQqThLo3Avu74mwss%2B%2BwNTL2CGeMjrwOEY7JQQsf8VRJEsr%2F6MNBcRIicxHC8eawUcqAC%2BvFAn90F9Y8gQOpIG2AM%2B6pdUV6XHliekqymkJvjdZ2dmeW6ijZLxVihBF4YIxV3pGAxsAwuFSQqw4Pz2XC%2FiK7sGaRZC8CsSLkZd%2BDqFQVPOgItAR0hmQAIuuQJZ8hyvl%2B4gLMWZiemo1MOa%2F%2BLwGOqUBJH%2FN8FFaiNQMebuDUoD%2BukjGxHqWYdjRx0HE33FAi1L42YrYVPPb0C2HwaG982cCGE9qpHJJrztGfXCgmbERqrLx3e5TxOPc06kqOpG7zyyYrpfUg0YXO9FWStZ%2B%2B2GWCrtrkVX0U0UYGTH%2BVkeRW3Z1FWhifDOpEIJgBHXDfACm4XekIb%2BADyt5sOXE%2FMHlN5FN3N1jtYiizUd1n%2BuXbOTrBmNm&X-Amz-Signature=9c91d01307bda83f8d758462570cddc2d3973558d4efc4d07738cba2d2c2feed&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=7c77b1f5e11d55eece91dc5963752873181007aeb6dbcc7625eb75374d9aaa1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=0c56d169851f1695e5345c383350cb52fda9400c6bb7ae8bb4d137f5d5048211&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=74b2a51a0c21aa54a8c8fd175b784debf13d40b6cdebc5ef3ea2aa17f836c675&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=4a7d2b756f7f9a164d894271495acdd0c65bb788bcfbddd0613d0c3eb4af4ebe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=3f462d52690ffadc0f82a1bf12378a04ada9b99f991b824b2d01fd72bb616b71&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZKU3PGO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaMODry%2Bd38H%2BbQJZJbmnscO1yy2NE%2BHCIqi%2B38gpDswIhAIhn0%2FOL7qg60KCVhArIFuZp76Y1dTm8Th8Oga%2FcgiSSKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxAhjzXRf%2FGE1d6pZ0q3AOTJDvXTDXxtEi5RFzzri4xXYaXaH7KVwXVeCkQj5Zf2R4u95D8UBQWdC5%2FjweL86tPXHiJhbjvyglTp%2B5tZWtffgzn9HGa%2F5fNmQVNpVHhwAVQEq7CWCKhbQVKw9I2o5LC0pwQbS9CbrIvpjFzg%2F6NJ73jQ%2BgtwsrDEgSTAc09A75YMIuZb9XFJzJnJEVKv11AUJA%2BOT3t%2FWc%2B3UwU4da7KOSfEw1c%2F5J%2BUwSm3SZ7E%2FnrViU%2FFdWPCyMi2fIRuLrrtCohP7tTQdZSXLNR5ghKnuC45nqSdktAF7mLfgk%2BYakDlCP0SPF6cO02ro74NoyihKZqMIDxCuqtKcFeha8E%2BJFTCf7dZZrkUCNMweoxwATenfpyLilZCJQdrufXHZZZSAAUOLLaAemArQOfpRkW6oaB%2FJo%2F2iPKmQDB59CHDYSELY2EL%2B6DAPA2L66cKuXZjy1NnZB%2Frb0F9%2BMQfDzmrLnJRk%2B9A3a9u9kbwhMSZUYCF3aFJ8Q6g%2B1VgoMo2HCMZqeWEjijZelwOaaPrY5xHWwkiu05%2Ba%2FaTKVrvrIs3mW0uIAJpAaV1FgjCZHmGwnG8trl34VCKxYICaHcxllxhvKrLV%2FjXjdDrPeVnOqqniJT96e9vaAv9Je1CzDZyvi8BjqkAVJSPy7S4v%2FBCJZT1XyFnFGoq0GagfcjmbSg%2BHXLV6C3X2j1DdUqZqv7PKO18%2B8WYwPS5944Tp5Dy8nEmgQYlRRGRITM84OavtV6KVQUbE7f%2FIrvCPFMzW90e3b2kXHWh1GEwjhkk65J2ebJtX88cEK4Ytlj0ISIgYI12YZKpyBi1VZH7hNrj%2BSLMVvyptWmMQELmy7ZQJWLJf2Ca5qNQF5cNYPI&X-Amz-Signature=1175846c5e0a8a25afd17e383a3c55a6b138abedb8a3aa6384e95973cd2d8577&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=eef718bc8ac36d1e2572fe5711079e4cc7fb9a7985aa0451bb4461d9ae3546e5&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=cd4deb5866c23348f14c127de890f3547b87d98497a6ed7b8b704f89c0cb3fe7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2YA4MV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkkP6UGYgfpDi4D%2Bfdf%2BLPzX2nuYdSspuVyyLevkj1jAiEA45MiAQ5W6YCNRohKCq73X4EnacZZ4iz7%2B5C%2FJpzlAuEqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPg8gus3gT5Ng%2FBRoyrcA1TspzZPIcuQwCJ8KOLU0%2FaEPAcMP7hgqtt%2F5ObGDWDVGVFL4i1Nmj1%2BsirByfnz1rxLDtpxpgb0FReauFkKePXYwg0X44c1EEiPu1xtxpBhzub6Nb1EbnwhTWy7fe8owIRbB1CpWuiWBNpcULd97PnmT8cDEY8zwj6rH3VRx2Ii1OLez34WJSRAmfcMbxrDrvH2yc9DhTNI6EGOYf3gjjwR9c7O4m2bsbQn13YFZKgbqCbpgJaiwzpGySiSOaUVPnisei2ybvoKiBbP3Yzkyyt%2Fx2BMFViBVFpQUAgMCretZCo77PoL%2B8sdIayPIkMRMxjTXQ8sC9mtXu1iCbE5Nv1lhI2nBCLEGm3ELx2tFuJcAkKz%2BGL4w188fXQ6aOUG5PC7frvPZukXwuGqc7p2E6sALTzOuksY5qxhb7KeB4uPS%2BLDtxfJpzsyOqhfN3NWs%2FlHOhza%2BGJepX99tYJHmxff%2Ff6ZBfcYrqrifeIGhEheRK04FiFqYfQRRpS4XUDrDyrOTz53Bg5wIIgX7L9ypXk0v4oKkj94PEtO%2FeBHZqJIKnWuFltSbubDndxUHbHJGu8uTrKmM5Z3KWGiHUWT6dtYRODdmykbECos0iZd9DDldgN9ir127RoXzcqVMMXB%2BLwGOqUBmp0vl0q1UB76z8heR7AqzQpjHeI4A9sXipNzt2AwjLN5m9qsrFWlMMLxlbpa%2BKqVfAt9CpHptI7S1RSbKJOXQhZkoi%2FFM5lAs4SRVfomrQR4wUFhyBsDR0Bo4KlLwOHlKMEH6yHjr04950ZFqahUCL%2FYEkv6mfcpkzito7IYxh7R6ffEsPsTOM66x%2BBTb2BNfvEp0ASBtqqkvh7z8VGFSYQvC914&X-Amz-Signature=87cf332ece9f3047f5036cd5f281db754b9f9c553b0f1e753ed6b2a8be224955&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=d35517a518518b798c52544b4ab0b72d14525445a2040aa4d87157d9986fb976&X-Amz-SignedHeaders=host&x-id=GetObject)
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