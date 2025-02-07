

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=d09041b032e0af8280f107de33eede3ee9373c8b0eb492cd3fff4f3f3e0f277b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=14d47ac5c7498c1858ff6a13321ea0f84315344744570e08cf0388ad075d56ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=134a18904c4cf5e2603ee86c1e352eb71a99edde6b2c35c2090646662ddcd751&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=81629f1e20b7af433972a7c0c0bb8adc4a706c21005819be2d96386cb059c1d7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=d9416348cb978f7f08aaac8eb207f8e8191182e4c426eea6c030391e278d3061&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=483b187d0d30223fb083e4334a81480812c4be65c3fd3619ed0028c3edc3e71b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=a44883cbaee5449056a3fb8aca7f7caa820feea0e50677a53ee9d4a099b0cca6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=f6a905ab787125e41b44bd884b2a06b8aab752a70ea30e599b171ac6d3f46be3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=c2d8b2938c1c002fa55b1ff8a69b220d715119c0aa8f1ca4d6339974e7442eaa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667736WBBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFgsCFLr1gz4sPsz36O0IYie4AF1NN6B2lSKUFrbOjq4AiBUTDGBTbsvri8qzSI7orV4du%2B8vfAL1%2FepYNimlO%2B0kir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMX9mzRE02m5sa%2B4elKtwDAwQAYQfz6NmOQ918zcPj5%2FsdlKZ2HKJdDCtlnYN11E9Qd0cWGAvEhra7IdBTyug%2B06A%2F2qkLdR%2FLmgGtGpgcTtU7Aj82ATpftziwKpDmFHT24%2FH7Im5b22VESmLkmwVXOWUNR58NZmBUi7VTxJRYpVwpWwR6AJSPm8v5IQOG0tdVtTC%2F9tIuFNQ2F6EDQyY7Wwr6fnJyAKvklB6NdlQHl4GVIHWnB9AC94GO2mTeWbdeIxRt3GX6Y%2FpO2%2BO693%2B0PzspRnz0V4SmHSLyrP2%2BRM63ZHMvVzJ6PDTO7TMXzAPoT1gzLFZt8aQnxgn4SwtJmhQW3RciqtMSiT2BRb%2FmA%2BXHEW%2ByvtUKrjUdqqZrVC0ViHx94ZSAcqyYihuMCM4uNbUF5Zvc3DwMz%2FVGta3DxggT3sbPdX7wGDOoS%2Fp%2Fj%2B4%2BrBtd2mGjTG9QvmliCkpXxOVj0ZMaV8yFJq7qmQuMYWuxMp3TH5McbHosxzbSZmhQMtBxUh3K%2FV2rFAsWW6vye28LRGg50dnCgDJtClguqlGfri5Uk2uL%2FZT14EyWwE5WF0P2khoHkMMec%2FldQTX0m4B8fip6YFKG6vPho6fXCzsudiIuipk4PL%2FDgMCdnubrYBUTw2A49HbtCVEwtZmZvQY6pgGnJaTjvX6pkMtrjSg%2Fnt1NnD2F0L6rrJvqm3ieqelxn7MyiJYgT4ujJSKM9LPdhGXQyiBI7N6AER2BFP27E%2BzYte%2BGhlv3cTG%2F4TR6OBPgBruEhfPS008LaNAopijURN0zkO6Xz1T6I0sFWk2oqcFRWYQb4v4w%2BcaDnLWc2cEqNlMPCdcp6pzL%2Fy7PeXixcWhGVcLy5Swr3etlEn2o3g%2Fr9t013D%2Bc&X-Amz-Signature=a3820a92383fca90f5962ef8c8009f91261d3d5b0b177478af7d2dbcc19d1f39&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667736WBBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFgsCFLr1gz4sPsz36O0IYie4AF1NN6B2lSKUFrbOjq4AiBUTDGBTbsvri8qzSI7orV4du%2B8vfAL1%2FepYNimlO%2B0kir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMX9mzRE02m5sa%2B4elKtwDAwQAYQfz6NmOQ918zcPj5%2FsdlKZ2HKJdDCtlnYN11E9Qd0cWGAvEhra7IdBTyug%2B06A%2F2qkLdR%2FLmgGtGpgcTtU7Aj82ATpftziwKpDmFHT24%2FH7Im5b22VESmLkmwVXOWUNR58NZmBUi7VTxJRYpVwpWwR6AJSPm8v5IQOG0tdVtTC%2F9tIuFNQ2F6EDQyY7Wwr6fnJyAKvklB6NdlQHl4GVIHWnB9AC94GO2mTeWbdeIxRt3GX6Y%2FpO2%2BO693%2B0PzspRnz0V4SmHSLyrP2%2BRM63ZHMvVzJ6PDTO7TMXzAPoT1gzLFZt8aQnxgn4SwtJmhQW3RciqtMSiT2BRb%2FmA%2BXHEW%2ByvtUKrjUdqqZrVC0ViHx94ZSAcqyYihuMCM4uNbUF5Zvc3DwMz%2FVGta3DxggT3sbPdX7wGDOoS%2Fp%2Fj%2B4%2BrBtd2mGjTG9QvmliCkpXxOVj0ZMaV8yFJq7qmQuMYWuxMp3TH5McbHosxzbSZmhQMtBxUh3K%2FV2rFAsWW6vye28LRGg50dnCgDJtClguqlGfri5Uk2uL%2FZT14EyWwE5WF0P2khoHkMMec%2FldQTX0m4B8fip6YFKG6vPho6fXCzsudiIuipk4PL%2FDgMCdnubrYBUTw2A49HbtCVEwtZmZvQY6pgGnJaTjvX6pkMtrjSg%2Fnt1NnD2F0L6rrJvqm3ieqelxn7MyiJYgT4ujJSKM9LPdhGXQyiBI7N6AER2BFP27E%2BzYte%2BGhlv3cTG%2F4TR6OBPgBruEhfPS008LaNAopijURN0zkO6Xz1T6I0sFWk2oqcFRWYQb4v4w%2BcaDnLWc2cEqNlMPCdcp6pzL%2Fy7PeXixcWhGVcLy5Swr3etlEn2o3g%2Fr9t013D%2Bc&X-Amz-Signature=30f2026aa64a343f557ff11c76a0d31d6a7d2d84a7b077f6d80254edad156570&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667736WBBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFgsCFLr1gz4sPsz36O0IYie4AF1NN6B2lSKUFrbOjq4AiBUTDGBTbsvri8qzSI7orV4du%2B8vfAL1%2FepYNimlO%2B0kir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMX9mzRE02m5sa%2B4elKtwDAwQAYQfz6NmOQ918zcPj5%2FsdlKZ2HKJdDCtlnYN11E9Qd0cWGAvEhra7IdBTyug%2B06A%2F2qkLdR%2FLmgGtGpgcTtU7Aj82ATpftziwKpDmFHT24%2FH7Im5b22VESmLkmwVXOWUNR58NZmBUi7VTxJRYpVwpWwR6AJSPm8v5IQOG0tdVtTC%2F9tIuFNQ2F6EDQyY7Wwr6fnJyAKvklB6NdlQHl4GVIHWnB9AC94GO2mTeWbdeIxRt3GX6Y%2FpO2%2BO693%2B0PzspRnz0V4SmHSLyrP2%2BRM63ZHMvVzJ6PDTO7TMXzAPoT1gzLFZt8aQnxgn4SwtJmhQW3RciqtMSiT2BRb%2FmA%2BXHEW%2ByvtUKrjUdqqZrVC0ViHx94ZSAcqyYihuMCM4uNbUF5Zvc3DwMz%2FVGta3DxggT3sbPdX7wGDOoS%2Fp%2Fj%2B4%2BrBtd2mGjTG9QvmliCkpXxOVj0ZMaV8yFJq7qmQuMYWuxMp3TH5McbHosxzbSZmhQMtBxUh3K%2FV2rFAsWW6vye28LRGg50dnCgDJtClguqlGfri5Uk2uL%2FZT14EyWwE5WF0P2khoHkMMec%2FldQTX0m4B8fip6YFKG6vPho6fXCzsudiIuipk4PL%2FDgMCdnubrYBUTw2A49HbtCVEwtZmZvQY6pgGnJaTjvX6pkMtrjSg%2Fnt1NnD2F0L6rrJvqm3ieqelxn7MyiJYgT4ujJSKM9LPdhGXQyiBI7N6AER2BFP27E%2BzYte%2BGhlv3cTG%2F4TR6OBPgBruEhfPS008LaNAopijURN0zkO6Xz1T6I0sFWk2oqcFRWYQb4v4w%2BcaDnLWc2cEqNlMPCdcp6pzL%2Fy7PeXixcWhGVcLy5Swr3etlEn2o3g%2Fr9t013D%2Bc&X-Amz-Signature=226a21c194b03298f14a462e401a37ed7e084dbc1359b8e0fc066c782f83b5bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=5195648a8eb5b78c5dfecdc2ded627eae29b7f044e73814d0764bd2164970a57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=005ed396dbbfd72f48276866aad0be249c310539b40640fe13328159cec787eb&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=21d5b0d00bf38a8d65f840eced6686e8b0774283dcd718b5a640f855228e6895&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=85e3f90f44acd3f952d8059e4cc74c6ba6ea88ac634426fe839d8a392562f38f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=231ca52eee1f6472f9aa221857174e3ccd6dd3adee2edb6898d7d3f544ce38d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCQTQATO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDG%2Fdy7q35MvPqbiwrMxDlBW58%2BbQT4RDDeXoV9H5Gb%2FQIhAKQDKzXuYZZ5EHrbUX%2FOxh6p%2Bte5PBn3CXiZr3pvxZqlKv8DCHsQABoMNjM3NDIzMTgzODA1Igz0PDm2K7tZ9GIplZcq3ANQyN%2BsvVMNjs15U60K2KewCuR33K3mVVWjdZREORrE5%2F1l08Tr9kU82Gu8LPPVEkffC5%2BUrY2fr1jfsARRINBXo5eelhgUtozqvJhZGQ1RIgwWh4c4SYzXYmP8ydo0CLNsQNYEBWdvCCkgLZ6dxjzJKURzhObl%2Btbs7h4UeQEmCy4CeLlTQ2hxJ3tD3D110W12sxJsZZUEFyjq1%2Brfq1zyWEeR5eKTeTckc7Ka5QK58mI90MEcmBbxDU6adN21Wwg2gNEDAc3nAQ94mtlfd8pk5450KfjUCeMejJoLAFOVJCoeVD2xVJ9GuWFROfBGk1Btc7s9Ocyiq7qQ7nAQLLVEMtVcxD4L228V2VSmTcDJldexjXsS92MMz6yo3Oy%2F%2Bhrh8zDyN1TY6GXxLghS7WnQOY8EkGl2Tw7lEN92vOKIHilqNfG50VTXuyLYcfU1HLpfm%2BJ8zUYLz8say%2BUM%2BEqm04%2FFwj34%2FjDAZmp7xphUB0VLK4VjbzjxXwcfHh66vSfVpDQEUF21Ux4Qw1rTVnitiwntL%2Fu9v8ArBqax9tQPM9R8EWdvpCzyft4rdM4FYyQs6G2E1SRl2p0X3wlgp2wCj47c4cWd8lz2yQX0XnwY1grJWTx9Q0BV0d7XBTCQmpm9BjqkAZ8kumYSOvazygkbfns3JsMMbyfdKi3xIi7AXaKStORxlZXio%2BM2W3HzY17E9nuoKy2q5Bpbf6o0uIohczJhjk%2BYRFBPNtpolwEiKx0NuJxsfqeu8mNZ%2FGjsTXsRPLzy8pwfcnjFlIGZUvBrzE9Az60v8BhskQz735D1l6VWTfSbLC8h%2BOeMlWA06GfopXCgA3%2FWrhGueiTv3O1Ejj%2BNbJInRoaU&X-Amz-Signature=f6549d348979e6f18111b320d5ac7f6340253350ede332c5d01770e2741c8f5d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWYXZWOZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCQGgMKfB1JYF2e%2BNJpqirzKvG%2FVSKJ9oBhaHT7kEFgCgIgGBMjYs1PDGdWxTKdAL3wePVHrjSqIGfymf%2Bc6Q9VOCMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDFQMrQ9nkuCtwGziLyrcA6wsto1PQy0F%2FrqH9%2BWChZeeLX%2Fej8VASekADPfpr467eOPscKXF%2BcxfjidY%2FKB8MV25J4uE%2Fjd3br9%2BEgXHy9pLldhA3PAJyAf2zglXi8AnuU4Mpchrc5OQpC%2FjjYU2C5uHMETublhEt78Zs33ZCQmoHbJPLoeFUKg0IX7AywTfQH%2BV1YWbVHRZF2mJYv3UK6%2FZos7txHmaBhcTfN4ffBtMXeiy%2BdhJHZMO%2FKStT1p8tzZIlAHOtTAvLSu0EOhQklNxTDkGUmOBsEU1hIJnXGGTnMFCWwYKC4FNTzLPQq3SpiU11xXFEDnrSOHGa6lFzuQwkDnXAmoKZznz7k2KBiu3PPW8Et1rdozXiENWmLWMFL6qGEdu8tmnc1RA4qjRJe%2FAdOH%2FchxQK2Nu6KNPznH2oFblpgNqPd3HJ1ubK6HPrbOVuhyeZwLYUK6jRT68d%2FWuV16w3BXMsJuz0dLpZAEK5OsjdOAEaAZveKPsz10uDKbwYCMgzjbwC%2BRykAzQq3HmdYrlkavuruNz90wJSM460lqEj5cC2tuNXabljFAWwf3PFSxJnO0LTFGOxyNllFu1dfS8GbnNvBbRogXT7vioDTM5I8NBs4y77OfXDEz496sG%2FCMYRTzlG%2FxKMOOZmb0GOqUBYOa4wmofzVZ6IZcJJ46FQr89hYM5veegfaNFvxDzlOJ8dZYP%2BxY%2BmLATtmfe959IEsl4przwor01R2nxRpS5P7Zv4aPYbK7Nx6s77kUiLmVn9vgFnY5c0P7AAk2mMP%2BXFPLRj9lDSSdb7H1M537aGPGz5q1oOIdhhK77BfKLT3psGmm5cx5z0HTIxnTYaIwItwB8rI3n%2FA%2B56o7MZUm0t4xglTHj&X-Amz-Signature=acc0849e0a142ba2864ac45979de0b20004309802471f4ff3879b617f2b16afc&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWYXZWOZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCQGgMKfB1JYF2e%2BNJpqirzKvG%2FVSKJ9oBhaHT7kEFgCgIgGBMjYs1PDGdWxTKdAL3wePVHrjSqIGfymf%2Bc6Q9VOCMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDFQMrQ9nkuCtwGziLyrcA6wsto1PQy0F%2FrqH9%2BWChZeeLX%2Fej8VASekADPfpr467eOPscKXF%2BcxfjidY%2FKB8MV25J4uE%2Fjd3br9%2BEgXHy9pLldhA3PAJyAf2zglXi8AnuU4Mpchrc5OQpC%2FjjYU2C5uHMETublhEt78Zs33ZCQmoHbJPLoeFUKg0IX7AywTfQH%2BV1YWbVHRZF2mJYv3UK6%2FZos7txHmaBhcTfN4ffBtMXeiy%2BdhJHZMO%2FKStT1p8tzZIlAHOtTAvLSu0EOhQklNxTDkGUmOBsEU1hIJnXGGTnMFCWwYKC4FNTzLPQq3SpiU11xXFEDnrSOHGa6lFzuQwkDnXAmoKZznz7k2KBiu3PPW8Et1rdozXiENWmLWMFL6qGEdu8tmnc1RA4qjRJe%2FAdOH%2FchxQK2Nu6KNPznH2oFblpgNqPd3HJ1ubK6HPrbOVuhyeZwLYUK6jRT68d%2FWuV16w3BXMsJuz0dLpZAEK5OsjdOAEaAZveKPsz10uDKbwYCMgzjbwC%2BRykAzQq3HmdYrlkavuruNz90wJSM460lqEj5cC2tuNXabljFAWwf3PFSxJnO0LTFGOxyNllFu1dfS8GbnNvBbRogXT7vioDTM5I8NBs4y77OfXDEz496sG%2FCMYRTzlG%2FxKMOOZmb0GOqUBYOa4wmofzVZ6IZcJJ46FQr89hYM5veegfaNFvxDzlOJ8dZYP%2BxY%2BmLATtmfe959IEsl4przwor01R2nxRpS5P7Zv4aPYbK7Nx6s77kUiLmVn9vgFnY5c0P7AAk2mMP%2BXFPLRj9lDSSdb7H1M537aGPGz5q1oOIdhhK77BfKLT3psGmm5cx5z0HTIxnTYaIwItwB8rI3n%2FA%2B56o7MZUm0t4xglTHj&X-Amz-Signature=f465381c98d54e3eaadef619bf68ab1e5f05c32afa254f3964de4977dc76b39d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMX7RV54%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIG6dwRnrpR2wgdFeT6K3v7LB9e1v%2Bljtxsp6BhdbbvxnAiEAirJE7k6R4yjo6XKzHhtYAdAtSgcySrGTfVXX8SQP13wq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDOe0%2FhwKoL5RRPEpSircA1x49CPgmXVEFeRaQcF1QJLVimqC3WVbk4AIJzPm0WAzwL5%2BalZCUU%2F0WEytr88%2Fbg%2FrulpGzviO%2FIvEezEs7CHAJzSDOl9%2FnC7spE%2FrJqgNybmh0Bdl%2FlILNxxe%2BmVO%2BPcXQh6GQYU2GeBmA5WpEJaOm%2FWdVZNl2IGTdKLX1B1ZVBdfMvNcAYOJ4SIDnwnL4q4zJUEVLDIKJ6QbdrtRiEAOV%2BlKXdftNC4uPjcYw713TSzIzx%2BnrkvT9xKHSGYu321QhYwxD6oBGT6GrUICQp57VzRkjHlGohn2o2CyWKMSYhpzSrajFfYli3I36kXV%2FCGYEFCx23ufaNEym4WkHGyp%2FhD2REqiQUo%2Bfz0XAWWXH46NtK51aEgBvaETsL3pw4p3kTqUdgQhCfOpSHPyqMIEieJnGuo3FRr6xQ8sktPPGq6mBMvJ7SOsooVefY3vl5%2B5ZnGN3hfAXcKYeq839mpeyEKMASF%2F84Nvb9vrN57rB1sodTbPsdGRqTf7yDSDhNUv39N6%2Ff9ewX94zMaqvWAslyPBgUmbNYmzAjP7lqxuDrxeDkWp6j1nUgrwBgtVht%2FfMc%2FaYrogm5J4kX1%2By%2FeF%2FjaeOmHqnLoMk3soNmVyImqkdZ%2Fjv8VEA6ylMLqZmb0GOqUBpCF1X7BbPtVGp%2BfXEeH1Q6niW5SsFlPY9YHvOG1jLE5kNnNEiJafQiTGFo18qTz7KWhiH9Tu9Y2fuK3uO%2FYD0QqulX3foRFlLIKhYbBm754eaLK%2BQ5xDBBpUnbFj9QBDXlYRTl6rQHz5yerbcXwkDcsczEbJoecS%2FjLlEkjCAvUoieCnRQCJgSr0flqbbw8odon8VeFV19%2FVw6CwfUp8xQdgqEw3&X-Amz-Signature=42c2413a47c087c906e2a2195c0862b1b62ad3e702fec9f00e91c493d707bf24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHD5VNLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICjD828FqsvcyMucnV7D%2FM3%2F4F7HIlsz%2BBklAlzOu3SNAiA%2BNIky%2BWexwEJ0gQjaZy%2F0wItB27AtYk%2Fuqy8XQn7FDSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEvqrk8aCrw7mocjVKtwDpYE2abVbAi7J3QcQAj%2Fq%2FEsPQgEcBwlm%2B6djGOOzOfwXXtZ7qomZKFwnsDidJAwmQxgLNdOl10z%2FuUtxmaH70cFS6rVZ3eMfj1Fuou7F5Kafx2wlf4zop561XCSJRyRuzNTqFRc8GVVIT4eSKkiQ2wfBmRqEnXACZHDFXsT0%2BvjcvINv1xqMdrV2yQHVxwp1dz02D9mza6%2BHK43MxBZJVb2DyuaFkwIxygPakZUguQcLZ9R0F%2FIN5bgCC%2BckTl%2BXEOzDbjALNABYktpCZiQRwfbvRq5gzxT887OQzR3LJfBjp74KuyiK3yKHoCbUCHHxzxifHQJujugD9qI3%2BPM7HixZJXiESHXnJvbIMCId3EsiayfdVxOQALWfxIYw5dQvZvpRs6zT6gzSoZIJm0d2cGoYtpPNE3nMfBpw1YsYxfCIjhXJ6Do82XfMcU3hEahojKvgzWWzcYgQcnCtFTsiYHG8O9ewPgm3FkU5pYge2Gg%2FHIrKzViKyl4yDpTvA7EuByLC6jNLLuSRfDwCa6Q8YCM7mDx4o96gWD6pjwk%2F0AGBy%2F%2FV0%2FMYH5JdM4audpG0oYSL4UvI1%2FbrqSgL%2BH6fqtoXPh62ts36aPm84MrBqpyXF9Qftul2GEfBrfUwt5mZvQY6pgG5VRIE%2FtnKxrnwOqRG51BexCgpwLKciBzYgqxN7VlXEM0qGfBivooZWmOB0ZNzdBVxEihhh0a1TNiNi2X7H0QcwasIJ92yvmPSReNGtvByNZyBrRCyDpqSxNXmJySCLE5Ws2Uuwmmwhi1usXrh37%2BkMAygpdNoJC0oyv4dAmJXEPCSZydxM41xML9vxuFjYRlkbgDObv1EYGSheYMLNttdJAwHMRig&X-Amz-Signature=41f857a8f9a17ecb559ef45589d46feff84c5bd1ec950cde55fb6824c6b606ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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