

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=7c88520bb758fb322ce80b9fe3ab0e7b0f914c6032f2a4d6fce1bb25826ec0fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=a5df8a10f107858f6bb5c88b17690020c8a01ccd4430816c9dab571d9a779c03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=9331d44533cb629d66defe39d924281cd5e26a6f719ee3ac22bd6829c3afdbd5&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=0aea4c5bdcd858e5a3e37ed753cd876de11fc8d28f7b673069ff087c70e3f74a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=73c5ab243e258bce8aabba001ce713ea2856f846cd98323cf15558a3e696e4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=fb94a7ca7bec101ac029a93277146b9af51fb590572a920e79ace8d498bc50b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=9df30227ce08fe032f8700a6b4c9db0fb8462007d4a3b9cd3bb7361ff1217f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=62bdf46ba69c41c06561714d72e6f093c65b468f91d1a04922574b0e0b304b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=3784f710799cc949d78d5b38f3aae9e1cc6c6f3ef584163cc249ae6a602073c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYT4WOQN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDqEtJSi0g96iNiGOmiLdv8K3DFV%2FFhuC71HfUH%2FICJPAIgMlhMUZVUWrlUK2%2BD9rEEBWrz2dvNGN1R02q7mdTa9pUq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDC3GpTTRP9qOVMfGZyrcAw0I3Sy5R%2BNb9a0GdiR7vG2xS0YhFfOm41xDGXr6jtCTZw2ghF6S%2BgcLKverj%2B%2FnBXJ2w5Lc5h1I7CKnwPwJ7r1UbDm3ZNONsvX%2Fgg0SFfheDM8H4Xtzr9pvDqGrS1qsxwzqDXkvYbCFfO3Io73EapmVaPA4msce2QcRgYzDIGL0imGfKP6mQhsmfmni%2BWuhGr81d12W5pS6DTM2OF32HUhI7s15fj3JUW8Frl8UqjvsMzIPan0VVkUgv3yn%2FpMlsyuoHFLhGP8CMxv7%2FoabbcSTfxT%2FNWmSNW6AM0TF2z%2FEAuqL3MUnZYQKgpy8TyhIxZkqzekGRKUrpSc%2B%2FcJplE1tuAmap%2BNX4b83lgzDjwkuVNqlNADD2Cj7rQUWOtM208dgOk%2BYRp%2F6jEOpAOVc68VkQuaq0sICzQQkyVtJvZkY1R7EE2dL7Jjylc%2BZNijAcE2qVC1m%2BvPl%2BDnNyM5%2Fni%2FA2CdVvttduP3x0K%2FXDSHBG%2FglRNGXernMZx%2BDwHDp6ajNw47J7T9iL99yQ4Ny1cd4Nur%2BN8OVnuxljGC5B2luVqsyycMkjBH9Zbqowl6hVDCuDjVam%2B6keXtz2jC%2FPwA4nSFDoePI%2FCRiNatc8up%2BpSI1LnrKHssTMoyiMKOCiL0GOqUBph21BP%2FcvKK11ZkPNFZQA9YxRW9ujUKVFE%2Fl07J8yerIFjcnvYHeDI3ls7FEZGW5UHdlt1arKauknBN2xMuIB20mcxjORMZrZms7ZffLMyZsuBgcH38BHrmMc8BO7elz1pe3%2B%2FLfoSBx3I695AFJ119wSuy7%2BwvkSUtVEhguvbCnMfwT06ndUCeQZTrD6VmA6K0ivtjUNq004dNarlDv2tGJbJiV&X-Amz-Signature=ba87229b10b329f69f9e50d83e8d6e95d94e39cb9adb8d4f3011bebfb81ec0d7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYT4WOQN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDqEtJSi0g96iNiGOmiLdv8K3DFV%2FFhuC71HfUH%2FICJPAIgMlhMUZVUWrlUK2%2BD9rEEBWrz2dvNGN1R02q7mdTa9pUq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDC3GpTTRP9qOVMfGZyrcAw0I3Sy5R%2BNb9a0GdiR7vG2xS0YhFfOm41xDGXr6jtCTZw2ghF6S%2BgcLKverj%2B%2FnBXJ2w5Lc5h1I7CKnwPwJ7r1UbDm3ZNONsvX%2Fgg0SFfheDM8H4Xtzr9pvDqGrS1qsxwzqDXkvYbCFfO3Io73EapmVaPA4msce2QcRgYzDIGL0imGfKP6mQhsmfmni%2BWuhGr81d12W5pS6DTM2OF32HUhI7s15fj3JUW8Frl8UqjvsMzIPan0VVkUgv3yn%2FpMlsyuoHFLhGP8CMxv7%2FoabbcSTfxT%2FNWmSNW6AM0TF2z%2FEAuqL3MUnZYQKgpy8TyhIxZkqzekGRKUrpSc%2B%2FcJplE1tuAmap%2BNX4b83lgzDjwkuVNqlNADD2Cj7rQUWOtM208dgOk%2BYRp%2F6jEOpAOVc68VkQuaq0sICzQQkyVtJvZkY1R7EE2dL7Jjylc%2BZNijAcE2qVC1m%2BvPl%2BDnNyM5%2Fni%2FA2CdVvttduP3x0K%2FXDSHBG%2FglRNGXernMZx%2BDwHDp6ajNw47J7T9iL99yQ4Ny1cd4Nur%2BN8OVnuxljGC5B2luVqsyycMkjBH9Zbqowl6hVDCuDjVam%2B6keXtz2jC%2FPwA4nSFDoePI%2FCRiNatc8up%2BpSI1LnrKHssTMoyiMKOCiL0GOqUBph21BP%2FcvKK11ZkPNFZQA9YxRW9ujUKVFE%2Fl07J8yerIFjcnvYHeDI3ls7FEZGW5UHdlt1arKauknBN2xMuIB20mcxjORMZrZms7ZffLMyZsuBgcH38BHrmMc8BO7elz1pe3%2B%2FLfoSBx3I695AFJ119wSuy7%2BwvkSUtVEhguvbCnMfwT06ndUCeQZTrD6VmA6K0ivtjUNq004dNarlDv2tGJbJiV&X-Amz-Signature=903b8255674f01183c26f6796c0ae9c1b2c121e88b4e516d8aa8ba2c7ab85d58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYT4WOQN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDqEtJSi0g96iNiGOmiLdv8K3DFV%2FFhuC71HfUH%2FICJPAIgMlhMUZVUWrlUK2%2BD9rEEBWrz2dvNGN1R02q7mdTa9pUq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDC3GpTTRP9qOVMfGZyrcAw0I3Sy5R%2BNb9a0GdiR7vG2xS0YhFfOm41xDGXr6jtCTZw2ghF6S%2BgcLKverj%2B%2FnBXJ2w5Lc5h1I7CKnwPwJ7r1UbDm3ZNONsvX%2Fgg0SFfheDM8H4Xtzr9pvDqGrS1qsxwzqDXkvYbCFfO3Io73EapmVaPA4msce2QcRgYzDIGL0imGfKP6mQhsmfmni%2BWuhGr81d12W5pS6DTM2OF32HUhI7s15fj3JUW8Frl8UqjvsMzIPan0VVkUgv3yn%2FpMlsyuoHFLhGP8CMxv7%2FoabbcSTfxT%2FNWmSNW6AM0TF2z%2FEAuqL3MUnZYQKgpy8TyhIxZkqzekGRKUrpSc%2B%2FcJplE1tuAmap%2BNX4b83lgzDjwkuVNqlNADD2Cj7rQUWOtM208dgOk%2BYRp%2F6jEOpAOVc68VkQuaq0sICzQQkyVtJvZkY1R7EE2dL7Jjylc%2BZNijAcE2qVC1m%2BvPl%2BDnNyM5%2Fni%2FA2CdVvttduP3x0K%2FXDSHBG%2FglRNGXernMZx%2BDwHDp6ajNw47J7T9iL99yQ4Ny1cd4Nur%2BN8OVnuxljGC5B2luVqsyycMkjBH9Zbqowl6hVDCuDjVam%2B6keXtz2jC%2FPwA4nSFDoePI%2FCRiNatc8up%2BpSI1LnrKHssTMoyiMKOCiL0GOqUBph21BP%2FcvKK11ZkPNFZQA9YxRW9ujUKVFE%2Fl07J8yerIFjcnvYHeDI3ls7FEZGW5UHdlt1arKauknBN2xMuIB20mcxjORMZrZms7ZffLMyZsuBgcH38BHrmMc8BO7elz1pe3%2B%2FLfoSBx3I695AFJ119wSuy7%2BwvkSUtVEhguvbCnMfwT06ndUCeQZTrD6VmA6K0ivtjUNq004dNarlDv2tGJbJiV&X-Amz-Signature=ef4c2c3f18a27df642a930422bf1174d7b13bc76c8aa7516fcf31e33e406e198&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=38c5697261bd2267cd54751d47fbae96753477c6445aaf90fd2c525a92bf2b80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=fe97312a8080111f57a1d9f6fce559e561a26c35dc06525345907a4ff463b7e2&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=c214376807ce9dcc168acf7793cf8d7819181e82cae433f2dbe64e4c06c59585&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=92779ed360bfc6e91895d8b36f691e48f126b20d08d9eafd3014625f125df338&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=dc642f8a6ec4e79a6a67386e4ec62357e68a10535dff680be202a4f86f46d8e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW5Q2HZX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDlA80phZ3t6iC%2BWSoNGWvvnMr2y7PKklUYwn8ELY4RvQIhAOQ7116GviAMvZAHYpSNMIDvwAMCKPpAyJFeJGhPJbSsKv8DCC0QABoMNjM3NDIzMTgzODA1IgywWxbrFfOh2fChHhcq3AMX8pYSP44ZT4I9ZzzRPa2CAfqwnUG%2FcWnS92GMKnBbx4yKht95f6N%2FMQOOMRE7%2BjNHCanWNJZJnS8T0T4eXxMIKg1t%2BsTgKlAXTEU%2BT2DTGM1o7G7vDDUAoU%2BTJmfXccJfnBcJ%2BDBImb5DU4lx2onahZnxYm01MyThO3tRif27%2Fzoylu0Ld%2BUTrkXfl4fDcIgfVllctNnnx9J2LHJahBS1LOb0f%2BwvQ5%2Fs%2FT5eRHffUP62nJAJjso3mzYrHUFyjx0gbXzQTFOln2%2BXIeybV9gz6QKopnyOgr8cnrmb2TMrr42TAcZ4DdnzdCYuMvnXOgrXy5iVVxe%2BTdaoLNTw6l061tz5SMvTiBssI0ruePvFrJHsPLvoQSMxWqfDx61xbjbS%2BumXwK3p8cQuuy1DYphA2V%2B7Q%2FY7qfwwoBNA4mH6JSvX1dhuAiAf5vOLtdVhkGIxDEuWik3xHsyePF%2FeNFbBI3Q%2FjO6QQR9bXUk9skuHn8jvy9gvBiedq4Sbm3h1ksZVSmXtBDbmjmFYaCco%2BSbzynP3N7aqVksT%2BAmRVmZyT2vgI5WDCEcIcWTn2xLlDn7i9mFveuKtqzBAGdqV3mMAC8YtS45IEu0tmBniv63ix%2FdIU6%2BGX4CjyN%2BtujCpgoi9BjqkAaNgIiRJT9ocGeW%2FAE9TeIXb9rg5hTLMd2Cs1vlhSVjiR5t1VGEZzmAN7SAOTEiwgtal12uKMo9ZdHrG0c%2B2V6clx9Pmwaw5xTK8tDNuE6TvUO0gGLNlfxdhVv3dkBHa0svebAJVntxROJbopVXU4nsafB9d5tU57dpGUFnY0FWPyVNeuqf7A7FHc1uy6uc2k7IYt%2Fn08GsZAXCfnOiihO6ijUFp&X-Amz-Signature=06759ecbdaf2657422301d1dc13d3467106644978440c5f699ea93400ecebf47&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV2LRYJE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCjwup8DWmqdj0WvaE%2FImxCSAfl8iSjbDbMnFXJNSf9ewIhAInUtvxS%2BmIcUHjQP9btoDImwTukJL%2FU1P7iWe9bmKnIKv8DCC0QABoMNjM3NDIzMTgzODA1IgxB10TBIKNofYvQDJ0q3ANpZAIzIwRZg%2BYd2W1GPjbwenhBcdCAXKzmg7K8VPm1CMcDEobPojdYblKiGy3KlbeBj4L8vbZ1P3RL5ABVX2to18LGaZE0ot5rHjrm45du47jff6hD%2Bbao7xkKlazvCI02SySeiquW2pwVxgr1I8ybr%2FbJf4T9%2Bu%2FQrVJUskCzecWp5B0YiQ7kjVckvyB3a7%2BVwCPoS0uArOflBw0x1o1TIKUPpZ29TxCtU2T0%2FGDYZ328KxQhsKk5N0qIRznvsFbOP7RotWxbTHqrjSj4YcnfLSfv7jt7aCvcSvlfTxuWmgtOe%2FFtCodIFbvgMubydu%2FbDy6ZtC%2FecNkkxPob986Yv%2FAtRV7C%2FonJLFtPJVb9PGaJK0xWIch4GkznQDaM%2Ff7jKCKyrCbx69rnPqShoRS7%2FkWFBN9B97iaxFBeYZvUEpLMj6RbRlcwELWM9fmusBNZsge0BAOq3EiJUFbQfEdK4xesOUCJr2pm35QfZVsP2zuimYU26v9u4dnXmVschqT7WpBrvsW5oGsx6eGIv1%2Bp%2Bmzv%2Fx%2FF1d7aeRpvdZ83kQ5nVNBUKgV044LADDM8KYX3Vg0jsVbgCagGLubTgXFo22umIOtspE7OhxTTmQ3HMc%2F%2FQUQc2W4eENFeFTClgoi9BjqkAVhUEKaHS2%2BHBodlIYZkTskE6xCaTVtX96G3JFFhPXsjhs2DaScqHeXjjb9HZxlbr7NobtkY4HZ0BZgvcYai8aPuEUEc4Xw%2Fi1I9G2j2sNVBxNftGa59OepKpfFJHe0aTWs2HF8uM1J2o9G49xcfW%2BNexI6o1r7nNOYkr1pSapDj6a%2F7nUnNMaml%2BIN1tWhUie9074KF71AV0bd9hAURjLby%2FHsP&X-Amz-Signature=2e2e906ff06856ad990ef0289b0cb87b9954adc8e451bd265a1d4dea6b10cb65&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV2LRYJE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCjwup8DWmqdj0WvaE%2FImxCSAfl8iSjbDbMnFXJNSf9ewIhAInUtvxS%2BmIcUHjQP9btoDImwTukJL%2FU1P7iWe9bmKnIKv8DCC0QABoMNjM3NDIzMTgzODA1IgxB10TBIKNofYvQDJ0q3ANpZAIzIwRZg%2BYd2W1GPjbwenhBcdCAXKzmg7K8VPm1CMcDEobPojdYblKiGy3KlbeBj4L8vbZ1P3RL5ABVX2to18LGaZE0ot5rHjrm45du47jff6hD%2Bbao7xkKlazvCI02SySeiquW2pwVxgr1I8ybr%2FbJf4T9%2Bu%2FQrVJUskCzecWp5B0YiQ7kjVckvyB3a7%2BVwCPoS0uArOflBw0x1o1TIKUPpZ29TxCtU2T0%2FGDYZ328KxQhsKk5N0qIRznvsFbOP7RotWxbTHqrjSj4YcnfLSfv7jt7aCvcSvlfTxuWmgtOe%2FFtCodIFbvgMubydu%2FbDy6ZtC%2FecNkkxPob986Yv%2FAtRV7C%2FonJLFtPJVb9PGaJK0xWIch4GkznQDaM%2Ff7jKCKyrCbx69rnPqShoRS7%2FkWFBN9B97iaxFBeYZvUEpLMj6RbRlcwELWM9fmusBNZsge0BAOq3EiJUFbQfEdK4xesOUCJr2pm35QfZVsP2zuimYU26v9u4dnXmVschqT7WpBrvsW5oGsx6eGIv1%2Bp%2Bmzv%2Fx%2FF1d7aeRpvdZ83kQ5nVNBUKgV044LADDM8KYX3Vg0jsVbgCagGLubTgXFo22umIOtspE7OhxTTmQ3HMc%2F%2FQUQc2W4eENFeFTClgoi9BjqkAVhUEKaHS2%2BHBodlIYZkTskE6xCaTVtX96G3JFFhPXsjhs2DaScqHeXjjb9HZxlbr7NobtkY4HZ0BZgvcYai8aPuEUEc4Xw%2Fi1I9G2j2sNVBxNftGa59OepKpfFJHe0aTWs2HF8uM1J2o9G49xcfW%2BNexI6o1r7nNOYkr1pSapDj6a%2F7nUnNMaml%2BIN1tWhUie9074KF71AV0bd9hAURjLby%2FHsP&X-Amz-Signature=5fb211b4dfc51cc4a2a041624921b3770a85cfc98c9859cb8cdb166389363642&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNITC2ZC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCjrYrlOjewXE2eFZp49pxPwkIMpopivPAYer9o9JALvgIgU1xphZACUv%2FjgLI1UU5iT1nWuyq7d7ddlnfpU8CszAAq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDPxwvEA%2BCl%2F5bmdk3CrcA2DxyTDT3ryFXO1D%2FNxkM9GtZ%2BzbnJiHR0XTBD7AigqufDEsGkHpGCXvx0XZXC6d9onC5YOoiTI1xGb7zfNAnIOBCI3LSzD6pAV%2F51ku3O7PoqDpSR%2FiPXYU%2BbxnY6ltA%2FJ52V%2FihPzK%2FPeOyC%2BoeZOewEoN0lHuulVw8631kXAwlKs35H6QyUyWUdRMWJKHOmtPZUYhMnzmiEuwm4MA4FDC1xkueBQrUUvtd%2FTGP%2BOxlUlfTk4LQcojylMI2zkMvFagIyir23cbXJU%2BypB600laQ0jkUgvf7HwIJheWtCsiw9GQKk3APVHhFdIVY574jpvGa4%2BsLj5G%2Bm6ppOIbJNataw2aRkcS%2FFGffV%2BBzJ9PpoIfxZzkKUErA4xJ6PpPDKqruYl5rHGhWuNzbXneckTO14apTaZLSXuEWT7FzmMONA%2BUNl%2Ba5%2BOQAjC6YjTm1xU17YqdoNfd1WYpup%2Bymjy0acMtAC6WJ%2BEtPQz%2Bg6vWH8%2F8%2BYUBOvvr4bsvPPOVgzCC4N7K9PayAYVR80RJyo%2Fe1zLo7T03cpFXB%2BwHnXGR13eJBj1pp1xWhOj01EgNUn44sJheTL30oSChYvPs49k7C%2BynHNNMZrloXzYm4xSvt1dVRUpY225wR9FXMLCCiL0GOqUBiiqbO4CHDA9%2BN%2B8vjczLcxwpsT%2BTHXvzloss6IS6pHjduoN2CDyjAJsARAPmLdjwLGd%2B3miQAo5ddXRq%2B0Aa%2B1JUzPsuIxnXDTRfuG047AkRh2CVpesHoOhL0iboq71tnL2N%2BUV7AfH8yhpKXk%2BnX%2Fdpg3omulGNYEx%2B%2FjQhgmfxARyc7JATZK%2BIgBprrwlpgYPZxRi3voB3D2RkoBblK45eJaEX&X-Amz-Signature=3256ad87b9587359b427877758f119c7c2c87ea25d5449606a65416b4424d50e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTE5LCKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDzk8dSpgCHx1%2BajdnZRfk5t3B9BAW2rwsXYgFZiURISwIhAJ2m1T5s%2F0yWUfgsKQuUKQwODeL85PhZYdF0y2ig3l%2B6Kv8DCC0QABoMNjM3NDIzMTgzODA1IgxrgKHURWlGCDAKZ8Iq3ANgQv5SOc2o0Xtrg2H9K7gc5sDreCXkcynbbfw3J5DwBskrAPxDat5idj3n0xnzAs3pMukcAOCGjD3MkWSQcK1kmRj%2BNWb36Ljjq66TcsZE1nYFVIj1gCunUNPtr8U6upCobAELmELn1vYnt5WGaQvymqg2DvrEmkS%2FKmh99GTtPI0NKyULK0pS2TT5J%2BVT7q%2BHfvRPUufRUCLDqKqDCgR7wLAJQbfYcMb6P%2Bf0gQXCQF9vmQKo79Y%2FmUArrJI2%2BDiexaAfqdXvARYpodN8uMqLrcUF9AFBCx0gO6kKVMMKmT58lDy08AjCzr2Opvwi%2F0PrmGSL5%2FWJuZPm%2BwRXc7i384i446xYjIDzwCZJm1NOPyr4QBpl73fZ8pbhSAlnIVvG9xr6oXjk%2Fzp%2BtNLOKCuf9rXkAjnVSceIBxVt4pMQYR9BT%2Bwh4sfpNyjrlXIG9nNZVr3iumjSbJGLrdo1FpyFm%2B%2F0l3VTOxUUdef3k%2B3hzRjIsTCmbwFP3Nvm2UlNBtwPCh%2Bav4QrNrrAwymKCMdd%2BOYdkx5RA3apDlVI%2BUaxXZjk%2BFmBrx6RS24k5AnT7XEhjA8hxHOqv%2F44BeV7qXQD5yIgryMpVrPKflxDWHMKSATUfW1uD8QrUokm%2FzDugoi9BjqkAa2VTttdDDpMgWA3LyS1OXidkBsurc0jL%2BkfJXGZ55LeoeF0kOyHLJG6gmZ9hIhHlIjQQ9CG0DH%2BQYors%2By14HTpVUf0BslwuvYs9ZNKcbcxatsZuLWqMJTr8oePYLBmkyKtpdaQylCmRxlDPk2V47dYGuZsMZM9iX56LnZPFOJ0FnL8qoOFdL5crLCqRmYTTKzk2OwXdQP%2FhLEcx6uklCmnBTnV&X-Amz-Signature=62c3ae9e06be64f1b93faa419cad351eb52ed423c2d7787f16082bd19ce2a81f&X-Amz-SignedHeaders=host&x-id=GetObject)
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