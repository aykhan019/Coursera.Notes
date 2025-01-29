

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=6e4349fdc8b3f828401494ac8f74605c79bacbfde64000d00a5ff0156090947b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=cf8cf8224d564878b818543ef0ad3b44287ea90229556be62f8f0d5a2cc0367e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=f486c40bf260f4ab4ff8cf1248efae9581e5ba3f043a199ef259a2ddbefc8c42&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=5fdf9da182203cb0ec4fe1d726d36c539f71e9afd22e9b38877549fe2b37bd81&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=aa4984aead6b5420be5927b389e4dfe3f63f365deed98b2edfdd110abf4b1b12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=60cf631887c717dfe1d3369cce8c9249ba13e8effe88b1f36cb55d45e6da0b65&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=244346284bc346f182659bf8a5e7d62c29ac668573de2ffafeded323df49ff75&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=9f46cafec67ca5fffd666fb1b2802580c50f474fd6ffeb1b4cf8a8c30ab2befd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=2cd0eb0dd6bc143fb4872b6d07d531593b621fa839245eb40a2d3206116da9d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBOTRPXJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD7laDda1oy2hAgkm6UjD5MocomDn%2FZLM8ZgZO5uiPbOgIhAIvLD8D2eaRKtRZPaGvyTnaxOFJTQ8EZLdw0U0L9iVHOKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNMRTkTDyFbeGPA9Aq3AOZPq7f%2BCX8Xgqax83zFeCSyVGBz2fp6dUeXnKsyRdtws3%2BIvLhhpLrgbYFrcBnhnAXy%2BpkIsCuavfeWZhYXMMfrgVd01FnDphHYefnRh2Tc7DdigMlAI6GtimpGrLrScS92r10YJDfgpRUgTUhCPssaH4VBZAbQZChcFvhFZ5M72Vo%2BHlKz86XRl3HKViNfP%2FJRHU8mt5LjvRsW3HuCzVjURwZAf0viozKXwRqru1LK0mVcTu3%2B4mgI4i4uNvK8nQaBKo7BB9%2BRIyNWjVhNUkuwLtCaybBF1GGOllsU6ldOn%2FyIa8TO5VUdYpiRxitkMVYynX3Yu%2F0q1rmtl70TgR3IW%2FVy1njwwQ%2ByUu9cMf%2F1rkBCxSSQVZGNJbPHe9k9XJ0tvvBJ8xJyjXF1JsUs2JBVim72aEg0%2BC%2FJamDBwbBn4DkTagnr2ILCVml%2FPzEtMGXybIiGp1wq7oiH2u3V2Ro9q1LyryqGPCHUqtOBncYCo24nikhOB5gL47JhtAp1cKbyzu5JR%2Bb68ozx0Sao32xlTq4rqkoFS26KwA7XgR1PigUJHOL%2F6pFwV9ZmWfquhrVDoFpNC2ik10S4F6YqM2XStEpzstxZKAUojo%2BDuy6g13jCu5g5intDYMN1DCHu%2Ba8BjqkAU9fdajrzPkkfv1maFa%2BvXr11%2FteM%2BHfp1DLJYfdw9caXYl%2BPzLd6L2TN8DjBXfHROqRm%2FlmkfSnUA4hdDVmBFAnyRsZUAc8JVBZvAmL5m4S4lRsoZd68pqMqycqfEcPDb0Y9SWuROP%2B1BIisyAof1o48%2BxSO7GNsntC9VJY%2Bc3viNXK5njAiytAj4NC%2B6c4N9xD7jdnC7Ie3ajOhsVPHmJZ98Mk&X-Amz-Signature=0feaf4fb95b88ab3e460776190cd9460fe7c923416ad53ff431e6fed417dad9f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBOTRPXJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD7laDda1oy2hAgkm6UjD5MocomDn%2FZLM8ZgZO5uiPbOgIhAIvLD8D2eaRKtRZPaGvyTnaxOFJTQ8EZLdw0U0L9iVHOKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNMRTkTDyFbeGPA9Aq3AOZPq7f%2BCX8Xgqax83zFeCSyVGBz2fp6dUeXnKsyRdtws3%2BIvLhhpLrgbYFrcBnhnAXy%2BpkIsCuavfeWZhYXMMfrgVd01FnDphHYefnRh2Tc7DdigMlAI6GtimpGrLrScS92r10YJDfgpRUgTUhCPssaH4VBZAbQZChcFvhFZ5M72Vo%2BHlKz86XRl3HKViNfP%2FJRHU8mt5LjvRsW3HuCzVjURwZAf0viozKXwRqru1LK0mVcTu3%2B4mgI4i4uNvK8nQaBKo7BB9%2BRIyNWjVhNUkuwLtCaybBF1GGOllsU6ldOn%2FyIa8TO5VUdYpiRxitkMVYynX3Yu%2F0q1rmtl70TgR3IW%2FVy1njwwQ%2ByUu9cMf%2F1rkBCxSSQVZGNJbPHe9k9XJ0tvvBJ8xJyjXF1JsUs2JBVim72aEg0%2BC%2FJamDBwbBn4DkTagnr2ILCVml%2FPzEtMGXybIiGp1wq7oiH2u3V2Ro9q1LyryqGPCHUqtOBncYCo24nikhOB5gL47JhtAp1cKbyzu5JR%2Bb68ozx0Sao32xlTq4rqkoFS26KwA7XgR1PigUJHOL%2F6pFwV9ZmWfquhrVDoFpNC2ik10S4F6YqM2XStEpzstxZKAUojo%2BDuy6g13jCu5g5intDYMN1DCHu%2Ba8BjqkAU9fdajrzPkkfv1maFa%2BvXr11%2FteM%2BHfp1DLJYfdw9caXYl%2BPzLd6L2TN8DjBXfHROqRm%2FlmkfSnUA4hdDVmBFAnyRsZUAc8JVBZvAmL5m4S4lRsoZd68pqMqycqfEcPDb0Y9SWuROP%2B1BIisyAof1o48%2BxSO7GNsntC9VJY%2Bc3viNXK5njAiytAj4NC%2B6c4N9xD7jdnC7Ie3ajOhsVPHmJZ98Mk&X-Amz-Signature=b91192f93f30750a690bb876c571de2953aaa043e87cd40d9abec8d8aec27393&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBOTRPXJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD7laDda1oy2hAgkm6UjD5MocomDn%2FZLM8ZgZO5uiPbOgIhAIvLD8D2eaRKtRZPaGvyTnaxOFJTQ8EZLdw0U0L9iVHOKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNMRTkTDyFbeGPA9Aq3AOZPq7f%2BCX8Xgqax83zFeCSyVGBz2fp6dUeXnKsyRdtws3%2BIvLhhpLrgbYFrcBnhnAXy%2BpkIsCuavfeWZhYXMMfrgVd01FnDphHYefnRh2Tc7DdigMlAI6GtimpGrLrScS92r10YJDfgpRUgTUhCPssaH4VBZAbQZChcFvhFZ5M72Vo%2BHlKz86XRl3HKViNfP%2FJRHU8mt5LjvRsW3HuCzVjURwZAf0viozKXwRqru1LK0mVcTu3%2B4mgI4i4uNvK8nQaBKo7BB9%2BRIyNWjVhNUkuwLtCaybBF1GGOllsU6ldOn%2FyIa8TO5VUdYpiRxitkMVYynX3Yu%2F0q1rmtl70TgR3IW%2FVy1njwwQ%2ByUu9cMf%2F1rkBCxSSQVZGNJbPHe9k9XJ0tvvBJ8xJyjXF1JsUs2JBVim72aEg0%2BC%2FJamDBwbBn4DkTagnr2ILCVml%2FPzEtMGXybIiGp1wq7oiH2u3V2Ro9q1LyryqGPCHUqtOBncYCo24nikhOB5gL47JhtAp1cKbyzu5JR%2Bb68ozx0Sao32xlTq4rqkoFS26KwA7XgR1PigUJHOL%2F6pFwV9ZmWfquhrVDoFpNC2ik10S4F6YqM2XStEpzstxZKAUojo%2BDuy6g13jCu5g5intDYMN1DCHu%2Ba8BjqkAU9fdajrzPkkfv1maFa%2BvXr11%2FteM%2BHfp1DLJYfdw9caXYl%2BPzLd6L2TN8DjBXfHROqRm%2FlmkfSnUA4hdDVmBFAnyRsZUAc8JVBZvAmL5m4S4lRsoZd68pqMqycqfEcPDb0Y9SWuROP%2B1BIisyAof1o48%2BxSO7GNsntC9VJY%2Bc3viNXK5njAiytAj4NC%2B6c4N9xD7jdnC7Ie3ajOhsVPHmJZ98Mk&X-Amz-Signature=754975a41107660ee66a98e7180f26f551f4ecb1944622d4b85dc1ddb85f5594&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=87051c40e74d965a90e3375cb5c2eea8a586f3e6de23c0e188d81417dd8055ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=bac677ec65c6a3efe0faae1e3a286086e3421506464a9e14030a26913bc915f3&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=927ee74a8603e313f394a2191f3b29d371cd7adf3e546b56fa521d62881f385f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=b521678777e3e1b5b0413181c6331fe17f0d68bfbfdae87542748bb996037a75&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=5a8528f7138d94e0dc7c1a4ae4879687f615e3b864b418acc26a80860e74008b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QND54Q37%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIBu54EymTcW8CDM8v0VVlB0mYSS%2BfMllJvRl%2FVSZ%2BZr4AiEAhbRW%2Bg1t18aBVBhpEWOiTReAzg1CRkRTbWzoXT9%2BD6EqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBtyZUvotXDuHMFatyrcAxlY6vo%2Fp89D%2BuU6hB%2Fb0ngFiaJlEIdjYxHmZTnOU2XO6cgM7jVn0Fn3hFRIoJLr3ZrEPhMDzf8unjpu2cNml4evDZz6EgC6o4wgVWy4%2FTTnSH1IyvxGxyn0kWClGoQU84zHa6mSzFo6HjZFZQFSKjJC22SMyLNyRL1BNiKJz1%2BM4AgGA69cgWmM2k9cM7vg2M4ymayVWn9ax2z%2FYFDD8M332q1kRhLGktjCEJ47UrVRPiS6EHbu7aDNcSismypwhfyp1l9C7FWpehZBnbIYC3ktv%2FvIAh%2FvZJ19M8wnBVvasW4iETLnic2oTjVQ9VCHSEXPsgbw28xCw8Vqiwzx3uCCycPbr5WJdVpTuVe9gzgdTFAxcJphodraPsAyImacQTmDZC8pVVFhwYnboqouYr5bIbVzX%2B8L%2BdyoHZaYQ2FHlU%2F9lx6r0qA4YSmDGXTSu2dbCGRvjGAudPIuUdtOxjNoKlTLy1VjdnaIyzgMmg43uWjrs82mdCLOrGAdk7OXF93EM3eUig9QSbiSE4r4dCuG61jGpXkawWRZzT643D4ShD5LSX8pa2fz461EQF3RM6%2FzG6ppErigEY97EQ8luE13Ny%2FVuIx8tr1%2FJ603Un24ecLK1D2pYrVM5SZwMKm75rwGOqUBVzbd2ULKkCb2uUMJDOjjLzzv8wotqvT2YcFw4D6XAynAGmhr2vvibhjGfLfJO5qVuNJduvK9nr%2B8mk8ZzMjc1zkcsEocuaWo794ftB8dJ0gVBTtoxssIbVwBSIekO4VrVrM2aDD4yLFM4DPNbHpGGGpf9KqI%2F4CZCAhkcre0IRZeJkiWa17LKzdKmH5UNZEocIhfMh132JOnta3pws5VxX%2FVsxLr&X-Amz-Signature=13d74a4453fc769fa2b775c79fc27be3d29b4813446480d6b7f8bf177ce54a2e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTI4S2Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIBcyIAbldlKQms1%2BgbccFUn%2BecKU9%2FblJCeqRuBz5wvKAiBKUm037MG5PLpVpNhtBMZrCQ%2FoX%2B1xk4BYWbvP59FJEiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlO%2BiOmOYKzRxdTBtKtwDHnl8k6r%2BJod6ARPFknmMgasmr3BUTU7HZmuKJfgEVd07tscrioav%2FK4HeDn6GCVDvws5ax93sVflxX4M0rkgpRqE3aZ6CmtuE4D2oGF77Kzq%2BkNLVA%2BGzfmylK4c1WNTB9DpEXE6gBMHMQheat8ie0dfLyvWIwSHNDfJGEuHQjhtO2SE2rYau3cqsuZxOevHL4bC4t60AY7FMOS0FhXfGR%2BoJtRozWpMAPH%2B7SRdtddIxON9P%2Bgp4vEJnrgEbmpKceR3MYDw0VE8G0fasqj74WhtFKqKEBy%2BNPYBP%2FTDZ9jr09EkExGnPAI%2BIdBp9RCxC8wKRpqtGvdJzjTjNzcVHLDi1AoqaoRZaseS54e0VA3Ec44wEpHPelpp9T5%2FOR%2FxICAm%2FAaYBsAYPGsAzyheaTT29n4R0x3DwiV6Ktk3H0N2Hm06vSDhlutIOvNXOtO6PiJ%2FkB0%2BvJx41mZJlL4DVgYVHe65Gc2Zg%2FAt6EjGD%2BeuUgPmSM3d5JijXKPk9KoTgzahKgAD9C6OiOBTzRrSelS85%2BsOwjhNzHLf%2B0VWSpfCNJzk8B3kEqdVMwWSWgSGFjTZKq7iGdu02nm860d%2FP4%2FHJv2UyMvRQ8oyy8AP4ePQu2TjcSmy0Jx%2By5Uws7vmvAY6pgHpEnzp94CO5A7Dzao%2F%2FzkzbC5kHLHSIwtoWnOMszqNrk0ROGMQgTzqLbcAduRNzU6TlkVhxBHg7xcSmGFlKB3fCPHXxKLILLnV%2B12KWo6m9z%2FUlRGQJ5gD7J24rjWK0DBgw9fRLJs%2FkjWoXdpCP0fn8Ji4xY52MfeNnfNMH29QNLjz9dFEJ0gHLWJCRovRU3QY1JB6Rql5K0KsadA8nHH9Mfuk8NFl&X-Amz-Signature=8b77db939997fb80b9933a2dd1032de78f541ed08fb2825dae19207cd694d3ad&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTI4S2Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIBcyIAbldlKQms1%2BgbccFUn%2BecKU9%2FblJCeqRuBz5wvKAiBKUm037MG5PLpVpNhtBMZrCQ%2FoX%2B1xk4BYWbvP59FJEiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlO%2BiOmOYKzRxdTBtKtwDHnl8k6r%2BJod6ARPFknmMgasmr3BUTU7HZmuKJfgEVd07tscrioav%2FK4HeDn6GCVDvws5ax93sVflxX4M0rkgpRqE3aZ6CmtuE4D2oGF77Kzq%2BkNLVA%2BGzfmylK4c1WNTB9DpEXE6gBMHMQheat8ie0dfLyvWIwSHNDfJGEuHQjhtO2SE2rYau3cqsuZxOevHL4bC4t60AY7FMOS0FhXfGR%2BoJtRozWpMAPH%2B7SRdtddIxON9P%2Bgp4vEJnrgEbmpKceR3MYDw0VE8G0fasqj74WhtFKqKEBy%2BNPYBP%2FTDZ9jr09EkExGnPAI%2BIdBp9RCxC8wKRpqtGvdJzjTjNzcVHLDi1AoqaoRZaseS54e0VA3Ec44wEpHPelpp9T5%2FOR%2FxICAm%2FAaYBsAYPGsAzyheaTT29n4R0x3DwiV6Ktk3H0N2Hm06vSDhlutIOvNXOtO6PiJ%2FkB0%2BvJx41mZJlL4DVgYVHe65Gc2Zg%2FAt6EjGD%2BeuUgPmSM3d5JijXKPk9KoTgzahKgAD9C6OiOBTzRrSelS85%2BsOwjhNzHLf%2B0VWSpfCNJzk8B3kEqdVMwWSWgSGFjTZKq7iGdu02nm860d%2FP4%2FHJv2UyMvRQ8oyy8AP4ePQu2TjcSmy0Jx%2By5Uws7vmvAY6pgHpEnzp94CO5A7Dzao%2F%2FzkzbC5kHLHSIwtoWnOMszqNrk0ROGMQgTzqLbcAduRNzU6TlkVhxBHg7xcSmGFlKB3fCPHXxKLILLnV%2B12KWo6m9z%2FUlRGQJ5gD7J24rjWK0DBgw9fRLJs%2FkjWoXdpCP0fn8Ji4xY52MfeNnfNMH29QNLjz9dFEJ0gHLWJCRovRU3QY1JB6Rql5K0KsadA8nHH9Mfuk8NFl&X-Amz-Signature=a8ec66a7e115375f77b25e568df2fbebed723792945d23c42a97c5f92cb57476&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJBW3WJ3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQD2jxdBN0PQrPNKNFdfFYnK4xMfodAKqlMn4N%2B4VQVIXwIgZvFAp%2BFJN1l%2FHKmVU5yaFZJFnWL6ODHLIY%2F7ZaQtlVwqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIeGvFWT3%2B6lFbCQ0CrcAxff%2B8VldRC4tHL8sClBJVXLB8loeowm84JAr%2FWU4FossrlZILbWPGzE25hyEeJPRpsQY%2BmvA7A7dUavylSjPZEJBKOiWN3jxPyp6NlMD6NSViJqKlze%2F1Z6BVJEvaxczz0NAklBZAtsizwhR%2BtvCda56lIN%2BfWiah4bajq5tSklw21zKljG0y9LwfrtQM%2BB%2BlfrxUxlVoqwefoM%2BZeMHUtuIUYWMDFPyCd2qEw1ClKLqKPVSMQxj%2FGPWeId2K4NOrh8qw4MUtNLmV2RyAjAP8PSvcGGj6N7OGZ8KwEXfZUTVT9e6%2FDZLO%2BQeDhLKRaf%2BkHQz20m6GbEWU6ARieL7Em2OmLurJ10e23ASvRXq8iNKOxY0q5kW%2FrtaakDQ8D%2FOCsC6AiaEL9IMXW4tfZKcFOUd2D5OswUguFmHuxrAqbiMxpJV%2F38H%2Bfj%2Ff53pZ0SjzSUz%2BWixhHsLMovqoRM76i4GibnY3bGj9d7O1skrBunyNw3nv6hiGcbmr19p16GII%2BxDzyfHcAofiJsKSfn5kynvXzsWLSv4UPQGgs%2FhSQgF7PLJoQg0L%2FOp6uzVLDGp18Wl3JJtO4m%2F8K33gW2j8mkOHAf9Noe2sMRNQ3VWAeajJLQmHt%2FQZHQrPICMIOQ57wGOqUBeNokWWX0quOsef4veLY7xAz5Iz7gYPkyvlm5lCiloEs1ZFH%2BmUmjC2sAjZOmwXoXE2wLgAAvWyMhoGU1Q6acWlDO%2FcvxcPkEnCFiCL8aze8V9iTP633Ih%2BZDNq5qxgkx6miwoLAYXbKPl%2FlWEj7NL0JmzfpJ3C0h0rilFnY9RRGi8H1T4ThElfdF3tOLCLuOPV8CCweYEF%2Bdofr%2FAFRFYOwnY8PR&X-Amz-Signature=b643764e6fdcbbb4ce3f831563fe0480398cbb3c90599c7bcc3c09a0682bd74d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGX6TSNA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHiL74%2Fil3nMELZjCWRluZ%2BzibFrhT70iJq0%2F5knx%2Fr0AiEAlGxN8xPwxKW1%2B0SmSZ4ibvuvU8y%2FKUHPbx9JA1ugusUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxsJA0xJiqG%2FCORiyrcA3gqh1NtkZ%2FYarPB2hL3a%2BZWME2MsRnRAFxi%2BmKEYNtNu8hAbyeeCEItTJNNMjK27o3Oqr3y%2FKAk%2BGEvaF2HGYIq1K%2FYOa3ehPYQfdS1Zjy229LgQyZapQ6Zjo%2Fv4NWxIq%2BiTRm%2BP7py8D%2FHzOX8sD5NemdUtGtdxJMxLhmSUMEssxNaQ5sF6VnReEG5w7hhUMgE0A4DaZPxTLGlpEY8MPGD0%2FxmSbY2YcwDp2fvbgi8aRJXnZo%2BycLa%2FZMW%2BAy5TAj2QWoWcj3mOWXq1prE30cs7sO57vP1hahlV1VGGqqMtE88BsPT0itTHV%2F2Jz%2FHD9Kx%2BtAmzWfk2mvCUZZv4mqnAuNzBa3g0Ry6k2s3IyClzT7wYILpKS7QzIjUiHhoYbgAr%2B7jJ%2BXgrOSnKlAaHJgIrjPKQiFt9jgdISJaFzPur66NIbMCuB5OvWHIaHnnfrV0fKTZMssu7ePKBwxu8PPdtzbHkkQOfu6HTUiF0csLcidudo1SSsQfM%2BI4%2FIiEpMU76gD2FaPopYX8uc62c32aHc1UYkqND1PW2QVBEd81pgJUIzZW9FQgWAY5ghMvoNCN0PgsDaE5E3DPxKydg6NDaCxKZUHnDy8Tdhs%2B9UliyvNfQBRX527U3H7UMIa75rwGOqUBKfGuGRRmdI7Ai6EJgz6kA1k2DdINWsIa3QEjGWZ2yEkBYIVQHG9D0Z38ZXjphLKOQx7ecswD4FiinPeHG1iixVyiv8w6%2FQGWkiczvwL%2BqlBzXBfqmRfHN7wBpUnqB0md2yZeA1XV89oWiJyio9gXZEvq3QmSDYGxFSUZHAiLEgRFP6s9mSBBR09OzvyH%2BEz4enMUMskwTgP0fLJ0yqLKnRtKqcA3&X-Amz-Signature=fc836cb04d9288c29375e428f9dfface98008dcc6c36a8508759910e40ce513f&X-Amz-SignedHeaders=host&x-id=GetObject)
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