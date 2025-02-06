

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=76b32f7442dbdc402db4a80db519c371d3910b5332338b84a793420cd9a61738&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=95e268a4c1a24efbbb5b84921beec79f19d5814ea0e47e14cea2ca797398d9e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=dbe2261654635f23fad849860f778ece71ad16e6867ca6b2fb946baa8021caad&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=03fa65a8e23faad40f1a3ae7fd5bd81128db09ac08293b235611daf8ce27a7ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=08fdcd085fbbc15ca25291f9177e23093315176eeab1d3509b0fbb84063e3b49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=bd001f29d8efb1c611a24cf85ef1c34fc46a1e5eb1ae671f0bbc885e14a08f48&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=b53dd048e9e5cf8a13a28e9b90772a05315fa935fc0dae2cde3c0c8b595ea3a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=58ea585cfb5b8d500bb797cd8f4a3be045824ae920fffcb1a2a43cd9d4dfee5f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=3eb07e65b64b6a5fdde2eaab544fb4d0cfcfdc520b317d53ac89208a99152292&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVPZWLYV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPd7P2gePqNxsA%2BvM4cYB03KQezBSxBZklzvQAJAkfCwIhAJGqHNyTMww9q%2BXExspzFvSyeqSKqiv3SNT8JvjDErjrKv8DCFoQABoMNjM3NDIzMTgzODA1IgyvVlMGoeVE7qRL1bkq3AMUn6Mjb9yLyyLfFatkN3DyJpklTMz9Re1khQL%2FmBlIyb5K2p%2BsqsRoUyrvV%2B8Er4f6B15t4H7lRAdgz9F2ovamz%2BlV9OqzQz3HSOXwnF3%2BFniaNbX1ihOdY2PnFUe%2BFBhaRWALv40CxHIPkVahcRkPvuSlozw9tXl1QX9F1Auv4HBNTLtdSyVVgwIPrmih6q3Z%2BjH6VzSu2LAgOK5dpjUWAr7yBqRsWHFANEWBQH0GhlPH0MXsodzIepKI2wZ7eRQTfRD5H31fO9VYF30kUQwiceMxEkCfX1bzevngpqC0%2FLz3JrpVyLY9sVAxzk8UN4GYYgGHhGv5id%2BUDycrp419uQi5eouVZncOLB1aD5t%2BpYwidyMdzcyGsrtdLBGlRKAQ6Z8d8mraBRdYtcPdnLqlrT9k9uNqp2vwpFqf60eFu2sN%2FcpIWgi%2FQp%2FTTwxDcUKs69LcCsmt%2FN%2Bwdh%2BiX4PUeO4OUtrUUBsm3UEf2OxImE8Tf6BKJv%2B9t6qEnD5IOxYR5mVyKHUnDuqvrzTWZKv6WA6Mq3TPOLFVXs62qN1TgW%2Boy775Udkk37eeRPbBQGTndil8iadIMutHLgbEfynEzmhQFItcpPOoweOf%2F8mz10AQ90mK9M7FIWygDTDT65G9BjqkAXBCPFcRzJ8hj95emA%2B%2FmKK6TgdUJ3nCX%2F%2FX2APG7mjKzLU0HZKCs8g0nl2bgmRRZDI5WLIR4A2GC3TUaAorzac7QjNbbJCMOUaKY1v%2BBXVlx8zEz8S9oTWhjJN%2FpR3xt5xHjEpw1vrIigvZ8OagTJYadItZT5Xo3WDLEsftFj7TkzdhTXVKwM7g8QBG8MPBdnj7pGqHAleZPD0400gRa4JOikdT&X-Amz-Signature=dfebb0c5110fe2dd5ce3d2a38e526422528ac7710fb66b5e3498adf8edb9ceae&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVPZWLYV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPd7P2gePqNxsA%2BvM4cYB03KQezBSxBZklzvQAJAkfCwIhAJGqHNyTMww9q%2BXExspzFvSyeqSKqiv3SNT8JvjDErjrKv8DCFoQABoMNjM3NDIzMTgzODA1IgyvVlMGoeVE7qRL1bkq3AMUn6Mjb9yLyyLfFatkN3DyJpklTMz9Re1khQL%2FmBlIyb5K2p%2BsqsRoUyrvV%2B8Er4f6B15t4H7lRAdgz9F2ovamz%2BlV9OqzQz3HSOXwnF3%2BFniaNbX1ihOdY2PnFUe%2BFBhaRWALv40CxHIPkVahcRkPvuSlozw9tXl1QX9F1Auv4HBNTLtdSyVVgwIPrmih6q3Z%2BjH6VzSu2LAgOK5dpjUWAr7yBqRsWHFANEWBQH0GhlPH0MXsodzIepKI2wZ7eRQTfRD5H31fO9VYF30kUQwiceMxEkCfX1bzevngpqC0%2FLz3JrpVyLY9sVAxzk8UN4GYYgGHhGv5id%2BUDycrp419uQi5eouVZncOLB1aD5t%2BpYwidyMdzcyGsrtdLBGlRKAQ6Z8d8mraBRdYtcPdnLqlrT9k9uNqp2vwpFqf60eFu2sN%2FcpIWgi%2FQp%2FTTwxDcUKs69LcCsmt%2FN%2Bwdh%2BiX4PUeO4OUtrUUBsm3UEf2OxImE8Tf6BKJv%2B9t6qEnD5IOxYR5mVyKHUnDuqvrzTWZKv6WA6Mq3TPOLFVXs62qN1TgW%2Boy775Udkk37eeRPbBQGTndil8iadIMutHLgbEfynEzmhQFItcpPOoweOf%2F8mz10AQ90mK9M7FIWygDTDT65G9BjqkAXBCPFcRzJ8hj95emA%2B%2FmKK6TgdUJ3nCX%2F%2FX2APG7mjKzLU0HZKCs8g0nl2bgmRRZDI5WLIR4A2GC3TUaAorzac7QjNbbJCMOUaKY1v%2BBXVlx8zEz8S9oTWhjJN%2FpR3xt5xHjEpw1vrIigvZ8OagTJYadItZT5Xo3WDLEsftFj7TkzdhTXVKwM7g8QBG8MPBdnj7pGqHAleZPD0400gRa4JOikdT&X-Amz-Signature=11755245084c3c91027139249838a653b1cd006b25f8bf13cd654cf41cb824ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVPZWLYV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPd7P2gePqNxsA%2BvM4cYB03KQezBSxBZklzvQAJAkfCwIhAJGqHNyTMww9q%2BXExspzFvSyeqSKqiv3SNT8JvjDErjrKv8DCFoQABoMNjM3NDIzMTgzODA1IgyvVlMGoeVE7qRL1bkq3AMUn6Mjb9yLyyLfFatkN3DyJpklTMz9Re1khQL%2FmBlIyb5K2p%2BsqsRoUyrvV%2B8Er4f6B15t4H7lRAdgz9F2ovamz%2BlV9OqzQz3HSOXwnF3%2BFniaNbX1ihOdY2PnFUe%2BFBhaRWALv40CxHIPkVahcRkPvuSlozw9tXl1QX9F1Auv4HBNTLtdSyVVgwIPrmih6q3Z%2BjH6VzSu2LAgOK5dpjUWAr7yBqRsWHFANEWBQH0GhlPH0MXsodzIepKI2wZ7eRQTfRD5H31fO9VYF30kUQwiceMxEkCfX1bzevngpqC0%2FLz3JrpVyLY9sVAxzk8UN4GYYgGHhGv5id%2BUDycrp419uQi5eouVZncOLB1aD5t%2BpYwidyMdzcyGsrtdLBGlRKAQ6Z8d8mraBRdYtcPdnLqlrT9k9uNqp2vwpFqf60eFu2sN%2FcpIWgi%2FQp%2FTTwxDcUKs69LcCsmt%2FN%2Bwdh%2BiX4PUeO4OUtrUUBsm3UEf2OxImE8Tf6BKJv%2B9t6qEnD5IOxYR5mVyKHUnDuqvrzTWZKv6WA6Mq3TPOLFVXs62qN1TgW%2Boy775Udkk37eeRPbBQGTndil8iadIMutHLgbEfynEzmhQFItcpPOoweOf%2F8mz10AQ90mK9M7FIWygDTDT65G9BjqkAXBCPFcRzJ8hj95emA%2B%2FmKK6TgdUJ3nCX%2F%2FX2APG7mjKzLU0HZKCs8g0nl2bgmRRZDI5WLIR4A2GC3TUaAorzac7QjNbbJCMOUaKY1v%2BBXVlx8zEz8S9oTWhjJN%2FpR3xt5xHjEpw1vrIigvZ8OagTJYadItZT5Xo3WDLEsftFj7TkzdhTXVKwM7g8QBG8MPBdnj7pGqHAleZPD0400gRa4JOikdT&X-Amz-Signature=e4a429da50363af78479b0abe6ab55118277fb8f14520ab401edb1dc4c9bbaad&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=1df7ebbabf4d0d6fa1817d918101f3750aa5879db43d9a4348d984bac103499f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=67b27e36947ad690acb067ad8d2b01adc2557a3be92c39cc6f5dd4b4a47b6727&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=3568c84f6155fc5d3132b7c486655b8d3a781fb8625a3f2b782d9417f94fed38&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=0889963ca5914a23272646020816b4c6d249b3bd942b6d8710f36f9c13268d85&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=1b410addd954b7e358b91c83f03e65483c8b00aff70334e7e439920a04fd1e29&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJNFPBC2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCFcy9YVhGvWMGwkk6PXwKqz11kHMT2si8GPC0YVEF7sQIgCVssdIcVBJCJDws4xNC396SSUOw3CHRX3YnK%2Bjq86uYq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDBt%2FwZewW%2B6qG9rAyrcA%2BeDcxKSbhpeeEaX%2F6sVWcW3tkFP%2BplQqNCmC6IOOL3IwqvcAAFv%2B4UjyyUk5SDf4uSDrbHvjtkG6%2BCv22nyJaoljNvcp8cCxwXIg27FSXjq73j3AMR3UHQs0wu8sRblcsXTHZekCvk3K8HCNnLG0OrQfJcI2K2U17SUNxAlUvYVGz7yTsgV7EnW%2Ftxym%2F9nOVJRTsUkujfIkeiYLm1nafNoGZXPOkAfaA%2B8k41OehCSBeiPUG7dYlJX4jjUzFv88q06NXEbwGhGU6PpumakDs3m3zDE6UOHxbonFr%2FMDkLJ1EXAYfZiP%2BR6zn02sDMEaL8zz7jQpv%2FbTu2TnIi2czeJQ0I9dZITVBYGKPtNq9A67wfs78tFC7Zny0QVZ4rrDrTmgnC3T2tL9bbUGc2LeB5qbb4AEzGiKMms80Q%2F2aL8QlVwypLTUP61pWaDNhbGQJmEood3MNGD4P2zAEFMC%2B52VN8G1zevE0nk8rbuj8OA7DvYnuPI78cc1QapuJ5eD8fFHldhFkJsGVV4Bam32YfTBe67mq1%2B4DlcDHxgKOkryYuqVfqkc%2BNHILAZYV7vCJu8Itm8yrd%2Bnc2IPb236TRl3Joc9JBejvlp34km8y2wlTIYHdmdPb8bVV%2FdMNDskb0GOqUBQn5hPZBmRhU7PdGgokuBP0sJuid0djFx8GqqCVc6M9xa4QzFa%2BX%2Bvjerzoy8M%2BSBBwxINBln2%2F%2BowFHpsjyO8aRt1XfJm9UGsZOpe%2Fftw81xZm4e7GAVO0M4zF4LGaLHmex%2F0avQnedA0H5cK3VFibMvFhr%2F1HBXySGKY%2BFMviB7ByMtpVfUHKfmQNy5twKhOwHm05NLpjFc3f3o0RcPeHwCpsXG&X-Amz-Signature=b678042abaa1ac7cd3e0d061c9c22ff24bc78950a76ecf4463789967109388ba&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBFY25D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCH9np90VAS4nb6%2BtvK7Tbzd6h6ZEGZxEG%2FhgkgnyIQsAIhAO5Knwkh0rzrPVzF55qOU7unMdVG1ZH%2Fp98iXw6%2BmAZIKv8DCFoQABoMNjM3NDIzMTgzODA1IgwBb4NM5Hm4KeRWWcIq3AOmsYuIrQlLmpAGVxQl165GXg5V75H42od3ARrfy%2FpSmh3dzdSTIsajx0kXS2Q64VEW%2FIaYLZUOOvqw16dE1FJ6qPBI1AhyXaEea9zMbQLtA3VrB8l7FW288vThR%2F1gPzaa9lHlbflTFAFDkdkZZGVJfkNVwKcApqRcAyN7drVHZRxxAgXz1nA%2BPi949rVvPDAcf%2F5RDHnCP77VMJ6JSk9kXOD59vPmVPeI9JnYlQlcX9z1rlCngzkm5fFXD3r5cekLmL%2FSSpLqMaq9iOzwO3HYzvpVg9X8OPknA03XVbU823YKkCVmwRRHCGNLc2jgm1o5y5q8bPgemH7Szl921zD4jcQG2E3D1x1cmfLHJRCvpubuXnL42jZN9HqkSZb6QLbX2etIi7wPY4Ew82oHz1U5oUVjp8Nvqc8dG%2FvrSQs%2B0I3SCCl7pNKWJQbnBgK8cMQF13Awc88ZX4J4bicMfj9Iq0vB%2BUXpgBC8USJuf7WAqRFyV3dfG8Vmtq9C7k8ApQ1zdbySLe8pSwfex6bES3hpfXzt59OqUJarVE9XRPIjWTUPEvsGrQjueYPcRhydMRUVyZ3rhiai9N3rJr4nDOr7zC70eEMlEGeUzgFPsV%2Fxsru0ZIieBLePNUCSMzDx65G9BjqkARk3BXe3puva%2F9nhw4tlxPSCf%2Fsd0IAPGI23%2BJSJI5SW%2FJs8S3cUQoC9Ua5tQ7KoqQeBx12xsXUkY%2FEsv7OaHiw7rKh1R6S2UlAT%2B9TbmMwrl4uZVLl6lzlJo0A%2BMQz0pAp7ANuCxfFw2iiImnvrQaITotRiRT7vcmmyzzcHSDkKZ0oF%2BLhsdiPJgWR6D7TLK4rL2dcYeKOci%2F526m3UuJ5pxYah&X-Amz-Signature=1e924a5425398362dcf1e142351096bf2ce99818bf455689705e9e8aff93f8c6&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBFY25D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCH9np90VAS4nb6%2BtvK7Tbzd6h6ZEGZxEG%2FhgkgnyIQsAIhAO5Knwkh0rzrPVzF55qOU7unMdVG1ZH%2Fp98iXw6%2BmAZIKv8DCFoQABoMNjM3NDIzMTgzODA1IgwBb4NM5Hm4KeRWWcIq3AOmsYuIrQlLmpAGVxQl165GXg5V75H42od3ARrfy%2FpSmh3dzdSTIsajx0kXS2Q64VEW%2FIaYLZUOOvqw16dE1FJ6qPBI1AhyXaEea9zMbQLtA3VrB8l7FW288vThR%2F1gPzaa9lHlbflTFAFDkdkZZGVJfkNVwKcApqRcAyN7drVHZRxxAgXz1nA%2BPi949rVvPDAcf%2F5RDHnCP77VMJ6JSk9kXOD59vPmVPeI9JnYlQlcX9z1rlCngzkm5fFXD3r5cekLmL%2FSSpLqMaq9iOzwO3HYzvpVg9X8OPknA03XVbU823YKkCVmwRRHCGNLc2jgm1o5y5q8bPgemH7Szl921zD4jcQG2E3D1x1cmfLHJRCvpubuXnL42jZN9HqkSZb6QLbX2etIi7wPY4Ew82oHz1U5oUVjp8Nvqc8dG%2FvrSQs%2B0I3SCCl7pNKWJQbnBgK8cMQF13Awc88ZX4J4bicMfj9Iq0vB%2BUXpgBC8USJuf7WAqRFyV3dfG8Vmtq9C7k8ApQ1zdbySLe8pSwfex6bES3hpfXzt59OqUJarVE9XRPIjWTUPEvsGrQjueYPcRhydMRUVyZ3rhiai9N3rJr4nDOr7zC70eEMlEGeUzgFPsV%2Fxsru0ZIieBLePNUCSMzDx65G9BjqkARk3BXe3puva%2F9nhw4tlxPSCf%2Fsd0IAPGI23%2BJSJI5SW%2FJs8S3cUQoC9Ua5tQ7KoqQeBx12xsXUkY%2FEsv7OaHiw7rKh1R6S2UlAT%2B9TbmMwrl4uZVLl6lzlJo0A%2BMQz0pAp7ANuCxfFw2iiImnvrQaITotRiRT7vcmmyzzcHSDkKZ0oF%2BLhsdiPJgWR6D7TLK4rL2dcYeKOci%2F526m3UuJ5pxYah&X-Amz-Signature=2a419209a83b3ebbac02adf19a547bb9ddc43cd6c1744e6c0d2ab8ef1fae7d57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA6Y476R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCDpNLSQ%2BWTc3eibPf6dPLi4Z1lRNB6h5xCPmOxdZB6bgIgH8dmrfW6ajNzeUTrQ%2Bzhpt8q0ZJDZbZuH%2FGBzAhwe%2BYq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGDLXkqs0sPkw%2F%2F60CrcA%2FfsYLsiZCehEJNXdYmH3g5wpJ6HQgW8OWxDXvqOPgN8LGgbxnFRcibhPWGP4ozJuXk1auXpmSE2ndx%2B5MQUOISJ4fTTU3prc3VAlivu692o%2F4Y7SXxnsyXrA2Jbs%2BO%2F8t%2BBEX4%2B%2FryZKySODHJ3kK88n7hFbYtFMAouQ%2FNvYbJqpJh0Eobi%2BgI80shlG0HFMv0CI%2BBOWQT%2FnhV1OzxLaE2yfG8z9v0zl%2FyEjzAXv7XBOBgFDU%2FcpO3tDKyY%2F8J6q%2BQPJmfclTCriTKTvvs3W9hVFKy3F8%2F9nDIGUUBl5dj4%2FYILwj6Zvw9GlF5VlzYnrNB%2BvMNClkH5b5mglkRUBbr8TrpUKrNtNxV%2B1xW%2BlgSzgiZHuiGipdjUzIyPrH5ZgQ8gvntVnN7kK8Nh2uC1zaYiSOHanUZdjv5Sn58Oe3TXwKRSYBvYX%2Ba1GhTLH9AXmRADYr68mS7NlIjf92QUZETeIvEyykxm%2BpM0ogqvUC8YiuobU6MBjEGWo5HjQK66JNnflGccF0AxBLd32lEG52oPCzWqv8NtDutJxSLo29nuviK%2FQO%2BqX%2BM2TYJ%2Fc%2FcMC5BpnAqbvaDbKBNfjpDaJEvwarJCLozZICrwj2Nl%2BCvzgsrQqonnt%2FZFbOBHMJnskb0GOqUBNRB8pvlvBVlvZ3q1FCwKAC07iEm5Tb4ubbH%2Fb9R3PpkbgT%2FCXpGr6QNnS9nouCAB%2Fd4SlJLuOZT0XQlJj4cs%2FTqjO6QFLxVkjdFS%2FQSATvut%2BKu%2B80CW00065Lql6y8XBcTUDb0kvVGwXzIJkPCrUolB%2Bcemrvq1BEV45ytQ4XgsdL%2FIpQ8zXyCoNNGq3pbF3WTueRa3TTFrM0aVpYsMLWbz7%2F2v&X-Amz-Signature=1444ff028b5e3cf1007c9cd2556bf2a531ba02acc102c2e5c1f0fc785e8b413c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=7fa891fc35d144ac183c695a8e45a2ca8cce5e8d21e614eadc101dacc7b06db8&X-Amz-SignedHeaders=host&x-id=GetObject)
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