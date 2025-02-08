

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=49d7245c1d867302b0a2f5f455be7d022bfd0ff94c04990363701a4fb5921078&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=8709ce5b9b4bb8157e2db366233db66ff20cf3b410fc564c85f632c35fe036f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=4694168a93233997f6d0aa4b8c2c5d62d9f56327ea5d4c7545b30991c1c0bca7&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=206626997d107dcc536b3c3b9235e4f83f84a8c624962499694e000957b1affc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=e03c203e2e3e1af2f1c8a7ad2c912eb6de10afc06be67e519b5f9e9beb7a0739&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=2942690a579b8ceb23487dd1a2bd9e4207d8955df745b3305b54c9e5610a28f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=dc7017e01c7f5d935c12775cbf945952b785f4e24917f7eb4c042f4d57252390&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=34fdb167c03aa3b6b1ff099584b39acfdce1f283cbec2c61e0613b44525f9033&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=9d3a673ee9d2c0448d828c35c4b81d2f2b54a8e275024b74885cea7d2d6d9b97&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GJO32U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHPy%2BT4YqqJFr0FXwQooHmoGcj1vznfbMjZBRxL4LJRpAiEAqY7YBEfLt4V6cQmrepQ3UEVIZORD3USSs6qjSnFOe10qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNVCXH8pYpxbFFO3pCrcA1WXI9CheqtxerWc2HOGbyEHbavwf2VTTYZHmhYrZzb%2BHY9rojn%2BK%2F3dk0Jh9wivuxCJ5emQIdBjGlxnn4Wep8U%2FkbP2NjhJxoHSmquQY4vh5uDt%2F2OE85SAHoVS4%2FNPr35qCEhzEdfNDrqBkt6HWuEyMNT9BAdGvk0yhuzf%2FFx%2F6Pcac7rWdWM8yPZf1QrjMo11XVShUDlt9cp0HTPPaNhaFHm3YIeJIb0Sx41ZN9IEvg00vegdaFkgs5xWfbvm%2FrxLBw9%2FyAnJpjuws0RnLDJAJjWIflDCfhRkDt0yvB0GjLeGR8GG3nl%2BxI%2FL44uimfwqhHHygIfpY%2B%2BfnSzBR9j2sFNobpvGLxTGtTESDBIpNiPiUYSiH4L9l%2BXbH3qei5T6bl78LOpsNqWuwVihKSXvd2ZQ9UqOLOX6Q9idChvDHH1iwLe2pQB4ZWh10Q35acAIbrGgEwhWMXtpMd1LbKqA%2BY1NlF7TABxVZCX57obw0BmhKtezDQIGFGkPDGFvA6Pw%2F2%2B6RecQnxu%2FlN6nwaASb95RJzNOzNi3YVs4OurULlHz2x%2FXtThEnwAm0IxsPG34f32u7tQqNwBrN58XxGpnDt0rN1VcMLnsmy90VaYkjLJZp8LmOMiTZizPMMeOnL0GOqUBSaAbfEA%2BpSIdoVDomh3F7ZClgCaw1KFJ76WdztQxGaoqg6Iotg%2Bt7z2S0Q0nAy57PTXzE6bq8wMn2WQ9DyifQSOADobFsoMpDIu3kEvM3t6%2BQTCxYsCcfl%2BeKU%2Fq3PhH%2B0u3dhZMxQHf8LxqAoGjULNR1J5Gn%2FFe%2FxkCIeZwf0pHKFkPcs1%2FMDtuxL37NfAjfn82neLLJT3jLoo53p4BAgXQ1UD3&X-Amz-Signature=ff5b35cc9704a1db60ed2f6235139b2886d6f594eb0e061407aa712c08c9f3d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GJO32U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHPy%2BT4YqqJFr0FXwQooHmoGcj1vznfbMjZBRxL4LJRpAiEAqY7YBEfLt4V6cQmrepQ3UEVIZORD3USSs6qjSnFOe10qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNVCXH8pYpxbFFO3pCrcA1WXI9CheqtxerWc2HOGbyEHbavwf2VTTYZHmhYrZzb%2BHY9rojn%2BK%2F3dk0Jh9wivuxCJ5emQIdBjGlxnn4Wep8U%2FkbP2NjhJxoHSmquQY4vh5uDt%2F2OE85SAHoVS4%2FNPr35qCEhzEdfNDrqBkt6HWuEyMNT9BAdGvk0yhuzf%2FFx%2F6Pcac7rWdWM8yPZf1QrjMo11XVShUDlt9cp0HTPPaNhaFHm3YIeJIb0Sx41ZN9IEvg00vegdaFkgs5xWfbvm%2FrxLBw9%2FyAnJpjuws0RnLDJAJjWIflDCfhRkDt0yvB0GjLeGR8GG3nl%2BxI%2FL44uimfwqhHHygIfpY%2B%2BfnSzBR9j2sFNobpvGLxTGtTESDBIpNiPiUYSiH4L9l%2BXbH3qei5T6bl78LOpsNqWuwVihKSXvd2ZQ9UqOLOX6Q9idChvDHH1iwLe2pQB4ZWh10Q35acAIbrGgEwhWMXtpMd1LbKqA%2BY1NlF7TABxVZCX57obw0BmhKtezDQIGFGkPDGFvA6Pw%2F2%2B6RecQnxu%2FlN6nwaASb95RJzNOzNi3YVs4OurULlHz2x%2FXtThEnwAm0IxsPG34f32u7tQqNwBrN58XxGpnDt0rN1VcMLnsmy90VaYkjLJZp8LmOMiTZizPMMeOnL0GOqUBSaAbfEA%2BpSIdoVDomh3F7ZClgCaw1KFJ76WdztQxGaoqg6Iotg%2Bt7z2S0Q0nAy57PTXzE6bq8wMn2WQ9DyifQSOADobFsoMpDIu3kEvM3t6%2BQTCxYsCcfl%2BeKU%2Fq3PhH%2B0u3dhZMxQHf8LxqAoGjULNR1J5Gn%2FFe%2FxkCIeZwf0pHKFkPcs1%2FMDtuxL37NfAjfn82neLLJT3jLoo53p4BAgXQ1UD3&X-Amz-Signature=801cd80d91e1a45f61257a40f87369331b7c157b751ad6cd3e92c253127c333c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GJO32U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHPy%2BT4YqqJFr0FXwQooHmoGcj1vznfbMjZBRxL4LJRpAiEAqY7YBEfLt4V6cQmrepQ3UEVIZORD3USSs6qjSnFOe10qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNVCXH8pYpxbFFO3pCrcA1WXI9CheqtxerWc2HOGbyEHbavwf2VTTYZHmhYrZzb%2BHY9rojn%2BK%2F3dk0Jh9wivuxCJ5emQIdBjGlxnn4Wep8U%2FkbP2NjhJxoHSmquQY4vh5uDt%2F2OE85SAHoVS4%2FNPr35qCEhzEdfNDrqBkt6HWuEyMNT9BAdGvk0yhuzf%2FFx%2F6Pcac7rWdWM8yPZf1QrjMo11XVShUDlt9cp0HTPPaNhaFHm3YIeJIb0Sx41ZN9IEvg00vegdaFkgs5xWfbvm%2FrxLBw9%2FyAnJpjuws0RnLDJAJjWIflDCfhRkDt0yvB0GjLeGR8GG3nl%2BxI%2FL44uimfwqhHHygIfpY%2B%2BfnSzBR9j2sFNobpvGLxTGtTESDBIpNiPiUYSiH4L9l%2BXbH3qei5T6bl78LOpsNqWuwVihKSXvd2ZQ9UqOLOX6Q9idChvDHH1iwLe2pQB4ZWh10Q35acAIbrGgEwhWMXtpMd1LbKqA%2BY1NlF7TABxVZCX57obw0BmhKtezDQIGFGkPDGFvA6Pw%2F2%2B6RecQnxu%2FlN6nwaASb95RJzNOzNi3YVs4OurULlHz2x%2FXtThEnwAm0IxsPG34f32u7tQqNwBrN58XxGpnDt0rN1VcMLnsmy90VaYkjLJZp8LmOMiTZizPMMeOnL0GOqUBSaAbfEA%2BpSIdoVDomh3F7ZClgCaw1KFJ76WdztQxGaoqg6Iotg%2Bt7z2S0Q0nAy57PTXzE6bq8wMn2WQ9DyifQSOADobFsoMpDIu3kEvM3t6%2BQTCxYsCcfl%2BeKU%2Fq3PhH%2B0u3dhZMxQHf8LxqAoGjULNR1J5Gn%2FFe%2FxkCIeZwf0pHKFkPcs1%2FMDtuxL37NfAjfn82neLLJT3jLoo53p4BAgXQ1UD3&X-Amz-Signature=cbc24c61ef572145c2089a0bcc4e10b3e1cd69fab19ee9cb2256f30c11fcd03d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=045195ac87466b5bb63267442074f0d2fc77554d7e24d07cd7c94f7397de9428&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=c6c42a02c1b26de3f4df7bdc2b0e3a08f633920d8e13ab61e29e7762fce6a65e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=72c07ceaa09772582a3edeca709a55cfadb66f5e4b791291c1bb3a5e7287f0fa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=265cca17ca5cb208c3cf132f2dfa167ae65bf9aea4ded1ed9c56cb933da01f46&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=0fbe2cf00b0368e6b93ec19524fff140ef0fec5984faad77e9788f6a32ffa70c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D6LP7UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDJ1GPkzs9ARzk6aLPpR9sRwsqSfXY0L1CUe%2FUOZzatRAIhALPkTGL85DjUvhatbOsPLCwD2a4YBBTsx18kzYYWpvF%2BKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1pWPyNEL3fbTOXl4q3AMjrjuBbLcHQklmWh0kaEHNt80b7muRBwlgQkj8uzg5Ghy6fBNfHmSeOrrUO0pkJtarSf2BvyWC9xK692AELi2fkFFq126cF15vw0zJ7pH%2FDsRKU3BwR58t9NBFY20Q9yNLUOLu4rtZG7GPiuH0UaSRhfl72WZdAYp7ouGSbURhTilCWCXv9mKnOQQMUKa59wBJ8mJjwsi3I6LkI3L3mXQ748Bm7nZAzEFmMDfpr5d%2BO2Z%2BZuj4L3jRyJcymOulI8d7AtWKMUngF2M9DC0vuLAKmdDWmxCpP3a0aCBpryyo2CVJO7f%2F1L4PQ4BYnSingHFho2%2FSBr2Ah%2B8cw1jvA1Mi1XS8CsvC5iTFx%2BWzBfOsCCyYDpIVGrU2%2B2x%2Bo%2FaEb7lWGQ6ADqi7i1pNwPWCnNFSXouQvwtiVjv8alDEtP%2BxVu65uywiBsaUKPvwntu1Gu09%2BW7fNWxU8YPWg4mA5SJ4H0e3JCi2njZkORe2dFZy81p4OhEytPnpIssfYJhsDX47yA%2BQfJli448HX%2FCuiJhGIUoOOPp%2BM6bJy4w5CxD3osr6PWyCS26ZK1yeiFFBIjDDmUPP5%2BRzpyCDSqkoE8ggiUkN5SuYdY8q4eKKO9muZNUgMQ3UW1JbWmkQZjCJjpy9BjqkAdjS5GlWr4ihcbfgUfGEsp9xAuNLRzIvA4bJ5yIYivkqOTrv%2Bj42QvW1yAtUIU4xYF23RKvp2xGmYhDalD71R8y%2FqLgqDIwtYKSwL9%2B4PyrZuNU18mfnXiDySZZq%2Fw2zjpOXBY1UqeejCYSP6jPxx3rWsJEmbM%2F5VVsYkND%2Bu%2FxgZRC7Zkq%2FVLhKZtJZLSsEeiIlX%2FPMcH8otTWsZa2ldc32OP1F&X-Amz-Signature=2e87e9809162584596a9dc0d59222cb042413819c012a45a6f6890464e3fff03&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6CJII73%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDbhjDfI7TVmnHqJ6H0e%2Fag1INi%2FyoZwpPF8Spwny2vzAIgWsxKLG9njUS21CG%2FUH0ecpkjiKT4lAjQvMR0OfYG%2BrcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL8uMbNnt2Zy4anQAircA3ohzKXtJWz2%2BApHZ3a9UN%2BoZkFMGy9TgNSt3xC590IBGCbjO3ybZUkbUTnAL2F%2FIkN%2BrGgalvb46ZiumoXRYVHC80dyFc6vbe0VZ0ScTD9MZq7uSco7onB6uR9LtB2%2B6PaSD%2FK1OWJvjNTdipCoOShPnxAI3SY5xlslz1l6GwduHSFv0lnY1lVGfy3q8ZNYHuyVr68L0iPvDIyvzTwzzOX%2FaJhjNShwk8Qwrm7q%2FbTEjwUvt%2BIYWINpunoj1%2FPTXpQNiMjzibk0SA9ZVsQMmfYi%2BvI1tN86py2m%2BRpx2U1MoNVwsFJ2OkH7giEh7Dyz7cJpqB3ap2DCx%2B2NtlU0NxFBCTkLFH12T6Prd0VlAnOpuDqD%2F0HSTsk6yQ9XkGpcMgkoMYJ1IefbZnE%2Fn%2BdvH4FsOPuYUY8ZWzDrpPl2QJQqn6ylsBluDo%2BAnjwIGTT%2BG0tqzFt2ctSmt7kirk%2FrFskpjUNhlMKkeAoAfvmivC8GqVgLqX%2F5oLRs1%2FP1rZxGv%2FaY8DgRpV0yKcKFTnRS2bUBwyx35fWwlWSrwoKUt%2FAv%2FYmldovoh%2FyaYMUOEE7jpTogap07%2FpUNlVwByuZzHjGvbQ1ZY71eDSWVnE8OiDPT%2Fs4o%2BcW1dkHqzT8RMNeOnL0GOqUBBkQs2Ip97HQR0sm1rKzmhnIqP%2Fv%2B7UV95u6AszI8nSkkUqadRm1pnQcnwboA5RPKSHVVQ6iertQ%2FAutKtfgekPzZ7bjO4Vkfv8c%2FU4BkOsmY%2BTaOEsj7ES5kAodOjNfU%2BU9TQQN%2BaQjBpvjvuiDSj4TuDk2esNDXne8lfF19c7nGoEaJTQUaIDGJEFZnjv3nUazXUtZ2wr1ir1PYBA8rd9K2kItG&X-Amz-Signature=47093b9e00d7956f2972abc51d570a9695b999c6136c61b0f6a3a8b4c8071768&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6CJII73%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDbhjDfI7TVmnHqJ6H0e%2Fag1INi%2FyoZwpPF8Spwny2vzAIgWsxKLG9njUS21CG%2FUH0ecpkjiKT4lAjQvMR0OfYG%2BrcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL8uMbNnt2Zy4anQAircA3ohzKXtJWz2%2BApHZ3a9UN%2BoZkFMGy9TgNSt3xC590IBGCbjO3ybZUkbUTnAL2F%2FIkN%2BrGgalvb46ZiumoXRYVHC80dyFc6vbe0VZ0ScTD9MZq7uSco7onB6uR9LtB2%2B6PaSD%2FK1OWJvjNTdipCoOShPnxAI3SY5xlslz1l6GwduHSFv0lnY1lVGfy3q8ZNYHuyVr68L0iPvDIyvzTwzzOX%2FaJhjNShwk8Qwrm7q%2FbTEjwUvt%2BIYWINpunoj1%2FPTXpQNiMjzibk0SA9ZVsQMmfYi%2BvI1tN86py2m%2BRpx2U1MoNVwsFJ2OkH7giEh7Dyz7cJpqB3ap2DCx%2B2NtlU0NxFBCTkLFH12T6Prd0VlAnOpuDqD%2F0HSTsk6yQ9XkGpcMgkoMYJ1IefbZnE%2Fn%2BdvH4FsOPuYUY8ZWzDrpPl2QJQqn6ylsBluDo%2BAnjwIGTT%2BG0tqzFt2ctSmt7kirk%2FrFskpjUNhlMKkeAoAfvmivC8GqVgLqX%2F5oLRs1%2FP1rZxGv%2FaY8DgRpV0yKcKFTnRS2bUBwyx35fWwlWSrwoKUt%2FAv%2FYmldovoh%2FyaYMUOEE7jpTogap07%2FpUNlVwByuZzHjGvbQ1ZY71eDSWVnE8OiDPT%2Fs4o%2BcW1dkHqzT8RMNeOnL0GOqUBBkQs2Ip97HQR0sm1rKzmhnIqP%2Fv%2B7UV95u6AszI8nSkkUqadRm1pnQcnwboA5RPKSHVVQ6iertQ%2FAutKtfgekPzZ7bjO4Vkfv8c%2FU4BkOsmY%2BTaOEsj7ES5kAodOjNfU%2BU9TQQN%2BaQjBpvjvuiDSj4TuDk2esNDXne8lfF19c7nGoEaJTQUaIDGJEFZnjv3nUazXUtZ2wr1ir1PYBA8rd9K2kItG&X-Amz-Signature=5f2cf874955f3dd66c9f3e615a572fa6faddf484729ab0de97885431e07bb878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642NAFGCN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCvc05z6v%2B0lNNFyu1rp%2BwxnhdYyzonEcjjpcmSs92pZwIhANkigjjxtIvrYVPeno2Yr3oO3L4xEj2JXFutsZ0zL24eKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyto0BZXdwOZbxfSmMq3AOjIRvEfFN9aKciKHQM0lKAiDcc7nbyme0e%2BQg79pUc%2FQzFhwqHjRowFbBMxnwCZT00wxGcSCsalPGnPR80zkspyzO8A2FP9PTXBNasV5aVUcg0YqUTJoCE8gDpsCZkC5S21I3Q%2BDdZLQDyr1nyxCIAuaRAI80VjL%2Bn3quOtSA7VsyFQUDAtn9L0gykN7AjW9ilKgy1d%2BBKB%2FQNIjAxUsuu9jxuZ4XhtRSa2SyVs3USm1%2FSoWCeFBzgVLWu%2BvriNHmNyQtW3y5VispdNAubWBJbR9wKNfkqGekG6%2FGiNljikrg7Z4fV9GLphQCZ47fnn8eWXtzoY6NiRKE9Sh1P0SZ63zcCRnhpN0ZCiMNLvT%2FkfIa5%2FVO45pRTpdgjA7IOphlPIoNqkl39XTjHWEg2Suf0toQDL1Zm5UuFMEBc%2F9WfxmyBZFhKKzMAaQuPwlruNNju8EZtHOPgS7bTChcO1OSI6NgJ1SqVPqKWAyPlTFug8JBHBuFNlUt%2BTaYIUUMirYc3w%2FXY0zWyHvwIXX3fzlEN7pUcgPoeNstnjQ35ZQeAOqYU2sx45N4lj3oFnOXnyWbgTF%2Bmvw2pgIcDLKlh%2FMrL6xRBJbj5XFcUbCukEYgTpl32oyhDBvl1rYKaYjD4jZy9BjqkAaDS7BS16gVHNzQZfVYZuwfdWBvKu058gttDHSQ81ncDMoVX4PglI%2BCW7lZzb%2FnN0uH%2FRUN4kjTILbE3ZDCQVUMJhrahA0bVzlOfrU9gFU3zSfhsOs9SlbfyEAOTfw1GTzyixwlyasdzPo1EE5E%2BHg%2BKrOI3ueEfzFx0H53ou%2FVoeoIu0DR650iiFPfv5QHSXyh3JQ7tYUBhL%2Fb6mEPfgM%2FdecGr&X-Amz-Signature=d53e0985caaf8759d2498b8d591a2dfc7bd28727ead641a14c89395808f4b606&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI62OH4S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICmKfw8x6Q8QQXlhE71ujsiE%2B8VlGq7XNo7%2BJ17V6nrwAiBhazUxpZ0BVOTi%2FoLltRMtH2%2FeM9ByyXs99%2FPSnxBu8SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM62HmdKWjEkWgF0rrKtwDgiCO6tji0sFfKK%2FSkjZeJTcZWmZ8PPS269szVmnBibM5jqI13SXT75nJGteHoX7rAdmGtrqZ7LcF3Azi6pJev39lrEwJ%2ByfCohhRnlBY7gWWjlWL%2FiQ5K0y9Tucu8warLU0kngz8QIrrkIOJO9yzY32OV%2Fd3wTZlzbvDsimUmOIRZwJsi%2F92hDjLnGXusE1BUNIYce3tbkDXd0i6xx2UIe9J470g6I%2BJs81tprreYOAE4x12cPT9gyYAfaVtNoS0k4BpIHACUorNHXXOJEtC2h25qL2uPC4n6%2FWZt%2B041hz8u1sRFxaQZ5xI6HHnuhZclHuUig6cQrK%2F%2B7BphKUPpQdx6ayJg82cTUGiooySoRNUNjCfR9awHRdovW7z7bNlztjSHsBYzCVvCdz%2BGH3oTCyfGDHsY9A%2BccFKmn1HUAF6Fn4r8ddm%2BKqULBRcoUBU5b0IiGVTwuYEO9X6844gCbZdJ2JACFZeCy3UFUJ%2Fv7bQn4ObwHF4SW2QWdtpXz%2B2gQFeKgLlscGb1d98T%2B0u96MUPfwA4s%2FKt8YnfJcVbJqDba52Icsr3dcMBYbxxV7shMFj6c1x75Ad3lHw%2F97GQ4IeDL8fLpNq2%2BGbzAWnLAhyjKdfhpEPiUlDvvowxY6cvQY6pgFvp5nA%2F4UHmg78PQ%2BJsotjeNslwGsd7XN3RIT4S9gnK69MwG1EAnuYM2vdfyNTiH%2BXFzJaKxMvv7o7ZlmQMdHMEkQYpiTSwRwxoZzPXSKkCxf2nJigd5IKhT9Q1fPiy%2F77MZMgla1pahtvyGwPNsGyuz2VzbhsInQrHU3b7JCUTvZWqCJGhKidVJYaO1dWAsXlvy7X3gEjZvKPyK21S3Y1lGMYhsa0&X-Amz-Signature=15750a394030a116a9b7753dda4c1e9bfd2a85d1a7e92ef493d3f4ea370296b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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