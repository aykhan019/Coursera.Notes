

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=7c469bb5f7e60e14ab9172f2c7b0bd0100c95afa16803d4f5a06229cb8ef80aa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=febdfef5f48def7ebc7890574f5700866e76ef5b7563e21a2221868250a636af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=da59eb6ec07812898c83e4ada201b8c634b18a4c41c252df5e6c22882d0af908&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=43489873ee5df57c43757c3e110d174ed4543be9c7c953f5d3a97560e513a1ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=19ee3893982eea340f2b7db86c39e6abda3f46be6e69cdd112a92521416e0eab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=a29c5617182c21bb879b0f0b35ee1883202006951d35b7a4639344b0885c901f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=5f5c65988268f2ad363d1c4fe123775676740ab3ba156fb2325ec90b879f8019&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=9d099189db659a7748a69539c35167eb39e184f77513d7117eb15f144c9ef0c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=7226a553278875f4f8b1eb6ddf599dd02883d734ca9f41234ee77fc092fac3c6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QVGCRIW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPPrjPin190Gs%2BdhxsX7JCcgQ10pOXkJ3SD6Q1uFJ2ZAiEAt6GoajgoFDk5pGzDKG2h0IjBjr0XhuUpQ0Tjyi%2FLVBwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzepYcLHsclCNaWBSrcA6R2VUXLKLh%2FSxaAmvuiQ2mfUSj%2Fj%2FgX4Tt%2FE7s9P3Yr8GDr5aidYJlgrhKjMjQ%2FpJomBhlx88RJYFRDkeNj7TY9ta3%2Fb3cSUKAC7NbihEfcyLFeSZOUDxa1fOOwyFrEx49ZRHwf0VnmhS%2Fx4tTFHlhedd%2Foi%2Byb8svnb0fDFYRkS02A5cFOauDzMUA%2FYGzq5gvr3gjEZvtdPuivf4vzxmlYFzVEoENJECauzQh0Mwfvr4iKtuFVq4RTLoA03m7y%2FFZ36wKXv0III8R4DJ8peccMVVL%2BNt3BjrAdnyOJUFSpvwZu30%2B5iK661LXdNNTlLjKhpVKfp%2BUTVitET%2FoHRMc6Oe5aWOvBUQ1%2F2pB9kRmgh3ymnyPumQbOmwMaHAlnxlSv9xn6MhwoML%2BbrUV%2FyLkD%2FJeurwdlTgid0pptGePED%2BV%2Bm8g67a3Ep2ZudghD4T21UwnZMh0189vvAU7aCjGEaDrrspR0uX0jczEVrwlxEXTEbTIlOOsMzzXPS8SnRJSZKSiLmHTaWFymEuWpvZM1a5PrKnEn9L2Bg%2F2gDMfGcxA73XWf%2FyEeXsECtIQuShQ5INB2%2Bpf9YqotSYkhBOIUStkh7fMfQctcI3IPg8HdaPwpDavb53vms%2B%2BXMNDQ8LwGOqUBsI01eoyh%2Bqv8ihve81GVLX1Ww4Hih06JT4HIf2DGMh7Qe5VTV5VtNb4NDk5cVpF6VY3C%2F3Tw9En4h3wV6Nx70SGpmdFoL6P9CmSLI1B0Bc3LxNR1yEVoezIEYNuKsUK73vUTfbeP2RtrJk%2FzHjmArjOB0xTPKgXb2GHr%2BhBTTuPFgOtAYKvugdQ9bJjvoDUMKOF0wCvXKtqVfo%2BWMjc1HzOdEXCk&X-Amz-Signature=69c1385542ad4918ef49078939d5cfece68b56069b030f599f908b3e5b4949ce&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QVGCRIW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPPrjPin190Gs%2BdhxsX7JCcgQ10pOXkJ3SD6Q1uFJ2ZAiEAt6GoajgoFDk5pGzDKG2h0IjBjr0XhuUpQ0Tjyi%2FLVBwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzepYcLHsclCNaWBSrcA6R2VUXLKLh%2FSxaAmvuiQ2mfUSj%2Fj%2FgX4Tt%2FE7s9P3Yr8GDr5aidYJlgrhKjMjQ%2FpJomBhlx88RJYFRDkeNj7TY9ta3%2Fb3cSUKAC7NbihEfcyLFeSZOUDxa1fOOwyFrEx49ZRHwf0VnmhS%2Fx4tTFHlhedd%2Foi%2Byb8svnb0fDFYRkS02A5cFOauDzMUA%2FYGzq5gvr3gjEZvtdPuivf4vzxmlYFzVEoENJECauzQh0Mwfvr4iKtuFVq4RTLoA03m7y%2FFZ36wKXv0III8R4DJ8peccMVVL%2BNt3BjrAdnyOJUFSpvwZu30%2B5iK661LXdNNTlLjKhpVKfp%2BUTVitET%2FoHRMc6Oe5aWOvBUQ1%2F2pB9kRmgh3ymnyPumQbOmwMaHAlnxlSv9xn6MhwoML%2BbrUV%2FyLkD%2FJeurwdlTgid0pptGePED%2BV%2Bm8g67a3Ep2ZudghD4T21UwnZMh0189vvAU7aCjGEaDrrspR0uX0jczEVrwlxEXTEbTIlOOsMzzXPS8SnRJSZKSiLmHTaWFymEuWpvZM1a5PrKnEn9L2Bg%2F2gDMfGcxA73XWf%2FyEeXsECtIQuShQ5INB2%2Bpf9YqotSYkhBOIUStkh7fMfQctcI3IPg8HdaPwpDavb53vms%2B%2BXMNDQ8LwGOqUBsI01eoyh%2Bqv8ihve81GVLX1Ww4Hih06JT4HIf2DGMh7Qe5VTV5VtNb4NDk5cVpF6VY3C%2F3Tw9En4h3wV6Nx70SGpmdFoL6P9CmSLI1B0Bc3LxNR1yEVoezIEYNuKsUK73vUTfbeP2RtrJk%2FzHjmArjOB0xTPKgXb2GHr%2BhBTTuPFgOtAYKvugdQ9bJjvoDUMKOF0wCvXKtqVfo%2BWMjc1HzOdEXCk&X-Amz-Signature=7bd7ff3b47fd2203c499e27658fbe880af686249975a6aa04c8922aed6762c35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QVGCRIW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPPrjPin190Gs%2BdhxsX7JCcgQ10pOXkJ3SD6Q1uFJ2ZAiEAt6GoajgoFDk5pGzDKG2h0IjBjr0XhuUpQ0Tjyi%2FLVBwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzepYcLHsclCNaWBSrcA6R2VUXLKLh%2FSxaAmvuiQ2mfUSj%2Fj%2FgX4Tt%2FE7s9P3Yr8GDr5aidYJlgrhKjMjQ%2FpJomBhlx88RJYFRDkeNj7TY9ta3%2Fb3cSUKAC7NbihEfcyLFeSZOUDxa1fOOwyFrEx49ZRHwf0VnmhS%2Fx4tTFHlhedd%2Foi%2Byb8svnb0fDFYRkS02A5cFOauDzMUA%2FYGzq5gvr3gjEZvtdPuivf4vzxmlYFzVEoENJECauzQh0Mwfvr4iKtuFVq4RTLoA03m7y%2FFZ36wKXv0III8R4DJ8peccMVVL%2BNt3BjrAdnyOJUFSpvwZu30%2B5iK661LXdNNTlLjKhpVKfp%2BUTVitET%2FoHRMc6Oe5aWOvBUQ1%2F2pB9kRmgh3ymnyPumQbOmwMaHAlnxlSv9xn6MhwoML%2BbrUV%2FyLkD%2FJeurwdlTgid0pptGePED%2BV%2Bm8g67a3Ep2ZudghD4T21UwnZMh0189vvAU7aCjGEaDrrspR0uX0jczEVrwlxEXTEbTIlOOsMzzXPS8SnRJSZKSiLmHTaWFymEuWpvZM1a5PrKnEn9L2Bg%2F2gDMfGcxA73XWf%2FyEeXsECtIQuShQ5INB2%2Bpf9YqotSYkhBOIUStkh7fMfQctcI3IPg8HdaPwpDavb53vms%2B%2BXMNDQ8LwGOqUBsI01eoyh%2Bqv8ihve81GVLX1Ww4Hih06JT4HIf2DGMh7Qe5VTV5VtNb4NDk5cVpF6VY3C%2F3Tw9En4h3wV6Nx70SGpmdFoL6P9CmSLI1B0Bc3LxNR1yEVoezIEYNuKsUK73vUTfbeP2RtrJk%2FzHjmArjOB0xTPKgXb2GHr%2BhBTTuPFgOtAYKvugdQ9bJjvoDUMKOF0wCvXKtqVfo%2BWMjc1HzOdEXCk&X-Amz-Signature=6e2278db39fcb84bc7e978748c93943a83d78fa7cab523625fb5b9777ad73071&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=bbdc1d83d28a8d87ae39fe6925b6b191f7b0ff941b7d05129f3f237ca8a0c5c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=3ca5b67935f2c54254b08fde9c1168d1055a6c8a9dd9cad1176c04bff9095a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=092582db871421960143f271a722ca972816ece6f728c772020049917afabf45&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=c9cec484cecd4a1d73031ff6c4229e319d4347d6c8a9aaae7222b5e249618867&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=e4d497e00fdbec3b5c4c4717b56f6e3e139575ea9e4144ba725fbacb80cc702b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=6b2887dc3914345e173b8c7b415ce573cd8fc6d472adf555a1dd994492a3fe00&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UL2VDLU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLnlmG3sdz5XKrpHtynC%2FTMjtNVfZRdnYYn6AsDKwKXgIhAPU5oV2e6%2BU66dVocNe7jgLaAgg0QIn53kxKK0JBYFcJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsgVe4f68we17wPFUq3AOnjsDO9Pc%2BAGIYZoBh4Gm%2BQBmKVOutzsri53TH7k%2BcugZJtHw8vVW2HN1npM2qYec1lpe1bqtEWxOOSfIiFQ%2BsrbR0CRxXplPIib%2Bs4GJUUDErnlOW4FNlS1%2ByfNUJmqhCE3YPsjkPUU4ZdSCu49lg%2FW%2FpP98Z3aFcHVkKSQjVlfE%2B9MI2xMBS3%2BTy4SFFQn1yj9wxONCLmDjjsLfORQcWHWM1coiVcB6dipGCfgotNM5bAYP0cBIOItuYT8dJclr%2FKyvAWgAMEM6wZJKIgmpCvZNMGrqcrYVcxWo0WIaqlFgOi%2FOOanOJfn4Xm3Xv42ujpCK4lB8%2BC%2FEaZHh9ZucPzS0%2BkWibpclH7cAycOJjz9twvQ9fw7KYp2l8GtfNzNmt3tQayM%2FOsVpFsuuxj4vU8mDKlk9obolabOG1hgfyJBQOwa%2F%2BUsBtNVsppHxV8tPRmG3ejmM1be%2BtVwF3nnXy41W4Uz5iFPYqXTwMXTwmxiGc6DPVktaFPsVEAv0a4FT2oEbj7i22SANrzZfceufQ2hc9RknISA4SKaVrfAsT5scZKYgiIdmgd8J0VX82%2BkGxFX2FI0alhMA4DzJt6T1qw9Vl%2BN3P9m%2FhtjwDF89XaA1XzoHmiAC3s%2B%2B3ejDS0PC8BjqkAW49O%2F%2FvRrtLFWnnbjCtCuWmv5xhIEJxnp2yb6E6X%2BEaZ%2BQBEZPCYJs75BLgmQ0L2FCS%2BxHE%2BiLcXgnWoBvctDLHdNPV3V9w6egdLk%2BrAq57XB%2BLA8c%2B8cFMxVU1jCPVKZGDeeuJ5ee9a8ndoz2a5dKK94g%2F0DWl8HxyEmDUz8a%2F630mCf%2F%2BpeMmByoC2C35nUsmhvQSCHbGPC%2B%2B0W%2BqbDmGv2tz&X-Amz-Signature=638a63a63f1a2d46c73e5509a7d1edebc5a9e64f97097114ec1edf9e9f7349bc&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UL2VDLU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLnlmG3sdz5XKrpHtynC%2FTMjtNVfZRdnYYn6AsDKwKXgIhAPU5oV2e6%2BU66dVocNe7jgLaAgg0QIn53kxKK0JBYFcJKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsgVe4f68we17wPFUq3AOnjsDO9Pc%2BAGIYZoBh4Gm%2BQBmKVOutzsri53TH7k%2BcugZJtHw8vVW2HN1npM2qYec1lpe1bqtEWxOOSfIiFQ%2BsrbR0CRxXplPIib%2Bs4GJUUDErnlOW4FNlS1%2ByfNUJmqhCE3YPsjkPUU4ZdSCu49lg%2FW%2FpP98Z3aFcHVkKSQjVlfE%2B9MI2xMBS3%2BTy4SFFQn1yj9wxONCLmDjjsLfORQcWHWM1coiVcB6dipGCfgotNM5bAYP0cBIOItuYT8dJclr%2FKyvAWgAMEM6wZJKIgmpCvZNMGrqcrYVcxWo0WIaqlFgOi%2FOOanOJfn4Xm3Xv42ujpCK4lB8%2BC%2FEaZHh9ZucPzS0%2BkWibpclH7cAycOJjz9twvQ9fw7KYp2l8GtfNzNmt3tQayM%2FOsVpFsuuxj4vU8mDKlk9obolabOG1hgfyJBQOwa%2F%2BUsBtNVsppHxV8tPRmG3ejmM1be%2BtVwF3nnXy41W4Uz5iFPYqXTwMXTwmxiGc6DPVktaFPsVEAv0a4FT2oEbj7i22SANrzZfceufQ2hc9RknISA4SKaVrfAsT5scZKYgiIdmgd8J0VX82%2BkGxFX2FI0alhMA4DzJt6T1qw9Vl%2BN3P9m%2FhtjwDF89XaA1XzoHmiAC3s%2B%2B3ejDS0PC8BjqkAW49O%2F%2FvRrtLFWnnbjCtCuWmv5xhIEJxnp2yb6E6X%2BEaZ%2BQBEZPCYJs75BLgmQ0L2FCS%2BxHE%2BiLcXgnWoBvctDLHdNPV3V9w6egdLk%2BrAq57XB%2BLA8c%2B8cFMxVU1jCPVKZGDeeuJ5ee9a8ndoz2a5dKK94g%2F0DWl8HxyEmDUz8a%2F630mCf%2F%2BpeMmByoC2C35nUsmhvQSCHbGPC%2B%2B0W%2BqbDmGv2tz&X-Amz-Signature=946b967e04ea41368d35e49d6e1588801c586626dc373e8ed864f87d51182c57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5EWNAR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2BQ3oYP%2BjRvyKdfKJIwXQatA36w3chfUEavHA6vzdnhAiEAooP4VMnRKg5mnQd7gacsZSzEJF1QYmZ7QEHV1lbiFrgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFzUwWYzFdrWa9G0lircAwaFNfu2WFkJXnhSayhr1qdXdsalWLLUaBElhbuUOxsdsdY2m7wfl7fkXodC4gJilWIciYb6TksdcFQqgm%2BttJHMN%2BXnYYDho6gMHrbJBxOFEJmsLtYcBj0Z8C0eDw1NumMGQF6cPp52i%2BRqNaNUi9mrST%2Bfan0QFeZfZluipbjod8%2B1JZN6eJ2Fbv%2FNg2axyOyVChbFfVMJyMRTgL%2FQZKSg288j4f8nGQHqmbqdErqEk9HvRE0zHiGeRwYDV7QnCzZZafWjswu5jqkddZhsTeDxrTfC1idvPt7Ctufepe8ReFAJcEhrIGol6Nqf85gwYI%2BmX10lldz7UFa%2Fs9VTyGn0mH5lIXDj0liqI2AKrUqClhgUS%2BfFKHVJPth4r9i6rbNZZaXLN2mYvo%2FFgVB9Sx%2FExvnShEjEdhc%2B8c8OltleKOXh8C9zHHUAsTmKiWXY%2BJFq%2BxPxK%2BrqGGjIXWvozOZ0M5aBNfQ9Okk73KITPrKf6v2m5fN2jDsqeLGw2%2BEIzgucUTPrWHnggfzDvhzG04z6I78hmOZXiHK7RzuXWycP8KPlkeV8ydYdd8iNDiASGiYyt00clLD8uAJkob14IbxVChqzPugFkQQQLd02nadJMDex4Y%2Fl5w0nOtQNMMnQ8LwGOqUBK5%2FObH22H942sVt5P4x4FSOaRVPR6oEv7nHZcAKoCBlkHML0huRo22JK%2BSZtuyMYwpKfTU8TLV6QvsdCshg8Cmr8fwr2BYJxjWLP%2BvFr5ZBAY0JshmONtmxvzghvpTRF5Cbq3d7ZLBY693JodHvTbxM5rGI3mGE5x97Zznfatw3xfVJdClC%2BIxR0C0aroBKp%2FGl%2FCnGR5Dh1z1Au4QJU8UlX%2Fgum&X-Amz-Signature=c11853bcefd254f906c7495e0f9acdae5597f13a0e271e7b7d2cff07f4fb35f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647KJWZRY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyFGd7eyK5YMzED9a2x6OCXJqoO6Bavc%2BSjM1jn4%2FSAiEAm2RGiCTxIvQnRDau9zT3zyjU4RHw2IDrOCAgrOHxvH4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi6fc2bil1SlEin7CrcA%2FiNJRuJCeqK7wJmU1COjeT%2BlC2AW7%2Bk1l8UJOGY4wVed32yCPmOGmmBFP%2Fd5S9lgsmmpSOTV0EGNwK5jKsWmXIwWu0YGNdhV1moIJOS3O9xzcvxjd4155661XpFlA9saNR8qTFHE8KQbjpxtRJLR5Jyd%2Fjg8ZB%2BTp0yoDpKKXuK74theg5d86Aie7MuOdnqpaLmfbPEFfVWcNAaOiJXK70SVEq8ewDMPH9L%2FVAkcghaw9BVqMQOj7nKdDBpVvc%2BQqxUb07%2BwGbQX4NpxEPrWoKym%2FH6%2FoAjYrRnXSbnSkD02aBZNJF%2FNa0Kov%2FlQHrp1Ol3hxSVVvmtyYEM78dWYY%2Fvuy13mjrvr030YIztwC%2Bff36a46iglKk%2F7ZtHK1JenHDdInrmtM35rT5w23W1Ixu6UL1iPcnrz8T9nrdpMvYKt3uq2w0r63j058RuNmVfhdu985PUwSQA%2BTuUq064PkuC%2BatpJaiIvANhwrr%2FUayn%2BwBNbOvypCmxYeB4ea58o1PmAaFzPYEE69JULatD2zFgsmE8erG4K4GeiFo9l8I3ChdtSAYR8wzPjX4PrccCWhdtHKa2a%2FOQ0SVtFUOI67yzLtGN19ElsC7LTfZhMPaWqm6who6ZLru9HK77MLjQ8LwGOqUB1j83CfG%2FG%2FpWRJbrxyuikgxvReFHTOXPRTbs8VCZig39WtqDZXzM1OwsV2RwtTrl4j1rKYwBcKyiWEa%2F1RXK3dJUcdEso7mYAnK47Ai%2FWvDSn6%2Bz5U89DAnedfqQJJ7t8xIkbS4zSON%2FFua1xmgeXm32E12YNAdxjEOt20D4yGJ91L%2BOuY%2F4bQKdWMluMMdfG9UC2tZz9zZXWsAJFzqNR5mQKCty&X-Amz-Signature=c51309d05e04c91749218cd7f3259e932239efbd11b71519ef8c41a8f0e6e040&X-Amz-SignedHeaders=host&x-id=GetObject)
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