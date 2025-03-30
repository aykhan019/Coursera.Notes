

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=c9a1da5893bd23ae4de34a08a0d1aa081d0999a2776f53808439dd29b69df62d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=ce9f55ec00579abe5b12fbf3a4abbbe9cdd8a7fc08ef798bb22daafcb8eca5f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=1996bb6b3956a4ad95806e42d72b2991c99a12204c4c1740d1ebca277cdeb4b9&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=7959ccd9a15c18fd3da3bc8b4529d232853cccfd5e73637347f4030111f8652f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=2fd3f10891e18945e8c3738a574a989ff76bcaa6821e54a520e273d480e8a3fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=3503e48651e2eb4bd5106e304b72dc3db199d34a920f4e635a9c5d80e20adccc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=5d362fd6c1113e0f7d92d2bff8ad0d059d64cdae181eae4cc16029ba4c1a4bde&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=df97444e33742e29e864b433c939c91a1487ee527de71f71bdea4918657a17fd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=e39e24d59df9f5e5f5d82c5f7479a0aa57872f208741a1123b46b3fb590e3b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J4E4ONL%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCICryF3iWi3xtYHwEQR7x8Wm0DJb5Fb3YKbauqrLhnkZcAiBBxJmcsRUJPsj6ZoDQsqmb1adLNc2xzG98xil0G7yWoCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1QmupG68QGcnMKvlKtwDz%2FbW0WMiPhOZYPTD7QPfgsYybVRgk0S1u1MwTx5A5N%2FkzM402zrZpT%2BqQ1PO5omtPj5vuj9Ubz5Qts7W6i2NFae0HRK9tPEwyjfBkQEwtBI%2B61ajmXhx6k13YPyMzt7nTVfDK76dM9u4q1YDitc5H4ABFaqNXS%2Bleg9kO6s6rEmAPGVWpwOioKwBTGjDDas2tERVz3XOuigT1AgMapDNPEidUjmlkyKeCwdlAYacZPD8Qk4XLhKknVvqHBX3%2FFbO0qEewfZV%2BKnwLBb62JKrXEF3kLqDP7T39qpW1bh%2F33jvT6D0JAyxPILRWwLgoavvayn9lE84GgyrMI1ObBqMqvGmyinC9QrFLs9dQY%2FKS39vFsaTr2G64%2BRboD4Tg5hqRJB0FxRqHpjSu3lKZdcW0xhtcphwiL3YpzBtVa8TOkziT4nIY7CzWifYOz8Ja1o31Hgnr2lSIrOHQzcNtK5b6ec6lfG6mQjuAdKrpa1V6rLdWovfP6QoofpzqFVewYlqVZUpTiAvZcYga35vK8qknmOJQaz9m7xLt2x1aOXU5n%2Fv1zhvsZ0CmR871ST6G0JLcy60vtIlU8omcqY3FcNX7jX1KekrP7f9wh17w9qIah8EceY40L8lsgIP%2BBswufyhvwY6pgHcH%2B8Us%2FiDAtskuxi9qYvvyAUlf4efkg2qmeJbQ2wjogJAQ3BPkQ8TkfCUYt90QV2yVuil6NvLeKYBf240diEIBtMD%2B3Rs3Zd1JsV8BDGjxX6htb%2Beczka2QqN%2FxN6oFkiZCltetaqNZ8fSo2t3R82AW%2FPQY7nFmikucHqIxxujvdFWnGeWxhd7P6zzGBEUo66XSlSgyjsyxY%2BsEdomUixqxfnSrQb&X-Amz-Signature=4a5cfa762301fb8bf69f0af635d137e4be9bf049da95753ee92a374b3dca8530&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J4E4ONL%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCICryF3iWi3xtYHwEQR7x8Wm0DJb5Fb3YKbauqrLhnkZcAiBBxJmcsRUJPsj6ZoDQsqmb1adLNc2xzG98xil0G7yWoCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1QmupG68QGcnMKvlKtwDz%2FbW0WMiPhOZYPTD7QPfgsYybVRgk0S1u1MwTx5A5N%2FkzM402zrZpT%2BqQ1PO5omtPj5vuj9Ubz5Qts7W6i2NFae0HRK9tPEwyjfBkQEwtBI%2B61ajmXhx6k13YPyMzt7nTVfDK76dM9u4q1YDitc5H4ABFaqNXS%2Bleg9kO6s6rEmAPGVWpwOioKwBTGjDDas2tERVz3XOuigT1AgMapDNPEidUjmlkyKeCwdlAYacZPD8Qk4XLhKknVvqHBX3%2FFbO0qEewfZV%2BKnwLBb62JKrXEF3kLqDP7T39qpW1bh%2F33jvT6D0JAyxPILRWwLgoavvayn9lE84GgyrMI1ObBqMqvGmyinC9QrFLs9dQY%2FKS39vFsaTr2G64%2BRboD4Tg5hqRJB0FxRqHpjSu3lKZdcW0xhtcphwiL3YpzBtVa8TOkziT4nIY7CzWifYOz8Ja1o31Hgnr2lSIrOHQzcNtK5b6ec6lfG6mQjuAdKrpa1V6rLdWovfP6QoofpzqFVewYlqVZUpTiAvZcYga35vK8qknmOJQaz9m7xLt2x1aOXU5n%2Fv1zhvsZ0CmR871ST6G0JLcy60vtIlU8omcqY3FcNX7jX1KekrP7f9wh17w9qIah8EceY40L8lsgIP%2BBswufyhvwY6pgHcH%2B8Us%2FiDAtskuxi9qYvvyAUlf4efkg2qmeJbQ2wjogJAQ3BPkQ8TkfCUYt90QV2yVuil6NvLeKYBf240diEIBtMD%2B3Rs3Zd1JsV8BDGjxX6htb%2Beczka2QqN%2FxN6oFkiZCltetaqNZ8fSo2t3R82AW%2FPQY7nFmikucHqIxxujvdFWnGeWxhd7P6zzGBEUo66XSlSgyjsyxY%2BsEdomUixqxfnSrQb&X-Amz-Signature=5d541c3edc74b205a0ea69fb4a9143172602bbed180a3449d11bbcb511bb51f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J4E4ONL%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCICryF3iWi3xtYHwEQR7x8Wm0DJb5Fb3YKbauqrLhnkZcAiBBxJmcsRUJPsj6ZoDQsqmb1adLNc2xzG98xil0G7yWoCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1QmupG68QGcnMKvlKtwDz%2FbW0WMiPhOZYPTD7QPfgsYybVRgk0S1u1MwTx5A5N%2FkzM402zrZpT%2BqQ1PO5omtPj5vuj9Ubz5Qts7W6i2NFae0HRK9tPEwyjfBkQEwtBI%2B61ajmXhx6k13YPyMzt7nTVfDK76dM9u4q1YDitc5H4ABFaqNXS%2Bleg9kO6s6rEmAPGVWpwOioKwBTGjDDas2tERVz3XOuigT1AgMapDNPEidUjmlkyKeCwdlAYacZPD8Qk4XLhKknVvqHBX3%2FFbO0qEewfZV%2BKnwLBb62JKrXEF3kLqDP7T39qpW1bh%2F33jvT6D0JAyxPILRWwLgoavvayn9lE84GgyrMI1ObBqMqvGmyinC9QrFLs9dQY%2FKS39vFsaTr2G64%2BRboD4Tg5hqRJB0FxRqHpjSu3lKZdcW0xhtcphwiL3YpzBtVa8TOkziT4nIY7CzWifYOz8Ja1o31Hgnr2lSIrOHQzcNtK5b6ec6lfG6mQjuAdKrpa1V6rLdWovfP6QoofpzqFVewYlqVZUpTiAvZcYga35vK8qknmOJQaz9m7xLt2x1aOXU5n%2Fv1zhvsZ0CmR871ST6G0JLcy60vtIlU8omcqY3FcNX7jX1KekrP7f9wh17w9qIah8EceY40L8lsgIP%2BBswufyhvwY6pgHcH%2B8Us%2FiDAtskuxi9qYvvyAUlf4efkg2qmeJbQ2wjogJAQ3BPkQ8TkfCUYt90QV2yVuil6NvLeKYBf240diEIBtMD%2B3Rs3Zd1JsV8BDGjxX6htb%2Beczka2QqN%2FxN6oFkiZCltetaqNZ8fSo2t3R82AW%2FPQY7nFmikucHqIxxujvdFWnGeWxhd7P6zzGBEUo66XSlSgyjsyxY%2BsEdomUixqxfnSrQb&X-Amz-Signature=d24e8446dec4b2f9fe2a544d0f66159e9af3100b6696cc9ae6abcbb1ccfab590&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=d6f2dcafc77f6b8d5986335d10453fa5369811c6f39459772b34fdcb1133bea8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=b4c73158fb15de242f7a8496627a4f663b590b3ae835b0f84d312e5132229d81&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=2f6bb2c1074d96311637af0ab25eae505e1b787cd0b8269fd53fb1f2ebf0d4a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=f7dd9be7b6b8629eefae6a712f998f6291f6568e2fb2609ce4bfe93abfa943ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=f6c31576ceb3d738904ecd6b32361099baa7c67102c2c541236a7f78685912be&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R37SDGNW%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQD8adw7xzIHolgjjg%2Fv7cVEKZkKtLn58KRNqNhrPlrgzgIhANUQyK8qR54u4Vpcbn43KJwE5OMSbJcnhzdIboa8UkQuKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOW%2Bp19mlyK3ABEZgq3AMiJskDKYmOVC9vB4af1Ze69ffNRzh%2FQLlVs7B2M2HK1N6IOEoh9DGYV48TrrIbQOUo%2BoilRu%2FxHuNIDzl2SqQZip3nPNMIq90%2BTXYdGjqIoLUpJpGrQUpDHBVq5wzg0wdjs%2BIJhJ%2FHb6Tpa9AbLsKxY3hTuEh8QABvu1WmG7cfYJIOU4GLHo%2BufYO%2BOMe7X2py9W98n%2FgiXDYui5u%2FdfABNukVoG2Dk7IxQSeoF0ZnnA6aDayQ0Rc0dc1%2BkggPIfCn0g2XShBjruOq2eJbZmSBjamCEdSyJOR8bwhfplgbmmrmri9vaLuxxfQwakreh6JgNae8YfGur4cWzMMIVAEuQepgvd%2BhJFinXfu6nqy15%2BlTpuKnN92LBu8LzRZQEb0XDmnJ%2BwU0KeE5fmCxAyXcPSGVO9EfoDW17LpSNfpbIP0WSmWWn9x7unx%2B21cuykHi1MOu02KFu%2FgWcfSP5NWhJS2FG94el%2BVfMzLu7wxdIyZ7QqSkgr8qhM3%2BODPtiwpr1uzYTbPydPKQ4qjk7WDi%2FmAJphVlVYw2tot3hFGdQwDXqfOsLZXKwlen2V%2B7sLvDXfLoFw240oinOR5vCHwyxDEhnPmamByAEc2Bnxi%2Fw7yUnqYdu6C%2FdfCFcDC2%2FKG%2FBjqkASo%2BjZUZjgIm1Uzp4Gu6asf5OYsZOFO4uM7It5PRYEs0zYQA%2Bq0Qy72BFibxQu7jJzr%2F1biJ6xJdyvN895cbokjX9rwOyChzOq%2BXKrfS6P%2Bjejvz%2Fahb%2BFwZRM4BWvSD4e%2BuVz3ELnx72drN%2BuzhR%2FPz7zq31zON91ckPmqrPOcn%2FYdwEgOMl6DEFuOldNsWS9hOnw%2F56QL6zA9qNHugQ3KfjRaI&X-Amz-Signature=fb357e967abe0c6ce4035ea37db319b9faa76e60a0bc550a7a16daebc41422da&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA7EXLPA%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIFJJIFL4yRfRm1qVTNZsekrs8zxeZthxkgFczKJZucakAiEAu7kNUQzXkGAvmCRVzLlBXP2g2N%2FS1piqzwZTuqnVHNQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvBx7iSwdKq2BSgByrcAxGW5YvepdL47IWXoOlpNTS2hTVsf85BZbvgFiW88uhEpJlY%2BjF38AafDX7mISrfAft3hu4jzRiJiOf6ziaWwBNKcj8jG6H7Kk%2FjPGQv5yOi7MjfXOmvNjGkSVRfMDhxQCjvbS1GiGbj%2BjqwkRMSKIzIqTm0nWjBFfzOzNHXfwsqtHpV232kO1hs6Y3cN2gsvJH2mNUbIHRD8xAKMlWJAJ2s0Oc6LXm3SrV8qIT7fwBASrd5hYsehACntZlAVRTeAVKZMwdjrMyRrSIsfcH970cnaUnxSI%2F6J4mfZ0F8D6GAuB%2BPOQTyBkMF%2FD%2Bw%2Bd2hAhr7QTzOi5El20lFqXZx1zfPkPNnc%2FDSA%2BRsoatgHZRoP3MtPg5Zv10G0fhmIE1IysSSbSsUMJO4Y%2FVfCyQUeKBTqtAgGMeLPTj0cytKW2qELdrJt%2FF9t0dfkTiPMlvWJ8gfF%2FULBhutPD5t7Aahk5w1YbRfvb%2BWJcn1j3T%2FWOeziu%2By6Gy77zGsvHnFaCXmSDtS13IA91F6hVm9blmcSGDDoeeIHlTMkFsvHYSbOgi1BseuvoRU1MeI3ncG%2BzEFweUZXNPebTJVGYzKbTvy8aUToxHkLsdaFQTrZiabJjDKm7YYAL2zcLy7cjPMMJyPor8GOqUBMAXEi3JD9cx9GHe6LisTPRkW9urbNgFhoODeXc1l5ZPinvtaG3pkfE4WxV3UPgKPCbXDUKeMRiDw%2FFXW7aq6YWGokP%2B%2FGZCdV7LO2PAAlDyIbj63B1HKXQvRFXvKo6avLIJAtqreij6K7tsQ7Sn8AEypY6WLmU4PVLc%2F9UThv8LDq175PvCZY1oo1H2iOl%2Bai4xXLHBC9Im4O0gH3bGYfok8htaR&X-Amz-Signature=dfd43bdfe5be9a5a45664d9b2b2a49793b84f378c3cde8b86f441c203effd411&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA7EXLPA%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIFJJIFL4yRfRm1qVTNZsekrs8zxeZthxkgFczKJZucakAiEAu7kNUQzXkGAvmCRVzLlBXP2g2N%2FS1piqzwZTuqnVHNQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvBx7iSwdKq2BSgByrcAxGW5YvepdL47IWXoOlpNTS2hTVsf85BZbvgFiW88uhEpJlY%2BjF38AafDX7mISrfAft3hu4jzRiJiOf6ziaWwBNKcj8jG6H7Kk%2FjPGQv5yOi7MjfXOmvNjGkSVRfMDhxQCjvbS1GiGbj%2BjqwkRMSKIzIqTm0nWjBFfzOzNHXfwsqtHpV232kO1hs6Y3cN2gsvJH2mNUbIHRD8xAKMlWJAJ2s0Oc6LXm3SrV8qIT7fwBASrd5hYsehACntZlAVRTeAVKZMwdjrMyRrSIsfcH970cnaUnxSI%2F6J4mfZ0F8D6GAuB%2BPOQTyBkMF%2FD%2Bw%2Bd2hAhr7QTzOi5El20lFqXZx1zfPkPNnc%2FDSA%2BRsoatgHZRoP3MtPg5Zv10G0fhmIE1IysSSbSsUMJO4Y%2FVfCyQUeKBTqtAgGMeLPTj0cytKW2qELdrJt%2FF9t0dfkTiPMlvWJ8gfF%2FULBhutPD5t7Aahk5w1YbRfvb%2BWJcn1j3T%2FWOeziu%2By6Gy77zGsvHnFaCXmSDtS13IA91F6hVm9blmcSGDDoeeIHlTMkFsvHYSbOgi1BseuvoRU1MeI3ncG%2BzEFweUZXNPebTJVGYzKbTvy8aUToxHkLsdaFQTrZiabJjDKm7YYAL2zcLy7cjPMMJyPor8GOqUBMAXEi3JD9cx9GHe6LisTPRkW9urbNgFhoODeXc1l5ZPinvtaG3pkfE4WxV3UPgKPCbXDUKeMRiDw%2FFXW7aq6YWGokP%2B%2FGZCdV7LO2PAAlDyIbj63B1HKXQvRFXvKo6avLIJAtqreij6K7tsQ7Sn8AEypY6WLmU4PVLc%2F9UThv8LDq175PvCZY1oo1H2iOl%2Bai4xXLHBC9Im4O0gH3bGYfok8htaR&X-Amz-Signature=9b0803e5a3815c72f86b33456bb45fcace98ad76df585a5bbc715f9f05e80935&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWEMY6IE%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCa2k5fzwMl%2BWWoPs%2FX6Ku460dDM0Ff5VJu2wE2RjB0lAIhAI%2FBxiLulz%2F2LuhRvV5upTv62KCk2PJap4XDoqc4qVrzKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIfxd9xks4dwebwbQq3AOHN1LQOfSKcXIpoV4osnifIhhZ9mrRYNqTlU3p62Kk2RJbmOFopcfcaijVfSzcgyAOGaE9qVMp%2BlAGTiHhYv%2F8n9FV1exLs0xLcsCALqYefT4qIpjQhvrKkgWb4zW2223rEfgJhWjEqEkNg2WIi4%2BzG4pJFGaOZmUbGlD2NJyH8hUPJPTJN%2FEEjTGecJq0HfUSONjKh161IJJeR5DMCvMZaayWjcPtx5QGnxi0zpZw7dUJDPV%2FsFFIqg8sBC5omyWrVeBILPYYv87eVO%2FrakFsQci7SiXUcKSrygDejtPIRHL04vKSncXVNtWX8ptX4GSlmCBRTaiAFvZeBU19ZJbERNmXy%2BFgIr%2BoBWveGzbGf%2BJDgjQMkAeOALb6TPd7%2Fvg9prb17hZcNlWE2bL89izgWY%2B2JTMZV0YiP5%2F%2BjwVG5X8eWGS8o%2B91NfI%2BUY3VChchknzLzESC9%2BGyff698U29Vgc9y3Yzubjqbwt1I7iEVkpIoX2nQold1o%2BFTJdhzDjzCjQDlzKQWKak9cAs8fUo2CylLqnaJ934H921OOPn8v2Jlf7ZmmmM4fFarmH5UvxpJBXKXbG3xYA3RLz5wt7OO5HFbVHI21cub4shBsn1XDDAR9jKrRiOLuD7ADDMg6K%2FBjqkAffoGduoLzhPVCkU1t1cmgVqDHMSDRV82twnzkUweWcWN4hnzTPoffJloXaEabsswziaLuYM3LQhSX7NZZiLavjs6bIlYa%2FVeuqXuEcl%2FLP%2FW0TkEuJVylDZjaZbaAxCSjJBHnr9PVfaa%2FxoZmPW%2Fa4EYnSMAnCLf%2BIVN3KmQKVC2bIjzXeN29ZN5qhZ%2BrPam6yY1DnDmjD0TAMhJIo7ZdLySoIG&X-Amz-Signature=0354c62473b575bc0cf16700fb9120c67f50d77d0850e1580f7091b49b30611e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=463e716e49bef56a7f3df49859dc1501bf249004b5ff587fd40e1a0c585dadf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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