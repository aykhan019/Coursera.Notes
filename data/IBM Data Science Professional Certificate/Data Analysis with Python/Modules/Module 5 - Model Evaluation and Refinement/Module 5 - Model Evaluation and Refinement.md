

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=977683cb65a20bf67c2d53642261d8d249a3116592893f77d29fdad51e77931d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=11c0a29e3db096c40d18a312da6877467aac1f69256f6e9cf0e028f3fb329bf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=c293f02887bfe1ffa202161cf59efa7f38bd390ea59142fb3c019b1c4287d806&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=784480e75d596f46795c07b367fc9e9c84a71f06a3c907fa704b2fc597576fd6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=7eb741c232f1fac5ad68bdb8bc215c11b7b5be02b1c7a2aa624a3305f96aad0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=75769b4fcf91bb2bcf6b8f61f5cded24964202548c48d084808ed1e076439546&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=151ddc1735a28f1f8423947da0f84ad4959726abb03dc609d2448aede0e13666&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=ddc2634a3e612d3959d018ecea65bfc05fb1442a31e95b7d914798863c3c1b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=6243cb7eb94097617444f5b996c7b2be22f396cb837a0e09fb3ab6cb2aa0d041&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOZFN5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICgiCIMP7xuirJJPHaPpOCso92nk0xnyW0nS%2F%2BDkw9FPAiAEd3xOJGpumaZCJbonsENyaW9QmLoCoY9Tjr4Akg0vXyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMraJq4EWpzWudfvevKtwDYol49lu0VXNa0SYSx1yeHSis6BLtTpovXU2OR%2F5VtmiOVkavA2CeJ2%2FcUCUJvjI0vNmKeeqNm7OJ9%2BMP6O0sk96nl99yV4uk8UEtkW0ITpDZLLYDCfBp4ORxufn5qJY7jXnYfsA2FIUjJ%2FvTO9Riv6cugd39LWcMV3CLRpiT%2BlOorrYwIdWBLA7sRH3Emhrf5kElyvLiZMggAvD8kvPMsZe3F9fiDWOQqpJa%2BK0QPyaxFZJxlXgRxWy8JXs69ntkV1nraJ9uphyRptcE8EFuyuEGx4vRnDQFWL8EvoQfYuae2Fk7W3fGXCWdOj789gwkdJZHhloj1Vw1nXT%2Bh%2FuIu5wPTTRwM3KjVlVBXsLYzaqcO%2B7lR7rHFNuRrJPyVETdT%2FZQqc3b2VSPEg%2BI5bQlU4nU2QdAGdouo6BBqMOv6pG8n3v8DqeybqMyfyqfoxrUDX9ANDJEYgI2ryFbSAvVi%2BEZ5F0NZeB6OohG5yN%2BZVbCDphgRPWTte0mzSx0DcXocpQOIlR1a9EHAIyK1QKCigh1v4ClOmklNjpE%2BuPQxV%2BOwyIEYy2ww%2FIX1fQROAKm7BjVi3etDNM%2Bp60G6cpzHBg%2FXCarnNnkbl1zaLewb2bwjk4MKsVmVs2PE%2Fgw0dKCvQY6pgHL7oDTYHmMdJBxE3NXaOLycwvjwGKfd3b5aJjIhrzeml%2BCDipPOdlr11mf6muTC%2Bg9D8CVhI%2FsgydlGrjMFsCFO%2FKQwes%2B7qsmj2CZ%2BJDFGKGmlbIWcut80l8pI0oAu%2FXjgCFf6YAh3jWnf4TcAoW9kDHC%2B2J5hpEVa9tAv3eCrJAVgrsO464lNwNZCdRuvgpQyEgNZ%2FVqALeACv%2FNtQegEiuwY0nO&X-Amz-Signature=2f1585a35d13a1594040965bad5163944540115085e619adda642df834574b29&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOZFN5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICgiCIMP7xuirJJPHaPpOCso92nk0xnyW0nS%2F%2BDkw9FPAiAEd3xOJGpumaZCJbonsENyaW9QmLoCoY9Tjr4Akg0vXyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMraJq4EWpzWudfvevKtwDYol49lu0VXNa0SYSx1yeHSis6BLtTpovXU2OR%2F5VtmiOVkavA2CeJ2%2FcUCUJvjI0vNmKeeqNm7OJ9%2BMP6O0sk96nl99yV4uk8UEtkW0ITpDZLLYDCfBp4ORxufn5qJY7jXnYfsA2FIUjJ%2FvTO9Riv6cugd39LWcMV3CLRpiT%2BlOorrYwIdWBLA7sRH3Emhrf5kElyvLiZMggAvD8kvPMsZe3F9fiDWOQqpJa%2BK0QPyaxFZJxlXgRxWy8JXs69ntkV1nraJ9uphyRptcE8EFuyuEGx4vRnDQFWL8EvoQfYuae2Fk7W3fGXCWdOj789gwkdJZHhloj1Vw1nXT%2Bh%2FuIu5wPTTRwM3KjVlVBXsLYzaqcO%2B7lR7rHFNuRrJPyVETdT%2FZQqc3b2VSPEg%2BI5bQlU4nU2QdAGdouo6BBqMOv6pG8n3v8DqeybqMyfyqfoxrUDX9ANDJEYgI2ryFbSAvVi%2BEZ5F0NZeB6OohG5yN%2BZVbCDphgRPWTte0mzSx0DcXocpQOIlR1a9EHAIyK1QKCigh1v4ClOmklNjpE%2BuPQxV%2BOwyIEYy2ww%2FIX1fQROAKm7BjVi3etDNM%2Bp60G6cpzHBg%2FXCarnNnkbl1zaLewb2bwjk4MKsVmVs2PE%2Fgw0dKCvQY6pgHL7oDTYHmMdJBxE3NXaOLycwvjwGKfd3b5aJjIhrzeml%2BCDipPOdlr11mf6muTC%2Bg9D8CVhI%2FsgydlGrjMFsCFO%2FKQwes%2B7qsmj2CZ%2BJDFGKGmlbIWcut80l8pI0oAu%2FXjgCFf6YAh3jWnf4TcAoW9kDHC%2B2J5hpEVa9tAv3eCrJAVgrsO464lNwNZCdRuvgpQyEgNZ%2FVqALeACv%2FNtQegEiuwY0nO&X-Amz-Signature=7187335bcc245d15d8ba476791eb2855348df3b73a8d413520586c91c60760d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOZFN5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICgiCIMP7xuirJJPHaPpOCso92nk0xnyW0nS%2F%2BDkw9FPAiAEd3xOJGpumaZCJbonsENyaW9QmLoCoY9Tjr4Akg0vXyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMraJq4EWpzWudfvevKtwDYol49lu0VXNa0SYSx1yeHSis6BLtTpovXU2OR%2F5VtmiOVkavA2CeJ2%2FcUCUJvjI0vNmKeeqNm7OJ9%2BMP6O0sk96nl99yV4uk8UEtkW0ITpDZLLYDCfBp4ORxufn5qJY7jXnYfsA2FIUjJ%2FvTO9Riv6cugd39LWcMV3CLRpiT%2BlOorrYwIdWBLA7sRH3Emhrf5kElyvLiZMggAvD8kvPMsZe3F9fiDWOQqpJa%2BK0QPyaxFZJxlXgRxWy8JXs69ntkV1nraJ9uphyRptcE8EFuyuEGx4vRnDQFWL8EvoQfYuae2Fk7W3fGXCWdOj789gwkdJZHhloj1Vw1nXT%2Bh%2FuIu5wPTTRwM3KjVlVBXsLYzaqcO%2B7lR7rHFNuRrJPyVETdT%2FZQqc3b2VSPEg%2BI5bQlU4nU2QdAGdouo6BBqMOv6pG8n3v8DqeybqMyfyqfoxrUDX9ANDJEYgI2ryFbSAvVi%2BEZ5F0NZeB6OohG5yN%2BZVbCDphgRPWTte0mzSx0DcXocpQOIlR1a9EHAIyK1QKCigh1v4ClOmklNjpE%2BuPQxV%2BOwyIEYy2ww%2FIX1fQROAKm7BjVi3etDNM%2Bp60G6cpzHBg%2FXCarnNnkbl1zaLewb2bwjk4MKsVmVs2PE%2Fgw0dKCvQY6pgHL7oDTYHmMdJBxE3NXaOLycwvjwGKfd3b5aJjIhrzeml%2BCDipPOdlr11mf6muTC%2Bg9D8CVhI%2FsgydlGrjMFsCFO%2FKQwes%2B7qsmj2CZ%2BJDFGKGmlbIWcut80l8pI0oAu%2FXjgCFf6YAh3jWnf4TcAoW9kDHC%2B2J5hpEVa9tAv3eCrJAVgrsO464lNwNZCdRuvgpQyEgNZ%2FVqALeACv%2FNtQegEiuwY0nO&X-Amz-Signature=1ce60834ebc51137878311ce9db35e99a838ddf7b964556a68d29118f0663884&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=91ae88a17a149f6bed35ed63df9e2d48a4d45f4d0e64e4d12bbc263d880f8ec9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=8621559d75235aabf51008b704e36e5d1472e1557579494bab299b5d59efba8a&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=c8ec602a872c72b2176d7e3b99eca7702642d8398fb94a9f9f2fd2da983c888a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=995a2d01ce4b1c13f3047b26dc44860de3174280cf81b69c4cf6c491dc7c41f4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=090f93bd88f7f0d442fd5ec4c0143cfbae8a48622d3c0e253020cb61582ef0e9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA2A5UMW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0oKIlGk6rMud1JTcYywy%2FkV%2BtWV2yt7Z6qxo0BWbZcAiAmvfp4UYshr6mL%2BzRGcFKRTRWVzodLRcuCc0fq%2FHv5Oir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMxcnmhFuyhZB8wOXJKtwDloqfoqsHGjY5Ox0wA%2FRXiIZ2WFuNm5wRrxCpx4Q754po%2BqBnH4May7n%2FXJQQbyngrxTMqOd8PFgiAHzrMMIdV5KJ78V3Cs2u2ojJCGmZOpFnzApLmrHmB9EDNlxqIEUHbLUoOfgkxIxRSLe0ve7FE3dXFotI%2Bcx%2FX9qOSjDTgkXL46LJVlWcbyNGNjpZOIgc7oX1mwFh%2BVQGg6BXF%2FJFMRGCB2nUUxP75zs%2FNNEwW7oHA90bdM8EjBXMCNgXuZoPI96C%2FFORUUFa2mMUDCfuo7T19GeOx%2BtAr1gRgx%2FHxKhTXn54Q0KwbeBYSdL6emf6f0gM0HNYv2deMQk4P4HbXi5D%2BaxBR4JgE%2FGL8Dzs8k59hjhIZaDtUeKyGpK5aVUgWI5efRcPt4XXcNMauofAIuTYmkP1caXt9DZuv6UHINtUOGR001vVcMK2WPmfyrxSJZrko%2BTEZ5HUtEzSF5UWueCW0nS8GsZFR2FUCgRE5wrTbaIAlqsNuMlmbPlyEmfXvtga3NxjCwqbgXyJ%2B7PlevfVvjsv%2FZtHfePiJRD9TQTDZzwVMqjAGU3WjBU6edJVuojc5zGUgSYD6aBwhQ2%2BWaQF5XK4cBL8ebl2RxL5mmOuFJ%2F0ESDwkzq4Kn8ww9KCvQY6pgHCkkrmoAhRJIUJZ5KuXodMSrbEukOafQ%2FetyTTYyzDThkL%2FgAv%2BSdApXvgQBtWvZpwC%2B%2FXRfm0zqimXYkbe%2F2H5%2F%2Bde976h1y%2FcbWZmeOvlF7PBWsqKcOmKZKI5f%2BTcQanUkuAANtmTDqWeLOIGVyWOHec5KowsXoTA%2BR8ebkBYn6ucFDwmr6%2BcPQ9aqfmEVIhcnOm1kPaXO4HkGRn5YidbqKgZicC&X-Amz-Signature=dd2c404741d0c1a882146347584380f18cb65146fcadc9d050f64ef4ffa30c47&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQL4RHTH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUrgVKF%2BVkJ%2FYOc2iw0kbynXZVQWrWVWb1XG7YeX3BowIgPHCmGq0xz7%2FR3pr5QgB2Z6kfxvVW3BPDU%2BrHu3gPCxwq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDIZgODDtRqtFjCWx3SrcAzNHqOwdhr9p6AYQ18zrbysj4RXP42%2FQYnKeAHPsISHTtrJELj5eXHiuNSwK7c9035dli4pohlZ4Hk04a7QFmev%2FNRj5g1BKxA%2B9ceZsC7hzajFEJSwopKEeN7rLgjsy845Bp8F3xzuDr8eO5H37TeGlUYI%2F9E3tni%2B3lkzAwj9MaHD4k%2FdsaXtM6Ru65t8fXu6LeXz%2FNTenvdDx1pz3n%2FFcnZRoifGNXObaxygcJIe2bTY2PC08FF79PWqUhwV3xyhQxaKNZIIRDANTIiY5rLtT7jsy%2FkUe6LreVzQEDiyS45IKpG1%2FlyU2I%2FRNm0UqJMC1Rnhw67ioCKDl9o34q1QzoSJTxLfLxDc4dsES14PGAWZjiFxh70hUBZ90Fbitih8gWOlga3ZG4hqDJslDehcqiejqFO5SVbJ%2F%2FpUk%2BA%2FU5j4Xt%2FeswjO0N6elcA3BkNwEr%2FhQCbS75jwviO%2FWa7x577mwIfH%2Fl5aIGMIvR%2FiUVTz%2BK3cKaqrWNyATH6q1vGEdgqShnKBkUbb2EewjWhAt%2FrmTAHJvOJn6ejH6rZ0JWHEyuo9juI6HHxMGME79EIr1EkR9HzOEwWVWMkS7gFfjG6%2F49stT83uOU5Pwj0PPSGJOrcTmtBJA2L5zMIjTgr0GOqUBj56WNV1hkRpFAmFv7mXP2rF5vXBNf%2FeC8ZpcHIEAk%2BJCkJmbP5vYlH6Mnan%2FgNStBza%2BChCtLy3R1tbo3xfju%2BLYPJb%2BzCjxNHPcHSezkUA2cdb5AGAd%2FvPclnXpapXmIx9tEYMEXCy4Zpqq582OI2wNZRvWK86iK%2F5NLd9Wqp3O%2Bdhbv4Fws9Z2RF%2BYttHqaWBdGWVfr0TFq04oLSmiaSAsbkqq&X-Amz-Signature=366d920e1132c764ad32762a33bcb562408b45a9f8b14b77922a0c0087b67fe3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQL4RHTH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUrgVKF%2BVkJ%2FYOc2iw0kbynXZVQWrWVWb1XG7YeX3BowIgPHCmGq0xz7%2FR3pr5QgB2Z6kfxvVW3BPDU%2BrHu3gPCxwq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDIZgODDtRqtFjCWx3SrcAzNHqOwdhr9p6AYQ18zrbysj4RXP42%2FQYnKeAHPsISHTtrJELj5eXHiuNSwK7c9035dli4pohlZ4Hk04a7QFmev%2FNRj5g1BKxA%2B9ceZsC7hzajFEJSwopKEeN7rLgjsy845Bp8F3xzuDr8eO5H37TeGlUYI%2F9E3tni%2B3lkzAwj9MaHD4k%2FdsaXtM6Ru65t8fXu6LeXz%2FNTenvdDx1pz3n%2FFcnZRoifGNXObaxygcJIe2bTY2PC08FF79PWqUhwV3xyhQxaKNZIIRDANTIiY5rLtT7jsy%2FkUe6LreVzQEDiyS45IKpG1%2FlyU2I%2FRNm0UqJMC1Rnhw67ioCKDl9o34q1QzoSJTxLfLxDc4dsES14PGAWZjiFxh70hUBZ90Fbitih8gWOlga3ZG4hqDJslDehcqiejqFO5SVbJ%2F%2FpUk%2BA%2FU5j4Xt%2FeswjO0N6elcA3BkNwEr%2FhQCbS75jwviO%2FWa7x577mwIfH%2Fl5aIGMIvR%2FiUVTz%2BK3cKaqrWNyATH6q1vGEdgqShnKBkUbb2EewjWhAt%2FrmTAHJvOJn6ejH6rZ0JWHEyuo9juI6HHxMGME79EIr1EkR9HzOEwWVWMkS7gFfjG6%2F49stT83uOU5Pwj0PPSGJOrcTmtBJA2L5zMIjTgr0GOqUBj56WNV1hkRpFAmFv7mXP2rF5vXBNf%2FeC8ZpcHIEAk%2BJCkJmbP5vYlH6Mnan%2FgNStBza%2BChCtLy3R1tbo3xfju%2BLYPJb%2BzCjxNHPcHSezkUA2cdb5AGAd%2FvPclnXpapXmIx9tEYMEXCy4Zpqq582OI2wNZRvWK86iK%2F5NLd9Wqp3O%2Bdhbv4Fws9Z2RF%2BYttHqaWBdGWVfr0TFq04oLSmiaSAsbkqq&X-Amz-Signature=02dc751516e9f89d52df5c7aa82f5d7401e7564f937c429a7ee3d1633968ed4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676P6VNXD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC9jm%2BCXX7cq7GpjS4VY8HIbAhl0X%2BLFJgmKc39rOgGIAiBn%2FvI3urOMb02XHNiXy2po7D0XGyB2ppLgaQ6adrZnAyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMf2yMCRzcuwUgJzpOKtwDiIhhwyCPvrl%2Fv6bDMtgYaIlGH0q6wzoDz9EkpxAWexqnn3zsgWf4vb7G%2BXDSm1kPlCA%2BB%2FO%2BeZpiuCIZx0ruM%2FrxI7jBMJAQx64CFEy6Lg6%2F6j2%2FGQFx3ng2wsLRV%2Bpd1CvZpywEOjFmOtPLaqCasSZ7GYV2ed8n1A3kzavHFYJGnjPiyHlI57LIXbAVxW9%2Bp2qJi%2B%2FJNfuhF8dlTBVQnQ5pOGLV%2FdGHCMxFxSL1AJUhQP0RdwtjFMDNqo36vsUKDbuIhrH%2B1czI1U4a%2BOFpvCIOZp1IQsaP4z3DigG%2FqB%2FPTZPObtON3DJy8u%2FCRaoAowPjFJ%2BocPh%2BfLBQEDP5vQJ4ebqTyxM34Y4tGkp3V2026pPwpv7fwbIq3lexdFDpD7NcPlw5Q5NlmbGsBb%2BQ3ngVVnzE3I0oIstvOCirFicJ2K7PrVBd%2FNyavm%2Fygyv5La0s6GKNScdE%2Fj%2BO6nmPSLwYc0Oln%2BRY3GlzZTgY%2BpPmk9EkkROsrWpNABDNR7Tqi8mfRN3fW9%2BpMx3ptKvsu94OjkWmy4vSClK%2BEo7czJdn7DGmd2KiFvKlEAXotfXfWkKGg8C4Sc1OJL37eOGDFrGuK%2BWekmOSJk8u%2FKEG%2FbMtAB5l6AIUP59jCyYw4tKCvQY6pgFVaPe6daXn9umQ5g3tEVoEK%2Bo6AMjGs1aK5apLiMfoC02OHBApl3uoHMT5mZH%2B%2FvnHHG6jroGL%2BuuVAR0FIE5Ag0S7dZgqwN6xI5EQq52Zt6f2V0HjI1XSgrdh%2F6RySfAmw21G3Fz3TXtQw08ZKl7xZf58VV%2BKoKb59qPgsLuSAwy1j4rzdsLhBOdPsRD9T1c8py1n2mG6SHEikTw%2Bn2eottelfAHj&X-Amz-Signature=8e7d48a3b1472db0c16ccdc3194dbd3cd29c12858e7f51c96c057f1dcc239f7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXZLCNA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfndoKC9LN3h2ZUAtrfs33%2FJHHt26wjkOCRqrYYtpv4gIgCG3dr5RoMlQnFo%2FeHg7Xj9LaRddgivf9F%2FSuq6CqFbkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDC0VcwhMswMmwRWRnyrcA2eVeiDTIvxznsDchqvwLhrq0IF6jvSrfR6hv%2FOxT3tfPKgkRFk2u7EnHfpsQn4N%2Bj%2FUUwBue41qsNUvKGd%2B13Oq5vNVBslqqZHnV5qiUpW%2F8P8kopIHg%2FVm%2Bon9SYl4bYVz5jln20AMlc%2FZ6ueYv%2BO2XtHo4o3alTktj3SgHTya7ya%2B3WY6znqM8y86drI27eywPk%2Bf4kiW7pteUWGHsblIVz%2BHXrACDyeJFtcZAU4dtwnm%2B5SN7OqNQtYQpMtmGxEIJs%2FsJ9WgXdTJDywCVX0Cn%2FxoLgA48f7LA7Gr6qUxbmaC0qlxRfMKWoU72v%2Bi7wdiQON%2FYOf787LDh%2BNNUgitCQSlHR2C%2BIIc7vJoQtW70pjwlWIw4a98HHMmUFhCYass0T6Ccl7sHPiVgchMlqRJfU99f0M%2BWLi0ocJERE2TkcrR4DHodBcHXwwB3g4liCJVCSAol5o3i2e0Ol9iZcVJuA2sepQXl4R9C8BFXkznLaTdEOzjuS7a%2BKQ9%2FVHDNRWW0uJdC6C4dqCJd3VPdTvtpSVeeke0csqPpfRHcXPkbAmEXdZjc88NN5iRVpLSVu9nY3yMwHzPY4549V7MLj0Kd1a0s8gGuki12LDoTM4vAY4xwu%2FCugbxDBpjMNzSgr0GOqUBfbHCGnp%2BcYLJPSrxKN29viZpmE7f5ERVAsI8PypoESEekXcNXOYkMt8e4TOKKklKObym2QP16kPrznA%2FOIgFVnXrV6pTQ8vTTEb%2Bd7wt6k3SjTI6CX8IJfPZYKrka1s5H4dtseI20MNerQQs1f5iHH%2F9PmcDmELFnS%2Bds4%2Bu5972B%2Bkr0Dp19%2Bp9Y6YM75bqnarBjNMmytRwNWF7hyOAtfDA0gtM&X-Amz-Signature=5113630d2265d5e459fc747e6998c1411d9b5ca0f29aaa06b6e4c7fa9bbf56ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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