

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=d6772c175c4423f4d5d32a9a503063ee5e089f8fb7d28a451f96190572cff841&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=0b507f50a5ce893ee1cdadf6c50648dc79a96410c970d53411eb1ddd13edfb4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=c2b9bf8f0f94446f0724989c21469ceabe503d657be17138b40b8c12a5caaa03&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=919d1b78b4ff7cce31a2c779e0017f865f524760261982e9507601898aaf852e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=f0bba17cc2ec21030d1a908683f8ade8d32f69ed2eadddcbe5ae3a1ee9d1b4a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=bb94922b9cc72e75b0e1852e8c2ead4163c56485a3ab6a9dfe569680e63a1dd4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=d394333d25bd17be1e56d4d864185b4b7bb9594dcc36683b42ba5425cb7b1975&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=eed875e7ae3b0e667f7ee93fc08a4b231adbcab65e2246bd4e74549da43285a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=1e0f30535f60b80acc1253c139769f3022715dce2b36df39435e4f1dc4ad70ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466475NXOVV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCj1M%2B%2F6FoFAcT%2FLdPU1aSi4qWJg0s5saB1o%2BGKD2qrkAIgE4QFYeQrUXmNb8qr6w1NCHkgKX1dxCweQW6KyKbeHDYq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDFeTR5Pl1RbCcoJMcSrcA9%2BBxuSOKEXA%2F6NnhCYWD61SQb2ijATrhqSTYaFkbF09uMWowo16t7a%2BbDxfyv2eO50eiPJDtBsLlmq5PDNmjkf%2BALihIB2iDW%2BBG1Y8SAXHRbYdBWrE9%2FVXlGrqVcUdnEGxPCr%2F4ghdTggjpsjDfyGmPlgPjq%2B5E4X3iJDPtR48PqWPLQ0s6Z26d0SEzj0wXDWCvRecucIfH9WItpJaZKMlOX%2F96yazKC1dN5PlPVB5HmzlOgJVn7iKUfKy5QYj4MMSIipKNz018c0wei3LCLqdpaREWCzs2nq9Ba2FQIx6sPz7eXBs9PYMkCKaegXKaTV1lJUddO5KdHWIChT0ngi3kw5HXQwAIKwD%2BH8P2WrqRFb6JzuM5V1Pz0Kqpu0e7xTiIZ1hH0LLFdc6KrELhih7Ijje%2FHY7kqisfV0NfztRwCao4%2BRBoAEJNSsNyIOEgwQAf7kNTj7k7iaZHTl9TQp8ZkBG3FK6h8%2FRXaLuawAQFiHrsoJedrlmVmBSDfzrE1DE0v%2F28u1oA3LaK4NGb6cVV1vutG35Uu9lfDNqti%2FPH5MGLVrWQJAmzw%2BqeRz5SHxBrN3Q6RlybOy%2FsH%2FPFxTVU%2BdP4FpwPrS9O39uUo5BR1XRvn8D4GmxPC%2FXMLDjjb0GOqUBt8uA2fJHEx0pc%2F%2FndSGebytey8eE5Xvr7L3Hz6O%2BmsU0MseVkoIiUs491ntuGgVSZYHVOzsjJ1DdHvylmXauJanSO1IzhjP9%2Fk6WS401qXdEGhrdyc97UWt6EZceCO%2BBOOjWhe4oZEcW9KYKwTeGDEKPYkWzW2aMN7uAnN2hzd%2B7hnc3GlooFcjvH%2Bt3VD9VPsfWMBRAYHYqGiOpLosSXmQdyKXb&X-Amz-Signature=be2a0b00a9479cad9a45573c52e1b47f8bd3e49b75ea6e40a2161a333cf35efc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466475NXOVV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCj1M%2B%2F6FoFAcT%2FLdPU1aSi4qWJg0s5saB1o%2BGKD2qrkAIgE4QFYeQrUXmNb8qr6w1NCHkgKX1dxCweQW6KyKbeHDYq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDFeTR5Pl1RbCcoJMcSrcA9%2BBxuSOKEXA%2F6NnhCYWD61SQb2ijATrhqSTYaFkbF09uMWowo16t7a%2BbDxfyv2eO50eiPJDtBsLlmq5PDNmjkf%2BALihIB2iDW%2BBG1Y8SAXHRbYdBWrE9%2FVXlGrqVcUdnEGxPCr%2F4ghdTggjpsjDfyGmPlgPjq%2B5E4X3iJDPtR48PqWPLQ0s6Z26d0SEzj0wXDWCvRecucIfH9WItpJaZKMlOX%2F96yazKC1dN5PlPVB5HmzlOgJVn7iKUfKy5QYj4MMSIipKNz018c0wei3LCLqdpaREWCzs2nq9Ba2FQIx6sPz7eXBs9PYMkCKaegXKaTV1lJUddO5KdHWIChT0ngi3kw5HXQwAIKwD%2BH8P2WrqRFb6JzuM5V1Pz0Kqpu0e7xTiIZ1hH0LLFdc6KrELhih7Ijje%2FHY7kqisfV0NfztRwCao4%2BRBoAEJNSsNyIOEgwQAf7kNTj7k7iaZHTl9TQp8ZkBG3FK6h8%2FRXaLuawAQFiHrsoJedrlmVmBSDfzrE1DE0v%2F28u1oA3LaK4NGb6cVV1vutG35Uu9lfDNqti%2FPH5MGLVrWQJAmzw%2BqeRz5SHxBrN3Q6RlybOy%2FsH%2FPFxTVU%2BdP4FpwPrS9O39uUo5BR1XRvn8D4GmxPC%2FXMLDjjb0GOqUBt8uA2fJHEx0pc%2F%2FndSGebytey8eE5Xvr7L3Hz6O%2BmsU0MseVkoIiUs491ntuGgVSZYHVOzsjJ1DdHvylmXauJanSO1IzhjP9%2Fk6WS401qXdEGhrdyc97UWt6EZceCO%2BBOOjWhe4oZEcW9KYKwTeGDEKPYkWzW2aMN7uAnN2hzd%2B7hnc3GlooFcjvH%2Bt3VD9VPsfWMBRAYHYqGiOpLosSXmQdyKXb&X-Amz-Signature=c9d011a5f85425fd894ed2781d09421305b264b8f07e832129358d18ac399fb2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466475NXOVV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCj1M%2B%2F6FoFAcT%2FLdPU1aSi4qWJg0s5saB1o%2BGKD2qrkAIgE4QFYeQrUXmNb8qr6w1NCHkgKX1dxCweQW6KyKbeHDYq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDFeTR5Pl1RbCcoJMcSrcA9%2BBxuSOKEXA%2F6NnhCYWD61SQb2ijATrhqSTYaFkbF09uMWowo16t7a%2BbDxfyv2eO50eiPJDtBsLlmq5PDNmjkf%2BALihIB2iDW%2BBG1Y8SAXHRbYdBWrE9%2FVXlGrqVcUdnEGxPCr%2F4ghdTggjpsjDfyGmPlgPjq%2B5E4X3iJDPtR48PqWPLQ0s6Z26d0SEzj0wXDWCvRecucIfH9WItpJaZKMlOX%2F96yazKC1dN5PlPVB5HmzlOgJVn7iKUfKy5QYj4MMSIipKNz018c0wei3LCLqdpaREWCzs2nq9Ba2FQIx6sPz7eXBs9PYMkCKaegXKaTV1lJUddO5KdHWIChT0ngi3kw5HXQwAIKwD%2BH8P2WrqRFb6JzuM5V1Pz0Kqpu0e7xTiIZ1hH0LLFdc6KrELhih7Ijje%2FHY7kqisfV0NfztRwCao4%2BRBoAEJNSsNyIOEgwQAf7kNTj7k7iaZHTl9TQp8ZkBG3FK6h8%2FRXaLuawAQFiHrsoJedrlmVmBSDfzrE1DE0v%2F28u1oA3LaK4NGb6cVV1vutG35Uu9lfDNqti%2FPH5MGLVrWQJAmzw%2BqeRz5SHxBrN3Q6RlybOy%2FsH%2FPFxTVU%2BdP4FpwPrS9O39uUo5BR1XRvn8D4GmxPC%2FXMLDjjb0GOqUBt8uA2fJHEx0pc%2F%2FndSGebytey8eE5Xvr7L3Hz6O%2BmsU0MseVkoIiUs491ntuGgVSZYHVOzsjJ1DdHvylmXauJanSO1IzhjP9%2Fk6WS401qXdEGhrdyc97UWt6EZceCO%2BBOOjWhe4oZEcW9KYKwTeGDEKPYkWzW2aMN7uAnN2hzd%2B7hnc3GlooFcjvH%2Bt3VD9VPsfWMBRAYHYqGiOpLosSXmQdyKXb&X-Amz-Signature=cea668cca6c8103a79c20e5a6b20831266a1f6398b0427f01be5d8d8291e195f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=e0f5ca90c8eed882f25f70b747042d6ab8a9585c058a8deb887d5aeecdbf993c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=a58c32bf0a0f33ae3b825d68cab4ee5d6807ebd8f44cb5a0e19761079244bd48&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=3e573cf79acd2cfbedbfcbc833814690fedf188f9ccfa56a5923872ff6f14f02&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=59ae07dd60b6e781225ee8a2fe082a35fccdf4165f256656109e2ae88ae1c716&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=9aa8a8a7f5b50f863ce54ab3832a69c93ee1f6c5013c943b5f666981e84ddc6d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675BNBNKI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQDB066siY14iwFfpqRrbUQySW5DGLjpBJUFnc90hlU6LQIgIeOmTWtrkG4vTNvy%2BKyzKOuaUFmJR%2BgoRz8k5ooi6hIq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDM5alY6bmMgnkkh%2BWCrcAygblSO6JrKuSd%2B93zrU5z10Nj57byr67%2B%2FRSbwoofwJPeyWWxtD%2FvCykaLXd3clA%2BVLLiJGZeDKii47TGusi6LY9eoXf7%2FwpIgK%2B34Tyivz7rcQxaEPwJYHL636n2rHtXDZsG48jYSlqN%2FCZ00r8LAIohSgU4KEg9DwX%2BKBgTIgXHLhBjJqiocP2iM8hyq2J2mUL324eybnffKYgsjuX3FaGs9R0AjuI2n7Gqg771U5Fa%2FbHoMN0SNzQj6C85wBxQzMIsA2e1QsWbDrz6IpM1ZJLWjHJyn4gm4LtG%2FBEENRWBuVnmXaaMXEZna6V9efHd24Fg%2F5IoplgS%2Fsbu1l721VhHAiLgKhebx%2FK%2BHiHnIbYtAafvHgBqnoIhHGkbJxuKszhULGDQV9q1hDXDffbpUuJsByLGnP4tx1W4FseLmG7HLnAIPE85PnBm26KfaXA6HcC2LoaJW7rFt0zQh40ErEg%2Fy4Mw6uRkHdIvE%2F1m9Kw61wJfE8dUqsL%2BOMyUg59pMfckynnPRu4t3dMojxWH7Skhv5B0tgnZ5GlWZ9dkgxjManPfFW2i9MGYhRZBCpG6tepe2gj9ZmWuYpMsZBx7KM3VRIxuO%2BnufR0Fw09EUyvShoSmiF2Sh%2FaeHoMJ3kjb0GOqUBhmWvYR92o7XK7RTYmcN2sfoT%2BnGRzUpEkCu0vHEWnXsB1ABH3GAcacL17xrsG4ouXPZfxrf4NcqKmBSHfj%2B48%2FSPX9KhkpioWf6LgARR2QhBLq%2FKC3EMJgNqpTCkjGTj5iVDdbRGFZ6hK8POglVCMljKbYsKl5biNQ8jaPV3jujUSBaScIBvkgg3TFLwjRRgnsQmXB1kZHydTEm6%2FVO7wUWvuMYZ&X-Amz-Signature=4191bfaaa8c8ebbcbc65bdeb522110760d9a888f9939e5a3004781e812ac282e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEX6QG3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDS9JlD41pQpd0ApaKpdt5osodeiYqJXnI2ESQvvPUJTQIhAIoXqKYrS34b2XWasfshoJB6XmwzYmarCHGqf9%2FuFcRWKv8DCEcQABoMNjM3NDIzMTgzODA1IgxxUxQX4cFq2VdACkkq3AO3zlzJPDa1BwQyJNFzeFMj39P%2B%2BzLWbR%2F1eddKE284P%2FeIJsxJrjZIl%2FTP8N5WNgcyorIYw%2FnH0TaeLDHkkfmuOSWh7jmWkk2pYJ9hWtAMlXp0wRwechdsXtZgvlt02BRHpT68guZMOPaXPpslhzzKcwgRLz1Mb%2FCQC6NChwfRarqO7sxJWqJHfAl2GrcaruAx8PcspcSvHzqF10mUocPsnsxX7YFpjW27xyJRhhnZ3FX9fOmZ8%2F7qH92DBwYXrRyfqtcsGZu17ab%2Bn5q9hHOcWhdnn6kNfgsFU6i%2FzW5SBbn8eS0JMRdAZ5PAXjM0KROVx0jOc7Ueyf7E1PAuWB2MnaU5zPh5GGYlRgt53KF9DHZ1c3E%2B6pZTyzKaZtgAGgNinn9SL3hrQtqQpU1q0YKb4DxrAT2sinIDzTiTud9GyKKfUibn8L34UKBM9gANCPVoHmTBGXB9x0VFNe2%2FE1Br2nne9aSox0OOD%2BE%2Fw6yyzxP4fjDzgunPZyA4fJ6UN51DeogOpIntLD7AGC%2BlGyPzLjm18%2FajFyqnTWh3ytpMeLplW9ngN4g3iPg7ins%2BvUL%2Fz%2BgwMt2dORMw3dYbtQNS%2B%2FEHyPbnCYIOsqNP18%2Ba9DeFgcYvU8jMXTkJTTCt5I29BjqkAUyjtkpsDjsiIc5FZrK6x1dsqcqyzeSdOx3s1ENBtY8OJxaxLI8n9Qy2gU5lZcO5sLiB7lZ6Vz%2FK0wCZVSg8i33YgovOeejyPqWeckzH%2Bjlpdvz54oVOXHCl%2F2%2BSjU3o5uPxFg1R1fYIFsNSVVtmj6Se%2BChNqYLKy%2B%2BvAfNhNIWbeAIdvBlwvbLDqGOomnfjrY6q9znvGpZ22mE8VZLvFiRgpyqZ&X-Amz-Signature=46c083a09429a25eb558e901a27dad6b0850e2f1231d2652be20c1b8ed8145d0&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEX6QG3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDS9JlD41pQpd0ApaKpdt5osodeiYqJXnI2ESQvvPUJTQIhAIoXqKYrS34b2XWasfshoJB6XmwzYmarCHGqf9%2FuFcRWKv8DCEcQABoMNjM3NDIzMTgzODA1IgxxUxQX4cFq2VdACkkq3AO3zlzJPDa1BwQyJNFzeFMj39P%2B%2BzLWbR%2F1eddKE284P%2FeIJsxJrjZIl%2FTP8N5WNgcyorIYw%2FnH0TaeLDHkkfmuOSWh7jmWkk2pYJ9hWtAMlXp0wRwechdsXtZgvlt02BRHpT68guZMOPaXPpslhzzKcwgRLz1Mb%2FCQC6NChwfRarqO7sxJWqJHfAl2GrcaruAx8PcspcSvHzqF10mUocPsnsxX7YFpjW27xyJRhhnZ3FX9fOmZ8%2F7qH92DBwYXrRyfqtcsGZu17ab%2Bn5q9hHOcWhdnn6kNfgsFU6i%2FzW5SBbn8eS0JMRdAZ5PAXjM0KROVx0jOc7Ueyf7E1PAuWB2MnaU5zPh5GGYlRgt53KF9DHZ1c3E%2B6pZTyzKaZtgAGgNinn9SL3hrQtqQpU1q0YKb4DxrAT2sinIDzTiTud9GyKKfUibn8L34UKBM9gANCPVoHmTBGXB9x0VFNe2%2FE1Br2nne9aSox0OOD%2BE%2Fw6yyzxP4fjDzgunPZyA4fJ6UN51DeogOpIntLD7AGC%2BlGyPzLjm18%2FajFyqnTWh3ytpMeLplW9ngN4g3iPg7ins%2BvUL%2Fz%2BgwMt2dORMw3dYbtQNS%2B%2FEHyPbnCYIOsqNP18%2Ba9DeFgcYvU8jMXTkJTTCt5I29BjqkAUyjtkpsDjsiIc5FZrK6x1dsqcqyzeSdOx3s1ENBtY8OJxaxLI8n9Qy2gU5lZcO5sLiB7lZ6Vz%2FK0wCZVSg8i33YgovOeejyPqWeckzH%2Bjlpdvz54oVOXHCl%2F2%2BSjU3o5uPxFg1R1fYIFsNSVVtmj6Se%2BChNqYLKy%2B%2BvAfNhNIWbeAIdvBlwvbLDqGOomnfjrY6q9znvGpZ22mE8VZLvFiRgpyqZ&X-Amz-Signature=bd03984bccd19d6f0e2e49966ba069671c1252c215afd97633c0786b5dc639d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOKVXYUT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDDe8dEbvXiNPL8Aya0pi%2F%2BcXcBrEGxWtwoCco2odfUIwIhAKTPIM5QdkSS8VwrwwhxNIkWavGNSzP9lb%2BAUWnWoJ%2BXKv8DCEcQABoMNjM3NDIzMTgzODA1IgzPgHrZ10BneFxDfn4q3AOXTAlSvXekWnle46wU64eKI2s%2B809wB6GO0K5rfskYEHoJ4DilpkXMBgQBPYsC0x4SB9lwSrCflNsC%2BeS2%2F2RQqlTepL4vZLDnV9YwWdj8DFo4HGLhXjkrvY2Lydv88N5U7s%2FLr%2FBRwmcHmmBnNPYeNJjBkzpPqiBK7Z7a1j4JHK7x4zN226s2Rfxtt%2BVP%2B3zR7hA08hwjOIwMxCWLXphoF4jQnEcKZyZs5CesasfdOHrwHC5wS6rkXGfonU49YqXbaP66AMuP9zsC2mtugG8bv3gNHHBKaRw8bVsUgJhcOrVDF3p0nJEkfOJ2UDuqlD3%2BW7bg%2Bc8Y2J1kxdX4sqV0x01UmsQ9eH2kBnZ3%2F%2FJEXrXhl8h47%2BtY9gjWUDG7rl4I%2B5ipo9sBvi5DXMsR%2BsOGEEvAHi9qfbpJrImUHhLSH7pr5QtJPyOb8eEVzwqe6NzSjxJb8m7fwQ37b7kUKusBMMVmm0X7Rf6GgwKfgHmb%2Bpx%2BrjkEW255pw3DHTye%2Bq%2FGhc0k%2B%2F2v%2FoZacZAdLb2aOTqk0hN%2BrQgDYbHK8uextGaxnrOpCdOGOwcv%2FcyvQmDPQTgm8BYiUAXpO70JRTzDytVeOaH6F4HoOjkSERkAapINPIzdbA7chfzmNTDu4429BjqkAUU2bNUVHMyMWR%2FMvUgNyoFkeVr4bueVVmvRJYu3GQgKTRdqcPd0dbWERsJYXpFuO7C1JWNHXQ%2Fm1tq6fLAahfMxh2HapEWaZ8vfDzseSDuTRrGtpKD9BY1aWVKidbh3Nq36WxxPyeoNwOnbL5I4nqItIb6Ne1YfZ7hXMA8sPJ5hhjkTOphYRgaarraga%2FHv5DYTJWiQ116QcvXN57Wxh93KKEKo&X-Amz-Signature=61a72b460afb3a68cd61d0b23c2edbbe69713eeeb7732edde68ce96ced77ed2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GWXZPV5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIDtOZEZ1cUxms1ciWXHSuJuJq0DXG%2FNQxRSnfT5E0CePAiByyuPQ3PhFlWzBtUCb6tMZb5x9%2BYhyHoXZEZrymuvCVyr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMHmNRzZI6l3GLLZPbKtwDVZeHo%2BTMGdwVGGHzy9waeHk6hJZpdLKaZU6LhMZ7aXB0yu1WUVj3533RmlcA6hvNnZZDMulELas8mjDF1HfFDhYg2HrEKsgNgkn0ytwv%2FQlOPOlgDD0XQJbjNEpxedx9CE035gzTU9jaZdYEvbQZ4VgOdV6sy1mTzxbU%2Fy4i3d03clEYdeloTNbZvgi%2BbpZfi9QVl65yXR3vIV2%2FRcXxf68XOe%2FR91ZbB%2FqbAaCu7s5ZbfaMh3K9x9XtVDlbvSMp98cpNkUc0%2F1rvyNoC6oqVSGKVVnZD%2BcHpYP%2B%2F4deQu1ckETFZI%2BoMhs%2FN78pTJ5MGFQW1VwCbWg7WKct5QBkR0J877GXV99vceazZk%2FCv38PnBrFhHltWYYpnL1yHAeph3w6nUKLJt4eVOB1nRZZ7zjp1IZGRh91GPkaK8jqxXaI4PbP9SmYL95sxrO0ZpnPZT69VoUbl4a1%2Bm4QXjtqeaoYbbxMTer08gemt5uLNzqy3Fey72%2F%2FSFZpW05ZI5MhOQGaf5Y3QrY8QDbdoXgy8PMjYcOZvwKfXNRVz24T4AQBLBFdBkUlQb2G72DG7CE32%2Fzd32z9Nwuse915WX96eJG34iSG1G3%2BFrnVzuzAoGwl0ZLgQoHwO8dOGSEwwICOvQY6pgGTslXYwaC9PV6ngRU%2BaD4biZQFefbPJ%2FNlc4ES9KTbUjaK%2BwPPMCPsjFUIYkbG%2BAKGjo5ZoxuWbDhyVBAfA5mEQPKUjj0YMcjYeUXWG677DEgjnMXhfXdoAxcsRHLLoXrzft%2FOR3oWAczqNhJyWuSnLTsAJDnbkFyMj3nRt2nv30cGeVrqmwu331KVbH21uKq6H0N1pe%2BoqCsPjzS3GV8jlV1fM56Q&X-Amz-Signature=2fe8dd88e54fd7332dc30acf48e01fd38bd500f7f3c015c8fa0edb6cc6e6ddbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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