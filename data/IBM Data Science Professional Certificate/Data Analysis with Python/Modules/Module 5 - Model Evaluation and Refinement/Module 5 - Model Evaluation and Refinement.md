

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=1c5500cd3ad708ec36b37f8d53c26f6619fddc75eec4c000101c014978ca2cca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=9a88015e1651da8cff3ae6d16e0afe647076ea79d7c1a03e2c616314fb24bef2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=e25239c6bf95767d1a99f276e0fbe2879954ec3521cf8f5b66673d24ed2aa279&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=3b8633161c6368e33e79c89f39b73cfed26729ba27e7ed3161bd0689bec294b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=96bbe13773fdcec2f1c9f14513a1f6905191caa0b31708a61d283963a4b6db5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=a6c0e6aa94a2d6b8e8f7364781d68708a596d6c1bdb9ac4d40c94c57bfc77fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=ea96d0a4c35b9ce5d12b716ceb965178fd4885a1499ca1b407cb045048b11e6b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=172ce66de8f6f267bf37f903446c1456b947a65eb3d33d065a9f060e3ceb3d90&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=c962270389051b824571d9ddda4b7b18d194378229674bb1775553c2de635e42&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3DNMWGK%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCGe5wgRMZ2t2owPVg66hy7A5L0KkRUcqeGpBGhSx8DhgIhAMFTkz4dQdGyNMaceBLHqs6tpNOzyrVIzdaKilT3hMeOKv8DCFIQABoMNjM3NDIzMTgzODA1Igyjq8FgXcHziv6vb%2FAq3AOwoECHUZ79O89CtWGscQo21aGDPX9%2BbefPFLphNoDdilLJ1kamwZdzs6WC53JfcXafIWnF88hLIrswK5QnrwzVYiENIBEpP%2FQNC1si0%2BadKJ3FSNk1qmDmn5HGFG8Ywh4QNu99nrVKaHhNlOpTxwQzSz7sDGWDQiRjEFmjxZcccveW8P1w6GGPjCgTZHpjp5atY5XI%2F3SrvQSXBxPhd%2BY5fk52cfDMVczFXiM1m%2FP3w5vOPHPeJrjgmjRyeH1vwmzHlVNCnMVEoyipR7y8BFI4lhr8fuuCVplrPoPWDqcNS0GOQXZTP8NmTgnnm2l7rpCdZ2AiDu1Y4nib6TiExm4xmELXwCthgTgGyrHDFSI0MtFeiiRJ0J2o4HVJEJ5uNC4gUsqV%2F9Zx0mwqjhr5%2FKUJoQiGa%2B4oiLL7a6%2FTjVQVIPLdr5ch8G0qjbjSssrV%2FZJNvoYvo1PjKQ4LZdaM56GaD5FgbyRcOj3coqGJrzKoTw6l1lgtZSZUUzRWKN8%2FjZgRsKjd8R%2B2k1aKQca3dYcAWsBCgsKfxDWQd44yjmVyqucQxEW5W%2F6W5wvCxROCIDItbIAfqnnujRFnHBqYpr1VpG7AwAv%2FlWVIfnyW8GqtyGDmHiflG3NDTtgNgTDp5MS9BjqkAb4KBp3lA7v5ZPs1go4OeXGG5HUi76kItnZS59%2BTWmXKWai95E%2FTBNaaHd4vjOF1Bjz9QCNQJyvYHvbw1fzc57bBc1uGZ%2BP%2F8c7NWOM4TxKK5qD%2BJATAxb7mjVxzsSRKs5kFrqNIWtQkzt%2B%2FLepOZWbQtlJ59MAHHIPrS6sOFDE82LIP%2FbY2H8UenVKpj1Agz6PhW%2F03VX1vWENvyPkVBG8c6%2BSy&X-Amz-Signature=a628fbd340a77da10d9cd7cc7bf65c2d31a451796b9b0f34cc9f370d350dea9b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3DNMWGK%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCGe5wgRMZ2t2owPVg66hy7A5L0KkRUcqeGpBGhSx8DhgIhAMFTkz4dQdGyNMaceBLHqs6tpNOzyrVIzdaKilT3hMeOKv8DCFIQABoMNjM3NDIzMTgzODA1Igyjq8FgXcHziv6vb%2FAq3AOwoECHUZ79O89CtWGscQo21aGDPX9%2BbefPFLphNoDdilLJ1kamwZdzs6WC53JfcXafIWnF88hLIrswK5QnrwzVYiENIBEpP%2FQNC1si0%2BadKJ3FSNk1qmDmn5HGFG8Ywh4QNu99nrVKaHhNlOpTxwQzSz7sDGWDQiRjEFmjxZcccveW8P1w6GGPjCgTZHpjp5atY5XI%2F3SrvQSXBxPhd%2BY5fk52cfDMVczFXiM1m%2FP3w5vOPHPeJrjgmjRyeH1vwmzHlVNCnMVEoyipR7y8BFI4lhr8fuuCVplrPoPWDqcNS0GOQXZTP8NmTgnnm2l7rpCdZ2AiDu1Y4nib6TiExm4xmELXwCthgTgGyrHDFSI0MtFeiiRJ0J2o4HVJEJ5uNC4gUsqV%2F9Zx0mwqjhr5%2FKUJoQiGa%2B4oiLL7a6%2FTjVQVIPLdr5ch8G0qjbjSssrV%2FZJNvoYvo1PjKQ4LZdaM56GaD5FgbyRcOj3coqGJrzKoTw6l1lgtZSZUUzRWKN8%2FjZgRsKjd8R%2B2k1aKQca3dYcAWsBCgsKfxDWQd44yjmVyqucQxEW5W%2F6W5wvCxROCIDItbIAfqnnujRFnHBqYpr1VpG7AwAv%2FlWVIfnyW8GqtyGDmHiflG3NDTtgNgTDp5MS9BjqkAb4KBp3lA7v5ZPs1go4OeXGG5HUi76kItnZS59%2BTWmXKWai95E%2FTBNaaHd4vjOF1Bjz9QCNQJyvYHvbw1fzc57bBc1uGZ%2BP%2F8c7NWOM4TxKK5qD%2BJATAxb7mjVxzsSRKs5kFrqNIWtQkzt%2B%2FLepOZWbQtlJ59MAHHIPrS6sOFDE82LIP%2FbY2H8UenVKpj1Agz6PhW%2F03VX1vWENvyPkVBG8c6%2BSy&X-Amz-Signature=65184ce6dc62b99b8fde3b59aeeb6e77a47beb6d9095fd7919c7691fa87fbc5a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3DNMWGK%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCGe5wgRMZ2t2owPVg66hy7A5L0KkRUcqeGpBGhSx8DhgIhAMFTkz4dQdGyNMaceBLHqs6tpNOzyrVIzdaKilT3hMeOKv8DCFIQABoMNjM3NDIzMTgzODA1Igyjq8FgXcHziv6vb%2FAq3AOwoECHUZ79O89CtWGscQo21aGDPX9%2BbefPFLphNoDdilLJ1kamwZdzs6WC53JfcXafIWnF88hLIrswK5QnrwzVYiENIBEpP%2FQNC1si0%2BadKJ3FSNk1qmDmn5HGFG8Ywh4QNu99nrVKaHhNlOpTxwQzSz7sDGWDQiRjEFmjxZcccveW8P1w6GGPjCgTZHpjp5atY5XI%2F3SrvQSXBxPhd%2BY5fk52cfDMVczFXiM1m%2FP3w5vOPHPeJrjgmjRyeH1vwmzHlVNCnMVEoyipR7y8BFI4lhr8fuuCVplrPoPWDqcNS0GOQXZTP8NmTgnnm2l7rpCdZ2AiDu1Y4nib6TiExm4xmELXwCthgTgGyrHDFSI0MtFeiiRJ0J2o4HVJEJ5uNC4gUsqV%2F9Zx0mwqjhr5%2FKUJoQiGa%2B4oiLL7a6%2FTjVQVIPLdr5ch8G0qjbjSssrV%2FZJNvoYvo1PjKQ4LZdaM56GaD5FgbyRcOj3coqGJrzKoTw6l1lgtZSZUUzRWKN8%2FjZgRsKjd8R%2B2k1aKQca3dYcAWsBCgsKfxDWQd44yjmVyqucQxEW5W%2F6W5wvCxROCIDItbIAfqnnujRFnHBqYpr1VpG7AwAv%2FlWVIfnyW8GqtyGDmHiflG3NDTtgNgTDp5MS9BjqkAb4KBp3lA7v5ZPs1go4OeXGG5HUi76kItnZS59%2BTWmXKWai95E%2FTBNaaHd4vjOF1Bjz9QCNQJyvYHvbw1fzc57bBc1uGZ%2BP%2F8c7NWOM4TxKK5qD%2BJATAxb7mjVxzsSRKs5kFrqNIWtQkzt%2B%2FLepOZWbQtlJ59MAHHIPrS6sOFDE82LIP%2FbY2H8UenVKpj1Agz6PhW%2F03VX1vWENvyPkVBG8c6%2BSy&X-Amz-Signature=9a45f5d8800de6aea17a127447aaa09182ecd25f8e0951aa4083694d803369a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=d09f2e5f3a674f320573d0a79e37846335d89296f210b3096e1622bfda2eadcc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=9878e9a0127e7f6beaca64454e7fb1b404081ef906e8771deff1e9e8d243f5c6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=29de27c6fa281bced575bd1f0415cf4d7c88e8509688c6b8da3cd4e17ca1487c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=b6da5bd57bd7bdfb93f402501484cee15340cfbc76395bf124f341cf138fd761&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=9eebd16611cea59125cfc8f39e15a7d7abe96cf5380bee389653b9e0a08aae08&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RUDDAJ5%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDiAkUgThmSP27Zy%2BoqGH2D4p1dEthlFdima0dwIogs%2BwIgU8XEoIPLMiXwCnYpyA%2BCI8K4DZpdX3XJKxWquHYsNicq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDHmvAFfvEDym8i%2FZyircA5mfH5laVVOkQtVWNC7o5VknzMcqeZi%2BECLOPobq%2FB7klqxMqEA%2FM55WtkYhxOvgZR7My6vyWbvfsCD2EcJE9hGb%2BePcRPSS2ZAnvAVHRSD9NC5ngGowb8ZWYCWcT%2BZPNmech1qvwjJLP1x3dj5n7lrLQi7ojq0neiN15ZtfsOCgrNwwoGedZJB6LC6Nis7hFAc1%2FE9JjAW%2BvWf4F3Gknrph4eNsg6u1WGshWIxab55lQNvu7uIi7ISHX6onn6XQU1nzHGS8AjEJXSzbxhQbb69eqfalab0MvX2e5c%2F4hibO7FRMHhjoQVigfgj%2Bvnfg216tjo9nm%2FwcHiB2xywqVZvqm0Nj3JOlbT4Xaf7QmCSIMa3LEdAnePm4yZqrWiKjF7R%2ByhW9yyfhUrH%2FwO25njp%2FioS0hvunRCTt%2BmbobBKevwUAolcxJz%2F1z9Vo4S3UxgiB51eXxbNHExtKp%2FN2kmnCqa0cUJR8T9Tr0MXgXXmHqh4O5TFYQ6ougrCVt3YGe%2FGcOVHs2YUpm%2Bh9m8sBmfy1vhKJENwXalNj6Og3mZ8a6AStnBX2uvUpPyzFS03%2Biw%2F5QENYttNRad2FjZZ53rH3iRNLpS2O17s7GIWxuoXMO4xVpoJAhdRcPUJtMPfkxL0GOqUBmuyyCcD6l1UUmJ0p2Hq4yMl%2FX4Wz3CsippW5JA32rADLgmKVIsreJ1z%2BTBHAVLhSprRAuVXj5qZ5bjs7B%2BjXmxrdQ2vtp%2BHKyqUdVVKRDrmXu5sTgiwa%2BiDejlhYOPaYE2Vq6G%2BXqgPKeKxaB5BHmQA%2Bd41LTakDdq7Rv0EWa9mt1EzD%2FTS534bHJhspS1AH3EP4hLkxlAS9w4GRIiNmHAn%2BDPWT&X-Amz-Signature=38972e5825b010db6b80b1650ac450b27d2252bdeee18ec02228cc01e9470716&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVOJDYZX%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG0tCwmfaOtPA98qDsNc2QohEjyQu2%2BELKuG6LIDPQ65AiEAiebC5bpvu7ZkAKgcssxXwM2qa0PRm%2BmtCyGOEHTStbwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDClLYpXNZByi5Qbr0ircA2PglcnHwI8MPPamPJsRwbedKx0rcERMTJ38j0qNnO8Kb5Jqo0M6lEPaiChnmCaE%2BXhF4tDSE%2FMEMSaXk9RTf7JJ8WqdbujjlAX38jn0fcyZm7ykNyLHNbtoHOeNGSP8YFGWMLrURWMEKeRTl8cf1hxXF0QrgsOOPpDDn%2FFRIaNCN%2BW1jX%2FpMInruvstHuIs4KDPWoca5%2Fq780wVBZoLq0Z01oa7hzzQHdzVrql6JaWRqqSHg9mVDFSjgC0KOaRTGsMYmFXfNUBI7TZ5cVg2do8cEfvS26EF01eTBd5YsUmmHhDMIqZxl%2B5WvEAbi6ck5GmUm1vz%2ByfDdSVpjuDK%2Fslk9EFrFy4G2EqoJEsXs5RinybpoBUXGA7BUKQ49VVE3%2BfAKO9uEBsyC7ZlKQVsr0mkT%2F28s%2BY5FznXxKMhEHEBdHh%2FmxwDr4psXhE44c6RriZ169iy4zIaSGJELixK1X9r5bmLDpq8TXbZx%2BfBvz8fVxYABTRz66DOf%2BgCOaKXxGX%2FsUwqONpOUWIpjimdkc0Ke6D0ArITqKzNOt8u9K2ff1yOEMfo6yh2qq82dDY2bGSA4DmcymfHMH97C8SGSeqGMYOlVJYPW34YhDLNKvJ0ae3Q7bXc8055NMI3MM7kxL0GOqUBahA6O0SoL7U8KIMXh24TjjJLvihohim06ktulloWgNHXPNAZaQAzpaCdooS9ZvQvbuqriWhfUQloNEIBOdkFI6GTEB8MOaqiuM3Gqrf%2Bep5J96132OuArnUeSpwYIySyMxmn%2BuPaaA2QrnqZV988XjRci2U9hDffJLYd4h2NUyIGi04LKceotIkRmgckq5rShqOpd3a34qopiVv6Y2WAug69H2ff&X-Amz-Signature=f0792d8823cd19b28674ab9ef84a25d4b2b0d933052f3eced506152ebcf6c427&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVOJDYZX%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIG0tCwmfaOtPA98qDsNc2QohEjyQu2%2BELKuG6LIDPQ65AiEAiebC5bpvu7ZkAKgcssxXwM2qa0PRm%2BmtCyGOEHTStbwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDClLYpXNZByi5Qbr0ircA2PglcnHwI8MPPamPJsRwbedKx0rcERMTJ38j0qNnO8Kb5Jqo0M6lEPaiChnmCaE%2BXhF4tDSE%2FMEMSaXk9RTf7JJ8WqdbujjlAX38jn0fcyZm7ykNyLHNbtoHOeNGSP8YFGWMLrURWMEKeRTl8cf1hxXF0QrgsOOPpDDn%2FFRIaNCN%2BW1jX%2FpMInruvstHuIs4KDPWoca5%2Fq780wVBZoLq0Z01oa7hzzQHdzVrql6JaWRqqSHg9mVDFSjgC0KOaRTGsMYmFXfNUBI7TZ5cVg2do8cEfvS26EF01eTBd5YsUmmHhDMIqZxl%2B5WvEAbi6ck5GmUm1vz%2ByfDdSVpjuDK%2Fslk9EFrFy4G2EqoJEsXs5RinybpoBUXGA7BUKQ49VVE3%2BfAKO9uEBsyC7ZlKQVsr0mkT%2F28s%2BY5FznXxKMhEHEBdHh%2FmxwDr4psXhE44c6RriZ169iy4zIaSGJELixK1X9r5bmLDpq8TXbZx%2BfBvz8fVxYABTRz66DOf%2BgCOaKXxGX%2FsUwqONpOUWIpjimdkc0Ke6D0ArITqKzNOt8u9K2ff1yOEMfo6yh2qq82dDY2bGSA4DmcymfHMH97C8SGSeqGMYOlVJYPW34YhDLNKvJ0ae3Q7bXc8055NMI3MM7kxL0GOqUBahA6O0SoL7U8KIMXh24TjjJLvihohim06ktulloWgNHXPNAZaQAzpaCdooS9ZvQvbuqriWhfUQloNEIBOdkFI6GTEB8MOaqiuM3Gqrf%2Bep5J96132OuArnUeSpwYIySyMxmn%2BuPaaA2QrnqZV988XjRci2U9hDffJLYd4h2NUyIGi04LKceotIkRmgckq5rShqOpd3a34qopiVv6Y2WAug69H2ff&X-Amz-Signature=577ebfc40a820c5904381ed21600c10af8de882d4ef56dc5deb2c46b257e17c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3QUQTZ5%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDa2yv7sBWNspG8EhWSH9fSB1aXAFEzksaxTf79nw%2B9%2BgIgL%2F7F2fkHzec1JWGVx%2Bo9tznMykELFMZoqs2jS1Ymuccq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDCIJQd4kJ4xffpslwSrcA3jJvmu2yy2rJhZLO%2BQpPM1Fo97p%2FCf79xcqrP37w3n5tcow3pwQFT4VFzy5q5ahzSvBWEiTVGJsRXHTH8nRQiexuCaJAr7PRbBMrxiSj2ax4ITH5w%2F5zx1IQ2sA5sVHiAWM1H5YKl3cwaN2vOK4Dj%2BDeEUUQ6aPRB2heKFlLLSAW3imROFN0qcawpAUUm4FuZOHqA9RVvIT5lJstDFLaum4ERH8SG2dWA7XX2njgJncCp6C0fv7Yzt3%2BCzYdqI0Tk5nh5fuEquLfCC6dchRX1nuHd5iWrQLO0zjbph9qNiqDl%2F8z0FRqjAPNJ3ZClChyNGd6%2B3iZfi9KzOHWgtB791GfORPebOw4NV4Acn1HrjH2SLTCReFeW6tHfgyx09k%2BjAZ93F3N%2FRMHn5fva5d3iz4knnwHQFBik4BZJbPYloYcT43RyzHJwsyJCT5nNXicwoC0Niavy1vfymsRlS8TYoYokYVXpWs5M%2BkQsSFrCpfDKUhEfjw755UXV%2BsBjbiP7924n%2FC6lzoxNxfxRkkYg04xo23u2wBAGo9UX2V%2BsYdxzMncM059fO0CSaj8rh0%2BSXno%2B2nYRoDjk0iNLrnxv6bcN1UXkYcZPllF0tL0rjv7KAGfKEYr6tvm9GLMPjlxL0GOqUBOVfH86FDCTem233Xq0UX1ebpVf95yjHsMYPy4%2Fbgz1TpGbtxSRffGRFYWi3nYxE41JW3Tgs%2BptF7oGN15iR%2Bknf6rxjvMrzTG4Uepnrrq9LJc%2F4PMQ1U7Q4%2BhA%2FNHOfp0vq5eYUABMKobJakobPea3cbfLv4eL%2FrhXYo5EeJNfdo2tc567Y33QfOIIF%2Bo307JfyNynCmGWSkYT7EK6nrSzbWqaVZ&X-Amz-Signature=5c00a5b1068b35a79d0957d9d57ad62936092f20feac1a4283895d4ffc593d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADY7LGH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZW6WzTSUDnnYvM3WJi4QTgKBJqRwed3i30qgXHdUNlgIgOF0wC%2BKTl3hQa0YxHizDf3r4hQsafUTvShTnemD3CN8q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJ9P4%2Bcby0fjxk2x9yrcA3V7k4pD3P8gFyP7qshjTtrjMJBcCn1dNVaLjn2pjKY%2Bt%2B0Boc6i2GKEdsXF6mp%2FM3ychWuNY%2B9ue5BTFInUJ1TNo%2B40KfTBICOZG%2FqXmU%2FaXvjJrOSDHQbsHhQgdRdE%2BxjHsYiMpB6rT5j0Mc%2BvQciVIc5HQkcyb0lcwTpS%2F6r48GBgYgRVlnKDnuG%2BQAD7KrgyYQiEkAkyfV7eLXpmqpH8jA10CZN7e1JASC38MTOGG7WPC9J3%2BTW5edBtEt19ihbxRrtUCjXnBX4byVFPY2aXGCFngb7d7vjCNoqaBeFW0HEt3PimIyP%2BBeWQfEoBgyr%2Bd9NU0xCzqUPj62h5vLRbCZB8uZiEyy2wlQV4vfFpSFylbNXpAeHE45C0MtNWQ23jW3vQ62Jbg1QiIEBVjwuVI%2BrG1rcfCyMYhXoIJsD7CS8%2FVF7E5TPi7QULPBOpYdOIZAZGnEOZyrtA9fG2Ok359CmPtv%2Fadoo0R3oTokDToQsRmX6%2BTua%2B0jf6MuIgYYJ4AqNwILkiV8jzx1%2BBWymwCS%2Br1hZ118qDj0By42SpSVDUB4qEEoxImRKwcSVoDusKva1LyGniLnK832kobVAp08Q3FExMJWfqQ%2F1945Tia6TPuFoV53MyucfFMPnkxL0GOqUBh5gZxaKrCwFYaxYX32ZvZqpvSuUiIxHPgBEKgtjv5cATlYbWGM4Pb7oiEirJV91Dq21oUj9wDCUDffCl8UPvhrezshDjqUe3WBQlUHLDBNFCQAUALtNHqFkWYR%2BrIVv5qZNldaZaI9EUlrGI9y0yateOGnq31vBfXK35UqT3GCXtkW6stoEkhAWzQk%2FV9ao2bJt0W9s9XY%2B6hzi2OSKBavDJxyEV&X-Amz-Signature=656134d308303ac76ba23eb61195c65b8c7df643411e34ae3432b14110448057&X-Amz-SignedHeaders=host&x-id=GetObject)
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