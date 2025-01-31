

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=ae81ceae2f7f6896ce259fe65726050902736a64328e53f806f57b2206691da0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=4e9b664057cf95a9db7543a3d6e9db21cce7dba1f1f19c76bc41d05c5ec448e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=af0f90ec01bdda1738bdb999f645f8b382602798633a80f4048ecbfbdd28ff1d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=c4686f4873dbbf3445a969e54aff39abc2af1ba67f83ab7de235845835c5af9f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=83f89c56d8870287748381476d301753b5f763068e44414a400606c768402d7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=f9ad704d8d9634e4e60881644f386701171e2b823916c8a933f1842dc41bd266&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=5673ba13dbb784a9a02f4560f8abf4fe860d1b622f45770ad58d8cbcf46ec459&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=2599eb32ddd01ae2bc95aa553734af4190e2674896314a17d8e4f6cda41565fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=e5eb754f76e22fa32bb2e6f9ce885f2730ac71d3be46e4e31bfcf7f17ce0b4b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4DXCUL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCCF8BzmG5aTzwgwz5axOMWk8J3lB8WJS%2FFnjooIVLvQIhAMK0%2FxDhVIAX6UNH83%2FecJVv1P%2Fw57cF1deXoFM7TpZrKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyVFkt4vlo9J9dYB4q3AP5hiYDu9G5UuBla99pFQ%2BsWM7Tj55TEzIvzUw8CPayuNiNqLlPWXZXx%2BSUbSlBd%2FTk9dokwJWjA83svoALwUX4Gvz04EnvRistifux1hZNf%2FpJQgdb5JDgViUd9klqFVaRAxes1NKvpbFmPyhCcQUIsdwvZg6VGGTQnXndxvnMGgHK19TIW%2F9za5MDOhcHofDZaMUCqbEOl4McLEWxIdpC7JjdRha1Y4Mo2woma%2F0EKGOiMI9U%2Bz7yCGrEv1sIxS6ACWS08Fwwm5OrSshE7AUx6BohseDs7RWBz5hUro%2FL8P4kvX%2BvdWWpsGzOkBX7Rj8hwFepoPP9b2e%2BSEDHXEoM8XyfcF9o2eW6vGO7jnKWIAA%2BmYeJ0GuddUZt0p56uGXDPbg0NZH1JwLCucx9xYOtGc5Gxs1Cx8InNk8PNb7XtKc5%2BXvbYmMyhQRyMhc5OY3o%2BEY0xpmCjNoMvQDScDB3HKsnr2BiZenBDjW2NXehbcoDQ5XMArRbU%2F4XfGHdRl%2FcK%2FWwUDKm5oNZgofXL%2BjhD4cypzUW%2FAfLvFCc0rc0%2BSukvP0%2FrHlr84C%2B8lj6mG6ydBC92KOD6%2BtnDKyu9Yk8T6A6n0y9En7JB9Jh8dn%2BYN99YWsmsxNxt4MPCTCQ6%2FO8BjqkAW2zj06aLgt5ijy8BJ1NXe%2BIsAnxweUS9QCN03Qk6RrGyItSGrSz2xXtfxb7zs1XdNAeGs6F3UXfltYLPA1qAx5pq%2BHiEOo8L%2FYQMQ6L4QXn%2FHvSe70ApTR4R1FwvllrstF4K4NXV7Qzp3nrSerb1H5NYIjeUb57Dl2rv%2BvE4CqpiOwU2hfgBFNTVCGs4PR7gm1xtSfIBTlDQ4IDASGIKeK0pRNN&X-Amz-Signature=606a271fcb382a83914c3ba537d3381370ae1535fcd0ae53c859eb30c22ce998&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4DXCUL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCCF8BzmG5aTzwgwz5axOMWk8J3lB8WJS%2FFnjooIVLvQIhAMK0%2FxDhVIAX6UNH83%2FecJVv1P%2Fw57cF1deXoFM7TpZrKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyVFkt4vlo9J9dYB4q3AP5hiYDu9G5UuBla99pFQ%2BsWM7Tj55TEzIvzUw8CPayuNiNqLlPWXZXx%2BSUbSlBd%2FTk9dokwJWjA83svoALwUX4Gvz04EnvRistifux1hZNf%2FpJQgdb5JDgViUd9klqFVaRAxes1NKvpbFmPyhCcQUIsdwvZg6VGGTQnXndxvnMGgHK19TIW%2F9za5MDOhcHofDZaMUCqbEOl4McLEWxIdpC7JjdRha1Y4Mo2woma%2F0EKGOiMI9U%2Bz7yCGrEv1sIxS6ACWS08Fwwm5OrSshE7AUx6BohseDs7RWBz5hUro%2FL8P4kvX%2BvdWWpsGzOkBX7Rj8hwFepoPP9b2e%2BSEDHXEoM8XyfcF9o2eW6vGO7jnKWIAA%2BmYeJ0GuddUZt0p56uGXDPbg0NZH1JwLCucx9xYOtGc5Gxs1Cx8InNk8PNb7XtKc5%2BXvbYmMyhQRyMhc5OY3o%2BEY0xpmCjNoMvQDScDB3HKsnr2BiZenBDjW2NXehbcoDQ5XMArRbU%2F4XfGHdRl%2FcK%2FWwUDKm5oNZgofXL%2BjhD4cypzUW%2FAfLvFCc0rc0%2BSukvP0%2FrHlr84C%2B8lj6mG6ydBC92KOD6%2BtnDKyu9Yk8T6A6n0y9En7JB9Jh8dn%2BYN99YWsmsxNxt4MPCTCQ6%2FO8BjqkAW2zj06aLgt5ijy8BJ1NXe%2BIsAnxweUS9QCN03Qk6RrGyItSGrSz2xXtfxb7zs1XdNAeGs6F3UXfltYLPA1qAx5pq%2BHiEOo8L%2FYQMQ6L4QXn%2FHvSe70ApTR4R1FwvllrstF4K4NXV7Qzp3nrSerb1H5NYIjeUb57Dl2rv%2BvE4CqpiOwU2hfgBFNTVCGs4PR7gm1xtSfIBTlDQ4IDASGIKeK0pRNN&X-Amz-Signature=2a2b318a32fbe3b4199d7464e986b4827d4c18cff64b208b4479939a754800c4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4DXCUL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCCF8BzmG5aTzwgwz5axOMWk8J3lB8WJS%2FFnjooIVLvQIhAMK0%2FxDhVIAX6UNH83%2FecJVv1P%2Fw57cF1deXoFM7TpZrKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyVFkt4vlo9J9dYB4q3AP5hiYDu9G5UuBla99pFQ%2BsWM7Tj55TEzIvzUw8CPayuNiNqLlPWXZXx%2BSUbSlBd%2FTk9dokwJWjA83svoALwUX4Gvz04EnvRistifux1hZNf%2FpJQgdb5JDgViUd9klqFVaRAxes1NKvpbFmPyhCcQUIsdwvZg6VGGTQnXndxvnMGgHK19TIW%2F9za5MDOhcHofDZaMUCqbEOl4McLEWxIdpC7JjdRha1Y4Mo2woma%2F0EKGOiMI9U%2Bz7yCGrEv1sIxS6ACWS08Fwwm5OrSshE7AUx6BohseDs7RWBz5hUro%2FL8P4kvX%2BvdWWpsGzOkBX7Rj8hwFepoPP9b2e%2BSEDHXEoM8XyfcF9o2eW6vGO7jnKWIAA%2BmYeJ0GuddUZt0p56uGXDPbg0NZH1JwLCucx9xYOtGc5Gxs1Cx8InNk8PNb7XtKc5%2BXvbYmMyhQRyMhc5OY3o%2BEY0xpmCjNoMvQDScDB3HKsnr2BiZenBDjW2NXehbcoDQ5XMArRbU%2F4XfGHdRl%2FcK%2FWwUDKm5oNZgofXL%2BjhD4cypzUW%2FAfLvFCc0rc0%2BSukvP0%2FrHlr84C%2B8lj6mG6ydBC92KOD6%2BtnDKyu9Yk8T6A6n0y9En7JB9Jh8dn%2BYN99YWsmsxNxt4MPCTCQ6%2FO8BjqkAW2zj06aLgt5ijy8BJ1NXe%2BIsAnxweUS9QCN03Qk6RrGyItSGrSz2xXtfxb7zs1XdNAeGs6F3UXfltYLPA1qAx5pq%2BHiEOo8L%2FYQMQ6L4QXn%2FHvSe70ApTR4R1FwvllrstF4K4NXV7Qzp3nrSerb1H5NYIjeUb57Dl2rv%2BvE4CqpiOwU2hfgBFNTVCGs4PR7gm1xtSfIBTlDQ4IDASGIKeK0pRNN&X-Amz-Signature=58ebf45117b8ebe93c824bae01289ce19503b96efe0f07bbaa7fb1481506b0a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=18443d9590f673f60c836960d13a6b4fd07fbc30aa7e6f46f00bf4bc25f3023c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=23ad75efd6f4c46349ea8e46e9504e1ec2157c297ff8281530d52528e39a1ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=8224f9fecd66abd66a91f3b8320051dc50269b78645ae585457e2513ed927cf8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=a0c68e7535c964b047e70d97546080538b95875df2e60ae3d3b2ae4433c3e0a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=63ca4cb6d434f2deae0898b791e796ef50ae610f0aead7a09121473b5ccbb452&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5LGCVWG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAw0TeIRo6zIREvQS%2BfZMJrVK8IUcMhF72Dv7e3F5IRrAiEA7xlR54tRWXgzfayYGEODTsw%2BJ6XjfC2KZBXT6wbEXnMqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFD3HOTDk39p59X2LircA5%2FlwSWgUqmmfy0%2BlwpfkcE87rGMyKcX0IQNDDQO7Gp%2FUx6Cd3dT%2Brt6XpoK4LL%2Bw7n3EZaCeZwMw834tLjFbacI%2B%2Bvt%2FFHK%2FplgqW4HaGuNrD2bLxUwmeLrTNMV3PucKinc%2FsjeFNDIVTXin%2BWK8NvF4AjhcNoQozqwWOCCT216yO0NIXRFUkS1bMcbx%2F%2Fq06JE23FH8Yr7F5lMfrXl1P4vINHo62jY8AEsgSnKljxgsil4m55tiTV8qx%2BY%2FySraOjnM1rKWyOdnzHcURuKRcujuM0UTNQM0iFy1XKkSU46CgSp9dVmx7pY1MWv1rhzXtTWHem2qy7KSdaRnrO0Wtv6KRgNTeituGDKGf9CbNnIrpV4Cdr4NVQRTJnJ9fNGnjn5uEPM0ubmsGMUug6wuL%2BcDYJL6cOaiO55O16IWZRznvTJZrl0yRPr0XZsReeszdQOC5a6xBu3bo36DMzHCT9bs%2F2QAruea6k4mLyeCLKK9xNy8rZdmcoE0oUxBjvRz0kMO1uiycYwuP0fs5qKSnXa%2FDLOhXJCiBr1N7wCH0iWtJVbSB62lOMZ%2FVRVmQRYNIAvF7D77RNfr6FoXP7j%2FoqVcttSlRJSnFqYHq%2B9RizGzIIIIS%2Beeqrg3qswMPzq87wGOqUBxG%2BRDa2Gpz9g9ZNAZxMgscMKVzzUxY2QUjfVh5szonS8pyRxa7dpL5rbf25xufJr2RtWpv5zAbrWzqn7JxyDmBPGCgYtB9oT8XAKWnzsafeFpkPCzagZKsCb56XyGj%2BDEQAxc6xd8DOw0wYZIhCkmO4rvATWrEd7nvAzklO6vV8bFsScTkxmGzS8C90fxA3DhOccDrA0%2F0CWLN1OwCwRbIWmbapc&X-Amz-Signature=3731b52a05060ea19882d547c272bbc045222e95b5b5838d08d5d10adc1d2b68&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLANSRJ5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKurSqZD1zyS6QkHQALY%2BMNDlyEbeK2Z2vLQEcXCw02AiBt3VwYeeNc7yOdg%2BXLfxt6pZNrbcj1gITU%2BqCoxDtXzCqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0YLgYgh4JnokiR3dKtwDDbP5xwTfByL49ZmUUUCFe8f71anRVea%2BD0f5NSYi7UPxIwPTxByLEna6NKYDhzdq%2BE8rtnOAPfE4dPnAZhGzSLnh6x1Mlw%2FocS4HonPB%2FB0dcG2Ezuxz57Eewqw%2BAAK7f7EWZIr9B%2BRkYbHeGJhyq1Hfp1yVXIl81tehqzmlDzD0KByRjFRkt7YWr95Z0YZJtDOemHFBG8NHylzET%2BXxgVNflntjYCuJCzce3DvjrXWGQptDeRN%2FMfmBbQ%2FqNPZDWsNRFKlD%2FO17M%2Fy%2FsQSzSMETrGNdntwoni5uI2L7%2Beg%2BslOtF%2ForfYQ6fzgqJusSlZMjkhdVh%2FMuqnosCKYgewKNeeGJA1r4LV3lYHA7xqArqMAhB2JA25BeAoqg4YNnjGZug9aHxVonBGvbG65LAgZ6c7O4XHOoZxyXJhrsqsaEUIah2us5yC8CnXaHcH8iReYxRFvaHzyAjRripwq0tQJztMH13N%2B4Mi%2FTIQJgt2J%2BTSvT3nr4Kk9oT13EHUzqipPBqRp5xENN2IzTN3NtU4fqw8DQekRAwzCt1pNGCMcnOU0MiDLgEtuk0UbAz5l%2Bbf2Jq0bzASEX5rXV7j1gXS62o3AYbqhpMGhxV5Od88crDmykjcoqFW2neREwkOvzvAY6pgE1Hra5Vuifezxzwx%2Ftovl4aQYpg4z%2FPlNEGo84WgcxCnh0r4GbC89ZKyUJa2U3SBJRnkIQlsQHueNWkInaqwqCFT8EIp%2FgDsnV1NES1Y7yEqNBOZAhFUJNOR56EKtqnWJpzrKPBCJuRDtwXKYQXg7kmCYGZPvY2Q%2BjbhIykJljh8Ocj2v3%2FQuWD8BwY3j2nzNhf92YWmm0fEzr%2FNsFtx%2FToekGIL8F&X-Amz-Signature=9b36819e27a57db7526d8677e0bd041029c52062fc9e6f753279c0599f524bf2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLANSRJ5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKurSqZD1zyS6QkHQALY%2BMNDlyEbeK2Z2vLQEcXCw02AiBt3VwYeeNc7yOdg%2BXLfxt6pZNrbcj1gITU%2BqCoxDtXzCqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0YLgYgh4JnokiR3dKtwDDbP5xwTfByL49ZmUUUCFe8f71anRVea%2BD0f5NSYi7UPxIwPTxByLEna6NKYDhzdq%2BE8rtnOAPfE4dPnAZhGzSLnh6x1Mlw%2FocS4HonPB%2FB0dcG2Ezuxz57Eewqw%2BAAK7f7EWZIr9B%2BRkYbHeGJhyq1Hfp1yVXIl81tehqzmlDzD0KByRjFRkt7YWr95Z0YZJtDOemHFBG8NHylzET%2BXxgVNflntjYCuJCzce3DvjrXWGQptDeRN%2FMfmBbQ%2FqNPZDWsNRFKlD%2FO17M%2Fy%2FsQSzSMETrGNdntwoni5uI2L7%2Beg%2BslOtF%2ForfYQ6fzgqJusSlZMjkhdVh%2FMuqnosCKYgewKNeeGJA1r4LV3lYHA7xqArqMAhB2JA25BeAoqg4YNnjGZug9aHxVonBGvbG65LAgZ6c7O4XHOoZxyXJhrsqsaEUIah2us5yC8CnXaHcH8iReYxRFvaHzyAjRripwq0tQJztMH13N%2B4Mi%2FTIQJgt2J%2BTSvT3nr4Kk9oT13EHUzqipPBqRp5xENN2IzTN3NtU4fqw8DQekRAwzCt1pNGCMcnOU0MiDLgEtuk0UbAz5l%2Bbf2Jq0bzASEX5rXV7j1gXS62o3AYbqhpMGhxV5Od88crDmykjcoqFW2neREwkOvzvAY6pgE1Hra5Vuifezxzwx%2Ftovl4aQYpg4z%2FPlNEGo84WgcxCnh0r4GbC89ZKyUJa2U3SBJRnkIQlsQHueNWkInaqwqCFT8EIp%2FgDsnV1NES1Y7yEqNBOZAhFUJNOR56EKtqnWJpzrKPBCJuRDtwXKYQXg7kmCYGZPvY2Q%2BjbhIykJljh8Ocj2v3%2FQuWD8BwY3j2nzNhf92YWmm0fEzr%2FNsFtx%2FToekGIL8F&X-Amz-Signature=978e7d0572dbc87ad1edd565b869d2b37d439d63528b0ddf7912c4d8e18377f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TISR2IXE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMCi6fVeuW8w9it9l%2BSIVlqzi0cjJq6wOWIg8ELX9NVQIgY1O%2FcyySPzC2qsTBqnqEpyOv1sB%2Fpeu8pZ4kFtDxnwcqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMFH9494OFRvW%2B8otyrcAwYfDMJccLs8HT%2FlkHjdofRSLcV7J2HZEIN4wILjFaS%2BVo9vSZYLa7SA2nBDt71MvpOeKECkYaUWnhA3cNwKqW2FH6cNoH4HuVTYTjkYzE%2B2WTWmyATZ%2BnVzQPOWO1efoilBSZtp40QHdrhKMjhMAO9FWMkackZax7ebzt9fVDre5fJMx5duHNaP0kikmYuBllqm8YJ5z1zuSJ84WWs7SvkclFpTwCy5Jw%2BAvId%2FVCqKkNFzLHjrl6gGmpnUwmXI4lZzGpQllKtt4MC9gqY7PDAyXCnWIHIg3mgW4mGvPETAZLCrpuNipz8TC6TpL9%2FFUhxqieEORT3h28Ixlel%2FwXMVw3S4YreomuS5UcuYHePyFAXVEIyqAlfSk2ieoMKHxS25q%2F4t%2FIiH5M53CPyUZeqxpG%2FnW9mLemGXjP1TtR6cfspxd5mpveY42Cd3QDjTIHMUhG8otgYPHT1tXzXWQiBJx%2FvrqBAKUI0UB7Byx6FzVY0XdaEfgzMSizztLsVSsrZQOP8Yanu7FaArQ5TvW5YzvcyCpuCjBHzqlQqhMAGaHOMlayKpHVh9R16sVUGCeD5huJ0orLL8wo0Oyio8JrfmEwxJ7LdCdDos6Sxkp2j0oQH8Fo%2FjfY%2BVBBgVMLjr87wGOqUBXlOYNEJ6UIqmjvDntqOCnqrA2JvaRQUnBTCH1vrSs0oahY%2BMM%2Bp8UtGLFJAGqZHmhOhglIlC3S3oxjkpbGWw%2BwEMMNstk4znIA0fjS3mvVthh9RkZ%2BwOK3cRgw56itY1utii13aQMrNmbxPvQ3Tt5onJDPnbyCwd8TNvO7C6ST8%2Fw6oAJA2TzFh6oXy0MfgdfrdhXRwNDjuce4N2J5SiD6wAAX5a&X-Amz-Signature=3a37f280f7d6ba23e472062d8e2b12cbee9057d7795c8340709876d1387a7ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOA2ZMU6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlv4k%2FQ8Y4UkRo1eaS8Tda9PH0sYXjMPhHQfyx1NpJ2wIhANAPBVfXw0%2FVlpO7AK8eno39ztiPqVDhnqDCNWi9gHKbKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwncDhazd1u67PUgRcq3APAS5xW2aMOENiCUJwiGMhtTgIFaivwdkR%2B%2B%2BMzHOwSqrG24ICq3vpac%2BW9%2B6tg%2FTtXQ%2FEB9yFMQg31hIh5cWM5xx4RLcQxCz17Nj0bhsxuv7gDGDB4UCEmpTVrkSbmsC6O%2BjZ%2F9d2N6aFT50EELIawPWjQGVOhRMLwLxQNwq8%2BxXaSFX2LhHU2UYa%2FxIrNhCJPs93DBFaIpC1Bnkx9SWBMk3wEIqef9IJLgux3bjX2TLgGu8CGwZqT82unqzAvRjkuXKrcMHAcb%2BhmKOOev5kVSnWXLVtEVd157yY1HLBLu%2FgHqsL4fhGJXZ0H79t6fVUPz8%2B1aTSGk1pK5Et5394Yb9o%2Bee%2FPwM7bRZ%2FAmb4%2BJAJ3WdoRoxKR8%2BlWWI2wPmRRNplsN%2BloI%2FQdPaloO5nEsiPAT284A7%2FD6J7evRXk%2BME4JmS4qLYjaQauTlP%2Bvs3aEhWSptExe5YKKX0bThi0Cr%2B%2FYVQqP0tj6KohgE7SumKsEojJpADKZ53tdpQePZgWO9yCAUWs%2BaNky6Af0rXoOIclCiexszjWE%2BZFJaUrsu79lONSl3mM2TwV%2FwMPtrCxclCVRx40f6RC9B8vsCoPHEvOUMT9l5BzhYAVkMxSKhdF7q2nKglW7baQDzC16%2FO8BjqkAbxXRH8Giy77B82N2VFYCtn4Us%2BGyGgs7wEALK9VDzhgLj7ED%2BbeJU%2BrsMUxXiHB4CfWUQs%2B1V%2FJhtHmyiAQb5L%2BsY0sntDYHBzMk8ZTjUALxO8hjKA6GqIsg7Z38K6jz%2BV%2Bn9svWNvFNboTYQgedxFuCGHt3m2bTM9dLkZ1OKvu9zaH8TE5jCSZW3j9nRkpoZbqSVw5OY1fRVymWA81Y1rkhWV9&X-Amz-Signature=c547efe018b620adee472c486dd4573600e6c3985af1c15a01b7286279ab97d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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