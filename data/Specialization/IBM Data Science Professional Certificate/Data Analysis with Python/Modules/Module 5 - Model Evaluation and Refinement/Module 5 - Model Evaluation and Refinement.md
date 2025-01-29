

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=4c6f3681c70747d692d18258b5568c8502335fe49061dde011e6e11670b902b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=a531fcc74ca943e08495d91dfbe16ba06447f7c1354e43d060db0d746f59f750&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=d18f7ef70a76f187e5eb1612bd09bb84d5cf114bd79fc30a7291f2a5a8d3f0ed&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=54e146be055e05b3229e6dc27e5774e9ad6ce50dde1b03aea72e413013fdf1a1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=3fb4b8d3ca0bcbccf6b224b322bbdb4f0740c5b86e6714cf9eb7a77cc6c646f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=c00b8b7a780fedc0bd69c2ce284ad4a2dafa16181335dead08f5aecd2c309050&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=b9bb8b02780077ffe3f27f625823c567d4819a511f3dab312c5fbd34bfce2406&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=45eae805734493c8e892b063ae36666b05d712cb0c62ca6ad3f38c578ad08087&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=11fabba02b15ddea07ea885d780bcfe2d9340f6f6fbadcb4ec99650aa9419d34&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BN3UGZF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDarOnECLneXlXw5Mc2t5wetSfCtF1xBK7z7uSnl2fKQgIgSlvpjiZ4xvsAGMrASBW4e0F7FK7%2F0rk845B7EK6Xo3UqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtSzVYOTszm9HPTtircA1SIirA5v7%2FqpFdvy5NS%2FonxBscO62RUe1uG%2FMmHAqm2vamUoz524Nji5Kl50e19%2BVJHcoEyF1TYp3WZi3JHMEdx6FOpahMTu%2FaOfmiyS4VzSZdO504yeTtWMEm5Mwuk6nCBt%2BEFw4AEazcxTiKpGdhOlgO3o%2BMiS1mGclp3a7HiesV%2BCcKQpenOi8Mdeiz9Nv4CLEi922qe3AeaEdU11W6I9j7dP2C5MMikTjCF44acHxhlQ4qqAz47WgSOuQCANtHQxgOrNfMYvzEid%2BfMRdkEufL2COsxuC6Uqs4Zi%2F6NNd%2Fm41e6Eq3Bf7nVjFcY1kOoHj20OBuK3LglQX2Rr3Glbu2B1%2BXtRlFwbITz%2FO%2BRl2%2FV7P8W%2Bvd83saYi3mIUrG4QclDTW43WBI2w%2FrRZUqb51JBFdxYNGWNugRcMgpmGMcRvgSao7sGELLe07Y7K%2B7fxAGX19JtoPdhu%2FKI2SmlZFo43xJ9W96xBFa%2BzJEmW5ZeC3wob5zS3IFPwiMBhUbBgMN%2FMMmFe%2BhZ6yzQ7YQz4Fo%2F2sD6khWo16aCXKW8s%2BX9NhItdq6%2Fh4hRVES9UWPMfTHkbY9MM2UnlYEEULTB6aLdz2K1X9hKHgeu91tQuCnsO9blxEfi73rVMODm6LwGOqUBrFl7asZ%2Btkq6qCxVpFlRhYFRTIIqrArqbn5hy60FgeqYxw4c%2Fr%2BsEIItKuAuIDkpsV75B%2F%2BEIohaQqB1oSUxEnbO4r45nUKFAoIJcdrfWWwKjRPbcf6jtioFjRHI4KePcKoBky39i9aiDTqMTDfJE4hPAPgXDXENT9bmLl28Vpt76%2BPqbioKzYfluUGsnhHwPmAyBF13J1TD8yUYdrrkz8dEOakU&X-Amz-Signature=fd25034f40ae5ad780d48e29d50c4a9c13952fbf9e0bf83c8901b68e43e82296&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BN3UGZF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDarOnECLneXlXw5Mc2t5wetSfCtF1xBK7z7uSnl2fKQgIgSlvpjiZ4xvsAGMrASBW4e0F7FK7%2F0rk845B7EK6Xo3UqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtSzVYOTszm9HPTtircA1SIirA5v7%2FqpFdvy5NS%2FonxBscO62RUe1uG%2FMmHAqm2vamUoz524Nji5Kl50e19%2BVJHcoEyF1TYp3WZi3JHMEdx6FOpahMTu%2FaOfmiyS4VzSZdO504yeTtWMEm5Mwuk6nCBt%2BEFw4AEazcxTiKpGdhOlgO3o%2BMiS1mGclp3a7HiesV%2BCcKQpenOi8Mdeiz9Nv4CLEi922qe3AeaEdU11W6I9j7dP2C5MMikTjCF44acHxhlQ4qqAz47WgSOuQCANtHQxgOrNfMYvzEid%2BfMRdkEufL2COsxuC6Uqs4Zi%2F6NNd%2Fm41e6Eq3Bf7nVjFcY1kOoHj20OBuK3LglQX2Rr3Glbu2B1%2BXtRlFwbITz%2FO%2BRl2%2FV7P8W%2Bvd83saYi3mIUrG4QclDTW43WBI2w%2FrRZUqb51JBFdxYNGWNugRcMgpmGMcRvgSao7sGELLe07Y7K%2B7fxAGX19JtoPdhu%2FKI2SmlZFo43xJ9W96xBFa%2BzJEmW5ZeC3wob5zS3IFPwiMBhUbBgMN%2FMMmFe%2BhZ6yzQ7YQz4Fo%2F2sD6khWo16aCXKW8s%2BX9NhItdq6%2Fh4hRVES9UWPMfTHkbY9MM2UnlYEEULTB6aLdz2K1X9hKHgeu91tQuCnsO9blxEfi73rVMODm6LwGOqUBrFl7asZ%2Btkq6qCxVpFlRhYFRTIIqrArqbn5hy60FgeqYxw4c%2Fr%2BsEIItKuAuIDkpsV75B%2F%2BEIohaQqB1oSUxEnbO4r45nUKFAoIJcdrfWWwKjRPbcf6jtioFjRHI4KePcKoBky39i9aiDTqMTDfJE4hPAPgXDXENT9bmLl28Vpt76%2BPqbioKzYfluUGsnhHwPmAyBF13J1TD8yUYdrrkz8dEOakU&X-Amz-Signature=6c0d01276aee53d4b30f7f3b3fbd842078e768370b0bb40aa5279d535d0558e3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BN3UGZF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDarOnECLneXlXw5Mc2t5wetSfCtF1xBK7z7uSnl2fKQgIgSlvpjiZ4xvsAGMrASBW4e0F7FK7%2F0rk845B7EK6Xo3UqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtSzVYOTszm9HPTtircA1SIirA5v7%2FqpFdvy5NS%2FonxBscO62RUe1uG%2FMmHAqm2vamUoz524Nji5Kl50e19%2BVJHcoEyF1TYp3WZi3JHMEdx6FOpahMTu%2FaOfmiyS4VzSZdO504yeTtWMEm5Mwuk6nCBt%2BEFw4AEazcxTiKpGdhOlgO3o%2BMiS1mGclp3a7HiesV%2BCcKQpenOi8Mdeiz9Nv4CLEi922qe3AeaEdU11W6I9j7dP2C5MMikTjCF44acHxhlQ4qqAz47WgSOuQCANtHQxgOrNfMYvzEid%2BfMRdkEufL2COsxuC6Uqs4Zi%2F6NNd%2Fm41e6Eq3Bf7nVjFcY1kOoHj20OBuK3LglQX2Rr3Glbu2B1%2BXtRlFwbITz%2FO%2BRl2%2FV7P8W%2Bvd83saYi3mIUrG4QclDTW43WBI2w%2FrRZUqb51JBFdxYNGWNugRcMgpmGMcRvgSao7sGELLe07Y7K%2B7fxAGX19JtoPdhu%2FKI2SmlZFo43xJ9W96xBFa%2BzJEmW5ZeC3wob5zS3IFPwiMBhUbBgMN%2FMMmFe%2BhZ6yzQ7YQz4Fo%2F2sD6khWo16aCXKW8s%2BX9NhItdq6%2Fh4hRVES9UWPMfTHkbY9MM2UnlYEEULTB6aLdz2K1X9hKHgeu91tQuCnsO9blxEfi73rVMODm6LwGOqUBrFl7asZ%2Btkq6qCxVpFlRhYFRTIIqrArqbn5hy60FgeqYxw4c%2Fr%2BsEIItKuAuIDkpsV75B%2F%2BEIohaQqB1oSUxEnbO4r45nUKFAoIJcdrfWWwKjRPbcf6jtioFjRHI4KePcKoBky39i9aiDTqMTDfJE4hPAPgXDXENT9bmLl28Vpt76%2BPqbioKzYfluUGsnhHwPmAyBF13J1TD8yUYdrrkz8dEOakU&X-Amz-Signature=d0031318f946a09b752e7a57b91e45bb624f9efa5a0a1e5d4cb5756c8e9a66fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=313e8c8a807fed0d0ec55e741770c963c30c9d12002a96bfacec13050ebd32ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=ed88701864e6857b06342d9a8ef60708285ea5c4d4272a100ab7b2bc0c82d51a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=51181708cf5af6ca280452c658632d47db14bb53d693d366e8903200d1db919a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=6b429bdf4b66bd95de79a8cbbce973177d271c768b09e8a483475178c23e6198&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=e5713347cb7699fd7f6c70e8bf64ef626630f2e047c1b25c9c92304bfcf21ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672ISMHE6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGdDPqU%2FcEDHngrollCp3n%2BmaA1Ruu5uGSJ6dlZ2GQsFAiEA3p%2FDbcz8eCuczdNJiUEGnrRlq%2BO6tDi20hWbEmA8zt4qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZxvNda50Ys1%2FdV1CrcA3VtpiL6w8uxDswQBJVc2HrIKvfm1R2S7euPFkfUB%2B%2FdnJgrTr8MUAs0%2F3r0QryJ3zlrWMo%2BNpslfaTAUfIuEcW6zAzx6jxXJIVZKAbTmiR9g%2B3jsi1u43PCMk%2BpZ%2FTbRg%2F%2BuW5T%2BYrkVeHLNd7fK3TUGs0cFDUY2pz0Wz6OYOrwQb4bflswnUD5hLF4LVau%2FVwKKrx4n%2F1PKWeU78NwWMNelpaD1tfdlLN4o0KOHD3j5fqp3X84Xo1KQ5IwKzva6XNbjnRfahBfulx%2Bf0ckaSAmADgTCj5QjknuYEgL5Ucu2H20UU5o%2FiffK8C5lmAnXAdpGXdtCHUV5kqVtlxENZaW%2BsYKoYTced5%2FD0Y%2BIQ0n8WkonTuhfPdQiWDGhXUaWqxgMk0hmIGt7ryEfX%2FPHNQzp7eeTzV3EHd%2BhVK5F99po3DUl1DC4fS%2BgFCbJ8qqHrlx41dC%2BkcuVnBbFp%2FMhTn0DIj5Dil3VabkxYYd7NRoTsvI6gbo%2BB9MZdy0p2Q61WjFNTPJK3HVwueDfu%2BVPAXLfo8%2FYWQR2X9Xn6LJzAwT%2B5dDRuflG6NaUc3ckbn%2BkYxcgskwj3S9McNYJ19P%2BVdPAe%2F6VVeHNRteHzj%2FMGSt3SEO%2Bzv6hO%2FUr3YxMOHm6LwGOqUB7XSFVmwmdhzaEM1MLMUE7rzbQYbNls2iqXLsVocQwbOMds90ttTYRR2KY8BnRODyMYNuNZGp%2F9rz6RtDeVnYCS%2BRuXYBD44AES7CEQVmT5mInupeTwnePGJr5iCa5XqUEpFwKin9pYLExQwL7k%2BhheuKsXdhM0WqnRHtBbhg5DNy8n7xHNkSktzKLli5MQU1roKWTL941y6NTZYPO4%2B5R8M%2BHNA7&X-Amz-Signature=85cd448c86a2b4c9e313d449627619f3a0d8b3ea6d28524f658fab3e43c1d3a3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQPQCJZ3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkbK3HLzmqkPzmyfEt%2BmpVraTx56pui5DDZrIHbqQPRAiEA%2B4qSOgHDeTBOyimQoGGvRn7Pi4obvF2EfWdoWeFq%2FPkqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3jgDjrzrSM6k415SrcA7a3ztiKJHl7gc%2B7FOV19WVCUOHBwV088%2FAXW6wUwYxq%2BEqH3CkP%2FiWzmNi%2BwS9VRUSFJ%2FhYr19MiJ%2Bj%2FPgvYYeuGNpjrUIqUfKim62WxLiw%2FaPCGuhYD1vKL7A1VH7A6KFo%2BZPAdwK73ud4SUYiPcpdHPAQYM8rJ4M1etOlM%2BmAgpZD41kYxhP4pV3mTieSUDuk0YG1KgDg5BN3p9%2Bv0kxaGrkcmj3gkx9zxBwvnytfFUk2XHc%2BBE9b2l7hTtqgHCf1zFMVTXc00K0g5x%2Bl78Dfs0pgXy4nOBLx3M%2BuFfYysvsGZXQy3GKeCQxxwX36Lxs64GS2Ip9qLwpXELtrLvUg7FwyqwkFM8oZbe%2FfaUgpcTpC4RNlKEX6ojb98TlFBQuUjEx%2F%2B7YShkBxU0WFe7GxUQ%2BO4irnlTTRo9WpHIjlzBpnBTAq3X4fzlHXpaz%2BVRJ2ScZwDWRn67uXaPFCxmF%2Fd%2Bw3aboehEBrMRIJ6QgVJvJNk8oMTE5UJT0gKr1DpwEutgVk6gLjvvxpiR0Ri3EHUuHV5N63bFYkYG6mVyFLWju%2BSLDJQE6iKdrX5Bevg1vg0AylFYd78TZzmyRCEOAvv0aELJ3TsgWoogz6vB5RoeJGQMnJXBeEKTEjMJXn6LwGOqUBilILAZ8c7%2FEfQ1mESWJvL%2FV6ELJJs2ERlzGIrvY71fC3tomDiXo%2BjQlG%2F0XGuxjR8RY%2BjhLZ32J1BZ2CNRq9suE6AJ0fVXqCV63Powhf%2FhktkvJ2S5SIj%2B%2FP9pg5YXLgx%2FsrakQNQRe7PeyBOvztU7TXVXz8uJrVOwkbbgvrL9b9Yf19n%2BE1Dgrydtu%2BGCJIzSPP1puhkoFMkpCysSzqmW0KHxv2&X-Amz-Signature=f61f3ac7dc65bf77fcaf8750ae8b57101e71cfe711c8c89503bbcae6d0fb3346&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQPQCJZ3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkbK3HLzmqkPzmyfEt%2BmpVraTx56pui5DDZrIHbqQPRAiEA%2B4qSOgHDeTBOyimQoGGvRn7Pi4obvF2EfWdoWeFq%2FPkqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3jgDjrzrSM6k415SrcA7a3ztiKJHl7gc%2B7FOV19WVCUOHBwV088%2FAXW6wUwYxq%2BEqH3CkP%2FiWzmNi%2BwS9VRUSFJ%2FhYr19MiJ%2Bj%2FPgvYYeuGNpjrUIqUfKim62WxLiw%2FaPCGuhYD1vKL7A1VH7A6KFo%2BZPAdwK73ud4SUYiPcpdHPAQYM8rJ4M1etOlM%2BmAgpZD41kYxhP4pV3mTieSUDuk0YG1KgDg5BN3p9%2Bv0kxaGrkcmj3gkx9zxBwvnytfFUk2XHc%2BBE9b2l7hTtqgHCf1zFMVTXc00K0g5x%2Bl78Dfs0pgXy4nOBLx3M%2BuFfYysvsGZXQy3GKeCQxxwX36Lxs64GS2Ip9qLwpXELtrLvUg7FwyqwkFM8oZbe%2FfaUgpcTpC4RNlKEX6ojb98TlFBQuUjEx%2F%2B7YShkBxU0WFe7GxUQ%2BO4irnlTTRo9WpHIjlzBpnBTAq3X4fzlHXpaz%2BVRJ2ScZwDWRn67uXaPFCxmF%2Fd%2Bw3aboehEBrMRIJ6QgVJvJNk8oMTE5UJT0gKr1DpwEutgVk6gLjvvxpiR0Ri3EHUuHV5N63bFYkYG6mVyFLWju%2BSLDJQE6iKdrX5Bevg1vg0AylFYd78TZzmyRCEOAvv0aELJ3TsgWoogz6vB5RoeJGQMnJXBeEKTEjMJXn6LwGOqUBilILAZ8c7%2FEfQ1mESWJvL%2FV6ELJJs2ERlzGIrvY71fC3tomDiXo%2BjQlG%2F0XGuxjR8RY%2BjhLZ32J1BZ2CNRq9suE6AJ0fVXqCV63Powhf%2FhktkvJ2S5SIj%2B%2FP9pg5YXLgx%2FsrakQNQRe7PeyBOvztU7TXVXz8uJrVOwkbbgvrL9b9Yf19n%2BE1Dgrydtu%2BGCJIzSPP1puhkoFMkpCysSzqmW0KHxv2&X-Amz-Signature=611b24fd943c58eb509e59a1c1cab43b280adde616341b2e8073aa966788eced&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ6DPXNE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJHAtqbDX1kEw2NjeVK7aMsMgIJLusgo7dzMR6dgujtwIgDS%2BhG8PmLdOG%2Bu3KZY1ohMbSSh1xKIkfuu%2F60HKMA4QqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgzxVymLXZp7PlKwyrcA%2F%2FU7sx7RK2kE6%2FjYFGPjO9pLbPhigp6t5qRnAIVGaHRPDTNHmkoZAYXwqpOjHXZwHNvenqFXpXVIxt0DzJ0Po357PASKpKT39VuKg3x84u6NECYf%2Fs0rQ7OVW6huEx55yENObFTEfDmA4rtUiwMcqpX%2FBgHmb16SE1DpyiQwSAPaLnLAt8YRVFh%2FVdkdUFnVsuarecygRhjqJuFQs6hy7t6%2FgT7QDbsVWlXfhRkNsIM9NOL3epwz139whOwgJeNfV46cpMeTeKmdnElDz%2F%2FzHPK%2BsIQh6aN6ZKJoBNBMP1HlXr7zjC7HCAq%2BmiVfevy%2Bsi67et5Q7WK29Jq6GsWw%2FS4FB8gtT8IGwxKXWAC38Dx8S3YonEFLQ7Ji7fEib6N4Uyz1GXSNxpQmSHot8pEciUHPyqrm73PkzGGaXybrzr92cd6VzX%2B%2B3WYWyQE6DWuNIvvESEAP25feYxFddRNuOIrVK5xgy5hbhLF9CSMn7GnpnwHRWCwQvEiA3Q30Q2raloV0QuKNM83C4e6485TJTeUiMsTKSDVn40PyzqTvt3ilnAbZB4Gc8wFzga%2BY%2FFoQVkDna9jiwNkZZfhkBhAq9EfVx2dzvPFTRPIMFrlYJ0N8iryn3bVsPfZPHJhMOzm6LwGOqUBTWWYWOgfKQuT9jj%2Bn1lbi1g4rSEXY%2BS466TSz1egahYAaeTnlpzzdtL3nyOCnlPDil2G1LdG6u0YH0h53JhE3hh%2BqmG2fmEzrw6iRd0giePaz3HSFxvz2kJNxuGBErkald5agvH8GJ1tHzIWLZfE5bYMJq%2FMrszO8aLpHPSsTCvbjzlp%2B8ZwnV1ppbKWJwQ3YU57sktNF6rNjh6S2KFZ10pABehb&X-Amz-Signature=2f52c724dccb53e9e5c220c959f01ef21e0329abc548829fa1851c5b23f1cd7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R2BOZTQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB76ZID0pKXIuzBcdR37T0Jt9I4eFTcARtlSKlsjT5cHAiEApAl%2BmQ9REzu%2B%2BtZe2CWvtO296VdS04qJ9MobmVs9vi0qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbFzycFtvpvNTBCCrcA3nFOiDudDU60se8YUATo32QftfqM6NPJJ0zaMintzBxqUtXbAMUb2pVjW%2BjqYuH2XR%2BBZ8K8QUyzM0Ejvndbq5aXv8yoPOEivLTL80Xdfytp53ELtZVnBU3oAWEtp0f3tnCm5xHxkdEu%2Fquk6TG%2BXl23khAWuu%2BEanA1MGQPGsLn9J5J%2FmevNoQ8jysV1Qxo7vLYamvm%2FweW7UD11uth9fJf0x2wxCVw%2BHjt7FGOSjyiRN4g5JMaOJeBqGn6a9N5Uf9z5wzla%2BpFyMtOmV%2FlOhPewTA%2FzLbG7S3PQ2ln6ZVuSSMfMF7tihySWu8aGLwDnxKShXZl0GOZk7C14bW2xJO2jM2%2FkSaUT2vhS3Z%2B6VJRuYyUHnx5LtTMc28H%2FufWvpSMWZg%2BlK7wU8hvRMr7YET2i2iYQtsM9HI%2Fzr6hffHWQSPRLX9eUOdqV7Wuo%2BsBb2RTa%2Fd5v36EjJzXojsCzhYJCSjPs4409g18aCzWCC8Osksk8bONtdfOoW0J%2FLtgWW195dvHjaog1LcrOV2sK2iT2Y8nJwCxxjS8Z1KqeVpSb9V8zwChMbcqaij4gq3mLTbNlr27qm4Yy39z6IaeMiKzuEll3OHkcAsCGIoJbep6YC2ChtUyFro8qZ8MLvn6LwGOqUBzuqGDBWKJ3yim7cMGU4RIB1INqhUbd5SG7tcdWG6tmNZBv8aDt8LfOsLBWubQuSgr9KDFHg%2B1oP59XWGAl73O3k561iSzGDCs%2BqGgBbzQncjw5yzLDstybvlwgcwXJ21Jp26IVC8OULIJVZ125k5oVxGNW05iS4xD%2FNWCCuY7vQvCpk4Y2tmRvzKaYgXxACzG7AuidbfAjcusJUwbLM0PCJM34U3&X-Amz-Signature=853c76344805dc5f8b6c67d0fb04daab74b51da56ffc402bf9b78928bb271941&X-Amz-SignedHeaders=host&x-id=GetObject)
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