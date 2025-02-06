

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=5b55fe2f8a556da83554dbf2aa4e2121cdc0d06aabf4c6313a8e3ed20436e39d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=56fe692288ba74bedb41bf42d6f9660301743a736925823a1a48b9b30f12b274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=ba3af56437d511537b0251fff1f006015e6efb3baf73a1c0ca6db799425e4038&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=9edfb9724cb9010cc1254b5e0281178da798ad363b21c5ebfbefa49a57010c4f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=d8da6ebc706a427845743b6597709eb5c148286730787d485a89dfa9a12d9cdc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=d243249c7c0436a5c1027b83c4b8ab951773acfc9aeee0431daaac301e0d5212&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=637d36fae9e40529b6d6ce0e8ae31cb09ea441c1ac4f81d5e7ef71129d24d136&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=9b235273a07387d1eea281fbf0255b88c9bc2a6ac5f47592bf5f4ce6c57609f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=42220d14fb689528c40bb1a7ab8ddd913e67f4f27473756379fef617792af9aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM4G44IJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHNtpLC6F%2B64uSqKfq%2Fam2T2Q9iKYM7I5sEQoXcWkvRGAiEAtr8wvwl%2BUaVYIIizL052a72T%2BXjHjsfnCh0uKA5XvDcq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCPSX1%2Bc07Mz06AW2CrcA6b1COBywumTudqJFcQX7%2BxsSTPVqhTimT3Fes8%2FRtfhVUP96dnZQbhx76r7EmPFZB94F%2BJTsTRMWK%2Fdri9DrBm82CILh%2F3U5XaPFmiASL9%2FGXBmGcfVt85J%2FK8fgpvEHt89fB4kQQqOZ4VPcvPoqCD3zp%2BBGv1s8xhd0f6snvqPT7dinkW6044zs4ME6mGE5l5P2HmyPnPfkTKoTEoZuTGX8JDV1qhwp2mhlZNp1PbOgw3sY3TcJGC1McJEGWdvcvTRP0Wn%2BKbyaEqq024FQvNXzBoJQhiKpgBnLFHg3nObNuOjAip18y9EOSzyOcx34lN207WoQHptc50BQZJ4Dzw6QWokM5sl3iCJM%2FiXIswn6d44W8y4hKQR8D%2BZTJiBN8sLTo8CR%2FASv7vAzHGKyelw62o9aRHN6fmrW9yWDHkwvLiTgKkfCeFVt9jyxtCtFp0STTU7FZfTSpfQGQYAvJDollLwTI44DSYQuwiyd%2For9arspzcbUbsjqYgKV6AU0C9ZfM6pqqXCz5kzZQXazMncq4vTIUo8gC12sHS2P8xyDQqgmXRcDERyzqCorSwltNSK6HbwkD3cHCyXG7Q7%2B%2BHaFnUKjYDZEkGX8%2FzLpAzvh4V7X1FmcmamNpwOMNP7k70GOqUBJuoYOabiSbodxXUlpZ6Is3rdwknO38ndpq%2BS4x4f%2FB8RsvQR6L0KlSnTiwjPDj7GmjAr%2F5Vc8k9p8lu09eOBldWbVKrmuaY%2F8SX95Z93KQ7DE7Wm2KyJiY38T9oKkMWkxLSYHpNDKp%2ByulEMQUTtMymtzELS4IX0TRYjGhTFixGutK4ZtwVFIHPEwr9uXPh9acLMyIXSl4vcD3%2BHF1pW5J3xvI8V&X-Amz-Signature=5088fffe1461f6a610159446915969789fbb9debe4e36f5028fb20f37a4c13f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM4G44IJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHNtpLC6F%2B64uSqKfq%2Fam2T2Q9iKYM7I5sEQoXcWkvRGAiEAtr8wvwl%2BUaVYIIizL052a72T%2BXjHjsfnCh0uKA5XvDcq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCPSX1%2Bc07Mz06AW2CrcA6b1COBywumTudqJFcQX7%2BxsSTPVqhTimT3Fes8%2FRtfhVUP96dnZQbhx76r7EmPFZB94F%2BJTsTRMWK%2Fdri9DrBm82CILh%2F3U5XaPFmiASL9%2FGXBmGcfVt85J%2FK8fgpvEHt89fB4kQQqOZ4VPcvPoqCD3zp%2BBGv1s8xhd0f6snvqPT7dinkW6044zs4ME6mGE5l5P2HmyPnPfkTKoTEoZuTGX8JDV1qhwp2mhlZNp1PbOgw3sY3TcJGC1McJEGWdvcvTRP0Wn%2BKbyaEqq024FQvNXzBoJQhiKpgBnLFHg3nObNuOjAip18y9EOSzyOcx34lN207WoQHptc50BQZJ4Dzw6QWokM5sl3iCJM%2FiXIswn6d44W8y4hKQR8D%2BZTJiBN8sLTo8CR%2FASv7vAzHGKyelw62o9aRHN6fmrW9yWDHkwvLiTgKkfCeFVt9jyxtCtFp0STTU7FZfTSpfQGQYAvJDollLwTI44DSYQuwiyd%2For9arspzcbUbsjqYgKV6AU0C9ZfM6pqqXCz5kzZQXazMncq4vTIUo8gC12sHS2P8xyDQqgmXRcDERyzqCorSwltNSK6HbwkD3cHCyXG7Q7%2B%2BHaFnUKjYDZEkGX8%2FzLpAzvh4V7X1FmcmamNpwOMNP7k70GOqUBJuoYOabiSbodxXUlpZ6Is3rdwknO38ndpq%2BS4x4f%2FB8RsvQR6L0KlSnTiwjPDj7GmjAr%2F5Vc8k9p8lu09eOBldWbVKrmuaY%2F8SX95Z93KQ7DE7Wm2KyJiY38T9oKkMWkxLSYHpNDKp%2ByulEMQUTtMymtzELS4IX0TRYjGhTFixGutK4ZtwVFIHPEwr9uXPh9acLMyIXSl4vcD3%2BHF1pW5J3xvI8V&X-Amz-Signature=317507935ad3ffcaddfc9e500af73afd244d3f003865154cb4358b6ee3716ab4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM4G44IJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHNtpLC6F%2B64uSqKfq%2Fam2T2Q9iKYM7I5sEQoXcWkvRGAiEAtr8wvwl%2BUaVYIIizL052a72T%2BXjHjsfnCh0uKA5XvDcq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCPSX1%2Bc07Mz06AW2CrcA6b1COBywumTudqJFcQX7%2BxsSTPVqhTimT3Fes8%2FRtfhVUP96dnZQbhx76r7EmPFZB94F%2BJTsTRMWK%2Fdri9DrBm82CILh%2F3U5XaPFmiASL9%2FGXBmGcfVt85J%2FK8fgpvEHt89fB4kQQqOZ4VPcvPoqCD3zp%2BBGv1s8xhd0f6snvqPT7dinkW6044zs4ME6mGE5l5P2HmyPnPfkTKoTEoZuTGX8JDV1qhwp2mhlZNp1PbOgw3sY3TcJGC1McJEGWdvcvTRP0Wn%2BKbyaEqq024FQvNXzBoJQhiKpgBnLFHg3nObNuOjAip18y9EOSzyOcx34lN207WoQHptc50BQZJ4Dzw6QWokM5sl3iCJM%2FiXIswn6d44W8y4hKQR8D%2BZTJiBN8sLTo8CR%2FASv7vAzHGKyelw62o9aRHN6fmrW9yWDHkwvLiTgKkfCeFVt9jyxtCtFp0STTU7FZfTSpfQGQYAvJDollLwTI44DSYQuwiyd%2For9arspzcbUbsjqYgKV6AU0C9ZfM6pqqXCz5kzZQXazMncq4vTIUo8gC12sHS2P8xyDQqgmXRcDERyzqCorSwltNSK6HbwkD3cHCyXG7Q7%2B%2BHaFnUKjYDZEkGX8%2FzLpAzvh4V7X1FmcmamNpwOMNP7k70GOqUBJuoYOabiSbodxXUlpZ6Is3rdwknO38ndpq%2BS4x4f%2FB8RsvQR6L0KlSnTiwjPDj7GmjAr%2F5Vc8k9p8lu09eOBldWbVKrmuaY%2F8SX95Z93KQ7DE7Wm2KyJiY38T9oKkMWkxLSYHpNDKp%2ByulEMQUTtMymtzELS4IX0TRYjGhTFixGutK4ZtwVFIHPEwr9uXPh9acLMyIXSl4vcD3%2BHF1pW5J3xvI8V&X-Amz-Signature=5840072accdce649f1ba9603b58a04ce527b82a4007720908765e759e2f57b8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=16f64fbd35c928ee1aa97ba7e051fe90e85426150d7bfd1513b448981bcce210&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=14ace9c0394524c0af1015c302493f2e435b1d9f2b9e5384fb7d682d8709fb93&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=3c8c16b69ca4d024512f54eb5fa6f2e754d9340b4a71d27353f2257a3600c224&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=b5a4b6d38f5104f62d5cc7b775b99adf0c0accaf1f20d9c28f68803badd49378&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=6764c7147ac3bc5e17ce842be850c072ea6411b8c7bf9afd2d770fb22508313b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D4UZTKG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDhCTetQZFHBwAKranakWEeKUCrr0clhU68k26HJ09%2BYgIgMkS7E8DdxiV5BcXrAGIMgxSr2iQPd6XpfeS%2FDd7KZBgq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPyphn5xNDDwp7vQhCrcA3RSORwa8Xr1vuUR%2Be%2BPa5PxIhE4k6mcF6936piLYq5nm1EL6Fq6RmZBNogYlTyGalSXq4mB6uxvtDjgEFEq%2Bw%2BRGqeRPtZUzoeQE9Oecf%2FOuGuRwyXtIFCbS4r%2F7N4eQLOgKoaH6ICap0kODl4gcTfhC4TbdGkT9knJTVlm1TMDHMik%2FShZfRHEBxPYVq3dwhkP41UIMd7BH7Zic9TWKb4Ff5YDP%2BYJfJfmNiq4pGrwoAmaKPD5YlyzTU1UgACLiSTJ3288rPh6GP5F3zJNEYWPjCXDezvGb938v%2FF7A5ca8XEoeTfpRKaUnwgXsWVKTQWNd4BU8N4o%2Fs3%2B%2FYy7zgDrNcSmQaIb54ok3TwJFtV61ANuqkFbdYsWjcR9ojTzHEfy54O2I88gYl6V0YJyAHi4Q%2FTrSg6UrpRrLtXlA41eNrYQ358MW2cutcPTbQdGaeahw%2FuoBnsuq7N6cJcfVM%2FQbs3fc5aR9UP%2FgT0LlabuxFcITvAEpo6%2BejEE%2B%2Bn%2FhFZ1W5BUUFcZr3KV5zavK%2BpwPBS859rHPwDN6ef3qT0QknNzzvT%2BwUP8qiqITz3cG4UfQB2FTVf5jhANxbL5MRnHMVtf%2F%2F%2FkDiVU5VOKdmlzXUOFPW7legoW5iFLMPP7k70GOqUBFksqqwZ%2BNpn2MUEYjSPtkXjzVqW0wTZeUW71kfaOk8pcbe8KttIU6lTNeREyhBSJLKVbOUoltTC2wpkZU35cYrIhRFwLEEKZ5ko44O6njOTLizwU3rpy1ZgnchGMxOFmb9dAT1oF3wwTy7QV3uI%2BApxCvf82dZbu5YfETOuXBMAE0FacZy%2BpnO3BPAGD8L2jZEEjYddcYP6unyNlNTCtUBPb50sY&X-Amz-Signature=72f6d285ae67e5acebbfb94ad2a7994ed54cd3e8dbb54e6aa1a365c251b20e8b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XI3RRZ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB106VyWae0HIDfB2nPDwCpkG4VJpf5lcojtIB3aeuqIAiA2K3jTwRWUZU432N5%2Fh4wmlPUZKLeEQqXO2bV%2BmGLC%2BSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMSd1OgGCGmLOMSh%2FQKtwDpwPR3ZoNRAzugRTtDKpbVBt3ay1b%2Bg5DKXNexQChtA7yCaUzUBGe0oTismb9c9blZto4pOKVJwWOeTg9cJFDTAf0gQmBGC9F75S0la4YNg6cxws%2Bv%2Fad%2FbAPTiJzhsYcPb4Y0TqFM%2FGdO21QBBhslCHuL8DMt50bF1%2FLQxAqMFqf14K253LmDC%2BNdwY3rFBH5q6lHMI65u7blBnyqO5xbjAAJIgmioeD6Bj5EPCu0TDm5ntwSQ13U71xW1VJUgkZiYZ8xu0Aug08lUv7sWgcJQ6H3yrE7lu7L4%2BKjV6SAIhrUbQDEZDFntOi7r1GaVVgjR0jVWnAtV41Qtk7DTjLZRjA05xG4Hm4PW4gtbFOjwNTLKpIeMngUZLwwSQgDdWRUvnJXtoiCLb9BJWYBQPDfRMdWRrqI01ga3nRwoK0kDV4YR2wzKrjb%2FzElMql7VO7c8UPvKnzopSb1kdD1cNQ%2BpYHeWHr7KCAdu0cHy4qTRzX0Ef0cySUr97A%2FM%2FwUCuuDOnzUkk6mIUTRnaW8WtUX9C1%2FvVIg6w4aROV%2BO70HfJy9EsIZet%2FcT264ZD%2BTmlyU9T%2FlXU1VcLconoXxaByoukfX4g8xasQGYCnbKMthAnAUoDnuJlWpOf3e08wxPuTvQY6pgHUHrHwj7G4yaA0A%2BMMKkMxgkItOmFaOMVIM0yi3KoUBkTjYqM%2FdoOMaLdEftHXouTjtQqQePSCSfh0Xxq0C6utfmDaiTX9OSb7nfcfUwO1Rd3lwrszPfhMMYRyTCIcNmCEDI3EueatzyRvPtSDvf7h1W4vxlbJxmrhb56ONbJ7ItbaMEdQcB81qvJghDLgBGJgTqJLccMGu2ud0CziCBowIZfe0cwl&X-Amz-Signature=716578767fd77b88b526b01f5a82326f8f98d006788168c6d0e17c3489b14bb1&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XI3RRZ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB106VyWae0HIDfB2nPDwCpkG4VJpf5lcojtIB3aeuqIAiA2K3jTwRWUZU432N5%2Fh4wmlPUZKLeEQqXO2bV%2BmGLC%2BSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMSd1OgGCGmLOMSh%2FQKtwDpwPR3ZoNRAzugRTtDKpbVBt3ay1b%2Bg5DKXNexQChtA7yCaUzUBGe0oTismb9c9blZto4pOKVJwWOeTg9cJFDTAf0gQmBGC9F75S0la4YNg6cxws%2Bv%2Fad%2FbAPTiJzhsYcPb4Y0TqFM%2FGdO21QBBhslCHuL8DMt50bF1%2FLQxAqMFqf14K253LmDC%2BNdwY3rFBH5q6lHMI65u7blBnyqO5xbjAAJIgmioeD6Bj5EPCu0TDm5ntwSQ13U71xW1VJUgkZiYZ8xu0Aug08lUv7sWgcJQ6H3yrE7lu7L4%2BKjV6SAIhrUbQDEZDFntOi7r1GaVVgjR0jVWnAtV41Qtk7DTjLZRjA05xG4Hm4PW4gtbFOjwNTLKpIeMngUZLwwSQgDdWRUvnJXtoiCLb9BJWYBQPDfRMdWRrqI01ga3nRwoK0kDV4YR2wzKrjb%2FzElMql7VO7c8UPvKnzopSb1kdD1cNQ%2BpYHeWHr7KCAdu0cHy4qTRzX0Ef0cySUr97A%2FM%2FwUCuuDOnzUkk6mIUTRnaW8WtUX9C1%2FvVIg6w4aROV%2BO70HfJy9EsIZet%2FcT264ZD%2BTmlyU9T%2FlXU1VcLconoXxaByoukfX4g8xasQGYCnbKMthAnAUoDnuJlWpOf3e08wxPuTvQY6pgHUHrHwj7G4yaA0A%2BMMKkMxgkItOmFaOMVIM0yi3KoUBkTjYqM%2FdoOMaLdEftHXouTjtQqQePSCSfh0Xxq0C6utfmDaiTX9OSb7nfcfUwO1Rd3lwrszPfhMMYRyTCIcNmCEDI3EueatzyRvPtSDvf7h1W4vxlbJxmrhb56ONbJ7ItbaMEdQcB81qvJghDLgBGJgTqJLccMGu2ud0CziCBowIZfe0cwl&X-Amz-Signature=3f29b2a7e0cd65d2b4e3e6d6762bbfceaa87182205f368f3ecff521c206dc32a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3X6XYSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIFhkOYhvQ7Gk7R3X%2BbZp1EWXi%2FQA7aDCGNHByhsJ2oSBAiEAyx1fNa0p6cgy8yTHVwQo74VwhiNPlRQNVWNDGR5REr0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCPmv%2B%2Fyu8JMJNsB%2FCrcAww1y9jzsQknRHWJ8YYbBo%2FlS9aMH7blRbd484UvUyoE75q8Gf6TM%2BuQSv1B9Z11ZiCzjkC%2B7jRVGIUs729n2dMLSpcUaSegaiZTzBYuHmV%2BR00foC0Wfdw4Vcxe5zbEJrRAfNmqWIXDT8vm1MpdnHQX8cLcXhdiXTppFTJkYlAcFgrGYVtGOUgFEo965Wyoeogy%2FobidFl%2BTV4NddwfmOiBn42uoP4RvthQmQs2ghgvdJIHe%2FQuRNPHv4prK%2FTev2%2BDZhQttwpgTYV12zXx3T9%2FEYOereA5cahjnWyJlCp396SDcEOp1h5Qgghj42GiO3eFcDusbU2IJthhJwzbLGrEwTkHlN2f5nJiMc6wJ%2BUI75bwk%2B46QkyKrsQ7194aLsW4cJDgA5aD8Ak0%2BYRAqUmpC%2FXg0xtm%2F902bvfTKRtMap%2BWQ5MfuLAfBZh43iGIRpqWpKVYpBhgzCGEX0ywNK52w5M0mdmjsA1Uffj1Ls1TgrgL5r7I9vIxnx4zVjj2m0K%2FTU7xOXzBT7em1SrsIwSBxG%2BWH5oXlVeJg%2Fa6M9VEEqR2CtOf9b0FcBfjkA8j86z3F2H1qaw302qZkKmCT8Gkhkogrk8MQLkltDh5HKXnyPu2jsYX052b%2FthXMOX7k70GOqUBkZFzVIWZBrCE70TVOh8rjwBYafTTXDVMvFt7bsHpHHoQCMlpXgYwlawz5LATEb3cXgp2PPf0mY3bTHYp6phYqFcGotIpLTvm2ge6wGR%2Bztz4JS6CkF7qdq0NfepEqyiCdci%2BSKBR2nzDwoBrPwLabS4eFLmPfmO6M5Tytyg82HgEiHdQ7jNlAE1CuI%2FImKImtRCyAgnIIZsJLadwldNW4ewdz9xZ&X-Amz-Signature=96c39ee7a0642c7ca30d7fff88fb723fd7b2a812cc8229e3f9c5fc69829c4b16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ATT2PNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGfYCWdqn8yBp7sNHzwW8wzK72pR%2B6002yXw6x%2BWniPiAiEAkXy7SZ0ag9Laqv19c4fwrX8g0t3Egl46sm1dSL%2FOGo8q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFhOD04HpQ0ON%2BdTSSrcAyfWwPxVt8toEYOjRZM1Fo54C90dsVtBnze64xfSrzZ1LyXeGAuriBehh9c61Z%2FlgcpQAGEXxIHjSuXyImKpHPMGmd7Deij1oLXjtmx6%2FPQ6LNkUsSDdbQJzQTjEG8jI%2FtUNjULt0ODNrmlEjpKtLBILMaCd6xUxot6BqvV3HsJg%2BW61%2F56FJu%2BmjLjlFh5uneXdqT0otNccdUJujPURSg%2BurhvayfpFyzMyZyyulshB8o%2BsOG42Q7H1h5qZRBZJkUz7hpCahCLuN9P%2Fhi%2B0HmH4cHWbsrNkaVu%2Fv8tUZJbX%2FG89Eg3062Y5CyLJJD4MvmbK9TmfD7feZI7mhwayCGvF5AKLTh3coMfdE%2B81E4zRCZx8rLAw%2FLLTwaZzfm%2FwLAlD0l9CSfnhlZd8%2F2l8jJ99K2NLIGUGrgoxly8QhL9mM1c1yf2M5jSaG%2FYjY1CoqUUULIqiZf3CVWgom1PuEfNiLNKjtiEknnHtfWzgvBN%2BHE0ZCWplrqE8MvVMl167HjAvB37dcilXPpzQacd119ZoaKvS77X8HjZEE29Z%2FEXnK1E9h1iTuYE%2BlOX5FffrHlcGRcZ0U2XiX48VRVFAQEyCLmdnx43OPcKCDYXNP23DYkwCm04ZK2SgtaEiMNr7k70GOqUBbn%2Fk%2BIgUgA2LuAKPtbaW1Kx1zgEXmcF%2F5DoD6nXRM%2Fv93WCz8J6gdezrQPpjj5bL3YpTMxDa8qc%2Br%2BJdd1vC7lJOTb%2BylsTZUIY%2FRnIjHkchlBfYqNQ7du159lZmFyMFn34GMZjtVWYJ2zmIGYinetmBeH4IzZ%2Bi9EdkEVcU8NETwJO4L4Vww5IMNvOto1NCWllQYs8z68zxJtX7vPkbYQ9r7pmN&X-Amz-Signature=94e8c2959c474564f11d57de8375de72598ae0bec791d144d31807233fb38a96&X-Amz-SignedHeaders=host&x-id=GetObject)
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