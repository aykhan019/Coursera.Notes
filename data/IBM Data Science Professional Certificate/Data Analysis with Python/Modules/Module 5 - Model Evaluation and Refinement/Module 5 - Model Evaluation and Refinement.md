

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=a5ec4b91d01f4275e6d2ad0dd8de59fce73861e08faf4e5ea7284b088d220bec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=09ae349669c3bae2b5a9fd102402e58da12a988a3767a36cbe91f19f6dbd8829&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=58bb72ce683d121259583af6a578cccd8cff7927cd0b7382562c750f1cbf5278&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=554615e15130a56ada410598d4ac12f289b3b74d17e4c9cec8bde65729e8130e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=0d48a4842cf4f91cec24bf7a1df3606d8e25d60d8014a29f4bda6f595370fecf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=f4ce94a7ad1f22c8c86247bf08dda39e094c54736aa5dd5cb6e80d698805a51e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=d3eb1a6bf373446b342b4f516bae07798bf93aec254be754dfd74d4833307dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=003aaf055a8b6049bb845ee439a90065eaac324e8cf3f834a87346fb596a3571&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=695c11b0ff39a9d4092709424c613711145c4fe8b05039ef28f472e399bc3eed&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VLIHZ4J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEs%2FuaC02fpgTz127uL6dBclxlNwpCh4992WZ9HVKRxsAiBP5oeaPjzJJ5aZaXjl7ViXcv27OI0YEPl%2BycbxqQfnuSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMRwAu%2BG8r58G5qpYEKtwDmWu6WYTRXJJLlKJ4lOMR9eA14Wvjfzm77XFk%2FCD%2BmMLR3sRdAP06BJjpZybnUt%2Fzu1V8sUYGHhAebC7GfIQZImoRtnzZu9Jm%2Fu3EY5G7n9hk%2B9ubhFqEGB85meZYAuGVjwr6epV%2FjNIiGs4ksdz2j9uBQZbdb21S8dmNfYDoH1YOuI5EgRJDsSKcwBt5e4nKgpBZK%2Fr86kSoyTzmy3nJBr76geNgHwCzeIhljK0ZBjFJDZHDAdx%2BkWIESql4wQ5uKIab8eRsECEmhutK%2B6KK2Q8Uhs12WGR2%2FcKmZ2FjUDDKHR%2BCfYnQ0CNmTYcvd6ZjWFWq5WkNNsOQ1iX1xTXcC3%2FCcwMmprcj9mClbGEskZXbNOQDxU36MzIRP9zzLXjB48mpO7vOS2paNplkNd1sckZZ18%2F8ePEbsu2zao%2BWSMnMB11lT6IsuqsYn556CQAILwd8JM6kyLLbyQjH8zDimw31v6w%2F3r6NlkBeST%2BbXJNO59fhcWdq9OZo5vJM0mxr%2FNrmgV%2F0cnkwWPjlaSy0Ib%2Fr4mx4jUDtwD6JKSY2MkOs%2Fl1tC4MqyRMkqBPCI0Ii2kV4lG5pvhdfAZ6c7Y1H2BLGdITU2MIA%2FU7KUyTLipOqSrO0FdnJobUdyHIwy42DvQY6pgFEPIlAsdV%2Fz1l8vcJnCVH1SUzeDiDafgX15vVlvMzRykI7mq%2FotTW8m76SKNNUvMCcRcjtAL7F2O10hbvwBj7CLDAcC6DMdpGcAaX%2FrOqAGBF5Jn3aK2qYioWlIdIhSCNjUoCq1ZbvT8G1bHdiAE%2BlrRRUJsp9zufX%2BKmo%2FDBFPXZ%2FI4JA%2Fwm8Fz6HZ%2FlcInm9ov%2FBWJARWyMMGcssqp6XOxqngQu1&X-Amz-Signature=1dc6b8216edb1fae69c20d512492209510ce335e18d9cb2e4540b637d9210c6e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VLIHZ4J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEs%2FuaC02fpgTz127uL6dBclxlNwpCh4992WZ9HVKRxsAiBP5oeaPjzJJ5aZaXjl7ViXcv27OI0YEPl%2BycbxqQfnuSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMRwAu%2BG8r58G5qpYEKtwDmWu6WYTRXJJLlKJ4lOMR9eA14Wvjfzm77XFk%2FCD%2BmMLR3sRdAP06BJjpZybnUt%2Fzu1V8sUYGHhAebC7GfIQZImoRtnzZu9Jm%2Fu3EY5G7n9hk%2B9ubhFqEGB85meZYAuGVjwr6epV%2FjNIiGs4ksdz2j9uBQZbdb21S8dmNfYDoH1YOuI5EgRJDsSKcwBt5e4nKgpBZK%2Fr86kSoyTzmy3nJBr76geNgHwCzeIhljK0ZBjFJDZHDAdx%2BkWIESql4wQ5uKIab8eRsECEmhutK%2B6KK2Q8Uhs12WGR2%2FcKmZ2FjUDDKHR%2BCfYnQ0CNmTYcvd6ZjWFWq5WkNNsOQ1iX1xTXcC3%2FCcwMmprcj9mClbGEskZXbNOQDxU36MzIRP9zzLXjB48mpO7vOS2paNplkNd1sckZZ18%2F8ePEbsu2zao%2BWSMnMB11lT6IsuqsYn556CQAILwd8JM6kyLLbyQjH8zDimw31v6w%2F3r6NlkBeST%2BbXJNO59fhcWdq9OZo5vJM0mxr%2FNrmgV%2F0cnkwWPjlaSy0Ib%2Fr4mx4jUDtwD6JKSY2MkOs%2Fl1tC4MqyRMkqBPCI0Ii2kV4lG5pvhdfAZ6c7Y1H2BLGdITU2MIA%2FU7KUyTLipOqSrO0FdnJobUdyHIwy42DvQY6pgFEPIlAsdV%2Fz1l8vcJnCVH1SUzeDiDafgX15vVlvMzRykI7mq%2FotTW8m76SKNNUvMCcRcjtAL7F2O10hbvwBj7CLDAcC6DMdpGcAaX%2FrOqAGBF5Jn3aK2qYioWlIdIhSCNjUoCq1ZbvT8G1bHdiAE%2BlrRRUJsp9zufX%2BKmo%2FDBFPXZ%2FI4JA%2Fwm8Fz6HZ%2FlcInm9ov%2FBWJARWyMMGcssqp6XOxqngQu1&X-Amz-Signature=4459b3853b88bcdf28b055c14a84e1bd01b17948a45fbeeff59fe09d250fe99c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VLIHZ4J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEs%2FuaC02fpgTz127uL6dBclxlNwpCh4992WZ9HVKRxsAiBP5oeaPjzJJ5aZaXjl7ViXcv27OI0YEPl%2BycbxqQfnuSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMRwAu%2BG8r58G5qpYEKtwDmWu6WYTRXJJLlKJ4lOMR9eA14Wvjfzm77XFk%2FCD%2BmMLR3sRdAP06BJjpZybnUt%2Fzu1V8sUYGHhAebC7GfIQZImoRtnzZu9Jm%2Fu3EY5G7n9hk%2B9ubhFqEGB85meZYAuGVjwr6epV%2FjNIiGs4ksdz2j9uBQZbdb21S8dmNfYDoH1YOuI5EgRJDsSKcwBt5e4nKgpBZK%2Fr86kSoyTzmy3nJBr76geNgHwCzeIhljK0ZBjFJDZHDAdx%2BkWIESql4wQ5uKIab8eRsECEmhutK%2B6KK2Q8Uhs12WGR2%2FcKmZ2FjUDDKHR%2BCfYnQ0CNmTYcvd6ZjWFWq5WkNNsOQ1iX1xTXcC3%2FCcwMmprcj9mClbGEskZXbNOQDxU36MzIRP9zzLXjB48mpO7vOS2paNplkNd1sckZZ18%2F8ePEbsu2zao%2BWSMnMB11lT6IsuqsYn556CQAILwd8JM6kyLLbyQjH8zDimw31v6w%2F3r6NlkBeST%2BbXJNO59fhcWdq9OZo5vJM0mxr%2FNrmgV%2F0cnkwWPjlaSy0Ib%2Fr4mx4jUDtwD6JKSY2MkOs%2Fl1tC4MqyRMkqBPCI0Ii2kV4lG5pvhdfAZ6c7Y1H2BLGdITU2MIA%2FU7KUyTLipOqSrO0FdnJobUdyHIwy42DvQY6pgFEPIlAsdV%2Fz1l8vcJnCVH1SUzeDiDafgX15vVlvMzRykI7mq%2FotTW8m76SKNNUvMCcRcjtAL7F2O10hbvwBj7CLDAcC6DMdpGcAaX%2FrOqAGBF5Jn3aK2qYioWlIdIhSCNjUoCq1ZbvT8G1bHdiAE%2BlrRRUJsp9zufX%2BKmo%2FDBFPXZ%2FI4JA%2Fwm8Fz6HZ%2FlcInm9ov%2FBWJARWyMMGcssqp6XOxqngQu1&X-Amz-Signature=2362ba792f3eb25c73e7a6df89bfecd41372c50ae6da2645574e8f66b1df02b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=dbf5f978f192962d5f12d25d7c01ed9231d84eb2774a2a0e6df8d1dcd68a6ef2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=3ca3a343ff2e15fa588eaba18e3de38a4a7b23e413d944eb802c9ca1b920a9ae&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=768772f2202b459bb3794f0e41f2ed089efdfea722448075989a9634eca0f34c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=093b541080d583b592a6aa6812439d3c9e180da0ad2480ac8940c67d243aacf5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=16c360e85384f37daf5eee4f36ec269950c087defe68740ebe56653470948096&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLT5VIT3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDh9rDA66Okkq%2B45dRLBif6D7jWvpSRiOUhn5MwykhDpAiEAw0lbopc3aAU9eFeA2Cr2vPCaTYBRood22gvfhaFUwYUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDpC%2BtG6%2BdFcQl7mUCrcA5KavU8r2xuFL%2FN8WZnXBfO7iPC%2F4gJuH8fYLbPRTJVr6yvvwal4axoshFlC7CIZm7Sk6V%2FN61BPLQ%2FHzdnfHl8tNbg7ftEjNfgCPpYi1kPCgRKf1IJAa0rxvWBgKz8WCVbyxcKww6QX8ZAvuldaYw2pZz3NHoR3rUZrYXKrX7GKfJaRXIrMdye7lmCYNHOa%2BY5i65v5nj01fCHGbRBq1lSUcCCXhRzR9%2BspSa17vNhVqYvjej8CJce%2BxzztPxfkCOYNLhK1xcpsBbCDvTXNfCDUcDSMUFPUMrRhlYw9ptWmkC%2BFL8TwnNTWr4H%2FlKhzfaiuhGyz52ceUMecEqkalpO%2Ff7l5hp%2FRMfe5MsiHdHKPdFOcH%2FmAwvDtuRX6zVHhfThJaaSGhyx%2FB0AEnVzEzZ64uNgo8JwCaY32ozi51bcTEM0lj3S6UeOIdOLsftPbLfXdhYknhbE94yoyNu8yGbKJSgcFi7frBZ8tSFxZsj9WcPTO02ABGXyOYBgzn8jsaMFFRFpyfQ8lNB5cNmaHOJ6mjqge2JzVk6o8vgKbcJg4MBprBPwXKCQ7b6Zk0d5I6jGFnW%2BwYGnxH0lpHmp2t%2FQtZA7HimEpar1pxPe2XTfImlcnfkye%2FljXZ155MLKNg70GOqUBDkd3kbpyQ3pNTrISAtNBRFDG2q2DlEnuxy86BS%2B9rvSoDl8gnXSplQfs0YML6iNBuSEcH6z8FQsCyJFcMDkBbQ9SLlQ%2F4Wm%2Bh8ijCom%2Bl1bGti4NxjFW8q%2FIzzyhfJKAuv8lNhxexJ2%2FXuiVFE%2FcvVaKqHwmcM4LeSsBV1gGo8c30iQ0vGIPS1Fnx9qHA0XJyMm3p2JZsRHJN0MC90DlbFhC1rpR&X-Amz-Signature=e02a83d1bc347218c4177978537f476794e5d20469a08c726ee73bba889f09fc&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HR6V5SJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1MxGDVccgAgVcx04yL96RX%2Bv%2FqMXbF8%2BhnhoDy7i5lAiEAqW7BPG84JkntcG3PpyBV66PoHzJbLab9Juq5L%2F6%2BgXoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEDj47yoJd40NSQ9qircA%2Fl%2BVPGB6wh6edD35lVkKFle4IdCmSxGKn%2BzcDDlj60H6nCx%2B0B0faD1fNrLalhybiX07eRSRG3XhNPRWkba0puFpNJbY7atabxXECqOpP3ezhr4OtD8HxM3xPmSk3ZLn3hW%2FpLjGu8Tt3VAo2gTzjv7RrwiZAjNdOQ39Roqv3uDQeHDiE4xmG4f76Td2W9SwyqFw9PkDEnGv5IaJv1p5aVW0k5EiDB6rz1GhLC%2FyYBbokCg7%2BpaZyRWOiEvycS6llDzio7dYUruzBTKixH6ETIJK4PyzWILsTOwUfJJougcA1dQyEZ0XzBLyZ6qPcm0f3txfevXEixyGGlK1qX3yMzloYpo7f7eAcB27%2FRjj3TGeUgH9rfhydRHBeuQqzN6FIXeEek%2B2T2oZ9NmnfNnRIWPLZzFY%2FuxF0sgtFtKiymyreVExKyxCr9564ClwMI%2BT%2FcDM4KHgTF5RLBYuvYs21mDcN8R8pm%2F%2FuhmFgQ9gjLoaMl2usAW%2B%2FjrnAFHrJfwUf8Mqu0tXzufM1RIzWntF%2FcE8gccLu796DZ80E6uMG9nXzG0ShxgfKi%2Fz6RHaZlT5D4bBC02b4za28AjVLQ0Y7D8cU2SM1IbP%2Bo61AxdzV4xiJ5M1T6O5VFfkFMIMNeNg70GOqUBqL%2BMqw13yOILQ4sNmngAgTJy8v7wo4ZkgikiHKjZcUm99WevTL4MCXbFVYiDZnwPymbhv79TLaJGcEvale8Oup4oTpB1QahVlP892916%2BeozTA2%2BpHHaoL%2BoV7dGY19Wg3pd6qsusvziljRhSsLLMuOCEc6iCWp9ZK2YqWJlSw6ll0AbudTdxMYCxwJiDl1rcWMh7teLlC%2FHujLudfXbn8XQaw6V&X-Amz-Signature=fba7a1be7a5b06f967e2bfff1ceadc439a6ba731cbe92c6250980358724d22e3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HR6V5SJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1MxGDVccgAgVcx04yL96RX%2Bv%2FqMXbF8%2BhnhoDy7i5lAiEAqW7BPG84JkntcG3PpyBV66PoHzJbLab9Juq5L%2F6%2BgXoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDEDj47yoJd40NSQ9qircA%2Fl%2BVPGB6wh6edD35lVkKFle4IdCmSxGKn%2BzcDDlj60H6nCx%2B0B0faD1fNrLalhybiX07eRSRG3XhNPRWkba0puFpNJbY7atabxXECqOpP3ezhr4OtD8HxM3xPmSk3ZLn3hW%2FpLjGu8Tt3VAo2gTzjv7RrwiZAjNdOQ39Roqv3uDQeHDiE4xmG4f76Td2W9SwyqFw9PkDEnGv5IaJv1p5aVW0k5EiDB6rz1GhLC%2FyYBbokCg7%2BpaZyRWOiEvycS6llDzio7dYUruzBTKixH6ETIJK4PyzWILsTOwUfJJougcA1dQyEZ0XzBLyZ6qPcm0f3txfevXEixyGGlK1qX3yMzloYpo7f7eAcB27%2FRjj3TGeUgH9rfhydRHBeuQqzN6FIXeEek%2B2T2oZ9NmnfNnRIWPLZzFY%2FuxF0sgtFtKiymyreVExKyxCr9564ClwMI%2BT%2FcDM4KHgTF5RLBYuvYs21mDcN8R8pm%2F%2FuhmFgQ9gjLoaMl2usAW%2B%2FjrnAFHrJfwUf8Mqu0tXzufM1RIzWntF%2FcE8gccLu796DZ80E6uMG9nXzG0ShxgfKi%2Fz6RHaZlT5D4bBC02b4za28AjVLQ0Y7D8cU2SM1IbP%2Bo61AxdzV4xiJ5M1T6O5VFfkFMIMNeNg70GOqUBqL%2BMqw13yOILQ4sNmngAgTJy8v7wo4ZkgikiHKjZcUm99WevTL4MCXbFVYiDZnwPymbhv79TLaJGcEvale8Oup4oTpB1QahVlP892916%2BeozTA2%2BpHHaoL%2BoV7dGY19Wg3pd6qsusvziljRhSsLLMuOCEc6iCWp9ZK2YqWJlSw6ll0AbudTdxMYCxwJiDl1rcWMh7teLlC%2FHujLudfXbn8XQaw6V&X-Amz-Signature=a1c6d8787418f5b2d6eb06057c01e526fdda78b5857964fe34953587ebc0aefc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OZE5JL6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICD3OiJkphlA%2F49nz%2B15WS1q2G5nECEwwHqvttCqPWfPAiArZtXdN5K2uuf5sYMOBlrqHgp7E8o3USp40N663f7iTSr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIM9h6EVNQTYF1Y948%2BKtwDSDjo%2BLb8Kzj6AOzhhAJtfAHoulE5TguaRSx8xrzn0sqLJTYXhgPupFtqq8NKu24dUqvBUZ6W%2FM%2BW%2F8Fqewu1qLgVtfZhBcPZXaqxrlXjEBGnNylUNzU1kiPFZoCiK2IBLfOxYYOW2MXHXKmxgoxvit%2FdrSll8BgvpVvsvfbgTpB5uhZDYaztDxlLvrVl8MGqBI27ObkgkseQzqNwPTxnSWwadewXmNmUoUFzvNtXRmZl9%2BSchJiAbJeJbbBm3pSgCGHSHctRKuqDxw32QYzH6idDdhlUhsB1zOSiYPW7kulCR9gmGFzSJkgLWcDGIUenrLwIl%2BOgBT5VXnYnqqtU8T%2FT%2FaN%2Bp7pOGvVJdQAqFvEqgsW5q1QP2qkYTKBo0S%2B%2BlCqIXcpixEIETqfboYvp82eKXOmCcnpG4QZVZISCdgX8YhvORhbfZ7UQAnU48kxSZiZMqWbSnMaL5MJWnF8qeBi6ziafvoKZtAMg2bwpEMYBqBQSjVhnIjlR54%2FDQ7imEN07u3PJZze60ThlKsyTv26lNXSrQ5c4bVyb2LvIh6gnZrswOIXacPDpvvwruGpX5Ve1wpyu3eQ4YWWsKm6Oi3p9OrpsG3M9vbUy6he934ye%2Fx4jxtLIeLeYrCYw3Y2DvQY6pgEMvTZwk%2FWeTdaPul4vANP27w9wsbhcOW%2FZtLDq%2Bwmbx8I3FdOD7WdlQaLmWOuNV93YvhJD28j6f70E4NJyUHUJq3SPjfsFky4gQR%2FZjYOreGvsFdEiS8zNzMuCnS%2BFEDj23o%2FqrgRv4bxUBRjNrGAubCDVUVhwh%2BBxoULLpHzWLc%2FoE8IUeYV51Mx6x6UjLK%2FKxKtqWh6IelWVhN5RigWjrAtx%2BBT9&X-Amz-Signature=33bdd49ff6bb4fa7d2e2fac2cb712b510053f4db20f4206e187c4ac3c8f08b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EN4YBQC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXU378L5CAs7ne%2FAVbKScMipdLL9BvM5AIF3RJnEA4uAiEAy%2FQNmetCVB9xlVA%2B2ZlZIwk66GgCHh3lpl2aIpX4kTQq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBblU%2FVRSzjnhgozuCrcAyr1BsBKQxjcJTY6z76hYMO8jAhkFPZd2Uu2x5mqp3d0twWd2IRNM%2FyFjs%2BOc5MWfGwgqpVzIUNr3voys0FuNYZmdozsdaqoGe%2BemPOFtOsQhkhqpB1Yv5O3ysCD4qCHZdNUVUKwRYFlUxLXQJI09PwZCJ0zJoVxpfJB07ldZ9Pkqtvmz3SUVntQf0C9UyB2Xf0jrxgbaoHNsoHtLTF8C6psj1xV5NVJm69SB7A16pVtI6TY%2FozLP6SaF90trGycme02OYRXE7jY%2B%2BAihz2BBACHjCCI4kAxsKuu%2Bi34GGNPSfbYIC1lXLlMfMEQpSoZTfa%2BVc2e4CTyegIG5VsQ57TczejnEsyzlQq14k2lswvReZlaJwYDvetWkFHJbC7J%2FZjcZUJEy92wDt2IMR%2BysXZsnMur52lEx2SgMFZZ4GBIGC7tJglU8z%2BBLvoe4RJHRUBES%2FISm4LpK2ZXZFtgCh7k4vBNUNyrFwBRds4q%2F9TQOJWikLrQtJjObFeRCdTwpm6tburhorlNU5hKrDFm%2BHHLSLzXszZDBtheHq%2FDRQLAXiEg%2B5OcEwCC%2B%2F%2BLJsjORhfK8fdjnWeDMEbw9oYQ%2FP7tlZwFPRiNzATPTAjnK42z0zO7PejmOv9PvVujMLqNg70GOqUBKPuL6X1PZ7VtVXFi8bf4UCrpvdzJIPUyz8VCfRJU6GEktx8LAES3oHDPh1ILpRo9vioLs6HT6bM%2FVapEX6D0PtjtHzdEAF%2BMsxEE7ptKRHDzJw26OXCiF9ENf9nOeZ%2F9bDj2I6udFHXCcmnBV3NZEwFXQdzc8VWXH%2FgijoUwMq%2FK61b5%2FyurC8wq0U1xXvyibTJ7XvN9ScYPJDXX%2B5S3w%2FqKdNbJ&X-Amz-Signature=97cd484a10db7e018c1697d469435b9f89d586626cc8393548fbf0d414353b8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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