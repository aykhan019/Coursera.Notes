

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=c950a0fe530acc0ab0132864561e0c212baf4e1b2c3dabb9923d16a7383ee3b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=ca7ff4f8ac04ea74ac4f6816d5739f8f6d7f368a0159aae5497305540385a7af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=a9b9df48cf369d0b9021cb9f13cc85cf3487578f0595215a95ce9e57304a4a66&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=adb88845c7499a339f771f12922fe7c3592c9aed6081b63669567d595bbcf831&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=20afbdd2240b4e3a09bf6a945cb10ac457ade6125b0bdcb72be0007aab893ed0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=2a5ef3b9cb44de27673ffd69d33a8ff2f8862a0c9f7b25accf4833ec0b474119&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=e1e219a964ce60dbf09592247ce75e4c070bdde440db86f3a818b41d6f69ecfb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=656fd7720e8c17e6b2213b1824693a6bf6ba5a151ea0faa906431d536ae36b3c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=abe8e3668110537779dc2ca2d42bf3f3470d59c45bf81dc844387f71a79f5fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQXLFF2E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQCskMl%2BYC%2BDYsL6rC33LRBl7QeAVm7c%2BRf4r4oPwjliqwIgOsbhWneH4mS6tSSoHYiSbuDmDAjX3zSVAuo5%2FkVcMTMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDExZQ7QUIliTsPR7byrcA8h3V68F86qfzxD7jfmM%2BNvph3AP6JkOdCd51vTiPFEttAUbCLOS3jHwZrm5mTkVZhERDQSrIHgpzyRUvt%2BaR8jadJ6kWeX2sN94MTzJxV%2FP%2BKDYlqI4TF2u5SfRa7DUXumea2UmCsVT1Xv1kk006RTWCKBOhhzcA8uYSCuPfwMY9YrOUX%2B%2Fn6bAs%2FdmEIDE76jTpcFFlz%2B2Hn1JBPK88lhclUqahPHBWgXnBCfjmTS9c%2BvwDoeAtGGlz7OOqFYgwxpoXIrn1lKhNuywUCrpzhtesG5vGXpqo8iiJbfguyoKKYzkGpEpgefSChBP1s3h0ghB3j5FYEitQYBXi%2F5%2F6X215JONHSwtZ8LhmChLoqhP83TENw8wClfO%2FMsyDA80o%2B1B4RKHwGENZf1AMag6OYr3vELxlSDjocV%2B53Nw9GswNCq2Nq%2FOQzG%2Few86ouM7%2BPY%2FKaNLq95MTeuTcXPkSMFahE3RibufssqNgrogVGykCupp9Y4zwYxnIF68Y1RolAJycm6o9Hfhybp8qW0eLp7hSQv0jp2%2BUyK5K1hVUTxmAeE4CCCcfkKTf0PE5oCZHYnANE%2FUUhO%2Fk7aMyx108ftQ8mJiuB8Szyqn%2BeDCbo5by3qij9cDrbCU7i8kMLC%2Flr0GOqUBhgH5MtMKCCHKPptbz0KEUANRfQkCN88%2Fa5u8r8uspS0vCthqwnVT2xODlDmo%2BX3uxT52CY0fOiWhSodfgL%2F%2B3kud1afBt0hdjlsr2CVqNC%2BAVs9WBx9658O5e4nc53NPoea6GUqj%2BtHfno4gISMT48b3jvzpbWoZe8pTizEMF2rda21pQulLZq6MOJ5SzLUdu5DzfpjaDFXHP0CDK%2B8rU2ekaJl6&X-Amz-Signature=07617940ab0e7dc3d08f2b5f51c2ebafae46364015619cbb8449941c60ee337b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQXLFF2E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQCskMl%2BYC%2BDYsL6rC33LRBl7QeAVm7c%2BRf4r4oPwjliqwIgOsbhWneH4mS6tSSoHYiSbuDmDAjX3zSVAuo5%2FkVcMTMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDExZQ7QUIliTsPR7byrcA8h3V68F86qfzxD7jfmM%2BNvph3AP6JkOdCd51vTiPFEttAUbCLOS3jHwZrm5mTkVZhERDQSrIHgpzyRUvt%2BaR8jadJ6kWeX2sN94MTzJxV%2FP%2BKDYlqI4TF2u5SfRa7DUXumea2UmCsVT1Xv1kk006RTWCKBOhhzcA8uYSCuPfwMY9YrOUX%2B%2Fn6bAs%2FdmEIDE76jTpcFFlz%2B2Hn1JBPK88lhclUqahPHBWgXnBCfjmTS9c%2BvwDoeAtGGlz7OOqFYgwxpoXIrn1lKhNuywUCrpzhtesG5vGXpqo8iiJbfguyoKKYzkGpEpgefSChBP1s3h0ghB3j5FYEitQYBXi%2F5%2F6X215JONHSwtZ8LhmChLoqhP83TENw8wClfO%2FMsyDA80o%2B1B4RKHwGENZf1AMag6OYr3vELxlSDjocV%2B53Nw9GswNCq2Nq%2FOQzG%2Few86ouM7%2BPY%2FKaNLq95MTeuTcXPkSMFahE3RibufssqNgrogVGykCupp9Y4zwYxnIF68Y1RolAJycm6o9Hfhybp8qW0eLp7hSQv0jp2%2BUyK5K1hVUTxmAeE4CCCcfkKTf0PE5oCZHYnANE%2FUUhO%2Fk7aMyx108ftQ8mJiuB8Szyqn%2BeDCbo5by3qij9cDrbCU7i8kMLC%2Flr0GOqUBhgH5MtMKCCHKPptbz0KEUANRfQkCN88%2Fa5u8r8uspS0vCthqwnVT2xODlDmo%2BX3uxT52CY0fOiWhSodfgL%2F%2B3kud1afBt0hdjlsr2CVqNC%2BAVs9WBx9658O5e4nc53NPoea6GUqj%2BtHfno4gISMT48b3jvzpbWoZe8pTizEMF2rda21pQulLZq6MOJ5SzLUdu5DzfpjaDFXHP0CDK%2B8rU2ekaJl6&X-Amz-Signature=36548f5a7bd88a6bbc01a9f220b2e181e047f05c25e85a4809206cd2e7838218&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQXLFF2E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQCskMl%2BYC%2BDYsL6rC33LRBl7QeAVm7c%2BRf4r4oPwjliqwIgOsbhWneH4mS6tSSoHYiSbuDmDAjX3zSVAuo5%2FkVcMTMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDExZQ7QUIliTsPR7byrcA8h3V68F86qfzxD7jfmM%2BNvph3AP6JkOdCd51vTiPFEttAUbCLOS3jHwZrm5mTkVZhERDQSrIHgpzyRUvt%2BaR8jadJ6kWeX2sN94MTzJxV%2FP%2BKDYlqI4TF2u5SfRa7DUXumea2UmCsVT1Xv1kk006RTWCKBOhhzcA8uYSCuPfwMY9YrOUX%2B%2Fn6bAs%2FdmEIDE76jTpcFFlz%2B2Hn1JBPK88lhclUqahPHBWgXnBCfjmTS9c%2BvwDoeAtGGlz7OOqFYgwxpoXIrn1lKhNuywUCrpzhtesG5vGXpqo8iiJbfguyoKKYzkGpEpgefSChBP1s3h0ghB3j5FYEitQYBXi%2F5%2F6X215JONHSwtZ8LhmChLoqhP83TENw8wClfO%2FMsyDA80o%2B1B4RKHwGENZf1AMag6OYr3vELxlSDjocV%2B53Nw9GswNCq2Nq%2FOQzG%2Few86ouM7%2BPY%2FKaNLq95MTeuTcXPkSMFahE3RibufssqNgrogVGykCupp9Y4zwYxnIF68Y1RolAJycm6o9Hfhybp8qW0eLp7hSQv0jp2%2BUyK5K1hVUTxmAeE4CCCcfkKTf0PE5oCZHYnANE%2FUUhO%2Fk7aMyx108ftQ8mJiuB8Szyqn%2BeDCbo5by3qij9cDrbCU7i8kMLC%2Flr0GOqUBhgH5MtMKCCHKPptbz0KEUANRfQkCN88%2Fa5u8r8uspS0vCthqwnVT2xODlDmo%2BX3uxT52CY0fOiWhSodfgL%2F%2B3kud1afBt0hdjlsr2CVqNC%2BAVs9WBx9658O5e4nc53NPoea6GUqj%2BtHfno4gISMT48b3jvzpbWoZe8pTizEMF2rda21pQulLZq6MOJ5SzLUdu5DzfpjaDFXHP0CDK%2B8rU2ekaJl6&X-Amz-Signature=1303b89491a782d7bf937785646074bc56c73c287d02e49ac200f0b027aae24f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=59fbcd76c1894c0ed6e6ee0b218d733734aec391adb4c4591b07764b5f633a89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=7362cbd7734a07ac51a4f43a8028c7c7af58e4075c6bffdc1f268da57896c4ab&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=c506612cb1f73c5e967c2d6d8d0346a3ed8389cfc9961bf1102017199d72698d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=fd1e42c59110e5add0413a7a08a751e9cd0b47e8933e9220c0454e37cc15e2b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=3060c558f1685f547d3f0126729f39df880af8ed35985dfc99dcb3316fd2fa7c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CSJP7DR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQD71cMqv4AUc%2BcrW2Ur7TZcCZV36kXbxlf5XuqXfBJiHwIhAKa2wK%2B5gt3rNcHOVaoAPbcbMj1TYLdQigPHMPDwdeGtKv8DCG8QABoMNjM3NDIzMTgzODA1Igy1m2DX9d2pjX8%2FrxEq3AMHVG3wnm6S55zpJZP0PfnEi%2FWRAOc%2B%2FcgQSN6aVn6JDlazxcbAtEcEBI5%2FHnkmK1emMZnm209v7p2gMZlhMvYNE14chdBpFTQDXzQwSbPva1cWvYNNe9Xwt2S06Q8RsnCAuaNPZkiYeCAltXbG4NMNSQBb5RIMDckTPPdy3NXBga8lJ3FIQY46KajK%2FZgobv3Dey7G5IUqvmhmrO1lNuExgvaaWOJc7adeNpBloJoLCq9wD6V54afyG6ZZQGjzmWIjNj7AkvwjigUGq8bfPG93mDxtDBBDooh81FVI%2BfLRHKqtrUJdrVB8qUurvvPNFvzSVh1AqbWDkljKxwTajXlHe4K66IfSTXlKMkYOGUUzEU7TV1fOgaRjJdKVEcShFLvQ%2BIIoioBsr1JE3%2FZ6kK2HBEQ51hBn251LRWTIUTuLXgsdulHsbvPaZFK3raT%2B4wFzQkzt90Xz2CGSBQGILW396fglN9zZfvva7PoGxNbtPRAuB1dM4B9%2F%2F09sX77Qca%2FyJjWFGXA72LVUo%2Fjagq6Sj6AIFAuluY6J%2BQiewHUoVmzNjzlR3Zh5OTyD%2FsnY7oslfUfJ4vJ9lhEbVnr13Lh8%2Ftj1arM0GFDMhGwFb9lsuv3lK6UKYNwoKBdxBzDLv5a9BjqkAbgepdDpsc6Os4FnXfUIAXW7%2BPWGByJFEkOXzT72pq2Ccfvu97GC7xeBCUHmoGkmyV0X%2BrUu3JtxTgHtWxG1VeDiuEuTkAWeilINA0EmbTG096ohw%2FvLcXqKOC4E5J5gT%2Fu0RRImhFgpEYenzMActF7baU26mCRGGSC4G2EnflnBD2Zy198ieKcMAbRar7kDLFExacC8glZzNIOLmmM%2F1iIKWlIY&X-Amz-Signature=b7d2cc6ae2ee47563a0a822b278b10a32f26b4f38d6f327f40670186b45fd09e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJOFAZDR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIAGyiFm51lPWhUKGkZ%2BKek2SKfw5vHve4y0DahaQv%2FX7AiEAsaOa%2FyqM8pTtWoTGR5le9pOuaigXtq5voLEhKwOjZNcq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDPBRRsG03A7EPLOSAyrcA2xDrwNeqSTRGDwBTXtRHurKXAQUm0Ci6PKIHDCst17eMBpPAbBw8ko0N7FX0g3mYSpj4AMh%2F86QbhEKs4ipD7BkyTK5KrHPS3xCGRXZ9R5N0%2Bq%2BleQCS4Td7zOB2Zgiq9JR%2F4p4WyopzA0SG43OPqIBEfldFyLx88E%2F%2BCE7KdQdh9P83hEuHdA41mGnxGGPBBO28hZDd9NRU5Q%2FUkQcwzfZQ9sSzfrEhlOwBYix9P4mcRZCD8Le8fEHFAIQydyTAZfPfPmiTED3racaE6nhD4IqKCSexLfZXimPD9ymmnC0bCG%2FahNOIb01%2BWKP6lRKrjxxsoX93rNaJz%2B5CkGNU3qpwclyxOW4aPOQ8JHid0rqP3IwHlLXfa6lZ9NOa9zganVUje7ElbQPXtTsStZR47Thez3C3C39iIQjW0XYwXM0OmV%2F20XG9T6ai9kh7N%2BQp7rOaR1HOAAort8zORRPwdd17tEnmkzh6IhBy0dVKAgzdIXmW7ADuvMDY0TB31HxwQjPtvPe%2BuO1Ug0AddUpLr1jP625xmUG37zRRT4tMZm7RhHt4OgIWz0fjNeJA1lX34%2B9WOCk1Y0%2FSCRFfqdBrtWWN6mNL5HIsqErgDdu%2BPa%2BLo9hsCBAq%2BYiH8ClMJ2%2Flr0GOqUBQVBCFs7ppB22vNymUI6OfwSvHByztLcMDQOmCFFghajZ7mql1O9shcMpR1G64YdL1Gx%2BcO5qpmbhW1ozYBDT1nyrvUbKAOuPXhSj3787NtCq6x%2FhBuTG%2BEs4wYLkuVNgTv7eCSJ45TDmZxBIhQbidX6egbVI97xAaw85Cca2ZIZmHa2%2Bq2DfdcHC3L%2FT6i9yo4Ck%2BmoCHIX0Y3%2F3hAEKlTck9N9l&X-Amz-Signature=fac748594c9e4f77eb82154cf6b37d4a5deba2a9d4c68b486ee52e0034bb68ad&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJOFAZDR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIAGyiFm51lPWhUKGkZ%2BKek2SKfw5vHve4y0DahaQv%2FX7AiEAsaOa%2FyqM8pTtWoTGR5le9pOuaigXtq5voLEhKwOjZNcq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDPBRRsG03A7EPLOSAyrcA2xDrwNeqSTRGDwBTXtRHurKXAQUm0Ci6PKIHDCst17eMBpPAbBw8ko0N7FX0g3mYSpj4AMh%2F86QbhEKs4ipD7BkyTK5KrHPS3xCGRXZ9R5N0%2Bq%2BleQCS4Td7zOB2Zgiq9JR%2F4p4WyopzA0SG43OPqIBEfldFyLx88E%2F%2BCE7KdQdh9P83hEuHdA41mGnxGGPBBO28hZDd9NRU5Q%2FUkQcwzfZQ9sSzfrEhlOwBYix9P4mcRZCD8Le8fEHFAIQydyTAZfPfPmiTED3racaE6nhD4IqKCSexLfZXimPD9ymmnC0bCG%2FahNOIb01%2BWKP6lRKrjxxsoX93rNaJz%2B5CkGNU3qpwclyxOW4aPOQ8JHid0rqP3IwHlLXfa6lZ9NOa9zganVUje7ElbQPXtTsStZR47Thez3C3C39iIQjW0XYwXM0OmV%2F20XG9T6ai9kh7N%2BQp7rOaR1HOAAort8zORRPwdd17tEnmkzh6IhBy0dVKAgzdIXmW7ADuvMDY0TB31HxwQjPtvPe%2BuO1Ug0AddUpLr1jP625xmUG37zRRT4tMZm7RhHt4OgIWz0fjNeJA1lX34%2B9WOCk1Y0%2FSCRFfqdBrtWWN6mNL5HIsqErgDdu%2BPa%2BLo9hsCBAq%2BYiH8ClMJ2%2Flr0GOqUBQVBCFs7ppB22vNymUI6OfwSvHByztLcMDQOmCFFghajZ7mql1O9shcMpR1G64YdL1Gx%2BcO5qpmbhW1ozYBDT1nyrvUbKAOuPXhSj3787NtCq6x%2FhBuTG%2BEs4wYLkuVNgTv7eCSJ45TDmZxBIhQbidX6egbVI97xAaw85Cca2ZIZmHa2%2Bq2DfdcHC3L%2FT6i9yo4Ck%2BmoCHIX0Y3%2F3hAEKlTck9N9l&X-Amz-Signature=101ef434c571926fd10ff45900825885f5f662c430bc4bf504402278ce996e91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LIQXWW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQCdVVh4ceShFzRzn4AiAUIPkObAkmfqG%2FQhwQCWaeBKmAIhALTttCVxLvRkv%2B0nNKtcwbKatd%2F7d2qaWbAb7YKXbir0Kv8DCG8QABoMNjM3NDIzMTgzODA1Igxsrym2%2BBBC%2BwfdnQsq3AOLmRP3TyMK9ucMY2ik8WkNyE5bXwkvRcvWqHFYtsCe2k5rD8cVT%2Bbt2GXraSYSanyY8gXpd%2B0tr9oUFoq6U%2FzH%2FJ6uY0FCxjVlwbXWlK390y%2BAejG6bSMJlmkt%2FjGsvVk1wPahES03hZ3NhnmWHcTNwpm9TmnO6qIbCzDLS%2B9apxZv6dW72gfph0ZhSi6RjRlvjdTmC0cC%2F8n8wFoYAwyr8VXIQPWEFmy7k9VYeN4tOhh3%2Fjn%2FwfUpkrFlsXTRzCMtzInW2%2Bvq5Ty1s52M3zk%2BEc2x6fKuWwlI7dWofgRnoFfRPTwOYFebZ2sAPjwnpfdEParifZpRzjpnxiIWfQrUYRvulUrK7ePmmxi9zc2OD2I73Exdxexh%2Fjvad4V99Ow05dcirC0dN7kCHDdy6i5cEWfOT0djwfoEAbaq%2BjjDbUL0gbJWQxe%2FTezSQKcz3pHQuoxP430%2FNRcDjMIspVvCK1UsOzhU1dfMpYwKNXXyH7IgvBDFNn64BW%2By3yKLdfsw1hzEXS21P8TdZdoFOW6junR9M1uGQjmEqw57czYbXZDaQpH67qXy2E9R7ph1Zty%2BNUm55rbpycjj0XW8nGLE6jJIz%2BgvKqdvCQOB5DqMzG7IY5fjyeNTuQUoVjDyx5a9BjqkARmv1rRw3vwH7nfkIoTPciETQBfhhBuDJVAKFoZy%2F70%2Br4RrbgeIlVv00dgZH4%2BVqzQ0gGinUBQ5IUal201I5ssBWLzhDejOEIv6Fuxn07LfmSQRiem5ps0vU723a7LCOGVav8%2FNs1rUCXya87UPyGLr34tthdXmrVDPLAb9ggGz8mjya7GfAWTTtya1mkRzat3yv%2BLdbXCHa%2B47HC0pUp%2F%2BFjtf&X-Amz-Signature=719755b1e3d7652647bc9ff12dd684a4ae1caaa42fcf98f44b729db73619dd9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D3SIZ3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIE%2FWyfk%2FHRQweRFP43S%2Bhp6CQe2o40WqvitchPc373H0AiBikViZEH6%2BW3WEtzpvGq%2FbG%2FqLXtLlSBD%2B%2BLU34zAAeSr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMhxCACwSNGQbaJlivKtwDxG6dQQxqUUrgoYC1c%2Fw2YTigBnQaqrIgiNqZuDJBV9Nq4%2Fm41Ui0leVkV4rdR6GHeW86TDRidmgQFq1z2xU4FubYrOWD5zRtugOvRnrzRlMmSYdwxeaqCQ2tD%2B2Sg3RKCa5yoMLr7KatF%2BKyMRi%2BuX%2F0%2FoHf%2Bd1p282uNtrnvIryyxXjMN8jMkh7Ze9LZVocPrfaI0wdmProXsSPtQ55UNfuBA5ftGSZpe9Ww%2BEH8ANm3eR9nBpVU7Ch22BGcNm3oFuTzgS6gHUGaB1gbwCfUcRtyQn1eevrkiTQaWPNKim3rrOB5RB0Pqh%2Bp6zo1FD9Pmas0YWQHw%2FWIvjEJAHtEtC8AMimPvj%2BqU0gu9VFdqX9yUp76t1fmO3vnN4A6ky56zQ%2F4hS9q8K0U9XbJFW8ATBL8rI9R34pd3lxhd3Kf7g549x0omj8did%2BdeKEh5fIFUEpbSoPIojxDyw5IOmhh5eaisreSYlt37yF2MyXMWTsmcQGcLdXPs0YSYvAtH7l5H%2Fb07rSe1tNUULYM1%2F1qyK4nn%2FmwkD0eHklIoDzFvDZnqcaexkp3W0U2lQWHBU8xExAVq1X4IF9gM9McdCSjNB1kZ62m6sHh4qVWM9Z4mxyFn4q4jA0YliaTVkw7L6WvQY6pgGXrVfPzwuXSPUf915iHi1CsKg9m%2BjMG6%2BP8gJHxyu3qdF0RYF0YZpjjolN1B3eCiCotT5cPEXDXwDwNpTgPzfKL%2F3xaX4Nmom5MiBqZbm%2B%2F41CNrEiMU7bzcG4gyvCMkWvj6teoYHGz1cz6QhkFLiZi6GWR0S5sV3oZTVcodTqKBxG%2FnmR2OZ%2FJlTuq28rH9WoKVFhjw721jPY%2FZL3XSgMtIw6VgyX&X-Amz-Signature=85de211ef7b419f5ef329a32ce1729d1ea4356831ab716977bdc19f4cd614f0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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