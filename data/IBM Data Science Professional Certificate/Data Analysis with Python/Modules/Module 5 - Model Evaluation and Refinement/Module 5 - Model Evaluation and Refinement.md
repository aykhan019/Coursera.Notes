

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=924ae05beb358c482f9d38e71ae571913c5902d7f76d92669bc280cd7e4df8d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=61d3481468a652f470d968702e68c12a44c05cfe941ced2fd837089f580f1667&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=1d138f5a24754abe94c9acb75aadcadd1b03ce92e1c0e5b99dd42ca8b985e5e7&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=27d86f782fa2cb69c7e0c725b688027d4202ff1920b2ab846d35573cb2d35162&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=86614afdc0e617353d5f2263800ce68e1311bd1a1d2f169a6c8b6c92c2f0957e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=68539d03464917dea0ed791ff8104fe7d0834ce35783498740b473306309aca9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=d4e4cff898b2ddf5b497f109a6610ea2e99abe737198a95888b33176a82467c6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=1659056f20651e1b565b29439027d4249049f5280f16559ef8c3797c34689353&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=dbe62c828a816175565b01332eb01c5559c7ae76fe70c96baa66062924fd43eb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZDYZYZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCDuekEhQelckO%2B9K%2Bz%2FjhKbiZceDm42LGNnLOsorEi%2FwIgWG6JijaCF9UjaYdd9UA9yJ1EpErOyQ4mS3QZ8MkA6r0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLq2bgxUuPmVx3MqryrcAzkbCUCfHWRkfw5oDqaiedt45Wc4g9EwYajoWhAdBPcC3SkfaaK%2BRZ7HQCbtcWGWivOrn10m0xlwX70sjTskPmBO%2BNRlqjHYwTDD%2F%2BOCHxC571Gg2G9umXDnXOh7PmLf2d5rFPM2K4GHiUlranRCrv35Ygfy41DClbsAXCDrPyb5uPGr%2Flc0Xq36ZVGQuXrPrN4%2F9UW%2Fj4I39llh43J7TqImgp1I4rE98sYMK890aD%2F2pO7fdsPi6JOYfnQ9z2Fa9VYCPj%2BZdF2GWo7BMdBcssx%2Bn2SSYrM2yIaC7aWayWhSAQ1nd4j6YfgaPqUnHKn3yP9UfxhxySsPiyQPZGkN10UmFlYWnczj587fQZWeZ6Dckfveiz2juDkWE0fDx8H5Yy3RTOHVH%2FQzCh6ea%2F4sD5oGmtXgn7Lm05qM%2FRt3LCVqpnbLm9%2FjVoVOek9bpB1nPDtFFaOpIdASflYMC5T8ZmkZHx1pEdQqlhPdQ%2FlgZJ8ZM0%2BxZzbe7SArJ0erP9Xhq9vQIoi2SE0DReTr2UT3SmWszbSLd93Rj04IV8dwp%2FruTShc49xXSrWr3AXGPsN3ewURS7zWz7S9xfFmoNT%2FAb%2FzvvelaTSlM4UH%2BLLLL9B3tCXhaHQZqtO7ZdrsMOGThb0GOqUBC38OjV7Bs3XpizfUk9MF58pf%2BHEADLarM13FkfS73f8flBfZTdD3w2puR%2BNc4zY0bpiDxnHYHlRRgjDg8AWHEPrwUfFgcS5FLJVkRlKefVzQ2tPkZDWp74p6h7S8l2b%2FnNYmyvxlSfmXPpkboZ%2BAk13Zu5rNY3gVBqW0YpKhEaQJ0bAtRNQ%2FxjOMjHKBBvmSW5g9n6Fpj869ZqQ6Iq5iAhpDAURN&X-Amz-Signature=dcf6efba74ae78a33af7413a3eb3a9ebb5dedad43df674111c94efa648d68882&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZDYZYZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCDuekEhQelckO%2B9K%2Bz%2FjhKbiZceDm42LGNnLOsorEi%2FwIgWG6JijaCF9UjaYdd9UA9yJ1EpErOyQ4mS3QZ8MkA6r0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLq2bgxUuPmVx3MqryrcAzkbCUCfHWRkfw5oDqaiedt45Wc4g9EwYajoWhAdBPcC3SkfaaK%2BRZ7HQCbtcWGWivOrn10m0xlwX70sjTskPmBO%2BNRlqjHYwTDD%2F%2BOCHxC571Gg2G9umXDnXOh7PmLf2d5rFPM2K4GHiUlranRCrv35Ygfy41DClbsAXCDrPyb5uPGr%2Flc0Xq36ZVGQuXrPrN4%2F9UW%2Fj4I39llh43J7TqImgp1I4rE98sYMK890aD%2F2pO7fdsPi6JOYfnQ9z2Fa9VYCPj%2BZdF2GWo7BMdBcssx%2Bn2SSYrM2yIaC7aWayWhSAQ1nd4j6YfgaPqUnHKn3yP9UfxhxySsPiyQPZGkN10UmFlYWnczj587fQZWeZ6Dckfveiz2juDkWE0fDx8H5Yy3RTOHVH%2FQzCh6ea%2F4sD5oGmtXgn7Lm05qM%2FRt3LCVqpnbLm9%2FjVoVOek9bpB1nPDtFFaOpIdASflYMC5T8ZmkZHx1pEdQqlhPdQ%2FlgZJ8ZM0%2BxZzbe7SArJ0erP9Xhq9vQIoi2SE0DReTr2UT3SmWszbSLd93Rj04IV8dwp%2FruTShc49xXSrWr3AXGPsN3ewURS7zWz7S9xfFmoNT%2FAb%2FzvvelaTSlM4UH%2BLLLL9B3tCXhaHQZqtO7ZdrsMOGThb0GOqUBC38OjV7Bs3XpizfUk9MF58pf%2BHEADLarM13FkfS73f8flBfZTdD3w2puR%2BNc4zY0bpiDxnHYHlRRgjDg8AWHEPrwUfFgcS5FLJVkRlKefVzQ2tPkZDWp74p6h7S8l2b%2FnNYmyvxlSfmXPpkboZ%2BAk13Zu5rNY3gVBqW0YpKhEaQJ0bAtRNQ%2FxjOMjHKBBvmSW5g9n6Fpj869ZqQ6Iq5iAhpDAURN&X-Amz-Signature=656621c717b7d7bc65b81b71c09998bd1a71937b099dbd5c2c23adec2e7790e4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZDYZYZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCDuekEhQelckO%2B9K%2Bz%2FjhKbiZceDm42LGNnLOsorEi%2FwIgWG6JijaCF9UjaYdd9UA9yJ1EpErOyQ4mS3QZ8MkA6r0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLq2bgxUuPmVx3MqryrcAzkbCUCfHWRkfw5oDqaiedt45Wc4g9EwYajoWhAdBPcC3SkfaaK%2BRZ7HQCbtcWGWivOrn10m0xlwX70sjTskPmBO%2BNRlqjHYwTDD%2F%2BOCHxC571Gg2G9umXDnXOh7PmLf2d5rFPM2K4GHiUlranRCrv35Ygfy41DClbsAXCDrPyb5uPGr%2Flc0Xq36ZVGQuXrPrN4%2F9UW%2Fj4I39llh43J7TqImgp1I4rE98sYMK890aD%2F2pO7fdsPi6JOYfnQ9z2Fa9VYCPj%2BZdF2GWo7BMdBcssx%2Bn2SSYrM2yIaC7aWayWhSAQ1nd4j6YfgaPqUnHKn3yP9UfxhxySsPiyQPZGkN10UmFlYWnczj587fQZWeZ6Dckfveiz2juDkWE0fDx8H5Yy3RTOHVH%2FQzCh6ea%2F4sD5oGmtXgn7Lm05qM%2FRt3LCVqpnbLm9%2FjVoVOek9bpB1nPDtFFaOpIdASflYMC5T8ZmkZHx1pEdQqlhPdQ%2FlgZJ8ZM0%2BxZzbe7SArJ0erP9Xhq9vQIoi2SE0DReTr2UT3SmWszbSLd93Rj04IV8dwp%2FruTShc49xXSrWr3AXGPsN3ewURS7zWz7S9xfFmoNT%2FAb%2FzvvelaTSlM4UH%2BLLLL9B3tCXhaHQZqtO7ZdrsMOGThb0GOqUBC38OjV7Bs3XpizfUk9MF58pf%2BHEADLarM13FkfS73f8flBfZTdD3w2puR%2BNc4zY0bpiDxnHYHlRRgjDg8AWHEPrwUfFgcS5FLJVkRlKefVzQ2tPkZDWp74p6h7S8l2b%2FnNYmyvxlSfmXPpkboZ%2BAk13Zu5rNY3gVBqW0YpKhEaQJ0bAtRNQ%2FxjOMjHKBBvmSW5g9n6Fpj869ZqQ6Iq5iAhpDAURN&X-Amz-Signature=89ab871d0234783339b851fb39954ac93a2323de805dfe66653dca3cb1d95494&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=0b6b14d109875ca5ad1956f968aa602050c1002013c57e15d6529fa0ae095ba7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=2bd4be81760fd214647b9e0e8bb621d7f9cb50968b47e812f7bd26114551bb5b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=9c2253fe512a77e6ef94a4e7562e0978972d6aa9ac3118a9a967c0567b96d09f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=0364117dc9061f6006736b26c75fddfffa45188dea701a60f5c3a3087423e8c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=6d36f3e6d916f3cdce891f06a7ee7a03f29b16914e839988404210467fe1a0e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3WV4PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIDaiBDYKoKGm5ptcm22BjY9P9%2Fj31y8XznKnIyZnR1ZUAiAGGoQvR0bjWX6dPZDTYi%2FmDCXGbS%2BUjAqOQU013ltKdSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEdFKw1di7BVqlJkHKtwD09SifKUX3HN4Z4XQQ7l97Cgp%2BHifZLEeVxV5mYRSlB%2Fd1kaXi04gem%2B5hDhozIL4f2vwsaPJLYaO%2FEjG2dqqUx%2F92VzVf7sH%2FcQjrC8bDe9Yb7477exfpcRxGQSCcEJx8i81HRLAjZ3%2FbI8rP%2BAq2ytQM%2FzEnbFpGianZNH2Q%2FKLflUbrKzuSGC6r2Csj6I4KaN%2BXDH4iSbgLVjoPGVJMS0emBVgjY4sCR3FUK4QXMSlVBestBAii8D5f1%2FH8zO%2F%2BCcMxpPsBFzstpj7%2B1UFiY6oo47ScuXkH8IEqqImTr%2FOQ3UPwpM2%2BlmhPmX7kA4aomnokJuM4vp5M8lIxgenuwa9FmshQ%2B7QSscZ1i2UgGXS9Fjwk7vZ6YgDJCqDTPmJRwPHsYoR2S43SGbemBWNQqTirM2fJ7H%2FxOZ2WR8AuIuxfiE1YLuxV2rnOBu%2F%2FL6UQctvw6wed075xDQ91MBVBzlNiBRfaMiA16gQ7cgpKFQ95CYULqi6z3eN3O0dIlzIjJTaahRnGz8dWt0CjS16kwVIkMbo4o%2Fl34pIbKRzt7mtSPfq%2F4ujSqhmBO8EmZkrgwH4pIAgVwy0m2cBeiBupq8yexilDGP6CePjb%2BFYEADZ%2FB82q5%2BID5UPxPIw1JSFvQY6pgGESTXRytwF9NpTgG9V5vamPzhDb8VQgaHQ36m8%2FDuAG%2BAGhZf%2F5nfwipyyfluWgLMpXvJsFj2YGqQ54XzZYJQ5Jsdj9AE49wFUuIE8DglF4YwQyKG%2BrH7ye1cBz7QJYbvW4h91ORxz4asAwhHHotwwdXq2aQ2Ewk2c5AsfGOxs8j2veshg2QD%2BzIppm8o5p7vAi6p%2F%2BKbCtI%2Bv3efYY3%2FHO%2B48Ehsj&X-Amz-Signature=1a463ad49622e0452830591ceaa85bf6d9460315dabd010bc9474ce06b87bdcc&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWNWTBZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDyOUz9H8OsKx%2BfnWflnYbXnOkuhGwRKbUSj0hHtn3BlgIgH6gDaFSi9%2FZRRuUpYRu0r9sJ484aLr5UrB5dhqUkuGgq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEdfaByqvU8CoJsxNircA5MTXxKNYZFFgCzNs656yVxlvzKViwFj%2FHNbqRwLQZpxyOcV%2Bl%2Bf6X9buXtZYMWp6e77dLJ1E2wSTh4Fb2tpQOsgcKNL6M7ZoCxFPM08B5eE3YlCU9Dg2QicrHbZer42MqF9RWhNCIXd5e4b6V3%2FdpiaGX7u1%2BICu6jnvgWUEKy3ao%2FLZ1XGP%2Bg0p6YOWsNrA1MLqgRArHO6oYg3NQ%2B8gZA9hIxGCoC%2FWdK0EbjA0ZPN8puxy%2BlqdqHMjz2epbBAcbpfxwJR5hfGrESkwTMcEiKgrt78xHKxvM9k9cNvOSi0ksGqoofIxWpb23f%2BdukXrlEgT11aEASDXcE8SNPhlr1Lcj79%2BXl8%2FdeHFu3YStRQEXRafbAwgfNo1SLtt5sJJObVWStpEAYJLgWfTS26K6RA5tuOPn7A%2FEWcVuMujqJ7HUwqg5R7MiPl9yjVCxNTcrw9ENF5J0Qpob3vkRMNPOM2qjy%2FjrcEFIVKmcPh2W%2Fgzz8OMxKV8hDAbf3ZTCUlDgNPR8VAZPIlU2USEYT1H6urBj3EGjgnWecb7BK89wUBiTIqka%2FufEwueAyAC4S1s95dQE%2FrsH1BOC7xrq79V94EvBlaC6gUAE3g9tN%2Fg7oXNnk6KrQ0PejOr9l0MM2Thb0GOqUBq%2BXQr5a%2BYL2aYyLNAE5k2HxNAyVTL3Bo2LXkyiDPNcXftln43tMdL68K1M5GEsGzEFYo7d96Po0qwSC1M%2Beoy2JdjW5VB3mJGDattFmUr3PZUXyCrPBXqYASknLvFDFqMd4%2FJBw4Z8WL%2BGJbXpNjQ3qz3sqnohw%2FZ5wl%2B%2BzUFzFrhVH5akj7YLvueRNNW8Ufq8MxjVtaVV1gOC%2BY5XQH9AoZuy3E&X-Amz-Signature=f6f2fb0ffcc7b643acf1ee3fcecb050472236e1a4eea2802f669a13d3ac3ce86&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWNWTBZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDyOUz9H8OsKx%2BfnWflnYbXnOkuhGwRKbUSj0hHtn3BlgIgH6gDaFSi9%2FZRRuUpYRu0r9sJ484aLr5UrB5dhqUkuGgq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEdfaByqvU8CoJsxNircA5MTXxKNYZFFgCzNs656yVxlvzKViwFj%2FHNbqRwLQZpxyOcV%2Bl%2Bf6X9buXtZYMWp6e77dLJ1E2wSTh4Fb2tpQOsgcKNL6M7ZoCxFPM08B5eE3YlCU9Dg2QicrHbZer42MqF9RWhNCIXd5e4b6V3%2FdpiaGX7u1%2BICu6jnvgWUEKy3ao%2FLZ1XGP%2Bg0p6YOWsNrA1MLqgRArHO6oYg3NQ%2B8gZA9hIxGCoC%2FWdK0EbjA0ZPN8puxy%2BlqdqHMjz2epbBAcbpfxwJR5hfGrESkwTMcEiKgrt78xHKxvM9k9cNvOSi0ksGqoofIxWpb23f%2BdukXrlEgT11aEASDXcE8SNPhlr1Lcj79%2BXl8%2FdeHFu3YStRQEXRafbAwgfNo1SLtt5sJJObVWStpEAYJLgWfTS26K6RA5tuOPn7A%2FEWcVuMujqJ7HUwqg5R7MiPl9yjVCxNTcrw9ENF5J0Qpob3vkRMNPOM2qjy%2FjrcEFIVKmcPh2W%2Fgzz8OMxKV8hDAbf3ZTCUlDgNPR8VAZPIlU2USEYT1H6urBj3EGjgnWecb7BK89wUBiTIqka%2FufEwueAyAC4S1s95dQE%2FrsH1BOC7xrq79V94EvBlaC6gUAE3g9tN%2Fg7oXNnk6KrQ0PejOr9l0MM2Thb0GOqUBq%2BXQr5a%2BYL2aYyLNAE5k2HxNAyVTL3Bo2LXkyiDPNcXftln43tMdL68K1M5GEsGzEFYo7d96Po0qwSC1M%2Beoy2JdjW5VB3mJGDattFmUr3PZUXyCrPBXqYASknLvFDFqMd4%2FJBw4Z8WL%2BGJbXpNjQ3qz3sqnohw%2FZ5wl%2B%2BzUFzFrhVH5akj7YLvueRNNW8Ufq8MxjVtaVV1gOC%2BY5XQH9AoZuy3E&X-Amz-Signature=6862b60772e1161d17b6afa38778956518a88beed9b14622db0bad3a957ceb92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BV7URTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCsrzKjNppopCuNY43QqBbWmjcEe191euzVJxbTaRA3KwIgDTnfAqvbJ2uJBhC5QlqYKFyQGvNHXpqqYJA%2Bh2vLf%2B4q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDDH4%2BooVF4cf%2FJOY5CrcAzd7DwC5bfwArfvAARhHVL%2FGJM5SDMTKxppGebFOTmYvhonFTck8xpK2jyl5XmSItWHIak1SC9dYn1pbOK%2FbAkShq9tzuvOItWbJJjMmXkhyJc94VCwNeraqZXPJaL8sKWkEDN0IIoZR0FJKpmELxLea7YV1C3MQVI6QYNLtpxw18UOlpdE3PbRzXWbvM6IZ%2BZEMnWGZNmwvPrkZ%2FFzXRNVlb3iw0oxGJldPgJtUKwythZ7S3vGnWe5vpD42fPPPwWF3yrFU8jH8INCu6BodMgMJM%2Fol4KJJcvkR1OtcrGkbCgFAn4Zl6egESzq8CAqK%2BN1dq2Cdwt9N%2FaXyY56F1ylfB3w4Soa%2F2iyWVk%2FNqb5vwkhdw0gM6WYjJuiY2FttEuP0nW1YTcb%2Fi8S3Sgbz6uRHc5qQdXRf9fTJruN593Y%2FaPgjB7%2FdUpziGHRiJ3TjsV%2Fh0Wo2pRokKLkZVGdeX%2FYONKEi2V8gUepZ2TY%2BusyPmSdwRSp8YNzF78sEhAf%2FEr%2BQYUMpI2emuqspZsO58OhONyABBSSzdv%2BTRnFoV1T8JPD%2FZxtJ6pXy7y63O3%2B3LK8N3Zwkh%2BW4ST17J7aJd3M65WZDHwcaFIJHuDAkwu8Yu8k9sDV8LZWJYd12MOGThb0GOqUBwxLSII8aJa5F72QzalxseCxDRgM%2Bc2KtGgKFNaULHI2og4BzxE1YUK8ZyHbaGgAGlFUpKbldVtmbbD50GPR4eThAU3sVdiEuJ6VrREQwND0wjRNdWqTLmvyvEtw2GCexYJcsCSQqfzESVJyZmeonu9IsGr2aFWYtZ%2FYQkYOqPgC4bX6dV4mXCmsci1falJWfi%2FxIAZAm3dV9HEwOnT%2FEWCV264XR&X-Amz-Signature=18bc331298db30d53b95fbd4dfc52b2a4ca57007c78f7b95d2412944438fa7c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKO73GI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIF96QqAcy89sjsXSgZtLXzKB57uHJfDNvkc7t1Jyq6jhAiAh9bVyQUmnEdh0dEn2YhHCpygnLeZQ8aDiWV6FHA91uCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMrlzD4I1emcWMZdRuKtwDxLUvIEvpfoggC45NTU%2Bq%2BAt2r06w2SfAL1lhGMJw06mmwslhb6pfDNMSuKdq8aeaHa6zhHRmE5LVmIccoW0RYjTUbq9fZW60Mog5enLM7zYk7Yn9arBnQzP6WNbqKA6E3LWwU4y1ZIKtBE9ra%2FPemwM641f1jGuyAtQn5VQTQ56lrd0RF25nnWbxwYsFuzRM%2Bmf6TUj%2FjQnpP0UbVMxoMMCluHF7TtzNwK5IOIm7mCJQmPIvDwXANqwHcd0D6pehPHlMeO3bzCu30j%2B8SIFugpqx8jGmpeTYmjh7uCk%2BeF2PChoV9W%2FlXwOIZsFjyLDVZOaNWsKFIg9RbTVm%2BI6dQTAbWF9pcpDbuwFCTlqYT7KN1swVFWggPHxESR%2B12TNZQoTUfR5VQRNskhnTFrkad%2BAlH4refhAg5D4flN6ptourzeHM7XK59PZ4iN2%2BGYq%2B%2BUhWj%2Bh14s7HChmnZAoWQlsPvFEVzoExxsNpICbDj5M7p8i8PTzT3qhq84qakUtDcZhjvv%2FanVAjmAlro3Ol5KHnJpeKThLpz66yKa42lpVUyJLqq6%2F0zfZY1rTqU7uT%2FpCnQbpT5tXhKiGQ9FNfVn9%2FywbkWsN8Q3TkU9hWUG2pLKCIbcXBq5gx1BkwhJSFvQY6pgE7QFfkUZQ1QS5EChJ15h1GOrjQjWQnnfpSQd8W7QI45oSl14u1zsIW1So39Kl0DCW7LGuoOMhL2D02iWIlbY9293eziQA4TXHAnk3zxHhvCYgxL9VQezl5h%2FeQMId7d2dw%2BobZkX20AjniLn18dxc8pCfuijNMWLD5HCInseDkG8nw4%2FupESc38gYdPO%2B6jJnWTMH0a3PX6%2FmlAfQC9%2B3NL8em82wJ&X-Amz-Signature=5e7e23edde224e9ae4ba53202f1112bec1390106566614eaa86a2630b9b5de91&X-Amz-SignedHeaders=host&x-id=GetObject)
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