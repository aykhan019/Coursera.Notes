

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=d8417e13eefc473c1ac027ea5e230dd553bfdab962ba873bc86b0c729d500ddf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=5c741e3eceb3aeef29751d7db094f7b6a6d66b98a00c239b7f3f8c294ea0585f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=5a3c63aba856bc499c59bc29fe60b510afa065073961bc419e0f4a58f7fc4c05&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=3cd07cab2b8729f334269558fd68d818298ebc9ffeeb80e2501268a6d8fe9eb1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=204fe594b4365e76078c8a8ecce64e51677d9a4773ddbff1f02b8ad7b3fe8d17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=52bf7d7bcffd571f475d29034bac5254a410f3e291cc599bed50a9750c450304&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=7cd91a3d1532ddee490b15f8818976bc9a5ad330bfa771a73f3a737adce7be54&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=5b837899353635aa18eb8e8745bb102513261dcc0cd089e77897c606a0f2660a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=9bf214f8018cd7f855eb0980fa78df63f36b3882908babecc215ca0985abefe6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UORZS3TW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCID8tDWfQLk%2FsvOshXAcnPB7R2XbJf%2FI6FX9g5so%2BSbjOAiAdykQVv49AGIyqbxjummEQ6yVpDyqaSr%2FTGKzTih%2F%2Fqyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM5fh6QpILhQQde5fLKtwD1frhFhYUFRqaDBMyEmvuxaUkHKSplGZSh7Syteb50FdbdxG%2FHgBDnNVK4%2FWZXq3T6ssMc8jrcAA5HfHCovyQaaZgsn2QrGrjLHkJsaxO2r2cvwV4mweC5Vu%2BROS2qWaAP3D9%2Fk12YKtV422uCLMO1x%2FHZvr9fHnlhrFbr9n4Kzip4AiLV64knoKpz0UhWAxunPlrpWIYtjBtOsVy2bIEkxfyHUEVagZlWaWb2aYaHvRJSoRUhTYEZrNRqBmflDubeK2BfdUyAoRZdVMduTyIcgJtO0HsVqg374NSThOk90sR0m6M7B9fglSvebo9oBDzhgrxLckEnQ54uypvfw6OcrXhfLAuYCddyLXNv7t2kk9kZ23hqdPFPwK0tu4Yclut2aADDbdJu1MH618fhVaKIiS2ljtGsXqW4UtALxNGpPiU1DSZOBKqm2YFjTtb%2BzCBW2H0aRenrPhrhVUFDZCzISi85a5ftK%2B%2BwMbh7wJeAAZADHAeDJgiDv5Lzkt8niZnJto1aZauvsbsCoNLUlh3vdsum%2FosL3UBowmAoGt3Ov1ICY0saqWNxBC8LASNoKu%2FfdavRVkSWkkr%2Fd12sQvTDBWNSzG%2FqVqAY7cEMKyI4RiA%2BI3m5cNtbb%2B0PDwwrbqOvQY6pgEUTrXaYx5bz7MESB3Doej%2BtudMuFjKVvOpOeO0BcuwwmK03oN2JFoH8Quln4Im7vxClYP%2FXGEnEc5pUfzw6ERmQ20UyXh%2F6zQqsta8RP0KewAggQ3W%2Flx3PzB%2FcZUGXuha3GIHAAUMLxosqcK%2FpKn9%2Fsb%2B8h9vn2Uce8%2F%2BqwPF0sCg8eGd4aE0%2Fduf8v9YMFutEPwpE4Qv0koPiMFFjtiryo3dw99W&X-Amz-Signature=bde5a657d25f3ec61b8e788d6d87fe0e700398119cc4f40b45ccf118c0dc20d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UORZS3TW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCID8tDWfQLk%2FsvOshXAcnPB7R2XbJf%2FI6FX9g5so%2BSbjOAiAdykQVv49AGIyqbxjummEQ6yVpDyqaSr%2FTGKzTih%2F%2Fqyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM5fh6QpILhQQde5fLKtwD1frhFhYUFRqaDBMyEmvuxaUkHKSplGZSh7Syteb50FdbdxG%2FHgBDnNVK4%2FWZXq3T6ssMc8jrcAA5HfHCovyQaaZgsn2QrGrjLHkJsaxO2r2cvwV4mweC5Vu%2BROS2qWaAP3D9%2Fk12YKtV422uCLMO1x%2FHZvr9fHnlhrFbr9n4Kzip4AiLV64knoKpz0UhWAxunPlrpWIYtjBtOsVy2bIEkxfyHUEVagZlWaWb2aYaHvRJSoRUhTYEZrNRqBmflDubeK2BfdUyAoRZdVMduTyIcgJtO0HsVqg374NSThOk90sR0m6M7B9fglSvebo9oBDzhgrxLckEnQ54uypvfw6OcrXhfLAuYCddyLXNv7t2kk9kZ23hqdPFPwK0tu4Yclut2aADDbdJu1MH618fhVaKIiS2ljtGsXqW4UtALxNGpPiU1DSZOBKqm2YFjTtb%2BzCBW2H0aRenrPhrhVUFDZCzISi85a5ftK%2B%2BwMbh7wJeAAZADHAeDJgiDv5Lzkt8niZnJto1aZauvsbsCoNLUlh3vdsum%2FosL3UBowmAoGt3Ov1ICY0saqWNxBC8LASNoKu%2FfdavRVkSWkkr%2Fd12sQvTDBWNSzG%2FqVqAY7cEMKyI4RiA%2BI3m5cNtbb%2B0PDwwrbqOvQY6pgEUTrXaYx5bz7MESB3Doej%2BtudMuFjKVvOpOeO0BcuwwmK03oN2JFoH8Quln4Im7vxClYP%2FXGEnEc5pUfzw6ERmQ20UyXh%2F6zQqsta8RP0KewAggQ3W%2Flx3PzB%2FcZUGXuha3GIHAAUMLxosqcK%2FpKn9%2Fsb%2B8h9vn2Uce8%2F%2BqwPF0sCg8eGd4aE0%2Fduf8v9YMFutEPwpE4Qv0koPiMFFjtiryo3dw99W&X-Amz-Signature=212d8a3f865b3460a91e83a9c5370f3e435fd0f8974d0958b2af8134b01268ba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UORZS3TW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCID8tDWfQLk%2FsvOshXAcnPB7R2XbJf%2FI6FX9g5so%2BSbjOAiAdykQVv49AGIyqbxjummEQ6yVpDyqaSr%2FTGKzTih%2F%2Fqyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM5fh6QpILhQQde5fLKtwD1frhFhYUFRqaDBMyEmvuxaUkHKSplGZSh7Syteb50FdbdxG%2FHgBDnNVK4%2FWZXq3T6ssMc8jrcAA5HfHCovyQaaZgsn2QrGrjLHkJsaxO2r2cvwV4mweC5Vu%2BROS2qWaAP3D9%2Fk12YKtV422uCLMO1x%2FHZvr9fHnlhrFbr9n4Kzip4AiLV64knoKpz0UhWAxunPlrpWIYtjBtOsVy2bIEkxfyHUEVagZlWaWb2aYaHvRJSoRUhTYEZrNRqBmflDubeK2BfdUyAoRZdVMduTyIcgJtO0HsVqg374NSThOk90sR0m6M7B9fglSvebo9oBDzhgrxLckEnQ54uypvfw6OcrXhfLAuYCddyLXNv7t2kk9kZ23hqdPFPwK0tu4Yclut2aADDbdJu1MH618fhVaKIiS2ljtGsXqW4UtALxNGpPiU1DSZOBKqm2YFjTtb%2BzCBW2H0aRenrPhrhVUFDZCzISi85a5ftK%2B%2BwMbh7wJeAAZADHAeDJgiDv5Lzkt8niZnJto1aZauvsbsCoNLUlh3vdsum%2FosL3UBowmAoGt3Ov1ICY0saqWNxBC8LASNoKu%2FfdavRVkSWkkr%2Fd12sQvTDBWNSzG%2FqVqAY7cEMKyI4RiA%2BI3m5cNtbb%2B0PDwwrbqOvQY6pgEUTrXaYx5bz7MESB3Doej%2BtudMuFjKVvOpOeO0BcuwwmK03oN2JFoH8Quln4Im7vxClYP%2FXGEnEc5pUfzw6ERmQ20UyXh%2F6zQqsta8RP0KewAggQ3W%2Flx3PzB%2FcZUGXuha3GIHAAUMLxosqcK%2FpKn9%2Fsb%2B8h9vn2Uce8%2F%2BqwPF0sCg8eGd4aE0%2Fduf8v9YMFutEPwpE4Qv0koPiMFFjtiryo3dw99W&X-Amz-Signature=e8a619ff8a9b42948dd7d1f5f7d31677853214d13b15645f1ca159b77d6baa1a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=bdbe408188436cca420ae63c5db89ef9d2de5d2cbe2f9e4cccde5126eca12613&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=011e9d760032744087060f2317d8364b4c59fecece1b1f3655b781e3fd8d7139&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=e90dac652be6552c30d9254e89ed85be8ffd0c408117ef52ef9ae14da48d5447&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=68741361b75cb0597e86cd80030f6d5942cfa5938abf930b1a920a409e1912cc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=30298c65b6f2c68e1f1d9de2bc97ccad6555df5104d5a3a8f12faf9959d6e098&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGVXMU2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBfSLuFPMRzzVzPJ0l5Ph7NNiE7zwsG2y0dWLYB%2FSaLWAiEAlafw4QzeQ8fI01VaV7KAPRBEhwyGiP9%2BSZK2ImDJTJoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHGRNMwjiL0%2B1fvJVCrcA2faw6vq5xgIVZ2Hv7tx9e5AaEhe1TvXLdREGCajTS2hmgl5NQCaVc9%2FS1Mc%2F1PoFvBdhZTdiNBCDWXcG%2BjlUyFkhOSrJQQqG621oDPrpmLl4WKpvRgmXc9VOEi4PIYGcQpji9Wx57ViUOAUWE64lTeQD2DocolsWjS4EfjzEiNVdLQL80QaU6kYJz0g3NMB9x%2FpL3jgiJitLspPW2c8iXuHF6WFF8p26bo9ZOf07aS4mrmNZjPn14%2Bc9lwHPv3hcbIpXdQYB8dsE79uVxIiWtQ3yFDy60SVlIA7kyOPeZRUpbDhF9kc%2FjJjx3jeYvqYlQgvEg6%2BiP106rSNC0t9DvYAxb%2BlHgmoWWuI8tN7IdMvYNCFYhYHZNTsw4aC8G0DdNOf1WOFRjaZbX8psCu0wjIEjsODDLmyrlfiGdgbdWB1LBCOh46KEtvFp8YNvQqrgCYKjtc8Wpf9Hpwf6aO6cxCxqcChFGzf4liOXgMedmvjy2ZPXfAcn%2BBMUanJItLuw3g%2BCg3buubJWpsG39L3sv8B%2BCYimliNizEPhh7%2FMC3FNkHn081z7j3E9%2Fn2NBx%2B8Fkh63CUpaw%2Fp2T0U%2FYVNPpYR1iMvdPEwyTjtMsZ%2BKkUs6EUyG29vkxMADJJMNu6jr0GOqUBc%2F1qLeds1yeEV2liw3pJ5ro3gPqDsAsv0o4o4wmFrVmQMQa4%2BMJG7zJ9Zc%2BRzS428L8JGfUgyczgN9vm5YGhL4xpUNSOrdG4fykmNcLE32E%2BTQ8CvkaSmFL%2BpKGPNSk3YkulVxQSyzNgBvCuqa9xnMfomSSbPScR1nu0K2DYE27AV2sXlNKHOZKPo%2FVGP5Js9Az7VvFj79sKfXS8DWIsKE%2BFdFve&X-Amz-Signature=7e4a3606f7df9be4ad56bf5ed99e1d6b3281dc14437fbce80671990fb196bde2&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB55BNYJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIFF7ukCYIab294pZe4TOc54GdLE97sWgLap0%2BKrBdJRfAiEA3MnscDFWF5P8c3EpZLzT8jOyLn7Isy%2Bqcu%2BvKWY%2Fy8Mq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFecYvSpl0GWPwQe7CrcA0gMA%2Ff3YaAzCMNKGlzpID2viv3dsHH6xSZ0vHh0eBBXmWk8%2FR50Ggs7Ylf06yl6b3McijoPwgQoHJFc1xEPRGbe%2FzOVXvf0FmrpxW7WgxTo3ZAS9OEyPD4s%2Fh1Xt3%2FmEGiJEc4vWnZKFTN1HShfRaeMXEBk%2Fxm4lST%2F3rldFmWfgoHESGGZVJEFTSPi0dVtsCaykzOhCmcrtLQlotTHXB88WbMGlaJdBLoQMXILBBpw4tfsQFhFlbC0XQ57Z5VaBhEgQAxHZ%2FFi03tXgt5p5EuRLompsh4IeJzoHfFHI5EiPu4x30s59nw%2B2wLKRq25ygysIkKgIUMM3BLh2kLHkJ0w75MNfIdjqLaVlltRVf86Z5ufwWMxlKn59ZgTZdyAWdZHsnHVga6ttMj4OabQKEKTveoWkfROo3dpFG3fJfILGjcGyqwmPFOzuBqrMf%2FrJqUnsjVAT3cmbjKEAAXhP3CE%2F3MTmyyQJiSRVqZH%2BjfTYbIPzmWIIDr4WJwrUXtD2tDY%2B5cWtZ38aVsoHakRTUiKV1IAhaIpt%2BsbmEHl3VvbGZrGo%2FwAwQxVC5tJy8nCiwyI2Ks8MmumibvuuDafmXhmGGNz2G3CVZJuXfE%2F%2Byz%2F0XoO03UOv9ZoMdq4MNK6jr0GOqUB9ZlxzyrCKYOIGtAYUIZbvav9f1imDj3vgglo8oHpOon5%2BbB8wgMfOAKmdpx9W88Ece%2BJuXKyOubPTkw5wb8xWo0hl1wXJCBXkzp5Q%2B6dYHMd0MIH53j9kvXdExADRIeGH66RBbxvKhPs49VCd62E1TZLxRhwaTNl%2FsWzGvet4mbA%2Fi8d%2BTb0REhxEFm6XhUkCGaJWsXoDASOkBfdsHvtdGCV84Oq&X-Amz-Signature=6cc326ec6be60d844e727be88c4caffc8986953f5dbe407760a8299404e4fdee&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB55BNYJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIFF7ukCYIab294pZe4TOc54GdLE97sWgLap0%2BKrBdJRfAiEA3MnscDFWF5P8c3EpZLzT8jOyLn7Isy%2Bqcu%2BvKWY%2Fy8Mq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFecYvSpl0GWPwQe7CrcA0gMA%2Ff3YaAzCMNKGlzpID2viv3dsHH6xSZ0vHh0eBBXmWk8%2FR50Ggs7Ylf06yl6b3McijoPwgQoHJFc1xEPRGbe%2FzOVXvf0FmrpxW7WgxTo3ZAS9OEyPD4s%2Fh1Xt3%2FmEGiJEc4vWnZKFTN1HShfRaeMXEBk%2Fxm4lST%2F3rldFmWfgoHESGGZVJEFTSPi0dVtsCaykzOhCmcrtLQlotTHXB88WbMGlaJdBLoQMXILBBpw4tfsQFhFlbC0XQ57Z5VaBhEgQAxHZ%2FFi03tXgt5p5EuRLompsh4IeJzoHfFHI5EiPu4x30s59nw%2B2wLKRq25ygysIkKgIUMM3BLh2kLHkJ0w75MNfIdjqLaVlltRVf86Z5ufwWMxlKn59ZgTZdyAWdZHsnHVga6ttMj4OabQKEKTveoWkfROo3dpFG3fJfILGjcGyqwmPFOzuBqrMf%2FrJqUnsjVAT3cmbjKEAAXhP3CE%2F3MTmyyQJiSRVqZH%2BjfTYbIPzmWIIDr4WJwrUXtD2tDY%2B5cWtZ38aVsoHakRTUiKV1IAhaIpt%2BsbmEHl3VvbGZrGo%2FwAwQxVC5tJy8nCiwyI2Ks8MmumibvuuDafmXhmGGNz2G3CVZJuXfE%2F%2Byz%2F0XoO03UOv9ZoMdq4MNK6jr0GOqUB9ZlxzyrCKYOIGtAYUIZbvav9f1imDj3vgglo8oHpOon5%2BbB8wgMfOAKmdpx9W88Ece%2BJuXKyOubPTkw5wb8xWo0hl1wXJCBXkzp5Q%2B6dYHMd0MIH53j9kvXdExADRIeGH66RBbxvKhPs49VCd62E1TZLxRhwaTNl%2FsWzGvet4mbA%2Fi8d%2BTb0REhxEFm6XhUkCGaJWsXoDASOkBfdsHvtdGCV84Oq&X-Amz-Signature=0f6db6cc9b2b9113c13bf479886e703a84342afc0653b7c8155416add152594b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSHGLXNZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCTbfB6EUWJl4w2gHl9bMPnIDrP%2FmgtMS0E3LBnjpQB8gIgYKFVd6NV0NTc6oBZduEuGJX7gmgNvwru1dTnDcGRLJoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDKpgAMdQBFtH9VwvpCrcA%2BtKCMyah2WXPhb6%2BTE%2BTcsmEb3UgVGqL8xJjxGS4iMkzKeD49YHeHsyi4toPW1j0XNljjImk0eCjJz6AIAPJqK2K65jEYJsz76DzJM4fc%2BSaPmhufncaB6AeIO5pPIWmQ%2FE7yS05Xv3wrazhSjHDeFk2hEn8EMeoYwnMvVYUwg6a30nwp6dAUUnCyrPfq7no2ExsyLCEp7Aq1G6mM4VVm6NicgxktqqJlZ5PY%2FlMh58XKBULrgDyqDPOuvNmoStcoJmO0zgDJ7S%2BD5sxfPK1qieZGlUPyoarRuH9RnhOR8O85sY%2FkarHFffsFW%2Brbwa3aq9sSaSBXVTdyUX%2FhLi5gCP%2B%2BgznuBVUck3g7CFcu4ZO38G%2BsRgPs3rGS%2B0DUHrF4lQKTFk7cZZz8%2FtXDbhN%2FjPvl3U2T9zZpEoZOalJ%2B3yBkHbt7c1Bl3ELfhg4lSiR03ftdducbNAuhcoRbbtXRCCLvlZepJY%2FPCMHGxzrZMCzTFHxueEaKyb3plziCv3p%2BjF%2Fi2McsIwJ729at%2FKlmtfdzb%2FBvLRVKxdbr9enNbue5FQbN0i97b8dV6Sl0a6P26VHB0w7K9VYFpnMpqdSR1hvgIHXFmFY%2BlPKmC6Dxh7j7a5y5Ot0mxihoMcMPG6jr0GOqUBRqLf46LFvltB2b7hVH5CWO4hiYZqJgOiLfHL%2BmtwAaBOMUpv32%2BBaZkr5pvanKDsRhKVcKTb241EAfzF5nyg0IZj3ckypBf2F6qLX6%2BBZrZ3MLvGffxY3TmjH7G7I1vB5IlfSlPq71Zmsx%2B1K6kXkaY6YTvyQN1o7HYAS5PqTHvKrNaptdme4Xoficu3qSFZz%2FFskMpS8IPMf43rDuGFfiiOjWzl&X-Amz-Signature=fafbe9b7d5f159d888bd488414b888a6967c05a9006e8a1b7d637239c38fb43b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZEEUDIY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBlWvToihrbLLZjMkvKhDA7hi6KALtxnDReYwIhg7H9KAiBk20slVaYP4dGG5X4hjVEouh11a%2BlBNVOQaVEHhSv0kir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsgguTqIP%2FLsuEtUYKtwDhrIjcnIXKT57mDRjuqIzeB%2B%2BUCwNj5w2Pg8zr0%2FVXgOHmBv1OUzr45y95TGWko9RWluruikq1yNcLqZv7AD4wXQSxzYJvuMgOueFF8x4vIRjKyQBlxmUQYjrwqsuOBveucVExWBCptMb2cyAzhmivBFWLkqBcox1vMn1wePDEmm703IunviPXPfcNHn5d9DCZyOjgJKgbxerMZ33AZeA%2FUq7Bx1Nt9yE7t5inrjRLokEi43%2FIKww1E%2FeLkYltJZz2EpEXzH%2B%2BQl4KpQPngiIxpwAVSfnrxag44EVqy1n9oKfd99c1RD7NWxEqMqNLtk0oi0bhxso0YDU4ewhTGVb36zKn5G1gNczuIK1VXMk9JAmzNBcbseUA%2BSI8KwNBkIpHPr4xbW9s5Ij4IIrEZU27Jfz31wxTVZfUjjoSxKj1Na%2B%2FmH8c59B%2BST0rVBdIZhFrIuPWp6zTGgx4yZNKlSXMGzYWAeOln6%2F%2FjAYBbHDriaDmUP%2FRzPHYcz5NyJcMCUhqZCObM4c9g6KeR%2BXd9PUN99V%2B2UsFO%2BTn8hSE4fvlx%2BaOf0TfDrgEa7PrAiyB6T9Dr2jSoZpt6JRKpMwd0K6RNhAH1x2kzctCO30E5YqNGIQpMK%2B%2B30sHetV5Fowt7qOvQY6pgFb2OfV2QMN90wlLZ%2FDNavHW0uWzxk0cNRTRVWO1%2FgfFJDwtynUTQJEFjlMth7KoOja14WVLUWeVFnNkkEvGeS61efXzBzXIWDHsDYPzmZJWIHgyP8RIfMZo4lL4XEsa%2BvC%2FAGdwnm1WYsXXvuuqFWJxHF9mNR%2B%2BTvqtrQSQdO2LtGFQ2%2BvJRlG%2BU1c3mpFQhQs2UfeO6LaIwa7toIg790CAAG9KNNA&X-Amz-Signature=70d37754100f21012e8fd9553b1263cff70d05182406bfbcb1db62660bd2d243&X-Amz-SignedHeaders=host&x-id=GetObject)
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