

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=92755c96247e3392e384e9b8980526addd778db6ab1f581b0abdadd4aff6b04c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=fcb0853087f0633923f2f480b0d35f51408e2173505226dd405a3af86f7deeed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=26cf51bdaea95d310ea406ab068ee7fa1ae46972f8b513e3b624ad0f06773604&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=1de43ead7c1a9830065a40f7cdbb0ca2d10c863a5dda55408d4fdaa0cd0f8bdf&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=0e5037aa42eb34a1e46926e51ed46c36e8d8f5bafa2ff3d249dfe58ee9f313b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=951f1834d178e875c0e0cdd780d5a5a46e57bd1c5e5b1491c2cf53b360428276&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=3a12104ca557edff49ad4aaae27098dca3be768216edc20d9147a69db097b74f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=2207b2b4d06eb5d78bb4b2a823fb2bec3b8786ba8e0febbbb18e583baa442161&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=9763a0dfe8a4f9bdf510bcb03576f6e26d875c68662912c6d77b08ebd6160e80&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP5WEKSU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDRpQRKjhFzaX1nrHnC1Hlb%2F77LT4LIuLeKvQK7hoCaQwIgVX%2BX%2Fuhgdj8QzlfuRo764dr%2FdYDdYtYk1B%2FwwAk7gW4q%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDCQ9VHRMM031ESod%2BCrcA1FdQ3tF6sP5mZolhdPZ6ae5al9HzDLGCWp6PiTL2jKF1mYb1WCEoCx3DOcgFbk3jb%2BYVs2nuAH7PM5j4%2FEUOKtPcki7jF5cq7Dlr0TDjsSqE6QnwcWISq6XW7Yd8p2ndOgw10IzR5cyE0TH9%2BpXkRknkFhe5D4Y1Bglk6gJpqPDfWMR5DRyhFvCcovdr8Q2KmbRjcaygWAQa9awM2Hgny8pRh5lCmFGoTFNqvUXurzk%2Fjmpvj3Mdk2inTiCBxyTxEyi2oZoXdZRLX6OA%2B7cduFadVjcOcDc2M5RkvWGodeRuZt2j3n9kUC35R40u%2B%2BxXQIrmgpQsd5l6lZa1CAfJNKhHjcl53DHcuoSOtmqDgnnJgZQTPkdLMGSlIKTZs7Dt%2FZhOZ4BhBvuFmsYOmUTGlmKgvu0kHcwWAiWkotcAFd9NhK5q62TqsDIn3NIAoM8lhtkMtRo6YOEX%2Fj%2FfctoHO%2Fox5VjeLnMSh53P7uZnyWciZDQMrHMqRErYpaK6eK%2BXFdPllFqw5qeIPbF8Z3WEH52PdaPYlEiwFcImMpW0S07rhlNRfbKZlRIQxQEM83XGK46gzIRqoFc5u69TP%2B0CN%2FyZe1pJZlPQHeFFSlULKO2LGK40Wh04DeBQKWbMNr9lL0GOqUBdSCBc%2BjNaUI%2FCE0I11rFdNLvBHw3KVTkflQ91lzTOSQsx7oXcN9ImMVe%2BYKWOFjPEyyahT5QjoLrBmBISSo3MWTFuZd8oBYPRfFtedgrSSsksxI%2FoJ2yWdCvdpyqMSmu2%2F%2B0DoZM132%2B4IcHV4TLN7FlhRXHVMj%2F4YQ%2Fh0XZJ%2FxicsmiTNnn5wj43v8U4E6BMt3chZpsALqyZVLtqydp87RgVIc6&X-Amz-Signature=b408a790c683770c34e06cad4ca8a5f0eedf0cd814ca14fcdbcea9e365acd4ae&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP5WEKSU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDRpQRKjhFzaX1nrHnC1Hlb%2F77LT4LIuLeKvQK7hoCaQwIgVX%2BX%2Fuhgdj8QzlfuRo764dr%2FdYDdYtYk1B%2FwwAk7gW4q%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDCQ9VHRMM031ESod%2BCrcA1FdQ3tF6sP5mZolhdPZ6ae5al9HzDLGCWp6PiTL2jKF1mYb1WCEoCx3DOcgFbk3jb%2BYVs2nuAH7PM5j4%2FEUOKtPcki7jF5cq7Dlr0TDjsSqE6QnwcWISq6XW7Yd8p2ndOgw10IzR5cyE0TH9%2BpXkRknkFhe5D4Y1Bglk6gJpqPDfWMR5DRyhFvCcovdr8Q2KmbRjcaygWAQa9awM2Hgny8pRh5lCmFGoTFNqvUXurzk%2Fjmpvj3Mdk2inTiCBxyTxEyi2oZoXdZRLX6OA%2B7cduFadVjcOcDc2M5RkvWGodeRuZt2j3n9kUC35R40u%2B%2BxXQIrmgpQsd5l6lZa1CAfJNKhHjcl53DHcuoSOtmqDgnnJgZQTPkdLMGSlIKTZs7Dt%2FZhOZ4BhBvuFmsYOmUTGlmKgvu0kHcwWAiWkotcAFd9NhK5q62TqsDIn3NIAoM8lhtkMtRo6YOEX%2Fj%2FfctoHO%2Fox5VjeLnMSh53P7uZnyWciZDQMrHMqRErYpaK6eK%2BXFdPllFqw5qeIPbF8Z3WEH52PdaPYlEiwFcImMpW0S07rhlNRfbKZlRIQxQEM83XGK46gzIRqoFc5u69TP%2B0CN%2FyZe1pJZlPQHeFFSlULKO2LGK40Wh04DeBQKWbMNr9lL0GOqUBdSCBc%2BjNaUI%2FCE0I11rFdNLvBHw3KVTkflQ91lzTOSQsx7oXcN9ImMVe%2BYKWOFjPEyyahT5QjoLrBmBISSo3MWTFuZd8oBYPRfFtedgrSSsksxI%2FoJ2yWdCvdpyqMSmu2%2F%2B0DoZM132%2B4IcHV4TLN7FlhRXHVMj%2F4YQ%2Fh0XZJ%2FxicsmiTNnn5wj43v8U4E6BMt3chZpsALqyZVLtqydp87RgVIc6&X-Amz-Signature=92381c4607eed44e914d885490ae56a260e6586580df86798e331895aab9eac5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP5WEKSU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDRpQRKjhFzaX1nrHnC1Hlb%2F77LT4LIuLeKvQK7hoCaQwIgVX%2BX%2Fuhgdj8QzlfuRo764dr%2FdYDdYtYk1B%2FwwAk7gW4q%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDCQ9VHRMM031ESod%2BCrcA1FdQ3tF6sP5mZolhdPZ6ae5al9HzDLGCWp6PiTL2jKF1mYb1WCEoCx3DOcgFbk3jb%2BYVs2nuAH7PM5j4%2FEUOKtPcki7jF5cq7Dlr0TDjsSqE6QnwcWISq6XW7Yd8p2ndOgw10IzR5cyE0TH9%2BpXkRknkFhe5D4Y1Bglk6gJpqPDfWMR5DRyhFvCcovdr8Q2KmbRjcaygWAQa9awM2Hgny8pRh5lCmFGoTFNqvUXurzk%2Fjmpvj3Mdk2inTiCBxyTxEyi2oZoXdZRLX6OA%2B7cduFadVjcOcDc2M5RkvWGodeRuZt2j3n9kUC35R40u%2B%2BxXQIrmgpQsd5l6lZa1CAfJNKhHjcl53DHcuoSOtmqDgnnJgZQTPkdLMGSlIKTZs7Dt%2FZhOZ4BhBvuFmsYOmUTGlmKgvu0kHcwWAiWkotcAFd9NhK5q62TqsDIn3NIAoM8lhtkMtRo6YOEX%2Fj%2FfctoHO%2Fox5VjeLnMSh53P7uZnyWciZDQMrHMqRErYpaK6eK%2BXFdPllFqw5qeIPbF8Z3WEH52PdaPYlEiwFcImMpW0S07rhlNRfbKZlRIQxQEM83XGK46gzIRqoFc5u69TP%2B0CN%2FyZe1pJZlPQHeFFSlULKO2LGK40Wh04DeBQKWbMNr9lL0GOqUBdSCBc%2BjNaUI%2FCE0I11rFdNLvBHw3KVTkflQ91lzTOSQsx7oXcN9ImMVe%2BYKWOFjPEyyahT5QjoLrBmBISSo3MWTFuZd8oBYPRfFtedgrSSsksxI%2FoJ2yWdCvdpyqMSmu2%2F%2B0DoZM132%2B4IcHV4TLN7FlhRXHVMj%2F4YQ%2Fh0XZJ%2FxicsmiTNnn5wj43v8U4E6BMt3chZpsALqyZVLtqydp87RgVIc6&X-Amz-Signature=7675f50ef99e0f419f33c33eb9c3bebbf8412fe5e3ab1dbbc31492a5410ee5e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=e9b9fb4201b4287da987ab7fe163f86abaeb4e4bb87c5ca98531fa547736ea51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=6c0d336ffda9d4a17d3759ca9a7919b60ca4798387012daef88cf257d36b3874&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=14b307b5690171e899858794e2dc2fb0b25264e6ebe7d0427e15b61b3c480e29&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=8c22c4b1851fac03705d252227b0b633357f1f1d5bf7e600e68023ed1503f772&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=c0c4c885f35784206a856d2599672647729c96022cee79ea1a755c1cef1b956f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7GRIZ6S%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQC3SQBqMqkyJgpUyjQgUrha7z8yBXP1iCywJpm%2FVRpqpwIhAMaCNaJdD%2FYaLLnpXshyDK9y3XccDMKKPLKNr%2FGnJ%2FSGKv8DCGgQABoMNjM3NDIzMTgzODA1IgyP%2F3nQTXxgrInWvrEq3APBk9eSIqXFG%2Br36qISbghglb5NMBUuBaQcCU4MLNUZa6GZRQULyr4OCU8BA10QvXg3Ga%2FCm9MOq7vSIThXfvDNKYMOUSxylSaJ40SzKDcOISOg4DQaFQlQSvkjJm%2FFv3j%2Fx5F9vggHg%2FLc3Ovq56zMj4J47WreyH2ssFNdwX7b4KhpZkd%2FSO%2F4EmXR7EUaIYjBizem7klsRhkBAcJhr%2B2F0U6zreT3fAqnVDvgMG4FBfiilo94lO%2FCLOv7B6SjF%2BmPCQBaQEMgNQQ96rnpGlnTsbE0cfSMhDOfQtGZjizWhJSNZmTUMpztVS5z2wqEGdliIQI5chboBkZvVlyuJ2GsLv70CRebwbtUhmxtcwkutXgGi41%2F4UDbkUej6Ov3b61otxxflb4%2BtAgbsHllxUxMZnMhaxDVSpBNT%2B%2F9P1AulBFEAdNGoDQbkw4LjFs4L33GhDcMjRH9Z9p9wDeX0viO77%2BJDRJJICYVoqMe1voLOdf1FqSl62whj%2BKEqTc1Yq9pw8byQb4ZOZimtojmyzv%2BewEQH6q0qq34rnsxIIBozZgMDMi54cvf8ZB7v2TsOzahY%2B4pExVAgGQ%2BHkkAmxqh2nQOijIT8kQSCf4pnG559%2F%2FS851M62b49feDpDCl%2FpS9BjqkAWhLdyEwfsp1yJnZq%2BpH3ky6jktQ0w2i8G9bdXO7lc7GBxVXbvwgzuLtUwC7JJ2lwtKsfXjm3nrP4ltjL6hI5qK1GdeAYkRIbIo7QiTyMmFczKd2JSZIXlAY%2FFSx6iz5Xf2Oy9S%2F914%2B25f6moL0xy%2FbsPdEinuzAZGV9ahFsee8zUSD7EdpVI8gBYd5Qw9coAV2ntQfvSPq0LXgEKDaa96zmDtu&X-Amz-Signature=314f4eb3501bc3e89aaf29a33401ee7fd70020d0583dc24999c9cf85582808ea&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636TTF7U2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIBxKNPknSzWSsoMGSFn130bqwW4YzFH05i82AseFfMlsAiEApf84gvI6pRU2M6SmoR%2BTwPMw01FP23uDTA8zlhc9PDQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDPA5P0otmJTKIdo9gSrcA5j42YuqD2rUDjh17xmzRKiJ2qPEvHoY1nhBN7N68QVd5uuCmgwt4KFrCdLlPdBy7gbFE1WYJM8kYfO7hE7l9WHLickh3BGVcZAyKSj4KtpJnEDgwveC3G6PPTesO9IzZtqXSb2batvKyffEJwuUcFnCZckznZFAnQ1DonTXItoVw7a6LFy6%2B7ofyHuBw7EShJH6oTy27h0Cas5GSnrfs%2FbKBtZFoffAwIf9BbjC6lptbcgB2SDqGLhXBJH4v2h%2B%2BMdFHvrEMnTk0adrYxI9VIDWtBypTEzqD%2F%2B%2BvRyFiPIuACx0WwSQKiDT3Mef%2BtXTkLfhdbFsPcYR1EK3rR0syFLkNPQEU%2FuyKtpvYWZsTMHcVS5OeA4yKjoDoG19tsVFqSglBU6PuH6h5jeKEdyAOe6XduMtxptvotcFNZ4Qc16zqtekcNBHjORo%2FB5rayAigarxhegqriqdQivuS21QjwPJDvk92bm3Sg7%2BonvceYLP9SwUtvfR4MQzE0sqNkNpvgWTl7mF0MkuIbKIKJ7YQ5ndXXYnUtmdCscvpURIRLwtwg2w0y4gc6ztkiy4He1Y6SJUz%2FgA1%2F7Z4hK73NkLDsHT5kDOaX0BG5BOs0OD6ytKwDBBwVKGdKLtKPApMPf8lL0GOqUBpRUUWMXCUwYPpl1VTWsJ2xrbVcs4nAVzew161HK9%2BeeDwg8T56wJ4KoULzkobiLcEZuY1RUn9gzwhRe%2FGVjqGNgeFdqghv9exVyn38Zng5rbhi5kTKUt4aBWXi%2FYOnDcWTtM4ZOREd0P1eMmJGjyUhF0HgkCQAj%2FHERceNBlnYYKFlYGGsfdRWZxhbj7L%2FSaV8qiadszbx%2BvkL%2BjyWYuKM%2Bkovao&X-Amz-Signature=9cd8738abec8ea020b3aa277be405aa51c5e0286dae238fd8db3bb17370d1e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636TTF7U2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIBxKNPknSzWSsoMGSFn130bqwW4YzFH05i82AseFfMlsAiEApf84gvI6pRU2M6SmoR%2BTwPMw01FP23uDTA8zlhc9PDQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDPA5P0otmJTKIdo9gSrcA5j42YuqD2rUDjh17xmzRKiJ2qPEvHoY1nhBN7N68QVd5uuCmgwt4KFrCdLlPdBy7gbFE1WYJM8kYfO7hE7l9WHLickh3BGVcZAyKSj4KtpJnEDgwveC3G6PPTesO9IzZtqXSb2batvKyffEJwuUcFnCZckznZFAnQ1DonTXItoVw7a6LFy6%2B7ofyHuBw7EShJH6oTy27h0Cas5GSnrfs%2FbKBtZFoffAwIf9BbjC6lptbcgB2SDqGLhXBJH4v2h%2B%2BMdFHvrEMnTk0adrYxI9VIDWtBypTEzqD%2F%2B%2BvRyFiPIuACx0WwSQKiDT3Mef%2BtXTkLfhdbFsPcYR1EK3rR0syFLkNPQEU%2FuyKtpvYWZsTMHcVS5OeA4yKjoDoG19tsVFqSglBU6PuH6h5jeKEdyAOe6XduMtxptvotcFNZ4Qc16zqtekcNBHjORo%2FB5rayAigarxhegqriqdQivuS21QjwPJDvk92bm3Sg7%2BonvceYLP9SwUtvfR4MQzE0sqNkNpvgWTl7mF0MkuIbKIKJ7YQ5ndXXYnUtmdCscvpURIRLwtwg2w0y4gc6ztkiy4He1Y6SJUz%2FgA1%2F7Z4hK73NkLDsHT5kDOaX0BG5BOs0OD6ytKwDBBwVKGdKLtKPApMPf8lL0GOqUBpRUUWMXCUwYPpl1VTWsJ2xrbVcs4nAVzew161HK9%2BeeDwg8T56wJ4KoULzkobiLcEZuY1RUn9gzwhRe%2FGVjqGNgeFdqghv9exVyn38Zng5rbhi5kTKUt4aBWXi%2FYOnDcWTtM4ZOREd0P1eMmJGjyUhF0HgkCQAj%2FHERceNBlnYYKFlYGGsfdRWZxhbj7L%2FSaV8qiadszbx%2BvkL%2BjyWYuKM%2Bkovao&X-Amz-Signature=93805d7cc662efad3490b1071197c0f6bece2d9ccb76ea7d4a60b20af9bdc251&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVR6VR5O%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQD4mdxMmH9KLWhzVTcWc%2FtFRKvJtXkgtCM435gXfHvcHQIhAI65mtGbO6OSJM%2F45467G%2BzePEdaKt6QhDRDlM4p2xcHKv8DCGgQABoMNjM3NDIzMTgzODA1Igzew9dIU3N7x4xBCH8q3AOACkwVmJ9eGz3e0ziVryPnkb2TfZDb%2Bu0KVsf8FB6rDyBniukUnI40VSNVPzFFxaD7a6MY5Kn8p7ScAYGobG9jtupHIChnNVD2DW0kIiYqPv3YzyVYbvYaURL4J3v1Ml3G8Z6KBsLusTFHK2TA3dVDaVYe%2FSaFfq%2BM3%2F6loI3wu8xP1fCsNzxiyFTE8x3pqjnt%2FWaGw7blZ8OTgoX%2F%2BLY%2B3ronVbuwYYR8hAipMP19DM6g6D3dOFsWDgZYxSihzBRKlEresEs7coUXvvStEl7YNPQLAllFZw8ckFmtnYKxWedXvznyLaBZSQscVWsd8x95NK%2FJMODjpIZLDJBwkjvOjAv6JbtLzefDvl4KMc9XmVnU3WqZO5Ad%2Fl9OgEv%2Fkz44bmmcZo4ff5kE6obn1xHFjWh%2Bpq46sh0p%2BS9JQ4OH5D5s2SQEvqjYG9%2FEH0BUx26Q5HXzS7cQvLEnjRnQVVBCe8nLz11llZs6BoM0Kp83AWjcMUsiyUv7Ei%2BtV3GAOw7a4zuNTZ%2Br8Gx%2BTjy8FVnhc%2BvNCC6OsB6wN7OUSBVxtah7KBeRKuonRvFNHSjvneY5%2BMQBpHvvYNRrlvQ3C8WsdNHnsB5JP1%2BC4PIwXOutEh7uOK9gVfjgPFqOXzDm%2FZS9BjqkAdWGVZcXtRUZDgm5ucfgxBG2Vt3Pfvju1wVMLm1WCRuX0MW1LeAsOwsIJJMaeSi%2F8pVU5oao5lEqWN19Q9i99KLWA6Mi6%2BoLkvdx6T66aJtmgbXycZ%2Ft%2BZpANKxs54zvCulGkjR8K561TozekygTL0NiHHgu%2FXPuM5JQjj05N4Xt9PcgctzDN0jkFc4%2FRWvGz%2BeyZ4MDvpXC5acY3ooI1jQHPU1i&X-Amz-Signature=921bba8649bf468bf33c30ba5018e9cf98252ea25259b3ac221b79a28b9bc675&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T47CTM7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDSTxWO%2F%2BwVnLIwVbp0X10V70cO05S0yaHL3BzX%2B%2B47hQIhAMt4tw9zcIs1F2Agl%2FnV6b1dWwdEf66NakH9a3jM0fjPKv8DCGgQABoMNjM3NDIzMTgzODA1IgzSWWFZuc%2BegTvdjOcq3ANfvCuRyVOcwtM0%2BtQrqr4mhIZlNKDTT4D1jpqQ8z9iev3XcoXWUFy86CUE0S7jqn5A0Fe1oPsfQGz5WTIOV2r56Xk%2BqB8BoEakqGCYDucEA5VKytXjScRaIHttYz7d8OZPSYtnk9trOn36qUtD353S4L8q4ILY%2F2s6lI1q5SwHnsvj69Zm1dbcOqwx4YM%2F55767xkVeQR3lJ9XN%2BWxRc3VsAijH9uXt%2B%2F4i9Uq974OrXHRViSr8HlFkw4nBN5dZeUYsMoUUF95sLUe%2Fixp9L%2BA9YITVpGHtX8qFkLkPQZP0qwrcx7MEuFz7mmhQ1J5CCP4t85hCJJUXQUYuHA31i1kssGMqhlu1ca%2F%2FJQdnu1ioyzbvwqYHHlaKIIR07UPFqTYGyJ9I7Gh%2FfXFBkQq4Q5M%2BcmaCxBXJRJ0CUpMdSpTI%2F1VF1Yw55hkUvnu7O08jU90dL2SoWeEVyZwyWxfWVxGdjg%2BViwkk3YwNCZojiA8AkDVCMFfEIeKjNtkvS%2BklpSqSpB0C8A7hJQBuFklOVcFq3BxgRfqug4rX%2FaQSpddkvolB1Fc%2FnCKKsib0A6hXrJUy9KbIjsVWF2UGfKWmqCYtaN1uNNcjoEyNy4Lk8RLxeFseONPvQ%2FQJ%2BvBkzCP%2FZS9BjqkAaQou%2BcGnfyNIbvPbW%2BbQsbg6KDw2RS2mbAz3mPqD8Cb4ne4ubOZdd11pXEydy5h7u4zF7QxmPAHGsyppJzEwUbx4IHtdyRCkED90AqJRgOSi3TBw%2FZar%2BKYalWHZ%2B3VMrnafL771HKCIL3FJi0L0PdlygKXb1wL%2FJYO669EF3MuXRGEJt4fFnEeZ3E3O3N2zDX2%2FaZRaq8AJC5HIVEfhafnQrvJ&X-Amz-Signature=37b6b57ce0e0ee8e83d531c87fc30b688dd23c8ae53f7a35d0368dd826ac4319&X-Amz-SignedHeaders=host&x-id=GetObject)
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