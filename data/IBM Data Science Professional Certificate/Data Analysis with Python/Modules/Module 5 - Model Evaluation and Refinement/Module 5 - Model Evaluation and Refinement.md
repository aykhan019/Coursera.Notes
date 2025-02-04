

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=f88979275d21484b94cc2c1b72cea216259181b51ec13b26783f6dd9796eae3f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=74674f1938b5a5fe6fae99ce71869303392fcff956448a450a77ba60a1cbb8e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=46af1531f5a32d35b213e44f6d30ff9447c13858432939dd1861756bd5385fc2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=8de41f5af1b28328a4152935668312b00ab5642aea5e5f94d1f369775e187383&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=5547530c99d5fb7f7b1455975edbd37654f5c784daaab0229d088607a0a9ba60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=ec47b01912632a83102fe4db788b1cec148477a4458f715c3f0fef7e3f0c1b8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=00c3f0f6b0089ee5b474975e9a7eb7577bc3eb8284a263927795a843941b358e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=9b97eebcb90bb79c1bda7b14065d389987520a749d56572351dfefccaac2a13a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=da0f6e8490c5bf251cf892a9766656606576e9a967d8e92cf01e4bc20307ddcb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JWFL46M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDHUgae2oT%2BBC8jv9%2BYIkOkA25VGmdvlSMP1RFHDi0ibQIhAIjMe5SuIU9BF%2B%2BNXLEs%2FzvYmgHCnGP5rie274BVKdoMKv8DCC8QABoMNjM3NDIzMTgzODA1Igx5MxYIUbWY%2Bc3MvR0q3APgAbCYObzzP81EryOzRfWG2AlHkEJ1D2J7BBNAjQkIwU4L49IkknoCdrAzsKJp7N7layaWj00scj7pVv6k8xxfHMzVQTuWW39k829vTH6Iw%2BFEl8QbmCG0xu6IkkSdDC7fejfQzfSF%2BXlnCCy4M62lXFQyuOGjcXeLgbmoVGlNyulydG3w%2FEh1A4UiAGzeNlvovxiuOqRIZASDW4J91C6YzHVxz1qPW%2FGCAszoNfwjDiaZL91vYy3H9jm40rutkg95K4OFXoOBTT%2BsY6azuCzF2MgbDr9D2tPoT%2B1c7ZVGQuDZZu44KkI1QlQh6B6Addu6hNbfi6eXIuATFA4BIzeiX0hRpvjJE8zPHazVhxziNdBhNogtZiRYN%2BiPBCE0nU3af%2FDC2zgu8HKlpqERHb9BGZgQH6nUhCqX%2FkCPjYoYHA1pS7V1bIpJCIjGq%2Fi%2FFxLJOCAnBcNY7fucGFPWiZuNlTzDUI%2BVGZ1AFChGlSbEFT6mC2iXfoLQQbKJj6rk1YwChBsaYudv%2BFpDSR3iSZosj%2FMu6iHu0SaViPmG9rDJ1S5HXlrj6dQ7%2BWKDlart%2BPm%2Bv3jF8Q1PHgnECEqNi%2FtCI%2BzxmoTcN9C7DmaXjLwtdC8ANYFS8MI%2FGldphTDCvIi9BjqkActGAjW4auAPJYuQqaKyOz7UcmkGmNkARArd4mMCYE6B0kMCiz8cxTQEOizTKsfcPup9San4PoMX2L4EGb77Y92FL9nN4RSZ03DHdbp4lLANgbFfYcLLIhifHloD9buIbd0WcR%2ByN9tyymdgm1Wd%2Fofq3xedrioT9zf28TVydng0429yE3zEdjJsB8uZY1in%2BeJsiDyo%2Ff79m%2F5tX6%2FBYZY7TuDC&X-Amz-Signature=365548115250b61e7a5903a1afba00270c44a0a08ec1019e3787785541a527df&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JWFL46M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDHUgae2oT%2BBC8jv9%2BYIkOkA25VGmdvlSMP1RFHDi0ibQIhAIjMe5SuIU9BF%2B%2BNXLEs%2FzvYmgHCnGP5rie274BVKdoMKv8DCC8QABoMNjM3NDIzMTgzODA1Igx5MxYIUbWY%2Bc3MvR0q3APgAbCYObzzP81EryOzRfWG2AlHkEJ1D2J7BBNAjQkIwU4L49IkknoCdrAzsKJp7N7layaWj00scj7pVv6k8xxfHMzVQTuWW39k829vTH6Iw%2BFEl8QbmCG0xu6IkkSdDC7fejfQzfSF%2BXlnCCy4M62lXFQyuOGjcXeLgbmoVGlNyulydG3w%2FEh1A4UiAGzeNlvovxiuOqRIZASDW4J91C6YzHVxz1qPW%2FGCAszoNfwjDiaZL91vYy3H9jm40rutkg95K4OFXoOBTT%2BsY6azuCzF2MgbDr9D2tPoT%2B1c7ZVGQuDZZu44KkI1QlQh6B6Addu6hNbfi6eXIuATFA4BIzeiX0hRpvjJE8zPHazVhxziNdBhNogtZiRYN%2BiPBCE0nU3af%2FDC2zgu8HKlpqERHb9BGZgQH6nUhCqX%2FkCPjYoYHA1pS7V1bIpJCIjGq%2Fi%2FFxLJOCAnBcNY7fucGFPWiZuNlTzDUI%2BVGZ1AFChGlSbEFT6mC2iXfoLQQbKJj6rk1YwChBsaYudv%2BFpDSR3iSZosj%2FMu6iHu0SaViPmG9rDJ1S5HXlrj6dQ7%2BWKDlart%2BPm%2Bv3jF8Q1PHgnECEqNi%2FtCI%2BzxmoTcN9C7DmaXjLwtdC8ANYFS8MI%2FGldphTDCvIi9BjqkActGAjW4auAPJYuQqaKyOz7UcmkGmNkARArd4mMCYE6B0kMCiz8cxTQEOizTKsfcPup9San4PoMX2L4EGb77Y92FL9nN4RSZ03DHdbp4lLANgbFfYcLLIhifHloD9buIbd0WcR%2ByN9tyymdgm1Wd%2Fofq3xedrioT9zf28TVydng0429yE3zEdjJsB8uZY1in%2BeJsiDyo%2Ff79m%2F5tX6%2FBYZY7TuDC&X-Amz-Signature=c86bd742a95901d59e20c9768c9574c088ce70b9f8e645e2fc3859ddc0e9b004&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JWFL46M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDHUgae2oT%2BBC8jv9%2BYIkOkA25VGmdvlSMP1RFHDi0ibQIhAIjMe5SuIU9BF%2B%2BNXLEs%2FzvYmgHCnGP5rie274BVKdoMKv8DCC8QABoMNjM3NDIzMTgzODA1Igx5MxYIUbWY%2Bc3MvR0q3APgAbCYObzzP81EryOzRfWG2AlHkEJ1D2J7BBNAjQkIwU4L49IkknoCdrAzsKJp7N7layaWj00scj7pVv6k8xxfHMzVQTuWW39k829vTH6Iw%2BFEl8QbmCG0xu6IkkSdDC7fejfQzfSF%2BXlnCCy4M62lXFQyuOGjcXeLgbmoVGlNyulydG3w%2FEh1A4UiAGzeNlvovxiuOqRIZASDW4J91C6YzHVxz1qPW%2FGCAszoNfwjDiaZL91vYy3H9jm40rutkg95K4OFXoOBTT%2BsY6azuCzF2MgbDr9D2tPoT%2B1c7ZVGQuDZZu44KkI1QlQh6B6Addu6hNbfi6eXIuATFA4BIzeiX0hRpvjJE8zPHazVhxziNdBhNogtZiRYN%2BiPBCE0nU3af%2FDC2zgu8HKlpqERHb9BGZgQH6nUhCqX%2FkCPjYoYHA1pS7V1bIpJCIjGq%2Fi%2FFxLJOCAnBcNY7fucGFPWiZuNlTzDUI%2BVGZ1AFChGlSbEFT6mC2iXfoLQQbKJj6rk1YwChBsaYudv%2BFpDSR3iSZosj%2FMu6iHu0SaViPmG9rDJ1S5HXlrj6dQ7%2BWKDlart%2BPm%2Bv3jF8Q1PHgnECEqNi%2FtCI%2BzxmoTcN9C7DmaXjLwtdC8ANYFS8MI%2FGldphTDCvIi9BjqkActGAjW4auAPJYuQqaKyOz7UcmkGmNkARArd4mMCYE6B0kMCiz8cxTQEOizTKsfcPup9San4PoMX2L4EGb77Y92FL9nN4RSZ03DHdbp4lLANgbFfYcLLIhifHloD9buIbd0WcR%2ByN9tyymdgm1Wd%2Fofq3xedrioT9zf28TVydng0429yE3zEdjJsB8uZY1in%2BeJsiDyo%2Ff79m%2F5tX6%2FBYZY7TuDC&X-Amz-Signature=4c24a05acf70830f25b213b43a12a7c9e4878776cf64a7a9603778488790772d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=e5b76ae18f46fcb67b9f4f32fd5fa3815637ad9950e0ae53df36558ddb6a1b36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=0b2be61255eb3febf2e15cbc33a8f98ace14b481993d08954eba38f4958c8555&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=f198a2c18fb481a6d4882aa105f7e6e29eb24ec99b757474f00d1dbce98b07a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=35edcb2af61a7f72eb23566d4939c5122a348037be6a32ba0c8aac4a0f9f7e07&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=30ae5843714ab55dd388d1ec497ab407064487d2845a081e8363b3bbf83aec06&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K54K4MH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDcwDEp9UmnkI1r4OdJWZ0JPU%2BM2VPnXe8p6ndCi%2FvOXgIgWus3w1oMK2awLsso7PMWJV1u9kAFxxER%2BWcH7oj920oq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDFfNx%2BUXLSKpgVr%2BdSrcA8nWCVgFZ%2F1%2FIQc94xRobdpUifkLVKrqPFizHqLRwNoxNr%2BMfi5tD%2FhSqpQmWFlOAP0qdhMXGxbPD8YGSZP5%2F01%2BkI%2B3XMALiPY9zv9fQouZyqL88yeamSZR0bmNxu6xEvk2ejZL%2Fmp7cWYBgM0gqgVcpZqc6ow8o2fGFgz69mRdnu4DISx5QKejrku1xA3j5AViqpEWwjCG%2BIeK2vwnzon8S%2BKuLyh5sMSGBM1gJpUTZaOphCAa26Ql1pqVrrZ2v%2BipQY5Y6395OQf6EVcuqqMlb3PcTrYE5dLZSjxU5KKYDbv54xSFR4WFDsbpfT35AsguA%2BRq3vn3ectc1utfHBw5LREdgDvCFgz%2FwodMzEs%2FKRB5jHfSEcK0dSdk8LdH9x93hikQqsP7ZNlc44TXQ7N5KjbYTcvCBZg5cVCymFIccrwCabMgkWcgFPm0aiK5ybG8vL7WfoF6QEhyZRtVMvTxlzw%2FjdEVsiwyiOUk%2BjTAsWS134Z2WEFsNyFf%2BuUQAcgqBhs1z8hisRFpTmF0NkuiyZczi%2B%2FSmaL3WnHD6vRiRWqM0VpSvYGXRZk2tew1BdGzfhsbVGpRuDjB1b0GFgJD1oiXKL3Ybf7DR5OR2SYsIIUpLqR9h3d9IPkTMOm8iL0GOqUBiz81VXXi8QiprP58mzO90A3eofP4%2BWj7JMqbfoc7r8iTnjRmVCIL9QpwE6BuIpVgtVqrkmMD566xFJ69wpz8PO%2BC1mYjiCFF0yKteVAFm9W7B2HOzF65e%2BzWnDbW6L68%2FGeDhkJVdOxrCAuMK8CDTh0V8t%2Fn68SjJZCkigRc9RHocsrcCS44zyBY4g8M%2FyP%2Bq84CvNTK4vaGC6aTk6cawrQed4CP&X-Amz-Signature=c2508dced1fd9eab509bade13d0b7ae6d627ba253462784eb4c755714789b54a&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AAW4Z54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIENgBHQUcQIMIj9WfOTnCUrmGyNaCmeRVjxDQ%2FAZTPfRAiEAy3RqxEx3kMJdPngmrVaYYJ1wQ5ppebhNBV1TjCpEsbgq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMYEC1%2Fvl4hrWcMupSrcA0aUWEW2wwjojr5%2BlcErlW8F%2BPUvvZ2Re31zEKwoTPfcl%2B%2BpaziVVOxIbsynvmdptaxMvfjRjRgMBQJyPsOQsKDaoGYisa17e%2FvvZL4QMrX8xtNYoiesRMu2fU8d0FF6aeMG%2FLwJw5ZCZ2yyOkShXxD8N818i0uwPfFk%2Fi3h7YGxf53NrQUDwzqpB2gj29NOA1gq%2F5dbLfe0LHtQ7p3NI4xO2rd2%2FSUr2saehrI2Z4yyjSlX%2BnIu7B3VmpqFP5FCNsjYuRJCumrpn%2FeJmANLCOlDRiGG0bh0Xbe4kxjNx2Ov3MHIHFjNvvr%2BnMYHTi5mVAAhBU28QKL9NSA1JxwyvTCee0LbWaOAEzA4szk9a1ATPkXxJwQaothBTz%2Bi37bNWBU2qHJ15736UedVIsOngMkxVTEfbIY6W3XnJrT0S1HH830p2vQSK6yn3znJQl6FdtYrnt5SCasKqQzjjAbFizLzMyi0Mtx95%2Bi%2FKBeSzJ93f%2FaT8oR9bYzxDF8Lu56LUhNs9XjLMOXJxIb%2BVjSna3h7xzxjlbgw8GXpz8c8WzL2ujv2k9XKfvEgqaLj6LZ0dJAmeThKDF%2BJOIWFIsnqfuc6sIgawGLt9Dt6WlCIxQM0kmizYFxeB486bd%2FdMPK8iL0GOqUByZw%2FlG%2Fa2HO%2Fq1O7YZJR0hhP1nqJ9ERxpXvWZc3HP3sB1Sb9iZwVm9Ssh2ubvcFyyM0PIZFO3DecHPFJXVrj8JNyPSv0Rt7u4%2FSmJBNvMKubxrEg6bw3D7MMrW8R4imM7wfijkDW6O%2FQaCw6FwJbyvAkssRUb2SRK62UIYRyfEr%2FQQfW5YDnn7u2RHgEQl7eRwU%2B4aCRyQuuyr6ZftiIQLHmyiiR&X-Amz-Signature=dc6ffa6443de72853c5797acbc5190a11efebeab55f8e09a0b98e4c2c78ca8f2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AAW4Z54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIENgBHQUcQIMIj9WfOTnCUrmGyNaCmeRVjxDQ%2FAZTPfRAiEAy3RqxEx3kMJdPngmrVaYYJ1wQ5ppebhNBV1TjCpEsbgq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMYEC1%2Fvl4hrWcMupSrcA0aUWEW2wwjojr5%2BlcErlW8F%2BPUvvZ2Re31zEKwoTPfcl%2B%2BpaziVVOxIbsynvmdptaxMvfjRjRgMBQJyPsOQsKDaoGYisa17e%2FvvZL4QMrX8xtNYoiesRMu2fU8d0FF6aeMG%2FLwJw5ZCZ2yyOkShXxD8N818i0uwPfFk%2Fi3h7YGxf53NrQUDwzqpB2gj29NOA1gq%2F5dbLfe0LHtQ7p3NI4xO2rd2%2FSUr2saehrI2Z4yyjSlX%2BnIu7B3VmpqFP5FCNsjYuRJCumrpn%2FeJmANLCOlDRiGG0bh0Xbe4kxjNx2Ov3MHIHFjNvvr%2BnMYHTi5mVAAhBU28QKL9NSA1JxwyvTCee0LbWaOAEzA4szk9a1ATPkXxJwQaothBTz%2Bi37bNWBU2qHJ15736UedVIsOngMkxVTEfbIY6W3XnJrT0S1HH830p2vQSK6yn3znJQl6FdtYrnt5SCasKqQzjjAbFizLzMyi0Mtx95%2Bi%2FKBeSzJ93f%2FaT8oR9bYzxDF8Lu56LUhNs9XjLMOXJxIb%2BVjSna3h7xzxjlbgw8GXpz8c8WzL2ujv2k9XKfvEgqaLj6LZ0dJAmeThKDF%2BJOIWFIsnqfuc6sIgawGLt9Dt6WlCIxQM0kmizYFxeB486bd%2FdMPK8iL0GOqUByZw%2FlG%2Fa2HO%2Fq1O7YZJR0hhP1nqJ9ERxpXvWZc3HP3sB1Sb9iZwVm9Ssh2ubvcFyyM0PIZFO3DecHPFJXVrj8JNyPSv0Rt7u4%2FSmJBNvMKubxrEg6bw3D7MMrW8R4imM7wfijkDW6O%2FQaCw6FwJbyvAkssRUb2SRK62UIYRyfEr%2FQQfW5YDnn7u2RHgEQl7eRwU%2B4aCRyQuuyr6ZftiIQLHmyiiR&X-Amz-Signature=a6edfaa906415f57e31d6e62a504c364e35e4ecc9019e1692f7ba2d7118e1eac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOHW6KRC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIFmfkfrzlcWWBh9wf68H01WGsbheukXKDouXHSkMoTiuAiAqx6g351QsBJ7b%2BebXAMORQ2EwIl9B5qJLBUOTXQL9ESr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIM8nN3iqP5fMZgTYvlKtwDGvce0s39w80RqqF45z0t0OZcHrTsmrnd1rGt%2B48rRBYh9L4kG74%2F4XyyzRbsB6XCZnIRdOY27%2BsJK5XUpLL%2BsdcWthPRA0Bpg5MAq%2FYy5SktI73o6mj9xKKf3LKBHvbvt4szQ3aa4GWFzmf4aKf1NVwsNccJBYKXNOq4B6%2BVQu0wvtK1szwTe3Qt2rRxtVs0a4vXc5k5OEWx1jHXvwplyinB0nNMhc5C3F9DrHnBWNhcb2zXDAgoryJeb52v6hAYL9NogvX1Hf7C1pvrYyfWTeCSCBOzTJO5eoGQVvtR1QNEPjKv8mEbLCT3TJeYS%2BIaIVc80jsftA%2BXnOVyksXE%2B91KpsJNPZ3FfBcHtNlhWXFMfoYCDhKMGASb9D%2FpvLtwu3sczqwtkWQlP7%2B%2Bb0e39IlnxUDZ2QSUm9btQZ5OW8qiLCVeUQvUsKBIG5LW%2BHyC7oxXWRPPlrAV9fvaAeQBeRHJRx9V3Belv9WI%2Bgu2jnf4hdABfI%2F8pY%2BClXEknAW%2Bl31LsI6hst0woGIpqXM2DhKt1D55xZ6OMGFMAW8LZm7DeUe12o5tnnFvYfMbmFdba3f2W49Vy%2Fn7iVJ%2BpamQlJR%2FOUmAV6LcAFz4D9QN3KZuf0V5vO2w12gW6dAwvryIvQY6pgFmZS9X9nT4T33J6Ufo862Vd6fUuoMLMVfOMbITPQPXXI7bzbJgRR%2BOzRnb%2BzNzJQR6KHtnK0UKY%2FKHvOCy5jVhzHDh9%2BCCItnIjOntKzGHIzuw%2BDPdK3AWT6ThUxvDNbZnGseajwY9KgBkalt7YC7UHlOv1KUy1YZTDszhKKmxcZ%2FtaVxKtDOwV2PRmLLG37jNf50jAwYoH%2F0lUWK1tg51lGP2Ifyy&X-Amz-Signature=1a51e6ccd50725342b9ab9484fc5738facd5903edbd26405625cc77c9043e2df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPT6SPLO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBmSVcMRcsEwRmLBW8noT%2FhvKWv1AT8KkB6LCucqwmpvAiEAna3SbfyhRfC3aFrRxY9NEy%2BXBECyA2LjAnfPQ3x7Ukwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAEJlB1RxIH92WJqlyrcA7h4Y2Qh1A5g%2F1vgQEO7S5wTmrXYRcYw%2B2lSaJkozwIuIVwmAGl%2FEewroWdp919fZVmhfN0tXNAZgIxXWVQxVyR5Rvutjj00BDSoHNv4SRdc77umEFWP5KXEx4jOepF9emOeATUtRk%2Bj0iHQagbdJ1wcx3xTD0jy1wPVUCXqWk2L7TWA%2BLxiY61%2BsujexlU0vVQ5gGvmuXUXW1hGyuHnRbI5xU1X3yE2X0Is7wGX%2F1RoRqqmj9tAr9KdXY88q%2B9SMeZ%2F7ehEe%2FNCGumHaGruHhElqFM4WhCirxFoG8Oi36%2BX1ysQZnhKzSPAtvsSxQAjdQMgTnGpE52QoxY7cvRUHaG4sKCxI%2FrIUSM5q%2FwrvmMp18Oqarks7NKxcV0pA9FqVj1AdIIQ52mo7VO8R8kcksQ2TvxIzwvSSkSXqEZpUNZkHSyw03rAHxqsyHMcyfQgzUa%2BjrlqTqxTEXTiFyd%2Fw3cUuoQA8bV4cFeWxtOL2Yt1DxTCCkxz%2F1H8fb8qF9R2jMUGoop3CWqEeBJ2dniuVn%2F9kbbZ5rKEVVRyqB20lUQlCOdCUxAnIZt0%2FDSguM%2Fa5r4wZrsQMPWyUr9kmk2tmTBvJSSzejrg8O%2BQTmEWRNnU1BNPv9ubgXU%2BrZyPMLS8iL0GOqUBgKlnmj5QKY%2Bl7irbHeqrbs5u0ry4bdNjXFgE3GEV3S870VM8CTOkbtSjHg9RIPTgl0I6oB34CZINoQzp2sh9qEPbkSIHx4eniuXlOj7qZoOurtMskvisEgEhBHVFhm6RDJtF6uxx4cb2KeV8fc2ClplZwJjhqD1F26tzVFgT9vOL6uu1jYLnSAWCryacqDwwKbpcR21zGy9%2BunJJsH7I7%2BcIDQyx&X-Amz-Signature=f896c16cb08b64b7093379aec95018e13ea3c22d48de63d4fce0aa0cc5aef589&X-Amz-SignedHeaders=host&x-id=GetObject)
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