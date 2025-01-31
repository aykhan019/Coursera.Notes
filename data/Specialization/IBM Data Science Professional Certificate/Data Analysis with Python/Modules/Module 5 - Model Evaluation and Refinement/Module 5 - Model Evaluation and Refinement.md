

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=a6164bbeee01538c761f4fd8e5c598c558fed43b3613de4e41173f46e83f7d02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=6628dc128bbfbbd7d13c82096ef26dd62717d43cd050a3d6cc33c36dabd2defd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=cb3ff175c8acff005115bc04d0f3bac2b7a499a28c085a678469bf52c8dc1e9a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=1893f7045784d9db8587eb438ae663f3810fe0490fc4bee735b2369b52e34f66&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=ff7f424732614e3845f3d4e66243ff4cecfc3f70a4be1c9b22cb92ccb4d00944&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=86e7b95ff44f3b10fd2f7b6b29f55194c8ec433faf795ae48b97b0735582482a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=08c95889aad8c8519f2b9396552b302c4016e6604f9466d8267fbecb62db2161&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=050e1b9d5350273f91b161f4039d4a8ef10bdfdda074447246827533edf500b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=7b107d6db80057909332df4de06727fffc602430994cb30b6ce63e2f090dbf06&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGBG2Y3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy037Y5P3%2Fuv%2BNBcnHXnNAXRkyB3CVTEi92ZIgFxr%2BngIgIRCUgKOxAqzVZZFO9ZraTZrY%2BNo1wTDLdLm0g3w8yWsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOmIno8muQXhAEPuyrcA5xdX%2Bc7yIJlUCzfMsloAHRVtc0OobB1dfyMiilXQt0UllD%2BtjwBVJR9go8VEluXvd%2BpPGbzZirvD22q1Khh4IVMC%2FuB7IgBt0H4C5CVx0snxzAuzC9WGQ9DU487Qk8LwVyRvYhyHs1HtSsCTVe0Yx6HFLZT0h0CIcHDxhHPKXGI4PSQQeD74UCDLUxOEHRS0teyimhldq2kVOGIghtqRZyqK%2FFRqCXPgiSv1J0Hcf%2B%2F1cdRc25GESCSAkXWCjTPTyhbjwDi%2F36ANCT5hxH1d73zIZrcCmcmKAJr3ecgaTEEf2DK2ReLpve3KFutHD8nhXOfGH1f9uYYzC2vVHbciiaWUfEOy3y6kkUNDp4Jz9nLor%2BAFtEGbVO3Z4%2BSfIZQAYfNF3g4ATJ%2BwBeU6d%2FSW9S%2Fy%2F%2BrPHkpFcMgFnxcA7rIp%2BXqcjnBwpZ1oEbmHYkJNLOCXEiCQa%2BbSlOQX%2FHg9xmNAU6ampJTm4sGgsK%2BIu0OnUQgTRJ5v3J3tD6NvWMQXudL7acpJwp4ffuCNVogoiejTp%2BQwAT8cwM7tra7lQlqJwtLK2V4u0dbHIv3At3AhA%2BsZq9VByJeXkGtBsry3cmy5nflGrEjj8EiIiN4OlHVhUt5yBFWwYOLJkgMMLq18LwGOqUBUZ4t%2FrirZ%2BLV%2FbNkpqRDCqLnh4j9feSfOPVtRk6SC8hZGIv219OUGovp%2Bzvb4eo5Y9oiovhl2uz69Z1vwSMCnT8VBi%2BjIAspuBCEul1TjxUAXj5%2FC0Q3brOsxSetZKcfYOmm8aRfrTYgU9CFBIkRCxSNAwLI2E7JWS9HmS38AOxhtHodftEUe8OStm0UBv%2BTImJBF0eroI4s5oUh7nDVWymtTydW&X-Amz-Signature=a9f099a7675875854569d2b75047990786bf2781590f675172c7713bafe2cb4c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGBG2Y3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy037Y5P3%2Fuv%2BNBcnHXnNAXRkyB3CVTEi92ZIgFxr%2BngIgIRCUgKOxAqzVZZFO9ZraTZrY%2BNo1wTDLdLm0g3w8yWsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOmIno8muQXhAEPuyrcA5xdX%2Bc7yIJlUCzfMsloAHRVtc0OobB1dfyMiilXQt0UllD%2BtjwBVJR9go8VEluXvd%2BpPGbzZirvD22q1Khh4IVMC%2FuB7IgBt0H4C5CVx0snxzAuzC9WGQ9DU487Qk8LwVyRvYhyHs1HtSsCTVe0Yx6HFLZT0h0CIcHDxhHPKXGI4PSQQeD74UCDLUxOEHRS0teyimhldq2kVOGIghtqRZyqK%2FFRqCXPgiSv1J0Hcf%2B%2F1cdRc25GESCSAkXWCjTPTyhbjwDi%2F36ANCT5hxH1d73zIZrcCmcmKAJr3ecgaTEEf2DK2ReLpve3KFutHD8nhXOfGH1f9uYYzC2vVHbciiaWUfEOy3y6kkUNDp4Jz9nLor%2BAFtEGbVO3Z4%2BSfIZQAYfNF3g4ATJ%2BwBeU6d%2FSW9S%2Fy%2F%2BrPHkpFcMgFnxcA7rIp%2BXqcjnBwpZ1oEbmHYkJNLOCXEiCQa%2BbSlOQX%2FHg9xmNAU6ampJTm4sGgsK%2BIu0OnUQgTRJ5v3J3tD6NvWMQXudL7acpJwp4ffuCNVogoiejTp%2BQwAT8cwM7tra7lQlqJwtLK2V4u0dbHIv3At3AhA%2BsZq9VByJeXkGtBsry3cmy5nflGrEjj8EiIiN4OlHVhUt5yBFWwYOLJkgMMLq18LwGOqUBUZ4t%2FrirZ%2BLV%2FbNkpqRDCqLnh4j9feSfOPVtRk6SC8hZGIv219OUGovp%2Bzvb4eo5Y9oiovhl2uz69Z1vwSMCnT8VBi%2BjIAspuBCEul1TjxUAXj5%2FC0Q3brOsxSetZKcfYOmm8aRfrTYgU9CFBIkRCxSNAwLI2E7JWS9HmS38AOxhtHodftEUe8OStm0UBv%2BTImJBF0eroI4s5oUh7nDVWymtTydW&X-Amz-Signature=177cf8611e70959236d3dbbfc63c9385f91a3d999cfdd98c264f54277678b51a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGBG2Y3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy037Y5P3%2Fuv%2BNBcnHXnNAXRkyB3CVTEi92ZIgFxr%2BngIgIRCUgKOxAqzVZZFO9ZraTZrY%2BNo1wTDLdLm0g3w8yWsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOmIno8muQXhAEPuyrcA5xdX%2Bc7yIJlUCzfMsloAHRVtc0OobB1dfyMiilXQt0UllD%2BtjwBVJR9go8VEluXvd%2BpPGbzZirvD22q1Khh4IVMC%2FuB7IgBt0H4C5CVx0snxzAuzC9WGQ9DU487Qk8LwVyRvYhyHs1HtSsCTVe0Yx6HFLZT0h0CIcHDxhHPKXGI4PSQQeD74UCDLUxOEHRS0teyimhldq2kVOGIghtqRZyqK%2FFRqCXPgiSv1J0Hcf%2B%2F1cdRc25GESCSAkXWCjTPTyhbjwDi%2F36ANCT5hxH1d73zIZrcCmcmKAJr3ecgaTEEf2DK2ReLpve3KFutHD8nhXOfGH1f9uYYzC2vVHbciiaWUfEOy3y6kkUNDp4Jz9nLor%2BAFtEGbVO3Z4%2BSfIZQAYfNF3g4ATJ%2BwBeU6d%2FSW9S%2Fy%2F%2BrPHkpFcMgFnxcA7rIp%2BXqcjnBwpZ1oEbmHYkJNLOCXEiCQa%2BbSlOQX%2FHg9xmNAU6ampJTm4sGgsK%2BIu0OnUQgTRJ5v3J3tD6NvWMQXudL7acpJwp4ffuCNVogoiejTp%2BQwAT8cwM7tra7lQlqJwtLK2V4u0dbHIv3At3AhA%2BsZq9VByJeXkGtBsry3cmy5nflGrEjj8EiIiN4OlHVhUt5yBFWwYOLJkgMMLq18LwGOqUBUZ4t%2FrirZ%2BLV%2FbNkpqRDCqLnh4j9feSfOPVtRk6SC8hZGIv219OUGovp%2Bzvb4eo5Y9oiovhl2uz69Z1vwSMCnT8VBi%2BjIAspuBCEul1TjxUAXj5%2FC0Q3brOsxSetZKcfYOmm8aRfrTYgU9CFBIkRCxSNAwLI2E7JWS9HmS38AOxhtHodftEUe8OStm0UBv%2BTImJBF0eroI4s5oUh7nDVWymtTydW&X-Amz-Signature=7348fe4c305388b9024af4de67ad29ca5b023172b43cb5fa6f63f3f473d9e0b1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=981012fc11250ff69d9fb6c0f69d7fb6e66ad1afc1919560550a2796eaacafe5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=6af70050061a6de59cda2a6af8d196de4736c0bb7c639920e081512c585979ab&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=0dfc7df129f81d74a88a73baaa2cefd4d358f642d0c57013371957d40daf3913&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=aaa8335a5d1870da3682c4fc32ded646b4b777c7574f889956a16fed92843646&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=3eca1e35768f09b4b4ee210ed83a666355b5d7be0993e8b50909950e246b07a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S6UPBGK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCH2eIObvwwgMbyEbQXqf1WM%2FdRJHFmjMkMz2CnasjAw8CIQCfVcuit7NQStEiElsUB5Ln5ZxnVSCBvt9CBmOq3p3U%2FyqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMERKHAyZweMAZIbYJKtwDAU3lqQ1UQyCJLqKu%2BiGgp9HYOHEvbGl2H8XKxak98fxpyu8charffLM79NB2Clq8AdosdMpw1y0XpBG%2BTU7hrnhIAD8iB%2Fjw4xRjmHSVT9nAO3pMSEWhG6UekH6B%2B%2BMSlezWXUn2%2Fom%2FeA3qPFGEOswSeZiBxiSmFLS8zTDgtiqZ9pKlsjGUpTjn3Q6WjOZXZQVou9efTwpBMsr3Mf49y8Mq%2FqR4qDZnpXg3p24vCw6Te50pWUNKj76Xze1jdHLom0TzFRONbffSFx%2FPnY%2BDA5qRewVtag%2BkTzXnOpu1DE6Z5UgXf3pyrkWNganZgTaJaR4c1TLELtoYIXhyAtcRiLRwpgMuGk6RH0Y12vc924IEkuf%2FUR1B1TMTrYwib%2FOIw8d3NRL%2FjO07cNK6xWW2rt3UgPcqv8EXAZ0Ar0kw0HmwA8HbSViTGFjEremUOt4er6x9b9FwcTFvz%2FC%2BhmJB%2FNz0dUuipQGk0uLSOY2hTT8nS7apJvcMluRGKg%2BzZ5YZs6%2BiY8Gfl%2FnC2lRQi9l%2F4mayIrosrjNydCbgWET79imf3d4nsJqdxAPHiohQv7peUb%2BteO51LyPAsugYjEwShhChlAKGFFPOAMglCn7FqDVw1SW%2F%2BR%2FOa2nL3r0worXwvAY6pgFfFVSlFQ5j2V3piUDEX%2BBcRU%2FOFQVMhjk%2F%2BsZwnZqA3o9u2D%2BvmMsWIS4Uwd3rI5s4dbZniy1N7BmPe9qZy7Oxpv2aLwtu0bn%2Bt4GHlBD%2Bnpwl6sq16RGOP5KjX3r5w4mosdV6s5o21dPWRwbdqO01M0Aw7PbCxXO%2FaCLBSY6RcXaZXdOsybIv9eg6BVQ1pE9YmHnynwQNMSKy8eZ6hJpqsSHDWbdj&X-Amz-Signature=ca11830925fbe95326b144803ddcbd5ffc7af0086812d62b4ba41b1cf593b640&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YGUEA4G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICv6P8MHUaVN3H67NtITvq2mQChmwLRHtlqlu5h4axncAiAahDaq6PhWOVJUy8B6ZHssJq2JdMuu2BBi1zqPJ6kfHSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfbxqJ2TYhoCgGqxWKtwDmBTfJovIYXwWVjWMcmxoydV9wdhGtwRIAsiOWlrgE5K1by6TNw2P7Q9doKV%2Fe6KeNfsnRRadfFEqT3vD7sJe68IfYOD9f%2FE4kVuNrhIj3BsYdRhHtdClDgoXb%2B2Yt1fSujH9fqJmlL8JJrdDy7axqjJfiPaMp9ewEFZV%2BdLnoMbkV3aQ2e%2BBnpe2SseGv7cKJwgdeHE8PjLVwZxbpjifgzRq6opmW9FuzIPXv8LwbHz41FHDzvVeOLe9Km01jF5P%2Fci0h8gvP03jxFYQevMYD5nItWI6sQM6zSz5Bj4WV7Q%2Bqsm4G3%2BHp1LTvpONrYhL8nebsCsbfPNt30WediQoSHLklKhOue2TCxYU1dl%2B8aq9lRACrjpKHmhRRSnmtH2m1pOatFphkqNJq%2BfRl4BvLjexIu7yO2OsvlNLAyUIKqA8cL7LvoL4dHzK4%2F1bpMuIoRcnYKJhcNQJvpsLln1XiiWDzRHbuXtcA944KQVCghEzalqgzfo%2BNNKdf%2FmS%2FGYbhpK5pSqqXEDcMewnKGmCf6LO2Ucnf2LmFvf91dZqmgcFnFzWahwt0PsDvDW2nRw2MixArubnpeiajER%2FFeP3Q0U6PSIfnvPQnemeyAMT%2BLGw6FC5qkXZsJL2AtcwrLXwvAY6pgGlwenMGDhuUrO6%2Fhp96xwyq0LGyDhaln3X7465dQmQ3JiyFruUT5X5HuTomht33HFyVFHlQUm1TBrGjGfOaqp%2FX%2BgTC6heNnMloD7xftqniWhhwsROHIlQxGQM4KPMfrWOvGM49UsRq5kbkPpghsQqqa0lPFO9N8QNLJsfpI2PnCiAsrd4g3Y4OBWfhIZAe7cGdGeOGWRvFQIJYXiuLuDr%2BFFzqqAc&X-Amz-Signature=806c0637e1fca6f3dc6a774e5dc7016a63b671fa6c82333da0d20a48608328e4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YGUEA4G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICv6P8MHUaVN3H67NtITvq2mQChmwLRHtlqlu5h4axncAiAahDaq6PhWOVJUy8B6ZHssJq2JdMuu2BBi1zqPJ6kfHSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfbxqJ2TYhoCgGqxWKtwDmBTfJovIYXwWVjWMcmxoydV9wdhGtwRIAsiOWlrgE5K1by6TNw2P7Q9doKV%2Fe6KeNfsnRRadfFEqT3vD7sJe68IfYOD9f%2FE4kVuNrhIj3BsYdRhHtdClDgoXb%2B2Yt1fSujH9fqJmlL8JJrdDy7axqjJfiPaMp9ewEFZV%2BdLnoMbkV3aQ2e%2BBnpe2SseGv7cKJwgdeHE8PjLVwZxbpjifgzRq6opmW9FuzIPXv8LwbHz41FHDzvVeOLe9Km01jF5P%2Fci0h8gvP03jxFYQevMYD5nItWI6sQM6zSz5Bj4WV7Q%2Bqsm4G3%2BHp1LTvpONrYhL8nebsCsbfPNt30WediQoSHLklKhOue2TCxYU1dl%2B8aq9lRACrjpKHmhRRSnmtH2m1pOatFphkqNJq%2BfRl4BvLjexIu7yO2OsvlNLAyUIKqA8cL7LvoL4dHzK4%2F1bpMuIoRcnYKJhcNQJvpsLln1XiiWDzRHbuXtcA944KQVCghEzalqgzfo%2BNNKdf%2FmS%2FGYbhpK5pSqqXEDcMewnKGmCf6LO2Ucnf2LmFvf91dZqmgcFnFzWahwt0PsDvDW2nRw2MixArubnpeiajER%2FFeP3Q0U6PSIfnvPQnemeyAMT%2BLGw6FC5qkXZsJL2AtcwrLXwvAY6pgGlwenMGDhuUrO6%2Fhp96xwyq0LGyDhaln3X7465dQmQ3JiyFruUT5X5HuTomht33HFyVFHlQUm1TBrGjGfOaqp%2FX%2BgTC6heNnMloD7xftqniWhhwsROHIlQxGQM4KPMfrWOvGM49UsRq5kbkPpghsQqqa0lPFO9N8QNLJsfpI2PnCiAsrd4g3Y4OBWfhIZAe7cGdGeOGWRvFQIJYXiuLuDr%2BFFzqqAc&X-Amz-Signature=323c33c1418e14aef89c8d89ac5ec4adc8a1a1c6a970fc0e3e9aea323ea9fd32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D7N2WFE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMNOM9S1%2FuFuT8ptkQqdNXGLGmTpraOmsTIlKz6RuALQIhAJCqP8UYmJ7ps9SklGVoVdByGH4BNUhLW4TSvKzNMRT7KogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxPcXYXf1EjKapmOwq3APKtl%2F64YW%2FVZ3rwozDRYsDwP9k4OshaXMlYQcc1jLQ4ex0yVwrwD%2FhnLMuvtG7hGYrEH2VMAW10J2ZLIpJNH0Mm23Hy8GeYf8EQ4iNXjM%2F5mIOWSYtMS3SaT8dh952ZWNAHpEa8ovIu7HmGffja1bIjMeDZ1GL%2F9KQSoBe3PbEgGIJlokJdLyhs9JytK8g%2BDSD6n7gB4UYmzog5vXlcoKYmDefy27iubAvpevvn2Rn2ZQHsZzTJJIWQ8DeYgiszChHgj7FfmGH%2F17JJapttOv52j%2Fx3JqEHaCsYKweb%2FdZ4xkahYs9PoaywV4rdITmT3rIcTPEtDe8qWjD5IpRxOTEhaIxEBLWS1WfaejNaPbQOeoTHGxRvko3cNN7I39LnKpTqb0BB2h7T34EiAX%2BB2nc%2FFtxLuiS2O1%2FyMc0NSp7qYwsF%2Bx%2FFZyXlmamkFdiSsdeIBPYnUa%2BCYbStXwzYprbeXwX8j3%2B655OCam6eDqhhljddytXNcMJZXJ%2BHdw%2F2DktYCUaVFjfM%2FqN7CwwkyLRVaI5Oi87QRiqdOPWa2Wcr2hFbI9ruSVL3e8PUVnmnbpEO8UhHpgXRg19uY79xvxclvNfI2FgrA0tz4dsR8W9RHfH2VtUQKEYdBLoUTDstPC8BjqkAWitZfukOzB8fA5CK5Dh4kaYsbFkO03SSw26nNuAbDGDhSRKqkYei9NhQOPtT%2FNOOOa%2B70NN%2BMcIxrLFjEYkR9xn71YdXjSRzYfNtzamU4bSLRgqHmL0MEy63IouOMBCRx9KQMQs8JhmYvNyaoRDgQbUGCoaKKdo4m%2B9Wq%2BanCh5Q5YhCfyv%2FC7KK0NBM8wsgw4fFS2PdPNlT%2BMEwWCf34Ha1fdw&X-Amz-Signature=21cf93d73f9deb9368bb817655b0fcb9912e4c24c0d0e770ea1f903b99e97ae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TKBO3BU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEYd0SHYpgIQhqSXBQfh0D7xIRKG6vyrITNLGm9CX6uQIgZzc0z9S4JxwXXrbJ8Stab8z3DpIsXIYfg8n8GzEZWjoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDp0NcbvDI38jJDw6SrcA3kXHEOD8K0WIHKQcS7rAHRmFcNYh0Rfe9teoR%2FoKc2MBAm8NyVL3kqwPTXIgNrm%2Bal4ldqIvKJyWCY3nTLCKvrcqXke6wBqS%2Brim6gyBMsE6u1hAR%2BWULvWVU%2F15ksyVC4sXXK5%2B2jFaTTLASmSoL82JTJk0XxuP7Qa2wqVn6xG%2BL6EX0ZbIWrqVxGmUFns%2BvdBfv3bqv2ygNF59BMa7mL43MIYmGj4PG%2FWrS2GJqVdMNRkvoWrR0nITkztW63jtT9m%2BPspcAe%2BuyCPyb5Siigo%2FZTNC53H1xmdTzhfJUDbHj%2BuprEMUjAAD%2FfAQvARCKiaONF9adazljeDrkfXa4wyZ9KQEmhKIeNrilIgzc1epXyN4oLMmcBb6hCoVJmVQzJppYUSgE5BxkMqWDWzCod19lreo34iac1H0RcTI6qwuZMwGmntzmVYBSkrv2jpusnqESTUs2ySDDdDmetWIXVg%2FjkcEOZx8eYqTTGHWOxHOpn10jGFWMtPwXwcmcdZSvW%2BSZtWcfr4WtShYTeeWU%2Fp7Z8NyHEct0%2F7fcgpxoVx59JuUospxAsolYje8ed7To%2BMpNU0YO4btoU7kgRG9TyJJdPAVHEIGGCC4DYeBC%2BVm%2BITbpn4NuqSrKB7MOG08LwGOqUBbotI%2FH9ZP9J8jw7JWudk8BlJi2nQpaqzFs5xogE6FoNGC2yffXIuBy3X7LlVEJvwhe3I0Qa3hjvBqUBFtfd3do8439PVnQYAv31ybOeu%2FvRSCGGczaPDpbgdXOlwdUsJx8Qf6XV0KQlfmtnnJyocaOz8ip1vu44%2FKXqnvj2g%2BCDHcsfM6UnpWnqoN68N5ByJpVtddjnFSx94E1NCNrgNMakFDUjH&X-Amz-Signature=fce4d1f48ce99e2f18492dcc5d1a2119c73d5680a0580c697bf8e9813360209f&X-Amz-SignedHeaders=host&x-id=GetObject)
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