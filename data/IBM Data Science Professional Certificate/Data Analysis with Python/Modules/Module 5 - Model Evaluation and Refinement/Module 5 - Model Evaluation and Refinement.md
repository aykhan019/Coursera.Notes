

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=4a60b2a16d7618c56ed9a510fac3b8587cbf9b1ba5d4eb174d90b9bd479a41fc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=914f6ba52ae815bc1b797b1dda7639e926ed8741cbe4d42f195b42882013a9f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=783fa14c8c7e67027eed06aced3a5a1f3877e51f1428677cd7a00f64c19c4bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=3aa6e47f6fa3084b28a39183ba02b1a15c079492ebb3e6f7c85cdfabf59bc98f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=9b664d12cbb808763a00e7cb86f1ef6fefd7d1e0d7a6331a9f9be696e2a43fc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=e9132fe0806a5dbdff1aab03221469320aa399f71257a0265f93e3874e63c6d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=4e6c47e774f8268348b7ad08eedac7a34a1cc6938bef536d76e0318d27a78b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=bbc80b96ad83f7642d02baf8702d5fa63c6a9991c4df9b499480c7dc57a6bf29&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=6591ec5c0ad4da28d82569eb44aeb91cc863e64fd1476cde118fd382d6b38085&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFK7HZCW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbfT3HTGhKQm1I5%2BqsmkfX%2FUCUyLjIh%2BkBa1VsMDIyOAiB6RCJkiztKNfQt7mCXhvI8HbhsYSiKezbvmWEkU6CTPSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWqjPF9jPk6Ty3mPVKtwDlH8QYChjiw1zTNpd6mnFGBi%2BiXiD%2BwiRZcNgS%2BrhYsLyvNzQA7HLaAQiZdrb7U%2BGDJqly50cl5dMNuON5LEHE4WUJ0FVaThPoShG%2FAj0jCY%2BbGT8zR3cv1P0CKfvuro2Gw4aVrJDDZ2N6pFChQ6V6Hk%2FaCpsm7N9Ejj5L94qCVlI7HMTigoiGhTkmPFp9GvTgwXB%2FKCDhTl%2BW4ZUFAlJ%2B0NJgoOd775t8VGJap3RTUlwGNB8CBI6%2FpcOvTw%2BGsMYJu6AeW5563w5iYQidl8rosl2Ign55dE0YS64EhPxm6IBIQV3iP74E%2Bvb2CEIpFVplM3HBwEYsR1PF58mUdPfDsEyLBFIiiDKntllB8X2zJpB2xtfOf9hYa0m6GUaImlV7m0WOiH%2FkRZvjndvi%2F6X8QrryukMFm%2BUp6VDC8X1nPg51cJuVGaK%2Bko14efcmLMaaqGY9FEZWVwGS4%2Bu2u66GPCMwelXKaR0gqRJCkqm1%2F4pcYzr%2Fmnx0XiBEsR6%2BhUP9kc1XwzF18dxNlxun1anFRK4cmV602%2FDrChJZ2LxOQ0K%2FBkTd60cG7%2Fa8RAXYqSC0C452I1%2BRE6CODuCglMIDf4favQ5np0X7GoXSd6PD98RVwvr58Q%2Fm%2FskXvQwrb%2BAvQY6pgGlDWCS%2FPLzgBJ6zJp8yB3LrgyB3U6Ip0a4WmmfLNthXQlKF8YF8pDVS8CODB1S4J4q%2F2K6%2BDhBC5vGtEA6TiuQxjpIGKHX33vLNQd2lnuIjs38upyBTTA0qh8irgBUebdUiTvIkRw%2Bm6zD1aN5afdJ6%2BFDJuOOIN4vD3305noDR9L1vdaRmcvEC%2FOcQz4YbVqQ%2BJHWENngo7TsO5ZP4wW2bplYns0C&X-Amz-Signature=86d894a59a99c7b979e5f594f83c72072f752bf03f8c897c2c70a2ecfc635a48&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFK7HZCW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbfT3HTGhKQm1I5%2BqsmkfX%2FUCUyLjIh%2BkBa1VsMDIyOAiB6RCJkiztKNfQt7mCXhvI8HbhsYSiKezbvmWEkU6CTPSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWqjPF9jPk6Ty3mPVKtwDlH8QYChjiw1zTNpd6mnFGBi%2BiXiD%2BwiRZcNgS%2BrhYsLyvNzQA7HLaAQiZdrb7U%2BGDJqly50cl5dMNuON5LEHE4WUJ0FVaThPoShG%2FAj0jCY%2BbGT8zR3cv1P0CKfvuro2Gw4aVrJDDZ2N6pFChQ6V6Hk%2FaCpsm7N9Ejj5L94qCVlI7HMTigoiGhTkmPFp9GvTgwXB%2FKCDhTl%2BW4ZUFAlJ%2B0NJgoOd775t8VGJap3RTUlwGNB8CBI6%2FpcOvTw%2BGsMYJu6AeW5563w5iYQidl8rosl2Ign55dE0YS64EhPxm6IBIQV3iP74E%2Bvb2CEIpFVplM3HBwEYsR1PF58mUdPfDsEyLBFIiiDKntllB8X2zJpB2xtfOf9hYa0m6GUaImlV7m0WOiH%2FkRZvjndvi%2F6X8QrryukMFm%2BUp6VDC8X1nPg51cJuVGaK%2Bko14efcmLMaaqGY9FEZWVwGS4%2Bu2u66GPCMwelXKaR0gqRJCkqm1%2F4pcYzr%2Fmnx0XiBEsR6%2BhUP9kc1XwzF18dxNlxun1anFRK4cmV602%2FDrChJZ2LxOQ0K%2FBkTd60cG7%2Fa8RAXYqSC0C452I1%2BRE6CODuCglMIDf4favQ5np0X7GoXSd6PD98RVwvr58Q%2Fm%2FskXvQwrb%2BAvQY6pgGlDWCS%2FPLzgBJ6zJp8yB3LrgyB3U6Ip0a4WmmfLNthXQlKF8YF8pDVS8CODB1S4J4q%2F2K6%2BDhBC5vGtEA6TiuQxjpIGKHX33vLNQd2lnuIjs38upyBTTA0qh8irgBUebdUiTvIkRw%2Bm6zD1aN5afdJ6%2BFDJuOOIN4vD3305noDR9L1vdaRmcvEC%2FOcQz4YbVqQ%2BJHWENngo7TsO5ZP4wW2bplYns0C&X-Amz-Signature=a384b54179da8ecd937d5925efa9dfe1fa166468fe58a659ad70f05c7fb43f5c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFK7HZCW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbfT3HTGhKQm1I5%2BqsmkfX%2FUCUyLjIh%2BkBa1VsMDIyOAiB6RCJkiztKNfQt7mCXhvI8HbhsYSiKezbvmWEkU6CTPSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWqjPF9jPk6Ty3mPVKtwDlH8QYChjiw1zTNpd6mnFGBi%2BiXiD%2BwiRZcNgS%2BrhYsLyvNzQA7HLaAQiZdrb7U%2BGDJqly50cl5dMNuON5LEHE4WUJ0FVaThPoShG%2FAj0jCY%2BbGT8zR3cv1P0CKfvuro2Gw4aVrJDDZ2N6pFChQ6V6Hk%2FaCpsm7N9Ejj5L94qCVlI7HMTigoiGhTkmPFp9GvTgwXB%2FKCDhTl%2BW4ZUFAlJ%2B0NJgoOd775t8VGJap3RTUlwGNB8CBI6%2FpcOvTw%2BGsMYJu6AeW5563w5iYQidl8rosl2Ign55dE0YS64EhPxm6IBIQV3iP74E%2Bvb2CEIpFVplM3HBwEYsR1PF58mUdPfDsEyLBFIiiDKntllB8X2zJpB2xtfOf9hYa0m6GUaImlV7m0WOiH%2FkRZvjndvi%2F6X8QrryukMFm%2BUp6VDC8X1nPg51cJuVGaK%2Bko14efcmLMaaqGY9FEZWVwGS4%2Bu2u66GPCMwelXKaR0gqRJCkqm1%2F4pcYzr%2Fmnx0XiBEsR6%2BhUP9kc1XwzF18dxNlxun1anFRK4cmV602%2FDrChJZ2LxOQ0K%2FBkTd60cG7%2Fa8RAXYqSC0C452I1%2BRE6CODuCglMIDf4favQ5np0X7GoXSd6PD98RVwvr58Q%2Fm%2FskXvQwrb%2BAvQY6pgGlDWCS%2FPLzgBJ6zJp8yB3LrgyB3U6Ip0a4WmmfLNthXQlKF8YF8pDVS8CODB1S4J4q%2F2K6%2BDhBC5vGtEA6TiuQxjpIGKHX33vLNQd2lnuIjs38upyBTTA0qh8irgBUebdUiTvIkRw%2Bm6zD1aN5afdJ6%2BFDJuOOIN4vD3305noDR9L1vdaRmcvEC%2FOcQz4YbVqQ%2BJHWENngo7TsO5ZP4wW2bplYns0C&X-Amz-Signature=18e6331fd77bd63f932bf19ba6a9bec311a93c1caf2edfc272b1554aa6b3a827&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=822b316802163c7d010ceac3ed8ecf8f6cb9afb33b51b13362432d9b7fb01b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=7a82d616f34a39e85328943d19d75568a59617a0d8e8059d38c7b72bd9369962&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=a49ab01282fd1d81fe2d643f708439d13d084409f3bbed8351e0dae99d5fe001&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=7416a6716fe572e3c08ad4f1f100170faa7b34b7e22c2e8c0b68c2e401751c47&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=cc8f70017638409116c81c22e3c278b52ac2584ce679fcd4f494c6c02fb8e7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQKPVCSD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFrRCbWQCN6YJ6wJyTaz3PKQJgZlLZbcKQpQNbYOCEGAiEAmQmuNpRvs5XWLaEJEznr5ZvCZhiLXVj0sK0a5zP5iNoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqOdJnt1eiE8BK0qyrcA5E25Zdu3bIV%2BjgESatfF50O8a0GHtNnN5qj3y4NKLjwIJhz2%2Fo2UpwOHQeGWpMzFqk6sZ0VqkTkqKnj7d1B4ULgbQl39%2FIHGFP%2BmqlyvPzEpLe3GcCUtv76d3GxgdKWGQm%2BlhSu%2FbHTz3HLITYg%2FvqprdlVzvxAKfCte8nzVTBZ9%2BctGdmxDN5Irl21RHnPN90agMotgYlzqx4GMA7t3MR%2FjUtDeFGXoLIIphuz5YPP%2F1%2BIYkvHZjgVk0PMd0uENJZewaCXwEM5ZgRtQ3wjD0JmnuuNI65PIlzpUXZIAVQaHFHoR5qxyYNrorqqmQNl4rSiNHAd5Sh1ZAjJx19%2F1YGA5AfMKsWysczJ8l2%2B4iLh%2FkTdWIIr4Izx7QPEnz60BqEm8NkYE4Mvec4mrsK31HH8EWQtvmkzzJv7N91gmkLH4GmZvbaC%2FZtPlmkybgnwoTgiwzHhwxMcch9rbOxWhewzBg55%2BXA005MiPfYd1th3n1f98gGp8QnvlCNAfuVhZmo3nOkCup7wq8PChNOU8KzDylQES2x2FEw1kzDSk8J08NjELoaTZIpGyQfZAb0Q7uFeomeg4eynAn74PFcWMPe75CSVtJhFAxfcUzBX1moa7NQimy21%2BlodviTAMJe%2FgL0GOqUBm7rS3%2Bt1xUvO9g2XEycgdULjlF7GTosoGWpnAsf5nQBQQkGM%2BgWERNFicofKgGUe6cl2%2FmY%2B5KL7QSf%2BhvB8Cu41JenNK%2BpkZ7Ib1FoTsVjid6clIBNzwE8DmrAdoT%2FJVJvJtDu%2FttdPkkbpQasLEgFWPgN05bf3qwrbbCoK07%2BzciuUpmM8NOxsMiCHzV9lPYBpU%2B8HCoL0jogaAjZxBgSZjL2L&X-Amz-Signature=1bcafbfcc4128b4458f4f82f0f2a4bdc32c4f04e6903eba9ccb9d75668210394&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHRWPF6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLsMIcaQFZc%2FIffkshzn496Dn3aKqNB6As8mj96Pp2uAIgMgXeaQ8FiKh18a4%2BtO5c%2B9Bi1f41yNSXTUSx2Ak6e6EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOexqD96%2BOIr2kreWyrcAy0xLDOT9hhQ4Nv0hNN7XuuNMY8wbFoVzZO1OPaZSGeyyNzvPesDgbyaDE9gPutuYRnqD9y2k4NKX2nkjP34%2B519VD4fvqX4igNjieiwpOabXZ3o%2BQUidOiCt%2Faf1cR2aTJXO2%2FS7%2Fq1S2nMQEouBDpgVTg4k8inXbZ4axd8wIKaRa9weeSiOLxqMSPuUaUOW%2BGlT2AgSyAZZvX40WBLjJyyLuhkHOBYpLqTqn7vhWSmoAB%2FjJZPBpinn9vsUG%2BPk0dpS4Yp%2F1zyyTwf0NcnUJ%2BWDpoqC48xVdwnRf%2BDsuios%2FjNIcab95sCL01tHdvH4zrIETDKLDAz8d22mPheMnOlmNP6VjbHhJDNy956Q6DoKTWzwqrmY62sh%2F3XKzWmaQH6Eks9VVjkfhTGIUBVjepmEdBe4aRyjwvSFiWkqsgJL%2BB4zdEQIw8UwQOlpJxQ80dpVWIpJjrwLT31bFybkT8cBFs2eJNEkSxSbpkVFh8sryij20LVj2kiZZOvn3mUYNh0OkyIzZ5FECwW4%2Fag%2BfZ3mlr9u6q3loYRFKH9lhRAeqe9UBFbV2GV7qtmS%2BJ9kBIc4Y%2FwXNf%2Fhl%2FKRNwtXVbmLiJ9R9J00TpWRgKVznEvSGkEE9iBkAuRSafMMK%2B%2FgL0GOqUB5j%2FiGlUsLk6v%2FBy%2FDq8PG4psKrI3PE9A2rytapIrzUHSFEnaCx6eauovG98fkAJ30Sl8f%2Fg%2BZXYsI5OX65OWTrWu8jVWERtWW2l6ckKd26M0gzsekrQ2o5fV2Q8BfKWE1mVhzAkYfO3I0ADadEvSocN4sbW5GUZr2D8YCiPk7CsnzPACHi%2FJH6ej2MbJvYycFRjkykD4Htaa2QPsxLncqew6LblY&X-Amz-Signature=70839b31243fb8d159a1a085cc8f1b9011b88dd5eb08d3147aaf78155d714470&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHRWPF6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLsMIcaQFZc%2FIffkshzn496Dn3aKqNB6As8mj96Pp2uAIgMgXeaQ8FiKh18a4%2BtO5c%2B9Bi1f41yNSXTUSx2Ak6e6EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOexqD96%2BOIr2kreWyrcAy0xLDOT9hhQ4Nv0hNN7XuuNMY8wbFoVzZO1OPaZSGeyyNzvPesDgbyaDE9gPutuYRnqD9y2k4NKX2nkjP34%2B519VD4fvqX4igNjieiwpOabXZ3o%2BQUidOiCt%2Faf1cR2aTJXO2%2FS7%2Fq1S2nMQEouBDpgVTg4k8inXbZ4axd8wIKaRa9weeSiOLxqMSPuUaUOW%2BGlT2AgSyAZZvX40WBLjJyyLuhkHOBYpLqTqn7vhWSmoAB%2FjJZPBpinn9vsUG%2BPk0dpS4Yp%2F1zyyTwf0NcnUJ%2BWDpoqC48xVdwnRf%2BDsuios%2FjNIcab95sCL01tHdvH4zrIETDKLDAz8d22mPheMnOlmNP6VjbHhJDNy956Q6DoKTWzwqrmY62sh%2F3XKzWmaQH6Eks9VVjkfhTGIUBVjepmEdBe4aRyjwvSFiWkqsgJL%2BB4zdEQIw8UwQOlpJxQ80dpVWIpJjrwLT31bFybkT8cBFs2eJNEkSxSbpkVFh8sryij20LVj2kiZZOvn3mUYNh0OkyIzZ5FECwW4%2Fag%2BfZ3mlr9u6q3loYRFKH9lhRAeqe9UBFbV2GV7qtmS%2BJ9kBIc4Y%2FwXNf%2Fhl%2FKRNwtXVbmLiJ9R9J00TpWRgKVznEvSGkEE9iBkAuRSafMMK%2B%2FgL0GOqUB5j%2FiGlUsLk6v%2FBy%2FDq8PG4psKrI3PE9A2rytapIrzUHSFEnaCx6eauovG98fkAJ30Sl8f%2Fg%2BZXYsI5OX65OWTrWu8jVWERtWW2l6ckKd26M0gzsekrQ2o5fV2Q8BfKWE1mVhzAkYfO3I0ADadEvSocN4sbW5GUZr2D8YCiPk7CsnzPACHi%2FJH6ej2MbJvYycFRjkykD4Htaa2QPsxLncqew6LblY&X-Amz-Signature=1b746c2833ccd43ded8225d70cf801d419401ff64e023ee45415cba2ae2613d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2S3RKXB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRx0GjlrPcrEnZpiHTtql5bEr%2FXpVCXDGIJghpGcBLtAiB2NySnvRCu0wihCqWC0HkvPiIM1NFYUI6FtM7KEwCRTSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJ%2FTOEbb3x9dcyIiKtwDIbfsPPcN89SG%2BsIiB7VXyqfVjrMTTRW2wbupWsMCxxekLJMVnIyW8z8ZU88r8k0GN9EgeMkTy%2BLSGuQElgEssmAKxs78%2BhqUWhuUGIFfGjmFbrVQ0UKZSx7bXo9mwe8wTX1mYvKUe%2BET%2FQRuuwt0BVhrLxXxdN6jqSShAMYCOgMLRrFZrty8n7NQQ6iyRxuYzbU5DOYIC4L54%2ByUt358ORyF4kCW4uAB1d88V2%2BnmnQPLI1l%2B8tgVgi6bwq0d5CtwuQ3kOGBbtn9sOydGHjZmPJhJttTMaj%2Fol73fSgcoh%2FkDVX5JSlEkLWFcEB3LiiJf2N%2FIJCgaSK2aQrEWzZ3ivAVONBP9fTxmoW9YreOfSxXlhkSR9FZsjuyfhjUl2GMiZQjHB1K92l7cT%2FjeWeOnvSroIUac%2FOgu726inG5K4hNz%2Bf9Zq6SXuclIRS3pwRMNmh%2FH%2FA7Fi0QZUE9VtUShr0t6RCGhYpeml8Kv9Z5mdV35iB6iEN02oSkf%2BuFF1IYWPd9gqffFSejWsnLauouapRIUhg059vYuAzrCZxhMSKC5ZvRnEyqtr7BhHUOnySqqK1Eh5vn32FLQ95rv%2FlZ62CXYEq05mo%2BFoq8O%2BGeSKn48WD8UneYbsQb1WIwir%2BAvQY6pgEcg5Ql3MHCCvOl7KUxTQxh0Vihk6FlXMGNmUWuIbfzwMzmbxrjw4JD%2Fia8Cj6FtPecVQONxU5K9gwdEMuuhxnSEfxQH6puzudsQqLwxd18lqOJ%2FomaNXAZQ82QMZYEOGr1KZImil4jrrF4rpy8b6ECj3ibI7lzHUxOxHCPx4J%2B5Ruh%2BXmZYgdK1bo1DH3GSzJDUPvQkGzsM0xpMdoos%2Ftf5%2FDwYWPQ&X-Amz-Signature=2bbfd7948c29aea302189f57e14e59323b1d03b5b1536ca6bcbe7c1ed6415072&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MBVKFT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDx4yy8RObj2jt4BTJ8MWE20An0%2FSCEMdjvGEMTNAUQZQIhALSvbe2KSRZQgrswJI3u7Bs8Ho80cQ3x3ob78F%2BfXkkFKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igztr8pC4lIb%2FtAzFiQq3APzSNbmFXywEMPr0SIIXFnkJs0APr2JvOfR%2F%2BICVdHEoDMDOIz77%2BxVAUCbre3tWHAWeWLruxpFnfxJKtourMi0WzeqX4xkXgi%2F0rhF0Z3vK9Sw4n2W4x%2Fo525i7dHzc1ipqTHGLnmLyrRc0WvEFPSXzzyGSLgjrJ9rX%2BzlofHOPHXJp25WAlMAB%2BM566ONbrK%2B85LhIIYPvjtyv3CmRnReZuUy5DA56ZwZFoHkX%2BA%2BiH3TH80rcTz%2BWCpg28aKcAephebpjfaeflDwfRxHNTi00tVf0pxr5aCgfQG%2FzSClEw403gc4RDND%2FnvVRYZM70KV830wCABBb6c3AKU8ZWfFMz%2FxWytzPoNIbRD93xxLXgnQ1GVs8PZVrothEa%2FJAudD8i6uPcL8SFLJ45tmfHPk2YFmoWlgnw89jZlFaDDjZUR0ulBAspJxFPfddYukkH4ltrFjE3zX04sHX%2FWUm7c7IW%2BfobEFnvoXHdPjUggnjjKA%2B7nwf4n%2BwslzpyHKNXRjAf7WOfDOlbyoFa%2BM1EPBhzdSSBUe46WBSQmsS4C6mmHxu7UPc0tu%2BlKKYJY%2BumQmSCsFM9utZIalM%2FzXIj4xnJ97n1QvbG7Z%2ByxvYOGWi2yuCBBp0Ox5%2FHtqbzC7wIC9BjqkAd46D9GEpK5QgzYPLVmmeVnvIO8U5FVj6vT9qO%2FJD4kOnaQ2uYdCyLnblSK2piV75Zg9FKm3bD27q6aB9DZpOgd2NSaq8eGo8fxgYAHGFZ%2BxB4EjZQNz359oJS7x69m8cdUIKqumWaecUYqhnTnbFUy%2FKgkiq78i85HR8naBj5Bml%2Bs6BJJMcnDE3ZyaUJIODvrJGSs55VXMkE5thLfgb8Yc6%2BNP&X-Amz-Signature=e94174bfeef85036edbe0d81b68533f412783c69340377403fd0c696c99ea7ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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