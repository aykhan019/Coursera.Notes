

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=29e8d908a64e121119b141d362f396c74c221ec30bbd77fa6d1cebe963fd606c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=dc490c2033965ecafc7b676780b5f0570ab69113afaeeb7c23e5a94d2e1959a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=de981f2a5003dba9a453e4bf077ce8dd1268521c97fadc003b64d99693e6f70b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=eb8d9a7e8293ce458efed26a9822cb6cd0616ea0528f6d30693588b4c05c2c4d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=29e766fc0fbe5e0497e4557dd551923081df9eb9d40cb529dd2dcf385b85a20a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=251b00c42dfc9ab138a2e50637282306b9749cc4143dcbd11e6719d6051e01a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=c70b4815ca92a3f47a4a67a19e8681e0c7e2afae9e14d5b9b624f8be9e186590&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=1d85e2a3b2fa41011a26cb0233500504da95ea86c087632edfdcafafd116f162&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=376f7ff9a4f82051780f33aa8bf0dc4c4b97b29b1ab14eb1b44fd1582b8c89a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MMBIVP4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiX6X1Pk1XLGhgSoA52O7m3P0MXXVtShLjUxM6%2FtiJhwIgYJIiUVlq2Cpf80HlqMhPaU00Ow0iojuVBkTFxWL1XwEqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKvuUtDq8TwNP9hWSrcA52%2BnqK1yp99bUlCGJNjP82P5AZpR0mnK7ZVfFkr3Pc31IvhOl29185SqFMUnphJU3GqxhKaU2%2BdoKMvCy0w7ZBos75BvHFPEgappqf2NGU8DvgqntDmz9fdF7yfoxY%2F8gr7YPjuGV%2F8glMzJ8Gaii9KJsAmHfri%2FEpJ6zda4fqfG92vj0MWH%2F8x4FnQeNSQT50WJLMqhhR0eQ56Eg3kFJu7Lm1ySfJN68WaBp2JN%2Br6KpGvIJ9AQjYn8PszBH7ZDMHPTjKTdHhCPnys6C3I3TSQH%2FGNr6Kg0z528rYb5k389CgWyt5s8dVljeaV%2BE2ZX8hl9ZmIL2aKzp%2ByUi%2FyGBgcKGFz7b%2Fz4rFpSk99e5eAwDVFMCGcCsusQWTrCZ2hWDeVBq7I05TvNUfAgtcSiWnSI0gbS5nyAY4wLCXkgwslQKrU4OvFkiqAs2DJi5jcBhpJ9BqiedcmOro%2FFeJo0MKbaoSwwcGfp5ATVlWcIPxqIWOjLqHaAzs0YNlG6aaDvKitY0K0DhugbWM%2FLdJhoEn8x83wtOp5vQkk26xTWZJTZgMO%2BZcSJS41aN2%2B0qSAHqwjHVJ%2BlY0yGSDFDpZIQ4UgDC1uCnybfbC3aF6dKOJk3ohtOwwwOStmiog3MIKY7rwGOqUB2T2YPFd0J8ATDdt4a%2FK8lvd3mJUQ8rDqUQchcN1v41knlz3R91jhPKkKamrK5i6jxe11lA5AIuFNcG9aua5w7MAvv5GQ3MjiNdPfYDfeS9jK7owfiYhz3usoxOxaxT7LbOE48DNFUOD8mwSzwDtyb4waldg9oJ52LzIiQDFQbsUgv5NFJcLULkujFTlVBewfsqzjV24z97bsqSl0LMfECh7%2FIsub&X-Amz-Signature=61e8e79c4c3ccfed01573632e1193fb644407c96a0a279a814f3872ddbb55e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MMBIVP4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiX6X1Pk1XLGhgSoA52O7m3P0MXXVtShLjUxM6%2FtiJhwIgYJIiUVlq2Cpf80HlqMhPaU00Ow0iojuVBkTFxWL1XwEqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKvuUtDq8TwNP9hWSrcA52%2BnqK1yp99bUlCGJNjP82P5AZpR0mnK7ZVfFkr3Pc31IvhOl29185SqFMUnphJU3GqxhKaU2%2BdoKMvCy0w7ZBos75BvHFPEgappqf2NGU8DvgqntDmz9fdF7yfoxY%2F8gr7YPjuGV%2F8glMzJ8Gaii9KJsAmHfri%2FEpJ6zda4fqfG92vj0MWH%2F8x4FnQeNSQT50WJLMqhhR0eQ56Eg3kFJu7Lm1ySfJN68WaBp2JN%2Br6KpGvIJ9AQjYn8PszBH7ZDMHPTjKTdHhCPnys6C3I3TSQH%2FGNr6Kg0z528rYb5k389CgWyt5s8dVljeaV%2BE2ZX8hl9ZmIL2aKzp%2ByUi%2FyGBgcKGFz7b%2Fz4rFpSk99e5eAwDVFMCGcCsusQWTrCZ2hWDeVBq7I05TvNUfAgtcSiWnSI0gbS5nyAY4wLCXkgwslQKrU4OvFkiqAs2DJi5jcBhpJ9BqiedcmOro%2FFeJo0MKbaoSwwcGfp5ATVlWcIPxqIWOjLqHaAzs0YNlG6aaDvKitY0K0DhugbWM%2FLdJhoEn8x83wtOp5vQkk26xTWZJTZgMO%2BZcSJS41aN2%2B0qSAHqwjHVJ%2BlY0yGSDFDpZIQ4UgDC1uCnybfbC3aF6dKOJk3ohtOwwwOStmiog3MIKY7rwGOqUB2T2YPFd0J8ATDdt4a%2FK8lvd3mJUQ8rDqUQchcN1v41knlz3R91jhPKkKamrK5i6jxe11lA5AIuFNcG9aua5w7MAvv5GQ3MjiNdPfYDfeS9jK7owfiYhz3usoxOxaxT7LbOE48DNFUOD8mwSzwDtyb4waldg9oJ52LzIiQDFQbsUgv5NFJcLULkujFTlVBewfsqzjV24z97bsqSl0LMfECh7%2FIsub&X-Amz-Signature=f9e121f8d1d7dceec1526e4f59330d47c88675af24f7beca8f9eedd18397e63a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MMBIVP4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiX6X1Pk1XLGhgSoA52O7m3P0MXXVtShLjUxM6%2FtiJhwIgYJIiUVlq2Cpf80HlqMhPaU00Ow0iojuVBkTFxWL1XwEqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKvuUtDq8TwNP9hWSrcA52%2BnqK1yp99bUlCGJNjP82P5AZpR0mnK7ZVfFkr3Pc31IvhOl29185SqFMUnphJU3GqxhKaU2%2BdoKMvCy0w7ZBos75BvHFPEgappqf2NGU8DvgqntDmz9fdF7yfoxY%2F8gr7YPjuGV%2F8glMzJ8Gaii9KJsAmHfri%2FEpJ6zda4fqfG92vj0MWH%2F8x4FnQeNSQT50WJLMqhhR0eQ56Eg3kFJu7Lm1ySfJN68WaBp2JN%2Br6KpGvIJ9AQjYn8PszBH7ZDMHPTjKTdHhCPnys6C3I3TSQH%2FGNr6Kg0z528rYb5k389CgWyt5s8dVljeaV%2BE2ZX8hl9ZmIL2aKzp%2ByUi%2FyGBgcKGFz7b%2Fz4rFpSk99e5eAwDVFMCGcCsusQWTrCZ2hWDeVBq7I05TvNUfAgtcSiWnSI0gbS5nyAY4wLCXkgwslQKrU4OvFkiqAs2DJi5jcBhpJ9BqiedcmOro%2FFeJo0MKbaoSwwcGfp5ATVlWcIPxqIWOjLqHaAzs0YNlG6aaDvKitY0K0DhugbWM%2FLdJhoEn8x83wtOp5vQkk26xTWZJTZgMO%2BZcSJS41aN2%2B0qSAHqwjHVJ%2BlY0yGSDFDpZIQ4UgDC1uCnybfbC3aF6dKOJk3ohtOwwwOStmiog3MIKY7rwGOqUB2T2YPFd0J8ATDdt4a%2FK8lvd3mJUQ8rDqUQchcN1v41knlz3R91jhPKkKamrK5i6jxe11lA5AIuFNcG9aua5w7MAvv5GQ3MjiNdPfYDfeS9jK7owfiYhz3usoxOxaxT7LbOE48DNFUOD8mwSzwDtyb4waldg9oJ52LzIiQDFQbsUgv5NFJcLULkujFTlVBewfsqzjV24z97bsqSl0LMfECh7%2FIsub&X-Amz-Signature=87e1dd70a22f1a987e8ab6d5cd609065139507319918637ef3649926ca88cfd9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=8939813a193a89b6c4b21fb9a45e394e740e7d741ad149995da17258dcd76d39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=21b4dc6615b702304a0f179ccf57e8b5e2aabaebaeb77c2f13b17b477b0c1dee&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=e34950789cb61eaa74515280e7b6537887874bca1ca417aa099ed48e7112578c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=372c3834c223a6d28f8ae7e6f5c0b9b02c438e2d9ff65585dc79df7fe0eff12a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=24355842ff1fb62cf1ddcd122e7b85219f1d4e3aa94be29aac693e455e6e0fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G2GM7VW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6IfBNEwoAaQsR7VMuDYWEmFw7Ejqb%2FzQGTLqp2OTUAwIhAOl7OWtnFq9c62nj8UoPYKlRSbvcuqcIEOcB9WmKLWzxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwg7AQFa97RmLM%2Flroq3AOqwWHra6QzzTq8GmQOkJoP6J%2F1zj0cZusUkAseSqFWQceqMoa02I89HGB3OtK%2FX03oqZclRLNXeUARtZlmq2%2BkxTMYNis2ysJUOsa8nPeqc0pC%2BtvjON2JLmwlht3v%2BCq5NhjySuZiQPpXrhwUOaTteUt4DDxmtYDPaxdOWJmjFlQ%2BHyFV%2B6rzrk1vEX5oIaHVL5IsTwA1W2A%2F4yAYxtDQwY3qTRejCqFt2BnM3JVCSjnevmyc2Bh4hzl%2F6UnFESd4zomqz3ca65G80%2FAbZYQ%2FSs4m3rf1ZBSI4%2B4ybMgmMju%2FwOebHMQSgh3lE696jsooSBwu2Ye8fDafq8bqipwu5lOLNRZSarVuCnl74dsc1Xju%2FjnxbPHARX5Q%2BTu1qWzhc%2FcRng577FnZD7ieYHcOUL%2Fix7FJubd235mKPr3Gfr20yuBbKNkubS5g71gtSWj%2FFSvidCmBjLTZnhQUe32MZvNfGvsQkVnaFD9nIibm0%2BwIbUKY%2BvIlyam4GtGWNeXY1cMjXw%2BjjfcJ746URLmoey4nkzbeFay21DOylUCX54cw%2F4k6f5%2F4pOmFPK1d3qNhXZ0IZjnIIFjHXi7457gnY6wJjIPV0nOXRw%2Fe4idXEd0GdpdrNQrQ39rw5TC1l%2B68BjqkAY2QRZMnSwMrdCvBwVH%2BclzvsIi9HjA%2BSqQP0QD0OTGMazBc8d4GDKB1YEHDSQ7%2FM%2BqGXXV5MVIXaULA1EvKdVjNkCRnbG3ruw9fSYX2RI0ulz5pUHBQa7Wi%2BKrXDkSB22P4oBpoDylB5XqvAT2cR75eSv8VPL%2FHrIxSe3TDNqlocSVitIuViQFuE2i%2FYOxc9JOk1Fw5D9cYK2KUyWYSjnc5tEKy&X-Amz-Signature=6d0991be75cf16cd7f6bb60f81ab02eda31ccba808c99a889cef58b529bdeacc&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDQ7W2Y6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4YE9Z8OSVs8l0TXd9tR54NQkLwx2R0tZn%2B%2FKMhObc%2FAIhAK8lr7GwIryL2bzfsLMvAv5ZMYCWibYOCN9kWHjanAx4KogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmHHkB%2FD2AyLjoUY4q3AOVpHeWts24NTf3Dhi%2BTxiQei%2Bm2TdZ7Q3wnAlKXIWdzYxQ4hR6xqKqJ6UB4raApHjfQq1%2BnW32UjQp4uHPfG8EXcDGJ76kNY%2F1Ilbg2r8ef1iVGKBjvy%2FP%2FWs0DILjiv1Tf6KRVm%2Fp7s19GTfdR4WmyRFHPtPL4NN8IIbjQC67PwdngzuTlD3ZZLd6VPso9SBjlydG3Shk3KH5IKndXZc9srxIj7cZX%2FQU5j0fEWZ93yGeSKExTbyTwu%2FK2nOef3414HZdx0TIIRu1g4VzQItq3QJ%2B5J2ucbkosVSDilSKTpz9kY3nYBXMMaHpS9e7GTKHqb76h%2BzO2UMtp87CN7Kvl2CC3j2ZdyG1%2F7KAbIVT0GVAVj7jD%2FDUqds9ojVoJE%2Fc%2BesIfHdR%2F227ddLwGyJRjju1uNIUR9P9uR2e9SJlle2WDyzRStjHvekTB6kXuQQ3wDCrCH5lzpxcvtiPJEaZpDbsRfaPfYr4M54HclACLQ%2FH0FwydvM8ILJqoCk2aCrHIZwwlQQcHnYkklje%2B355RvF7n4zxRwCmhP%2FSxZQk3xab3qjB65FLy59Ah%2By02l6snVfN7mBts1teA%2F%2FET3rUPezfDNsTXKbuLURqXgGugCtdIXaEGgvVC150FDCAl%2B68BjqkAQgpFxGn%2BS%2FlwtdbgL4sOdWe2vU4ljO6DORi6TOr3Ta9gCGDc1ifXz5%2FNWFL99YJ8Ulz0%2BdreysSZj%2FMgAf7vlH5CNRxG9l7jZ%2BhRF68WAlygUUrjNJkjn5zx8ri7%2FMz0DQGxyHHSBCCYdmy10mPE15QAmSyOHga9HVcbT1nqXeWwWYT4j9euWpbC6dUTGQGkhxVPhlsCa%2FVPiuAFW0OnsbF1ceC&X-Amz-Signature=c3ecde4540c6170961a92ae321fa6cff2647e8334ff9aa6dc75210f72707cecb&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDQ7W2Y6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4YE9Z8OSVs8l0TXd9tR54NQkLwx2R0tZn%2B%2FKMhObc%2FAIhAK8lr7GwIryL2bzfsLMvAv5ZMYCWibYOCN9kWHjanAx4KogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmHHkB%2FD2AyLjoUY4q3AOVpHeWts24NTf3Dhi%2BTxiQei%2Bm2TdZ7Q3wnAlKXIWdzYxQ4hR6xqKqJ6UB4raApHjfQq1%2BnW32UjQp4uHPfG8EXcDGJ76kNY%2F1Ilbg2r8ef1iVGKBjvy%2FP%2FWs0DILjiv1Tf6KRVm%2Fp7s19GTfdR4WmyRFHPtPL4NN8IIbjQC67PwdngzuTlD3ZZLd6VPso9SBjlydG3Shk3KH5IKndXZc9srxIj7cZX%2FQU5j0fEWZ93yGeSKExTbyTwu%2FK2nOef3414HZdx0TIIRu1g4VzQItq3QJ%2B5J2ucbkosVSDilSKTpz9kY3nYBXMMaHpS9e7GTKHqb76h%2BzO2UMtp87CN7Kvl2CC3j2ZdyG1%2F7KAbIVT0GVAVj7jD%2FDUqds9ojVoJE%2Fc%2BesIfHdR%2F227ddLwGyJRjju1uNIUR9P9uR2e9SJlle2WDyzRStjHvekTB6kXuQQ3wDCrCH5lzpxcvtiPJEaZpDbsRfaPfYr4M54HclACLQ%2FH0FwydvM8ILJqoCk2aCrHIZwwlQQcHnYkklje%2B355RvF7n4zxRwCmhP%2FSxZQk3xab3qjB65FLy59Ah%2By02l6snVfN7mBts1teA%2F%2FET3rUPezfDNsTXKbuLURqXgGugCtdIXaEGgvVC150FDCAl%2B68BjqkAQgpFxGn%2BS%2FlwtdbgL4sOdWe2vU4ljO6DORi6TOr3Ta9gCGDc1ifXz5%2FNWFL99YJ8Ulz0%2BdreysSZj%2FMgAf7vlH5CNRxG9l7jZ%2BhRF68WAlygUUrjNJkjn5zx8ri7%2FMz0DQGxyHHSBCCYdmy10mPE15QAmSyOHga9HVcbT1nqXeWwWYT4j9euWpbC6dUTGQGkhxVPhlsCa%2FVPiuAFW0OnsbF1ceC&X-Amz-Signature=0d380a73236f1632cabecd0de3033d6d968639023b480dc1426d66f8ecffd567&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNT2PHKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8HTmutIwixQCX8GaxRS%2F1mloQDRkS9qoCEcl653JqKgIhAN8TN7q7bLyWOoRjofccNY%2BFwSehiE%2BHlHGWivkc9jp4KogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlR0wsZ9r5ZMilBlYq3AP65pejFFrDPblXck7oky%2FbT9OM6uZUEHDo2OcGIc3S68TPolVisNKnSENmxx9MfPJj7HMZHgDmOZkJQAcvnMz%2Bg%2FVcl76sKbp5K1ZELeoIY51%2BrWYPIsBeeC06a80HqEk7e6Oz9Rs8Sd4MOTbe4O75K67TK0nVYyPjkxj0uJ77k%2BplD0%2FppWajgqJYUbz5EBQHz3jk1qmq7PGMz5F6WP4%2F3kiOWVQJB6EaSv%2Fx4TnmsByKkLo724P0n%2FyDB%2BBSVEzo3tKQMc%2BmUKcMfqZcJvGaDhgYCZHJD3vylyCge%2BDdCVENoQbF%2BV5Ne91SkrBYJ8Eo1oYS9JX2kKfvkJFxiWMN5TQj7nQXkEE30KTonIOHzH3s0X2ItyXcxgCry8WAVIli8ICBfDgMFmTy895RGyV%2B0ooBXrC7TFzBVlxXD2cXsktuiyQV86nDq2WTtAILSrmRvzW%2FCvz392GRtAH99LOUhi22tXtI7tOvk%2BkJqXpq5X06PbqO%2FpDhtN2VLRvvie15TGA0H12WDTP6c61JvHvsvaJNEq%2B%2BcO%2BHNfaQjBQJRZKWzfoNoPIe6ANs3KJeogRYkSPcM%2BzX%2BJCOEqjSj6EaSfvhqMpm%2Fq5VIzBDiZZyL%2BujYIiB6yP8lixIljCGmO68BjqkAck1xT8Qi2C6Zc3subFXGMGidftuGnQk3NWJRQgnzwl4%2FE717BkqI5%2BAdLrFHyWqqcRuVa4oaY6Q7s7TdpnqLHsYY52Bhg%2Fv3M%2FZgFLq9mwVFTkUcrTuCAUmbJbtttVBG8pvw5ZUhYTgQCuoU78HzTYSOHVzc0gGaf%2B31tQWKUZCvFX6N2NNOTxmf4%2F0NMJvP%2BWQzPWkNfQ3uDhKbTqQkUPAp3Uy&X-Amz-Signature=e87978917c11ac3e675195e86a928f74b2d787a34de2e428ed3bae2bde2da512&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLECMJ7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu9JRxTmq9wKhsB5E8QEtW%2Ft1J5%2BriPMkjnWr3XXlu%2BgIhAP29k%2B12S7Job2H1FUiDzyFApPzWcxTJf%2F0YpHrHpGoxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycLzm94rX3mifeVfcq3AP58OZUYwEu4d9%2BSnFYD6l5%2BEo1cWEnWjBNZSdWb%2BBVFeikwu0bjaV2d7eP%2F9dMdZScVXJHEzCLK8LSrnjHHsJHq2nTGWlokPx6W1%2F39wD81UXHUqss74R0cxmDpqAVVCUBAMHf%2BhYalaUklms6ac1Qi3hT2CCdnU%2F6mxk7usf6DGwAl37YFGkpZlCU08TCSx9C6sSjZf1%2FVe2OcWuehO63%2BVqFaWtz%2BEpmih%2F04dO6%2B1TjFuCA%2BboGNws8xSMMylcqbwt%2Fz%2FCSUAHHVu4qri4MJN6TRkCWR4TwQHU3Wu9BwZNYstQUaR%2FFzVjU%2BFz4B4eEWY7o7Mr%2B1Dcx2jfCYT5vo8AMwpu6PTKf4tU%2F%2FJPSDNsoysErwHaZhvsQY3g7cv4CrqeFb8oC%2FG0H8i6rqrHgSBQlG2ny2qf3uFqylvNH%2BYkVEU64f2UeNzMhsjOsGRO4rvA8NR%2Ft5AQ%2Bq4wXZiWXT0LbBLBNaSfzjHaAlo1AcsVC1%2BeorGHUVbAq5RTRcz%2FyorQFSwSF5z15v74r6dU3uKe%2BGWqn7AsWKX4DHDdZ5wEGUzL7Vd9DaRG1VRzPivedjUpWcLW%2BMjQZq6EqJRAg3kC6vW6BX8Z5Le882bR1R8%2F6tUhV8OY4Q5moWzCEmO68BjqkAf78eeqko7hhQfoIYeH4RaAfTsTgisQP50ocBBBo87%2B9IUN1HRf7L3vZ4s9uHkP%2BfhE0Y4lmW0janTjKFOW1ffuGTjETL4dXztLbzhqbsFJXt%2BzoLLNyAYdjIIAz3s4yO5rBZBDjUn9aLDtXlxGdTfUoflb13J%2FQ7HYGvGqmvsBij9%2BtTVje2Of0WYlBHcDjITd7nJi9MzZ5tJEA9%2BhgL0rLsZ5j&X-Amz-Signature=83c215a0c533fc2a093792f10cb7a7f239a7d450ff3e6e9ef4ff554fb9afbaba&X-Amz-SignedHeaders=host&x-id=GetObject)
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