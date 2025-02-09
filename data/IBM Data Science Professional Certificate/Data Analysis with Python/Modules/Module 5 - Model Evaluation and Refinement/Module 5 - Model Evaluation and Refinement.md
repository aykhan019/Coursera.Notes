

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=eab0e05a9b8c3492e80dfc5c96ef2bb54ea81868a78140e26a8327d1bbd6da62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=3ccf74e5a2acde21c59dbe9409f5db4620a51084fa2d30c51c8127a6e8b08a96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=205cfeb0a591e96ade931ea03cacfde67f7aba45fc7fc4496efb5e68e3d1a31c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=624b4f0f2c8bc6dcd2ba83c1178cdefb4d59b04263a7d9a5b22f5e9d1d47da66&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=08bbe65dbd40f28e2703cef7e6d5a385494fe53736dd9e5b41aaa4219f823323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=4ef15a393c9845674d2a44703e7ae1787714938cc6898178c7f7e990607ea9c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=ff82f5b543201714dbe02cf0f92fac1b367ea0a339668062dbc410f974902c62&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=396d74e1df3efabad97dd4a86ab90fb621600bae3473a44d790c28f3c498dee2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=513fcdefb1306b6bb681cc76aa50f9abea47d634823fae5483739e0dc6c9e817&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBHHCXS%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS5wPmIO1BBDoHkpyiZTHNJojsYuPYyCr1Ofhro8cYTwIgKkbnLw%2Ft9iJfMfoQXdBX3VZ617TsPgtMwQUAD4Jp7uUqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFEKiUZ6Lhp%2FIZAeCrcA1EG%2BTDd1i%2BOcft5d9QZfHPPMQw1taUZjQd7nGdGhmnZ4tXGlwC%2F8wJmqcce6Oq%2F%2Fj2K2Af1JmIV7X6efW%2F4IH0lMfThJp0Kgwl9%2BAxxlNeEOLi8BltsxGdolBuUfUpeBdZNQTC0r%2BlE0qMpNLc2G07r8MuJNhN3%2F4X36uN70Cw4tLagMQh1aFMDsWWZFKoUUIArbVzLw0LQ9fmxlRNfj4nel2Cl3uWUKEmJ4jgpqU9LmwyeNTJsL3AejNo%2F19mTUFUZxCqiYzcj5eOeOAg1x%2BxZB1dKlrsac3ihDX2hXxF9Bjst3rQsHerGvipvjHv0vqtN3ZrIdXbnh7q4oNo1MIr9z6OPUQsX7KJJOhSVqVO4LV6qf9%2BX7hBfUeaeUhpTEBNFvc5oipE2njBBJeaT8ZP7plUnCosYOir6VJo9f28khMKxIhGW8yaMs99tEAPzHaLn3OCx1fZl%2FbEXqnd4FgME%2FcuKNl%2Biw%2BRPHLoOfPyuoMuj%2BG4yxEZU4g88jsJqPy7Zu9K0Tq25vDFIgI9NYqWwN4WyoA8UYWgCjbtzuzGF0z7KEUAJbKgVIJwJ1yec91WtAtaW%2FzIIGXJG3yWqHVqPcxPp2ZiUDg16gy%2BBx350QlaRVk9YqQm%2BpCGPML%2FWn70GOqUBxVFw8eGMtCYlcgtGsn4JmhsZ54KV%2FsqjCsOjYPPEv44KGi3sx%2Ffh4ecwnajxdjyMSljuiYVlBjp9NW3MfyyHK4oqbbxz3rAfA%2Br7y3jVHlQDiegeshVWnfdYcD4b65%2BGdMLN3ytpKrPdp4I6FExKeo1SL10ElxP9gKs8cNdtVR6u%2Bx4by1LafzaFJYhbrywBNdHSFf8oPP0kIhqttQIs0P4%2B7slV&X-Amz-Signature=59af815443bd94f86b291fb7a66bbd150a28d002b4d257ae0682aec7849a14b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBHHCXS%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS5wPmIO1BBDoHkpyiZTHNJojsYuPYyCr1Ofhro8cYTwIgKkbnLw%2Ft9iJfMfoQXdBX3VZ617TsPgtMwQUAD4Jp7uUqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFEKiUZ6Lhp%2FIZAeCrcA1EG%2BTDd1i%2BOcft5d9QZfHPPMQw1taUZjQd7nGdGhmnZ4tXGlwC%2F8wJmqcce6Oq%2F%2Fj2K2Af1JmIV7X6efW%2F4IH0lMfThJp0Kgwl9%2BAxxlNeEOLi8BltsxGdolBuUfUpeBdZNQTC0r%2BlE0qMpNLc2G07r8MuJNhN3%2F4X36uN70Cw4tLagMQh1aFMDsWWZFKoUUIArbVzLw0LQ9fmxlRNfj4nel2Cl3uWUKEmJ4jgpqU9LmwyeNTJsL3AejNo%2F19mTUFUZxCqiYzcj5eOeOAg1x%2BxZB1dKlrsac3ihDX2hXxF9Bjst3rQsHerGvipvjHv0vqtN3ZrIdXbnh7q4oNo1MIr9z6OPUQsX7KJJOhSVqVO4LV6qf9%2BX7hBfUeaeUhpTEBNFvc5oipE2njBBJeaT8ZP7plUnCosYOir6VJo9f28khMKxIhGW8yaMs99tEAPzHaLn3OCx1fZl%2FbEXqnd4FgME%2FcuKNl%2Biw%2BRPHLoOfPyuoMuj%2BG4yxEZU4g88jsJqPy7Zu9K0Tq25vDFIgI9NYqWwN4WyoA8UYWgCjbtzuzGF0z7KEUAJbKgVIJwJ1yec91WtAtaW%2FzIIGXJG3yWqHVqPcxPp2ZiUDg16gy%2BBx350QlaRVk9YqQm%2BpCGPML%2FWn70GOqUBxVFw8eGMtCYlcgtGsn4JmhsZ54KV%2FsqjCsOjYPPEv44KGi3sx%2Ffh4ecwnajxdjyMSljuiYVlBjp9NW3MfyyHK4oqbbxz3rAfA%2Br7y3jVHlQDiegeshVWnfdYcD4b65%2BGdMLN3ytpKrPdp4I6FExKeo1SL10ElxP9gKs8cNdtVR6u%2Bx4by1LafzaFJYhbrywBNdHSFf8oPP0kIhqttQIs0P4%2B7slV&X-Amz-Signature=9e9e7ed340086a8191984dbdfd8748f9780ccdaedf4ec7ca6674ee2439b07381&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBHHCXS%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS5wPmIO1BBDoHkpyiZTHNJojsYuPYyCr1Ofhro8cYTwIgKkbnLw%2Ft9iJfMfoQXdBX3VZ617TsPgtMwQUAD4Jp7uUqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFEKiUZ6Lhp%2FIZAeCrcA1EG%2BTDd1i%2BOcft5d9QZfHPPMQw1taUZjQd7nGdGhmnZ4tXGlwC%2F8wJmqcce6Oq%2F%2Fj2K2Af1JmIV7X6efW%2F4IH0lMfThJp0Kgwl9%2BAxxlNeEOLi8BltsxGdolBuUfUpeBdZNQTC0r%2BlE0qMpNLc2G07r8MuJNhN3%2F4X36uN70Cw4tLagMQh1aFMDsWWZFKoUUIArbVzLw0LQ9fmxlRNfj4nel2Cl3uWUKEmJ4jgpqU9LmwyeNTJsL3AejNo%2F19mTUFUZxCqiYzcj5eOeOAg1x%2BxZB1dKlrsac3ihDX2hXxF9Bjst3rQsHerGvipvjHv0vqtN3ZrIdXbnh7q4oNo1MIr9z6OPUQsX7KJJOhSVqVO4LV6qf9%2BX7hBfUeaeUhpTEBNFvc5oipE2njBBJeaT8ZP7plUnCosYOir6VJo9f28khMKxIhGW8yaMs99tEAPzHaLn3OCx1fZl%2FbEXqnd4FgME%2FcuKNl%2Biw%2BRPHLoOfPyuoMuj%2BG4yxEZU4g88jsJqPy7Zu9K0Tq25vDFIgI9NYqWwN4WyoA8UYWgCjbtzuzGF0z7KEUAJbKgVIJwJ1yec91WtAtaW%2FzIIGXJG3yWqHVqPcxPp2ZiUDg16gy%2BBx350QlaRVk9YqQm%2BpCGPML%2FWn70GOqUBxVFw8eGMtCYlcgtGsn4JmhsZ54KV%2FsqjCsOjYPPEv44KGi3sx%2Ffh4ecwnajxdjyMSljuiYVlBjp9NW3MfyyHK4oqbbxz3rAfA%2Br7y3jVHlQDiegeshVWnfdYcD4b65%2BGdMLN3ytpKrPdp4I6FExKeo1SL10ElxP9gKs8cNdtVR6u%2Bx4by1LafzaFJYhbrywBNdHSFf8oPP0kIhqttQIs0P4%2B7slV&X-Amz-Signature=325a1077b653e25ca493f8adb0215d9f345e0c964fdee2ee6e4fdad8f8641388&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=5875da496377cd9f98c1d72022120cea91e0a605ec268cc5b2b47a693ab248e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=82afe9b8e20b0982600d3c520d5aef5fc88ab447b0a01dc165ad19d094bd61ee&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=1d5e234c8bff4078c86f7beec6feaed645a81fde9237e37f2a2e5fb624a722ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=5aca20ff542d192f783e1faf36a0c673f2a5cbb2eed29fa6aa59a549aa976625&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=7c04ee2af51a11b29f4d2538efbe0f03706149d76948b5f399d5c07f114d5b46&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAKPKEX7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4CQdqezzWRhhwrYg4uce%2FEvyoSLJg0BIZmeaz8tVr%2BgIhAKM%2BaoHdj4S8mF7cRJBCEaAvJZTY2X98zZK6L5owviR4KogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWhY2sI3FdIyJRIYoq3ANgoiDvmkNmIwc1QzjoZadVkE5hZ3vrau11qMq%2BNqkREJ%2F7nvyN07KaxqiHvGjplcS13%2BDiuw04n%2FCUQOsaM3IkAaYS4YYkUuN5XS9rJtswmjDYofPp3Vv60YdFNH%2Bh9u9KStRb2LrzLT2g7huHpUYP7yIi3Pq0M5WDbioOnTRK5IAtoMdstb16%2FPOSevqHAMS4LIsk%2FIH3sbw3KHV0KbA9X5J%2FCKcBs7TIRRa1mK%2BqmJ5g9PrbXWoVmgOQsCa7eBuIUXM1kN6dim3DQTwJyAIdJ1NZTapy5%2BL2jOjAskChCIRm1uSp7hwtDl3ki4QU9LT2191c9ZfGQw4paVCHFBbojtTpqcQgnx24%2BfyTVnjD9VAjO84xexHntTegmuHLj9Uya1%2FnON5qPoZm%2BbbsVcHRA8TnA0BU2z6T%2FVWtZTjkqlYeXMQiRqeU9SNGXysI0EQtkZ48aHHzn%2FKLGag%2B2n5qYGmQ3LFB8olJXr8SDnRxttzO%2B5plLoWSLFlaVX2mVYO0zl55QyRZLBqyGmLvT%2F7Z9MaCHf2UJNTq3izQS2TVvoYq6uaS6R50vr4VN3Pl%2FsuGZK%2Fxuh37BhI1C5MtbDVYnO6AxCVAtaFZRz5TXlmZoQ4%2FH8%2FY2t4cIlAQnzDO1p%2B9BjqkAeBkQ1VLBxmrPFyVUaKZoNTwGrIcU2Pknio6MKRmGCxX35UNnCRWYmAoBDUfCrb%2Fb9c23Gd5NLjdqoRBRA%2BmriUyV2dxXo10%2FtuKUC4sRsAonSC%2FAhLSAnXEmHGgU2fvTStpGIZvqzCZpu5jbRH%2FrH3pPg6rEU7woaAQNbtaQ1B%2FX3HUr3FhBu40hLhE7X9FuYu2L%2Fr67CpBXhS85JDTqqH2MZtJ&X-Amz-Signature=d3ff6b894f9e054749333e67f1a649d59cdb9be52228137f106613976e441335&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FB5WD7B%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRP9AGaoW5R5KyVKnf0%2BgVA3oPoODNHpsuxg7k6JRJmAIgAeyWV04Nq4S%2Bj%2BkBOpkiHOHGIXR8WpF%2BUlyZAIMXXEwqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrERSBVMOCQaiPc8CrcA3CnxG9NY38EnUE0ik2eWMptbES9CNPbH5nZ8493yKgM23ruzzV3eOLJWaeKFDhwxqpPQAwtGtlG9d5Fl8gSzgp9IypoBTCtWMTskLYX7Q%2BGp4tk13RDbXdPhm%2Feuf%2FKVY9ZaVJ3lSz%2Fzz3VcbMNH8b8q7usTMsblz%2B0U0MrMcg2DVnZmZYxySBLahDb8onvM%2FN%2BP6WMkGZEOo1gTYbwoXlCUX%2Fe0rJvfvsivzUHQo4iacleLpj8mleLMUVziesS3jJlQiti5HUn1fl4vi1DhBmcuWthzHST5Y9ps7Z5WSF6d2ZeHJNZKUE8EkD74YCG0LWSYUkhsnyIXeVRdk6Wbg90uKF7V1gKQLLcFs2voMHg8Kn%2B6YJsDd5qeBYzYpxNDmrtXQupNXUQVavxVnNJO7I3iKUxjhbI0N%2F5WgWM47X8MsXjlyhjjt%2FOHjcK38%2BOMk5lxse%2FVJtv8Pc4t9bVQlkjqH0QGmRxxvTScZKl1IVj2yf3lVE%2BRP87Hd5IDpMC8B7NFHontM647lXPemc0Wc7yupGMWZwMFmhNjrfk7QPbhJB82Fa0q9YgCEpZYg2bpj9sI46mlEGSIYJteKK0dgk2OCrkN9LSHwwOlDoFU7x%2F3FXucMys9FzrkhReMITXn70GOqUBiIQ5AGFJZaG1z%2FGWEbHimFhHpfOHbHojkssxsRJxb6VQD7d1ymV4zHng7UJn3V26I%2BkDBu7vb%2FtyAwHOwZd0hImfqlr5OmNE2wAUsrpN4MTjYA5l3sURR6yPUt4mWVsMyZqJy2wVA1ndNZpm7PqDdxY3XJnMqiyDVZlVfXb3nSHLblNRCygXIPwo0yknVr6I4cyTiLJ9crTJcm4JqSPAJbUUVCph&X-Amz-Signature=73de1d6f2b42db22eee6df7bec48f88b52f248ee2bc354c7c3a277e2ee30c4fd&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FB5WD7B%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRP9AGaoW5R5KyVKnf0%2BgVA3oPoODNHpsuxg7k6JRJmAIgAeyWV04Nq4S%2Bj%2BkBOpkiHOHGIXR8WpF%2BUlyZAIMXXEwqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrERSBVMOCQaiPc8CrcA3CnxG9NY38EnUE0ik2eWMptbES9CNPbH5nZ8493yKgM23ruzzV3eOLJWaeKFDhwxqpPQAwtGtlG9d5Fl8gSzgp9IypoBTCtWMTskLYX7Q%2BGp4tk13RDbXdPhm%2Feuf%2FKVY9ZaVJ3lSz%2Fzz3VcbMNH8b8q7usTMsblz%2B0U0MrMcg2DVnZmZYxySBLahDb8onvM%2FN%2BP6WMkGZEOo1gTYbwoXlCUX%2Fe0rJvfvsivzUHQo4iacleLpj8mleLMUVziesS3jJlQiti5HUn1fl4vi1DhBmcuWthzHST5Y9ps7Z5WSF6d2ZeHJNZKUE8EkD74YCG0LWSYUkhsnyIXeVRdk6Wbg90uKF7V1gKQLLcFs2voMHg8Kn%2B6YJsDd5qeBYzYpxNDmrtXQupNXUQVavxVnNJO7I3iKUxjhbI0N%2F5WgWM47X8MsXjlyhjjt%2FOHjcK38%2BOMk5lxse%2FVJtv8Pc4t9bVQlkjqH0QGmRxxvTScZKl1IVj2yf3lVE%2BRP87Hd5IDpMC8B7NFHontM647lXPemc0Wc7yupGMWZwMFmhNjrfk7QPbhJB82Fa0q9YgCEpZYg2bpj9sI46mlEGSIYJteKK0dgk2OCrkN9LSHwwOlDoFU7x%2F3FXucMys9FzrkhReMITXn70GOqUBiIQ5AGFJZaG1z%2FGWEbHimFhHpfOHbHojkssxsRJxb6VQD7d1ymV4zHng7UJn3V26I%2BkDBu7vb%2FtyAwHOwZd0hImfqlr5OmNE2wAUsrpN4MTjYA5l3sURR6yPUt4mWVsMyZqJy2wVA1ndNZpm7PqDdxY3XJnMqiyDVZlVfXb3nSHLblNRCygXIPwo0yknVr6I4cyTiLJ9crTJcm4JqSPAJbUUVCph&X-Amz-Signature=70db96423debb39a2ca42c76c87279d1e84e4d7d1d66defa7078d35714f5d28d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQB7SNA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEEZzIKrU%2F8t2hTRuHJ%2F0hz84wDJfBhTJBYUtKwd6A9iAiAtqi18wgLM%2F4cdw2iVRFZtT7ipboMVsLTyVvXIMRaghiqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB6SfhuiNipCfx82vKtwDAjkVU3pc%2FkDq%2Fs2AotZzyre7VSbwCWJjNS%2BEvYTKzKmgbScDyJzkwbMBBNP1gzc08fQ8vnCXAqCwz%2B4SrPm8srIA8yNpeXy1eMNH6%2FtljB3G%2Fe3IMNDLsmFVyz1fBi7x0RTd8IdnoF0w8ppwO%2BcxGZHbQftN6oSDDs3VfRvtKyYYbXPsbx%2BAyVlZlK4kOZD51BEGevj7dax0SXwMybWrdXOvtiSE0Nwu8SuW%2BHdywSCa7YnCHC3JSzGtL%2Fadeh2ur%2BA0JLeaaO8kTDKzAgjmhcnwYLNszrCxSoyE9YyP6CQSRbYSbzfgg00oT9tkbqX6%2BE5e2VDyLp3pVZZdgmaUSYwHrjOi0qlDGOCJeXJ3fv0PIKKDmbLUoKZ%2F909OZNwYlxz4cjycaV3BSNtbI7braiYp%2BHb8PAZ98hDeYpieVbprdGEc2QtscksAjJSjVhrmzyo6KLdVSeqTqOWbP3k4gkiWDhNyPb6YMzMTHGm5e%2Fwb%2FYYDTC20RGorAov0mODgY6Rc2w006QHo0JqWfe9bNEIKp%2F3ScTCkAFgE4BImxSolYwyaKRV92S5rZbV6r23oztJpoZdtz8Ho4xIfRmh9hgz34nf83LYXknaRFrDBRegaQQxJc7ip7lbgr8Qw1dafvQY6pgEEy0W7YOqGU6iC9Krbd566s%2Bgm4dF0%2BZ%2FR8Ts1yX69pb6Ou4xi1ypRu3p9BRFZYziocQpQiu%2B6Frx8op46JWqC8DDhjTMXRDtyTLizUkT2cesj8AsPXNy0NhjUd5VvARonmlqG9%2Bho08V7U%2BlxWt2c5a0b59v%2BCJg0n%2BLM9Fr08BQYjsun4T08R9QhxlM%2BwtmQZbnA0Wk8j8EZsL84ixlHx2xYB6RQ&X-Amz-Signature=d9a6424b00f189a75fcec79a7f807d3cb1d0d8d9e0da6f7c76e40587571f04e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6XIW5Q%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnr%2BhBEVKWoddfOk9lspZ%2BBxDxBFBRHxtusmy2BtcpGAiBLuE060ObSI%2F%2BKsIuuoqvNRjfh5JhkuQiGXWY0SK6WCSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUHGrGsCF2d2LOIkOKtwDClN69ep%2BffAlHQ1QKrvZ1LwXYH6E%2BOYd40VHbnV3vOnMNw5sfaxSEibygtpjJ6%2FbtfYnLqah3ZbW8GSxyUveGqku%2BW9a6LLxh1BuY0F6%2B5n0QRGpQYEatxP4aK6QmwBxnWHEvkJmZN6akU35Bp6a37TuWtY4dtYh%2BwhpNlYRO8Kw3PBfI0nMQKbgfdrB%2BZ6IuqKlOH%2FAhB2LVZPLf86dfoIfmX4UReVWGWFgy3ZOjjGLim2AuHJ%2BfLITv82sNalAcCIsQChb6N4J117aCEY9EwdRz40f3peFRBhGd7rBm5GBR7mDMGxsH0rD9olnnRYdX73XSxWZWT6miw7IsS9JTBxLaI4SZWDg74bnjWHk6uxLfny9r1UeNCbRRXCVT4QWYPTQxH%2BrGG9xDlR8QrkdnnL%2F%2FiLvv1jx%2F0gZoRpmiuOFgtixUJPMsfcOdGBe9D04MyJSiCj7fzXQDxJ14m%2BQy1tKCZWVcbG%2BfkmJ3q%2FyESZSU9GBj%2BZxDlfkJ1wKSEu1JX6GV1Ge1pq1hR%2Fou%2FUqlM3xuWDg2d7%2FSfISakQK%2FDri98mD7AIgH0AXtBZ3C1LO%2BV81YzL27XXcV8YPWUqbdQ519%2FD5CdE%2BmlY06SPEHpB3F4rDzwEonL0ee9UwldefvQY6pgEWIN0qsb%2FWAL4xgAlTEnRc5LkigBYs3TvZ6E1exYofDoyLdmr%2BuN0bCnoyuAmkVLt5RiZ40RQk8cO9LWWJ5BHSN4Q%2BnHyX3uQS9S8FwYt9MeH3I05i1eb3bQDyNcyoqBoobYXcxmGEhIpePysQJAsn4JF4eBRjddImUgYbeu2A58QFCMJlk1%2FngBjuGJBv7pnF6orNMiS9vE8cgf18gyBP3OmA%2BraQ&X-Amz-Signature=49a4077060eab04b904255d143384678fba5112d831d776762bd74249f43a5b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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