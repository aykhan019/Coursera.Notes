

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=c9b78d9ed8ddf04617f3526dac63e5e17ab08e311354d69829e24339194be56e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=9ad6820f7f9227963d22ee7e46622c4182c30cb9108d520168db7759884ea2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=52ebea171601fb9f2f28ec15efa5d29efa30b70a58eecd4447a6276832b8984b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=558c8bdaefc327160a0096136c1e4c5c0e8125cd6ce7308dea5c2bda68275885&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=032213cef05b05569714935b89ee5f675b63ca87795359e5af3676ce464a8f8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=bda6bff411f967e4b6fc0b0cec9c22c9eab9ff1c8659cd60d5c705ab7e15402e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=e70d70399f08c3bab64a00cb49a5b6252f1688ced3e5c69fb94fd54894aa9670&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=a970acb136d9447e35a1de4e9640be59f35c31be6756769878f8b59b5f74ea95&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=04e57f7eec54018b454e0604f2f0e4e433e4bdeafcd4599733c4036dd8b33d89&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQGALMO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPyKsB3Cese7s3KySLzHOUuvr5Q4a3G0OoZjo9Oj1ceQIhAOryrZLqODnUIR7VUnxr7J7JUpY6pOdcCKw%2BxkV9KtAeKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBxNnjiQzbNNhMZtQq3AOLAnIRcLppkFnmCUcECIUKfS5tHI9zOpUsV8VxI35HIF0n4B3h2bdopm8IdJb1vD5FaIqLq1GCVL%2Fxaxpv8LgbwVb15AKMXml%2BlaiqCamtUaXIJnCCzlJUTbcjGjWAT%2FCRD9YQmyC16UG0gSh7jACubuBF7gwJ20W94R48aNeetl8m1rVT%2F4ZG2VhXQmUTFsIjlom8sMZFho%2F5eGHehvE7VCeaiVNRGCWLJwu6D%2B27urhHtu8FZj1mwnzTStBd8dsyoGNdXjUIBY2IFOewCaUQPhb6GqWdOrmKvrOoeJj954fmE7ZTaPvLjuohvJEaynYTft4vS6TWnCgVwOMHFaTF%2BI2FKefbIR5MYnuvOcK1SfamcPWwqyPcQErO%2BIzhV1Ue0jj6yM6YIADjNEpXesaI18guMwfsfLaKWg3t1yV%2F3HT0v9bcUUAD60H1ELJTofC0lKtZmXinUcmRuf7bim9yen%2B0eJaZHUgCmAJo04BOiZIOxgK5S0d1QFRuVHWQNP%2FeXf7FVbUggQ6ub3cg8E3btO46RmYWQgjFhAkmC40NIJZTu%2FImBzEpgvtOaP81WixF%2FWS0lOobSBTjsfv5sDrH47Bk42v%2B1qlIXVeKPulqr3JfXEHTWjtwuUx%2FfjDlv4C9BjqkAWbikjwGShTC9tQK6PfXpHc4zYmvS4NsJyDArOtFsdPjcTX9W2ItV6Im5vpT61Vbbz1CkHaMLyoDwaSezZcPu9rr0cqRh2hYjZls5yLViYEwiapGj7SEfOCFAOxrfCCGHoDFPrlz5R7wi7Bl5ZVDxAi%2BI725rRaL4VRcDtL9WFynUN5pxAItBdg4I0s%2BdoccizXnSLcYLmzAQ9S2oxOrrdV5rmEL&X-Amz-Signature=4fd0d07ff2017aad2391c94520555eeb4027aac016ea4c5f543bd4710bf19df0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQGALMO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPyKsB3Cese7s3KySLzHOUuvr5Q4a3G0OoZjo9Oj1ceQIhAOryrZLqODnUIR7VUnxr7J7JUpY6pOdcCKw%2BxkV9KtAeKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBxNnjiQzbNNhMZtQq3AOLAnIRcLppkFnmCUcECIUKfS5tHI9zOpUsV8VxI35HIF0n4B3h2bdopm8IdJb1vD5FaIqLq1GCVL%2Fxaxpv8LgbwVb15AKMXml%2BlaiqCamtUaXIJnCCzlJUTbcjGjWAT%2FCRD9YQmyC16UG0gSh7jACubuBF7gwJ20W94R48aNeetl8m1rVT%2F4ZG2VhXQmUTFsIjlom8sMZFho%2F5eGHehvE7VCeaiVNRGCWLJwu6D%2B27urhHtu8FZj1mwnzTStBd8dsyoGNdXjUIBY2IFOewCaUQPhb6GqWdOrmKvrOoeJj954fmE7ZTaPvLjuohvJEaynYTft4vS6TWnCgVwOMHFaTF%2BI2FKefbIR5MYnuvOcK1SfamcPWwqyPcQErO%2BIzhV1Ue0jj6yM6YIADjNEpXesaI18guMwfsfLaKWg3t1yV%2F3HT0v9bcUUAD60H1ELJTofC0lKtZmXinUcmRuf7bim9yen%2B0eJaZHUgCmAJo04BOiZIOxgK5S0d1QFRuVHWQNP%2FeXf7FVbUggQ6ub3cg8E3btO46RmYWQgjFhAkmC40NIJZTu%2FImBzEpgvtOaP81WixF%2FWS0lOobSBTjsfv5sDrH47Bk42v%2B1qlIXVeKPulqr3JfXEHTWjtwuUx%2FfjDlv4C9BjqkAWbikjwGShTC9tQK6PfXpHc4zYmvS4NsJyDArOtFsdPjcTX9W2ItV6Im5vpT61Vbbz1CkHaMLyoDwaSezZcPu9rr0cqRh2hYjZls5yLViYEwiapGj7SEfOCFAOxrfCCGHoDFPrlz5R7wi7Bl5ZVDxAi%2BI725rRaL4VRcDtL9WFynUN5pxAItBdg4I0s%2BdoccizXnSLcYLmzAQ9S2oxOrrdV5rmEL&X-Amz-Signature=cec2a4d8288570a6e9ff89ca20e9d687474ff3d6a964d18183a6fcf58e00dbad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQGALMO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPyKsB3Cese7s3KySLzHOUuvr5Q4a3G0OoZjo9Oj1ceQIhAOryrZLqODnUIR7VUnxr7J7JUpY6pOdcCKw%2BxkV9KtAeKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBxNnjiQzbNNhMZtQq3AOLAnIRcLppkFnmCUcECIUKfS5tHI9zOpUsV8VxI35HIF0n4B3h2bdopm8IdJb1vD5FaIqLq1GCVL%2Fxaxpv8LgbwVb15AKMXml%2BlaiqCamtUaXIJnCCzlJUTbcjGjWAT%2FCRD9YQmyC16UG0gSh7jACubuBF7gwJ20W94R48aNeetl8m1rVT%2F4ZG2VhXQmUTFsIjlom8sMZFho%2F5eGHehvE7VCeaiVNRGCWLJwu6D%2B27urhHtu8FZj1mwnzTStBd8dsyoGNdXjUIBY2IFOewCaUQPhb6GqWdOrmKvrOoeJj954fmE7ZTaPvLjuohvJEaynYTft4vS6TWnCgVwOMHFaTF%2BI2FKefbIR5MYnuvOcK1SfamcPWwqyPcQErO%2BIzhV1Ue0jj6yM6YIADjNEpXesaI18guMwfsfLaKWg3t1yV%2F3HT0v9bcUUAD60H1ELJTofC0lKtZmXinUcmRuf7bim9yen%2B0eJaZHUgCmAJo04BOiZIOxgK5S0d1QFRuVHWQNP%2FeXf7FVbUggQ6ub3cg8E3btO46RmYWQgjFhAkmC40NIJZTu%2FImBzEpgvtOaP81WixF%2FWS0lOobSBTjsfv5sDrH47Bk42v%2B1qlIXVeKPulqr3JfXEHTWjtwuUx%2FfjDlv4C9BjqkAWbikjwGShTC9tQK6PfXpHc4zYmvS4NsJyDArOtFsdPjcTX9W2ItV6Im5vpT61Vbbz1CkHaMLyoDwaSezZcPu9rr0cqRh2hYjZls5yLViYEwiapGj7SEfOCFAOxrfCCGHoDFPrlz5R7wi7Bl5ZVDxAi%2BI725rRaL4VRcDtL9WFynUN5pxAItBdg4I0s%2BdoccizXnSLcYLmzAQ9S2oxOrrdV5rmEL&X-Amz-Signature=7e2306de3597a7d2a53831d767b83e14182877f303036df7dd36d1b2c1fbe9b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=37de073d3916e99486bd762079a0730a80ff6079fe2375a55e2f30fb925509d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=98f2d9a54a868cd56a5c3843dc0123866617d51365e9e07d869a9aaf5a708c70&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=cbeba3a09bc32d66b9999249e34e2f54601b37e46b1da040997c732b2a13091b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=3d723a9d946e25648b2452a7a7dda47db959437e3087b8188aee886e26ff42a2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=9a4e4d9423e1e44e9f7382e3ae673a8b2bd0bb7bd950356c71b937f6ecc6df6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZKV7ZF2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC54KFpTWW02OpZAc0oEQJuO0H7VcGcL76%2BWl%2FGG%2B2SywIhAKhMztNqqX6sx9pZSjeQY3s370yp2XQ7Legi7q%2F3PGjLKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBD9i3dDWZWeR4LhAq3AOZ4cJzZnYNmOd%2FBdJDsUDOtDdWBpFVtoJXwG2NqBr9E4ycHXhuwAsp1%2F7%2Bobc4779WO0Wc0TMwMTYVObaoaqUsjX%2F7aDLCskEb1J%2F2iqBAIJbhHr4e8Z1urGofUg6Zm3uARcXcUEDtOySo2GP7Eb3LsXqm%2BMnn0SgnI0FYqpzNu9EpyJnfLeh61kNJgRFxKYNfXX3V%2B9nLFI%2FayWzWjuqwS9tCdjiRkTMFoTT7YEjyuqHtqSjEiS0aYDCBh6oRrrU7sCSAQuqTnnKfBjTt1gsG5SHC4et8vNtnxadg8nCOCBUADAWZROXEgPxBbKfrR760vY%2F4C1%2B7Lq0hv5IQIZj2JxqpwkjRTX3c7WchZXpXGhempUY2o0HiENsu5HpY5u4ZoDOdu7XfMbXDhkdSaOqUrb8pYD0u9HdIvv%2FXI17YrD%2BZ%2FDq%2FysaKeevCnh5VtaSQed25yfqAphU7%2FSv1G1%2F3UVOwguUBrd95K03xeg4GoD9rGWDDhfK8CegaS6M82ndGOUV%2F0G%2F1WbliMIVU%2FK12emsHw251E4DqpUxxbcfyZKmUINvXBcRmG%2BCfKrHMSnI4pvg4E4p8VgAph8ZoP6AP%2BKzk7V7Gvm4Ee%2FbIMrD4VMgz%2Bi1pdObhVrx9pTCtv4C9BjqkAWS5%2FIVIcNqNDcEKQtIbaTFlv%2F1FPn7bXc2btNyvNJcTbgJHejVyZH%2BWNBYt0xFbNg6f298NWFSXOOQUIHPgEPVX27AGVeS9Vsdr%2FYjp%2FrfLgXjBpqMu845M2sEsN4TaEm25Wkr3NwUGro9z5Te6riTrY890MmFHLYEk1Q5LinOXpWnbVoSCnuPxa7EBrQtLcNZG35ocuyjGXTqzxBrfLUGHfk8R&X-Amz-Signature=61d09cd32a81603f6800a25e8b8d1f55a0c98b9d73053a233def083a09af567b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOXCJEF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT7KGuuLj3xcfEG0SIWD48lFc4XqrNwAzKM4Rx6An%2FfAIhANx3v6Snf6gKwqqGgO5u%2FNFOBfG%2B9001DUt4CWv0NuYTKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7NIwhbVod1YzBPpoq3AMhs5LSuodqvTDW7sOhXIhW%2BAo2DCLQULNeNhLIREB3CyiVU8XfG42FCcQLOKArZ467egCvQJY87aHn%2FN5AWqdM0EJExqg0gzpAIUjEkbNtZw4wDICqcDv542FhB6s%2BflnhUu8r3185sY%2Bv4sbTKDhXJ%2FcdwsE%2B4W3uYJOxodQEp%2Bnq%2FUmFEm1Wl5h0sQtIqA3z9omYN7IpM7hSEcFQypGBGl71j%2FBBX248BXtubCksrJAB90L2XvdP4uJ6ZfTYpraiVpfR8b8TvBYFbj3H%2FrF5L2buQISp00rahmI8cu6XrzmUSEtjY%2BLcA6IG6EowexYz0k7IcMC2Q%2F%2FPEn9F%2BkueTmuPEfYvzs3HnLnFKSVnWr1a2mZ2V6T27KIRSA62IgCsc4D4C%2Barr6TLdZKi778yvfB%2B8mvuRKREwRWHssnxYAcyQljDQJxIxfezoKAqKbQs90NokSeaqDWdLUIdIoiHoh4LLeXGH2tJjM6%2FAYOdZtsYWvRmKIbmSN9DMAUmt3KOTHgzYaBRKiA0HIJw8GLD3aVpy7RyXlOe1l049VDBfbP1c%2F4F1g8xGUlarZeq60g2CWTAlXkS1jD9nlcnmo3D6lO4j%2BhmzUdWpIz24aTOxDuR2%2BuaF3ZI8PKipTC5v4C9BjqkAewUi3K5PLi4Xha8s8CF7zNnnvkRbYkZ1ZzUvNkyrv2jPqCh591gNWW%2B%2FG8IuEChysTH1rc13CSzWztp%2F%2BKSUnzWmWRcvblmC%2BHac6U1qAjlcyl2Yk%2BM0QYaTSq%2BC6he3FwUAYjIAqzLuY6hWqolOfw8cMjbRtNhFzfriBr8OAtZ9xEuiPEjcPbg1n%2F0QeUPxbl2oT%2B5R9vyf3tHeSMTRfmlRvii&X-Amz-Signature=2b1d0684406e7d46f5e1a1eaacae32bf95b811fcdf8b4e99560687b9e3baf50c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOXCJEF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT7KGuuLj3xcfEG0SIWD48lFc4XqrNwAzKM4Rx6An%2FfAIhANx3v6Snf6gKwqqGgO5u%2FNFOBfG%2B9001DUt4CWv0NuYTKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7NIwhbVod1YzBPpoq3AMhs5LSuodqvTDW7sOhXIhW%2BAo2DCLQULNeNhLIREB3CyiVU8XfG42FCcQLOKArZ467egCvQJY87aHn%2FN5AWqdM0EJExqg0gzpAIUjEkbNtZw4wDICqcDv542FhB6s%2BflnhUu8r3185sY%2Bv4sbTKDhXJ%2FcdwsE%2B4W3uYJOxodQEp%2Bnq%2FUmFEm1Wl5h0sQtIqA3z9omYN7IpM7hSEcFQypGBGl71j%2FBBX248BXtubCksrJAB90L2XvdP4uJ6ZfTYpraiVpfR8b8TvBYFbj3H%2FrF5L2buQISp00rahmI8cu6XrzmUSEtjY%2BLcA6IG6EowexYz0k7IcMC2Q%2F%2FPEn9F%2BkueTmuPEfYvzs3HnLnFKSVnWr1a2mZ2V6T27KIRSA62IgCsc4D4C%2Barr6TLdZKi778yvfB%2B8mvuRKREwRWHssnxYAcyQljDQJxIxfezoKAqKbQs90NokSeaqDWdLUIdIoiHoh4LLeXGH2tJjM6%2FAYOdZtsYWvRmKIbmSN9DMAUmt3KOTHgzYaBRKiA0HIJw8GLD3aVpy7RyXlOe1l049VDBfbP1c%2F4F1g8xGUlarZeq60g2CWTAlXkS1jD9nlcnmo3D6lO4j%2BhmzUdWpIz24aTOxDuR2%2BuaF3ZI8PKipTC5v4C9BjqkAewUi3K5PLi4Xha8s8CF7zNnnvkRbYkZ1ZzUvNkyrv2jPqCh591gNWW%2B%2FG8IuEChysTH1rc13CSzWztp%2F%2BKSUnzWmWRcvblmC%2BHac6U1qAjlcyl2Yk%2BM0QYaTSq%2BC6he3FwUAYjIAqzLuY6hWqolOfw8cMjbRtNhFzfriBr8OAtZ9xEuiPEjcPbg1n%2F0QeUPxbl2oT%2B5R9vyf3tHeSMTRfmlRvii&X-Amz-Signature=bd8f318e26d1d3b585538f8d6ae21b5e663b63acb66f660c01d2d28ff71f3d04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP63FFWL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCGBT8qaHpgf7Fup9CqknCgnQ2XvXgSgjHGVkEQEKKC%2BAIgWRWb8fadeqsGyAKwFmCYwHQTzdnytjN2atX7xmcFQ3gqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNdIXiZwx29u%2BrwkOyrcAyPPUQx%2Fho0maeID6l6RtIIvFD%2BfNLoRzCEibeFyousZYHgoX%2FG%2FfeEh93oAHQvC9xgCepOCEHGPAi4ibDICncS%2BmkP4cNxiDqzO0%2FCD7%2BHwdfCJRmGzp3ueCN9kmry4wwSlRzvCOQLmqRsOOCaFbTNj0hAdPgJWq8eHIGXkNwg%2ByOpaCEooPV2ywdEOXzlsVRD1WV%2FuoCFDoXH%2BgA4oKoG%2BVcC7NzAbELmzJ21Q5Z5NkB5NN%2BeqT6cjQ0HxH4K08OIfQ1D2cBCFRPozBPAeZZMn7GBY6ADIf8av6HqOEzrd0EXsvyXls8GMiD4RBAOmMnJPKbPayI9iElZOsm9RdTS4eXN4fOwKInJTVK%2FEzAWdEd4zwDu9neyUnkQ%2F5BVDLUJWUIqsvVbQE2DpNhUYCICm8d9f4ym8yK1I55QbsMYD67CTCJS1Jb6Gqmnjc7XwOv7KQE%2FcF6JuKavcQAA0Aza8zKJp2bky4c23Ii1EXq1d9agsXCrryZNCX6gfp6wcOlKGo3I26WJlrHWJOEKMsp4YW7Ix%2B8oUufIpaGEEfcVYQZTISMpYj3MNplyQunInoE5Jlfs1CtSWq8Nnbv%2Ffa9qx7Lwhb4aFFY04KTJ5XFMtEXxEHgKApTWcAoM3MNa%2FgL0GOqUBCb6wptbmZB2LbJWJFxavLYKxotIvynl2m1N8EqikBzemNdPFxjfhtI4nJIq22sZO14gq3Z2hRerhTPWqBT2fThh%2BgdzJ4TNZFZr2pMlwxoOzx7h64bQYxpqa%2F1PANaUVhnr%2BMW5O7XPAZWJX38bG%2BY%2BoY5eDPkmAR%2FZwxginiap5m89F2XVp45%2B6ttEr%2BCXwY8VxHmGUqO71bMfvN9g7jJRlhGQc&X-Amz-Signature=5add6ca8d717da552cf2c4c9bb4af685e7d7fb4d9e9c51301e1b51501e79f374&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAIQOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcXT8H%2FsHwBJsHYs6UpKFMsWYMiFhSS6t4%2BZjukF%2BbHQIgXm1MZQMRp3%2B0u%2BdH7yXLGrlDfoW7W%2B4PtfLG0CmSNBQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7fXB9QVTn11pjhsircA8UOEWStGgI6L0PbmzcmUWSo4hF3QBQhAB8CMWDKyZ3U7ZNysbfTdeQYxc2fhyYGbwOIYdmGpJHQcInZsuH9Z9l7ZnGRCwCZ%2FEB4U6Z3A%2B0i8EjPmDVZxOt9yg3ryacAQ7cZV%2BCAvq4FlFD%2Fv7u7Emx7M4iXpzsFR4PurN8%2F5JgJ2erKmuBIsPiYbL1FNKryq2zJS4m4REj%2BR2aRFb53seKkwcKl0NUQ7TOp3Jw0nwQBRjfkAAjfsqe61w6Pf%2BmV1L6YP35J1ZeRnijtBh%2Fq56oPZhCF26oq6tdqjYOhR5r9yvjCsTH6cAhfSfNqzrjw8qGqeVBMFar%2FLlyZIGAYpkpRdAl%2Bru4EhyGQqcmZfbYMEVcsHQivuUo0hcdJLjwiRw8pNLQCfUZxMTHmkEbB3kWLRhMaM6bB1SlRHm2S2FDAKr1ubAqlZrEhCOVxR1se8Amt8sWj6ejIvD8GmFsZ8x8kPTjRQ7eIuGYvAVqd839DpB0iDkUKbiiW5xGT1hJYXm3%2FougKNpaQqg6QRZ5P5%2BOQeQGTtacz6h7G%2BW5AfCDDF7AmC7IKBsQLZMj9L8B2R2MPptNzR0xbJNmYm3CBgn0FsLqcZDxCrbsZfCnP9dgYNIo5a%2Bllm9UaUIcAMLe%2FgL0GOqUBewIUqQWE36VuT%2F2qDx69aKReFqfdouCaZUEQakg8RLs%2Ffn%2B3um0X6ugVYDEtZe4Xf5gFDxlfhvLVvTr95GP0pSYXEQdneg0Kl3OsahVaASuFBMFJiIAgL8J%2FQbxCl8smdaahtzomaxMvxknT4LYHZqJv7J6zMJUyRXJYkoGpmDYemYErFrY7R6kDONJa3s0xHUOxNNCJPhbhhenGdk64lVEynCwV&X-Amz-Signature=3184c30ef41c96fca1acc6ca90cac207d29cd397826245bf165cdc944e7defc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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