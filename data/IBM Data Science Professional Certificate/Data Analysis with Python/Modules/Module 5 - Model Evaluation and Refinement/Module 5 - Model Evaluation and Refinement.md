

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=837aa6d37c74f476bbfb7131e9bf64e498523c7887730ee2bb1abb0776831cb5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=70364257ef5f882d4302052911e1d3be5516250dd213a4b816413651ab9f6ab0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=03a92ecae5c4a7725ac3c4acce51d20042434e99a6cc6beb7175901cc0b7212e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=10e00ba9ea88094b2bbc2fcb4ae8dfbb690f966a2e2a771f17854c0fbc8b9ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=152965e741c4e2e6c19e54f89059c9ebcd3968fa1515cc31677de1e6b5ca53b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=5a7944e290ee7bd49eb9eca02e28f65bd813b3af8da8085e69e5f2b3e24890ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=e98887243e25fa116e0ddbb09fa340292c40b6f26b43be3279f55aba139ce712&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=3cc94a776224f02618dd90e66db36588b2bf85dece04fb8f540dbcbc40d328a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=69c4c3cb6c9c2d890bdb7df45cc4cc3a4a00c8fd718f9629c043b58bb0e0beff&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GTHDII7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFcKU040yI%2BJJQafD7A%2FD5pHTwevTBNKiuzO%2BSZN9zM9AiBYb8CwpdpJfh6BR%2B4xy%2FlgupfC27rm2UdPC2sJF2xNoSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM%2BxkJY4JsQ%2Fu%2FTWuNKtwDeVal6SHu367GGRRc1fqJS8QlomI%2BC6dyx9gONbuHy0TIMx6LIdrmvTGI4YprKD7Blcsw%2BYiCek4pIyC4C4IIBFdNDkIwNGjLxPd5Nmmph4Uol5zNhv%2FEtbZm0LukPw6AFOGmCWpAzajWJUNDUgIkVGXpTzQ%2FoYvJhIfz2faNiG7GaJbtiyjDZ4XCE5HqsZIohbw7n3L7R5WgQSwR%2F1MQQS1IRWqjtQrThfpIxMk2BnkLj%2BZE159u0BduGWP4AIJUyCuhMKDlvmrtSiC91O8ZXb1RFalITC552gJNVcx1LBOASYOVrCxlyQF07hh6UXOdSfBuI%2Fa8W3BMaNCYRpMjUjWDqwgENkkkKxSkRstegqVBE7DWwGX4G5z2XRBqa%2BnobDEBVq3avhllYq57Fy25O3Kdl5bcp7rYeo77wIGxpkBH6qsCfseXholXqL3%2BebF50PkvJ3LIRTtl%2FyRxdnDo6l89mnXEc5A%2FHwzwMVeYQRlNu4onPfI3w7MnSRrJvfblpYp%2FC3NJtlKldvumwdkM%2B%2B90x1uquBGhJaHXHPWevl8sgJIt5UiorZGT7CpRLCgobrmOIAynxKjdd%2FLXlnb2xqv%2BfwOrN4gTzz7NqQq4uud2YvFPXpdPPBwZSV0w3dyJvQY6pgH63Wi3hKmeE%2B%2FCK0wmhUriQNU0%2BEM5HeznO2UVV2M4ebv310nlJJS2vMpsXUDll9VmUBlLN4hKJKwZvLfL4NE3GkzIdiLfA8W3DKvjSPuvcVFfzDSx2AqnndIo60KtrPN2UmApqDMoNLDXTdKt3u8hM8efWMXdS%2B8PorTQLZEpGtBt9RYhTS%2Bf4eTqqkGlQwBg3uUbB2rLSZMC47eoDrQNdicP5BLb&X-Amz-Signature=e17e22d5171267673387f5a0a85709eb246ef129a10b2400d2db28fd90c92029&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GTHDII7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFcKU040yI%2BJJQafD7A%2FD5pHTwevTBNKiuzO%2BSZN9zM9AiBYb8CwpdpJfh6BR%2B4xy%2FlgupfC27rm2UdPC2sJF2xNoSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM%2BxkJY4JsQ%2Fu%2FTWuNKtwDeVal6SHu367GGRRc1fqJS8QlomI%2BC6dyx9gONbuHy0TIMx6LIdrmvTGI4YprKD7Blcsw%2BYiCek4pIyC4C4IIBFdNDkIwNGjLxPd5Nmmph4Uol5zNhv%2FEtbZm0LukPw6AFOGmCWpAzajWJUNDUgIkVGXpTzQ%2FoYvJhIfz2faNiG7GaJbtiyjDZ4XCE5HqsZIohbw7n3L7R5WgQSwR%2F1MQQS1IRWqjtQrThfpIxMk2BnkLj%2BZE159u0BduGWP4AIJUyCuhMKDlvmrtSiC91O8ZXb1RFalITC552gJNVcx1LBOASYOVrCxlyQF07hh6UXOdSfBuI%2Fa8W3BMaNCYRpMjUjWDqwgENkkkKxSkRstegqVBE7DWwGX4G5z2XRBqa%2BnobDEBVq3avhllYq57Fy25O3Kdl5bcp7rYeo77wIGxpkBH6qsCfseXholXqL3%2BebF50PkvJ3LIRTtl%2FyRxdnDo6l89mnXEc5A%2FHwzwMVeYQRlNu4onPfI3w7MnSRrJvfblpYp%2FC3NJtlKldvumwdkM%2B%2B90x1uquBGhJaHXHPWevl8sgJIt5UiorZGT7CpRLCgobrmOIAynxKjdd%2FLXlnb2xqv%2BfwOrN4gTzz7NqQq4uud2YvFPXpdPPBwZSV0w3dyJvQY6pgH63Wi3hKmeE%2B%2FCK0wmhUriQNU0%2BEM5HeznO2UVV2M4ebv310nlJJS2vMpsXUDll9VmUBlLN4hKJKwZvLfL4NE3GkzIdiLfA8W3DKvjSPuvcVFfzDSx2AqnndIo60KtrPN2UmApqDMoNLDXTdKt3u8hM8efWMXdS%2B8PorTQLZEpGtBt9RYhTS%2Bf4eTqqkGlQwBg3uUbB2rLSZMC47eoDrQNdicP5BLb&X-Amz-Signature=747e2cf6923c1ce3776f74ad8165e5e201472c19355c41cdfeafc0f0cadcc502&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GTHDII7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFcKU040yI%2BJJQafD7A%2FD5pHTwevTBNKiuzO%2BSZN9zM9AiBYb8CwpdpJfh6BR%2B4xy%2FlgupfC27rm2UdPC2sJF2xNoSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM%2BxkJY4JsQ%2Fu%2FTWuNKtwDeVal6SHu367GGRRc1fqJS8QlomI%2BC6dyx9gONbuHy0TIMx6LIdrmvTGI4YprKD7Blcsw%2BYiCek4pIyC4C4IIBFdNDkIwNGjLxPd5Nmmph4Uol5zNhv%2FEtbZm0LukPw6AFOGmCWpAzajWJUNDUgIkVGXpTzQ%2FoYvJhIfz2faNiG7GaJbtiyjDZ4XCE5HqsZIohbw7n3L7R5WgQSwR%2F1MQQS1IRWqjtQrThfpIxMk2BnkLj%2BZE159u0BduGWP4AIJUyCuhMKDlvmrtSiC91O8ZXb1RFalITC552gJNVcx1LBOASYOVrCxlyQF07hh6UXOdSfBuI%2Fa8W3BMaNCYRpMjUjWDqwgENkkkKxSkRstegqVBE7DWwGX4G5z2XRBqa%2BnobDEBVq3avhllYq57Fy25O3Kdl5bcp7rYeo77wIGxpkBH6qsCfseXholXqL3%2BebF50PkvJ3LIRTtl%2FyRxdnDo6l89mnXEc5A%2FHwzwMVeYQRlNu4onPfI3w7MnSRrJvfblpYp%2FC3NJtlKldvumwdkM%2B%2B90x1uquBGhJaHXHPWevl8sgJIt5UiorZGT7CpRLCgobrmOIAynxKjdd%2FLXlnb2xqv%2BfwOrN4gTzz7NqQq4uud2YvFPXpdPPBwZSV0w3dyJvQY6pgH63Wi3hKmeE%2B%2FCK0wmhUriQNU0%2BEM5HeznO2UVV2M4ebv310nlJJS2vMpsXUDll9VmUBlLN4hKJKwZvLfL4NE3GkzIdiLfA8W3DKvjSPuvcVFfzDSx2AqnndIo60KtrPN2UmApqDMoNLDXTdKt3u8hM8efWMXdS%2B8PorTQLZEpGtBt9RYhTS%2Bf4eTqqkGlQwBg3uUbB2rLSZMC47eoDrQNdicP5BLb&X-Amz-Signature=236f2769cdd8a7d748e28efa72e9eaf794b3aaca68df3b2011b5a132c9635e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=603ec2bf98af8d6f98897eaac8306feaa0b1b43dfba71e427816efa659cd2005&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=4c47d32db0b3a6997cf4c264e26940ffe353ac6337a329882f30d22cee767e72&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=0e1a06537aeee61655c35d6bfc484eca53bd3f0d7686ff43656e13d6abe9837b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=f2175817b625010081ed2b0481b62c8c1f58ad9dd9979d3a4040d4a61c3947e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=dc94df6a48de2dee15f01497b86b818edaa0a1b3bd32cec9971c53f94eb76c5c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEXFNWFB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCkcE3dBK7MRh%2BywndrAVxiOZCmucJj3J%2Bp3NFgy9EuyQIhAJEpLTAqZt%2FpqYUDxf2ecsr2CFXHYU6LzLK%2BwgkjoecSKv8DCDUQABoMNjM3NDIzMTgzODA1IgxWuJZzRhpyHvzdpFQq3ANzIOiCaK07H31hzdwBvcGzenQSkHHq9md3LW8M96wa43XPTN6n3SG91GzxDskhtJoDJYIZ8HcBNzobA2%2BwbXbcWcCitLQny1oEjqlwbqDGAs51RhpjkAj1z7UsxHdFOm%2FqayppyN009OPBUN4MtnteR2w5iZtZ0QWDBVCJqMJnQ3JCbJi4Udsg75XA9na%2FMjOtrcsor3yx81jFQkx6Puotxm6RXdADlZ0cpaa4rTB%2FsJmbLTgzX0OBYlwrwvByrXGLFTsn7T37M8iJw0ZVICwVPylM%2Fj9eEWMzYJVV7IoM4OTHFsviBayfksU9OjoeU3Cn6%2F%2B4OEj4hMtbLvRqS1pem7T8uWKDn69dVeRFrShvy0yovAHqpv8Sx8laLmlxfpCgnqy3%2F1%2FKHeSCXXXp6BhwgBLOQk2vscJ5cXjDPngeyobPfiuWq%2FpzVnxHdVOngCKWG8KmeJk%2FeeA1zfpAhO0TneM7vwwpcyYzG87iqoi7awVY5bn59aIeaRnPHTWQPUbthopo80ePd%2Fy3sD%2BE69mYUTlwN6RPA0pJ3V1PLKr4yTUbsdWtpqmP7Bu0dX09uB6TzgJSV5OqTKFPN9Tl3dUUpgPVh8oumEr%2FJ5s6%2BChpeqpzpfOfiorpvyAqmDCP3Ym9BjqkAVIQkwaTpjBBZNLoDbMF%2FicMr%2BpwQxWUjjK2ZKQ%2BiF9PQB9Hi%2B1L9lOMgxsEPQ%2Fsuu2hiE3WxMS7%2FGrvSehAapA8bwU7ztJm2zhdduraYCmMTcHXs5rXR522WZO5aIjGQWY4qdK%2BT9Ik7AeMgMcLjsT1YIANMHoDWsLaUe64nHnfQG3AbU0lLZxc9pcpbViOg8z4bKs679uw6D7cnX5ZODXPIw0%2B&X-Amz-Signature=5acbafe537250166ac9288a67394ca69deaa55daa884687570fd49e63b262f0b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCCR4PYP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCWrlz%2Bk%2F9SEiXG1IGNEo%2FN8%2FDHeZMqwCqZT%2B3Z3PxncAIgCy9r5Z1GTaGoKURF%2FH3iDm3ffZXO1kbmZdT2lLVzPHEq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDEZOuhLFkG3ldH%2FNlCrcA3obG%2F6MqS%2Bk%2F1zeRsTT2t5f%2FN4Deg0ogbbO8%2FG7GcAjWJp8WIDsLqhZuKxZYM2K2Le8IN8jNBFoNSU786H%2BmDTNBhuKosHeVU8P2p1zSucHvwr%2F%2F0fDIvjOWpbQlaesE8jYKjYUKshKJQdAvsVz5RqwkkyFH10mxqznqpoc0Lxivjo5XzQ74In6jDof4n%2Fa%2BLMPBPU6DYbIobSy%2BNavGHKV18cYdRSMxBnAX3zkxdlcTtfiCmf6vEhiZwPVSvAAKmMAUNNUIdEVsBHrICRUxu08xhZiEM5A4BXyW7jSK24EsZ08H021XJizqQ7VP5o1WPM%2BUFIiZY9O1UGQ%2BmhmmKoB%2BeqW74ZxcV4X1YTTarP5uobg5CZ9lWH0gY9zOc2sPPbHIGN5ZU2YicTkI3qq0XtPqiIIveNnlCwJWoHAhINaK5nfXK4Pn0rRiYgfyKnFTlwE9%2F6LF43l2%2Bf7uH8tJzfCXkiKM8W33eh1hJG9FQS6eEWnKkARMXdi5TjdhkYRXHg1wwNhoDZqfl9lLKz5wDZ%2FIiPQSv6hZaZ9Ry2oxTHDdAieKYXMSgg0Mg4D9sU%2BVZgKVMojyT%2F39ruoauFnt4vfDETsoQi6gb64ccBytg5RbQpy%2BSfQE6enDdY2MPHcib0GOqUBiBlZaGvrnvNjsDITn2ML5KZA%2B1RJsC8lXvxC4ZLQWlgXL%2Fcs4oR1Q8roZjiiGN3npRLmpVikdOBwvh%2B1xstQyAFh%2FB6dl3mIpSHeetzUrODy2JJbzazOGGbsTvASYhN6CLo41zFGwt3YS0%2FAQtSsFHkN1KLR9ZHpGmVHUEWQ97zCFjoEpjUMAgT2io%2Ffzo1CToTT3b3K%2BZFGt6Xjo0k%2Bc%2Fl0m5aS&X-Amz-Signature=9fd3f72677ac00d5bd771731ac33171263cba34897fbe2cf09b39fbba4ab8520&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCCR4PYP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCWrlz%2Bk%2F9SEiXG1IGNEo%2FN8%2FDHeZMqwCqZT%2B3Z3PxncAIgCy9r5Z1GTaGoKURF%2FH3iDm3ffZXO1kbmZdT2lLVzPHEq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDEZOuhLFkG3ldH%2FNlCrcA3obG%2F6MqS%2Bk%2F1zeRsTT2t5f%2FN4Deg0ogbbO8%2FG7GcAjWJp8WIDsLqhZuKxZYM2K2Le8IN8jNBFoNSU786H%2BmDTNBhuKosHeVU8P2p1zSucHvwr%2F%2F0fDIvjOWpbQlaesE8jYKjYUKshKJQdAvsVz5RqwkkyFH10mxqznqpoc0Lxivjo5XzQ74In6jDof4n%2Fa%2BLMPBPU6DYbIobSy%2BNavGHKV18cYdRSMxBnAX3zkxdlcTtfiCmf6vEhiZwPVSvAAKmMAUNNUIdEVsBHrICRUxu08xhZiEM5A4BXyW7jSK24EsZ08H021XJizqQ7VP5o1WPM%2BUFIiZY9O1UGQ%2BmhmmKoB%2BeqW74ZxcV4X1YTTarP5uobg5CZ9lWH0gY9zOc2sPPbHIGN5ZU2YicTkI3qq0XtPqiIIveNnlCwJWoHAhINaK5nfXK4Pn0rRiYgfyKnFTlwE9%2F6LF43l2%2Bf7uH8tJzfCXkiKM8W33eh1hJG9FQS6eEWnKkARMXdi5TjdhkYRXHg1wwNhoDZqfl9lLKz5wDZ%2FIiPQSv6hZaZ9Ry2oxTHDdAieKYXMSgg0Mg4D9sU%2BVZgKVMojyT%2F39ruoauFnt4vfDETsoQi6gb64ccBytg5RbQpy%2BSfQE6enDdY2MPHcib0GOqUBiBlZaGvrnvNjsDITn2ML5KZA%2B1RJsC8lXvxC4ZLQWlgXL%2Fcs4oR1Q8roZjiiGN3npRLmpVikdOBwvh%2B1xstQyAFh%2FB6dl3mIpSHeetzUrODy2JJbzazOGGbsTvASYhN6CLo41zFGwt3YS0%2FAQtSsFHkN1KLR9ZHpGmVHUEWQ97zCFjoEpjUMAgT2io%2Ffzo1CToTT3b3K%2BZFGt6Xjo0k%2Bc%2Fl0m5aS&X-Amz-Signature=837718d1662155e47d3c9af29c7d5b93050ec5c9b02141f2d6d51927c305b169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNM2RBLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQD1h9fAAPrLF7Yx5NRFMnezkYtSQ5fLyMLzDWhhpuYhOQIgH9RoPE%2BhvuuFa5J6G8u2Rl0xckIxUxDsjJI6pmvxUbUq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDAum5HV8izlb9wHs7yrcAy2IzuB0KoF4KTCD0gfeZsSCC58Zp5i7gkZTHbOfxtZ2O%2FUZPS6b4%2Bp%2BWQs0DyIzYSPNzxU6RENwOV8YkJCubvKI1cTsAxsmZQqJkcG1aRQOQ8mEdULqhct5MdxaWkX3%2FhbgwgYeIEgsHADuz4KRxBKxIt%2BGH0DGNO7LNXHWPPOEsbbf68pC04fLqAdIg6TFNt7gLwpxtS5bB0EnTHeWsBFpyUQjwPoOWbXs3tO4TzEarvshcXT5ErxpYQjConYz%2FJQeVgli2FhatWvvaJkQhJ0%2Ft1I%2FThq7V3rGEGGwV5uX2URUoASZaTCZSWQQjZjPnaCIlrGkY4A%2BXiakLoWxtLOFHhHUHwnh9b%2FQHgoYHqiwCb11J7Lqu3LDH0%2BhXtOkyJeT2Y9sw4U%2F%2FmYjJxzX%2FVyTlxVGg6cVzgH4y1I51VXOfPdVuxcI0s1yunsXs1fhbjhxMwG4IQ5K1TpdqDbjzhU716e5sVvXG%2F0eJu6kGg9pC4KXzGPvCafRZeimv8nzUmoiqf47hTDxn1wq6bqD12p4h52SnZL593lFASOVoNsWd2aHf119p4iFzqUFOasc9M0l1QlG8kDWhK%2FOedz25d4EbSUJQYhAuMhT%2FlNZKQfE6irKMHH4Hl5qyuzNMNbdib0GOqUBvNrC%2BvQmXZbqkgROR9m2ocJZ1woobDUq7O8ocriqwSVTc%2F1IK7LxcrqCX3lhGDR7ATWYPPppkj73l5ctlh6xW%2Bnn2yZbrZw3kW6GQkkS%2Firf5AJ%2B82Jy2EVCJ9IbfPacmw4hye%2FO7sD24qO9VsEOY8zO4CD7W4FVXVke3l6dbcvdDidgK%2FY%2FG%2FuKcWANusM8nrlmSshRa8eKCym6h2e2ypWpESuQ&X-Amz-Signature=75bedf4d5e93feb8efec327f1d3c13cb63175c16c7910d01bea2f95a560f82fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OR2B6GS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGyXCfLNoxA7zcUztiTlm%2FH%2FI2Mkgv5PSaYgnv%2FPPcMZAiAdh8JhdORR7avSSmYM0avfzilVtvbRko4mZHL%2FhlQFUir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMs9baKfr9CNSW9dssKtwDy6KYS7tCj%2BqQqcZOAHVSfZ%2BrYBhpAO7AHI9xX7Rm42NW1eEnWsAWZZSDDdCthBuBKcrZYPHXHCXDM1XgvkGaqC9gK8qqjdN4mA%2F6i7trlpAfoFsDKkSrjneWtC8RfMIHWZUpBlWpStFUkkBlvCILB%2BMQsfbt%2Bl4v96q%2FV2t14QEyP64sjjRTDTa1eYt%2BX9hea6hI7oxgG%2FNtvWaiBK29%2B7clI6UURbAAe%2B36AyIC8JSGWMIP5XnMKd8IymltmVO2txA3ZPbSWgh6Ad0rd6q5U4SHlJCFYCDYOmhWPxb4JVoCWABIsOk2uWOFe2sv2HDr1dc8KkBvWZIDsR8m9EXNP9GZuGN7I8Diy7qKzg8ff%2Bq%2BYiwYw2bxrGrmlR9Th3WTCuUSBVcNmRsoGLz25opNAlXcl2LS3MRCpbQJ6VFuBX4Dlvg0iiWLo7y1V2ZXy0GiQMdMpMkgoJuDDzE7HPlKY01CdP3e%2FVRsuTkKOn8ouEOHXZygGK%2Bgo9uJW4jU22RTGTTclamnrDYXSuspMkOJ5OP2AFoNUXz9d%2F%2BjYKb7batycrJuiIK%2FdICEvMcKZldsTf5%2FGGG2juS1QOWrpRUlq9dLseolf5qbYlQYEduagkwVTbU6vOuyXA5fFI0w8dyJvQY6pgFTfJtYkpvwjgBmh7HlSQwOlWh6YD68I2vQ97Oi9ZZo%2FRlxkU0h5q%2BbEUTbReLl%2F0epul4A%2BhHfbskywhe%2Brng%2BwwRACOW3n3LKTmTkfLsFFTdQpgnKdYFjaGPBiBXmzCPBMMvAEzZP25nKN0NADsFPYqedoMg2l4rh3G6pGNSmHhPGQYqfxqk2M4R7Zj4UrfJiVwQ4qhj86hreqDr74BFo7AuXYKOf&X-Amz-Signature=5982ede7c32509e9c3d9b08cfb63d65f2095d57e8bf0a762d7948b6cdb88d8da&X-Amz-SignedHeaders=host&x-id=GetObject)
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