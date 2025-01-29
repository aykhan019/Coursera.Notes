

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=da585812d0a7c0830675df0904c9256a2b3ecba7079b7cab1d95a1f7c82388e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=1c5480651b23ad0c4b79aa71d47a79ba282dec9dd1204896c8c9e0995804e122&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=f1081b1cae9329c3a4b33175fd199cd63e87349cf5bb24f86f410a10cd08db2f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=8ed47e6e2aa0f9f136cf6837a52b625bffc0e743508be9717bd9df1ec9c555b5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=6c66d63e5c2a1939b8aab220363e28d48d759e51b19d998e41b9f8aea9b7e8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=4f19f5e830661bca9babe5aab2bcc4c25c02f47dc6e181e82b78802100bbf661&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=02fbb0694362430713f5bb39751274b7e79a91a6f5b5a4c04cbf3671aa9f1ebc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=ed26cc6c819fff8f4068e9a5158f352b313c5b87e0d7229fc8d7f259d8722054&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=bcbfe4b5b362bb715efa146777de7b6c9d08e03d64687f10beb4c10c6262c5e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6D5DP2B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCMq41oL8kG%2FFmbIEzXE23vaHtTzH94BPF7%2BtQoZN5XAIhAKi7mX8vtWhFa4hBCEYBUOv3KyITN0GmoI5TgMaQaL%2ByKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVS81YZeDexUh3iscq3ANpmnzXsulc83%2FHTpuJ9%2Bjeabzc5Z4hpBVP4MvXI0JWLGPTzklXqtbDqzR0a1%2BdLarLVz9joiwFKq9deo4C9%2Ble9JgVMEgAagTSlZlAWy%2FJP288Hrp7JTtqbiE%2BVWdtaQ2kWjazFgPfNSTn4u15qN7%2BXLXMeqg6etbeAc%2B9Mq%2F3FtwvBXSoMIU6%2FftpFQUELa0NLI6z6k%2FqDpdUceibfuyAGMwJWN%2FLrgJTPVwpY7a04RXad%2BMUr%2Bgu2awL0raqkN57LjplJmuTMX%2Fy0BUV1yGcrkwz2ZdP0JWveBrQa97wxmITngK5PtiaqHvF%2B8OVM8L2orpEhnhz5p2mYezJhITxT2%2BCdQt3UFSImj1%2FqZWp%2F1Y%2F60Wbx7mCjpRMwANAsq%2FYavLCmKjNAO99KBN%2B6hitgPrry0nmAdUQEaVadobsr%2FhInJrMa7qbA75OyhiKDSpQK3AudZ39d9yqp%2FqPMsiWLm9oh%2FXuQ%2FZ9AvjmGocoU2NAby13zQU4WvD6vnTGbtLo9y6VPN%2BXXkz6oaYKFCPjY%2F%2BwACLrKXQKpB5xMDPUiFnQFaj3fDCtsXKmBVriD%2FcNjdMK2ACtQ5cXdrSNkT1XM%2FwrDGNoN0pvI3zeHDBHR3pcFcIK9Mw9zaeZfDC1x%2Be8BjqkAfTA9U6OclRq9CA5wGdYBlDHfpGeSw7N%2Bj4tbzPEpBB9D1DNwSOoMsCtl3HR27I%2FjJVbFzUoc7JthJFFvl0IvsVZbADoauRG0LRJkqvM2g07Bs%2FrSchXJfxmDjFMLPKaS5HZF9X6O5K1auPfeJKLdMjKVEtrIOttzNKAhJuCYxJnOV5ANBcNc0HqAYRYDAFbhNl0dSZwSpIH63qDF%2BM1Xibg9zfG&X-Amz-Signature=ad08742c2ed28d01f3203ffed19e5f54158d1f27c33fb4cee38837eb610afaa8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6D5DP2B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCMq41oL8kG%2FFmbIEzXE23vaHtTzH94BPF7%2BtQoZN5XAIhAKi7mX8vtWhFa4hBCEYBUOv3KyITN0GmoI5TgMaQaL%2ByKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVS81YZeDexUh3iscq3ANpmnzXsulc83%2FHTpuJ9%2Bjeabzc5Z4hpBVP4MvXI0JWLGPTzklXqtbDqzR0a1%2BdLarLVz9joiwFKq9deo4C9%2Ble9JgVMEgAagTSlZlAWy%2FJP288Hrp7JTtqbiE%2BVWdtaQ2kWjazFgPfNSTn4u15qN7%2BXLXMeqg6etbeAc%2B9Mq%2F3FtwvBXSoMIU6%2FftpFQUELa0NLI6z6k%2FqDpdUceibfuyAGMwJWN%2FLrgJTPVwpY7a04RXad%2BMUr%2Bgu2awL0raqkN57LjplJmuTMX%2Fy0BUV1yGcrkwz2ZdP0JWveBrQa97wxmITngK5PtiaqHvF%2B8OVM8L2orpEhnhz5p2mYezJhITxT2%2BCdQt3UFSImj1%2FqZWp%2F1Y%2F60Wbx7mCjpRMwANAsq%2FYavLCmKjNAO99KBN%2B6hitgPrry0nmAdUQEaVadobsr%2FhInJrMa7qbA75OyhiKDSpQK3AudZ39d9yqp%2FqPMsiWLm9oh%2FXuQ%2FZ9AvjmGocoU2NAby13zQU4WvD6vnTGbtLo9y6VPN%2BXXkz6oaYKFCPjY%2F%2BwACLrKXQKpB5xMDPUiFnQFaj3fDCtsXKmBVriD%2FcNjdMK2ACtQ5cXdrSNkT1XM%2FwrDGNoN0pvI3zeHDBHR3pcFcIK9Mw9zaeZfDC1x%2Be8BjqkAfTA9U6OclRq9CA5wGdYBlDHfpGeSw7N%2Bj4tbzPEpBB9D1DNwSOoMsCtl3HR27I%2FjJVbFzUoc7JthJFFvl0IvsVZbADoauRG0LRJkqvM2g07Bs%2FrSchXJfxmDjFMLPKaS5HZF9X6O5K1auPfeJKLdMjKVEtrIOttzNKAhJuCYxJnOV5ANBcNc0HqAYRYDAFbhNl0dSZwSpIH63qDF%2BM1Xibg9zfG&X-Amz-Signature=fd3f799d68a7deec519e95c38cd9cf89b1f0add0da306da98759a67a178227b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6D5DP2B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCMq41oL8kG%2FFmbIEzXE23vaHtTzH94BPF7%2BtQoZN5XAIhAKi7mX8vtWhFa4hBCEYBUOv3KyITN0GmoI5TgMaQaL%2ByKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVS81YZeDexUh3iscq3ANpmnzXsulc83%2FHTpuJ9%2Bjeabzc5Z4hpBVP4MvXI0JWLGPTzklXqtbDqzR0a1%2BdLarLVz9joiwFKq9deo4C9%2Ble9JgVMEgAagTSlZlAWy%2FJP288Hrp7JTtqbiE%2BVWdtaQ2kWjazFgPfNSTn4u15qN7%2BXLXMeqg6etbeAc%2B9Mq%2F3FtwvBXSoMIU6%2FftpFQUELa0NLI6z6k%2FqDpdUceibfuyAGMwJWN%2FLrgJTPVwpY7a04RXad%2BMUr%2Bgu2awL0raqkN57LjplJmuTMX%2Fy0BUV1yGcrkwz2ZdP0JWveBrQa97wxmITngK5PtiaqHvF%2B8OVM8L2orpEhnhz5p2mYezJhITxT2%2BCdQt3UFSImj1%2FqZWp%2F1Y%2F60Wbx7mCjpRMwANAsq%2FYavLCmKjNAO99KBN%2B6hitgPrry0nmAdUQEaVadobsr%2FhInJrMa7qbA75OyhiKDSpQK3AudZ39d9yqp%2FqPMsiWLm9oh%2FXuQ%2FZ9AvjmGocoU2NAby13zQU4WvD6vnTGbtLo9y6VPN%2BXXkz6oaYKFCPjY%2F%2BwACLrKXQKpB5xMDPUiFnQFaj3fDCtsXKmBVriD%2FcNjdMK2ACtQ5cXdrSNkT1XM%2FwrDGNoN0pvI3zeHDBHR3pcFcIK9Mw9zaeZfDC1x%2Be8BjqkAfTA9U6OclRq9CA5wGdYBlDHfpGeSw7N%2Bj4tbzPEpBB9D1DNwSOoMsCtl3HR27I%2FjJVbFzUoc7JthJFFvl0IvsVZbADoauRG0LRJkqvM2g07Bs%2FrSchXJfxmDjFMLPKaS5HZF9X6O5K1auPfeJKLdMjKVEtrIOttzNKAhJuCYxJnOV5ANBcNc0HqAYRYDAFbhNl0dSZwSpIH63qDF%2BM1Xibg9zfG&X-Amz-Signature=65557f88d433f90edbc7c5730cd5f10bc2dece934259a23e909e981fdca44c4b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=80502a4542fba7cfc8616021c9de1bbd54972e126faa21a0fb415fd31ba6d449&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=7ed53a32872ca68225f6d790248ceca77240b458849ea53f3bbfae3fe7f3b9b0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=b73aa2f71c6bf9766a05d524d127a25ce9e17bc64654806618ec9ca6cfd36ec4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=94bad30b5995f5c91612ed335f5f52442643b5bbf067b4810b9ffbf91d02ff54&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=5fc7e5cdb9d5d31ec61faf0e962e7c52ebb5b2d89c79f41164732cf1b2da5494&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCNIJLVI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAphAoj7gCYYqTZXUtkmSOQiWO1eHecSQcYOGTjaxIpcAiEA7igMUtt3giUpLROdIyIZ%2FQCBa%2F8fHwM1hHWGgvexLVQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQp8%2Bcak40nzEX90ircA8HfjCNKH84vV9JVNrcCSqSd41wgPPMSk0XOMIgYGo9gaaMB815SEVYh73SMvr0FNASW5KThlSTp%2FcWyOq0QK3lFR9WAXLIePMctvmz5FOEzFE0HmtJHhMcIPwZtbej3Jk79svJZYgKky2sMraqrZ%2BtPQoiXKUlJYkJp8vV4c3JliwXpNDSMm5DiUss6J3V4XFRy4cPwO%2BWIDTv57ozwz7ryNoEKbfNoOJtwp2W7gAFgS8bk%2FtVTGz%2BxUsPf3YBZ7o4RE5BenTOm1GjnjMC4z84PGcQpZQZqenXmoQyQAgL0wKNKQK2%2BrV3LiAIjgr9XrwctnAzla%2FZ2vpZ1zq3Bp7wLLzwnPXL8H0lH96DMuRTmpl5DyzbL3y6VeorGazVsHL17snxaM6UUYXb%2F77Z6TkKgnTVWgJvsYcifLoXvOL3%2BC003hPw%2FK0cClapy9Jmu4aypbjrZ0aDqT%2B53U0UowWKQhB32%2BFzafS4RyKoocTPrNSosBs6MNkss6HKMce7PgJ3wO58hlxTyj5NtY1vCgEnqUw04wHuYxxObMegX9y8eCYcfc0amZI8CkWjbCuhXOUCk6kXgDz%2Bhm5Q8Usji5Alt8JO4sZKbteLxEXaHXclef6t2rJm%2BKCB1obU3MJbI57wGOqUBuLJy8n9NN64QWNvanFTNNvcyQnDIrvkS8alzPvkvYmFEjSObDkPZxRKuWQrDDNMU2s2mlgy2KKVTWvyJ90FPY3UNHPoqOPk2iW9Wqv4jB8yHlxESiU1nQlsKxsR%2F2oXjjeXRcK21KI2Zo5Ucglf4oS%2F8do6ZBIn%2BYx2WR%2BLO7PZPssonEoNVKKBjxacR%2B9s7TqhAE5xiyemNww9UqtTCk7iTsrTE&X-Amz-Signature=a6446b1861744770bf73b3d59c2f1d2703dfc92391ea8bb73959104ee1ed0ddf&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBWO3HKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCmdpUL2F3M3mjpioY%2BPY%2F5HeM9M%2FMT45ZVixvcs6rtwIgFJeqD%2FPQ585HVTcfF9wtnotRqU7nf%2BxwXzkpmpFm6PMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB3gKXy4Ya8h04TaircA3BOdOekmqqCAUFp79hVAabSsddBiaXqXgVaJ4ZA9bg%2Far0dRdmTjVYDvncAzaxt5T%2FH1ElBCWXkTQ2jowB7LWUPnN4dSyVa%2BguwBqhlzxY0lUHIPwjnWXYuL1rZ%2BNizMhf89daDcgrntHf1KAHyZpeAy3kAlxfDsY9o91Zxmud57OE4k7zDrK2Wa3qbyQqBoxwLsD8ojndR2wPV%2FoXEj5KrxetZZn67GLyz4rpQUbg9OLxEpFkvIyt0iL2nJzceSQDQHr1MBM%2Fzna08gH5EdHzkfexjCsKcTUJN0O0QXxuWWV7IkgQtI9rsd2LhfiLgcecOJnameUqBpQO8TnXL4%2Bqni5X8BfEeNPzvTZ74OBEzkVTNO5kNdpZQ1Fd972I%2F9yXRJ0Ig6hQx6Jlow7LaMq5oqcSdQPwCLvl4CKbfcKq0WED1Ga2Fm563zT6VcaOXMVaHGbnsXSRm2QdybJqhdqhacOU%2FY2xshuWvxwdA6cLBxPmOFN5fesRsWkerQF3jjx%2BzJYR9cCB0lZAx%2B2eoRLFM55T8zcNmKddKtGqs49Qq86vArjB0RSq4wuKp%2BuXNXGRDAU1TMNKpDOJADjaa%2FET%2FM12Q8M7WRl01Zq3wgEnYiS60uF3YepZMyRuIMJnH57wGOqUBZXsoDiayKL9pfjdHF0NNXFwxjH5uBIlMKA7ULljsV9%2BF7BqmND2nosIoF3%2BtoHp80wCsFuRMfUt0NIP3lyJKQyN8Bda4cSvtvfx52k2o1LdeRXv2Z20seiBUDirQPfYCxzpO4wQz9iUuZzrK0QQHgug3sVQHfxTiU1U3wI8NhOOwjiNjlxJ%2F2LSs0D24hEcBDABQSug%2BkVOQ4%2FiJ%2BQNwC6pWwt%2BJ&X-Amz-Signature=52488c08c6f229e681aa49b331e851b5476cabfc845a4dc3b6abcce267c5b1f8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBWO3HKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCmdpUL2F3M3mjpioY%2BPY%2F5HeM9M%2FMT45ZVixvcs6rtwIgFJeqD%2FPQ585HVTcfF9wtnotRqU7nf%2BxwXzkpmpFm6PMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB3gKXy4Ya8h04TaircA3BOdOekmqqCAUFp79hVAabSsddBiaXqXgVaJ4ZA9bg%2Far0dRdmTjVYDvncAzaxt5T%2FH1ElBCWXkTQ2jowB7LWUPnN4dSyVa%2BguwBqhlzxY0lUHIPwjnWXYuL1rZ%2BNizMhf89daDcgrntHf1KAHyZpeAy3kAlxfDsY9o91Zxmud57OE4k7zDrK2Wa3qbyQqBoxwLsD8ojndR2wPV%2FoXEj5KrxetZZn67GLyz4rpQUbg9OLxEpFkvIyt0iL2nJzceSQDQHr1MBM%2Fzna08gH5EdHzkfexjCsKcTUJN0O0QXxuWWV7IkgQtI9rsd2LhfiLgcecOJnameUqBpQO8TnXL4%2Bqni5X8BfEeNPzvTZ74OBEzkVTNO5kNdpZQ1Fd972I%2F9yXRJ0Ig6hQx6Jlow7LaMq5oqcSdQPwCLvl4CKbfcKq0WED1Ga2Fm563zT6VcaOXMVaHGbnsXSRm2QdybJqhdqhacOU%2FY2xshuWvxwdA6cLBxPmOFN5fesRsWkerQF3jjx%2BzJYR9cCB0lZAx%2B2eoRLFM55T8zcNmKddKtGqs49Qq86vArjB0RSq4wuKp%2BuXNXGRDAU1TMNKpDOJADjaa%2FET%2FM12Q8M7WRl01Zq3wgEnYiS60uF3YepZMyRuIMJnH57wGOqUBZXsoDiayKL9pfjdHF0NNXFwxjH5uBIlMKA7ULljsV9%2BF7BqmND2nosIoF3%2BtoHp80wCsFuRMfUt0NIP3lyJKQyN8Bda4cSvtvfx52k2o1LdeRXv2Z20seiBUDirQPfYCxzpO4wQz9iUuZzrK0QQHgug3sVQHfxTiU1U3wI8NhOOwjiNjlxJ%2F2LSs0D24hEcBDABQSug%2BkVOQ4%2FiJ%2BQNwC6pWwt%2BJ&X-Amz-Signature=8fe137738f2026dce1236817e1dc4a01ec09e3471d832b5fd231ec1bb02850f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQXA3KUH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXzD5rjJGGbPg3Hiv0IzhcuwXDsWm1iTx3qlclUQEOdgIgf3jc3ECQhl0cR%2BEnxVnu49CbCCFQzmVuUXKq9tTUhXsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTNAUoHXwHd9xgPjCrcA3TGLS0MI8VLZenFMbYCc50pmmMowOVr%2BXSm688Ea0EbGnDaveiLxzB9jbXZQXvL61ScE%2BRdJprAWYx5wSuyZJB6VErVvj%2BohbKPeRtZKlMIgaDWhr66B7nnJN1xQ2%2BeiWDPHJxd3NtCDvHdwX8wtiYc2mgeiLwHSNXeVRkHQkcM2q3u7p0GK0bW712%2BPy%2BUrwvJM9KBuRoHhXPmDcRO%2FBzK39oyDjqVHu3lpfW8QUWiSgnGcI3pFaxiA4P6fWLJpVCuwLlM1Q%2FlgjO9FISL1LTvYHwLYPQ%2FTed%2BKj4Fr%2BopULAScP9WEYjPv5DAQDS6ZTQGG00UbLWOEUz6z83RKybXLNQnrqjCHYSBwUb2MA71%2FoQiJd0GZD%2Fa5voOALUql2uLCnezt1XkspJrAd6DyezibnqNd4pxVzOorG6khkf1y4gArfCJbSDjbizjoTIUBPjl2zlkMYnl3h%2F8E%2FNcHkOLi5Jljnb3GlIPWhh%2B8%2Bt5pYNC7bY8%2Fzu6xJaGJpiLjtWgZ7hvWrjqsdRgNz3X0qZoocVtmJ8lJGnZjzDar1obHxzxE1K2vYRWea3MdFLcogpaUUFdEEwSgXjXhqvznoPWuIn17367lE977tAStPn6pKiwsbKG0gI5bS4sMMvH57wGOqUBVIMGB1buOtJEyBdeDIsqtI2H%2BpxInL%2Bu2jZ6ngk2MTZ9zKsWm8iA9jq95i%2BV%2B0dFBpoyN5PRp%2FRQ%2BAz5PHl7yXUa2Jf%2Fkdtrjxh3e%2F66WkIOPYBOqRWVxs3yOi5OCNst4IubQkKeuKwFS5v5CWJmou2cPbFc7lH5PuJEzo%2FMNgCxF6AiJ8Rx5IGZ2%2BdqPtgDwGg7KzY1lUt20%2BDLprvNDauRK1vT&X-Amz-Signature=955afb5d5a231e66b46b87ba54eed631c009b0a9c08f9d6c62d486023b2b8586&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZMPM22%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2FLwzwvtHt0M07BWAYDunKtcHODggVkmBuWxMrhtoegIgeuI%2Bb19DKcfUfejkXJPMGlgUXqIaI0Qr7GbJJrm2cdgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMN7M4O%2BzZ3b0UyZSrcAyMSqQRx1Pg%2BSYU0NG9Q1yvKPvHZADwW%2BkQ69DrKco77EplqpjjNaSMM0Utsc7dD96uBpEYqsR0ttEdpJYIyndeM6RefqU32CZU49Ssp0il9fLXl2f9TtjgeqpcbkfNqebDg1CLPsyF6exQb%2Bt7yQprKq%2FWePuB2a0tnE50tJ3B%2BKXlCOD%2FEmsYKvesoFtOLF%2F0YhNOrssjQEiIqlbSTboCzDKE3R2E54otlePpzkHeMkbfK0cKt4nPFjyzBgaqr%2BdMjgQ4g7rZPa3QB9MUj%2FZv3gYsHd6e%2BiP2sAqEQYkpQlbI3ztjzfHlDSoeMxoBR8NysG%2B7gZVuJq1NCRFOSr6NLekvA94xi2PTis8mWc9M9rUJUR67JIeC%2F%2Fb1gpLlNe3kJGZ9ftVkE9sl3Z12q3OOjAqrGSXgjJaVLJi%2FjAtCt%2BkEEelr5jnbb1P1QP7IDaE4vfekZYTfFoyVvbtic2pBL264hOsLdfTNMjN1Ar0buPcTZBL3u2z4iPt%2BqE2sXP7Bb3HMQbOP%2F8BqHn6YAc3TmeTk5vL4UJnSqgtlHKqaBWjqAVnkuBsJM8QPt87rVIY3Purto0GdiWvosAux%2Fs2KpKb9lW0327R6QoBT9OsVmXKWLJT9sztcp63dvML%2FH57wGOqUBwaD9AHsIRoWWqcUY1slUvJUV1QADuVW%2BhoCls8hyTbiQNVTAnWcWC4VeUSUzIRQjkZdX3l9rIBqkkqGd6ZZ5zgO3QG9bEWeQAbx89mz7gxN1GtsbBe2J2eb9Go7OZRrbFIo%2FP7fwq6xqfQpGEKakrRH2nBKaKxJlcTVc0LDW6meGTbkKegt4aWjgIYAWQzH%2F9iRZUz%2FNhhmreTi%2Fi%2FRppGXlkl83&X-Amz-Signature=7feb0e1ab518933ad9d0c09b1c9f4ca468cb239bd4714ef66082af56d720a8f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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