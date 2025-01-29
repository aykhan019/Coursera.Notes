

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=79e172ae9337cf11bd7189fafb55bfd42de2e0d3e0232cbb26c14b70154fe66b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=6ae24352dcf4786513a9198081dd53f73d2c274aa4c2953e8e82feb85be5e0a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=18a79139cb5a15212cd107079c4ee261a9c4ae7b106dbde20b77efd225fd613a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=52750739948fe5df1aba26847b94acc6863280ed4138edf9387e76bfa3fbf02e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=935ba57ab1c3fc3e456c7e20b7f61a100a506d921489d38738b566ddd3053f02&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=9a1a729e3105d7a692ff65518f41b068709f97e438555e1ee47142ed058313ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=3fcfa945f3e1eab107843685bf0a2b8efc60d4dae22da30c1063bbf04aadd73c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=f6f01bad949950b5a6d8f89d1e186ca0f46b0f1dfbde6fd14eb94e12df2463b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=b61ad8e42b117a2cfb6a597260f331399eb697d9b97166ff15360bb4205ec385&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6VVHKC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCG2vt2JgE4BtQS0vOhpiO6izbtffD41LWVIUzJm8pTxAIhAIrwFnYcy8WyenR%2B3aIYTcuXxmNO9J1HrDQOu3M5aqXVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqQ5fJpXrsjM2mt4Eq3AMn8kep9L02sBVLNg2i3HijKBWFp0Gr9z5Vt0yNc49Q3tXxpb9joHKm2z9b3M%2FcHICoUHZQHREe0P0mkv9RpcH%2BnqT2XVl4lVIwTwT%2FDZKmS6O9ki55JHjcCmKRWr2fjeuum%2B5wR4OowVeo1R2h1L%2FbCK1WKYisukexbOTSy%2BZW0wg6mBAaNQU3ly0x%2FYsvSZELGrsOXCCkGbc0oQrVP39HIDdPBIWD%2BWqv0otO0K2PuhyDGHIcz3Al3S45GSm1jl%2F2BtC8X9Bqf0hmGNv2%2BOolhwrtlkmt2j%2FHEPooJIDSAp5iAj2FAtUeYfena3QNG1lkIzNhtzZKab0%2BK%2FheMNHjjl9SWIeqXrz1FRAxPSjvllh%2FCRVpYy5j8bwXsCqstqIdlMSXmXEqQ9rKozHAetvIDEYyA%2BCYffrOFRyUpeLdnIJIVbO%2B7uDS5xDlR5j%2BTXOe4vFWKJT3yJ08fWR93eB3n174ZIiYf58lRcy0yejGw%2FzL1bkgOth3JroKdQYDFYXMS9Zeqlb6mtxl3urEBCn8P3QzxSfP70UnGOYDlfOxQtW7sTyb5SlKyAhqzALgp%2BgjqAvNWVF8RnpHj9LJS5aER4aXC2%2BOrxCKQoDHaWhfL%2ByCaJVV3hg%2BS4sTNTD05Oe8BjqkAaON750JOLIBoyC8fDCBD1yBRKAJ%2F7ghcqUcm23bklDdd4jJ2rDvW0kN%2BPCrvhsR4KpZeSdBqSmlIayZi1DUn%2Bx5hGYTJX7oR3HCuMP1lk0EDafMiBxgWxqt515fEQbtRsjsAeG%2BhPMRfMvbHRdTgP7bxWiIhRQdDTOJfVTg9vIYf1bwnQuzyXebIa3KZ8sRZFczeG5waciEcuEa4mV%2BenrxSB8E&X-Amz-Signature=43eb4a55e95ef00b754f144f66fc4ffdb5d05a65501bf581f8123666842a69cd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6VVHKC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCG2vt2JgE4BtQS0vOhpiO6izbtffD41LWVIUzJm8pTxAIhAIrwFnYcy8WyenR%2B3aIYTcuXxmNO9J1HrDQOu3M5aqXVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqQ5fJpXrsjM2mt4Eq3AMn8kep9L02sBVLNg2i3HijKBWFp0Gr9z5Vt0yNc49Q3tXxpb9joHKm2z9b3M%2FcHICoUHZQHREe0P0mkv9RpcH%2BnqT2XVl4lVIwTwT%2FDZKmS6O9ki55JHjcCmKRWr2fjeuum%2B5wR4OowVeo1R2h1L%2FbCK1WKYisukexbOTSy%2BZW0wg6mBAaNQU3ly0x%2FYsvSZELGrsOXCCkGbc0oQrVP39HIDdPBIWD%2BWqv0otO0K2PuhyDGHIcz3Al3S45GSm1jl%2F2BtC8X9Bqf0hmGNv2%2BOolhwrtlkmt2j%2FHEPooJIDSAp5iAj2FAtUeYfena3QNG1lkIzNhtzZKab0%2BK%2FheMNHjjl9SWIeqXrz1FRAxPSjvllh%2FCRVpYy5j8bwXsCqstqIdlMSXmXEqQ9rKozHAetvIDEYyA%2BCYffrOFRyUpeLdnIJIVbO%2B7uDS5xDlR5j%2BTXOe4vFWKJT3yJ08fWR93eB3n174ZIiYf58lRcy0yejGw%2FzL1bkgOth3JroKdQYDFYXMS9Zeqlb6mtxl3urEBCn8P3QzxSfP70UnGOYDlfOxQtW7sTyb5SlKyAhqzALgp%2BgjqAvNWVF8RnpHj9LJS5aER4aXC2%2BOrxCKQoDHaWhfL%2ByCaJVV3hg%2BS4sTNTD05Oe8BjqkAaON750JOLIBoyC8fDCBD1yBRKAJ%2F7ghcqUcm23bklDdd4jJ2rDvW0kN%2BPCrvhsR4KpZeSdBqSmlIayZi1DUn%2Bx5hGYTJX7oR3HCuMP1lk0EDafMiBxgWxqt515fEQbtRsjsAeG%2BhPMRfMvbHRdTgP7bxWiIhRQdDTOJfVTg9vIYf1bwnQuzyXebIa3KZ8sRZFczeG5waciEcuEa4mV%2BenrxSB8E&X-Amz-Signature=608394fe60255d21da4b39a90497fecb3109cf86c954e3b80c47cdb92927d3ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6VVHKC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCG2vt2JgE4BtQS0vOhpiO6izbtffD41LWVIUzJm8pTxAIhAIrwFnYcy8WyenR%2B3aIYTcuXxmNO9J1HrDQOu3M5aqXVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqQ5fJpXrsjM2mt4Eq3AMn8kep9L02sBVLNg2i3HijKBWFp0Gr9z5Vt0yNc49Q3tXxpb9joHKm2z9b3M%2FcHICoUHZQHREe0P0mkv9RpcH%2BnqT2XVl4lVIwTwT%2FDZKmS6O9ki55JHjcCmKRWr2fjeuum%2B5wR4OowVeo1R2h1L%2FbCK1WKYisukexbOTSy%2BZW0wg6mBAaNQU3ly0x%2FYsvSZELGrsOXCCkGbc0oQrVP39HIDdPBIWD%2BWqv0otO0K2PuhyDGHIcz3Al3S45GSm1jl%2F2BtC8X9Bqf0hmGNv2%2BOolhwrtlkmt2j%2FHEPooJIDSAp5iAj2FAtUeYfena3QNG1lkIzNhtzZKab0%2BK%2FheMNHjjl9SWIeqXrz1FRAxPSjvllh%2FCRVpYy5j8bwXsCqstqIdlMSXmXEqQ9rKozHAetvIDEYyA%2BCYffrOFRyUpeLdnIJIVbO%2B7uDS5xDlR5j%2BTXOe4vFWKJT3yJ08fWR93eB3n174ZIiYf58lRcy0yejGw%2FzL1bkgOth3JroKdQYDFYXMS9Zeqlb6mtxl3urEBCn8P3QzxSfP70UnGOYDlfOxQtW7sTyb5SlKyAhqzALgp%2BgjqAvNWVF8RnpHj9LJS5aER4aXC2%2BOrxCKQoDHaWhfL%2ByCaJVV3hg%2BS4sTNTD05Oe8BjqkAaON750JOLIBoyC8fDCBD1yBRKAJ%2F7ghcqUcm23bklDdd4jJ2rDvW0kN%2BPCrvhsR4KpZeSdBqSmlIayZi1DUn%2Bx5hGYTJX7oR3HCuMP1lk0EDafMiBxgWxqt515fEQbtRsjsAeG%2BhPMRfMvbHRdTgP7bxWiIhRQdDTOJfVTg9vIYf1bwnQuzyXebIa3KZ8sRZFczeG5waciEcuEa4mV%2BenrxSB8E&X-Amz-Signature=93023a4052eeec9e5f31d84349b094a0a81cf425c9ca5bde97caf8506b1965b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=0df480fff72bef8c525e46898fe89d885a28eae0e4ad43358cb693396fde1234&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=0e74f1b6d9d1bae308dd7af2519baa11c3ee1d85c112539458c20c158c1565e2&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=2c6c0c2fa5c6ddcf24fc260fef77883aa2de14c99296324eb7cb5a5a6baff94c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=5e06935f41aa786b70c826c3a6750cb02f6921164e56294bffd0843b3661ce22&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=cd2d9c4fb70de20fd39226f9fff46178108d90ee5fc23ec0ee56dbca9970a61e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FRNUEUY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6lqY6tzBuG7N%2BL47B5bqEZkmmxDBOeonvN1wlQhYOWAiAUWC%2FYmQplRL9EbbPxbW54fHsn%2FtLtr5t%2F25VbbeMJnCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeBg%2FvZ0SxYrBY%2F6VKtwD6WExTw2d38eT8UsMakJFadIcKZsvQ63AaVxLkNumQcvqmjm0nLJQoj87xO9tBb7ZNAXuBfmO0NiQE%2FqszZizaxhwfHs%2F8ESiZ0UdJfJh5rQYW%2F1eqHSZ45LP2cnXMqfR2m3DxZMNYD5SKyKYNR59A6UNmMKHSeR9X7swOugTkxHR%2BLcA5B6VUdy5eT4WxV1u8n6uGbELbjyFkf3i5VFqJL8WYUFLb6gwBiMOvpCMlGRUwDSMYG8Do30YebKrVKBfxL8bz0zH54Z3ArgQAjgoJMtBbXti%2B8ExepktEL%2BFv3Pw%2BQXX0Vds4uFwcK3dnrptptMbD2aqcR2diELen9ZsaCQka%2Bmp7IvTu1qgRlbzlRpnIBJHrm0CxPWphE8mjBXlyPXsPkIlZJitAB8h61QdGj6N%2BdO1KQ%2F414Rw%2F4DdQbY%2FrqQeRUyZrIzVrVfWxaZzkdUfMEQlloTunuM7fsdscjB7VXNJ4AOgICj8RD8jCL%2FuSvoNMdY4rCLKK6Lbr%2FsJyc3TRww7Sx84NTGLCUSeBvXOMBLPN03%2Baz%2FK2j6euvU6zIDirG3GHmr5p0IoxbFgLYI0uz42fRq6ZGc5TpxoWu6BdX5G5dTCBNFHRgFbRrcEJGDHzgjiCrpDpW8wwP7nvAY6pgEkheii9%2B1FmlA%2BU3hR8mI%2FSHTYnnuEyiTZ%2BLxejawzQoMUKl4J4zq5UpN86sDHbxCNuQ3jV6BEsRkjCBVtV3FkpTAI34yN%2FQCwdnth0wdm6xevFWJ6AuC8%2F6jbbiXxAGK1zcoBfvUICNwZfDA3mEbOBhwqeB1yTiHTIm6haBc46JHHA%2BLaDa5JhyjtwdotEoUBu7HfBlQ7ZLC30myf3KMa0A5zY3YR&X-Amz-Signature=7b2ce479f953285c0bb34375fb656d9ed11a9047e35b943fdc44118c50ff17b7&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654XPGHNY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAp8teYuBB%2BCkRP0e5ApuhbCtbFEsUg9kggF1o1Uq04AIgWujJJHypeVUGXcatzgITh%2BlYP9AEGL6745RlHMYJOHIqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BvmDgtdRq9Pi%2FI%2FSrcA9gXkNZUv6aNBK7OlXH%2Bdm%2FoR2vLXG95x56OQJJXJt5GwqE2FCaiqOSBvTtjC0c7qdY%2FtwZxMGMYKLGTeDPrTbWAEp7OGGpbESp0%2B1Sxp3PbedAoDVArU1f29OD6nMTVNh7d%2F%2FArVHUn8849A00B%2BMsFBnsubgkoSD9iAx3jEy9QqLZqwuKxgWXXay83sFS9HgEwV6jNXOxmfeQaYnopw8ishKbBG85G%2FXzvbugslE1lWDLIVvO5tvWPfSeRJK97Bs8%2FXQ6CRLZKXkiq5SuEPlEUKNlmvxxtcD1d5CNgx%2B30TeX%2F8fXC3b3POrq4GYtZKJXubUByyAoYe70LTbpfHY8d%2Beg%2Fz9HYdwuHzA%2FpKTWtC%2FZixYsH%2Fvt5MBodtZfFAMrenvMIjPkqohS1ZQWZw9Ya3VCCQE1%2FKLKGqAY4rnu0%2BqmoyPgOHyMDLQ80vRXPsYlGxmpQ6XRCnS6WJstFadtr%2FZAo23SvqMoUdgwUSRlNFvtFgvnrrUdvXIhIVOogWF19k%2FVKbtfolXby0hMWooQvWHn1WipxT%2FRaPsA1WRG4aafKn%2FO1%2BQBswhZ8yVrtL%2BjgQuFldesB1SoOksmSf0%2FNeOBj1YGPYepEasbtQSxZr5a33Ce39EBWULPEMKHj57wGOqUBFJGAUTHkNNPYV6NgLyHRHZoNpyaQNNlWxSp%2FIJLX6fPL5pvf5ZIR7i5%2B5cBr4iWxfCPoSZMUsp%2F4Dzl5ZP%2FMOuXzaYADmXWa4R87qNgG%2Fhr1RKWFCyYNWi8oQapToYFSGxu9G5GCmlHzPHhbUvnh9585f6UgovOYqGBjgMPJQs7B5%2FRF6n76qmQSYC2vdV%2B3M2lIM19XNwml0Q5WTP6MGQhIkIqU&X-Amz-Signature=0bde0409cce7464eb3b9792bf926ac378d6f02caf4186b9f1350d3dc210e84ac&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654XPGHNY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAp8teYuBB%2BCkRP0e5ApuhbCtbFEsUg9kggF1o1Uq04AIgWujJJHypeVUGXcatzgITh%2BlYP9AEGL6745RlHMYJOHIqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BvmDgtdRq9Pi%2FI%2FSrcA9gXkNZUv6aNBK7OlXH%2Bdm%2FoR2vLXG95x56OQJJXJt5GwqE2FCaiqOSBvTtjC0c7qdY%2FtwZxMGMYKLGTeDPrTbWAEp7OGGpbESp0%2B1Sxp3PbedAoDVArU1f29OD6nMTVNh7d%2F%2FArVHUn8849A00B%2BMsFBnsubgkoSD9iAx3jEy9QqLZqwuKxgWXXay83sFS9HgEwV6jNXOxmfeQaYnopw8ishKbBG85G%2FXzvbugslE1lWDLIVvO5tvWPfSeRJK97Bs8%2FXQ6CRLZKXkiq5SuEPlEUKNlmvxxtcD1d5CNgx%2B30TeX%2F8fXC3b3POrq4GYtZKJXubUByyAoYe70LTbpfHY8d%2Beg%2Fz9HYdwuHzA%2FpKTWtC%2FZixYsH%2Fvt5MBodtZfFAMrenvMIjPkqohS1ZQWZw9Ya3VCCQE1%2FKLKGqAY4rnu0%2BqmoyPgOHyMDLQ80vRXPsYlGxmpQ6XRCnS6WJstFadtr%2FZAo23SvqMoUdgwUSRlNFvtFgvnrrUdvXIhIVOogWF19k%2FVKbtfolXby0hMWooQvWHn1WipxT%2FRaPsA1WRG4aafKn%2FO1%2BQBswhZ8yVrtL%2BjgQuFldesB1SoOksmSf0%2FNeOBj1YGPYepEasbtQSxZr5a33Ce39EBWULPEMKHj57wGOqUBFJGAUTHkNNPYV6NgLyHRHZoNpyaQNNlWxSp%2FIJLX6fPL5pvf5ZIR7i5%2B5cBr4iWxfCPoSZMUsp%2F4Dzl5ZP%2FMOuXzaYADmXWa4R87qNgG%2Fhr1RKWFCyYNWi8oQapToYFSGxu9G5GCmlHzPHhbUvnh9585f6UgovOYqGBjgMPJQs7B5%2FRF6n76qmQSYC2vdV%2B3M2lIM19XNwml0Q5WTP6MGQhIkIqU&X-Amz-Signature=41efdd6b6cc54b74f525767fda49712e645fbbb2599c925264dcd7607d5738a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NDV52NV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG24iTIPTpV5O365IFPJE%2FQAquSCw9PM4POKaxLsdcaTAiEA6KfP2teNDSub3IPTP3NOmPNcHoil1uEDxHmqSvInrQAqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIR2skok1WMO8RH9TyrcA500AetZ3VbGYTYqigRrSmLNwqq7lYfejZKbW5ICyMJ0mI7ltUd5gw2yZ6tFPKiAF2boRf0Ll%2FDPhwqXNzXXxonulywkwiDPvYKdpv7iP8gAGpEmd1BFu7zQChIG53rs55oO4cIixHh3EH721PtDbTL%2BRPIt1LhxXVwnuUaJL9lTkbWFQuhxvPfnOIZ2%2B31Vx6s885GJ9w%2FN%2Bw4s4%2FzFst%2Fq%2BBV1AgSd%2FET0BrsI8MsudAXoY4lj6ZeKRCoXLBv4GG0tJhQksms0El9KaV9ZZDlL1Pre0y0NHN7rrxSSx4MSHJ8DcfJ0uQBdLc5shDRaxIu01gEPiAZqC92j%2FYxClgLbKc9HoA02AfLd9JaxHLhic%2FJ%2Fztkhp5LsUZDGBt5bw5aetDirQVA6oC%2FDdh4m3jUn%2Fxl1ARR80J5B0RoMppqAVuyXeAplem4GJGVReTSyEJE2vO6tMieNYfIRW%2BXj1CVUlNgoWoRWbQXvE2%2FRUQQ7yNSYCWQlI6nscR0PhpGCJauFrq3tHgWa6o%2B6CReU6L8K3R6SVcbgfDeVkLJuAXkR2d%2BOYwFjF3V2dE7nJ6LEfela60xq6430AyrMKMHc9fVkNFANeW%2BfBwrw4i%2Bvsy3%2Fz7Z%2F6NNxeLb%2BU7drMM3%2B57wGOqUB5bbthOhHERCvO7QC3Wks%2BlPIEWhN8HME09A4LnYG2dUVC66wa4Vf78Fp2Db8%2F32ufC6SybwbRJN5DmBLm%2BRHz7T8cK1LYxWLB7dWcy3RCHkhGJ9TQlGgNdM%2Bg9XunWvY2WhAfnW2pfn4Ni9B5gbxZL5OxCMdhwkTYh%2Fgy0VBMoCIJhD9fdsOn0rq%2F8yPPgMW%2B%2FCOV7iSPbCJCi6HBk%2BWz9aD57JI&X-Amz-Signature=df99e891e009801d32fbf16ccd82099644087fe50e06d64a22198c10498219d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623SB77P4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6ggEMelP0nlFPJ8PhfqJ5tGdzNEDOubw346F6vV3VHQIge4iuvfRYbiAsGMXiMjDMnzyviLUku5Q0iImmpPgz7eQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3BQdvHfrHIc0J90ircA5J0UjHLXRG3sKsqixe8ocKABbfsmZmWCaznY7wdYabZ4q4I6NMDa1TfO%2BH0I8t%2FSRbKEqyG1VhI%2Fj4ZsoKvV9teiMZmJvbb8cIn0Mhb8%2FruBCIthX3ZWjxWq1NROGFM56M6HCJfFKyGtVRUZHfV5PjFONY764Zf%2Bd%2BiK2F76bKhs2zKYhe2WUQpXzIiBk82WbwR%2FNHdeJMqWjjgqaov96YbNtN7cRqPii6rBZ4kpC36m7qBv6YSgPySF%2FyxLDaZZgnxjk9QICuN%2Bh1F%2Bq0OFOi8PFYTUzFF6p42FTMhGpNEwFPLP86yz3eoUXuSfvFo0yvjOlP3Qh3sB%2FbYxd7Vu2OJQBDR0AD0%2BjqFo4iXGvZ%2FLwQKGLBJgsecCfnas2SnhinFmPgz5taqFORjw7mH7PeLcM7u6sLHfwEkpl3CfLoVFHI%2BjUpQmSJeEmLjjvxxFNohV30YbtmFiGdx5W%2FGcXbFQ3mqtDs1S2RhWUT7NCR3po%2BYtFoinoDeCDiwRVOOnhXa4qooFQCdnGOD2ucpAtdWUvUCmqWKOLGyDVGCYsJbkxlPgbWQFxcFLhTDT6VsC4J12cBugXArUAP81i5GqBWz33phmNtERw%2F1GcOAFqeCd0hKFp01UcU7RovXMOv%2B57wGOqUBbYqBnwhk7soLA%2FLypAI78k0wRsz%2BzS1sHJNqy10SYbupji9jKT%2Fo0jiWexyGIiUlU4hvqoqb%2BUTqpjhPnQpXdMgEmpzENlA6PoTbAn2F4EnF0ht55fFS2xFGrR9rKhpOtrmd2n05ipmt03yV44XTz2xXk0yN78SBNuLJZQHR9lrtgrNYzMFl%2BtnpYK0qMA6XHbuSfai35ad%2BAVYw3lkwQB9N0XpZ&X-Amz-Signature=ce074e44388c937d8e9b0b59faa6006000505fea19bb31aa746d7c1e5d7f780e&X-Amz-SignedHeaders=host&x-id=GetObject)
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