

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=e8940738ffde626112fb0806b5b2065cb5d01ab3fe780d0d31e5149920eee236&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=413313ab1988a7995f52defb3d4776377ee2f93ed5868579300050da31c05818&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=815c45772c381bcb586d8dc5a3a3386a73f562fdf1b5a13946c6481f71c113a4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=b5eaa9b0c4eb5f6ce19fb0ff79b7d188a21b7652ec930c32bf37d18953f57485&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=edbd387ddfdd1faab82b0c895ec462fc48fdae00927299858d7dea6c48171247&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=bc87157dceeb23d04125b8909fc11b7aba5817d4ee00807d5ca00cc06a31a572&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=605ac78706d2a7ed1c5c25eb1c6f59fe8e9367cfe21b2543e9664efff3a414b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=17b04dae0a0450c6a2e95039958ad21e3ecc019e163876d4916c437131800a23&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=cb5a27e3a467742e1ed3725d5c59b11762574f154b6f963443bcc6454b73b40d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJIEQAKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZBgyZiR4mnuDcxFfy1fBVCBh%2Fc2xXyWPwJ1FB9k0P3AiEAyLBRB1RsjA1aV5WvLsYGqFBlyuMIamTS6%2FS3GUS3g68qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFa4V4qNYFZS1MV16ircA5hH%2B%2F7XzrgBIJMz9wS2Ah0wylvcMeyiFVgLNAWZSTHIWAhBMpxQ4hcdrZwcqc4xATs8ozDRS7uV%2BSRNM1e2nnK%2BD8KGmJCly03GSYkSa%2FyFp4bpPHmlo8v%2Fuftu2I4LkEFOyVJ91PkWQulgGhmGf1gZ4AIj%2BA2UN4CCb6ed4d37ejrzsD3kyNN4%2F1lY%2BTNrmCQxrvP2MrPc6SqnAKwBRscLNlp5jXnJy2tXhFVB0EValFwMecihpc4Jso4Xouk28Kzy6nic5d1UoB5C3xSywBRbteDoZB%2FLdMw269mMo64QvEjI8H%2B455lKoCMC2PwGne0lkpYgCV9bU62GdXxoILk1VSXU9dw4uyL6pcJwkM02PnXbhL6YrEfvvh1M3U1S0rkftFMdwC4f7ATK0hFXczyATUahNngNHfHtD%2BXHidwCuZasxCAQ52IoR7o5pOhEqoknLXCKsymDplvdESmJ%2Bcv8JggOJHBWZMjGL9y3KXEYiu7xd27p7GkHscAxFNPW6s0Mau2Dd9pEdBW7HCI8MrkFhWYoWY5QXKkA4ECwlfmwGYfntlstqStoa%2BxSNc1UGpWMYH%2BmCYzNF8qWcFKIXVuZWjDELJojLhy0iR7ost2GXn9cJPbZbuVzxpYSMPGi7LwGOqUBHBwWqeqoTuIJ%2Bf3PaCkV8Up%2BBDlQw%2FOpPqqNp2VRxWznwmgSuTTThRvruLch67FaFradZ6suNnWgAWctA2pg6qW0Vfux8MRMpUmWxr7QWBLKCcgEBn1L2tTj6dndchyxHVCcc8%2BB1aRd8fqCg143DMk7RJZGFybFvss2dlSsFMoARm4HSbDeAymzZo4pRksTZWI9bV2NxRQcFXTFpmymfKFkDAh5&X-Amz-Signature=df8c47d5c0da1dc057504b5d1a4bcf9a22dac832918bbbe3098b39148103d347&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJIEQAKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZBgyZiR4mnuDcxFfy1fBVCBh%2Fc2xXyWPwJ1FB9k0P3AiEAyLBRB1RsjA1aV5WvLsYGqFBlyuMIamTS6%2FS3GUS3g68qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFa4V4qNYFZS1MV16ircA5hH%2B%2F7XzrgBIJMz9wS2Ah0wylvcMeyiFVgLNAWZSTHIWAhBMpxQ4hcdrZwcqc4xATs8ozDRS7uV%2BSRNM1e2nnK%2BD8KGmJCly03GSYkSa%2FyFp4bpPHmlo8v%2Fuftu2I4LkEFOyVJ91PkWQulgGhmGf1gZ4AIj%2BA2UN4CCb6ed4d37ejrzsD3kyNN4%2F1lY%2BTNrmCQxrvP2MrPc6SqnAKwBRscLNlp5jXnJy2tXhFVB0EValFwMecihpc4Jso4Xouk28Kzy6nic5d1UoB5C3xSywBRbteDoZB%2FLdMw269mMo64QvEjI8H%2B455lKoCMC2PwGne0lkpYgCV9bU62GdXxoILk1VSXU9dw4uyL6pcJwkM02PnXbhL6YrEfvvh1M3U1S0rkftFMdwC4f7ATK0hFXczyATUahNngNHfHtD%2BXHidwCuZasxCAQ52IoR7o5pOhEqoknLXCKsymDplvdESmJ%2Bcv8JggOJHBWZMjGL9y3KXEYiu7xd27p7GkHscAxFNPW6s0Mau2Dd9pEdBW7HCI8MrkFhWYoWY5QXKkA4ECwlfmwGYfntlstqStoa%2BxSNc1UGpWMYH%2BmCYzNF8qWcFKIXVuZWjDELJojLhy0iR7ost2GXn9cJPbZbuVzxpYSMPGi7LwGOqUBHBwWqeqoTuIJ%2Bf3PaCkV8Up%2BBDlQw%2FOpPqqNp2VRxWznwmgSuTTThRvruLch67FaFradZ6suNnWgAWctA2pg6qW0Vfux8MRMpUmWxr7QWBLKCcgEBn1L2tTj6dndchyxHVCcc8%2BB1aRd8fqCg143DMk7RJZGFybFvss2dlSsFMoARm4HSbDeAymzZo4pRksTZWI9bV2NxRQcFXTFpmymfKFkDAh5&X-Amz-Signature=eab69503ace5f2a558e07ed82333764a81431997c38dba5c58e21bfd169e839b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJIEQAKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZBgyZiR4mnuDcxFfy1fBVCBh%2Fc2xXyWPwJ1FB9k0P3AiEAyLBRB1RsjA1aV5WvLsYGqFBlyuMIamTS6%2FS3GUS3g68qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFa4V4qNYFZS1MV16ircA5hH%2B%2F7XzrgBIJMz9wS2Ah0wylvcMeyiFVgLNAWZSTHIWAhBMpxQ4hcdrZwcqc4xATs8ozDRS7uV%2BSRNM1e2nnK%2BD8KGmJCly03GSYkSa%2FyFp4bpPHmlo8v%2Fuftu2I4LkEFOyVJ91PkWQulgGhmGf1gZ4AIj%2BA2UN4CCb6ed4d37ejrzsD3kyNN4%2F1lY%2BTNrmCQxrvP2MrPc6SqnAKwBRscLNlp5jXnJy2tXhFVB0EValFwMecihpc4Jso4Xouk28Kzy6nic5d1UoB5C3xSywBRbteDoZB%2FLdMw269mMo64QvEjI8H%2B455lKoCMC2PwGne0lkpYgCV9bU62GdXxoILk1VSXU9dw4uyL6pcJwkM02PnXbhL6YrEfvvh1M3U1S0rkftFMdwC4f7ATK0hFXczyATUahNngNHfHtD%2BXHidwCuZasxCAQ52IoR7o5pOhEqoknLXCKsymDplvdESmJ%2Bcv8JggOJHBWZMjGL9y3KXEYiu7xd27p7GkHscAxFNPW6s0Mau2Dd9pEdBW7HCI8MrkFhWYoWY5QXKkA4ECwlfmwGYfntlstqStoa%2BxSNc1UGpWMYH%2BmCYzNF8qWcFKIXVuZWjDELJojLhy0iR7ost2GXn9cJPbZbuVzxpYSMPGi7LwGOqUBHBwWqeqoTuIJ%2Bf3PaCkV8Up%2BBDlQw%2FOpPqqNp2VRxWznwmgSuTTThRvruLch67FaFradZ6suNnWgAWctA2pg6qW0Vfux8MRMpUmWxr7QWBLKCcgEBn1L2tTj6dndchyxHVCcc8%2BB1aRd8fqCg143DMk7RJZGFybFvss2dlSsFMoARm4HSbDeAymzZo4pRksTZWI9bV2NxRQcFXTFpmymfKFkDAh5&X-Amz-Signature=0596982a3d91d7dde4a810361caf413bcbf08ee84854003d2649f6875aa9e023&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=5d7005defde981068b635179c708c9ed6b9f4e95a03f9dd2e768af909fc7fdc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=abc060bd111f553b68fda8d64368a1e4c87a1f91ee56b731f2a5863eaab4ff2e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=7a248adcc05608dcf916fecbef4e93e87db670f33adea6a5e954d1f5f8c824a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=90754a6f3a25b35a2bb60683810960766db0be22c708dee15d6ce5c0d6227269&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=ca653706dd89ed142d8d09b53ff85ead6545e6261cb5cfa5669e45f015c9c189&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT4BHRQX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEAL2uSoX2LjKUTrD69SuaaoIi59HrTeK3fNF4AN3ZkwIgVDH9z%2FZrI9N3KT5lPJPAE1dvGJ8ozDEx70XzdJnvbDgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdAWKTEGin17lktZSrcA4lPQYqbjpZ8N2wXKnvefEcEPxWA%2BswPZz1MoNef1dGBYG6E%2BwLswCh7xgQ%2B3I3wBBzTgSa4fNCrXMysNKJ5RSppoHbvng4B6a8ZDKJ8ydv72RFkN5kxFusjFjPxZmuIgDP2xVJ99y6Qp1at1Pgx%2FueE61ZabztsOBxX5Y%2BJxMNKttoHZMU7gs2LbtgEy%2Bye901lHTVaGsk%2BwhOrgFV8E7rTwZDcOBJPEjdLoiwktoGEIYxKMXipBEowlxNSMohb9CyeZzCUaaV%2FUQ8oOohe3qFWPx39%2BblYQYYn5UqhluPd0CAdsYluX7Zgeh8oZtAy3XL2MPpitfXWJMaxylCR3HM1v35phUhGr8jnMdwQqd0t%2BySTRxTm4hFzIdwT1KDHVQeX3gP%2BQ%2FHH1SIGtuii6g4%2BvgDR3PAkoBgrBFYfDT5hxjJ3TiTd2hXFOkH1VVoHf4hfguydiUqE2rdN6tEbh5pFNxzFBSEckGhPtZPfgcXFxsrVUYycjsvqQung%2B8gn%2BIoDJ1TR7I0148%2Fi0ZkxNq8UEE8%2FOf57LCqehUddoK%2B9zYC1iBr6%2BFrdtuIOgq%2BmwBAjex72N92Zpl%2B5ocGu7UmfzRtxy4WcBFvgPH6FFbRBWs2zef3wE%2BrpjH0PMPii7LwGOqUBznhoY9%2Fo2yo2HGOAayE3Z36jrTyDW08gT6n5SoHQNIM1gjx4%2BJ8ERDrlmDE6ePAq3iHrwT%2BKiY0avASrrUx3BftVG4HKN9ulpcqtnpcHf6ohYVSB6yvRKl07Qqp3dfnzI%2FCpovkk15fwMxjxsBGfZEp%2FdQh42N0DCTt9Hpd8QFb5GJasdT6LlzOsYVg7gW2TyWlob3R7c26JPnuUs8cdjmSSWb30&X-Amz-Signature=e86e043b8ad4ceb2e7822b7f537d5f39215ad102230aa34d52eadbf5c2e5931f&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TUMGZ3M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo1wR4E2tbd1ky6CsYFYyw55yOykmpT257HueOqaXtTAiB27Ig9kEQHTW2oHnlrBzpi1wFWW5F4ROdShikr6eOfECqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrr7n7MYki%2FESp3w%2BKtwDlSlR4EN6EKpbOpqFKNKrHWDybbMZiAYJ%2BORw87SaeLuS8tLkSiQPI3HOhXfYhTAlr6xhIy9eQNbFLpHA3Q2PvL8YSEtng2OrP6uT4kovC9L0wvHF1JAocLx%2Fyz3GDbyehhi%2FJzIVh5GfR0OxRdyU2utFdDkduCF1Mn%2FElEbLUjAj0XBu5GiS06PazWJcT%2Fw7snHf%2BetLfDG60f3SHOZlfPoK2eKcp%2FaqcCzfqdnevZtN7hMhYE%2BfJ%2FfaV2xAulk87G4%2BXcJ6qJJlRt0CB1gdWsdDLA0XSYCtZDmzW4rIw8%2FrkE6rLevt7hQt07x7OUJOS8PJwFTUBgTEXfWNad6x9Rw02s3604pS%2FyjAeWGbbTHsvWLpkp4vpQSH3E%2FG%2BEqHzkg08r0TccV4x2xTkoXBSYQudKaOmataFNLZ%2FoWJq3m%2FSceg3gowx1l0Tj3XIix9zRJgF36ypmqyVMqwGoT5DzM3qZjFSTmhsXdN%2BV0t6UNeTtJT1XFl%2FZwZ9J8rVjUidwbiwxAN8w0fGo9JzCJNVEjZkjJKjQoM8DCag2KGlE0JqyW0q639qMgFhH4LSQ90IpgjDGXKB7ps9Wwym%2BDVqzOxvOPqhxr%2FCI2OQjs3hVY00YW1Ixfw9RXIB60wq6PsvAY6pgEIPms%2F2doC8dZtKNHbgC15QlDYRPeZY7Hupd9IS9UlYtjfqmIKygSAhEnO4e2LnVwDc9x5BYLtYe2A4a5RHV19n5gu9emgNqGxuQTBP1am3d9tK3I17wqMQSUt6sSoRPcoUSRzeGNLvnbj3Gg%2BGWIldif5eEna7XkuO1K5H4JZLFKGWAFICLf0pnqk5Ie1itW7NVwwANARBkNT4AENA1ZfHEWHQUlt&X-Amz-Signature=3fea22e155c2d87800efafbf3d46f6ad1b35c469a52af25f6fb89e771889dc92&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TUMGZ3M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo1wR4E2tbd1ky6CsYFYyw55yOykmpT257HueOqaXtTAiB27Ig9kEQHTW2oHnlrBzpi1wFWW5F4ROdShikr6eOfECqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrr7n7MYki%2FESp3w%2BKtwDlSlR4EN6EKpbOpqFKNKrHWDybbMZiAYJ%2BORw87SaeLuS8tLkSiQPI3HOhXfYhTAlr6xhIy9eQNbFLpHA3Q2PvL8YSEtng2OrP6uT4kovC9L0wvHF1JAocLx%2Fyz3GDbyehhi%2FJzIVh5GfR0OxRdyU2utFdDkduCF1Mn%2FElEbLUjAj0XBu5GiS06PazWJcT%2Fw7snHf%2BetLfDG60f3SHOZlfPoK2eKcp%2FaqcCzfqdnevZtN7hMhYE%2BfJ%2FfaV2xAulk87G4%2BXcJ6qJJlRt0CB1gdWsdDLA0XSYCtZDmzW4rIw8%2FrkE6rLevt7hQt07x7OUJOS8PJwFTUBgTEXfWNad6x9Rw02s3604pS%2FyjAeWGbbTHsvWLpkp4vpQSH3E%2FG%2BEqHzkg08r0TccV4x2xTkoXBSYQudKaOmataFNLZ%2FoWJq3m%2FSceg3gowx1l0Tj3XIix9zRJgF36ypmqyVMqwGoT5DzM3qZjFSTmhsXdN%2BV0t6UNeTtJT1XFl%2FZwZ9J8rVjUidwbiwxAN8w0fGo9JzCJNVEjZkjJKjQoM8DCag2KGlE0JqyW0q639qMgFhH4LSQ90IpgjDGXKB7ps9Wwym%2BDVqzOxvOPqhxr%2FCI2OQjs3hVY00YW1Ixfw9RXIB60wq6PsvAY6pgEIPms%2F2doC8dZtKNHbgC15QlDYRPeZY7Hupd9IS9UlYtjfqmIKygSAhEnO4e2LnVwDc9x5BYLtYe2A4a5RHV19n5gu9emgNqGxuQTBP1am3d9tK3I17wqMQSUt6sSoRPcoUSRzeGNLvnbj3Gg%2BGWIldif5eEna7XkuO1K5H4JZLFKGWAFICLf0pnqk5Ie1itW7NVwwANARBkNT4AENA1ZfHEWHQUlt&X-Amz-Signature=f5fca6618ecb646ef284edf063181754c90305fa42c2337ef5731084fc56b0ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3WW3AVM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMCvFOtc2%2FGqN8u4cNqP%2BYay7Lw%2BehZBhG1oBE53UF8AiBbGshlj%2B2jLMC5DyN1OozcvyMgthl1dsxcF271aaXo2CqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABoJfSNH34xS2bPEKtwDnhVMyTUoHAQr4%2FfZCpN7KRp%2BUDgEIGyJ8sm%2BtIo4wd7k5MQNIPIhM%2FhgzfDTrthdWFriV7lsr5Yu0eaRP4k3783We1TlPkKTy2Ahz%2Bc6%2FPhn4lPnqJ%2FFGBRJKPHcDbXNpjP2rJvx%2B9v5mPmgJC5y%2BpZDyU6N7%2Bp8n3UdQWiIA1FxXA78tvGwLROV9O38W%2Fx1cwGnhBvFp37Q2%2BMO9G8qElwL3f%2FDqIWoXgWjqaA1OXQZPi1tnYyIgE7u2rp5LNSsM3YM5cU5cSAw27m%2Blesxtw%2BgG9tpW1H2%2BODdTWWKOUldtQuFQHG2ssn4IHh23tbkIW0L462dYDUDkG66qFXleKsbOdNzA6LXu64Q2coXRBsAPu89RA9yKBMjGp5d2Pbaxrj2fD3Hm9s1G5mqifVE1xstAjiAsbZkPEZ0CarYTteWGXdR9rXfbO7s9ru%2FatALdjaV08barNn9deYwMoN9BftGIo4bxEwGvDr5S%2Fnx%2BgAVkZa4lTnFXGbEJsG2BHRo4w1zIHyB9qP9Ya84pcOeCVGw7wxFqVEWObVIrKs2QUvD5IXRfXgZBevDyNVR5a05xRn3%2BcDeSJB8MUIeXjq6CmaAUEfNU4TPR%2Fd7RVt5gYSGPjvc9kK1CHFMVv0wlevsvAY6pgGag6%2BeharmRJxdeMn0E8hMpLBCwHukGCpxaZDVCNZYiElTk4AWevIXirXDPp0sDDDbTfzWhAG82c9o39VryJhQNCtEAXB46AXlYmEf%2BkMb9Ue0mKnTbcahLyFFDMbvfbPocPLGAh9nqUOQzqoAEe95jt%2BddZHI8K57VzYKPIk8bynEhnAWZ3ZrVvamz2EU7KMozvsA2s8%2BND%2Fusp79rv5b9Mc%2BigH4&X-Amz-Signature=9e994345aad8b789021cd088923beee5248b451ff315310a80f7d6d462dc32c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQBNSEXK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTCrLFut1mbyld64IqnS7uPQWb8XpwdvHtP8i2p59K5gIgJ8%2FBWQJcIXk8jE17WZomiB%2FAKNRVm%2B12cgSLlSZjYXoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCflDDmsu5Vd6845DircA%2FVgTKVslOglYDMKdB6hG4P0yhOvaaqJX%2FI92VfpQVYhJzcuDhfrcqwtGf0n5NmjAwsL76UjTjeqdj7HY0RxRHoON5jR2yDyx%2FYOzzLDm5960%2FYn0FnMTFE2FgbXNptxZ7vEeTh8alfMnDC1lo%2FgQuE3r%2B5YAL%2BQgbAyd9CMNccIyg%2Fij6H1oE%2Fsq4MHR176E%2FvrCByfswF72wg2u2hKE4A9V0jYzOJTJryEih2W%2BpROCKN9agSxQ9Lh2FHMzVd7Q%2FQPavbkqijE2N9HqnRt3SIzg7EzmqbA6Yo%2FGLtFeBPvtv7zd%2F5feedFZVjGzVuZxlVszSJ9zSELEUOQSqi%2FacasN1gE%2F52DK%2BjESaPkTmsAbvDiWiu6ChsRB0Ik2pVTREl6IApbb3xJ4YdvoST4DaVHGZkQLBoLhYynEcrjlFXpoBwstO%2FXTWB0EhzcM3FC1GG8%2FupAzUeULmvjYMfr%2FH1j1DINK8UZzuOmGG2sW54HIpL0jOQTlDOQPSx6oZVQ0Mi7FNeCOF6mn1MJbzldkHqScM55HULP5kjpTeHEy1tQ%2B6WDUqFtR0iT9mXaGaG6GJcq%2B4Mwlnws1Fnpgv9OzL0AqWltyyZey0agp8qDymUuiBva6cPw7oDwsjIjMMOi7LwGOqUBYUR6OYLz%2F%2FU%2FjxiLHfZlEF9NgRDSIQlmjFnpx5PMfRMkNRyOzRnEYvOOenQRsl6xByPi2ZllTljULpMtV8fIv7rsETLxh%2F57fUxAYo6Asumvva8I21zAZzUXgoUOvGZU1kR2F9N%2BJgknPLwpVtuNrhTnIA4Veb3nzCn1Ar9T0aGvCjoN2yCrzB%2BQRJLh47sS82eRtF1vpCIJODc%2Fn6sIOAtaJxWy&X-Amz-Signature=6b7ad6f9f922703dff8b92cfa72f246a4eced1de75a46d334e6eaf2a8a76d7bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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