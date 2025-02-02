

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=2b0c4e3d853d176a9bd79bed236e9c8e5b7851ffab758f903ecb82a50ce1000b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=67c9c350af42a0e11679ff42e9163b264d0e32fd74a4471a829f243ffb336144&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=426d8d1d1502933ebe39649f018996ed64378fb442742fd8e20c18e75181f169&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=9774ffbb680b4025417ca5262dec3241b4da924a87f93bbb0fd53791b20e50da&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=19b59971d91a9de6640f3fb86ac76eaa9a0f7214a57d924a9b32e16fd1a46f11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=c8ce79f94f6ab25022523879f34544216b3d514c0403821e8d63e0cf587d4eab&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=cde171d991a03b12566ac12f3f4cd7e6d8b71a520bdddfc3c62a76bdc35b1661&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=ef912cc5ecb9a45a38dda90bd38231f7a8a57b6a7ea49f3575222cdb6942bf95&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=04f44f094b53d354f36fb668eb4026dc0fde0e1f1e49317e5be66e663fa66bb9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637E2EOZH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERzSV2j7MFy1hNSuVSvkhnb%2FSY9AZitwk%2BuNPhqISc4AiAmMe6EfKnJ7mwtNNgDsLnmvLWdCfXWeF3dV%2BFb0fXzpCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNzWM366G97w6JPfXKtwDcFtV31pn0uAmxP3tiuLXsU6dwR3WeBlsqVGkk0bKrt5fbvRfQdpEJFGpLyyVHR1bWBV3Nek0YwsRnirt3GgbCa8Q3NG%2BS%2FGubZkHycd43%2BfPHttEq2s6xE9JIjGWNpftadMjwBnjWhQjtKqJlonjfn66MDSqX29WGyn4MmZzir2S2jYB3dSCnfS78fVKnxzD2qehnb4O0zT0f33TChy%2FAODxi1JXie%2BFlJXwImH1ksAcmm5XYoiLgOzoJJV%2FxI%2FLUquuIQpYAl%2BlraQp7dgtH%2BYB4aUanJLQ3iPRFndpXpvWse9d%2BGJGeWyHFBxetHQfJUxz1iCwI2%2B85XwGCLuAUVmpLwpbv9Mq3cCg2va81cVi3WDCWUEPHt%2BOSEwhsOhugXrdXggLDqpKiYjnbRq8R1vUmRlMy9EPtMMwzHRFqjIGEzXWioNdVxyJH7A%2FW9q3zajDOPteU0Midcn7J7KUzPuHikHA8oQ%2BnrlREe7WGww8gV2a7bn9o6Yn%2Bmnh8U2WrY2Wn3k1wc8KHkSGpAAeD9i3J81Cwm82mOqli2hvqDU1dY1raAAmWKAN9XY3vvoWXxt48slmMe2Kgek9OJEyyn3KBfTh1AyOXChmx4G%2By%2FjkyksxDrNGyg7fZ5cwyL%2F9vAY6pgE4upsIEsyE67JtIUn0dlwr9jm1JJcMd32TM%2BAfRq24H9V5VQWyC5r%2FuyMmf4Zbgz6w6tz%2FZr8wWTfgabzjyuYpQMxbJ1Bm0XG%2Bw21g7ekFmbAQOMQqzM%2F19qpFokhITDLzEMDmuu4kbQS40Ji1s%2FApp3%2FBqTETZUOXsQ26jsc%2FzD6lA7nNGUU5WVoYF%2Frz5%2F%2Bg8H%2BgtJ%2FauBvNSv8yPKd7vMevSaa4&X-Amz-Signature=67d53ec4c29a4c837013ff72b454d3c701709ff1c4f513307529c0b281ca08fc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637E2EOZH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERzSV2j7MFy1hNSuVSvkhnb%2FSY9AZitwk%2BuNPhqISc4AiAmMe6EfKnJ7mwtNNgDsLnmvLWdCfXWeF3dV%2BFb0fXzpCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNzWM366G97w6JPfXKtwDcFtV31pn0uAmxP3tiuLXsU6dwR3WeBlsqVGkk0bKrt5fbvRfQdpEJFGpLyyVHR1bWBV3Nek0YwsRnirt3GgbCa8Q3NG%2BS%2FGubZkHycd43%2BfPHttEq2s6xE9JIjGWNpftadMjwBnjWhQjtKqJlonjfn66MDSqX29WGyn4MmZzir2S2jYB3dSCnfS78fVKnxzD2qehnb4O0zT0f33TChy%2FAODxi1JXie%2BFlJXwImH1ksAcmm5XYoiLgOzoJJV%2FxI%2FLUquuIQpYAl%2BlraQp7dgtH%2BYB4aUanJLQ3iPRFndpXpvWse9d%2BGJGeWyHFBxetHQfJUxz1iCwI2%2B85XwGCLuAUVmpLwpbv9Mq3cCg2va81cVi3WDCWUEPHt%2BOSEwhsOhugXrdXggLDqpKiYjnbRq8R1vUmRlMy9EPtMMwzHRFqjIGEzXWioNdVxyJH7A%2FW9q3zajDOPteU0Midcn7J7KUzPuHikHA8oQ%2BnrlREe7WGww8gV2a7bn9o6Yn%2Bmnh8U2WrY2Wn3k1wc8KHkSGpAAeD9i3J81Cwm82mOqli2hvqDU1dY1raAAmWKAN9XY3vvoWXxt48slmMe2Kgek9OJEyyn3KBfTh1AyOXChmx4G%2By%2FjkyksxDrNGyg7fZ5cwyL%2F9vAY6pgE4upsIEsyE67JtIUn0dlwr9jm1JJcMd32TM%2BAfRq24H9V5VQWyC5r%2FuyMmf4Zbgz6w6tz%2FZr8wWTfgabzjyuYpQMxbJ1Bm0XG%2Bw21g7ekFmbAQOMQqzM%2F19qpFokhITDLzEMDmuu4kbQS40Ji1s%2FApp3%2FBqTETZUOXsQ26jsc%2FzD6lA7nNGUU5WVoYF%2Frz5%2F%2Bg8H%2BgtJ%2FauBvNSv8yPKd7vMevSaa4&X-Amz-Signature=ee202ec24f04a19034d63ee67c66d1946e11662f355ffafa87d88033b8f1c39b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637E2EOZH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERzSV2j7MFy1hNSuVSvkhnb%2FSY9AZitwk%2BuNPhqISc4AiAmMe6EfKnJ7mwtNNgDsLnmvLWdCfXWeF3dV%2BFb0fXzpCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNzWM366G97w6JPfXKtwDcFtV31pn0uAmxP3tiuLXsU6dwR3WeBlsqVGkk0bKrt5fbvRfQdpEJFGpLyyVHR1bWBV3Nek0YwsRnirt3GgbCa8Q3NG%2BS%2FGubZkHycd43%2BfPHttEq2s6xE9JIjGWNpftadMjwBnjWhQjtKqJlonjfn66MDSqX29WGyn4MmZzir2S2jYB3dSCnfS78fVKnxzD2qehnb4O0zT0f33TChy%2FAODxi1JXie%2BFlJXwImH1ksAcmm5XYoiLgOzoJJV%2FxI%2FLUquuIQpYAl%2BlraQp7dgtH%2BYB4aUanJLQ3iPRFndpXpvWse9d%2BGJGeWyHFBxetHQfJUxz1iCwI2%2B85XwGCLuAUVmpLwpbv9Mq3cCg2va81cVi3WDCWUEPHt%2BOSEwhsOhugXrdXggLDqpKiYjnbRq8R1vUmRlMy9EPtMMwzHRFqjIGEzXWioNdVxyJH7A%2FW9q3zajDOPteU0Midcn7J7KUzPuHikHA8oQ%2BnrlREe7WGww8gV2a7bn9o6Yn%2Bmnh8U2WrY2Wn3k1wc8KHkSGpAAeD9i3J81Cwm82mOqli2hvqDU1dY1raAAmWKAN9XY3vvoWXxt48slmMe2Kgek9OJEyyn3KBfTh1AyOXChmx4G%2By%2FjkyksxDrNGyg7fZ5cwyL%2F9vAY6pgE4upsIEsyE67JtIUn0dlwr9jm1JJcMd32TM%2BAfRq24H9V5VQWyC5r%2FuyMmf4Zbgz6w6tz%2FZr8wWTfgabzjyuYpQMxbJ1Bm0XG%2Bw21g7ekFmbAQOMQqzM%2F19qpFokhITDLzEMDmuu4kbQS40Ji1s%2FApp3%2FBqTETZUOXsQ26jsc%2FzD6lA7nNGUU5WVoYF%2Frz5%2F%2Bg8H%2BgtJ%2FauBvNSv8yPKd7vMevSaa4&X-Amz-Signature=2e3819cd22ea11c92d030b4cd09d591df3cf3d9d9d5748ab2e5f6b1bf102e7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=72920a269bfad61d135f2d30bdadef193055840d1b78b28ff1c0e1a5fa4f81a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=95d5840124c79bf24c215f6d9709c723950d8012cd556196bb9fc02905cd0977&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=9e1c1c7cc3411eb7ea59d301145eb77bb5266af3f1761de09989b2f8acb9095c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=59e0366e8413efead5ba6177bdf019a53938f02b0c472dc5297f488215bcc49c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=aaa9688d6963046929771ff58600c461195e93e2b26cffceb8958e3d3811a42b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UFNESY7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDw9kVqfdJTg%2FnsutG4AKXKPQjVEG8aKUhlLMeJzSNJOwIhAKV51gB%2Fq9bMMnM0CWg48a%2FMYYGwcney7F486wz3YnxvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVioW1h09vjsN%2B0E4q3AOjt%2Fm62L9bILkQkYKpGKhHvItreF30NUI%2FfXG8gpVvYyEMKcN06TdNjI8sV6dCj4IpAkJ3xP9LWozQ1ttH5YSSy9IA7deyAxhEXbXTOdGC0GhVzTJHPAG10qXGT7ixqWnsPuU4dyG8dV%2BiBrZNM%2Fezjds%2BPekRVETz7mdWbgJNV4F7AiTsxOZKf8nCPWG%2BhRf3sHqVN4L7bSvcZ12sxzf1grqHpUpEHeQ73c%2BDdj%2FH2KO3It4ArWir3MZ1w9TwW8cKUd2C%2BsWK%2Bc2eVuWAc2Z%2FnnQguCwW0rk%2FqLDtDteXHxNY%2F3DmECIYIjTmZYUTugLDw5vI%2FqHq%2FAmUVsLY5Tl2%2FSstKFxC8Ha7B6HqtM5IYbfXd%2FG7haaKDuLNS5743G0aCvPbKHGKoi8vRiEk%2BPjSCNvYLG1wstvvXpVb9iUVAyJyWPm6ruM%2BjWrIzzWsZJkh%2BI8GnezIJAhUTOUkJDRORrJ%2FGIZWHZBUwOctMvS2NxNKkGoRB%2FAXqEmAYtjkMxnxCedQE2fWIYHfH30EVfRtagcIyw6uJ9BDe%2BdYku9XGAC4Ip1aZK%2BgF8nAyOfj6OHuzkDzNlcoNHOqk50dfhlI0dwL3jn2tITRlwzdCxXMbmw%2FYaaH%2Bgtqa2vWRTCPuf28BjqkAQMIfHwzUaowGvit6lD%2BzpblMX9RVUTjxGX9dAB2sPI2gIw%2BwX4ZK82xx2XrY%2Bbs2wlW09xNg%2Bmsk6cZtUHrmqY4g17Bm%2FwikOIdOnF4YtvZcREDnn5u6B0LW%2B578cGygObmZJiNzNGIy4Glyori%2FQaM%2FbC1QQD%2Fmv9d1Rcb%2BA8IQ2YunmyK6LvVnTLkNjGEoYAjsRRyUOy7iTOFEvLZ6%2Flez4Sl&X-Amz-Signature=f174859cdb3e04264c7827513efab7b7c89e055090ddbdf5bffb43ac9a638091&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627KZNAKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEhGc095A04cLDJpbmssqnqP%2BiTF%2FOnculsAuBAwb3sXAiA3C70MKY4e%2BA9saS0zCXgn2cbH1v4CbLaGIo5Bjm92QyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlb29lkeinn7XImQHKtwDThISMQXwSIBI0CKQvbp54qju82DXEh8hluC0NFzMR3rcsG1jKrHjOip5f0pVvKzbDZEzU7PJHOxQWBmJhnmnW8spmoIXJdOS5xDbrxTUoQ0Nlta0e83gzCOhwC2QYoX%2Fyy5FOcUp3bsoaW71OAsqUPyOVSdNYZdlbeqB2NZLj4p5vENzEeYuI0osR%2BuEwsUjrQnYsRro8Q1zg4e2%2FX%2BifXNr%2FXAGn%2B3NAHuUUDvppfSCle7Wv58hMbujtczoTA%2BtcxvxeE8vXrGfhr9F1g%2FYrABQmdorYGSa%2B58AOYzyoua0wJ%2B7tzFFq6dyGJfUsAAMydRWBh8lLiCXedtGbAVHMTXPIPRGT0t5ZEm%2BQDnR5FM9IY60IQRs%2BtLRNxgcSk83eiXBtgTm7Dxcpv5JuUOP3tsfes0iSdpTYdd1X6ABtqUASB2BW8RZg%2FkD30aid1T51vHD8jxlJr4%2FBOZ03p0b4exbRELvjgsF%2FbtHdRgOeZjvvRGvR%2BKCuGlS7Ygg1iMU6OiH7puNKAlR2uIhHW2MApPuNNz8phYbJAwllJsCOYZNZQ7a0C2hzfdyab%2BTlYr6FJHhSFZf1l9ljt75P2QvXXLDpkvmeMWiO5jVQBc6l9Dg6YgowwsSq%2FlsJ3gwzsD9vAY6pgGHpJUlfKhHNx0%2BQV7MmAjmXHE4GD3iV%2FhzPwsS0ul0inSKfY9x0fXL0RiYjMtqyb10qlZyBCg005MBzhL7hEQZvICcnR0YvyjpZnLwq4C5yfZPoLexdenyEktbatv6DD8DNAspBogHnTwq%2FOfdv9kactDp0D4JrR8a7bXHayYk52aSfTQ5vXndA65o%2BjJIaT0Xw6imvUR2lOly5bHK6N5VwcqFJ0NG&X-Amz-Signature=dc80f0beecf0000a1d15d6fc9f00772557fc0e3f008a04be612d9c132c7b25e3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627KZNAKY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEhGc095A04cLDJpbmssqnqP%2BiTF%2FOnculsAuBAwb3sXAiA3C70MKY4e%2BA9saS0zCXgn2cbH1v4CbLaGIo5Bjm92QyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlb29lkeinn7XImQHKtwDThISMQXwSIBI0CKQvbp54qju82DXEh8hluC0NFzMR3rcsG1jKrHjOip5f0pVvKzbDZEzU7PJHOxQWBmJhnmnW8spmoIXJdOS5xDbrxTUoQ0Nlta0e83gzCOhwC2QYoX%2Fyy5FOcUp3bsoaW71OAsqUPyOVSdNYZdlbeqB2NZLj4p5vENzEeYuI0osR%2BuEwsUjrQnYsRro8Q1zg4e2%2FX%2BifXNr%2FXAGn%2B3NAHuUUDvppfSCle7Wv58hMbujtczoTA%2BtcxvxeE8vXrGfhr9F1g%2FYrABQmdorYGSa%2B58AOYzyoua0wJ%2B7tzFFq6dyGJfUsAAMydRWBh8lLiCXedtGbAVHMTXPIPRGT0t5ZEm%2BQDnR5FM9IY60IQRs%2BtLRNxgcSk83eiXBtgTm7Dxcpv5JuUOP3tsfes0iSdpTYdd1X6ABtqUASB2BW8RZg%2FkD30aid1T51vHD8jxlJr4%2FBOZ03p0b4exbRELvjgsF%2FbtHdRgOeZjvvRGvR%2BKCuGlS7Ygg1iMU6OiH7puNKAlR2uIhHW2MApPuNNz8phYbJAwllJsCOYZNZQ7a0C2hzfdyab%2BTlYr6FJHhSFZf1l9ljt75P2QvXXLDpkvmeMWiO5jVQBc6l9Dg6YgowwsSq%2FlsJ3gwzsD9vAY6pgGHpJUlfKhHNx0%2BQV7MmAjmXHE4GD3iV%2FhzPwsS0ul0inSKfY9x0fXL0RiYjMtqyb10qlZyBCg005MBzhL7hEQZvICcnR0YvyjpZnLwq4C5yfZPoLexdenyEktbatv6DD8DNAspBogHnTwq%2FOfdv9kactDp0D4JrR8a7bXHayYk52aSfTQ5vXndA65o%2BjJIaT0Xw6imvUR2lOly5bHK6N5VwcqFJ0NG&X-Amz-Signature=813df0211866722900f35633bdea23e9eb588844d06b68bb3226095c43825713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3PFLPC4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGq3BuW%2BfRIkUqwR9LSlaDqhMoiA%2BlIctIpomhSS0wMCAiAI2w36MZ0df0sRdVqDNGIZYZS2sotfW5SYiOgMEHvI%2FyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgv4nUbqslge57rDWKtwDmm0SbuMDz37lNyxY4q2y%2BmIRxCnqqM9nn96%2B1hC689WruNjnT6cjtKyaBJCBTWHoOCuGxVPfCN9B4vZ2%2FA%2FPxiBMf78hIFV49NSVhkt06i%2F%2Fl0KaHvHV6gZ9%2B8zHafJvUcRfjpKxzuJ5xKx0M28%2Bda1ZlvDgZWhoqU25fVv1q3RxGv9GZht6VqfYMSXnCEU4uwq3tGZLkbZ4%2FlmaChNCiChlKXi6bdfBVJGXN1KP%2BG8x1Wy2sz35%2B8C5QfVmxWHj1Q8gah4TWCClqMitm7wjHQTMXD%2B1yz5Q8fQi7v2IQm5ef5W3ZK%2F%2BKK3n1LWT2YzNJ%2Fzr6LzByBL7v3Z3skif3wiWVHX6IoiBXOjafqkvB%2BPJH9akVmgr%2FZTKzaoCW6ZiWNF8TJ%2B2QkkpL3qjWjSvZ8j4pgaQD3LNL1QDeKoiN6NOcsIGzmXpI%2FmNy92azAWoVAAIBqvF0yy8lSaJTy1TYWNMYfCxXQSk3ULySRL%2Fudai%2B86pkr2YzNxhx9a9FA%2FSrVzFfVvKBCDaMvIQtZSiWTEEXuzCJdewf21U%2FbkRHL5B59atRIUVfJvmrUgVqAh5MJlLXdC%2B0QewAUjsJZqjcNW8gtcuF5L%2FlmEkOrELduoZo0geA8Ua9TiddHkwkLn9vAY6pgF85VQEGNZ%2F3Ht1Kb3Fbz4kwhOEiyzZS%2Bkj6bcN3nE7vruj2nB6c%2Fj1gsDEkIprxdYb3ViP05cACfqBUdJZ1q6hYlLS%2Fc0CJnHnYtawnHgZnoLSLxGJJPf2vcPSVZ9neB4NeUlXYQm9nqhjehTZ29zxX2I9oszN%2FBh%2BXO8unrCNX03Dkz8gsKeLd6lOvFda3axP5sPH%2BCHqF0dQ7BWSUpTn66qF7zu%2B&X-Amz-Signature=aaefa96a7f67d0f021725e9f550aa93eecde14548ba95e840216545e8cae4efe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVLFRUQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsdu9hmPNTmxng%2FJDTwz22MRMpKwUXtmPF5EJ7WyTtewIhANhXnYIGlHyOm%2FOPgB%2FZgWkUAU0Brt0R5U2YydHXoLFqKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzU7wwWida101VXkcsq3AOUQ5kye42r%2FJz6O6qWBuJ3%2BqVCjBg639dnrfe6kkZoqwOgutpzXqfTdVZCWxm3%2BUG%2BNrpoUqD%2FoK0Fj%2Fnfyr7sCcYexRBlLqID03i3b%2FUqWDqQ69ajmwRNQ9QmBRHa3e9vyJ6z0QRM%2BGTfOyD7o1%2BGNPFK6vUzE8tctZ%2Fd0EKeWIBn20K86rk0Fldsa8ja9dXh406lvbiYP3LXcPHp%2Bkp5ANgwhSoYAUOLEzF06gYdRaLJzj9iIBVIEt1ixDT0KC9sJM9h76%2BqTwBxNLi2AuVFkYYRyOsaappWSjVgNFZxjFyTdQP0JwnV%2FTNOpUGszeL%2BuWTxIAgOnmbn6yyZq93AKBjT7KpMywQTnUA32oucafZCTmmFzUpWil7lMDaaBAMfmthDt3iPJUXLHrFqW%2BpaAZA075IRLPzx2WEaNDbP5ondZ6djWtzYz5Lj1W0iCQ%2B1qQ0X9v4jLTDQk%2F%2B%2Fta20N%2FHizLHnWGR5TdeikcNoYxhWhKBxJx1lBlQo7gXEc3%2Fo%2B%2BWI7zmS3yYIqUIpNjB4r8rruUrRr1nG6qyBwOeSrFa1OuSWSo5Ap%2BjH%2FAe3FwTiuruvs500CnGlM9r%2FMcr%2Fsqoq6s7YfClsW6B3EvBWRT5QptI2KsJS0RrNijCku%2F28BjqkAerKdMveRMCa9HNkQCGM6iX6R1hH2cu4JlKzscnHP%2Fg6wsFUxx8%2BLUJtxzcdUAzMhZ2rHKNqTPv%2Bh3xJs3zpc6i1ELBDbCGk68%2FrufM8Vtk%2BXPrXaXFCiZ7N9dZU%2FBsUZLwQxhkEzt2yGuF6AZLxrgYs2pRLU0k%2BD6VlAB36HHGWYSKprVpilegQby20zncdwxaKH8mpigMAd38OzdF%2BrQlfdR31&X-Amz-Signature=2f618ac1770973bcb779a08f73ec692930a370dbff1807afa3f1d89ff5433346&X-Amz-SignedHeaders=host&x-id=GetObject)
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