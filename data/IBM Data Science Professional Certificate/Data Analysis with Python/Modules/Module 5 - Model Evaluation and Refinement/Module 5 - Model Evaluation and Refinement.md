

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=a4a043251cf173d9429cf2ee4efa0a5629817edb7b5c3e221c90952efcc8a2e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=0c47130e5820e18b43e0b16f20b97de321db536d88ec8ebba52b9dc83259e5da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=2ca7974841cec8a2ad6a90ee420c5e352d01ab91790ddf29e76bc35b0ca1f785&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=fe6e6a14bdb2d41885316f476f5beba8e4deec1686b13ab4ee5165800b92ed7c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=80fc6fc30d17c7a57873d3acf37898012a18a84896908af3eb3f814baf9cbd77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=f38b68bdf014f862377c09a5995ffc6e58bed75d74dbc54ce11ab06d384b81bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=a95a504e31337823b46e945fd5d3ed8938f6d13ce2f4ae59b3129fff2ac777cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=553392c58502705a831f7892c4a48699395bf52e0518caf8114a9e31dc24d9f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=d92a6c138f325481e432e8dce96edc0ea2f8877dd5241fc4255c73e3ed3323a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPL523MK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWOYltHZ2tb6PETd4cn2RGqDUCJ4sJACuEsI4TChGzEAiBA3%2BJVcSFAXG6yP1tl8W2E0wrKSxRQhmadZkPB1fgyHCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi9VmtZFVJbLyMUvkKtwDLumrYZnriV4cFuFe9jRJ2YkFp8POwHYQBwQKe9ahKMHTKQuAidJG7iQTA784Gtembzq1tAmde15lSnOQTyiVfw1kBHKwAFeWIeSJsuyW734zzrhzBN0sbtV0d1MQCs4Y0Nm7Vr2UWeEAPKyVnZc0f2c53AWbdFOQEcrmg52Q44wdkDNX5QeKplv2XP%2FLLlPkW1Nfkk3%2FzW9RgXeCN%2FWk7UejZittI%2BHcOwSBensKpF7E5CP6xJMznpytDGOPYAnB%2BRPGsHmU4C0DA67wQZs22LxuHB5eCyi9%2F%2FN338ZfWmH%2BkLmhtJJY%2B5HH%2FF%2B%2BaR4UbExHQz6tAjJszlVlG%2BVYko5cXJ7mr%2FCOc6pR10pzFrfgb2CkhGk2r4VfEM8kju9LjMMjRkhdmEDKnPrKDAvyDLaZuazXYXnjMZmF3VGAvc1nmCN9kAhKymn23%2B5ywM4yYQPm9BwRLTLoFb%2FzHlE2xDmuqx%2BTGn3KTSubkxBacOwl6SYjidvDj7tB6rqXmWXSO93f6H09kjEUf%2FIsTLvuJA9H0k9BbQxEMjmfOU1oJn0cDMnyk7FEuipFnRyVcMGZOYBJ0PX9WkBe9Jux1GZmd3XUfLDqb2Mk5t5TYL0vQxZGcSIIF%2FvS8QwZbeEwoZz8vAY6pgGf7bXZeuzejFjQAtriegJBRLElbKGz4RhbyeF%2BG56QKmwSGrUG7U1riBe7mHSY1UwnHaePQ88ZmN0dy08sY6omw1uR6RdLWwBKgXB%2Fo04z8A9lj5R%2BG5eLt3kl1nL9eWTILqnoYHdxDOpfVDGKp%2FL5YRjGlHBtqT%2F5%2B9rz%2F4qjsxnkIJX%2BKqFZgIeZ0API7ZTrpmNxAByy1Rvfg9xEE3Fh9mymNC%2BB&X-Amz-Signature=4ac4685f513baff2cfc8ddd222e52b4fbf2b990664d32ba6dfc259ed8dacf1c4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPL523MK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWOYltHZ2tb6PETd4cn2RGqDUCJ4sJACuEsI4TChGzEAiBA3%2BJVcSFAXG6yP1tl8W2E0wrKSxRQhmadZkPB1fgyHCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi9VmtZFVJbLyMUvkKtwDLumrYZnriV4cFuFe9jRJ2YkFp8POwHYQBwQKe9ahKMHTKQuAidJG7iQTA784Gtembzq1tAmde15lSnOQTyiVfw1kBHKwAFeWIeSJsuyW734zzrhzBN0sbtV0d1MQCs4Y0Nm7Vr2UWeEAPKyVnZc0f2c53AWbdFOQEcrmg52Q44wdkDNX5QeKplv2XP%2FLLlPkW1Nfkk3%2FzW9RgXeCN%2FWk7UejZittI%2BHcOwSBensKpF7E5CP6xJMznpytDGOPYAnB%2BRPGsHmU4C0DA67wQZs22LxuHB5eCyi9%2F%2FN338ZfWmH%2BkLmhtJJY%2B5HH%2FF%2B%2BaR4UbExHQz6tAjJszlVlG%2BVYko5cXJ7mr%2FCOc6pR10pzFrfgb2CkhGk2r4VfEM8kju9LjMMjRkhdmEDKnPrKDAvyDLaZuazXYXnjMZmF3VGAvc1nmCN9kAhKymn23%2B5ywM4yYQPm9BwRLTLoFb%2FzHlE2xDmuqx%2BTGn3KTSubkxBacOwl6SYjidvDj7tB6rqXmWXSO93f6H09kjEUf%2FIsTLvuJA9H0k9BbQxEMjmfOU1oJn0cDMnyk7FEuipFnRyVcMGZOYBJ0PX9WkBe9Jux1GZmd3XUfLDqb2Mk5t5TYL0vQxZGcSIIF%2FvS8QwZbeEwoZz8vAY6pgGf7bXZeuzejFjQAtriegJBRLElbKGz4RhbyeF%2BG56QKmwSGrUG7U1riBe7mHSY1UwnHaePQ88ZmN0dy08sY6omw1uR6RdLWwBKgXB%2Fo04z8A9lj5R%2BG5eLt3kl1nL9eWTILqnoYHdxDOpfVDGKp%2FL5YRjGlHBtqT%2F5%2B9rz%2F4qjsxnkIJX%2BKqFZgIeZ0API7ZTrpmNxAByy1Rvfg9xEE3Fh9mymNC%2BB&X-Amz-Signature=59cf9f2a269b4956976a33e5c30ab9dbc6c02164dd3083bd521269cc6de3eaf7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPL523MK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWOYltHZ2tb6PETd4cn2RGqDUCJ4sJACuEsI4TChGzEAiBA3%2BJVcSFAXG6yP1tl8W2E0wrKSxRQhmadZkPB1fgyHCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi9VmtZFVJbLyMUvkKtwDLumrYZnriV4cFuFe9jRJ2YkFp8POwHYQBwQKe9ahKMHTKQuAidJG7iQTA784Gtembzq1tAmde15lSnOQTyiVfw1kBHKwAFeWIeSJsuyW734zzrhzBN0sbtV0d1MQCs4Y0Nm7Vr2UWeEAPKyVnZc0f2c53AWbdFOQEcrmg52Q44wdkDNX5QeKplv2XP%2FLLlPkW1Nfkk3%2FzW9RgXeCN%2FWk7UejZittI%2BHcOwSBensKpF7E5CP6xJMznpytDGOPYAnB%2BRPGsHmU4C0DA67wQZs22LxuHB5eCyi9%2F%2FN338ZfWmH%2BkLmhtJJY%2B5HH%2FF%2B%2BaR4UbExHQz6tAjJszlVlG%2BVYko5cXJ7mr%2FCOc6pR10pzFrfgb2CkhGk2r4VfEM8kju9LjMMjRkhdmEDKnPrKDAvyDLaZuazXYXnjMZmF3VGAvc1nmCN9kAhKymn23%2B5ywM4yYQPm9BwRLTLoFb%2FzHlE2xDmuqx%2BTGn3KTSubkxBacOwl6SYjidvDj7tB6rqXmWXSO93f6H09kjEUf%2FIsTLvuJA9H0k9BbQxEMjmfOU1oJn0cDMnyk7FEuipFnRyVcMGZOYBJ0PX9WkBe9Jux1GZmd3XUfLDqb2Mk5t5TYL0vQxZGcSIIF%2FvS8QwZbeEwoZz8vAY6pgGf7bXZeuzejFjQAtriegJBRLElbKGz4RhbyeF%2BG56QKmwSGrUG7U1riBe7mHSY1UwnHaePQ88ZmN0dy08sY6omw1uR6RdLWwBKgXB%2Fo04z8A9lj5R%2BG5eLt3kl1nL9eWTILqnoYHdxDOpfVDGKp%2FL5YRjGlHBtqT%2F5%2B9rz%2F4qjsxnkIJX%2BKqFZgIeZ0API7ZTrpmNxAByy1Rvfg9xEE3Fh9mymNC%2BB&X-Amz-Signature=4b351126b9c9c80c13380312b55430b4cbfab725a825647deb8cb889fc299112&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=ddbce0571f0ad3acac8796351ae0c40b00c108e259227c81074ce77d2c0afe77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=d15d383c7ccbb279da1f5cfc888555f9f85ef14a90a815b5083049893823ce78&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=f0b0b00f660729c4f6b9e61603e0eb914b759657b6cc0177f0bfb638ef69ea32&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=15daf5cbf874a6ffac10b92bfdbf52b2ced2c0f609db393427ee8b044c719e33&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=b7294b5ddae7dcada9fb6a332ed544ca5482cafd033bf48d08e5ddd889e13444&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXCDF7NP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUsRjPIu9sD3wuFooUW31P2aHBPhERyNXLpIhU0ndY3QIhAOp5RYUHY6qgTH4XZTc%2Fs%2FBE9yrk2%2Bb6813gWkf3%2B1CtKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV0a4vohbPnNGJiMIq3AM2dUFL8q3zxkX1tOG0q%2B02WeVOC91TBnC4%2FeSsuRqwzVA9j%2B8UILOAW7UHSVKyk0Z%2FewbbP8vVNzBrNnzHQ1u3eLhPZUCmvOsHcLyIP0faSwMCttb0iJbfIhBHNzTFS%2FheaGLgJtYYM32NzrqA83en7EPFdSC3edn16flDUtcCzIPxtGhL%2FQpCpxHnDW%2FDltjqbRILKGn4ZacdRUjMTAcgxGKKHBPcAqAPsUm03IDVXO730qjRPaWt5cWduoFaTZQQe8Fio6nh2Cj2uuyGO3xDdRYLmz4qgqPgLeD6udh4giRcuqK863lZgGu2TKUiq8FAKCx518eH6YZ6emNwyjSYIa8nb%2BN%2Fk310qW3%2BF6lfgi9HQItqmpdH%2FV3KfiMaBjDckO%2FCuaLAtr5ypf5nAY4dNb2%2BEfyk9cfLKjPgPx8POyaW8%2FoTTxoZgNzhcugUXih63YCCj%2BmfnhuTSnIQgisU%2BtF1M7ItTN5A3jG%2B7Nh7B01%2F1BflC%2Fm7ZgNPnSgEXgfxwK9pPJ41wdSFO%2BdfV7LHlU3%2FApLpDQpqmGewX2iIrgSSWOX2ZRQSLujRUiraeQeae0oOFqCk9iwv3MRL%2FwbtVWoNibnQ2xQSZCvwSR5eEMJYTBMnUFkN20OVLTD5m%2Fy8BjqkAS8VuXPrUY5ne8YOIX321N3xkzPcfGVFPaT7jQSGiYJ2lh6to2Tp%2BVIfuCvNawaeZ5b%2FsQfxy8dK1I7I8CEQ%2BqT3ldsFQ3K4f7Vaoc%2BD%2Fznoi26R6IXgQ%2Fan3bmmTmG3IvS0BREu8lMpoFIL%2F2Khnva%2BSJCgVDVo%2FPlj2u6x%2FLmlBfDVH9%2F8bwSXBP4Ui%2BycqzSinML1mtwTn1ZUjvxyBma78iUK&X-Amz-Signature=4b2086b7cbddebbaf2187baf6582f563096efacf3e1b0d831d3c68e43b03943e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HGBRYN3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe1QipV4Rq8wCcz8PcgaEbJUoiRvbO5w3ckqI3Ec3hLwIgVgKvM%2FRxihJQnoTvigAOYl4vndygfdWxarh7w6T8uJwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKVdrTb0kfOZDCumSrcA1WuvLPA1MPbtItuGf3BuurBLU5bEWSicjF6lHnMKbxgUHzw5NmfH2GRa4P92deIlnXGpULETxlPb4C3nAii8w9AeRhlgN%2BC5UGEajuhXzspZfMUoW1z71eg3tfoL6r4BDxrv09fW1li1Y1qkXiGwtNo%2FldBtHv983Umj%2FSLILpibkl0KHslR5UiHDf%2F6gSSAn2FLN1NMSMZ9Q2vLMWBo1HChdgvsafzq8C2G%2BVbdnXDZ8zCj4Xxh5zU9pS%2FhzLoBOC6Nvw7ojz1xo6s1zCEY3Vk8fxPkPw7HThh5ZAr%2B1dADupYTjTvrcyKF6SupgAdfzU8Zb4rH1b8DCjywEXv6jzrI0mRaPjuXj3EaeEU1lsbGKEnjlz%2FGHQAnXAyZBtp5gke%2BtXSOjSzVofMzU34aJuhw0pJq5qQZg7qWii%2Ba2rh43IBcRD2dlIGtIswUcyVdvTeIoDOYSd0j%2FpA6lfbrCuF4HtEaVyCoS2oUHF8prDLXWd7BNFSuYGYXxqNeSsoRYUT58TrsRUmtN0wcqofe9hssZjn%2B6ntiE2JFMzxvayPwFAqZ74Fac8kpc4K81fvqTi%2BUwXhRPYYaZI%2BXhh91lGiuutbfZVxWbh5oaZcdTcY%2FUKhOHVnTg4FXlpOMJmc%2FLwGOqUBooed2UpH6nl%2BYayZInedqjjck%2BSVVd2RXl7bEezJnQQqR5Qn5ZZslE7PBgnxBomMd%2BKFHtovMNH%2FteXsKs9alKslPDXJE2aKjxSnkwv7wvzpwFSSQvbwcfNqgL2%2Bel%2FbWptnJd5nQlFGEk5LEL6mmRB1tS1ry2TUiSzvBPy09GcGdxp8fjGfkWeQHkapM1ZK3Q2EVnmF7TUdryiPl%2BxzGvOZ02eI&X-Amz-Signature=e47e38ad588131ec38191ea79dfc6f984cb35b43681d20f4a61ed0810ec5d361&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HGBRYN3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe1QipV4Rq8wCcz8PcgaEbJUoiRvbO5w3ckqI3Ec3hLwIgVgKvM%2FRxihJQnoTvigAOYl4vndygfdWxarh7w6T8uJwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKVdrTb0kfOZDCumSrcA1WuvLPA1MPbtItuGf3BuurBLU5bEWSicjF6lHnMKbxgUHzw5NmfH2GRa4P92deIlnXGpULETxlPb4C3nAii8w9AeRhlgN%2BC5UGEajuhXzspZfMUoW1z71eg3tfoL6r4BDxrv09fW1li1Y1qkXiGwtNo%2FldBtHv983Umj%2FSLILpibkl0KHslR5UiHDf%2F6gSSAn2FLN1NMSMZ9Q2vLMWBo1HChdgvsafzq8C2G%2BVbdnXDZ8zCj4Xxh5zU9pS%2FhzLoBOC6Nvw7ojz1xo6s1zCEY3Vk8fxPkPw7HThh5ZAr%2B1dADupYTjTvrcyKF6SupgAdfzU8Zb4rH1b8DCjywEXv6jzrI0mRaPjuXj3EaeEU1lsbGKEnjlz%2FGHQAnXAyZBtp5gke%2BtXSOjSzVofMzU34aJuhw0pJq5qQZg7qWii%2Ba2rh43IBcRD2dlIGtIswUcyVdvTeIoDOYSd0j%2FpA6lfbrCuF4HtEaVyCoS2oUHF8prDLXWd7BNFSuYGYXxqNeSsoRYUT58TrsRUmtN0wcqofe9hssZjn%2B6ntiE2JFMzxvayPwFAqZ74Fac8kpc4K81fvqTi%2BUwXhRPYYaZI%2BXhh91lGiuutbfZVxWbh5oaZcdTcY%2FUKhOHVnTg4FXlpOMJmc%2FLwGOqUBooed2UpH6nl%2BYayZInedqjjck%2BSVVd2RXl7bEezJnQQqR5Qn5ZZslE7PBgnxBomMd%2BKFHtovMNH%2FteXsKs9alKslPDXJE2aKjxSnkwv7wvzpwFSSQvbwcfNqgL2%2Bel%2FbWptnJd5nQlFGEk5LEL6mmRB1tS1ry2TUiSzvBPy09GcGdxp8fjGfkWeQHkapM1ZK3Q2EVnmF7TUdryiPl%2BxzGvOZ02eI&X-Amz-Signature=11f8ee2f1b531655db0e171c2aa0e23ba2acf6118472b106ea1222ff8b716c4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GQODPKD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHObC8ADvJI1uGGvDioFZQPZg3%2BbC3UwDZWLWMe8rDbxAiEAlPjO1XE3H2u0Iiw6mcVaATzoG9Q47qPsfScjHkKJDU4qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FcdKyOXZ1cfQTiayrcA%2B%2BWsaoDwjtgzigJ%2BVvupe9BSEQ9TDCOPmW6YH%2FWu37UOy8dLwZGXr3jmCpPkbcBWFRmihBsqVdW5V2MdKhcswfgmLSl1qpQs3uJGdfNCNg2hHVgIiXM8e2kxs2DoiUBJd6pwp0jz%2B2b4E%2FqrQhfoYhTFQcuTxh%2FkVA%2BPEiDziW%2FbZc3E4Kn5lG8L0%2B6swDzLLwB2lNRyi0cR0uEQHy7hwIelSbm1s8rSq6A5raYJ9namuMird1s7i7nlj%2F%2Bdm09SYz532hwvY9QK2bbjQxm897huAUe2lOf6mlgehYEV5hZhzOVeKLb6ej%2BsjOSj8rOeIwpczayUtdvessdxNn3H5oK39mAVOFwzpSSsmN6GBeDSFBiNq3Pqk31424ygGQ7GZpAVsP%2FxWoMbTaA5Qu8OEfxtcfj4umpFPAiT5ltMfrr6%2BWP2z8WzJ0sOTnF9rC2jBqwHLl2oMh2EI9WNI%2BWQUT5yLvL7Qpmms%2FL5eG2dRjBYZs%2ByxX94mDwo8J%2B1gyHM4jHWXEovDBmUMxZeeIRVz2%2BHE1HQ0E3g994CbB1MWqIQMJ1UA8M%2F2I65vCThb8H2DuzzYflDjkyqQ39U9yfKAYx4HPYzy%2FI7EAhDbYK7pgl3mDyTbz0YtozQDdFMKSc%2FLwGOqUB3YdVTRuuLuMVSTZ9XlOczPQP4Qf%2BYFRM2e43RcIoDUDoJ9qGpl6WnHSmzIaWBmY%2BgMxrD8%2BU%2FBBzi3hjPH5rJEdpQdSnimqyctPh9qYcNBRxDU9%2FIl3qRceMRa2XNdWABQ57lFyOyljehhGLDrf9WFk5CYnw5lRWsBcQBxxizZDGVNb%2BIOiIhwz3lvMPs%2B2niHzbk6%2B4u4Pl1I4M431LMgKH8jIw&X-Amz-Signature=fcc0cdd383af1c051d50477584a37d486531d5edf0b9a9ee3a4bb6284277c107&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RDFWEZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxnzfKgfD7OgvpIqAz0tsBy819Wgqu0IK%2FLzQB7DT0zAIgfkpPwMSdUUpN6Gp3yViQsUmtYKCTbfxcRZAu9SPV7bUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZhAOObQPjB8oiWOSrcA990wzL20NpJsXg5LejX1UiL6zb5FBlt%2FQvjDdelORyDni1YgUzpTvQWWq7QwPOV6VyE1OAl8ueSf3O3at0VQ%2FuTrplxv5H%2FfSQYEWjDU536tkvW%2BSz8KbKpnMO8MIJ7vjtd5UvLeksnRtmSx76CZantABaZotOD4SSo4VmkfjxLyrGm%2F6wizd9Rr41g0HnE2%2FlLE7%2BbQuOrHggiWamYrPajdpqW3CPNw3AeT0u3vomyM5MOqmuIWcg5lA9uEFjVOIXk2FwXQyiOeCz%2B%2FKfiw2OO0v%2FyFnUX8%2BXiWTv34pK0hEgedaOY4qiw0Zine6NJrHkkE7%2FlxnkZCZDZOWCjSQY%2F3NSANu7OdWcmpKkj5lTSR3rvmmZ%2Fa72xxAEYO8bcsUjUxdsijztcfeF5J7SDsxlK8Z3aHbAM6luhJKFLbiKp2wllrB8iCaPkfIJmRvr2Ex6iAdg9ylXH79lW%2B3cNleQ8XYmzWUEwjm98fcUkl1zstfL%2B516ukUBK4PSzL9RX7j75DaFUIMzOZI6B2GPLv7n9yQVeYHshAiZydU2ykI7ho4vIHDGxWjYzXhMr%2B8ZX03%2BPckzmBE1QoNbLuHDLt02Phhw15KOsoA8fM8uYJaOyVmlrgUGkPNBb1M3XMOub%2FLwGOqUBvLJLJhsAcJgosTlTKRR39%2F%2BYr5Tax%2Bqh7W7S6NqFAvNXxbOubk4Ls3RjKOBo82Y1hjLMUG3gyxTOhSBVFTpu7XsSUxUHVJTnPf1Q4vmHe9ic0uq%2FNrpZZJ0IwaKd4Y2%2FIrAOGV6AvNmXxTEVoCDbM7mInjmkwChdka5SElIPEBN0aAWJHlNm7u9BGlffdltgOl3GfAni1ai5TxK1KYBN4tNQg56s&X-Amz-Signature=ec59cf102076d0efc48aae5c04c88aa07d0f7f3ef88063fc28037342d442cf21&X-Amz-SignedHeaders=host&x-id=GetObject)
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