

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=003a698a111f42bfb02b9f9ada37c5b6afce4f63689a63051670f4ecaa0e8824&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=cedf0a0201e7a8b9c87662e7b6668dc73d35ff1d03744d66ca323ac2c8cbd387&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=eb53b8bd7b34b56d648ff445ab3deb81cfbdcbb297b200c3fcb4bdb6790a3cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=c505e73c497ce4d2e8e672cc278a24be3d26768c17ec7dbf6f0fbe4cd9acd481&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=ef6289384827548811d2d17c89f071b6585d15155750685bb84645eae5829412&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=78f25d0c2c2e720e59a53ab8969ea6dd079736bfb820a6295a64f17d51f7e228&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=d524ca32f21c51e7a8dcfa06af92fa0ab397a13b533fc153fab6ee7fda75a7f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=40718674c7e6a5467884ff2efec037dea6335e480cac30924b91261dadaaa0a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=e93714437e751724d396ad29dfee85e47f52bd660c1e1ef192ee9d06f66f81bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DLLIU72%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGzeQqdaySLrviXiIc%2Br96qcBZ%2Bf3FcuSxzHdC0DkIPGAiBYJPP%2FV%2BcBNaKB7TNjzyY4SeaTVE%2FwBVwECMWOWsSdPSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrNkI2tTHRszzSvlaKtwDhRqNgR8ebp4adla3%2BVtN3%2F6WzBGgrSuCSx5PTt%2BydlgB6xJ71KoUTg%2FQGPIjuhpN6cfpJAZS6AgQQzWsPgUlwAIozyMWjaTqs93X7ETIx7ymv6URUGl%2B2JMKe00kXcGSacOAXlL7JdYP5iT38FFKqHaGQ7ljUnpiJVfCVn7ssMiE%2BOGsi25jm7BsKc7zeXqBMLVWBzoYirUqK0dorJwPmKJ3YgoSoLLtWgSrwPr54xSvo4VAn3CezEKwI7DvbniUP%2BnbwCCzrizfhw8C5xKBraQEYYp6%2B9ibBoUNN94jijMELqbfUJhNWjIUI%2FP%2BR1xSrrfOd5NmrJv3W28d6i7kD%2BRX3d89cYwATf1b329SQa1%2F74QqFktYWzgBXh%2Fzm8aIwISVjyMczJs78u6wCNgIGj%2F5nfB7opsJLDnpG9uJMBSrTOJzr5DhhouGKY%2BWHSPgr3x8PoX90dhU5nIwF7zPtNme8aX49pbPpnnA%2FPYz%2FsDRqgfkSId%2FDTk%2BKdKDmLvCDEb8zMc1VFwbyoLyo010T7ntA4aFdKrpSctoM1TxCXfeC9ckiaGLfmNNGcFVdwZFp3EKT2OFNZmqfw8J3WzO0RUzvDwqEhu7Gy%2F5NKonYVPvi3Pjy89RoeztoHswk4uYvQY6pgHdIG9or3J%2Bku3%2BuGQq260iA%2BYo1kqIR4n0VV8w5GPIcw%2B10NbNqZAt0Rie%2BD1NZ%2FjCPYvvfe2oMyXEP7advncNiA86Zy%2B3%2FWcg9WduRGr03HJ97ZcTXMFSTtP%2FbnG%2F4IiJAaBwyIkybKbGaYY6bKg2u0vENB3KZ%2FB5qV6x4J3PYq6sijCfgz38zt%2B96ADGgaYe0Ra0bUwPWhJnaXRCAbAlQ9I9milC&X-Amz-Signature=48ceb70617cdb7aa654dbabbf3cd6e4e73a152f8859d036fe5178628305ab400&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DLLIU72%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGzeQqdaySLrviXiIc%2Br96qcBZ%2Bf3FcuSxzHdC0DkIPGAiBYJPP%2FV%2BcBNaKB7TNjzyY4SeaTVE%2FwBVwECMWOWsSdPSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrNkI2tTHRszzSvlaKtwDhRqNgR8ebp4adla3%2BVtN3%2F6WzBGgrSuCSx5PTt%2BydlgB6xJ71KoUTg%2FQGPIjuhpN6cfpJAZS6AgQQzWsPgUlwAIozyMWjaTqs93X7ETIx7ymv6URUGl%2B2JMKe00kXcGSacOAXlL7JdYP5iT38FFKqHaGQ7ljUnpiJVfCVn7ssMiE%2BOGsi25jm7BsKc7zeXqBMLVWBzoYirUqK0dorJwPmKJ3YgoSoLLtWgSrwPr54xSvo4VAn3CezEKwI7DvbniUP%2BnbwCCzrizfhw8C5xKBraQEYYp6%2B9ibBoUNN94jijMELqbfUJhNWjIUI%2FP%2BR1xSrrfOd5NmrJv3W28d6i7kD%2BRX3d89cYwATf1b329SQa1%2F74QqFktYWzgBXh%2Fzm8aIwISVjyMczJs78u6wCNgIGj%2F5nfB7opsJLDnpG9uJMBSrTOJzr5DhhouGKY%2BWHSPgr3x8PoX90dhU5nIwF7zPtNme8aX49pbPpnnA%2FPYz%2FsDRqgfkSId%2FDTk%2BKdKDmLvCDEb8zMc1VFwbyoLyo010T7ntA4aFdKrpSctoM1TxCXfeC9ckiaGLfmNNGcFVdwZFp3EKT2OFNZmqfw8J3WzO0RUzvDwqEhu7Gy%2F5NKonYVPvi3Pjy89RoeztoHswk4uYvQY6pgHdIG9or3J%2Bku3%2BuGQq260iA%2BYo1kqIR4n0VV8w5GPIcw%2B10NbNqZAt0Rie%2BD1NZ%2FjCPYvvfe2oMyXEP7advncNiA86Zy%2B3%2FWcg9WduRGr03HJ97ZcTXMFSTtP%2FbnG%2F4IiJAaBwyIkybKbGaYY6bKg2u0vENB3KZ%2FB5qV6x4J3PYq6sijCfgz38zt%2B96ADGgaYe0Ra0bUwPWhJnaXRCAbAlQ9I9milC&X-Amz-Signature=7164bc6cc343dea5c0d53023af36f989ce9f7df65da9b8d25fa19229b9704991&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DLLIU72%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGzeQqdaySLrviXiIc%2Br96qcBZ%2Bf3FcuSxzHdC0DkIPGAiBYJPP%2FV%2BcBNaKB7TNjzyY4SeaTVE%2FwBVwECMWOWsSdPSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrNkI2tTHRszzSvlaKtwDhRqNgR8ebp4adla3%2BVtN3%2F6WzBGgrSuCSx5PTt%2BydlgB6xJ71KoUTg%2FQGPIjuhpN6cfpJAZS6AgQQzWsPgUlwAIozyMWjaTqs93X7ETIx7ymv6URUGl%2B2JMKe00kXcGSacOAXlL7JdYP5iT38FFKqHaGQ7ljUnpiJVfCVn7ssMiE%2BOGsi25jm7BsKc7zeXqBMLVWBzoYirUqK0dorJwPmKJ3YgoSoLLtWgSrwPr54xSvo4VAn3CezEKwI7DvbniUP%2BnbwCCzrizfhw8C5xKBraQEYYp6%2B9ibBoUNN94jijMELqbfUJhNWjIUI%2FP%2BR1xSrrfOd5NmrJv3W28d6i7kD%2BRX3d89cYwATf1b329SQa1%2F74QqFktYWzgBXh%2Fzm8aIwISVjyMczJs78u6wCNgIGj%2F5nfB7opsJLDnpG9uJMBSrTOJzr5DhhouGKY%2BWHSPgr3x8PoX90dhU5nIwF7zPtNme8aX49pbPpnnA%2FPYz%2FsDRqgfkSId%2FDTk%2BKdKDmLvCDEb8zMc1VFwbyoLyo010T7ntA4aFdKrpSctoM1TxCXfeC9ckiaGLfmNNGcFVdwZFp3EKT2OFNZmqfw8J3WzO0RUzvDwqEhu7Gy%2F5NKonYVPvi3Pjy89RoeztoHswk4uYvQY6pgHdIG9or3J%2Bku3%2BuGQq260iA%2BYo1kqIR4n0VV8w5GPIcw%2B10NbNqZAt0Rie%2BD1NZ%2FjCPYvvfe2oMyXEP7advncNiA86Zy%2B3%2FWcg9WduRGr03HJ97ZcTXMFSTtP%2FbnG%2F4IiJAaBwyIkybKbGaYY6bKg2u0vENB3KZ%2FB5qV6x4J3PYq6sijCfgz38zt%2B96ADGgaYe0Ra0bUwPWhJnaXRCAbAlQ9I9milC&X-Amz-Signature=382ac2ca8ac5aa3c73a42a02a12c5b7cf7f0ea432718d46277fd9651d021bcd9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=f2c0a685c6838bab8e5f7c587d91658aa8241ed00acffd2aafe56afe5dfd77de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=556de66d6a0715b0817cc33ce8d51beac15094c4c91dcfcdccf0a5038b14d502&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=85e4d8d1b184e7016b893b4224a52aba76c7e2fb6cc7545a22aa1c9740439864&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=9d8e70459a5ee23ac685925949676e7890b8f199da832f41548f733f2c2e4714&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=395ec481ffabe50d5d494067e1eeae3cb03c059dbf27a089992e6499b8ec3a98&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPALUNRH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIHonWQmhsVQCEfxRD3w%2Byng6ZYIN35ApABoqGDAZPiPnAiEA9VWrh7VfVlUv9fUtpp3vk9RnZ8%2Bv3qstnTU9cuABmQ4q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFYCbLuIB5JHt5GD9yrcAwt1om50BiBdBhq4wPd9lIExpJsUe3nIFZq09AopcIA%2FAMaR0BPrkru2uNVoJwMYEH3Sq5hGXdriX1Pp0ElOiV4bLw0J%2FP8Pjl%2FYOZXVYEGYMQmA9TWgXqeZeIpNIAmOjPgOP6unJF0IWMBZW9DT4NtamUx1G%2B2VL4zkdV6f63MHcneA2WNjGKo%2B0oOssuI9xxnj5XvWpT%2FEjWXCfGDJ1sSFtd2MnqWuIc%2FxMJ6zdAk7e63GupC8puHpNQGYAqr8bLAxyv%2F6T7svO3fdBlxT7cPfRcPSf%2FamdRImAJ%2BlbaQY2qdTKgXRz5app4NDKgE963JEG3ZlW%2FYcDJN3r6hXEgUNiNw0HiSdHvmwjybzmxw3l7b6vhr7auC9kMSOhqoQt1Q%2FJzIQAlObVb2kousoXMrjZ9qV2vjzzsK77a2MMAqEHcaP%2BDQ3WJllcGD%2BEEZJt25DfTIErGmXLAq0Y4SvZedagqhy6aXJdwlCWCuTP%2FbCRQAiZQEBT1LHvJ228ahttK0C60Q3vYW4y9R38RwLBAbH%2BDvreV2X4fT1rxsOmnhHaxQAowGw30sQI6xYbAOAJQroxfLobizCNJ%2BiWE4NMrWHQLPuFH9mF8DB00TUiWvue7ycWDnF9LnwdSLZMJGLmL0GOqUB01R6LTPYBi9lEwpWUD78iJ3TjvQey12E3I8hmF38qaXsSRkqZR4y3y2A9vRqOshGhmeESFQ5IsOnIbUCcnY%2BHV3Gn68J7MltLYoH8RHvbDA5197SkXWv4s%2FCAbzKCpDgNVoZH1A8qTP5RDUaHWuiwPPrXcOz2GELFQp5kFOEWbkpsA%2BkpmzDVTnSvAPkQRLinuLZhBjrYr2idkVwT7wCXPgjS9s8&X-Amz-Signature=4ec1c41d5d6856f7f61222d19e330fbc2e499eda7a85f7d63466ea9a77a8ef12&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEIRBGOU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIHj1Ea91NHEF75qXyXgTOEuCpVDpUnBeM%2FX7FM3e1IXJAiAbsRqDyanIRJnK03WLjnbwkAmLBhUJqnvQE2o6ZLnxcir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIME1B8RoMJ7MDLuXXtKtwDJ8uNofqGgTQh%2Fqrd%2FdA5jRizJ4JzSIXGAt9rzrxEA0bf6Qi8G6j4A4UMZoTvtbJDp%2BHBUB%2BCRk2Uh5Xny9cXSi9Z%2FSg%2BKGMIn1ll7S0IVvBhj2qlzfK4nCnVCnnkikIudpI2xF%2BK1B%2BVAzykC5UiCHhKFttTyzfZT8iA7cazDFZap8hq6Vcy5CSi48AphEIDFFtGDv5UeVI9KfZYjm5hw1DuGYFNwBzOUheUGrlY1wJBst62fLUZqTPXB0%2F90hxfyEFsyHv6QasDg90Buq68jhdVJg0ir57bbxnZ%2FxtoQldgI6h1NNKTR5oeG7K777VT7fam8sga6YsqM5XzUbAGY5XgMVivALMMKqBOWyaExB3ccBVzDSQmaoy955RCxoRDr8P0GVN%2B1LTOO%2FCovTzZi2ceDaW4xHc1H4urNJRuw6JOv%2FwGbjc%2FXlEupLCaG81GDLDoQZaOooC%2B7nwbdsEzs1d%2Fx%2FjTHTS%2BOq%2F9rGKS0ybrbTr3iDQCZJ34nyZZrEclVPwRDVNSQmUjIhtD2SCIenF2NXtsYV3moZBR7nQYBesZqdtT9CJb0bNimDK%2Bc7q6dQJFkFOJzPX%2FVGILGWSxjii55s3%2FjB9foUx1iugB8xeMLuWMTD1vnHq3uJgw4IqYvQY6pgEXC2GnWmTcRofPAy6sIx9R1pGdwL%2FdUq8UBNJZ8LiEvOIZ44Ghr0Jv6kL3biGm45AzfvOhCC3%2F3q48chsYZNZi3VO0d77zbgBkBhrbQ8CTb2gDceSFK64VSGPuVXcAXqIHMKMUo%2BkDbDzvZnQHZGB%2BFyZCfjBE6MGn%2FkIexlN6zQBnlQar4Ie88nvgmX4IQUyy5Xt6tdDB6c7mjEHtD%2FN%2BHinJiu%2B2&X-Amz-Signature=f14318c8f9bdc73e4fcb0bf6649b8d34cd21fb9df79bf8a293be74bec1aaf28b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEIRBGOU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIHj1Ea91NHEF75qXyXgTOEuCpVDpUnBeM%2FX7FM3e1IXJAiAbsRqDyanIRJnK03WLjnbwkAmLBhUJqnvQE2o6ZLnxcir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIME1B8RoMJ7MDLuXXtKtwDJ8uNofqGgTQh%2Fqrd%2FdA5jRizJ4JzSIXGAt9rzrxEA0bf6Qi8G6j4A4UMZoTvtbJDp%2BHBUB%2BCRk2Uh5Xny9cXSi9Z%2FSg%2BKGMIn1ll7S0IVvBhj2qlzfK4nCnVCnnkikIudpI2xF%2BK1B%2BVAzykC5UiCHhKFttTyzfZT8iA7cazDFZap8hq6Vcy5CSi48AphEIDFFtGDv5UeVI9KfZYjm5hw1DuGYFNwBzOUheUGrlY1wJBst62fLUZqTPXB0%2F90hxfyEFsyHv6QasDg90Buq68jhdVJg0ir57bbxnZ%2FxtoQldgI6h1NNKTR5oeG7K777VT7fam8sga6YsqM5XzUbAGY5XgMVivALMMKqBOWyaExB3ccBVzDSQmaoy955RCxoRDr8P0GVN%2B1LTOO%2FCovTzZi2ceDaW4xHc1H4urNJRuw6JOv%2FwGbjc%2FXlEupLCaG81GDLDoQZaOooC%2B7nwbdsEzs1d%2Fx%2FjTHTS%2BOq%2F9rGKS0ybrbTr3iDQCZJ34nyZZrEclVPwRDVNSQmUjIhtD2SCIenF2NXtsYV3moZBR7nQYBesZqdtT9CJb0bNimDK%2Bc7q6dQJFkFOJzPX%2FVGILGWSxjii55s3%2FjB9foUx1iugB8xeMLuWMTD1vnHq3uJgw4IqYvQY6pgEXC2GnWmTcRofPAy6sIx9R1pGdwL%2FdUq8UBNJZ8LiEvOIZ44Ghr0Jv6kL3biGm45AzfvOhCC3%2F3q48chsYZNZi3VO0d77zbgBkBhrbQ8CTb2gDceSFK64VSGPuVXcAXqIHMKMUo%2BkDbDzvZnQHZGB%2BFyZCfjBE6MGn%2FkIexlN6zQBnlQar4Ie88nvgmX4IQUyy5Xt6tdDB6c7mjEHtD%2FN%2BHinJiu%2B2&X-Amz-Signature=263e104b9d53dd4c83f100d87e602c877964a0eb94deaf3119e37fc61a708438&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CSIUUFU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDsEarIOULlRAvRR0qQh6cP2MBKLjzfDFF2If6aMHi6KQIgCtQQZTBAybzCbnHV530%2FWl%2FBD%2BVVN%2BffEQG5tucBO38q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHioJpKtJyLtv7Gl2yrcA3Cr4UtUqV9yijwGNqK%2BU2lgzFD2gwCa1tugzVj39lMrHfZDXJAnn9qBPna%2BX%2FqQH%2BfTjD%2FwLyG8XPDrHeX9pMmtmewMkvJubln1ALANWL05XDh1N6euQYIR7iRkMTQi1H8Tn4KKNMOrTrjgBomZkQ4CDdVU65jq%2FgWoET7I5XeiYoZzlnylQgYzbHDti0cY8IZLAbsuCmJNqR0PzunQOJBcjy3AD%2BEIGWyBySj2vFSImV%2BQRz8NUlcFxnzwqkajCkNSfG4YJqPJ74xNRvqvN0I2rZetdLWRW6ZgUsurYv1Z3Q572hK5epc%2FHneqN28ZrBVeMgQ0b7qpt5wheONivm2%2BVYnAPty58a5aYn7QCOy%2B8pC0P8fdkDbQInl1n34AFl2WEeJEEqaF73Kc6vIYtWYTwTsqlIJqYh6LkqtMMiepXOzzWvAO%2F0VpFm1Z3vGQsh7zKbHneIOv5AUM4UL%2BlH8Y0djAx7DyX1QdMeUbsLkxPF5rWnWbKVhXfEBpWw%2FaPnq1sFcvskgknVVVRXmsddAExkw9p%2BN1eq91wpHmlDvCQbawqhppHUPB1rTrF50Mgf1TQIHvqw2jpIN82Vo5WCPtDUWdM3cwKRrmvdeH1qWTM5sqZTSrb3%2BmeuBUMLqLmL0GOqUBZR9Irc3GGUiEHGQ35Vasci27jPsiAOf7ohgVOfhfw34ctcEaAGxK8UF60I8ZHDhKvPiJvog0p%2FqnJivi9LoCVMfWLvKqlUTbHiF5idM7qyU9xV3aSKGaYmSDHGP5EsxhoS%2FlsNPgY5890kuB7LLc%2Fb%2BenmdXKDllz5%2Bsfh03reU6L2qYIFWI3aX%2FXY0zMFmGS5HGbP7uiYxNvN4KapZAm6GfI1O8&X-Amz-Signature=53b9381c46c9ac9ef5b1884dc9cf4c437d3572a181b32ff271654b73e3bb0a4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHWQ5IO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmPlCgsPflimdhfufauVP44urM7nRLn773K09L6qAk7QIgDPn22xMlLYqCXOy7X8Y71CqYv%2FxAE5Ioad%2FuBJFMDwAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLyjr4bHFWaoim94UircAyw7eBXdyLJ46A2C6M4Ne6AvStyvMw9DQaEM5YbrhFr0BT0TBS4zKYBAEQh0weJQxogqhQfvDOxZLZioJzZne6K5F%2BWRFFCBpZp1hb5GzkEW7VbEqIN2GOU1vT2kf5KjQJ1W8tvvcxSaMnJvk44J1OmL1eHt%2FSU%2BCBfThUujrjUrTtUen1HaRafcF4PN%2BzNY%2BlSw%2BSaTKLf6FwetFczSg1jqTnSFfhR4WzaEfgXO09NHDWqt%2Bim%2Fb66POCv%2FhtlLBzumagcWIfIWzbnrMl038TKhS9izsBN9FOJTvYI9W28j3Ap89%2FZWiCABUNMgkrEbAzaFvcS2lXcAKFn3NfRoHW2457gTrXnwG5KBOfS81x9Xi%2BEjULF8G7Ey5Dyu1RbEpw1QqN9X5Kp6b7on8gmOFvaFMt7EK80o28qoKIaGKylQw1GWStDcGtkTMHKx6KnSM%2FRSbyU8TtwG8J2Deg%2By6sIatQrf5vS%2FSghWNSr3wA4LIM0w03QsHQyVi3xScUoholk3ei9CBLDC9C0jbr1lMQAJdmm5pd2RgXEIr1cS1U88pZmS76VoLc5dWax%2B1mVUbOCuIOHDMbrjsHJZqt7uVKHzFXCEVP6TprlfugSZyKGAFpv9F7B8yV4yQlDVMJKLmL0GOqUBWkaEMypRUxGgrW2URax2FD43ny66%2Fsd5mbVAwpGuTQnBOj9UP%2BIdYbZGlOXep8VY%2BHaMBBWbeQI8njel3SWP6h7Q60spuH64KUI1nE47XcsJ2d19wOVJFM7urhkAKHlWQZVchM9UnYtwB%2BwzXWRiwxqYjpcip8f0Rp0CL%2BDP%2B7sgI0RMbG6iZv1p2%2B6LOa06Qv7R8FojjLl3Q2bTtTjrxT2XBRjV&X-Amz-Signature=a7e53d59787929385b7ab1ad2295a9e01312cec49b48c0301d4e8313da343064&X-Amz-SignedHeaders=host&x-id=GetObject)
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