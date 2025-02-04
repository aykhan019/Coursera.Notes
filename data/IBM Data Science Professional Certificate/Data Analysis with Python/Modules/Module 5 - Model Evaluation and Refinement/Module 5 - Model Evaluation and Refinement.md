

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=f90cb5f79bf3d8ff5a6143a59fa2b91551aa3df931ba7b336e356ac3dfc82e82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=8fe90d6c7a183d9f53f85414d3ce3e93d2762c1683da5b50931e004f5fc6bba0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=4ee31a5e1137999a5c6fe8cef9627ec3b931a7f178b9a8a6b752db37d84986ff&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=f072bc193157a37c19ae9f906cca1d1b30b8b87208fd6aef59750f57dc59cdb8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=6244d6ab76a54af49d636594964a42c9eed6b92edab9a196781ceda4776a2f9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=f0803ce3a9dcb7728f655b4a9cd7375da8916371104a948389c3d0cb7572ac22&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=a18996790886eb45e97350cb53a78fb75e5c89bcc39fd61d1fb89b81cf05960a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=1466adcf8c900bf7b1ecd6fe51801900b21f780bf2a8e2fdb259a4ce7cdfc6ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=c7001fea0c896935324355dbe47a9085edb6d411cb21ba5ede050d281f15fb7a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626QEJPWR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDuIObB2KNYtjlQtFgs0YI0RYFBjPSX1qx0BPjCTFW6fAIgRMmFCcCsD8JELFvOKmGdUx34Vn6VwqsUs7h6MIOFLtIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDBGkR6UEtL1r0KtqhSrcA2YM%2B%2F8PE1akXoYAkZKPsamsQSufE19HUTexOXK1hnXgLZb%2Fap41v33KEG7PfxX%2BQQdV8hAk5ZySUuCiRk5MXMLBuhVZzkFCkPXF%2BN1ag0cY4%2B%2ByL5Oqo4%2FPPuMaaVZEI70KY9nWnijI6WDRrdec3pYmoTCmg6JYVKCgT6%2B21kOY4RNUnuKObd2VsqUt0am2GSF9m%2BZPtsnrWFvVT8y35fya0YK7Zl6sXz9etJKZEr2lMZVZKUWJN19m7ZC%2BKiRFxhJ9EUpKEim1YjQ09Tw%2FDjFpBUiutByGH6zbzzhu9t%2FtTm60dVec6ZfDV8qKwZ8KFG0F2buDj1fXrxMvSiRKaSUYbiUWKz7G1yPfX3HaDZvUGDVeVIXK5wUUeH6psrQeXZTpjMGFp9XD8ccUPPGaoV1PJxTFA7synvGY5Nf7jRVYHFTOR6Lt2NUMbr88%2Fv0oidwLT2Ae8uJdpDClkXCZ2keC%2BXbqUCsDJvEpimLpuV2J8GmIdbVy0J8SrXUylCJXRzE%2BvFBeq3Fc8RDioEFXZmeinfb9mkj%2FPNFwtxGIe8iwPPhy%2FIlF%2B67bRqccg2wmB563tqTnXT%2BWb5JJ%2Bqq3aKvjYSus%2FH5Ftd%2FmxfXV%2FZxF2iCHv%2Bk4lW%2FnCUz0MKnphb0GOqUBhr5bWX7jUUQ4KUDWS1f71bqW%2FzyXE2wxLYRi7wnxZ9GX7k22WW%2FeF1X08XA%2Bu%2FOYd%2FkIlsjumMOcJtSzMb32yJNc8evA9CJq5%2FfD7MzPaeIVww6xr0tY6b8IRVThrvmMJlZDDecm3CSavTKaM94uuhu8HIQOCQe3SccsmLa7JuVBSeZB8W98a8at6wL7%2FE%2FMGuzm4SSr%2Fw0o78kRzbc9vxuQSttg&X-Amz-Signature=3192120fa44a41374686c8c6679a137c8be819b1c012fbe856146927740c3190&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626QEJPWR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDuIObB2KNYtjlQtFgs0YI0RYFBjPSX1qx0BPjCTFW6fAIgRMmFCcCsD8JELFvOKmGdUx34Vn6VwqsUs7h6MIOFLtIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDBGkR6UEtL1r0KtqhSrcA2YM%2B%2F8PE1akXoYAkZKPsamsQSufE19HUTexOXK1hnXgLZb%2Fap41v33KEG7PfxX%2BQQdV8hAk5ZySUuCiRk5MXMLBuhVZzkFCkPXF%2BN1ag0cY4%2B%2ByL5Oqo4%2FPPuMaaVZEI70KY9nWnijI6WDRrdec3pYmoTCmg6JYVKCgT6%2B21kOY4RNUnuKObd2VsqUt0am2GSF9m%2BZPtsnrWFvVT8y35fya0YK7Zl6sXz9etJKZEr2lMZVZKUWJN19m7ZC%2BKiRFxhJ9EUpKEim1YjQ09Tw%2FDjFpBUiutByGH6zbzzhu9t%2FtTm60dVec6ZfDV8qKwZ8KFG0F2buDj1fXrxMvSiRKaSUYbiUWKz7G1yPfX3HaDZvUGDVeVIXK5wUUeH6psrQeXZTpjMGFp9XD8ccUPPGaoV1PJxTFA7synvGY5Nf7jRVYHFTOR6Lt2NUMbr88%2Fv0oidwLT2Ae8uJdpDClkXCZ2keC%2BXbqUCsDJvEpimLpuV2J8GmIdbVy0J8SrXUylCJXRzE%2BvFBeq3Fc8RDioEFXZmeinfb9mkj%2FPNFwtxGIe8iwPPhy%2FIlF%2B67bRqccg2wmB563tqTnXT%2BWb5JJ%2Bqq3aKvjYSus%2FH5Ftd%2FmxfXV%2FZxF2iCHv%2Bk4lW%2FnCUz0MKnphb0GOqUBhr5bWX7jUUQ4KUDWS1f71bqW%2FzyXE2wxLYRi7wnxZ9GX7k22WW%2FeF1X08XA%2Bu%2FOYd%2FkIlsjumMOcJtSzMb32yJNc8evA9CJq5%2FfD7MzPaeIVww6xr0tY6b8IRVThrvmMJlZDDecm3CSavTKaM94uuhu8HIQOCQe3SccsmLa7JuVBSeZB8W98a8at6wL7%2FE%2FMGuzm4SSr%2Fw0o78kRzbc9vxuQSttg&X-Amz-Signature=47f81a6aa58415833fb572bc857f50377f641df27090ad29d32c1a2ad638728f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626QEJPWR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDuIObB2KNYtjlQtFgs0YI0RYFBjPSX1qx0BPjCTFW6fAIgRMmFCcCsD8JELFvOKmGdUx34Vn6VwqsUs7h6MIOFLtIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDBGkR6UEtL1r0KtqhSrcA2YM%2B%2F8PE1akXoYAkZKPsamsQSufE19HUTexOXK1hnXgLZb%2Fap41v33KEG7PfxX%2BQQdV8hAk5ZySUuCiRk5MXMLBuhVZzkFCkPXF%2BN1ag0cY4%2B%2ByL5Oqo4%2FPPuMaaVZEI70KY9nWnijI6WDRrdec3pYmoTCmg6JYVKCgT6%2B21kOY4RNUnuKObd2VsqUt0am2GSF9m%2BZPtsnrWFvVT8y35fya0YK7Zl6sXz9etJKZEr2lMZVZKUWJN19m7ZC%2BKiRFxhJ9EUpKEim1YjQ09Tw%2FDjFpBUiutByGH6zbzzhu9t%2FtTm60dVec6ZfDV8qKwZ8KFG0F2buDj1fXrxMvSiRKaSUYbiUWKz7G1yPfX3HaDZvUGDVeVIXK5wUUeH6psrQeXZTpjMGFp9XD8ccUPPGaoV1PJxTFA7synvGY5Nf7jRVYHFTOR6Lt2NUMbr88%2Fv0oidwLT2Ae8uJdpDClkXCZ2keC%2BXbqUCsDJvEpimLpuV2J8GmIdbVy0J8SrXUylCJXRzE%2BvFBeq3Fc8RDioEFXZmeinfb9mkj%2FPNFwtxGIe8iwPPhy%2FIlF%2B67bRqccg2wmB563tqTnXT%2BWb5JJ%2Bqq3aKvjYSus%2FH5Ftd%2FmxfXV%2FZxF2iCHv%2Bk4lW%2FnCUz0MKnphb0GOqUBhr5bWX7jUUQ4KUDWS1f71bqW%2FzyXE2wxLYRi7wnxZ9GX7k22WW%2FeF1X08XA%2Bu%2FOYd%2FkIlsjumMOcJtSzMb32yJNc8evA9CJq5%2FfD7MzPaeIVww6xr0tY6b8IRVThrvmMJlZDDecm3CSavTKaM94uuhu8HIQOCQe3SccsmLa7JuVBSeZB8W98a8at6wL7%2FE%2FMGuzm4SSr%2Fw0o78kRzbc9vxuQSttg&X-Amz-Signature=015abc2bd0ed1aff9b0881ee7ef059fe8bc8509824b520581bd796db673c6c00&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=257e99d3284f04cc372831fe47b31791f7993507e2b5430f601c0125f3afd233&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=5ea793293bae727137eeccecba542d99a96a1c6d2261cf4435cf7aac225123e9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=775625093a5f4f58e3b699596556bb1f044483b8be948ce867eb8e27e09c273f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=ed72b2108f74fd2fe23758aedd4a13477afb25989d2416009fcd1a118739d496&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=3d027730741d949a5bb3995aaef5a13dd0a1ed97fe9607b6b30c59a24a840d0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2LXJFNQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIDS0vG0gciyek5h6cs0nUMVd0l0POJS3en%2FnXsA%2FMMnIAiBQTRtkcKpJLqPJU5YHYWEsMmmvnsqeX4oWqODF2BS%2BMir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMlOFL5nr2cD8i9eyVKtwDmnOCGoMP6p8PsTGMtFtBlJj2RFFJFPLYD2Ez7eFBfD1PNMv%2BDBbtvrCjQ76vwuV6uqxptwTKYfqgrMyIK70YZpyOUggd%2FVNYb5FG81%2F3sFMd3ZXuja%2BODssM7dDkaBn22mknoGtCoZnroT9krqbHJ4hsaJi5q64saIRW7q9zSw3gvUSWXZwcWsts3eqQ6d6aexTH25VieBIiO1pEeIB9lfvNEY3U%2BkA%2BAAzEkZah4TquAgBvva9%2F3M6mxEa4ys4jkszs4VqJiHQild8emcw3LdSvwkYEvOb4vkrV%2BuW%2F%2BQ%2BQWt23Y3PM%2FeLNaUbOxnnjfVjVSoUyQpNjKy%2B5YCR1EsmDdvjCqSUIlQjjlri%2BXFjq%2FExovlF7lXv72%2FSMM72lzwRbKEC14Y86dxcmgDNxbwIoepPGYyiXPLG1Kb1ypdicErAl4QdsW25%2BFqaLqCNSR5GwdvOGEMg096wjPpW%2BRpDb9aGeHwC6xcHb0J9y7%2BMEEkpWoz8gV3Re5AS50rRHjnQPJI6eqIrZkCAj8s5qJE1Z3txitKzs8l%2BwajY3kWBlorTOzlTROxif0vSblIF7G1G64mIt1oTYmzvPl3EiNbgRbXo%2Bka9Z%2F27ikMv4CvviPtyZtSkCjBupR5sw6eqFvQY6pgEvWqk0KwX7D%2F3kDrA8LofygmKRh3a1N6oX6rxv1K3vnKEr6ru12Mv4YvBpMuX%2FF1%2BSmI8wsCuVXPF5od%2BxEIIB0CbY1FduwyVsRJu9mQtsQylUUSNmECbPw1TBMhD3dhBKkH0uFP9GHSUkIzw5z%2BtkLx%2B3fkG9WWdRkp2hZ%2BBTRqUyUrTEA5xxGxiDeNZy26LxCdeoNCN0EqM1Hji7fhB5hxyZ8ads&X-Amz-Signature=cafb5cfc782c523cad40f4c18b4dad0edaa7cfa36cfe2140124a570e6567de68&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENVQEQK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIF05n%2Blq1cCykh6VwiqalbwnluasQhrbv6LvEXUlrRxHAiEAlio%2Fcfwk2TG%2F0U%2FETAEl8L5aqstO8Qa%2BTYdvF8OkZUsq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGsX5NWUJM37cfSljSrcA%2BLtpHCFeO7Qd56bIf2bCWqxnzyv6oHLqMJEtYZvypOBtchPiSg5da%2FiKdFwPsrUaNB3LW96stO9K7p%2F3mBj2EtI3XkATJsdeV1cm16aMPT5e7tgJz864IgYfAQZ9rJGJqdm7QIf97mGKpq5K1SdqaJWR7767UFdIvecN7O72MhV%2FI1NMzuxK%2FGgMFEkJCb%2F27mioXOc95itU%2B0ab%2BgUBMJZJXj%2BcXb7GVEe6M2iWMdpoOENBhJPA9oUl4vg1iCcTa%2FHGnBtqMIdsJIQrPVzk694nd2ZhpG1jmIC849ykX%2FihAaXVVT7dGxLcmnYL5EIfPh4ck5orD8pNUR1%2F9jilvDnkmPpKZttU%2FheKBKBlbOI284Pb%2Fq%2BM1Zv6TiPVFtDeFaCZi4mSndQypZxfCzVvBIeUMn5z3T%2F4c1NmGSPtSAAmMLZ%2FN%2BKrC2UfJkrrTEpT33SHdpnh3tBFfdWzr8klxCDyFQk9my%2BPYUXKALSlB%2FOTD31%2FCQbo%2F9IW397wSai5EeZ%2BguUAjaSbI7TpUzHSCQlFkCqHAYEqnYNa5YnCNisNXmeq9NXOfEwPNomu0%2Frv94gT2K8LEtXw7ookGUYLURVmrZQnUZa8VP%2FMUFEF%2BsDP5MoUqhtXEESUlerMLTphb0GOqUBNidSvbK54LWs9%2Fn6WEZ%2BEMwsdCGPCpo4d3LCoEvE816lDAEVFAuCU93JGJ3lH36HRu194cY79AsbbtQxMrmxW1ejB%2BiCUjLkvtIvg4uqltlBTtn4WsADtcC9iCLYZgnTRWQvnpaavu8Ybr8TcSFi7phQB0LQkfd4qU7aKIJXMWPk%2BpRZzbfcrxKFHHE9E5HBBSPhjgMMhikjCsX4RM3RSQyizfnS&X-Amz-Signature=938572fb4aef3d16737c8d2268d5e825e2a575a5b4c436786b5e9c2ce5161546&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ENVQEQK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIF05n%2Blq1cCykh6VwiqalbwnluasQhrbv6LvEXUlrRxHAiEAlio%2Fcfwk2TG%2F0U%2FETAEl8L5aqstO8Qa%2BTYdvF8OkZUsq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGsX5NWUJM37cfSljSrcA%2BLtpHCFeO7Qd56bIf2bCWqxnzyv6oHLqMJEtYZvypOBtchPiSg5da%2FiKdFwPsrUaNB3LW96stO9K7p%2F3mBj2EtI3XkATJsdeV1cm16aMPT5e7tgJz864IgYfAQZ9rJGJqdm7QIf97mGKpq5K1SdqaJWR7767UFdIvecN7O72MhV%2FI1NMzuxK%2FGgMFEkJCb%2F27mioXOc95itU%2B0ab%2BgUBMJZJXj%2BcXb7GVEe6M2iWMdpoOENBhJPA9oUl4vg1iCcTa%2FHGnBtqMIdsJIQrPVzk694nd2ZhpG1jmIC849ykX%2FihAaXVVT7dGxLcmnYL5EIfPh4ck5orD8pNUR1%2F9jilvDnkmPpKZttU%2FheKBKBlbOI284Pb%2Fq%2BM1Zv6TiPVFtDeFaCZi4mSndQypZxfCzVvBIeUMn5z3T%2F4c1NmGSPtSAAmMLZ%2FN%2BKrC2UfJkrrTEpT33SHdpnh3tBFfdWzr8klxCDyFQk9my%2BPYUXKALSlB%2FOTD31%2FCQbo%2F9IW397wSai5EeZ%2BguUAjaSbI7TpUzHSCQlFkCqHAYEqnYNa5YnCNisNXmeq9NXOfEwPNomu0%2Frv94gT2K8LEtXw7ookGUYLURVmrZQnUZa8VP%2FMUFEF%2BsDP5MoUqhtXEESUlerMLTphb0GOqUBNidSvbK54LWs9%2Fn6WEZ%2BEMwsdCGPCpo4d3LCoEvE816lDAEVFAuCU93JGJ3lH36HRu194cY79AsbbtQxMrmxW1ejB%2BiCUjLkvtIvg4uqltlBTtn4WsADtcC9iCLYZgnTRWQvnpaavu8Ybr8TcSFi7phQB0LQkfd4qU7aKIJXMWPk%2BpRZzbfcrxKFHHE9E5HBBSPhjgMMhikjCsX4RM3RSQyizfnS&X-Amz-Signature=b7de600116db77002d99dc65d5190716159773c996bb78e57181925cc271056b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EIBCWY5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCj7pClW%2Br0v8qfuBXqCmlYW2jc4jWsZaTVY1YfJxd6igIhAImsTelMLt5OXUDQRV%2BL5Lh4jG%2Bkuekq9WQOBncOtUb2Kv8DCCMQABoMNjM3NDIzMTgzODA1Igzkd3R855MYGIxFA0oq3APBAxxbyGOGdI54wb%2F95kiCAZW6VrTVDhx2F0AyQ4eC%2Fk3WMEsaK%2BPvgGieVcIYQp73ES8YEksAMVSNtALlAnLGQzGRs%2F6wetylu5Jpw7c3Su4X5s23%2FxVCdJNAy4wDpLo%2F3WVYwK%2BiqP2NuoEFfBPczbDzUWVfIVVu2gJB%2BkKM8rl5mfE%2BC%2FOwNNOkRKQzBBUbcC8ghMnpiv%2B9mOCf1Jh0JvitCFfYHmlpNexC1RA5JS3P%2BlMU9TdM%2FT%2BQLDFp%2BNFYsdlOuCDQu3SfbyDiCr5qHYzfQpZceo%2FmqmoA9vu9GvGqfZSPZd2aUuP6NqlC%2B%2BbPusY5KqZu97ZKjjbLX5ZKjAUnLNxUu2nV2VdyTSH9pikz81EQRYHLTPGWtJ10sNvt336ElkWpEV11pBI84J0vNnmzA38S1aWp1ivzPLgJ3QLLxXnq9tZFqe%2B1%2BGpe7%2BwI%2Bmnwl%2F38BJrXMGp5qW2PzcdVixU4gvFypftcX8FKqHof%2Fx%2Fvrry6aaFdABPt1as4WrQPHHXG38rHsckHy8vsg9Z5uAQtKZcm%2FywCRX5xIc3N7CL%2B%2FBXXzFG5T2ZiUUqeXdTESWLdhSUWkQHBAOAi%2BWkKKSEGXDOxqsY6UAvWL12yJRdWJEPZxh9nHTDP6YW9BjqkAcRj4xiYtwshpBZwDwWQAmupGt08eDsypFkKuvBv9WTJDlRclzULFxnyqwrkxRqXunPad1D6hO%2FaYInZOdjgXWK3zI%2BfEdNgKFK2uZywu8ALiYSgnEOzSAvIAL9%2FhpijuKuWNh895m6bAA0mFVtAF2cidu4clIGkNb2LC3Y2ro%2FXxDpCpjKAUA1cfOWRgtHm4jRi%2F0OuWc7ToecRXeUjRDThHYeA&X-Amz-Signature=6797db267a2db35c66403751d02bfc909fd65846c0bccce90d047cecaff248f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MXE3BHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIC0PVWd05Ryli5d7gm6BPathfqucbHvGel%2FoM1yq5lS7AiEA32SJocgyP9sfL875nkJIBqAxPDu2Y%2B88S0h2H43FfJIq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHHJ2Y2hErQ%2Brz1H%2FCrcA9oB%2BZSpeRo3YM0cQ5BVh5GcKXXzBEP6l8kzr975xq1AdWxY6PlOnVXY9yG%2Fj0DZU53L2Z2vNu4zwwNfSHzzX6rrjslM9br07sWGUoK8UNNuSmWkGKWnZbz1luWh%2FmEPddJhC4mTDhyg5ETTmdwLcgsuGsjehmVh1SlMuR%2FPlWWeJhJFnON4qGtJ1cXbYVr96HjBApS1t3dBEP7NInbKYNWgzSfNLcMsJMJsgJV03uZYMeVTsxYhkYJOHPc6WvyXJxU1xz0puCKXQnv3jjJGdhaKaPvlfkguj42ojZkeVTZkJ7sV3ql6%2B%2FIC%2FUWczNLb1MILzJkgWrrgm%2BNvOeO6qskuHVkFNKSounThN422zwyUCIGIlRZb%2Fa3g3mbw4i3sOoTPdiSuGL6kEUeeI%2FgCohhqQsKWriru4ztCZngADXlEkq7hNNbGw5yaEAD4TEdsIBi6R7YDj61Cl6U7CJCWkrNdyzV%2BEezA%2Foev9AzC2lkeINGaVQf3LOWfhONmoYEvy1khKtInUVkb5Oy0OlQw2jIrROiDTurCi3sL6GreMeiRCrq5n8D%2BZQUR3TqWcDwlPqjhCNPHKSB9m8aqH7%2BN98Zb9bro%2FS%2BPQBZ1UdJC0ydoISnG2Iw1pTarh8HkMNDqhb0GOqUB9C5%2BVSkP9a0jjbTjC4bLZM4fSJtvuppk%2Fe31MmjJbh%2BQTVdKq%2FS9OJYOGXC2NJSWGxMO1b%2Fl%2BVZabegr17FXhcQX9O52KRds%2BTn%2BGBpR6ECxdM9kZgPMJCcadyVDSGmJCNBnSPDAUSfvlLFSiOuJVVL25kBEax%2F57CobSdefa%2FK3rhN8w%2B6%2FT%2FsjcScyqRbGqfFH%2Fw54VHNlP1BkUfoG5GqDP7Cx&X-Amz-Signature=16746ee947e9c5fb74c00cdbd3d573c2c564aa8ff520e9ba792688f249714328&X-Amz-SignedHeaders=host&x-id=GetObject)
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