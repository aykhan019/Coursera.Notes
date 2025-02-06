

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=e7bee80ea83837a2223733a101fb2fd333c555047550ef4f56bb54ce3ab1dae7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=1f5b7270a0dbbb7672ade86d3a326dae545d02d1f3b78801d8453439ca044f9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=e4396f2765794aed672cb6a3cd7156bbda7e33ea351e6add230427111328daed&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=4885c2b102df47ecbf869937a3fc14c06163cdee7684c82776629afcbf2d9b19&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=f888f92e48c4755adaf4f240caa26418649b2731e8dbc1d1bcc39671e07b9ef4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=9e594a80c3a7ab6e3003b9cc40edefcc3376bc7c745a64163ac1042f560f18f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=739e02506a5cf1cb6a56593b42ed8128eb8c580a19763d6d411239053004f6dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=9bdbc086076ecd48b8eee6a8ddcf3d0b5e426204da8eec5d139d1f2d7ab02037&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=67dafb12111314c7368edb7d508a84672b4b58d294c1d94179ec67cf88102f58&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZNLL4TL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIG9ctP7mN5M%2FE7eJoo5C3jHjm0kI4bn783Yx%2BxmhZbPlAiA3NkcP7mG7ZzsVGHD1kZ6aKKWD5wdYyfiw439j2xnS5Cr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMoCUIqp%2Fpkt0iAkRLKtwDETgVQPL0O8csK978FyIF3JAf5SrKNnoddd9HCtU71%2FcIiGHcdqswBHGUFWL4LFn4CT%2BRFVcnN3JsXtNWnkUPwF5BxZjkJBt6hGIG4kzGv3gmLnntnNP%2BiAT48%2FoACDM70d%2FGKvbWi0RWfs4rJEfvs3E48tQ23L3RQ0Y64e7uqKzpv8c%2FflSiUv02XmiC%2B7s4buC0mpQGf5jEjOuT0oy4hc38ctvRjlW%2FX6UiKvBHrvG3RWAOnEI2ypfJnbW31jfqfahwqjxijX0hy6mzNgsEUKsLM6TMzgZZSnlUrJZfR9C0lDERYDkIlCznPel03IbFlxEKVABkiI3vpczluv73lDPDDPCPWg9zViwdrc0RHTs3ZiRJK1UXvjgx%2BC9%2FaTXNrEZUVy%2FZyR4lfdFAXJjl6yB7UzVZD0vZrTqPon%2FhXIfKRVJ6VgxngTnB0PVmPaWV44l5Fgho0eW5Zoknq67Hw42kq9FGDwL%2Bn1MUQOpXN3m7VNnPcQ2sfqvJF0XhKo5PonN6911X8AAwrfCW4mVwPgjuksoy2H%2B3q9Ua%2FS6EqMUkGiplsj1SjlAGNEe%2BJkFY4DD8tTFavZOI1hBTwkhseXKu7vKkcMqM4Fly8dX46yJtGPZ0lGxNOXCzz3kw59GTvQY6pgExjps2a08Phs0zTQPTFsJXzTiMFIA2MrfqfBGr%2F%2BSaYCmjonOof%2FhhGoqGxHhGVc7ntPlu3DJdy4fcYy89Y%2FEdULyknLDZebPszWj%2FqL%2F%2FR2lFzsGVkgxdutnILwvMjK2bDEPW4nQVl8rMZFXV7PiHGghQzQvh9JMlke0lOVSlCtXIBpLdv3bGYp20U2IvEW4GnHXvvbcWbGT4vsVRhQqNZ47H9TAN&X-Amz-Signature=718499c98573609b00c36f7acee43f8cf13671b10ad840be3e62a702b35a803f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZNLL4TL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIG9ctP7mN5M%2FE7eJoo5C3jHjm0kI4bn783Yx%2BxmhZbPlAiA3NkcP7mG7ZzsVGHD1kZ6aKKWD5wdYyfiw439j2xnS5Cr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMoCUIqp%2Fpkt0iAkRLKtwDETgVQPL0O8csK978FyIF3JAf5SrKNnoddd9HCtU71%2FcIiGHcdqswBHGUFWL4LFn4CT%2BRFVcnN3JsXtNWnkUPwF5BxZjkJBt6hGIG4kzGv3gmLnntnNP%2BiAT48%2FoACDM70d%2FGKvbWi0RWfs4rJEfvs3E48tQ23L3RQ0Y64e7uqKzpv8c%2FflSiUv02XmiC%2B7s4buC0mpQGf5jEjOuT0oy4hc38ctvRjlW%2FX6UiKvBHrvG3RWAOnEI2ypfJnbW31jfqfahwqjxijX0hy6mzNgsEUKsLM6TMzgZZSnlUrJZfR9C0lDERYDkIlCznPel03IbFlxEKVABkiI3vpczluv73lDPDDPCPWg9zViwdrc0RHTs3ZiRJK1UXvjgx%2BC9%2FaTXNrEZUVy%2FZyR4lfdFAXJjl6yB7UzVZD0vZrTqPon%2FhXIfKRVJ6VgxngTnB0PVmPaWV44l5Fgho0eW5Zoknq67Hw42kq9FGDwL%2Bn1MUQOpXN3m7VNnPcQ2sfqvJF0XhKo5PonN6911X8AAwrfCW4mVwPgjuksoy2H%2B3q9Ua%2FS6EqMUkGiplsj1SjlAGNEe%2BJkFY4DD8tTFavZOI1hBTwkhseXKu7vKkcMqM4Fly8dX46yJtGPZ0lGxNOXCzz3kw59GTvQY6pgExjps2a08Phs0zTQPTFsJXzTiMFIA2MrfqfBGr%2F%2BSaYCmjonOof%2FhhGoqGxHhGVc7ntPlu3DJdy4fcYy89Y%2FEdULyknLDZebPszWj%2FqL%2F%2FR2lFzsGVkgxdutnILwvMjK2bDEPW4nQVl8rMZFXV7PiHGghQzQvh9JMlke0lOVSlCtXIBpLdv3bGYp20U2IvEW4GnHXvvbcWbGT4vsVRhQqNZ47H9TAN&X-Amz-Signature=001799d27c8df99baffaccba125106f319126d57aeeafa8588c61f030e56c3d7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZNLL4TL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIG9ctP7mN5M%2FE7eJoo5C3jHjm0kI4bn783Yx%2BxmhZbPlAiA3NkcP7mG7ZzsVGHD1kZ6aKKWD5wdYyfiw439j2xnS5Cr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMoCUIqp%2Fpkt0iAkRLKtwDETgVQPL0O8csK978FyIF3JAf5SrKNnoddd9HCtU71%2FcIiGHcdqswBHGUFWL4LFn4CT%2BRFVcnN3JsXtNWnkUPwF5BxZjkJBt6hGIG4kzGv3gmLnntnNP%2BiAT48%2FoACDM70d%2FGKvbWi0RWfs4rJEfvs3E48tQ23L3RQ0Y64e7uqKzpv8c%2FflSiUv02XmiC%2B7s4buC0mpQGf5jEjOuT0oy4hc38ctvRjlW%2FX6UiKvBHrvG3RWAOnEI2ypfJnbW31jfqfahwqjxijX0hy6mzNgsEUKsLM6TMzgZZSnlUrJZfR9C0lDERYDkIlCznPel03IbFlxEKVABkiI3vpczluv73lDPDDPCPWg9zViwdrc0RHTs3ZiRJK1UXvjgx%2BC9%2FaTXNrEZUVy%2FZyR4lfdFAXJjl6yB7UzVZD0vZrTqPon%2FhXIfKRVJ6VgxngTnB0PVmPaWV44l5Fgho0eW5Zoknq67Hw42kq9FGDwL%2Bn1MUQOpXN3m7VNnPcQ2sfqvJF0XhKo5PonN6911X8AAwrfCW4mVwPgjuksoy2H%2B3q9Ua%2FS6EqMUkGiplsj1SjlAGNEe%2BJkFY4DD8tTFavZOI1hBTwkhseXKu7vKkcMqM4Fly8dX46yJtGPZ0lGxNOXCzz3kw59GTvQY6pgExjps2a08Phs0zTQPTFsJXzTiMFIA2MrfqfBGr%2F%2BSaYCmjonOof%2FhhGoqGxHhGVc7ntPlu3DJdy4fcYy89Y%2FEdULyknLDZebPszWj%2FqL%2F%2FR2lFzsGVkgxdutnILwvMjK2bDEPW4nQVl8rMZFXV7PiHGghQzQvh9JMlke0lOVSlCtXIBpLdv3bGYp20U2IvEW4GnHXvvbcWbGT4vsVRhQqNZ47H9TAN&X-Amz-Signature=f6b68b8e0c787e10c48658a0eecbd3f9eee2a528c56f67981529367aea7e04dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=65d43810843c889ca975173749195236dc7ada7edfdb3b9f48ad35c5a3777274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=7417d1918ba00c2dc594c78f5557665e58f6fcdc693bfe63d201d92302dacdb4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=3f60542e51785459b96a149e1495514459f3aac0fa26407ebf05191982d97246&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=e67f95a119e190108598e980ad9052488ce903e27f026d57ae9f05193d8587cc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=9b40f17181f7cf1156f1c8a7a014a42e9ccf012d5bba56609479b1e3654c2db1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HTSBHFI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDSon80k2O5k8QpBbT5c%2Fx653sAEd8lAcEA3mRBcgotLgIgOYgQKHAP01Ywdcwdrgqndqof7%2BAc%2B3dAlJ8iNFbIVU0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBgRSgyeaqTohMEQwyrcA1fhOLYVF34bp12luP%2B93twUtOqdfDO%2B61l%2BTykvFDlk2UHIUetHArlQG94Ii8NlMnHXKEjstFrgmWBVQfjiimGrjK%2BFypVlHXo7ybQDtpXOeolMaFyEIZhDFR0MOJwp0vPEG3FM8sW1sjcu3VBZkNbEFd6bsg2qZppEDssyBtp3%2B0k7Ncu%2FnrrlicYma5s1dFdCrJg0MmXcjKdwiF47LgsIKlu0i4Tc3MSRB40lbs087YxLUe%2F%2FALVjP%2BI7ZfVzJRNvwU3%2FqllUmf3aCQrTWyDvle%2BCDJE9LkJSLMKZblp98cEblvWS56YKr3pqL9QSz25oU9rpOJh6fwZgGloFbZFmBHS9d0rkeAck3uThmDrlmhzmXQuQYsbk0O2Jr%2Bneg8kQyCkpmhJ3kJaFN7KJ%2BLSnsz%2FXtf1Qq5OrKEnu3nsrmuFnQj7TFejf0HBe%2B%2FyzGziTulgIaq1m5jzr9GqxMs4b3%2BN4TvBk38THdDspjD%2B50GLMdA3zYbwm40mw861778hOugBCXvSidPVVvIo%2B47sYTqK24X%2BYTXJ5GQG3PVO%2FjYvcsxy3a%2F%2FwLuXu2mP1YG2WG7LzlcThFC7GN4p2zXlCOnFz0UBpwx5Cb6BriO1%2Bp9RCKlL%2B6iAGKHpSMJHRk70GOqUB6ziZXij%2BV3LT%2Fxi8Pbxnu1CqtD0MD6SilYCRgbLa8IN4eFFdS0XAmrLHkbJXc7txEeROlTg9Zj4w%2FP2Isph31SkzAIUPhLwnDRpgIHq7%2BVBqX%2BSMqDbcI0Dm9SIS17jcdHCz3Gd%2B%2BpCK9t0n97HMT02q3MsGb%2Fau9gvRlZcoudln7CCJ4V2nWroGSsnAxV0ttFtwt3Lu9EGrskxoIx7w1vUCmC0x&X-Amz-Signature=e2c4382c00146f68a03a271493efad63f24f9e3bbc9ecfe62eb61569ad8b57eb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHGYLMAL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCwHQWcswywZr828lTjfUEWi7CE2T9EOocBQ3OSeN%2Fv3gIgOoM49f2%2FvBsaDDh5mn1ARMlBi2hESw%2B%2BWoPzQO5U4jwq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJrcIRKu%2ByBQ4WoylSrcA7YQ1y40L7qrWtIwxphH86b3CIFUhCIr4TXFl9OxSklGC7DQsxIy%2FPVgRoQosQs0MfjIMurXAUCy%2BVTdu9Gs5stDZ8E2iEJ7%2FkPSVOJ9tWJ1UeTCTlQFig863R9Romq%2BL03jh5yGhXGWLmFiTTsh8WN0VwtacGIS6L2mACl9%2B3L5GFovZl%2Fys6pje54HQ74ooh6Gbqbd52kB45XT7e0VP0TAL3dI7J8FJEy7jU8ENU7uE58bhEf%2Fg0QIARRl5FDLQtKYx3eWJFQhAJXQ%2FzwvJM9tnWMqLHiqT3WLDCz0XsOplWvMnvKEsBUvUEozGvt4y6q2BypPxYOKThRumoQ41b4cTqpkI1xs%2B1vaf6Zgl29OwbxQLFjdgH7B%2Bptce%2B48c9VjHUgR6EE4bEDsTRPe4nG%2BGWir21flR%2FajKF4tW10ZPBlpEWhC8CrcFzGUK6rMWcblqfhtJfzq06OdfUzGKj%2F2qRXR%2FvGbSNJZDiila01w20k80iJKwpeFYgBmrJY8Li7hldSpliOWZ3YCoTiEuJtLr4LNLV8QIB%2FpjT%2BwD4TBmx9VofvjELEBTi2ykDt8BII8TyWy2bnpIqWkW9br4UmdVo7%2F9bLUPfLiqermWUBOPiuPKkRe8rFPT99XMNXRk70GOqUBbhKSuKanchWpX0OhtqS3IkW5tM725CcQ%2ByHQVX%2FrFxi21%2BmFgah1whyQkrRdbPA6zsflwrHAP2Q1HogOxQp1JHzF4bVjDuvuQGJbFWyZd7gldrrF9192B4bwDNoMWAQQB%2BhuAt86zxYUZP9H0QCglbb5BD7n2MUGtdCczNkS0I0Jf7AegBKogyCchjKTa1ilN6GQJMmH4I18V3lg8fE94my0iTrT&X-Amz-Signature=8077ebbc2c199d3928c1a6270395651139b15b8b97127a92623685839691aae5&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHGYLMAL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCwHQWcswywZr828lTjfUEWi7CE2T9EOocBQ3OSeN%2Fv3gIgOoM49f2%2FvBsaDDh5mn1ARMlBi2hESw%2B%2BWoPzQO5U4jwq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJrcIRKu%2ByBQ4WoylSrcA7YQ1y40L7qrWtIwxphH86b3CIFUhCIr4TXFl9OxSklGC7DQsxIy%2FPVgRoQosQs0MfjIMurXAUCy%2BVTdu9Gs5stDZ8E2iEJ7%2FkPSVOJ9tWJ1UeTCTlQFig863R9Romq%2BL03jh5yGhXGWLmFiTTsh8WN0VwtacGIS6L2mACl9%2B3L5GFovZl%2Fys6pje54HQ74ooh6Gbqbd52kB45XT7e0VP0TAL3dI7J8FJEy7jU8ENU7uE58bhEf%2Fg0QIARRl5FDLQtKYx3eWJFQhAJXQ%2FzwvJM9tnWMqLHiqT3WLDCz0XsOplWvMnvKEsBUvUEozGvt4y6q2BypPxYOKThRumoQ41b4cTqpkI1xs%2B1vaf6Zgl29OwbxQLFjdgH7B%2Bptce%2B48c9VjHUgR6EE4bEDsTRPe4nG%2BGWir21flR%2FajKF4tW10ZPBlpEWhC8CrcFzGUK6rMWcblqfhtJfzq06OdfUzGKj%2F2qRXR%2FvGbSNJZDiila01w20k80iJKwpeFYgBmrJY8Li7hldSpliOWZ3YCoTiEuJtLr4LNLV8QIB%2FpjT%2BwD4TBmx9VofvjELEBTi2ykDt8BII8TyWy2bnpIqWkW9br4UmdVo7%2F9bLUPfLiqermWUBOPiuPKkRe8rFPT99XMNXRk70GOqUBbhKSuKanchWpX0OhtqS3IkW5tM725CcQ%2ByHQVX%2FrFxi21%2BmFgah1whyQkrRdbPA6zsflwrHAP2Q1HogOxQp1JHzF4bVjDuvuQGJbFWyZd7gldrrF9192B4bwDNoMWAQQB%2BhuAt86zxYUZP9H0QCglbb5BD7n2MUGtdCczNkS0I0Jf7AegBKogyCchjKTa1ilN6GQJMmH4I18V3lg8fE94my0iTrT&X-Amz-Signature=3e6f949e00bf6b34f4e1619ea8aa9604c0438989f87f8021b7903be96144aa1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MYH3WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDCAicjEGNCyIV%2BzUcn3gDX3xLdCP2ERgI8YM6w6Z9bfAiEAsHBVFKc6bcZWwX4AxvjfxYt6L6LRkNzCVjaKm5EAQIgq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDFtx0gsHvAgsxpXP2ircA27pAJEr88AMz%2F79TKoaB8UL1prtYMd8%2B8V5apwHlmrpitsmpDhpKR%2BRK11qMPe%2BMC%2BExD0KOZw99oD38Br4wGGJJo0pbSvv0BZmBVdB8JrokKiebjEoaMxT0TpSLBsUBxAeKNEJdCV27AH8whDfk9MxfgfRyGpJJv4aYalO7VJyuUwnfRJytOHJAwBOK222xI82x%2FgIEZPmPEH2EMZF9qh52VMku18c9MHEf8zRE%2FVKfkzWzsNKzhsVLxszhtuoEtueubKRiYZWT3aIfLxGdaUuhsG3uFiV0yerb5QUuJK912O59BTCm%2FJyMVjA91n9%2FO6zf1N%2FxuXGHvhQRsxIlUuq7ihuFEjwo2WgTxnxQYNtujaKGYehexlun3atc44o0gcjbsyxCS3VExiKmnSGgCKq4xQvBFjIyMNfZTOAs77drGr%2BU7RmAv0vWYB4RtnzC9ElBguPPJBKRTeLTHZ8mMqcryHqFyHTtfnHjXl%2BLLJ0vww%2Bpax4z0telZB62mo048T%2BLuj0Y7dyvTIqPTFpy8QPcU3qB%2BT0wd2xFldHUSK5lIzywRb%2FqaiznopRW7PEHjEMK3vdX2gSbW04KBFU6eSJWoyBr0xMwKcNng7ol63tt6klw0%2B33EqGA4fwMJXRk70GOqUBLQuZmP%2F6b0fuO%2Fw8OjgDU2lGN9gJpnVVBUOK7L8Xc74OS951TwnZuhhD027lqVZd%2BA9H39kUq7egxJdB22brkDNfM8u01mQxAoKYeKAdH4BDT6lbxhDeN5zSPzY%2BV3jS6RGQvyZRsFWJJfJZvMAlPNBmpyUDSziQbuofSLjPN7SFkPqOOHY1rfwu4mKJ9uJ7Q74Yp%2BLg0h8v883rfM2%2BZElSLffx&X-Amz-Signature=f7956d1acb2e8f6d58198e8e463101a83ce1f4e39268f2f54edbfcd60a441c0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642F7ANBR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIFxQdT9XtWJVH6zWkyC2%2F1t8Xxt%2FdjucSCxrmpQ7yEixAiEAiola8H261zmkSTLFtHhaaDsPWSoxA4nQaCK8YYJtjDIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGJb435r2LWEm5DmtircA%2Fm6c2fm0Hh0cUz%2BAwmz81nnHpqC5r077FZvv5kpWaTDvZRn0M4WrSKfg0%2BVSLnF7keG5Rqm7BUcymYlHCLTYMyEPu5e97QipycrqpbyLWA5wGF%2F2LCcPf9pUkmu8dDAtDJ6JOsAEyk8NZZMw1c%2B7Gpy3ReLGqesFUn7tBrk3eVyiiQMHE3gql8653nxA1%2B1KezsTMZv3JFxVHxIUsN2dzFEJ7j1T1Z%2BVpFy00mzRRjSaW%2FdguxYA4O%2FnTiVLCpBtJrJ7ft9qzFGxtIp%2FozhC%2B25VKT6NJ4Fx6MwfQfoY25WSsdpis9IQ2iz5kGwKi1YHgMYJJlLgnsqwwR71bVrIo8Ev3qrkX0qeo9uNhLvl%2BobmHuYrxSYSIn35OKMD%2BlEkqPdlN%2FbI4bQGsu0rz6skY7ywbgXuFuLmpD0g4V1D5fl7JnrJQVSKZNEztb58p%2B%2FGObae2lw8J0O9fH1f6Gr1Y%2BKBGAwCOSKK%2BETeC5D6UMv98oJ8mnWHZ5L7EtGFmE%2BYbJ1CwRR4o7vjAYdZ2ycfacgGp1kP4NIH4MjSvUNggBkcDrJbv7sVTOba0K%2B3u4DwNvLzW5H766Lt5QzI76QjB1RChh7VmEGnK7salUVrWFPi2h%2F8WlbetLo1cLbMMTRk70GOqUB%2B5J6q5lAq84h5azjA5JYqg6oUEU25amTS%2FAeULJKTMFpb4ZR6oQpl3gyT2WtmuNARxvGmUtf8JLfGOpS0BOBLVGvIdJKcU%2FAWV3%2FwIw6vwOZJep%2FraYjrC2BfvYRsclC%2FoctkVz2qGGqynFwjbq0hSxsFg5jp0hQ4vlPR0INvwp5gffYmpeSI5%2BiJTPlGEsFNd4Kti9ZkXlJqYOBApOu1jwjkp1w&X-Amz-Signature=41bd9b7bd17e9638ec87cc367e13766398b027a3ad959999836faec60c2e5339&X-Amz-SignedHeaders=host&x-id=GetObject)
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