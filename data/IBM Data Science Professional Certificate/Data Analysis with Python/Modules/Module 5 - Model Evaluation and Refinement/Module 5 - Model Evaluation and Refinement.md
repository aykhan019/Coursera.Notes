

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=f085f10c82a3d8d2bb7158967285c000a9e4e58e7365513d233c337269085350&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=3122777bf828a325380007124068411ab9cef0f0cd18b2061259b84064ff0f13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=b9da04bc4242323b8c81752bcaec78199529398d9a8e128498785862e214e4a4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=398b476e8e6bac36eaf14c968b1cfded527ecf4251400431abbf19c5f03df6ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=33744dd22f9d4fc8998f01ea1d91ba3dac39762de4e01909597034e8832e7c60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=41938b2de46aa006d8365742c3cb044bf1c7b26b6da379e864a01c0fb818d785&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=93fb47e4aeb71fe739de6e7e86a5fd1297f57f98282936cd58a7f8aa2ff52c6e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=b1256e2612ad83d231298036237f3bb2eeda48162e4c0b56b254411042ff325c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=d6e591d00535b0e4f6a4d7212e4f970514dbe02847f7e5045a16fe45467d0078&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMTL7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBtCe6Mfmn30hSPA1i6rw9coKIaPWFTA%2BoPM30B9MaQIgWyrGJ73XxIupGO0FfAygBxQXWqyM%2FhdbI0jPSvuLH60qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPy6fHj3nomdiq9q0ircA%2BFF%2FOdhOJZgCq6y5vZpF9h3RBm%2FOvHBaC5YAaLy6IeO32%2FoeHanEDaqaIzf2BNcKmEw7vKcZbWd1T%2FH2dh705UV4gEQHTNlzSs3j0mrONNta0kxB6PMaMHCD2pZftQx8CYqw6cyxESg77YO0yD91V4vWroyMg0pSMvdnbkeSgvdLHFwytbV0%2BtcIwZSHn2IioggJKex1yY07QR7yaXYZIbiDEq4QipDt%2F8aQlhYNBK6RKVj%2FoLEfv2xUOONxFFzRoA3iqWqGsfcBgHozA29NuJR5mz9EPRFkehHF2X76aSaKUYwIC2yJktYnJSucTLjPqTR6oa7t8qZP40CIDup4LN46AjIzhzrl5BD8ZSa9U96mWbdUHU9XSPLDJ6IbPOlyK1Ur6SDT3jTvc1YIj6GIr2JoCKn6ce%2BzOxWSDIPn3wGElmlGVFUaGHlFdYU%2FSqjYvgA5C8xj2YFpUdcW5ASOyoNs%2BxKjigNnza73devqNiruilWGpK%2Bv3SQYmL08My4IbTL5UUwejsj%2B56vtP7vCpnvxKAeN%2FwIsEYwCCUAkLLI%2FAla9UfEaZb12rxcRnAV6rHZcfq9KUNQzzoAe9z5BlobAig%2FlITujDX4sg%2B%2BcPSGh1eGxAcLTl5v9%2B2nMNy7%2FbwGOqUBl3BBSG%2Bz3TUuw9IgOzV6MTUgD9pT8ROYQK5bcwh7RSK9DTu3GD8kc%2FGX%2FbjZJVO8emSAphdRnkcCICwWhu9xrddft%2BGeUX52TIXk%2FT59w0R33SoUoJQD21Vt12Ae5KXE9HyPWLSFMlMt6PMc88GtxNtjbj6grIHAQpH1nRVZlPZTKky%2B8zHNuKI9kdZOMUeG7%2FWgpYOcYzGYhWM0xi6TMW83a8bJ&X-Amz-Signature=b01fdd7f1b6322da95e921dcd8a5233367f1e0394342a7ff1c23cf43ddbad10d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMTL7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBtCe6Mfmn30hSPA1i6rw9coKIaPWFTA%2BoPM30B9MaQIgWyrGJ73XxIupGO0FfAygBxQXWqyM%2FhdbI0jPSvuLH60qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPy6fHj3nomdiq9q0ircA%2BFF%2FOdhOJZgCq6y5vZpF9h3RBm%2FOvHBaC5YAaLy6IeO32%2FoeHanEDaqaIzf2BNcKmEw7vKcZbWd1T%2FH2dh705UV4gEQHTNlzSs3j0mrONNta0kxB6PMaMHCD2pZftQx8CYqw6cyxESg77YO0yD91V4vWroyMg0pSMvdnbkeSgvdLHFwytbV0%2BtcIwZSHn2IioggJKex1yY07QR7yaXYZIbiDEq4QipDt%2F8aQlhYNBK6RKVj%2FoLEfv2xUOONxFFzRoA3iqWqGsfcBgHozA29NuJR5mz9EPRFkehHF2X76aSaKUYwIC2yJktYnJSucTLjPqTR6oa7t8qZP40CIDup4LN46AjIzhzrl5BD8ZSa9U96mWbdUHU9XSPLDJ6IbPOlyK1Ur6SDT3jTvc1YIj6GIr2JoCKn6ce%2BzOxWSDIPn3wGElmlGVFUaGHlFdYU%2FSqjYvgA5C8xj2YFpUdcW5ASOyoNs%2BxKjigNnza73devqNiruilWGpK%2Bv3SQYmL08My4IbTL5UUwejsj%2B56vtP7vCpnvxKAeN%2FwIsEYwCCUAkLLI%2FAla9UfEaZb12rxcRnAV6rHZcfq9KUNQzzoAe9z5BlobAig%2FlITujDX4sg%2B%2BcPSGh1eGxAcLTl5v9%2B2nMNy7%2FbwGOqUBl3BBSG%2Bz3TUuw9IgOzV6MTUgD9pT8ROYQK5bcwh7RSK9DTu3GD8kc%2FGX%2FbjZJVO8emSAphdRnkcCICwWhu9xrddft%2BGeUX52TIXk%2FT59w0R33SoUoJQD21Vt12Ae5KXE9HyPWLSFMlMt6PMc88GtxNtjbj6grIHAQpH1nRVZlPZTKky%2B8zHNuKI9kdZOMUeG7%2FWgpYOcYzGYhWM0xi6TMW83a8bJ&X-Amz-Signature=4bdc1d37f7b2f6250901067753bbb09714c6cb271c5661db8e9c4dff17476675&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMTL7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBtCe6Mfmn30hSPA1i6rw9coKIaPWFTA%2BoPM30B9MaQIgWyrGJ73XxIupGO0FfAygBxQXWqyM%2FhdbI0jPSvuLH60qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPy6fHj3nomdiq9q0ircA%2BFF%2FOdhOJZgCq6y5vZpF9h3RBm%2FOvHBaC5YAaLy6IeO32%2FoeHanEDaqaIzf2BNcKmEw7vKcZbWd1T%2FH2dh705UV4gEQHTNlzSs3j0mrONNta0kxB6PMaMHCD2pZftQx8CYqw6cyxESg77YO0yD91V4vWroyMg0pSMvdnbkeSgvdLHFwytbV0%2BtcIwZSHn2IioggJKex1yY07QR7yaXYZIbiDEq4QipDt%2F8aQlhYNBK6RKVj%2FoLEfv2xUOONxFFzRoA3iqWqGsfcBgHozA29NuJR5mz9EPRFkehHF2X76aSaKUYwIC2yJktYnJSucTLjPqTR6oa7t8qZP40CIDup4LN46AjIzhzrl5BD8ZSa9U96mWbdUHU9XSPLDJ6IbPOlyK1Ur6SDT3jTvc1YIj6GIr2JoCKn6ce%2BzOxWSDIPn3wGElmlGVFUaGHlFdYU%2FSqjYvgA5C8xj2YFpUdcW5ASOyoNs%2BxKjigNnza73devqNiruilWGpK%2Bv3SQYmL08My4IbTL5UUwejsj%2B56vtP7vCpnvxKAeN%2FwIsEYwCCUAkLLI%2FAla9UfEaZb12rxcRnAV6rHZcfq9KUNQzzoAe9z5BlobAig%2FlITujDX4sg%2B%2BcPSGh1eGxAcLTl5v9%2B2nMNy7%2FbwGOqUBl3BBSG%2Bz3TUuw9IgOzV6MTUgD9pT8ROYQK5bcwh7RSK9DTu3GD8kc%2FGX%2FbjZJVO8emSAphdRnkcCICwWhu9xrddft%2BGeUX52TIXk%2FT59w0R33SoUoJQD21Vt12Ae5KXE9HyPWLSFMlMt6PMc88GtxNtjbj6grIHAQpH1nRVZlPZTKky%2B8zHNuKI9kdZOMUeG7%2FWgpYOcYzGYhWM0xi6TMW83a8bJ&X-Amz-Signature=a5707fdb243347953c01064ec1f94b6efa78a4045cde94efc1bb81566fbcae76&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=eb95a8a1aee5775e6a12d16df287fa1e4d6e0360de7d140b0a46b66f42f99149&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=f6d55aa9b7fb5e8f114093964cfc535ea6e3817dd3412af44949149e117ed1a1&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=eacb33b3bd5ad7dc32d68d5cd4f446ed60e223c179df3923ca59462b74b70a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=dedc728a31b9901233a00f7f741e0236833af1bfeccd32fd0cb99f5cc6e3cd00&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=1efab6efa20526710338bc5e4a8613cddccc66ba88fd5118f3323bc1a74d2600&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM4XEPFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BnW6y2Wfr9uIsUhy6Q8okbL7GU1GxPvDNv232tkYrIgIhAIlEwPbKMfQhO315cqWcZ796byHo7B0gyOKonRphXkDdKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5YIPhr0o2tP9PG3gq3APY5O4qWNP3EQIYuJrSn8tVdrgMch0oFRXvdSYlbmA5rVRFQg1GvwAqBxZkfbub%2BBYn4X1jxPqjxY1%2B2G1m%2BIUAbp38yczNeaATeUosLdcwykUGBNog9srhSrG%2FpG3m%2Bl0Gr1duHCx9tDq3tLkY3IAdO0aiyN9RARscd%2F4EJFAElWqqQvtbwU3jgvBhS7zM7U8Y7%2BVpw10OCGPNz82DxwFwEvfAqNW1sAsyg36DDI%2FOmCjodOL1Shrg7Beiycp1Irx8yP2vnQ3dJS7UrWGejait8Bh0sKUgAjPKh32zpUnyIqYeqNt7X3ze1aNTvbNge6B91RkX2MLrN7gtZR7w2KiSf%2Fwct9zDPkuhvcS%2BWnJOWpKn6sTH%2BprpvZceBtPi%2F52x3VeKK%2B1oL5qorsE%2BQHvvt7Kgpo0WPMV71dI1YoCO2AtsB129avCe9XBI65BvC%2F4ZuGieCAD5NulkHuTMh4Xibt%2FfjbiR%2Ba3Qab0CEmg8R0Ht4v5cj0Urur2L5D6OQjbwzGZ29tftzfmAC4esoaySSgIYPOiMGf5V9cdmYrL44%2BTEc78PyhAMQxyyfbpsircrycPvYz0zaocGjlKdB96q%2BIJCaZ3gHVZ8qfe%2Few4T%2Fg3JiujeSxu2SeCqmTCUv%2F28BjqkAemNGMLlLvBlTaLL9d9LKuwbCiTEJSJchrmo2yDtnQ0ihQMPcl7dftu0Rae23OTlSfO1k33DtpOhv42GAODmudvPAKOMQaPygWjRvqbCQqZl4VNRAvo8R99f7QsAuKlXXvzB1D3iJRvpVqAjUyBAESBGPZhd%2BlYYRzxx7g%2BjVGcorntSlaw0bhgvKJ06E37%2Fpm7hjhXK%2BJmE6gTEj3kKawTQt1aO&X-Amz-Signature=07846be91dc9af170adc19a15c37b26add0627cc1145d7f3ba14b1cfd2e07b60&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAAFNFXR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvYeSBigyhTHBqPsZ9iQAxDe2UJxJMxD4thxscbKqJXgIhAIUd6us%2Ftvbdr8nHeIfgTnulLGs3eOxMJdDoUbsjps%2FiKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNGgeCmE3nanbEEG8q3AOcXOu5GoW9kN4xCt3B7Y58KRUJscAERsZj%2BdO%2BXhs8Mfq2jh8wt00ZWjo9z072Bygm2EIiLDmgAmUX%2F%2Fib3naE28EY29Y78CVCXACTdMu2VOpixN2nLV%2Ba3TnHWv%2B8KIKsv4SliEwHrVQCYxOjOf7DecTPQmisn8uM1saGQ4DzrCWzTnlibEVYdtp1hmes9gfIBJCMFXv5mSzkirPAnBu7Gj5ptqodOcF5ovZIVKIlyEOujTTkudM4zvJAmS9VT12dxkAgEuLFkLUrNQrLUGIS1o%2B0eZwGXTEU5%2BRiH94Ey%2FzUKgLpOdvRU6Zyzn2ibA5RCkm004KapzrTYDas5SlQ%2BiW7ACqDUcd8BmeZbJ3xKOCHjVewCyPz3%2FY3Xzb7x%2FxNkDQc6vCTiTKqv9kdH7H%2F%2FQiIRRWZGUCvClnZvl3igzprbUSlJFsjpK4uXv68CZrXFt020%2FZueDeol4DGwquqq6IzudmgBsyR4jyhhuGX77eplvg2gSBcfNjyModMFlS1wARi05ws4Y7v6ffuR9l1jfhUJivroqsMM6%2B8uX%2FWaJwqOFqWIBT%2Fcs%2BtGwJI4E5g%2BMecdWXl4FO%2Bi%2BWiJ2yPeBdXxoNfdgIXOMMQ7yOGwxuthIQVCoint5ohwTDCvP28BjqkAepMuBeyUYIaHoebWFs8HwCtAQ9%2B5If0Knwx4S%2BBcSWNxGPiBjGFi0YFyZR1JqhHVy74Md4YNzDD%2F2AjCincQE28TUqqhFPJatLpV2I%2BiUycCoNOHHZag1E0NIu8ySRBafHgHto8Mof1qoEx0OWUy%2BSLrEFhGtMhIp8JaH%2BEb6I1RmjPprm7w848NCReDnqjLHThZTSo3nEzPHrGyz1VKDLRaGpY&X-Amz-Signature=6e62d0f9bc6b0685599494dc0cdcf5d00f9bfb3e2d5b8f75011d724a57f73271&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAAFNFXR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvYeSBigyhTHBqPsZ9iQAxDe2UJxJMxD4thxscbKqJXgIhAIUd6us%2Ftvbdr8nHeIfgTnulLGs3eOxMJdDoUbsjps%2FiKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNGgeCmE3nanbEEG8q3AOcXOu5GoW9kN4xCt3B7Y58KRUJscAERsZj%2BdO%2BXhs8Mfq2jh8wt00ZWjo9z072Bygm2EIiLDmgAmUX%2F%2Fib3naE28EY29Y78CVCXACTdMu2VOpixN2nLV%2Ba3TnHWv%2B8KIKsv4SliEwHrVQCYxOjOf7DecTPQmisn8uM1saGQ4DzrCWzTnlibEVYdtp1hmes9gfIBJCMFXv5mSzkirPAnBu7Gj5ptqodOcF5ovZIVKIlyEOujTTkudM4zvJAmS9VT12dxkAgEuLFkLUrNQrLUGIS1o%2B0eZwGXTEU5%2BRiH94Ey%2FzUKgLpOdvRU6Zyzn2ibA5RCkm004KapzrTYDas5SlQ%2BiW7ACqDUcd8BmeZbJ3xKOCHjVewCyPz3%2FY3Xzb7x%2FxNkDQc6vCTiTKqv9kdH7H%2F%2FQiIRRWZGUCvClnZvl3igzprbUSlJFsjpK4uXv68CZrXFt020%2FZueDeol4DGwquqq6IzudmgBsyR4jyhhuGX77eplvg2gSBcfNjyModMFlS1wARi05ws4Y7v6ffuR9l1jfhUJivroqsMM6%2B8uX%2FWaJwqOFqWIBT%2Fcs%2BtGwJI4E5g%2BMecdWXl4FO%2Bi%2BWiJ2yPeBdXxoNfdgIXOMMQ7yOGwxuthIQVCoint5ohwTDCvP28BjqkAepMuBeyUYIaHoebWFs8HwCtAQ9%2B5If0Knwx4S%2BBcSWNxGPiBjGFi0YFyZR1JqhHVy74Md4YNzDD%2F2AjCincQE28TUqqhFPJatLpV2I%2BiUycCoNOHHZag1E0NIu8ySRBafHgHto8Mof1qoEx0OWUy%2BSLrEFhGtMhIp8JaH%2BEb6I1RmjPprm7w848NCReDnqjLHThZTSo3nEzPHrGyz1VKDLRaGpY&X-Amz-Signature=029df1226e7955b1c36143e40b209e6a0ba3b90ecd1a456039ef05c1947ac417&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOO3HLXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQa9rGYHmxsgqA%2FAjoFhwfff%2FL68lRSazCmGs%2Fc5sn6wIhAOzO5NI6Fh2OfFO1KzewK5QfWOzyCc1cd8NNQDyjYPIBKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZLnAfu72BOu2PDlkq3AOn%2BRLhrXKEEUj%2FPXXoLwPyfegANa3lR57t6w%2BPV4ZDyGLZ9eDsesIFGX38K9MsFFS2xXRk%2BcucdyGlvcdQDZr3YYk4CtOuU7r65HWWwBPxa5ZXoAJmmffB381EOWCB27BqwYfu0xBK6i%2BsfnYEWI7xW2hAX1j3hKQkIASPtmhN0IR2XAdZD0xu1dwjh4vCVbXvtmvwqWyah6Qt3wzZHNfMv742ez02rAPjGfkLFZh%2F7CDOAxdOK95qPbN4ItwIQnEtBXgPmO3Tnn6jW5yGdPGjMemzhPIeKYblQmGVZYzRK%2BlnpjUJ7cXv9xs5XxmPh08xTa7smJYc36GU4Tn34F0J1h7JhIuG09wKtp0iv%2Fgt5mfqVB9JPXpfcQy31m931t%2FqRWMxiikHA%2BUXiOOfjEF6ibXGdMuQT6bgRSp5jg8%2B5Fe23mhaB1CP9PgyXJkPPEkG1LDjfTAvuRQn8C3LHi4imiFVZW%2FiidInuUGl4C4NH9ivh1yNxgClAFZbl9PsyJ0b8oNMr8T45Rn9lWy4KXQSegnzn%2FAG8YPb1YtJQP557htrRLC0a%2BaF4K3kA4rPOaqD0aNmAmn%2FGk016eknL0xppRFCER3AcafVErZP%2FYGlb9%2Fk57VDdhZszBX%2BMDCMuP28BjqkAWZzPZNBhN41tMcsU35OfduK39c7tt1ASPp2L7LcLf9Q92S8Zy7XZNmB0%2BaSpdO0p8HSDAU9Wj6NNAK%2BCFzrLo0Hu4%2FZoVrim%2FUzlB8FzXvf%2BmQU%2F4WzClfCyYAZWhg6jKUL8VD54nU4bABY5kwFTxUmcy%2BB%2B3o%2B2%2FewsR4jZL8AANtsOnnhXFz9oU4FIFukPOYIAJCHgwXTV%2BNkIKTm%2BU8BQpWy&X-Amz-Signature=b619332eb2b1af5b125ab5af5985c33620e839d45d54d120a3863f27fad27174&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T734RUNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl09gdbaTCs4KRfnyM0D5J5ypHeMVG%2FIgcG7iEhivCHQIgXOgUxVmPj8%2F56kIfXYhzSFOQJgn7ynRW4yNsR20w7nUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0bTLD47h6bzdnXwyrcAxIODxCW9tylL0%2FZLwZDQna14KMwdEPVTht5mIYGbZkV4hug%2F4tHfX9UYQetw1LdhbLn4Wf9o9NYB0Hu6DviqNibTfb%2BLTA%2FdQZtT4YK13GRGXxejhVwQ9Z9xuwvbHmwYtXyavTfpJdOUJjP0cDyA4ig6vndcVgQeayBDQy9EaXH5p7THlugyTykywUfSYMP8XlKxlJqtvGOLb2Cg4%2B6ntfaJP6hTQaLyhCi6vNtdAZb2ABXU2ydGaaIT%2Bkl0wpw3jgKJd8bMBos81oISSZ8LlZIM1s9fgZslpgiaDXjZwD66%2BwDnaT6zKdY3wwTfZHhNdxP6pWpfNMfiqN%2F39bZuuP7vR%2F3ULVEas0QFX5MJlkif6ufamf1AotSA0%2BHMBcQOocLYenlSwoyDfPLHTtTaSX1tFNQoee1hOJCArbfPFyYxcYa0IeQTLhaq7U7hMyG9TZP6h%2FFj3PX6hovAQIBjsUkKabZuZumspRGWGjRd9OaUdc4x64yKT2pYdhcN4JWl3s%2BwbfyFrdqf7fZUqtQwU34KNgkdX4FaLOioGm9UxFwccZhaQCo%2FflncPYjGUirHVLA8I7QAdcQkWLhPwloO9mPUyh9r5UrJ6skDdZc3W0rk2Aldsdt7prrnlaKMLC9%2FbwGOqUBVD5s78%2F38KAO2yF%2FdscsMUAQTeUW083pkloF%2FUNwF%2Fil%2BpJhxrxLVOc23WsewxKhb3Frp0JPUMpfK%2FcHkfKOZMvKtgd58axwkOW2kRl51mUsMWdG0VOYBshSaro%2BiGt6W7w4LPW63uL7hUTfvcCicfwWtX%2FJRaMvP9U10VGlopnFnltDDDv49OARcpWCnfxUnz2Hgd5KIHrUJiiDWgrAIHJJoNIX&X-Amz-Signature=b5292fb8852f78c0d23d8fc272f2327cf30101355941f66d2a845032841f79b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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