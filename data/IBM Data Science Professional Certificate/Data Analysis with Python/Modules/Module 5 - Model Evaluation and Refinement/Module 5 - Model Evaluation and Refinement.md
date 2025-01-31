

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=ad6c162ff2befa6217a7e4f39bac2779aeb45b299e7e9def5255e481dd3160d8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=8b7e162d1375d2229fe8680c3f33a70a183eb19c9a0cb1441b738ce90033c03b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=d7f4eb73100a12372bf4057535c0372af3ed290b25a25cc23b9d62bcee0d17d5&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=ee6aeff2c9dbf47a4886a0a63ed6419f22d0bd0bf1aa1868bf5281bad8041042&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=3ed4104f900097201072c184c506ef56ed2f04fe6725183e021151a44396a295&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=403487dfacbb9dc1f6c875ce2c11d8a3431d2ab05d6db10ebae5a53b7e4feccd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=cf787b18e2590fc9cf23322038bc2e8c36a823bb7d3f754a531e6b44ed4c2e2e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=54cd4c313fff5313bef4e05c50a8a8d2ce749fb797845d75dc1a7f7be1e7028d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=d8d730740c4c7d15b3301c0d27cb5807c85e2ba9c4ba4f19f836fffda5f81683&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T5H34EL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEFgE%2FKi5%2BNQ7CXpUHwBxG80R88L%2BcUFM9Wb2UjZrVqAAiAzhLzPL1lTEsTlxoE6OHfF2tyZ8%2BN4G1rFdRGuvmaH0iqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FKe60SmVKLqguVaKtwDbbfvagqOJbplDJnGGoSyPjnjyw6gPRhQydeyaGGVTZ4ogGHBvEfb3bptVO3KnQy%2BjSh%2B7fXyl%2Bz4YDReuyVl5tVo8gWv8tXN9XWbem8B0VXjCyRfiI%2BK8B8rQeoSW4OAlARRv2WVrLRTqEpdAOImfgVeLYNi11D0%2Fv%2BLb8z4GWbrcGM5jSj3%2FsJK60mnt8rrrbOGPla72iO%2BfQf8sXWJAkef2k79Qp2MZ34IjR98Db17re87jrV9%2FsErERfTLy0ZZWgF%2FkV6%2BJAP9%2FwwrQfX0kFo5Iff4aspFaIBRe4OHxQsBIV4Rbn%2BAf%2BPlnHr5qmTc0mwnw3TtyaOgZu47QAL5XB099O9Rh0uf99xGpiTDtZNTfSWlApMYU9Rx5HuMOn52wILUslHsLkdYokN9Ux8CFl3Sb6RkOTso5knynN6yuAewExYFfOj0AylYlPZcLVPNTuMn3a2oTdXLRXniC%2F5OtcVfO%2BFHKwc62j7vRnQ5vqTIb9c3B%2B4SPV0Ve3sJVCm5fUehZDbZ0W07eaQAra6fNo%2FWEr06YqlQcPmgfriYOFQrwTUg6qm96G6Sg%2FlNJ2SletvX%2B%2B7VBpcb5vZMFFon1mkD%2BrddFC0WbpoJhV0yRnG3%2FiTKYKycf33ft0wlqT0vAY6pgFNCetwtNGhBWkN3imx2%2FtY%2FFz1mkU5i9blR01w1Goxxq88i2VEPMSA4sWgT6ttdWJQL4j5joPQ4dVvTtMZSRRjtRAAIODxFvdF1d4lBYJzPwuiH2AZBpxF%2B4O%2Fw74TwCNftGrCeeGJFZZZfQgj8haRzBUUfNJewEmc%2BvEwfKZQCB%2FNpx1lUqx36o4u19KKh%2Bw0EVYyhe1FFChSdgVCx8%2B254fJT6t%2F&X-Amz-Signature=db519bc4f0f83f8d7851bcbae8668e035cff3cb01c497e406d64dd6726ac7e09&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T5H34EL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEFgE%2FKi5%2BNQ7CXpUHwBxG80R88L%2BcUFM9Wb2UjZrVqAAiAzhLzPL1lTEsTlxoE6OHfF2tyZ8%2BN4G1rFdRGuvmaH0iqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FKe60SmVKLqguVaKtwDbbfvagqOJbplDJnGGoSyPjnjyw6gPRhQydeyaGGVTZ4ogGHBvEfb3bptVO3KnQy%2BjSh%2B7fXyl%2Bz4YDReuyVl5tVo8gWv8tXN9XWbem8B0VXjCyRfiI%2BK8B8rQeoSW4OAlARRv2WVrLRTqEpdAOImfgVeLYNi11D0%2Fv%2BLb8z4GWbrcGM5jSj3%2FsJK60mnt8rrrbOGPla72iO%2BfQf8sXWJAkef2k79Qp2MZ34IjR98Db17re87jrV9%2FsErERfTLy0ZZWgF%2FkV6%2BJAP9%2FwwrQfX0kFo5Iff4aspFaIBRe4OHxQsBIV4Rbn%2BAf%2BPlnHr5qmTc0mwnw3TtyaOgZu47QAL5XB099O9Rh0uf99xGpiTDtZNTfSWlApMYU9Rx5HuMOn52wILUslHsLkdYokN9Ux8CFl3Sb6RkOTso5knynN6yuAewExYFfOj0AylYlPZcLVPNTuMn3a2oTdXLRXniC%2F5OtcVfO%2BFHKwc62j7vRnQ5vqTIb9c3B%2B4SPV0Ve3sJVCm5fUehZDbZ0W07eaQAra6fNo%2FWEr06YqlQcPmgfriYOFQrwTUg6qm96G6Sg%2FlNJ2SletvX%2B%2B7VBpcb5vZMFFon1mkD%2BrddFC0WbpoJhV0yRnG3%2FiTKYKycf33ft0wlqT0vAY6pgFNCetwtNGhBWkN3imx2%2FtY%2FFz1mkU5i9blR01w1Goxxq88i2VEPMSA4sWgT6ttdWJQL4j5joPQ4dVvTtMZSRRjtRAAIODxFvdF1d4lBYJzPwuiH2AZBpxF%2B4O%2Fw74TwCNftGrCeeGJFZZZfQgj8haRzBUUfNJewEmc%2BvEwfKZQCB%2FNpx1lUqx36o4u19KKh%2Bw0EVYyhe1FFChSdgVCx8%2B254fJT6t%2F&X-Amz-Signature=b9c8ff1b712557474a5e0b354615a7a91c93f4d696bed4bf0cb8906358e2039e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T5H34EL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEFgE%2FKi5%2BNQ7CXpUHwBxG80R88L%2BcUFM9Wb2UjZrVqAAiAzhLzPL1lTEsTlxoE6OHfF2tyZ8%2BN4G1rFdRGuvmaH0iqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FKe60SmVKLqguVaKtwDbbfvagqOJbplDJnGGoSyPjnjyw6gPRhQydeyaGGVTZ4ogGHBvEfb3bptVO3KnQy%2BjSh%2B7fXyl%2Bz4YDReuyVl5tVo8gWv8tXN9XWbem8B0VXjCyRfiI%2BK8B8rQeoSW4OAlARRv2WVrLRTqEpdAOImfgVeLYNi11D0%2Fv%2BLb8z4GWbrcGM5jSj3%2FsJK60mnt8rrrbOGPla72iO%2BfQf8sXWJAkef2k79Qp2MZ34IjR98Db17re87jrV9%2FsErERfTLy0ZZWgF%2FkV6%2BJAP9%2FwwrQfX0kFo5Iff4aspFaIBRe4OHxQsBIV4Rbn%2BAf%2BPlnHr5qmTc0mwnw3TtyaOgZu47QAL5XB099O9Rh0uf99xGpiTDtZNTfSWlApMYU9Rx5HuMOn52wILUslHsLkdYokN9Ux8CFl3Sb6RkOTso5knynN6yuAewExYFfOj0AylYlPZcLVPNTuMn3a2oTdXLRXniC%2F5OtcVfO%2BFHKwc62j7vRnQ5vqTIb9c3B%2B4SPV0Ve3sJVCm5fUehZDbZ0W07eaQAra6fNo%2FWEr06YqlQcPmgfriYOFQrwTUg6qm96G6Sg%2FlNJ2SletvX%2B%2B7VBpcb5vZMFFon1mkD%2BrddFC0WbpoJhV0yRnG3%2FiTKYKycf33ft0wlqT0vAY6pgFNCetwtNGhBWkN3imx2%2FtY%2FFz1mkU5i9blR01w1Goxxq88i2VEPMSA4sWgT6ttdWJQL4j5joPQ4dVvTtMZSRRjtRAAIODxFvdF1d4lBYJzPwuiH2AZBpxF%2B4O%2Fw74TwCNftGrCeeGJFZZZfQgj8haRzBUUfNJewEmc%2BvEwfKZQCB%2FNpx1lUqx36o4u19KKh%2Bw0EVYyhe1FFChSdgVCx8%2B254fJT6t%2F&X-Amz-Signature=0f62e7484662456bb7f8e2f9a350c519865da12e53f3b989be33dc4b73ff730e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=1fb13663a1ff5bf7c2d3ec559bf9ad5fc58abab13bf4833a3a05c9a02d1c6a74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=1eefc2d08154e18b1c52ca723d243fdc741d2026e6bd425ba7672c82346ec18f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=9638b3d4f560878e8db3f222c24fa8ca0f9b964a6d1b0dbfa2d2c4cd06667a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=7ed89d173b11449f016c7fede6b65867b7c3036673e955a61ab91c2081929018&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=8dc7c2448145899fb22adb4923217b2fa11285214eb8e3e24a496419198d90e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVQQ2EAC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBAdu2YmO3wOQeIFrBloK7lLnq0WarkpwY3WDLqmUglAiBVUqpWeqeTRYDwi4mXPaxtlKuBMObL0W76bGeJcHMe8iqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrMoxjmR%2BOX3ZtBJOKtwDe2c%2FrcGIIJ9cDRc9yeZjeXf8i0Rr1Ybt0Ya84%2FQ77VB3%2FQgJ9se0Lj6oCLeAqQfX8OagjpOXg330l7cR3WnrNbLtEDqgy0ARXUmNe5bvTKoeue6zIgnVxI0KKi2CjzbTVyB6iCBmvmp%2FCnByF8ibX48OUrHc73s2tjK5%2BhBuwos4NfDSq8cV8BC1gnMSif6d1MW%2Bbg0pTITXEEkbkyzYQzUIXleJeC42zj3Cc7DVleilZVLE8d%2FwVU%2FQnwE5KQa6lQEe3dM6UvMerGaUblZBDbccLlY6RIZ8r0qiwYvK9Z3V3wIKkCuK1zfYxZvFhvdXLyjGbKHYDVlvm%2BhdxejtXxG8ykze614kHe9gnr8WO1Ake88lmu%2FOun380eaeMGVRaVtZTnQGsWqvq%2FVVYPr8hn06SAVCcsagQoLkbXyBA8oOPirkq5Z6VgB7Z4hlHKoO5oqvNo78ATMROv2yMmgYUxZ%2FXSl4fG1rm8Lm3ZFLXPs%2FWn0GS%2F0HOS1LG8PA%2FNWVeu03l49nKui%2BL0HSLvYH6FkkTw%2B0QsiC%2FYGa%2BjendfSk%2BbqeVz1CFmRes2H4InovfGBL8GNViMT%2BHXOSlH3CIs%2F7S%2B2o%2FIHK0CgwvvzRL2Rnjpa80zGEpL4MEG4wyaP0vAY6pgF99rQQtb3I3r%2FQyoSxJpCronl2jcMOQjkkLun7xHRq6vmXPsiKGDcJRExo6OTzBorfPbrPv5knKZ1UlM0AD%2BDwtwdSbMLE899eNhUJcBs5r4G12fX3Piz4xGYMfeM6Uue2Ccv9HTZ7rQGkRi0swyqPUJav%2Bt4KWksbawZJHgChjo4zEKZew8QODLjPfWWBf37ItIE19NsGpVjpS7UfGTwWyreJy40A&X-Amz-Signature=05ebdbb8146be7c17f19e8b58957c65e07ad8211eaebd00fb4f122b768be904d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TLGWXCY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDUgvuU7I7mjrC2QyvokuqMGpoHAoD7BC2QpXZizEYETAiAijxZ9cyj16a%2BFQ%2Fu4vkjRvyAojARRaCjSgwqz%2FqUUYSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5WuuRDOexzHgPPiTKtwDSQp1jr2u9YXXxYqELaAEQM71Jq%2BgOqL%2F93sYmENKLtck%2Fij44hm7zBVwwe%2BofKtPJjcxO24%2BUc7jfr49sx5LgFmXbFTi1Q4T28jQ%2FLhTrcMLOvWH7m1d8UHr26uV3Kk9i52BEcb2XD%2BP3hKWVaT1yxKXZJp0N2Ys9O3zbz82VVZTxuwHg3fob7weo866o%2FNY0w%2BEAFZ5bmaTgzyYWirGQKIbM7UJdL5VfNt8Qv%2B0eqbXRvcTgDJ2TYC0gMwfBKqNVWu0gESkcCVnJX6I0RnT9qbGVRjvd0AoMd1LCFHRDwdV5q4x5jDRRoLRovaL5G8B1xqLreJLFOZvKn6QAzdl2rAg4w5WQI05keEyoJG5qh%2Fgtp4YXZOJHW75LI8EAROnyFkaEk8EZgYI8G8wJ6K5eVGRG9UIHGutrjUZJrUxTaX7ewyOyiMfjBJtDbTQmG4AM3sGozV9ZdjPsV5G2Kfy3ByRivxTLtSJuaXl0sMBSg9UYY2P3UK2DPvzFLOPHL14sy02oUO5pDhEExbW2SbsPweOEH%2BoQ3OXD8Yecp%2FWjL4ANuA0cwh04iwHwbtl5wHXCN4D2gUV5CkGTarbjNT7aIIIiuX3uSefI19HhzhP3oEEMFUBT5BYm%2BzLVMowqqT0vAY6pgF1UAsU%2FjmFtn2%2Bo8w2TfIHpMrK91l%2BBMt5GrWVqaHIPHmVMJEKN%2BK%2FgYAjqQSIHqfVpfytLlNQCMQrksjN6UzH50H0LsHlllWMeKB4mHRI1BVGF0ZUD7UuiJHxZKDZFpNlEN3I3cja6Qcgy1fvA5vE3cBRQE1IwMFvL9q2DSAF0vhEzamdFNuR4GFWbbj1eRYm4FBgLWio8MZQt79WPYU%2F2%2F87mtkN&X-Amz-Signature=61582bcfeab718374f83478b713951c288c0cffa97e8bf9020c3191152974c75&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TLGWXCY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDUgvuU7I7mjrC2QyvokuqMGpoHAoD7BC2QpXZizEYETAiAijxZ9cyj16a%2BFQ%2Fu4vkjRvyAojARRaCjSgwqz%2FqUUYSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5WuuRDOexzHgPPiTKtwDSQp1jr2u9YXXxYqELaAEQM71Jq%2BgOqL%2F93sYmENKLtck%2Fij44hm7zBVwwe%2BofKtPJjcxO24%2BUc7jfr49sx5LgFmXbFTi1Q4T28jQ%2FLhTrcMLOvWH7m1d8UHr26uV3Kk9i52BEcb2XD%2BP3hKWVaT1yxKXZJp0N2Ys9O3zbz82VVZTxuwHg3fob7weo866o%2FNY0w%2BEAFZ5bmaTgzyYWirGQKIbM7UJdL5VfNt8Qv%2B0eqbXRvcTgDJ2TYC0gMwfBKqNVWu0gESkcCVnJX6I0RnT9qbGVRjvd0AoMd1LCFHRDwdV5q4x5jDRRoLRovaL5G8B1xqLreJLFOZvKn6QAzdl2rAg4w5WQI05keEyoJG5qh%2Fgtp4YXZOJHW75LI8EAROnyFkaEk8EZgYI8G8wJ6K5eVGRG9UIHGutrjUZJrUxTaX7ewyOyiMfjBJtDbTQmG4AM3sGozV9ZdjPsV5G2Kfy3ByRivxTLtSJuaXl0sMBSg9UYY2P3UK2DPvzFLOPHL14sy02oUO5pDhEExbW2SbsPweOEH%2BoQ3OXD8Yecp%2FWjL4ANuA0cwh04iwHwbtl5wHXCN4D2gUV5CkGTarbjNT7aIIIiuX3uSefI19HhzhP3oEEMFUBT5BYm%2BzLVMowqqT0vAY6pgF1UAsU%2FjmFtn2%2Bo8w2TfIHpMrK91l%2BBMt5GrWVqaHIPHmVMJEKN%2BK%2FgYAjqQSIHqfVpfytLlNQCMQrksjN6UzH50H0LsHlllWMeKB4mHRI1BVGF0ZUD7UuiJHxZKDZFpNlEN3I3cja6Qcgy1fvA5vE3cBRQE1IwMFvL9q2DSAF0vhEzamdFNuR4GFWbbj1eRYm4FBgLWio8MZQt79WPYU%2F2%2F87mtkN&X-Amz-Signature=44985a7e125ed22968ade9fcbfd0b65bece14f2794b0c672c32fef165f764170&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDU4F5JZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaepV14kYNmoqZCVzma04l54DLcEbu53UXNNyf0N%2FizQIhAK9eIOi42Xly9vDxikXDI3ITOnuf%2BNKZ42AH7M1TeHCNKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FOp4Fa9d2swVfhRwq3ANhbuFqVSGngg7nzU1SX62dom52c2dTBEMKSvtkgocElSC1kJPScwf5xR66DvlcpJqiL0fGvKV9HYQbqZl0bjBtvpLL98bhspQOQmtOQbcKDwDleTs%2FIcwntOkS2w%2BExzcnQWYs%2BIANzzVCMLJGwkplVPcaG3y4fh5SHuP9MMdm83mwiVUQVk0XiaeNlzORuEz6e86bfvSwNZtcY7TsPpnI37luLy25PotFQ5%2B94fW1tFaUQnZdRy2YZsNC3q76Xp84tMrJhoLwtL%2BG%2Bs6BeWvFcmBreiQHuseiHvQ%2Bbn1FGjzJvivrwEl8nl8SyFLRB5u3ecXLQdlUjVG0Z9XCDTWTsL9%2BFrO5cDfzqzs4erhwBKCsCMr5ffokUGHteU%2BozC2TSsmEZfA4x6YE9DJj3Uer8aNnZDDsg6VaKswvDRoL7Oe%2FXSAwbek74XaYFzB3kZNsRSBJPfHxcreomn2UDvlJAnRsS6a2hj7I9ndVVoEDauaqrcjcPyY36p5PdrWknuHUgMfEYw1Xa4ZTLyo%2Fi94mEgjhrdU3uYcd6ZCKAZ4tyCf7M48DxJDSqyS95wNZ1c6YRjFoCkCpo1Z1sQlLuzweZxrxEhCIAraiV1wnp%2BPODVxJVCGUr6tT0bzdljDoo%2FS8BjqkAWIECqV4b9sqk%2BXCA7mRPW3hNFGKZbAiJvaITP8LiMdy0mt6sje8iimBH%2BZkdtmcB1d5AZ6FJyQ242JpIzfrrIj3L15qBn3WuLwLrdOaQrekalhnTgnHUDNBqAIljt%2BkuGzOLuN4vKGbroP7jpneEIvpkSuGCialsRAL48pjhqoqL86%2BytoKA1r7VwYjaiVeIUpm%2BBZMMNtkNCyaKlLJ%2FOtFe3q8&X-Amz-Signature=b4cd5fcbbb3313dc87d179896a49b5a4abb1614bf8f3f3b0c67f0a7a2f0ffcac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNYKYFLX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0mnZjVZ%2FYXNXgWOepSnr3SxncyFM89BLMzajxEC4WeAiEA9mYr61dWyT1eiVgrKsiKiTS4bEqvzsxtQvdbaQJZJ5YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVNtzeNzy%2FHjhDcCSrcA9K%2FQ67xlkraPmNpdYe1ZKuN%2BZxI%2FeUhe1s47ILWFb1FnxUkdM2AlDpZRD2zBcYyXv4AssfWAMU%2B%2BCBHwh8bt9GPctE%2BrefPt8NdZHwAszimC4sG03DJntubUhzKDreBRQavLQliAwjthPU3M5cUqHgRMFF9fZV%2ByMP78sXnfdZMT7N0QMetCB9Y%2FtDhMZ146K7nxsW5JsVKszHw1CRj1WCSIzwK5n729WRpdTXrfbRhHjLAVvv1KJC3zYJnHBfaWZQ3auDELfndTi7xLr2goT1zEdft8VJCnYHZK2hlH6IwooGZIO02u1QO%2FEg2Vwfu83lPZOgaXmANmYfvnD1TlF71EqNjuhLndGtphtBbHkThefpaztKSSYEELdYm6aWUDNuzp%2BDJWPniTB0%2FsrQgX5wKQUOPb%2BZIBgJmPJPfz4fYz8sBZvcUbPLP6708ARZ3PTwofa33no6sqjyl2QCSW0vnATgwoSyrw5EqRskC8d5XXMs%2FSqLsMXp50ylFpcoKvu94EIS7hSDH53kF2RUnH1OlcbS3cRVLjxm5JGbZuiP6oK%2Bb7R0h2q6yMXFxIcdlvi0K8dry0AnU%2FRWbjLDPeLbUCwi5%2BFwwojmqzCXLPzWYG0Nj12fiuVenpweIML6k9LwGOqUB2neMbTyA%2Bz8DHMBV4WA4Bov0uM27bmQbH9vyTESIryqL1YwUzq4n2zVFmZtsPvRrqWJEQrrYZUdqujxh18pB27zosZ6OVeTLArCDF8WkZXLd%2BTmsXMuvQvC2OQzyPk9efBfvkPC4tyilKYm0E%2FfHjA30XDP6Vyz8%2FkZNZYqDtsywFs5ic69%2FEFL%2FbghsQzCf59jja1lJkKu1L%2Fnf2XSNGK%2FpvTx7&X-Amz-Signature=34d3115016ebc0e9e1242adf6e8d0480a37268381ca716aeed5ab04627f046b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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