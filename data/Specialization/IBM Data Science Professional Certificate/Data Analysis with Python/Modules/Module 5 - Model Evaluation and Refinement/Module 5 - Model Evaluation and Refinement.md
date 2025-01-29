

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=df4ed5a04260051729ae1e47b6b3af9fa0bd58112488d1c87a9c4931301cf0bc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=83aca804d4d51c30fabad299ebb1341ceebcb02855c9a34df2dac1aef869f685&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=cd4f33998b8c7ccefc0537ce9f346be7eb5f310202e2821636d666d58843702d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=68637038fdfec3ed2122269b1778245137b6f42c40cf72d797795c9ac5de05a2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=c4fa15aeffd98799a9556e989dbdde8f4b0033f61cc123997f30c9f55f6fd7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=4941feb23a903a09ac8907d6e11e37c89cd84ee5cea0588f8ee996e9c19f1e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=cff58125c407de6e89cd7d01a10bc4841d45c1364b190f35203cca53f762e1b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=d64cf54f4cc0538f97a757cf406e26370c733e64d9dd2fbae8fd11a6f843cea5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=f3a86cbff9a8856a113f49ad7c82a794a3e5c93531e6bfd0fc84438e06f2eca6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUXAF2DU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAPt5XIAg7dKoAKtoafLtP79XtIDum1apnzgazmK2%2BBAiAGJFFsXe2596BwWhzH90iqwNd3lppm1LMnNA4tsh44hCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM91jOuCKeuonx6rc%2FKtwDR0EdFjQIBxWhxLlJmMWJSspyJ8jJbaUu%2FQYUVcS09flrUb66J%2FBTeKj1gcD6Fy0AoVYs4gKhed6cr%2BGbOCyHj6fhd25jEGyqmhekZBRkePoOAPqEMYnZFcl6OKXjEW1oR9LzuU0TOuOqN7ahOgxKFvlZh0szqmDwjxIHhoxRhMA1toN5HmAIN77vSUCgJaQWEb%2BiSMuZVmcLHfOsW0xH9S%2FaKAJRE2nEC9idAp3Q%2FvlYeCcojzubmI3EatWX54veqSbfZxunumv62ChKvf2pjS1kTVHAcJwF3e3ZrBsz7hM14dfc86lQs0CMhelMMKrkQOG46IKSPUoB%2FguKbtvEpwuxz%2Bw3Wtw66nknYO7kWNE9J4ar2ZWn%2FQqbrfchR9O%2BWc1HtBOmeQBq34FVCjruzxjNbTaj%2BSsai44hhXyLyNLMPxveHBTqUV7o%2FZA2cQa8zX6DOoflSxuO%2FLQFSYs%2BVhNgl9YCDCRpBlLn3oDFwgEwAjMLpQA34gsf1StRVXzZnM%2FNLxpkXKyAy3SdgZvo0KmzqqCfQaYBVt0EunWewnmG%2BWwujLBIuZOLg2vhUChskTNEtgVZTcL5Fnnog7GXyRgs6xexzdbqU4uW2ksI6xLf7P5yKyKZAf%2BItfgw34PpvAY6pgGF8Bb1ytSMlWs6jwOSVtdZiz3vuuf9pnXJgME2gt7okOEe1OVKqROnpNC69WEycIbX11frAfA8AjltL3S%2FwXya4pHIEOmuknmIOpG1LNxpWq4llVm4yZKdoqTLfrVa%2BxqKpTtqlecdmAB30R7BOqGRqYW640ImZaIO2a1EVX3kTLks3Dv0GTwjsqLwKw4xw%2FVNwWBgowy%2FGQHB02K2QWjxkbGK5WzS&X-Amz-Signature=e463c066bcd5d31720ff56e84e7adb2e73ec732719f776610ac227efd665ed20&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUXAF2DU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAPt5XIAg7dKoAKtoafLtP79XtIDum1apnzgazmK2%2BBAiAGJFFsXe2596BwWhzH90iqwNd3lppm1LMnNA4tsh44hCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM91jOuCKeuonx6rc%2FKtwDR0EdFjQIBxWhxLlJmMWJSspyJ8jJbaUu%2FQYUVcS09flrUb66J%2FBTeKj1gcD6Fy0AoVYs4gKhed6cr%2BGbOCyHj6fhd25jEGyqmhekZBRkePoOAPqEMYnZFcl6OKXjEW1oR9LzuU0TOuOqN7ahOgxKFvlZh0szqmDwjxIHhoxRhMA1toN5HmAIN77vSUCgJaQWEb%2BiSMuZVmcLHfOsW0xH9S%2FaKAJRE2nEC9idAp3Q%2FvlYeCcojzubmI3EatWX54veqSbfZxunumv62ChKvf2pjS1kTVHAcJwF3e3ZrBsz7hM14dfc86lQs0CMhelMMKrkQOG46IKSPUoB%2FguKbtvEpwuxz%2Bw3Wtw66nknYO7kWNE9J4ar2ZWn%2FQqbrfchR9O%2BWc1HtBOmeQBq34FVCjruzxjNbTaj%2BSsai44hhXyLyNLMPxveHBTqUV7o%2FZA2cQa8zX6DOoflSxuO%2FLQFSYs%2BVhNgl9YCDCRpBlLn3oDFwgEwAjMLpQA34gsf1StRVXzZnM%2FNLxpkXKyAy3SdgZvo0KmzqqCfQaYBVt0EunWewnmG%2BWwujLBIuZOLg2vhUChskTNEtgVZTcL5Fnnog7GXyRgs6xexzdbqU4uW2ksI6xLf7P5yKyKZAf%2BItfgw34PpvAY6pgGF8Bb1ytSMlWs6jwOSVtdZiz3vuuf9pnXJgME2gt7okOEe1OVKqROnpNC69WEycIbX11frAfA8AjltL3S%2FwXya4pHIEOmuknmIOpG1LNxpWq4llVm4yZKdoqTLfrVa%2BxqKpTtqlecdmAB30R7BOqGRqYW640ImZaIO2a1EVX3kTLks3Dv0GTwjsqLwKw4xw%2FVNwWBgowy%2FGQHB02K2QWjxkbGK5WzS&X-Amz-Signature=f39205cf089939dc5068c3ff568ecf6b998f94d1e822ce895e42b2cc17678ac9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUXAF2DU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAPt5XIAg7dKoAKtoafLtP79XtIDum1apnzgazmK2%2BBAiAGJFFsXe2596BwWhzH90iqwNd3lppm1LMnNA4tsh44hCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM91jOuCKeuonx6rc%2FKtwDR0EdFjQIBxWhxLlJmMWJSspyJ8jJbaUu%2FQYUVcS09flrUb66J%2FBTeKj1gcD6Fy0AoVYs4gKhed6cr%2BGbOCyHj6fhd25jEGyqmhekZBRkePoOAPqEMYnZFcl6OKXjEW1oR9LzuU0TOuOqN7ahOgxKFvlZh0szqmDwjxIHhoxRhMA1toN5HmAIN77vSUCgJaQWEb%2BiSMuZVmcLHfOsW0xH9S%2FaKAJRE2nEC9idAp3Q%2FvlYeCcojzubmI3EatWX54veqSbfZxunumv62ChKvf2pjS1kTVHAcJwF3e3ZrBsz7hM14dfc86lQs0CMhelMMKrkQOG46IKSPUoB%2FguKbtvEpwuxz%2Bw3Wtw66nknYO7kWNE9J4ar2ZWn%2FQqbrfchR9O%2BWc1HtBOmeQBq34FVCjruzxjNbTaj%2BSsai44hhXyLyNLMPxveHBTqUV7o%2FZA2cQa8zX6DOoflSxuO%2FLQFSYs%2BVhNgl9YCDCRpBlLn3oDFwgEwAjMLpQA34gsf1StRVXzZnM%2FNLxpkXKyAy3SdgZvo0KmzqqCfQaYBVt0EunWewnmG%2BWwujLBIuZOLg2vhUChskTNEtgVZTcL5Fnnog7GXyRgs6xexzdbqU4uW2ksI6xLf7P5yKyKZAf%2BItfgw34PpvAY6pgGF8Bb1ytSMlWs6jwOSVtdZiz3vuuf9pnXJgME2gt7okOEe1OVKqROnpNC69WEycIbX11frAfA8AjltL3S%2FwXya4pHIEOmuknmIOpG1LNxpWq4llVm4yZKdoqTLfrVa%2BxqKpTtqlecdmAB30R7BOqGRqYW640ImZaIO2a1EVX3kTLks3Dv0GTwjsqLwKw4xw%2FVNwWBgowy%2FGQHB02K2QWjxkbGK5WzS&X-Amz-Signature=52c733969d9c5f526a0184184004f00f5db77882bdc8c502e2f2517e1e69af36&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=937d8d55b0bf7adb9d98cb6769e6eea03412fcbe5c0f0b649fcb340a7e552012&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=5165de2985368912481921ba59917d419514918b491f5a746e7b89661ff4fe52&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=c539979d518015787f6b12b014da2c34d1f4923f5b5d300e563f2712870e3e5b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=bbe938e5f9be342245d2fdbd6a7cbdb4126a08911421a4a48a4cba27ce3a6248&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=9ecd5e2d4bc162be8b18e6372c2bf80889600188263904282305e62ea706f260&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTWQYPNQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGzw24XM9JjFnFkX%2FI3u0bfNw%2FzSY0cByl6xRq%2Bd%2FG%2FAiEA5DXdOi92bU1TyDdh3VjENEFV%2FvXZfsBtEoIPFJYdPFIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BHtQ6IiwYB9OQICSrcA6ZO8NHmDuOxOCFbRrs%2FQOQC983EpMFyD93Q9%2FYoy2xki0dVQc1rdyisSHFg31f2dxvqmyDqzVyjvt0%2F20kKyXICP5HhqUXJY8CavgKjZlmVV9A9l0CdfQmH%2B0PZfvX0rPolPab102%2FAfXCpYIqf8cWfipzFCHt%2BGnnH%2FvZSvD5Q52Xg0HKeN8W%2B7rGw3nlETXn8JDitdMP4PoK%2F4WJT0SHDvj%2BA3dvvcRNHJrHSTRMEHZSaUfI6kL4xX1O8WgZTgF0M128jRJgau%2BDR3oU%2FkaIavuaGETlA2WYSOYkamdO9eAdmU3HosLwSAck%2B5VSF3exf3GE2xYkCSb11Hb6sCWhpCf7ai628t6HO7%2BKWRsHW2cRcGJQGT%2FtoRyeQ9tA2lgJHWCzwHVLxT6POzk4wrHxnLREXBR%2FDNM8Sa4IVWS2OI8BgyyvqMZashNRiJGNyxquRkyMS82uoSLMQgJoqxUPJ%2BOLmPU%2B58oiUW%2B%2BXLj6%2F%2Bau5GmyGz%2BqUh7JJQjMwCojiEKHw5UWJ4dSvvQyaBY%2Bh8jxchY7nnGHUXurx89sQEf6N0ZVi4i7un74autk5V%2F0GDurrwEwgOaCvkz1P9isCELwJDzGRnbM4Q5glJ19aSXJr7wadiMYTGm4IMOqD6bwGOqUBzIM5zUTwtnjlnu1z55XaJzP6dwCU30qnY%2B96kEDO3ejQ2Go%2BJhOrYm8m9yFVraVEV6ViQOrX9rAPGUOPYRhRzl%2BJ4A%2FLDXTAb%2BbwX1qLVkNdt8WvenA9F035J5j4kzqL48%2BpKIHWOVsKK4OQjgnm75diEgHIH5b0dVlweJbJHtj0SxSYeKTqz1CB3QTGIkO1W6lOzWM%2FFCIWQl1ZuRiu9iMosAby&X-Amz-Signature=8386b06fcbb4dc63ce6dedae5becda2e7dbe55bf0988596c6cd52ae6768f123d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZI6EIJT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqhNbC%2Bp8o%2B7xy%2FVbWhQ6j5Z6Sv%2F4TbnP0q5xSLkErIwIgd0p8Ja0kEgm5ffiHEoxphQFGHSSC6B2wcgvxit%2FEyigqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUjvBHcPRdRoxnM1SrcA4OTyIwuJIi49HMNiWrqJpvD6AAfHMkvGrCIQEaEEf48Cxzci4yTVBHTjO94gkGBdwp2S1M3Dg%2B7o3jCLI3BImfwryQfg%2B091x%2B0%2B0eT0OFu3OgSy0QQ%2FKAHgEGJFtTnIgs%2FQucruLZja7YF4WhmACWhSS3bFuwL2ZfJbplemInNshxbVEAh%2FunD0C6Ccgwpy3b%2BIU69A2POoMKEyKko5blczJSseJQOBdIzfbwUznyhOQsJRFSHi0y4FbjM48nZpFDSH%2BXdVShOfTVL7KblgJ0QIClh31rAX4UvYil3qp6HUhzD4TC%2BaDvn%2FxwVbBiFghKrEL%2BsQHHwu7xX9aK%2Bd4XULWo90NlGJuPuFtXYd216o%2F22AFLOomIgnjwx7cDPMaenX8A2PX96uqpOBm3puIrREb3d9cPeRPAGkbrDWkofRRDxnMpnS1ipEKn%2FkOkppwfib2EFwPMjAQ9QmT1Wu14XhcwiJxGOCX37XmB5Mzs0WcPnbSZzBp88BfULkrU%2FqOnED1AXuks8RNmOAArcYYuE3UE5u9cDbuTmdkBqsAnUFHO%2BDJszU7xT3IDpL27bD%2FruhT4AaoZg%2BaamTc0P9vbLFfXUX4flNLL92qu7o7Nt1Hh6UnloR9oWlpEAMOqD6bwGOqUB73FS0Crv1nx%2BnxAEXQxIjmvuI5d7sUWF0E6jmo%2FgoBttvxOrpVpbi5NYLMUhNvQ%2B0JxWFDMlOMBEcLqH4vNZzI5mPL1YeQt0Lp4eWk%2FxgbzEYB730KgnILFIjIwg9GQL1I4ztL5cAhtreQ62t1QCTwib0NYfH1%2FhB0C7p5fm2nnKkN36mrFHcxtXndYFxh9ZRS92rLp2Jg4Vd%2Ff0juCNVTnraxHm&X-Amz-Signature=e324bb2c613b66e06ae7f608a20021bb3936441adaab36559e659e29055572e9&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZI6EIJT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqhNbC%2Bp8o%2B7xy%2FVbWhQ6j5Z6Sv%2F4TbnP0q5xSLkErIwIgd0p8Ja0kEgm5ffiHEoxphQFGHSSC6B2wcgvxit%2FEyigqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUjvBHcPRdRoxnM1SrcA4OTyIwuJIi49HMNiWrqJpvD6AAfHMkvGrCIQEaEEf48Cxzci4yTVBHTjO94gkGBdwp2S1M3Dg%2B7o3jCLI3BImfwryQfg%2B091x%2B0%2B0eT0OFu3OgSy0QQ%2FKAHgEGJFtTnIgs%2FQucruLZja7YF4WhmACWhSS3bFuwL2ZfJbplemInNshxbVEAh%2FunD0C6Ccgwpy3b%2BIU69A2POoMKEyKko5blczJSseJQOBdIzfbwUznyhOQsJRFSHi0y4FbjM48nZpFDSH%2BXdVShOfTVL7KblgJ0QIClh31rAX4UvYil3qp6HUhzD4TC%2BaDvn%2FxwVbBiFghKrEL%2BsQHHwu7xX9aK%2Bd4XULWo90NlGJuPuFtXYd216o%2F22AFLOomIgnjwx7cDPMaenX8A2PX96uqpOBm3puIrREb3d9cPeRPAGkbrDWkofRRDxnMpnS1ipEKn%2FkOkppwfib2EFwPMjAQ9QmT1Wu14XhcwiJxGOCX37XmB5Mzs0WcPnbSZzBp88BfULkrU%2FqOnED1AXuks8RNmOAArcYYuE3UE5u9cDbuTmdkBqsAnUFHO%2BDJszU7xT3IDpL27bD%2FruhT4AaoZg%2BaamTc0P9vbLFfXUX4flNLL92qu7o7Nt1Hh6UnloR9oWlpEAMOqD6bwGOqUB73FS0Crv1nx%2BnxAEXQxIjmvuI5d7sUWF0E6jmo%2FgoBttvxOrpVpbi5NYLMUhNvQ%2B0JxWFDMlOMBEcLqH4vNZzI5mPL1YeQt0Lp4eWk%2FxgbzEYB730KgnILFIjIwg9GQL1I4ztL5cAhtreQ62t1QCTwib0NYfH1%2FhB0C7p5fm2nnKkN36mrFHcxtXndYFxh9ZRS92rLp2Jg4Vd%2Ff0juCNVTnraxHm&X-Amz-Signature=84d184fbe340e277514551693550ba95f281ec4b6d963f2d9e4450d5202c5e82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3ETPSPZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDFoBr%2BquKklRL3rUiXqbc2CRA%2BgIxw3zZC5cAJZmckvAiEA5FAvWDtFJkVnGeBr9seMj91K8Ny8cBkZ0WgLNLuiyAsqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGHCe2enssAAl1aECrcA2Y8WOqdyXL4JlwbHRdWqhbb4gc6jtD5yFZcwf3HUD%2BAxlbNGOlxxfDM1hl36Ko3Q%2FQ9LDs8ZiCsJEAUSADaRWGET8uo4%2Fh9LA21rhjE8teBqskWu7EBF9xe1B9lVuginNP23gMoCGjo1SNnLIN61tPoxfb3rrp1DlKaHcs82FD3wKDDpnkCUu%2F7oWtBVlTx0LVWx4srwkWuG1Or%2BPuW%2FuPBU6qN4y2OrKrGQmYKC9hTv91i3ujAlHCaQcc1qsCu6svBD6X%2FD%2Biu3xXii1uiCYLEG%2BybfwGQqdoYBZaJgyWrLTlBV%2F6bjtlAZAKduPnGN2LuXKW%2BgKZy3P7GAuimU7gbS%2F14h%2BntWwh%2BzKL8fTQtVyrWDCgVjtNcCAZywObG8N9bMukOwSPdr4uQAFyHpJlD4ZTq8I0K2Ic3ieWEalm87Q781c59TUYBOxCnCj21PNaSpgwTFCVHVzhcSRkfuHX5mru%2FwHD5UnuH%2Fjg7THpXl8bD8b556r3FLox7sie2HKnth1304KCBgctu7689o3uud2WEWeCHLb7w04jaPpdZ0p3EY6ddgjirY5TAD4hc0LqAVo%2FnYGk9okPevCXoOu8Dy04NlO2X0UgaIsxkZsLrK4AHbG7rTAzkOkZsMJ2F6bwGOqUB0Mc7hO3jvsi3IzrWGtkzEWAdgoamRKDDXSCOS04OPuZWS5c4NKxjGu2J8XGvLe%2FsmUtfsldxhy0mJu%2FE0KMs0i5O2TqMWUy9dipxig1VXW4RsCXX9BkxuchGiv5GrdFEj9ddz6bZgw9TIPRuG51XOIYEygl4N7hpxMn58YdRV41%2Bfgk5TKr9QKwzvweP0rQNHsPH%2FCtHxXYeJqSrARrqH023EW9Z&X-Amz-Signature=93707f06235d019a52d9b41fd809d57bc1020bf8c80c698a7a6549f83de740d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFFC2NVN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2Bs8aExdIH0P%2Fm7e8tu2Yd8Hhgo35Pyd5vcOAPqWzjRAiEAhRfpwW%2BxvkT3Q5484CFS9mv2AMKTdRoMzk4NB0haIvgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnZ%2BUbuwcgWg%2B9AwCrcA1NUz3RN7pN0eFud8qltnirbn51puVoY7OXTuM3UDJSmKv%2FKQoiNaH4cqM3FfVfJTSFnENzGyCPW3DNmHRCkf5BAEUkzNoiqv1MtTGvE8wilhLZmxpSbr2V83E99NEz%2BYFHltllKkqJMLY3D4OEt4QF%2FdgliuQfT5jeDkGpFHbXj84TH0PdTJwfZ5njBb6oKSYClDDbWtwW%2BLuEseGbb3ak7%2Fm%2FdwXh5qNnzTOGQPh%2FAl3XloPfuc8JaF1h2DSQvy9NKKbbOoLpdUkDgDQzbfTRW%2FG%2B5C%2FvjWo1Gw6z0fbWrWMw6mJiiWb4xd3U6Qr9kku3p72sFGA8fGwEWaEHWbCyBLQHMtlkoBtrpb%2FExL4EEpl6b6Isg%2FcwKNiEka28gC2BpLh271b%2BtS3K9VBzEzY%2BmeCpayd17nMNuByQCSWx4HfN6b1fBXmn%2Fa%2BMnoR%2FOSybC7%2B3ij%2Bc6pM40%2BTmD9XBAlfBZcOJZBOwiN76FIpMRunqPEBHQc7mrRbJFeWsXGZmXHphJNHIlBpj4YWOu5echd0DIPY1zQyxPNdWKYhk6wW37Y90cpazurTWbGKjnR4FuhHvmVDNH1XFRp22nAvK7rm65popp1Zd70AQqlAH6Vj08yYTTMPOz7JnlMPmD6bwGOqUBqK1Zh8fipZf74PGP97ziIdcHm8eaTPqf7m1hBVYs4gFGoTV1GqSnPdIYPZMK9ZGoW%2BNDZ2Zi6bz6qzemWu%2Fvtqur7Q6kO%2BnURQB%2Facgy0ow5tFzUjA96ZI0l5tQFdBj7zNi8WkQNYZ4rOCwNqaZs4X%2BaLhiESu0qf%2BDo6WewTe8JCqMryAa2VRyWpLOhqw5B%2F3qsIsYfI8M0wTjdVzBbvYQdt0%2Bb&X-Amz-Signature=51731af1e282357d757c4b6aee78277a4915de2a0eae92fdee2b39eea9c90be0&X-Amz-SignedHeaders=host&x-id=GetObject)
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