

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=a790a3df7dabfd853b7bd03013805ef2f295ea80ca4412ac1203b51b7189df8e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=467734e2bc3e0b42c058a697e70c7cef07bc54f141a069bf87fddadd79427251&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=863a9415d08c88f7fbedcdfd24e5e72b209ae3f7c9cb8893dbc116e1266d2b77&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=1da5e6b865c40773cd8be1f504e3f6bd3cac1581c4e4aed61996c447148b9c01&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=b0c5cdb47aaac7330b1f28fe92a94a1a52c844c89fdc4494581c66144590cfb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=349357866ff4a4d5a5495a237765a5b317a534a7bf45b6909b04ecc7bb3aaca1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=68a858cb4831f840d43bf72330906a6bd9e8410f29de6db8f5ad40c484a97acc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=c9dccb0c8c0b28a8c91601c57e328a7aeb36a06e5c6ceec9d354515797db8b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=12424108e87d62a24748a153535de0d3a5317d5df0f776548817fedccd21e469&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QN56JZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBSFgGLjiilltd4gBgbCVvAhT1vSClKty%2Ba3NGqgnxluAiEA9Jaq2lmx7C10DwbfKYL31kqesgIc8McFM%2FVcOTbNGnsq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDLM9%2F372a%2BQESoDcLCrcA4enEvT%2BXgsnEOGrFg2ewAAIxqdOe%2B%2FWAZPvmbIfX9UC2bi3ty0vdXIZel62Mo3xpU4D5Pe3KPWZULPyVFGYKJ9SSYgLamDK3YABHiHyFEhXlno6HLr70baRRhj2H4%2BMkc%2FsCRQ0VeAvSasmZWxj4gjXyHR4mNzy6CCRrPPoDYF6I9a8Ymh6dQ3VtfKAullpFJMX98LvFkXQbf6Rqq4CQv5m9zF3ofsgtWRSwrnFnfz5nOdLd%2BbGwVyV1JudggPVvCyrXqC6%2BWn%2BBFUrUzndueStspgXayX6n4rt%2BEuLGq7Yj%2FZdH0%2F6DNZu6Vx6qjPhn6hf80749Lo4QWsAowTMQafrgp2dZDt8IKBLwACRwfiSwN2qb2tHJbXBNeZ0wg5WyKcGtuZ%2FcLxLrFSU07AS9mn04U6yFBMsWUX6qmoccmFSq%2BPpxn%2FVgMWriF%2B2nHjGT8ZxeV5EqIQOGFTNhLbGfAPGCXO9U9v%2F0N9qFOM0iMSf0ghsxggRlk1Yk106sqH6Fp2QRV5Crh1Kccif268luFMldbF1pO1JdUVcgY3f5LsJwR7AcV1jGAmT0THhcWBtxuQS%2Fi%2BdzgyDnVEvI%2FrIUTP3PDGmXK%2B3U%2FEwSD5rUTFb8bQ5HPX58crZlYjgMO%2Bbk70GOqUBMPOXRMOnH0DAztOg1CjGOEMY2OqMRIlP1G4X3m3rcMF6%2BO8NAnUGxeIubFbj0DTof%2BnQYU9zdH%2B%2BpGkwt%2F0BLNEsWZE50iO5prHoVtP6O8o8mlAMnoY4reaxAaX5vBypwYM%2BDdp%2BonUb59pbAjSkWXW63wkTVW0DAtD7TwWAS0RwAaaxMpqL9bskpbykiGK%2BD9MMQcKLWYULoHMuh23a7xGLrCy%2B&X-Amz-Signature=ca49588e51c70f350ffe6b2993f3e3acf4a3fb4b8ffc34750979381cf0c91258&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QN56JZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBSFgGLjiilltd4gBgbCVvAhT1vSClKty%2Ba3NGqgnxluAiEA9Jaq2lmx7C10DwbfKYL31kqesgIc8McFM%2FVcOTbNGnsq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDLM9%2F372a%2BQESoDcLCrcA4enEvT%2BXgsnEOGrFg2ewAAIxqdOe%2B%2FWAZPvmbIfX9UC2bi3ty0vdXIZel62Mo3xpU4D5Pe3KPWZULPyVFGYKJ9SSYgLamDK3YABHiHyFEhXlno6HLr70baRRhj2H4%2BMkc%2FsCRQ0VeAvSasmZWxj4gjXyHR4mNzy6CCRrPPoDYF6I9a8Ymh6dQ3VtfKAullpFJMX98LvFkXQbf6Rqq4CQv5m9zF3ofsgtWRSwrnFnfz5nOdLd%2BbGwVyV1JudggPVvCyrXqC6%2BWn%2BBFUrUzndueStspgXayX6n4rt%2BEuLGq7Yj%2FZdH0%2F6DNZu6Vx6qjPhn6hf80749Lo4QWsAowTMQafrgp2dZDt8IKBLwACRwfiSwN2qb2tHJbXBNeZ0wg5WyKcGtuZ%2FcLxLrFSU07AS9mn04U6yFBMsWUX6qmoccmFSq%2BPpxn%2FVgMWriF%2B2nHjGT8ZxeV5EqIQOGFTNhLbGfAPGCXO9U9v%2F0N9qFOM0iMSf0ghsxggRlk1Yk106sqH6Fp2QRV5Crh1Kccif268luFMldbF1pO1JdUVcgY3f5LsJwR7AcV1jGAmT0THhcWBtxuQS%2Fi%2BdzgyDnVEvI%2FrIUTP3PDGmXK%2B3U%2FEwSD5rUTFb8bQ5HPX58crZlYjgMO%2Bbk70GOqUBMPOXRMOnH0DAztOg1CjGOEMY2OqMRIlP1G4X3m3rcMF6%2BO8NAnUGxeIubFbj0DTof%2BnQYU9zdH%2B%2BpGkwt%2F0BLNEsWZE50iO5prHoVtP6O8o8mlAMnoY4reaxAaX5vBypwYM%2BDdp%2BonUb59pbAjSkWXW63wkTVW0DAtD7TwWAS0RwAaaxMpqL9bskpbykiGK%2BD9MMQcKLWYULoHMuh23a7xGLrCy%2B&X-Amz-Signature=122b795f8941b37f61d8e261ecfc6098f24492923e688cf33e2ec7eecc9d5c0d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QN56JZ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBSFgGLjiilltd4gBgbCVvAhT1vSClKty%2Ba3NGqgnxluAiEA9Jaq2lmx7C10DwbfKYL31kqesgIc8McFM%2FVcOTbNGnsq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDLM9%2F372a%2BQESoDcLCrcA4enEvT%2BXgsnEOGrFg2ewAAIxqdOe%2B%2FWAZPvmbIfX9UC2bi3ty0vdXIZel62Mo3xpU4D5Pe3KPWZULPyVFGYKJ9SSYgLamDK3YABHiHyFEhXlno6HLr70baRRhj2H4%2BMkc%2FsCRQ0VeAvSasmZWxj4gjXyHR4mNzy6CCRrPPoDYF6I9a8Ymh6dQ3VtfKAullpFJMX98LvFkXQbf6Rqq4CQv5m9zF3ofsgtWRSwrnFnfz5nOdLd%2BbGwVyV1JudggPVvCyrXqC6%2BWn%2BBFUrUzndueStspgXayX6n4rt%2BEuLGq7Yj%2FZdH0%2F6DNZu6Vx6qjPhn6hf80749Lo4QWsAowTMQafrgp2dZDt8IKBLwACRwfiSwN2qb2tHJbXBNeZ0wg5WyKcGtuZ%2FcLxLrFSU07AS9mn04U6yFBMsWUX6qmoccmFSq%2BPpxn%2FVgMWriF%2B2nHjGT8ZxeV5EqIQOGFTNhLbGfAPGCXO9U9v%2F0N9qFOM0iMSf0ghsxggRlk1Yk106sqH6Fp2QRV5Crh1Kccif268luFMldbF1pO1JdUVcgY3f5LsJwR7AcV1jGAmT0THhcWBtxuQS%2Fi%2BdzgyDnVEvI%2FrIUTP3PDGmXK%2B3U%2FEwSD5rUTFb8bQ5HPX58crZlYjgMO%2Bbk70GOqUBMPOXRMOnH0DAztOg1CjGOEMY2OqMRIlP1G4X3m3rcMF6%2BO8NAnUGxeIubFbj0DTof%2BnQYU9zdH%2B%2BpGkwt%2F0BLNEsWZE50iO5prHoVtP6O8o8mlAMnoY4reaxAaX5vBypwYM%2BDdp%2BonUb59pbAjSkWXW63wkTVW0DAtD7TwWAS0RwAaaxMpqL9bskpbykiGK%2BD9MMQcKLWYULoHMuh23a7xGLrCy%2B&X-Amz-Signature=a5b284aebc8e342bf56a109df88a4cc4ea31c466ed170e65a38cd538cd346275&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=7da2f5b071032b27dff04cfb799a28128329bd385798631ce8358dc14a3fcd61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=2c4e6089fe96e5244746e0f93103c9dc4a119dc0adbe66dd8735dd351a2854bc&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=03b1fefb31d020fd095e31900c4e4e269167b44175e7240ed948d6dc1d0ed63d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=f10aeee3d824d11638f59aec28fba669ab11a0a406cea58ad4514cae05bb4692&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=5cbcacfbda23b5163a18bde63064142ee7bd1680116656f78c9eb4cf0926e6f3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGZXRRD7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGNPFUtMzCjsjUOFymYQLJGToCQfJRmCPgRcbiGBCZRXAiEAl9U8MXc1MNY7dzypiMa%2FHxWPiqhS07n1z%2Fi%2BMGyn440q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDIM7ABoyCW0Kki1jRircA3rn7%2FGQpkIqIZ69fjmzo2n0Jgkqu2l9vSkD6akudiUQ9tMJoM1WyyBkjFMRSyOcvo7P%2FJOP8KFhZjf%2FPNk00v%2BxjONoMA4ctgD9H69nx57rMXXrGk6aDFsJH%2B%2FgMIr6bg6azDPhgz4869hLaKYRuLyHI60gFA%2FdC4oE44pvdTnu3ixJiMX2TRqh6Sc%2FadcdOZWuh7DLoNGrbNE5Tn63sakm2dFh5rrcKgHAcx2tKFqvk81CD%2FdGXQuOYgMLrcUEVwLHtXBdj52xe9noLHzs4oniVkZAtwvlxymxsWAyRmPVnJVpgw%2Fv66B5hJ3KEdXFAjztoChOKeSJPX2lNEM%2B48w0LyDjjN4CUkZmnxIoy9sDJYqioZ9pMeyYpjQnjqWoe1ekzDnyT%2BaIoIbzuybmWoExWDGD36ZjyOj1xhRF7x56r79rCi3y5Mqfycd4jxFTPxNCtFGtUabBSNkZdX3X8s6T4etgw%2BlzqgQqysQs01qAHwjLX82dcBhPW9wX645hxjRztSdnRh4PhhvnN4haeUcLhOyaAEMw1ih%2BUwlHTd5rNB4XPp059Edx54TqnMU8Qo1ZLH2Zre6DxLXiHpSHXk4SDMeFO8ZNzqLAah4WQGx0bIM0W7iuRN2LU7hbMLuck70GOqUBu04CWRTb%2FI07g4TVfeISuyAfMfSnP1xBlev7lOxJD5SeQhLYPeOFqH6ezbf0zoTWWDJLhkXB5yfr%2FVsq0qnO9qE78%2B%2FrNTQ02YvGH5HPhOXaQiRKMeg1OQGGzhaeTaxUb8fgwb%2BowOkQ3NED2lJzl71mGAgquM1B%2BkiGOEuhabbnEEtW7w3lcSOV0qZyfikPWQvPikqb3SyqHjXdVq128NvCvCxu&X-Amz-Signature=688f77ba8c1b23b3b8fbd97d55b6c67c6d743ad287112dee67dc692fcf246718&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RR4WTZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGfat%2BsAEhNUHb4yBe4BONa49E2JvJuk7CM2zE1D1czzAiEAi7Fttq8tJnRW4CMH8gu0KaLmTRkGCX9bqNTRnZvbpnkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJhLFsya1upbebgHxyrcAxIYvRQwZBNnNCrhPnLJftQd3Emuq%2B1eVUQgiHfOgvHIIZ2ZewqD4PlDMz1DUGJun%2FfD1FZvU0RxehwnnKa64TJRgTfKChfSUV9uY%2Fvt7Kb255RqmEMbHQAPNobH00ddeNHC2q1xiGfW4XOEFPOuPvYuqyxLpiO1RoUhBvKc%2BhWPnOqNJFR2QicWbVSMuZHAVxXFiMhfxf9l2gcCWst%2FxeVnbo2Hh%2FDeG4xhViruGnyIBcGIZtWZaIZOyQeyDxBv9mpTrkh2XtH6YEV549A5FOB5ye1oUcQB8wagYPa%2BPS3JmYJJ4%2BAJidGc5IRHTqpllOElraKtPK94cyUKsCSYpRcYqZ%2BT5pe3QHVa0OGM81F7RXXFUQXeUG%2FG%2B1bDAJOe7wnPbTDOAnIVOLrZnZn0oLYywTXPKMeIHcMhdfbNvgGyI9FXucF6zV%2F4E4%2B1pLjGEhqFjVTBl%2FaMkZZARm6AXTAkOT0iYaDHBTXLqN9vBYRhK0nPH0c%2Ba4m3kFcYj5vILWfCCaVt5kYCeJ%2BypdbLjmEQICg0ECZ4T4JpOpSavbhqFfcp8GpVxJR1QFC5GiY0PWTPU3v9KZEJk9K84EDazkCyrUv%2BuQRgehF2nUwyS64MJllgPp9RBYRv9VS8MK2ck70GOqUB%2FgKS8VUgSI0B0KvZB%2B%2BAx04X0ZR8tixxRJaeoD42wjZPPWaQENCgg30Z1wvL2rY8aj2y5jEIDhEqNaXrK35mPPaxBTEKRCE0hF5Cpq3HMxx5YKKLgSjYgXEV8j2VRGAEeKymYZPeUv0%2FtKoTDPaw3d0wkKFuNqgRmo2oc1esRfQEoAkGbLHa9UqRyuLwqE8tKWN44Przzghd0kMRf7yh7%2BQM8ZSd&X-Amz-Signature=1c9a8116e95e9a96c439381e447ec23c82d7efe7999673850d0970cd4220369f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RR4WTZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGfat%2BsAEhNUHb4yBe4BONa49E2JvJuk7CM2zE1D1czzAiEAi7Fttq8tJnRW4CMH8gu0KaLmTRkGCX9bqNTRnZvbpnkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJhLFsya1upbebgHxyrcAxIYvRQwZBNnNCrhPnLJftQd3Emuq%2B1eVUQgiHfOgvHIIZ2ZewqD4PlDMz1DUGJun%2FfD1FZvU0RxehwnnKa64TJRgTfKChfSUV9uY%2Fvt7Kb255RqmEMbHQAPNobH00ddeNHC2q1xiGfW4XOEFPOuPvYuqyxLpiO1RoUhBvKc%2BhWPnOqNJFR2QicWbVSMuZHAVxXFiMhfxf9l2gcCWst%2FxeVnbo2Hh%2FDeG4xhViruGnyIBcGIZtWZaIZOyQeyDxBv9mpTrkh2XtH6YEV549A5FOB5ye1oUcQB8wagYPa%2BPS3JmYJJ4%2BAJidGc5IRHTqpllOElraKtPK94cyUKsCSYpRcYqZ%2BT5pe3QHVa0OGM81F7RXXFUQXeUG%2FG%2B1bDAJOe7wnPbTDOAnIVOLrZnZn0oLYywTXPKMeIHcMhdfbNvgGyI9FXucF6zV%2F4E4%2B1pLjGEhqFjVTBl%2FaMkZZARm6AXTAkOT0iYaDHBTXLqN9vBYRhK0nPH0c%2Ba4m3kFcYj5vILWfCCaVt5kYCeJ%2BypdbLjmEQICg0ECZ4T4JpOpSavbhqFfcp8GpVxJR1QFC5GiY0PWTPU3v9KZEJk9K84EDazkCyrUv%2BuQRgehF2nUwyS64MJllgPp9RBYRv9VS8MK2ck70GOqUB%2FgKS8VUgSI0B0KvZB%2B%2BAx04X0ZR8tixxRJaeoD42wjZPPWaQENCgg30Z1wvL2rY8aj2y5jEIDhEqNaXrK35mPPaxBTEKRCE0hF5Cpq3HMxx5YKKLgSjYgXEV8j2VRGAEeKymYZPeUv0%2FtKoTDPaw3d0wkKFuNqgRmo2oc1esRfQEoAkGbLHa9UqRyuLwqE8tKWN44Przzghd0kMRf7yh7%2BQM8ZSd&X-Amz-Signature=d3a4b00c279afd651df20cc5cbcd9a35c938269d6fe76d3c4caf871af46b336d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I2PMTWC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDvhoByKt1PIPAmaaXLAKzabSbNansGYqd7zMyj0cy7hwIhALk9afDeCgOr4trS4tDlRuekf53xM4JI%2F%2BO9Pttd2EkKKv8DCGAQABoMNjM3NDIzMTgzODA1IgzHKnGbJWFMFvc7TOIq3AMZxnIa1cj6D7NC8XKp13KmFtejyRoV%2But9JXaOwDCNI6X3gVD521IP6oDz%2FUvJaQtdI92%2BzdPbFUpRQcqhdBqQjzLH5PRiPjMqmsAlHtpXRkCRLD1Jpf%2FEpcGn8Jni4bk%2BuWNk2RjSX4YkCbqlpzcTaUFXYfmTxalUPFkBqa7X20ZG8moJslrpqnJVJMKxClAcGefLDJ%2BagpFcwYFYwaD2XRV3ghkoS9ZT%2FiuqsLjOuaq5jwTeM%2F%2BTlA5fZjhxe633XtCY6O9%2F42UP%2F3bDkMMn0oDoE2te%2FXZ9OHlZk4JsXMNV9UVpF7yVQ9qvs%2FP2Sl0JewwXchGpvToQMxUpiiV5c1nAlOiWdX6WSQk%2Bm4OuylFpTtz8GRT4Pi0dmy7v6NKMB0F%2FDTm0cLWclHflRVgigJTNSNYRkAwKI0l6SVJE6EMV9wTaEYA0jfVnFvZQ4JKUZyEFB3ZPq7jENcmxbwNq9DwXDC2BpZt2M5CcCVhiGUWBWwxBOTLuzOtp%2FWGRlqFLHKSG9M1zNJWwGwmETcpHpc%2B%2B52skEtQfYnI1hd9PNhtHuJd32oEOEDyz5GaPuNPJXQYVzMzf5UlFBZIbCxvIWNAKbjc0HKPVKosuHF%2FrCqf%2Bzi6ziOZjEL5VDDDGnJO9BjqkAV%2Bbw8zl8wpUCijy9Ig0bPeUtTIyjNWPwsVK4SMX9SZoxsZXyOn69jtD9CcPTJcAwU%2BeuYG1xb23JVw3EgUT8jhPPrtSAf%2FW7XhPAEBcL1%2F5ByDUh04y%2FuFJKnwOzutA9XSEyZxK67ccwuciXzKhpRmxPF3%2FzVBXf%2FovwZhsy%2BTLH8ueOHOweRXEC%2B0M1lyh3Fg%2By5D6%2F21ju90TqcdL1TGuMv4N&X-Amz-Signature=f4574dde1d27301a0d89ae9329c97ea5a53877db08c5ed0844ab250f4efe3f29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T44LMMT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHY%2BoW4hElKkz4uep%2BA%2Fjfhy856mdAtcjQQoexmzCiMXAiBAxfKlRmm6nyfKETZUtgDcZUGOjG9xM%2FdXjs3ZT%2FOKOyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMlrSBLU%2BjABGkPjHlKtwDnW5v0a9O5GeegIUbbXHw0M6rpOOzqRyCe0exaSb874rTg3fCLaJKSFFcORVq1v4fRK5PBndIdB1xAWtcL34pMr5u7ewMd4HcuBVJRjLOBtp4MgNzWC0wGqOocz%2Fe28RUVcBbvhYRoRo9WBB8cNsDmJ8MTL6ANlcKiZMylDEq0%2F4c2caFWDZpQMmdCuUsRfP4zsYRL%2B8iERx4da5hff0tXlh8M5A%2BHoJkRBESpCn0k4JoKMreKu0AmGO%2FaomDUtqd8eSJ9IEigwMfR9aeH3XW02ETOOd8TZoZfoRuobYQUIMNhlZ%2BE9KrcJluwwzdeGFJUkRdsgmdTG4hiOJBLR3dMfh4VHmSLfpMY66vrCye7TYU%2Bqo3XUt4qi6QZaWowhHZufeET%2Fq%2Bgtl4Dy4cVpTWwAuCFiNvwanwH3NuGRjLFu6QmWNVrPNBpZzFWs8J3u3R1Njflpe%2FZ6y44o2Z%2FwlPqr33phv1a3%2FZ44SbFspOQsrMf4STXVfbUHppMHsWW5Vq6xXWepoVu5hyH6TZA%2FNbx%2FX%2FS5niTs3IbspjpY80JPtqs1k6Ov2ip9%2B2IMbXkEp%2Fhqj9VpkQvXdbJajPq5uY2H7Wkrisvo1GBGxJLUlyggN0j0GXm9X7jTp4JqUwmJyTvQY6pgHqcJbOXHk2aPmsaiEEvnwCjKrPEWL0jcxcqjfdxhDoUf0uLCrAe2YtUlPQEwdYQaGyFecZ3b2flLV3MnSo83MUXUkFHjUgqXizK29qEyh%2BAzCeInLe8RWKl7I9CsvB0nFZYF0NwOxTL2DPS8bP7%2BQdpH0vc7M91khUV9MEBZGxReahxlCAZOlg2h%2F8n6Kw60CnSTWoNYIe0XRr5vB7yTTwHslg2XT6&X-Amz-Signature=7c7142beadfc14d3f76d90c8d0b1d939cfcdad6b31a8afbfa10266335b33c39e&X-Amz-SignedHeaders=host&x-id=GetObject)
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