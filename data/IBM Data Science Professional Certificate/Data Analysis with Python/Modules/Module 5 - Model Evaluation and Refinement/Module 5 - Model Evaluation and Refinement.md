

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=ea9bad49a1d696beca76ed0e7edcf394423eb18414a2da9b42573d4facc6e9a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=2647a02289d6a8ca8cd1c175b2aba1d623f1471656f2d3574bbf4fc8e9332306&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=01f3d95dcaa29b19d2d62c984c921bd1a4a7a00541a07a8a752093074b8ef94b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=ff149a38efd42b0503e0438b3acc3f2d19efa0f8142c13d8cb9290e19e29fa35&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=7eb8d3fe02f6feb1d36e0c4fd222170f4d1d3ed108a292adaf8b031a32d9b934&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=b8514ee2b6974b2280d8eefee7011c935137f3c6748ae4385c4cb0e63e2a1c93&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=6a317f8a904d2bde0067fe94063831f51fedbbdc2b64b55899ee6434108035b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=ec589f94d52f91a926564f21b32d2ef7d2c8a6afff5f63a37c264dc94b3b852e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=3d993132f08be525826fa4db474aaa1b11eaed2d0a0a3e43ab96333e52e568c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P74E6V4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCbN734rOmkykFz0FW%2Bum7q%2FG9NwO%2BJiSnARPy3BwxwoAIgPAu%2B4F0Go2BQiY5kmxc3UxS%2Bqlj4VKxwhCwm%2Bn0QbW0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGqLUmV%2BTpBe%2BRuYOircA3ia%2FJdks9T%2BzMySRBTQ8vpfASJEROCtrN2gSNHiuZp5YO8MsDQ8Yn0hrj2XrWsEef6ZLl9g6jlax27oVthlOQ98DZ0cyLH%2FdQDB4%2BFSA8PWv8F%2BlGl15t9rUSGR%2FFaHHp%2Fg74vgbTWG8XYYPS6WczThm%2BrOkxdO%2F0f531yCwHjvfXZFmE1Ia%2FU%2FHxESbTxt%2FZ8x8tJzs4Y%2BMthqby%2B06vwrJEW7JmpvlK0KPTqvuPlLqny8XjXd62yeAr%2Fawb4BMBi3wCggoYESbRH5PSF7BVLN86GAStyirMG0FzRVNfOC%2FJ6odWC3%2FfPCW3kYdO5%2FbIsTSUVnXN6U6YXnpVGTfSdH5G2YyUZ%2FlsR%2FLkq9rHJXPx4SPAj42OByl5tFuPZW%2F4EUzR%2Fd9ek7O6Wod%2BvX%2BlBvJqLeKOGcMQh2VOTs83VB%2FZQenoBLwsSLIJENB4P6XlCEyM0GqnV%2B8EcxHK6TDzp6s51T9f5mkADk%2Ffwc2fgRU93MhBC8603E32OU5JxjMprbhtHIAlRKn0DIelzzqsJt92tETHFtSTKyoqjxCIZvFybiSbLIpwj9xzh5UTteR0o1bNXgEkCdisiSXzjOuWWJEuuOB7ULguJPTtkNsR2gbzZ2DrZt%2BRt4O9ANMInRk70GOqUBykTLqWRRcADv01VXJMP3m9f06beJXS3%2F90ignCPQVRJOxhWWboFct4VTH%2F6CFQ5es8H6uwrfAxrWzs%2FZPQYun9uRxAoKYkLADTgjCnoV4NP0pAH4O7xRp1a8eCoQPN2VgmdETlOVgJSKVts0%2B8U1EZv5Y24gdeHhtrXg0KeWelvTm9lGpugIwfSKTMNSmK%2F6tMAoKN8xBHtRDXo75A6gYPp44ki1&X-Amz-Signature=9c1be8d9400b2caeadeea21ff484e84419e3b05d1d48542576bbf190ae3c7b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P74E6V4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCbN734rOmkykFz0FW%2Bum7q%2FG9NwO%2BJiSnARPy3BwxwoAIgPAu%2B4F0Go2BQiY5kmxc3UxS%2Bqlj4VKxwhCwm%2Bn0QbW0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGqLUmV%2BTpBe%2BRuYOircA3ia%2FJdks9T%2BzMySRBTQ8vpfASJEROCtrN2gSNHiuZp5YO8MsDQ8Yn0hrj2XrWsEef6ZLl9g6jlax27oVthlOQ98DZ0cyLH%2FdQDB4%2BFSA8PWv8F%2BlGl15t9rUSGR%2FFaHHp%2Fg74vgbTWG8XYYPS6WczThm%2BrOkxdO%2F0f531yCwHjvfXZFmE1Ia%2FU%2FHxESbTxt%2FZ8x8tJzs4Y%2BMthqby%2B06vwrJEW7JmpvlK0KPTqvuPlLqny8XjXd62yeAr%2Fawb4BMBi3wCggoYESbRH5PSF7BVLN86GAStyirMG0FzRVNfOC%2FJ6odWC3%2FfPCW3kYdO5%2FbIsTSUVnXN6U6YXnpVGTfSdH5G2YyUZ%2FlsR%2FLkq9rHJXPx4SPAj42OByl5tFuPZW%2F4EUzR%2Fd9ek7O6Wod%2BvX%2BlBvJqLeKOGcMQh2VOTs83VB%2FZQenoBLwsSLIJENB4P6XlCEyM0GqnV%2B8EcxHK6TDzp6s51T9f5mkADk%2Ffwc2fgRU93MhBC8603E32OU5JxjMprbhtHIAlRKn0DIelzzqsJt92tETHFtSTKyoqjxCIZvFybiSbLIpwj9xzh5UTteR0o1bNXgEkCdisiSXzjOuWWJEuuOB7ULguJPTtkNsR2gbzZ2DrZt%2BRt4O9ANMInRk70GOqUBykTLqWRRcADv01VXJMP3m9f06beJXS3%2F90ignCPQVRJOxhWWboFct4VTH%2F6CFQ5es8H6uwrfAxrWzs%2FZPQYun9uRxAoKYkLADTgjCnoV4NP0pAH4O7xRp1a8eCoQPN2VgmdETlOVgJSKVts0%2B8U1EZv5Y24gdeHhtrXg0KeWelvTm9lGpugIwfSKTMNSmK%2F6tMAoKN8xBHtRDXo75A6gYPp44ki1&X-Amz-Signature=5aae4fdae5c62a47189c611a49466bf35bc4c4f41032a3bdff1d16e9c4c8110c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P74E6V4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCbN734rOmkykFz0FW%2Bum7q%2FG9NwO%2BJiSnARPy3BwxwoAIgPAu%2B4F0Go2BQiY5kmxc3UxS%2Bqlj4VKxwhCwm%2Bn0QbW0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGqLUmV%2BTpBe%2BRuYOircA3ia%2FJdks9T%2BzMySRBTQ8vpfASJEROCtrN2gSNHiuZp5YO8MsDQ8Yn0hrj2XrWsEef6ZLl9g6jlax27oVthlOQ98DZ0cyLH%2FdQDB4%2BFSA8PWv8F%2BlGl15t9rUSGR%2FFaHHp%2Fg74vgbTWG8XYYPS6WczThm%2BrOkxdO%2F0f531yCwHjvfXZFmE1Ia%2FU%2FHxESbTxt%2FZ8x8tJzs4Y%2BMthqby%2B06vwrJEW7JmpvlK0KPTqvuPlLqny8XjXd62yeAr%2Fawb4BMBi3wCggoYESbRH5PSF7BVLN86GAStyirMG0FzRVNfOC%2FJ6odWC3%2FfPCW3kYdO5%2FbIsTSUVnXN6U6YXnpVGTfSdH5G2YyUZ%2FlsR%2FLkq9rHJXPx4SPAj42OByl5tFuPZW%2F4EUzR%2Fd9ek7O6Wod%2BvX%2BlBvJqLeKOGcMQh2VOTs83VB%2FZQenoBLwsSLIJENB4P6XlCEyM0GqnV%2B8EcxHK6TDzp6s51T9f5mkADk%2Ffwc2fgRU93MhBC8603E32OU5JxjMprbhtHIAlRKn0DIelzzqsJt92tETHFtSTKyoqjxCIZvFybiSbLIpwj9xzh5UTteR0o1bNXgEkCdisiSXzjOuWWJEuuOB7ULguJPTtkNsR2gbzZ2DrZt%2BRt4O9ANMInRk70GOqUBykTLqWRRcADv01VXJMP3m9f06beJXS3%2F90ignCPQVRJOxhWWboFct4VTH%2F6CFQ5es8H6uwrfAxrWzs%2FZPQYun9uRxAoKYkLADTgjCnoV4NP0pAH4O7xRp1a8eCoQPN2VgmdETlOVgJSKVts0%2B8U1EZv5Y24gdeHhtrXg0KeWelvTm9lGpugIwfSKTMNSmK%2F6tMAoKN8xBHtRDXo75A6gYPp44ki1&X-Amz-Signature=011bc0e45ccc7b781ffb06d340a5fcdfda6327cb9ae40afbee6c3038d5e2ab90&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=99b8d89faf0c035d6a2432dd01cb5210439f0ef1fe8a96a4d9c5e5a84701db20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=96a16c27d0105751360b41e3c57298f5116bb2c2efb19491009ecd235e01b2fe&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=660af56c7317b606229dc57457a78d3f07e18cbbf6f94dd01a1385826a4c2e23&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=4b63cefcb9087378515a2b6b709e088b0d850271060ee32b5103e882a947fe5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=405eef85bc3a2a3f8c856a6c372b04508df2f521d2a08fd4dd5b31661420e428&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAYLBD4B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQD1knZB9vELq%2Fkq7FNADE9rqUklFG4Su7u9T2aI6ZdDggIhAOnr5ycf9oMndiZj%2FIzO%2FTs2LZC7lXlugHnUHZaGNY%2FoKv8DCGIQABoMNjM3NDIzMTgzODA1IgyrTPEWquaZ25tXj0Mq3AMeRdGlKKn4%2Fj0OGdF%2B0qIBQvHAk8wFuw6ow4feFrUUayJLpZ0HHQ%2BC%2FyGYfdFWKaJGlPtBeUgjulGnzAPnMwaw%2F5wYIRKDoN3MJazn3NHbnzL%2FR4q2qK0fEJK6B9mCy5v5zUvSXP3Kb1%2FWoENiWF5qySViLixn67bzL%2BYynLjNW%2FGjFZFf234e3Q7qmuMlY%2BJ9wY1rTVbcUnM81rjjsMnog8Sd3%2BXpo4eHk2CwD5FTYbPK4QKK41m1Xi2aOzX75G%2BWh3wkeXFRKr4aXm7qrudeorbtOmmaQnSsWAjQ5bBAYbJV5EEohV1kuijF4TlHCHNimdmuixNLlRhEOQWjb%2F2Tl7GQ8lxkJ3H%2BxemQt2pRyMIOB2mXaWlC1AB8SMsSFo0ESCHroi1JCPbevRb8d1NGhwKcaw8IsCbJHqjeexK2Yt1ZiVPLOlgBR8PYWwG16BkFkqF1QRQuR3QV7W1iXJOTLsySl2nqi3ir6rXJORTYGZCS7DydD2rw9EMfEgJtwWRuWY%2FmrG5iqcqtqQBaHdTawL1HzjxEWBjWaCKFkqdSM4C5j5F5gTQBAJdaw%2F1sQqqY75FvBZRl2rdMZHAm1aTFnB5IkPlutaymy4QDj8fvBk4JJLDiXEFQfY2uiTCb0pO9BjqkARCe5TbwcryejUnyb2kUxNweOr1jKXU36n2w7BBDR8Dz6iBNidaaPmDBp%2FgOVN2uxj3nQWr3CvaAEhNjc72KsYxlQBTrpOKs6xwli2xZm%2BwdAnffTcvAMLMz4KdcHlxew5o%2FK3kprf0GPe9sd08e5R7GaHkD7NvYWGC0F79eKT0BZx0YfCyf2z6ZiPqzbaTro8n62LrktqWS19cwwpuNhMDzSrjM&X-Amz-Signature=c3dc6439304a827bb14435ea9ed2bb2c7a802737fc7fdb6fb9cbd6aa00ea0131&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y472X4PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCPDcRAwmcA%2FSqG63q9yOCRhiciQ9SM5uNAPUFuBwJX0wIhAL%2BK%2BHC%2FbhhoG942xuUYx7gJWc%2FLHqEvopTIUmM508e7Kv8DCGIQABoMNjM3NDIzMTgzODA1IgyHBieVOJHAdE7pHiMq3ANJdJ%2Fd9e004LJOQJzih4ywRyCAsR3CV%2FFZ7PxZhOdpuDLs42EkusCUAML6YXFpdT4BzXc4II7DiIcb9zNP4834yIbotAln0in78Axbrb7G4F8ecD2jNHOMuzPyg6YmhqQ1LZidvGBP0OYwpu6Uu08Wxa30S%2BNwX2iB%2FhMeuK%2FSiLmWGZ4GY50UnAgRzBzvHCXpCelz3qx1n8DRbVgCwYnVQIX7jIaRnn30tn%2Fmn2Zu5p5RgPQjS15QznKvP6ieVTotk33evK7k7hZ%2FIMNt4%2BieaBCXz%2F%2Ba6HNAmysSBQzdYJoRIoosda6e0kfd1py3Ypi7YDBkArut%2BkoSVPKEp8mWp9%2Fg0nAmFj9GyYHP0SgIR55%2BvSv94osxNNUuGNgddiG1BbDpeVgCpXEYZzJKEhSVSb6GImfhce1M3rMBqK%2FgkjGdEgfmAgVRlnMjwkNhwmA0LYKtSU8ZYJ6%2FO%2BSC6iMkPciQtD08IE6rmKazYtVbk2aPRu4MxyxOUjbuy7PovKqTIvCKp8m%2B7joKTyziHwH%2Fjc38iaipDVzUSua%2BKPKXaCTShE4RJJtAT0ANNHikNLSa2UDultOc6thrJr5dqCulqIIRiXnsXzEP3iNCFzTj2l36dvfc9sIEJDvwJTCl0ZO9BjqkAd0V1B1EpuFzJ0YC8hVw264paE4%2FyfhFaBgUL%2F1xEx6W%2FrA5f2NuhsbekaKSUwrgwLmnSK0m6z8asrHbP6E9mPulIJ9AV7kIiGbUlAgEVg4H%2BulUDJZIsG5LMqe650hIFtXuxu2Hx4nyAwg%2FYVSHV6lIauvWz3OqogGI%2Fxtpcm8S387SQzMwBMkO9LUGwGFO%2FReZECEMvFsO8Vc4zYvkLqRmeMKg&X-Amz-Signature=17e4fe5eb6076d802a8371e0850e4e53f247e2e7cb949a186f6329e1b80f0923&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y472X4PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCPDcRAwmcA%2FSqG63q9yOCRhiciQ9SM5uNAPUFuBwJX0wIhAL%2BK%2BHC%2FbhhoG942xuUYx7gJWc%2FLHqEvopTIUmM508e7Kv8DCGIQABoMNjM3NDIzMTgzODA1IgyHBieVOJHAdE7pHiMq3ANJdJ%2Fd9e004LJOQJzih4ywRyCAsR3CV%2FFZ7PxZhOdpuDLs42EkusCUAML6YXFpdT4BzXc4II7DiIcb9zNP4834yIbotAln0in78Axbrb7G4F8ecD2jNHOMuzPyg6YmhqQ1LZidvGBP0OYwpu6Uu08Wxa30S%2BNwX2iB%2FhMeuK%2FSiLmWGZ4GY50UnAgRzBzvHCXpCelz3qx1n8DRbVgCwYnVQIX7jIaRnn30tn%2Fmn2Zu5p5RgPQjS15QznKvP6ieVTotk33evK7k7hZ%2FIMNt4%2BieaBCXz%2F%2Ba6HNAmysSBQzdYJoRIoosda6e0kfd1py3Ypi7YDBkArut%2BkoSVPKEp8mWp9%2Fg0nAmFj9GyYHP0SgIR55%2BvSv94osxNNUuGNgddiG1BbDpeVgCpXEYZzJKEhSVSb6GImfhce1M3rMBqK%2FgkjGdEgfmAgVRlnMjwkNhwmA0LYKtSU8ZYJ6%2FO%2BSC6iMkPciQtD08IE6rmKazYtVbk2aPRu4MxyxOUjbuy7PovKqTIvCKp8m%2B7joKTyziHwH%2Fjc38iaipDVzUSua%2BKPKXaCTShE4RJJtAT0ANNHikNLSa2UDultOc6thrJr5dqCulqIIRiXnsXzEP3iNCFzTj2l36dvfc9sIEJDvwJTCl0ZO9BjqkAd0V1B1EpuFzJ0YC8hVw264paE4%2FyfhFaBgUL%2F1xEx6W%2FrA5f2NuhsbekaKSUwrgwLmnSK0m6z8asrHbP6E9mPulIJ9AV7kIiGbUlAgEVg4H%2BulUDJZIsG5LMqe650hIFtXuxu2Hx4nyAwg%2FYVSHV6lIauvWz3OqogGI%2Fxtpcm8S387SQzMwBMkO9LUGwGFO%2FReZECEMvFsO8Vc4zYvkLqRmeMKg&X-Amz-Signature=64125e91fae7c0709e7878be3d9c05bf5cd19171ec07ffdafb9ae6b94280dea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVJDRY2H%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQClJiAf0sdUyVZnHc%2BQNf49g13XGwY65j1SkzSf%2F2YCXAIgdKleIdRFdmgYUWhO4k5OaVS%2FuFJwxs0n%2FNWgQfsiCqgq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPfifii%2F86zFMB2LircA%2B1hMxkzsaj4aVJhCkYzpDfUZ8%2FMkMImr7qfMp1NRmoYFjTwWHwVTbcq9ve32gsYTQCT%2BUM%2BPkYc71PYee6V%2F6DvGMqs9Sl7pDnxHdapTW4K36NgeMVPhI76AEvTtX3ldTt4jhoaY38aZUgwmskCUoQhQxF9f7u1v%2BMt5UKslTt9gLlddoXWId5VY9aeeJ0TrkXfd1mwsTQy99IV2TCuRzQICtyU4LaCrTmf1ktUOvoNk21zdOBTG1yR7HUucherkIsTZVobnUQpedO4fCCyvc8Uev1mwbPoNi%2Bz843mDjd5vY0F751YtFOyEMAnCB5%2F%2B2OjpMNTFI7A4JD4OsorRIyY4Ba0jDxd2RyPAhuJAIZBF2P0uH2qMRqR463px974GxqpAonaEPmvg3rsUU2tYpBkLiGJ4eGZva3PIqrwamYKlfDKULCa6Mbkb9qO86Gnuh01X2YotkRaM2bWBBbAZyIQY9dBxFl9hfnUj5t3%2BItixBe%2BSeqOCHGVPUJTNNDT20gPLNx7GKMXXlZWEf884bStPAJXa2OxJf18ZnXRG20OZnwpEVs9wp2FZYebG%2F2Fv1xdcW4JI8m8kl%2B%2Ff4CAw3s%2BKB26x2780Gx38lusmi9jdrDGDWpSl8oed5rXMJzRk70GOqUB4lsj0KJsVAPOQx0470PvH5HYQiwnSZi0qrIg2Qn6iNiV8tZq%2FihTDJ7KJSAES2gzurjNL%2BdmlMpK91zVd5Y3Bo7zzs48slNffLRI4TMhlegTgQea19NKxJ7gW5QlQJkuix4npXtTiStq69qPx6OwwgNbgDHhkERDgYKUz8buDq3rotyWhFoypmz8mO6jSDveOLXj%2F17HtCL%2BjtErCZqvru%2FuHEMe&X-Amz-Signature=978586b82a1277533a7c11ee6e6d6d0094e5ca4686408276d8fe3722244a74a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFAWJO64%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEBWJiOeqTRGsUZXIms2kJs06kJOTw9XoNqxGG92QxZWAiA%2BrmcDULfiWReXBiDPJOGRwmeoAueq6YVSgAmYH0lyDCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMYhf6YcZiLzCi8LZKKtwDBOAaFiU6iX0GzXp6OlRC5bSofVAy4RFuEoDExFjI5rvNtkmn4geGxUJyp8Vph1IwWK%2BO4mAqMxX%2FFmw%2F%2FweJwOf9JLN%2BNm1KD%2B%2BGsAZ82mtukJFe0We1Gb7ac9iPO%2F1jYkQfPriFloB2RRoZf0GfteoZKuLBxmO0dv4V8SOEB4gXtm4vsMIFEoCA0jF3%2FPsEDW7EBAkFelPehcw1cJXpNX8ubwnZGImRvbitRTjAgaQyzJ55HMMMKY6R%2BUJFcvbPga9FemaIDsO1E%2BUIzp5J80B5XL%2FnAFdVAcPU%2BSXh4zHOFBCVR%2FwdQDHJyKJRVU1FiKfZfg0pA0QypQbNjYHi%2FZUoXpDPuX75D6uc2b6DhCAx6eysaGd%2FHY%2BkHJqL6xHqste2%2F0ZvA%2FoH9apFvUxKtjxxkpCCjfLbpY8llr4gFAQndJo163aQtby4H%2BzJpPKsXVHZLo9GMm2wtS%2BwlPWrYs6ESCCT2EXEbrkyoed7BDS9FkMqCDeJ6U1mBZCPvvACGkAwDjYpq45PMmdFZJpEilHKhcw%2FykbajcEAHvKttoyfRxVzJPbeyTAtwysiXyHFtD6W3t9FFaf6aiHzkRne9uMRaeLVXiD9BkWyW2tYij1TdEPDqG2Gy0h%2FOzwwwtKTvQY6pgHh2bvnXoIO1%2BJ4MmLy%2Bp4tSs%2BF4qxlwlmgGZDcaDvMDiYBNCypBB3%2BwLHNBq9jxNVv01KvT%2F4WbDRszJx7OgH8EeXNbMW8EKAXE3996M1jbIld7EpEBhuCPwVClPyD0GeN0%2ByI6iXYID8MZfgttOL7T3pbiQF%2FMy300w4r5ZF8urUZfU7DV%2FbODR64OQV5Jm%2FBztGWCYAX8%2Btc%2BuIJmRpzmCmxnGiG&X-Amz-Signature=e824f3d1311cde194c98148fbd5a3921e3648bf47e89d7c3e5879f9b91e1ac9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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