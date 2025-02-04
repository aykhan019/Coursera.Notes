

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=d7910fec0f38d436d2f8d9927e416d5bb6746718e5453690c41348b39543c227&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=8415ea56a431c063ff07cecfdb5f29b3ce0308776aee7363f896844721c028c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=094d00534e04e38edff3001a2e2b8403095761409e48fbcf19d18e0477fb8c0b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=15fe07ec84b4bf496edfb2596d93050ea913ca208a4b92d09ae22bda2c44e7b1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=54d733e8e0d758df2ccf45a5d7c16797cb5010da5c2bba0e459f7dee4243daae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=75b6e750a3d96d886dd1c99c86d780f0d17da6464b002751f88f3fdf650cf2bb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=cd3c528340757ae5af68cd70d6ff77546abb79693e5b928257abbb4f290b37a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=f208761d21bbf94cb2e018dbbd158fe3cd73d6d7b064eac407501eb5a7be1493&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=4db0942eca38d500b134ac29172c5c27436a92a8bd4fef14a025a09e0f98e324&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBIEIUMY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCCeAOwi7avneuFFQy%2FZXCzG%2BB8hW9%2BhaPQcTqTJWLfWwIgS9Izo7iDsES8xrBBwxiQ03frRXTETgkshMT31VfWUNMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDC2W4yYlfcv4Etsd5ircAxEjp%2FalCu62iREWJzgvsSivcuYQsypnQLIJVupOIC2TTnz88aK8N5SfPvE9Ty6XTr%2FXWGNaO2Ot6Mf2ZsKkwp989c%2Fzqo6tzgSnIPFyVz6jIDUN9sVxgB3YpDS96nTZ%2F6v9Es3JIr0UaidK5Y3N%2BWkov1SMlLdzABfx3eVBY0PZYZsymX6uNnWkEar974Q3%2Bt7dQWZNV30O%2BohW8278BHAkoduWEDFRnAYznLAl8m3EMxgaHl6thDciqJG8emwM2BrVnezH3UePgazEiBukvTTDsjQEpjcn1hbWz2ZorE%2F1luEhlznnX8MbI10IYQDVuqZ%2FAcIUVDmjKbJsjbouNcD6wbZ2VqyqlpyoRU%2Bwf5HES7bGl7k6iDCLPCq%2B%2Fa7%2FtPFOrvzKpi0HyFY8dnbjlruWx9Lk3Jz0VQhUG9xtJ%2Fna3WHYczjg5XdTIAsXV%2Fq469PoC%2FbYwp424yasu56QfFt2u%2FfG0PTJKvnRkQLWPRJ3RAkq3V898s%2B9o955y9CTqX0fiDfdfATNJBaJN4g0aRkOVZLkDVc3GsLj554IZ6203hg663Es7pUlsYRpyx9Ixl%2BeZI5Hv1fjZ8CIOCUIdU5vzMjqqJkLAwzh7JjMU0TayxbT29NLp50c9chrMOOihr0GOqUBJeJDsY7DheRADx5XamKlQ9wvbtRF6uibRCOWGLt%2FtDomGHsXw%2BVs2fngOHOF2mg0ixL4YzObBF7U1hWgMxW%2B3yqeRozoWvXPlG5uXgUrfwi9ysgywPzQsPwFT2Mr70RAg%2Bclsn2ZEXHILHAM4YqFwkA%2FuM%2FBtB2QvpptE1IuZBhoG6jS9Al90RKkIA8697kGXsraN7y%2Bm%2FY3C2l7EyJnj2jUnzz5&X-Amz-Signature=b43a0c92edd570cb09d8106195ab40c4929d303cd61badb0af9a1474254150b2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBIEIUMY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCCeAOwi7avneuFFQy%2FZXCzG%2BB8hW9%2BhaPQcTqTJWLfWwIgS9Izo7iDsES8xrBBwxiQ03frRXTETgkshMT31VfWUNMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDC2W4yYlfcv4Etsd5ircAxEjp%2FalCu62iREWJzgvsSivcuYQsypnQLIJVupOIC2TTnz88aK8N5SfPvE9Ty6XTr%2FXWGNaO2Ot6Mf2ZsKkwp989c%2Fzqo6tzgSnIPFyVz6jIDUN9sVxgB3YpDS96nTZ%2F6v9Es3JIr0UaidK5Y3N%2BWkov1SMlLdzABfx3eVBY0PZYZsymX6uNnWkEar974Q3%2Bt7dQWZNV30O%2BohW8278BHAkoduWEDFRnAYznLAl8m3EMxgaHl6thDciqJG8emwM2BrVnezH3UePgazEiBukvTTDsjQEpjcn1hbWz2ZorE%2F1luEhlznnX8MbI10IYQDVuqZ%2FAcIUVDmjKbJsjbouNcD6wbZ2VqyqlpyoRU%2Bwf5HES7bGl7k6iDCLPCq%2B%2Fa7%2FtPFOrvzKpi0HyFY8dnbjlruWx9Lk3Jz0VQhUG9xtJ%2Fna3WHYczjg5XdTIAsXV%2Fq469PoC%2FbYwp424yasu56QfFt2u%2FfG0PTJKvnRkQLWPRJ3RAkq3V898s%2B9o955y9CTqX0fiDfdfATNJBaJN4g0aRkOVZLkDVc3GsLj554IZ6203hg663Es7pUlsYRpyx9Ixl%2BeZI5Hv1fjZ8CIOCUIdU5vzMjqqJkLAwzh7JjMU0TayxbT29NLp50c9chrMOOihr0GOqUBJeJDsY7DheRADx5XamKlQ9wvbtRF6uibRCOWGLt%2FtDomGHsXw%2BVs2fngOHOF2mg0ixL4YzObBF7U1hWgMxW%2B3yqeRozoWvXPlG5uXgUrfwi9ysgywPzQsPwFT2Mr70RAg%2Bclsn2ZEXHILHAM4YqFwkA%2FuM%2FBtB2QvpptE1IuZBhoG6jS9Al90RKkIA8697kGXsraN7y%2Bm%2FY3C2l7EyJnj2jUnzz5&X-Amz-Signature=71c10523e9411a5797349eb21124267e12b0ee32a363b3176fc0fddc659feae0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBIEIUMY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCCeAOwi7avneuFFQy%2FZXCzG%2BB8hW9%2BhaPQcTqTJWLfWwIgS9Izo7iDsES8xrBBwxiQ03frRXTETgkshMT31VfWUNMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDC2W4yYlfcv4Etsd5ircAxEjp%2FalCu62iREWJzgvsSivcuYQsypnQLIJVupOIC2TTnz88aK8N5SfPvE9Ty6XTr%2FXWGNaO2Ot6Mf2ZsKkwp989c%2Fzqo6tzgSnIPFyVz6jIDUN9sVxgB3YpDS96nTZ%2F6v9Es3JIr0UaidK5Y3N%2BWkov1SMlLdzABfx3eVBY0PZYZsymX6uNnWkEar974Q3%2Bt7dQWZNV30O%2BohW8278BHAkoduWEDFRnAYznLAl8m3EMxgaHl6thDciqJG8emwM2BrVnezH3UePgazEiBukvTTDsjQEpjcn1hbWz2ZorE%2F1luEhlznnX8MbI10IYQDVuqZ%2FAcIUVDmjKbJsjbouNcD6wbZ2VqyqlpyoRU%2Bwf5HES7bGl7k6iDCLPCq%2B%2Fa7%2FtPFOrvzKpi0HyFY8dnbjlruWx9Lk3Jz0VQhUG9xtJ%2Fna3WHYczjg5XdTIAsXV%2Fq469PoC%2FbYwp424yasu56QfFt2u%2FfG0PTJKvnRkQLWPRJ3RAkq3V898s%2B9o955y9CTqX0fiDfdfATNJBaJN4g0aRkOVZLkDVc3GsLj554IZ6203hg663Es7pUlsYRpyx9Ixl%2BeZI5Hv1fjZ8CIOCUIdU5vzMjqqJkLAwzh7JjMU0TayxbT29NLp50c9chrMOOihr0GOqUBJeJDsY7DheRADx5XamKlQ9wvbtRF6uibRCOWGLt%2FtDomGHsXw%2BVs2fngOHOF2mg0ixL4YzObBF7U1hWgMxW%2B3yqeRozoWvXPlG5uXgUrfwi9ysgywPzQsPwFT2Mr70RAg%2Bclsn2ZEXHILHAM4YqFwkA%2FuM%2FBtB2QvpptE1IuZBhoG6jS9Al90RKkIA8697kGXsraN7y%2Bm%2FY3C2l7EyJnj2jUnzz5&X-Amz-Signature=f7a645db0c842ded89e03c9f00ef45fffaf2fd4cb6175f2555ad423d36897897&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=451cba64b97f128eaf8bbc18e49428e1ce648b944ca2140688f6be04104ba42d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=f4d52b663c8b455059e1b5d200d541a81defe79f8c3296f9daeb4fa7a67d5ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=b883fb1ea5b245b91855b0531aa04af3b35e24ee85ccc908231ae9a4b8f21090&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=446bd539ca773c9c5f13de542a762067d45ef0d4d9482b8de919aee3fc68a4f6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=8e09b84b20d24cf95702d297b54ae6d73de61f6d5643c422ef7383bfdbe70493&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434VDYG3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCICv9Ul%2F0vcU2PIjaCXpeNRgFbh6flhFMLkpiuYrN88fnAiAYZCEdH3YHO84j2e0i4ALrVhtBk%2FFkhIDmjCJQGAbQiCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMJ9iG2CkQjoefhIaqKtwD4UsJcHBvV%2Fekiz%2BE87WnIVmzGg908lGLTs4cbTwbxI2c%2BTROhAFwqliwEK4TxKOuIFNKReOtEuZMZTKQeDlHt8cy1VV3iWHpzboh1LU%2F7Osm5crSA1FdrHGioDN3bsDtyustw1VHebs5h14Ysh9GGNL0wchCzrVMLOOlLalIYDNkxOs704lGPN6GURDImJhCTnyN5%2BsNElmiZbh%2Fmalqxw7rOFMLnur5iclVp2hU4VSq%2FMuObm03UtAgMIyTUEQ22rkswrr%2BTERoDuaS9tmt%2FqYa4it1ZdreID33gxliHopNMrNRM9ddxkqWDIeDCz1%2Fqw%2BbY2GFx8M71sv6DglZnQ6gbMD7wu0OLy%2F%2F76gwVQthEVWnH413OyWlPGq%2FKipVSnBBdUNx4DN5R4PVAU5S%2BFGm%2F%2B40rigSRp1feOEH8FA1T5%2Fy9d4QXvuvasvAx%2FW4z6198oEQWkdWsvZmw9T%2BFx39uMspxf7xySjOfTW7N7%2FWRYZaEiUFYyVWkUPFyd1zE7YCwMmh5hULfVBKFj0Qt1JYgQLHD9P43J%2B4OiaS%2BuzXZ6h7Xd5gt5zZNsDan1QCHZii9Hu%2FTE42%2B97%2FPvFpHI9lAjr2JtiSx%2BsW2F87G%2FS8jQqTD298pcPIZXQwyqGGvQY6pgEmQe2LjeyppTtRLWR2vqtuOzqR2dTE%2Fzsn4yUhG0VY0POy9%2BmKI49CugtJTYd0286%2FJAA4ust4i4COtsWcuzIqOCWhbIOUPYploVrcv4M7MsZRfEk4Ewqx7XjFf2G1HsayX%2Bm3XtgHq%2FMoNJcmEwjOXLnyujDrELhFvkUgWkTQKDOBbMuCU8rbOvqDO33ctA9I1DPLZB6r9Nyzd9fuD93zdxCWyJyd&X-Amz-Signature=d6a0241fd219e6ebc57e5119e8195eff73d3772f988ec3c677938ea2a91caa42&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAP66ANU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCjyaLRPbwGWJRKK2fNamXP6fmxIz%2FKJ1efoHf797ywLwIhALVGhnTk9EJXH3K2y2Kgcg5ZIe1DvTnSnjdfQt99YJ9KKv8DCCUQABoMNjM3NDIzMTgzODA1Igyg%2FAhWbSu01wCzM2Qq3APrdsfi5Bi5GIEGZ3RYacCR5yYzKxxEHF7lz7OArlTpzSAw%2Fu0%2BMfGSpzs%2Fmp686HI1AbHMs3jc2AgHHdf2t9Sv%2Fz0MDbOJau3cncru3FAC7gkeI0791QhOTfH6W2sORXlnR36WHSeFX3yh3WEOmWMLpDxHZ6HDtLKwT8Qx0aTY0nRvaRdqRcjvg%2BKla7IdQjS9jC4i5fykR5yhluocfHcC0RZRKMA8gRcyPbnX6lL%2BPCNXP3xytl3qvLGQtsCpruFM5z0qUa3W1%2B3dSSsgMnPVTC%2FhvUeK6KWReJUs%2Fn99%2Bxkr%2FBH9yLVAybwBPx9WjStwqP1W02xfjNMRMjDVSnPDUEQPIJ%2FvaC3thRBNwEtExgNy1w7JpmjU8Ba9fMAy7rYh2UsxB1QismY5mOkUiuDMJ1kFIOxWVbb0LblmXVRMyD8aq5z7q6Nb8lAR0ta4Mpq6l14if7Qv8cxectnWZ1MhSnfsunYWx%2Fnrn7BGObWktNmLYJcEWlCRaOTwqKadO%2FT9WLyjrXJxSmjLOPEaEy%2B%2B5wM%2BqtYp7eVNGT%2FmJNfiWgyIlbuHVxqOzOqFR9CL%2FXjXYKh1nAsWMzBw05evVKtEuGVGvSG1t65jJRcLhGBBWKioriLYNk9nodaBTTCMooa9BjqkAXHQbGeYpntoPF6REgu1pIxYPDYjO6ERAmoBIy5gFvyeqyvP5Te%2F%2FG%2Bv%2B%2FMoJFplXbLLyRT0BX6q8FoWa5FjKhP%2FH2wG8KoOki0%2FzLSX4bMSAN%2FgkBpME%2BQC%2BeUAD7CjtBt7pKKXPc3DY%2FEZcjlCdfD2FHUVJ9xYHfIKO3Mb%2FOW6YwvgVYeq1DWqw%2Bl0OaWBqCL%2BTbou24pYpiUl410xBoEfZmEa&X-Amz-Signature=e3f7d561bc3ef1b039e55d85b2bcec47b0753d2b6063339025e10efd88ec3b95&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAP66ANU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCjyaLRPbwGWJRKK2fNamXP6fmxIz%2FKJ1efoHf797ywLwIhALVGhnTk9EJXH3K2y2Kgcg5ZIe1DvTnSnjdfQt99YJ9KKv8DCCUQABoMNjM3NDIzMTgzODA1Igyg%2FAhWbSu01wCzM2Qq3APrdsfi5Bi5GIEGZ3RYacCR5yYzKxxEHF7lz7OArlTpzSAw%2Fu0%2BMfGSpzs%2Fmp686HI1AbHMs3jc2AgHHdf2t9Sv%2Fz0MDbOJau3cncru3FAC7gkeI0791QhOTfH6W2sORXlnR36WHSeFX3yh3WEOmWMLpDxHZ6HDtLKwT8Qx0aTY0nRvaRdqRcjvg%2BKla7IdQjS9jC4i5fykR5yhluocfHcC0RZRKMA8gRcyPbnX6lL%2BPCNXP3xytl3qvLGQtsCpruFM5z0qUa3W1%2B3dSSsgMnPVTC%2FhvUeK6KWReJUs%2Fn99%2Bxkr%2FBH9yLVAybwBPx9WjStwqP1W02xfjNMRMjDVSnPDUEQPIJ%2FvaC3thRBNwEtExgNy1w7JpmjU8Ba9fMAy7rYh2UsxB1QismY5mOkUiuDMJ1kFIOxWVbb0LblmXVRMyD8aq5z7q6Nb8lAR0ta4Mpq6l14if7Qv8cxectnWZ1MhSnfsunYWx%2Fnrn7BGObWktNmLYJcEWlCRaOTwqKadO%2FT9WLyjrXJxSmjLOPEaEy%2B%2B5wM%2BqtYp7eVNGT%2FmJNfiWgyIlbuHVxqOzOqFR9CL%2FXjXYKh1nAsWMzBw05evVKtEuGVGvSG1t65jJRcLhGBBWKioriLYNk9nodaBTTCMooa9BjqkAXHQbGeYpntoPF6REgu1pIxYPDYjO6ERAmoBIy5gFvyeqyvP5Te%2F%2FG%2Bv%2B%2FMoJFplXbLLyRT0BX6q8FoWa5FjKhP%2FH2wG8KoOki0%2FzLSX4bMSAN%2FgkBpME%2BQC%2BeUAD7CjtBt7pKKXPc3DY%2FEZcjlCdfD2FHUVJ9xYHfIKO3Mb%2FOW6YwvgVYeq1DWqw%2Bl0OaWBqCL%2BTbou24pYpiUl410xBoEfZmEa&X-Amz-Signature=04dabfb40ca2e1051d2e9c89d648c2d8e6afcaa2eb0c9011bdcaf3e50b7590cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TFDZKZP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIGSxMqmCgZtgrkQ0l9vI%2F7vl0RPTfTqU6judHiRpbtF0AiAVWM71%2BQI0ii3LzYguV91fTBBlS42157ft8ThOOHrg0yr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIM71hbVDyyRCyk7%2FYsKtwD9Ws6pG6c39wp6cWtBrUuOP0QTlRxoBPszRPthshwUT%2F%2F5%2FtGLahVqfkejxuvQcpigLlndudDTsQw0kX0tY54nYjezC9kbZcrFgQT0UbF72R1sIdw9zLa9pRVn%2Fq%2FZ6nL4k54D2sRUpXx75OyzVkPG5mT3hODpybG7H%2BFPoAy0r21KaayHGc4e%2BAINn1osomXhbMZYCbA4TUyAzb5ZOCGfibg2%2BxNPJmsI%2BNMA%2FqeiUtX6yklTDYBXl4n8Yg0BuiLPEwcYWxyQuCGvXdNrG5sLoG4qtQAGTIFsINNERQtmWwuBWh0FWqjvphzbU8sNyuouCCt4z%2B0HGjR1nIP3lYivGii8pXFS%2FgK1c%2FGeXlPT%2FZ%2F3L%2BRKVkkzcgzUMu%2ButKPvHY9ztvMbLgMp2NkN98q4WhB66AUFVXLu4wqWuAvPfwwjoMIPj6IZGWgJ4bbaTLop7s4UP284u1s0fzsaz%2FPQpdJ1q97A038R1bcjrB0AmUvjMYftj76UUq1uRkLsyq3qCvvt9BSkyxBSidkoli%2FzzNIhCGQTM2D48CdQJF%2BIV2YavXH8wjZAnD4BJcGhCA0pbwdhlu%2BxnLLWiScd%2BucEMYvfY9szQXo0hPRg6Jw5llfotwlcZyItLVcVcYwiqKGvQY6pgGMHtP%2BNCdE4gwmeqcAnZMEVz51WWd6bMe2yK3NBS8cyvQWnZo0BR7AVVrvqpS8uXRzxTrzAjQ4LKF%2Fa90tHV2gfPkUiA9qCTa8J5wETus7eWidUmQn%2F5IJwq84B8EG1nlY1fELyBs4PsJFJgK%2BlNsCgWBxGg%2F4QjkqvbU55LQiu5oAn397q62LbYg2xUX1b0glClqfkBjziCnVqz8yjHbEkI7bfcSV&X-Amz-Signature=3017f05aa7166718a70fce4bbbbb3d4017efff3c8bdaaae3a4ad82a81d1cfae5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDPUHNJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxwSylNaCUWxPBg2KyGWXXClyj4HRndCQPCtPat%2FfMJwIgbVGeBXJz%2B4tH1n9EHCecCeVduVq%2FPmy%2FtkZErQGXrEUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJ8MtUn9LdlSp3STCircA68VWEtQTyXtWNe3%2FB3boU5yFNeoC%2BBwkCWE9qcvIlriZkCHERLBtS%2BlOn8qmPGDmP1YkbDeNlf%2FIEY5vhhZKDrROhMuDwfibelInNv1OcjL%2B987tiY3FqYvemtalnS0078qR9TpbRzA5gE6qabXHvgQeewWU0b4i9wjhlFmAXOOzWqFpNXy75OkhMXbZJihyvLLi0YZcZiV9c5hxypIJxqKLO7GArWH3W1JaEvWpJ32JzQoJL39cKg9A%2Br8ZcSklP0%2Bf5A3ZRcJUFmIirIVqFXE4ul06Lj1%2BaDqbqhve7tBbsmcBdTX7JScW6YwtFy%2BCGMsJiPwWlsA2BbF3lOLoj23frku1QftcpXmu1lH4ZRhnknFD5xv9DVtS4MhE2p9QJXO%2F8rOAsUGrYHqKM5Crz9AitmJV4UJp3lxHKftZjCQoHkiHHD4jsE5zBhAduoGVHRHEOD8a4VdM2yDxl1kGJZOK8LiVlH7Y4EFZRKIhY7woyKGP%2FIDdN6VmLsa8NejYYdyE2zJD9ZdM9d10xaknoqmAye1I4xFLDortUmsZk%2Bdt1gbRMkFgs94MFwLfoN5gATchX6Xwb4PXq5cHHFO2%2FW%2BJhrC6BG9qTeptfcBhWkA4tgcwvQAwjHVR17EMOehhr0GOqUBf0KC8KllKtMyK%2Fki7lG7dkYgBurK8qTqFFMpKLHpLJvt2YmKccAjstH3jkxcvLE25fy9hBCtHcQXE%2BfH7mOg%2BmPuaEU3pHxgxmBF5wdxV%2FuE%2BCSFWiyNr709%2BhtyQhBwIo6WkADl7q844xVMdhQKPq5N%2BIOid99%2FYKiIwK086BmTUnSnRVYxsGBgVWJS%2FAAwTXSCERWPedsXHfK6rvctMshKrgqd&X-Amz-Signature=4b8ba4c57a04157bf3a699fb44f7c3a6a6d30838fdd369fef1e422c23fdaeb1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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