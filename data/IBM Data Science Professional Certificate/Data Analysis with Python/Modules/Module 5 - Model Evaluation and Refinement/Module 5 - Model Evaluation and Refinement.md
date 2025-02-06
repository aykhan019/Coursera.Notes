

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=a41eac16e66a14eec5cb49bdd14a7ec4277151c576866d6bb6fd436479ae8e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=6dfdb3bb1f6e69a60b4cf4b57372255bda10bffa88b5fe1abb897de37c65a008&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=96a14565d66efd93d2f672810c296e05858df55732506233d75c769b613471dc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=d3989404240044b5d8064e2bc03af1b0e433c877f0c7e95be161cfcb8f68ce68&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=2ce4078afecd4976fa0d0e0709a552db0ca7b1ac544471e04dbc554c30792de2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=6aaa0be910b0ee28e25bc14ce4e7c206d28297b9fdfaaec3f201ca3fa79517d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=b232212e5c94d4b79c8dac5dd60a14a1a7b35d0ef40440e0c8d54906bcd906ad&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=12ea496ca17c593719d21bea8b0b418e13c57a4c966d372d91d33758f7087ada&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=d7f83f2da1ea9766443734cc5a66b467cfa2c918de9c21d47953a6a5bcf8d7aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623QSKN2W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBZrrBJMQTnl2Z%2FrwsFU4haF4tBCiPAhIEbA9zNoIJekAiEArAFvcmjmvZ7xMGq%2FUhvvQafVa8bqHr9UrZi1bEhXXJsq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDF4l9lHPxxnMXPPWiCrcAw2wG69u3b6%2FmmttqO%2B0DBILVouxN8UeGPiYEqZ98RHC7S9JpL5t%2FbvRMxvSvm1tuU0dw8l2S0LfHXSocIJTcGugeGwSyz6vGyosFQdzl5JaPO%2FyQbznHehrhZVTDzbABwVKOds7QvOUiVjG4c5rtMKmrCT51KnkXiJ9VtCZJN0Plm7UTSAAs9PbmNI93vKh0UJ%2Bsms%2Bbte3q2qnc1NLU5PeNXMoMewvKfw8vJtdlmuv1mmljMXJepfLmOb5ZYp6njBsH8P%2BCmHXOwfJS5F%2FS3RBDoQCiAOU1TgWH%2FRsYi3lu0hfM8zf1CK%2FfRDJ1SAR0vE446GGc1Y4O66d40y0V6%2FTfwRfBJHxmJx0bx7VzBJWiMDU34weHTtYVmjAvbCYBTSVC9syrUbRM2ETWZNkd71OI3RZzdI0Af8%2F5XZj2Es%2Fy80WhZWO1u%2F8am2yiPvmyEiTxah7EKaON3F7r%2BO3qV09kuCzOLqe6drxmGuGpz8AISr%2BeZRFEYAb%2FlnoOfHEN8XrBWO6mk9DWV1vbcT5PitkH5xSio8fVnDvrEQMReqrDG%2FBRrWTXn4K%2BKfFvs04VN2lfgsFgCOSL3RvBwckIMaboSN41TE8dbz%2FDsRl3oPjmQFys8PSjrp4XS5UMLrrj70GOqUB59YdUSk%2B1OyBZ3c3J5y5HWHSWBtSAbgas1QU5pZFAluuiiIwDS1qxb%2FrCmidvfM4SMtsQmxbGoSRWDiDRiarN6nffGtWxHvOFbOX3JLWJxPoerNuQSxMIBEN2KAIiMe3Utym5W37GbwAcYvDRHidj%2Fqpjl9xySDJLx4oyi3mmBwiQoLSrqeSzQwVtmAcRjhGsHImDztCMXKf1HlGoTlVSTyai6FQ&X-Amz-Signature=6a51db55836d5dcfa4c4c1500821d7ced1ff09cc1d43a6bcfbd9b212defe77b7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623QSKN2W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBZrrBJMQTnl2Z%2FrwsFU4haF4tBCiPAhIEbA9zNoIJekAiEArAFvcmjmvZ7xMGq%2FUhvvQafVa8bqHr9UrZi1bEhXXJsq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDF4l9lHPxxnMXPPWiCrcAw2wG69u3b6%2FmmttqO%2B0DBILVouxN8UeGPiYEqZ98RHC7S9JpL5t%2FbvRMxvSvm1tuU0dw8l2S0LfHXSocIJTcGugeGwSyz6vGyosFQdzl5JaPO%2FyQbznHehrhZVTDzbABwVKOds7QvOUiVjG4c5rtMKmrCT51KnkXiJ9VtCZJN0Plm7UTSAAs9PbmNI93vKh0UJ%2Bsms%2Bbte3q2qnc1NLU5PeNXMoMewvKfw8vJtdlmuv1mmljMXJepfLmOb5ZYp6njBsH8P%2BCmHXOwfJS5F%2FS3RBDoQCiAOU1TgWH%2FRsYi3lu0hfM8zf1CK%2FfRDJ1SAR0vE446GGc1Y4O66d40y0V6%2FTfwRfBJHxmJx0bx7VzBJWiMDU34weHTtYVmjAvbCYBTSVC9syrUbRM2ETWZNkd71OI3RZzdI0Af8%2F5XZj2Es%2Fy80WhZWO1u%2F8am2yiPvmyEiTxah7EKaON3F7r%2BO3qV09kuCzOLqe6drxmGuGpz8AISr%2BeZRFEYAb%2FlnoOfHEN8XrBWO6mk9DWV1vbcT5PitkH5xSio8fVnDvrEQMReqrDG%2FBRrWTXn4K%2BKfFvs04VN2lfgsFgCOSL3RvBwckIMaboSN41TE8dbz%2FDsRl3oPjmQFys8PSjrp4XS5UMLrrj70GOqUB59YdUSk%2B1OyBZ3c3J5y5HWHSWBtSAbgas1QU5pZFAluuiiIwDS1qxb%2FrCmidvfM4SMtsQmxbGoSRWDiDRiarN6nffGtWxHvOFbOX3JLWJxPoerNuQSxMIBEN2KAIiMe3Utym5W37GbwAcYvDRHidj%2Fqpjl9xySDJLx4oyi3mmBwiQoLSrqeSzQwVtmAcRjhGsHImDztCMXKf1HlGoTlVSTyai6FQ&X-Amz-Signature=4fd0aef16eb6037ba77094f073fe8992390b54984a2d6408c3a713b938a89be0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623QSKN2W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBZrrBJMQTnl2Z%2FrwsFU4haF4tBCiPAhIEbA9zNoIJekAiEArAFvcmjmvZ7xMGq%2FUhvvQafVa8bqHr9UrZi1bEhXXJsq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDF4l9lHPxxnMXPPWiCrcAw2wG69u3b6%2FmmttqO%2B0DBILVouxN8UeGPiYEqZ98RHC7S9JpL5t%2FbvRMxvSvm1tuU0dw8l2S0LfHXSocIJTcGugeGwSyz6vGyosFQdzl5JaPO%2FyQbznHehrhZVTDzbABwVKOds7QvOUiVjG4c5rtMKmrCT51KnkXiJ9VtCZJN0Plm7UTSAAs9PbmNI93vKh0UJ%2Bsms%2Bbte3q2qnc1NLU5PeNXMoMewvKfw8vJtdlmuv1mmljMXJepfLmOb5ZYp6njBsH8P%2BCmHXOwfJS5F%2FS3RBDoQCiAOU1TgWH%2FRsYi3lu0hfM8zf1CK%2FfRDJ1SAR0vE446GGc1Y4O66d40y0V6%2FTfwRfBJHxmJx0bx7VzBJWiMDU34weHTtYVmjAvbCYBTSVC9syrUbRM2ETWZNkd71OI3RZzdI0Af8%2F5XZj2Es%2Fy80WhZWO1u%2F8am2yiPvmyEiTxah7EKaON3F7r%2BO3qV09kuCzOLqe6drxmGuGpz8AISr%2BeZRFEYAb%2FlnoOfHEN8XrBWO6mk9DWV1vbcT5PitkH5xSio8fVnDvrEQMReqrDG%2FBRrWTXn4K%2BKfFvs04VN2lfgsFgCOSL3RvBwckIMaboSN41TE8dbz%2FDsRl3oPjmQFys8PSjrp4XS5UMLrrj70GOqUB59YdUSk%2B1OyBZ3c3J5y5HWHSWBtSAbgas1QU5pZFAluuiiIwDS1qxb%2FrCmidvfM4SMtsQmxbGoSRWDiDRiarN6nffGtWxHvOFbOX3JLWJxPoerNuQSxMIBEN2KAIiMe3Utym5W37GbwAcYvDRHidj%2Fqpjl9xySDJLx4oyi3mmBwiQoLSrqeSzQwVtmAcRjhGsHImDztCMXKf1HlGoTlVSTyai6FQ&X-Amz-Signature=1ada39877d05ac4e9b4477631af0e9d6165e4de12adcd3f05016433c168dc87f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=5d63deadf0244d5fe2df48b02ee54deb9677e785799791405b3223b74f952764&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=3836b3d5003fbb1f2ee659382a7ba61b2a930d783db5073841640f40f1bec334&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=1fe631f5a264f292564615316e5775d52b0a4932398a896e1c50f1d0176d1af7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=0681676bd4c7069743e98c949a2071b5755b671bfc52134ba4ee2d07ce782ef6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=a90a3f4d27f201314e7ff5b5b572e3e1ade62d79ab910d39f5f8cdcaa824dc0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=949930c64ea8fa94b20532e89b62aa86df965bce8145f3849893a216c8b4d682&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S5TQ3JW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDJ09pub6Tl9RahKG09Q4djjc97ZQDPeDkUWw3uLbgdOAIhALoH7XRDiwYnyJI0gT8ojMbW64myDYkXMZ3fRS67DHigKv8DCFEQABoMNjM3NDIzMTgzODA1Igx%2FZalP45euCA7mmmQq3APNi4ngShzBordX9EEHTz8f1oUFxdBhPhpFLIRsQOVi57zWADA0TX0uG%2FtWvw%2Bk0pMGJpAcO%2BBJOvD%2B6MZays9gNdGSDBIRTvdQQ%2BF9sgwbuGGG4Cp77%2BWicNsgqTOll2jRElZ0PL8rzNaiJuY6FfD4MNPsABhlFTjoi8L9JzdU9yxr%2FHTHO5iETkpmiZTLsRqAt2j1bbsQpsf96K5ZKfkAcGyQKcF2uvQNwMWVBc1mVbvSlRPZfiDbDJ2sCxan2jtMsE%2BClHp5iuewY4e3vvfwi7CKuUq4D3LtVwcOsA0poMFmbwb71wclcknQgAi6SD3CspRU4FQErIo3S1jjRJvOrYDpb2j1JOzSqC4IHN5FWpi1xgMETVVh%2B%2Bt3LTClrWGF85t9qjzfCtYAiRe2dX3k3qR8kPi0IO6EcC08TT6TcZ1HMsPj2hmgzbRDkmeC6SBbOrsGKZxjIuyotZRnSJrLXIaiQyobYlUQshLN1h6MhGd4ihzMN5KY0lCh9JcOdTxUjzfmuEBAjS8zTLl0QGYekWmCj4XnK%2FDLwZhlH%2FEh4i2hWg0vnyUmQXDEt3UELlV%2Bm4HFdpcWxfKE53YWYWPri%2FhO1zQcG23Aw5w%2Bq4qtWk5cdcHGIP8PFb4gmjC46o%2B9BjqkAbpZGD1BMsn5yjCOzJF8zfIj8t2QIzPOVyRYAPu85m%2FBgQ%2FWBhW%2B4V3nWY%2BqH%2F%2FEMGzwpKHFLN%2BG7Vp9c%2FExQJy4kRKM9CG3mjcAQf0OiYTzLLGCeUfYfiAmqiFRQFHbWsPGr1DOwpEAwYoGpzubtt7f39meW8GyC7AAQ6WQlSE6HUsZCGMkw%2BlaiZvEbaArBwo1%2BFVI2my4yX4R0ZjJQGrWCGPg&X-Amz-Signature=72a733fbfa0d70732f6a0c86cd9094f99be1fe1b5879802238cdbb681e38adf3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S5TQ3JW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDJ09pub6Tl9RahKG09Q4djjc97ZQDPeDkUWw3uLbgdOAIhALoH7XRDiwYnyJI0gT8ojMbW64myDYkXMZ3fRS67DHigKv8DCFEQABoMNjM3NDIzMTgzODA1Igx%2FZalP45euCA7mmmQq3APNi4ngShzBordX9EEHTz8f1oUFxdBhPhpFLIRsQOVi57zWADA0TX0uG%2FtWvw%2Bk0pMGJpAcO%2BBJOvD%2B6MZays9gNdGSDBIRTvdQQ%2BF9sgwbuGGG4Cp77%2BWicNsgqTOll2jRElZ0PL8rzNaiJuY6FfD4MNPsABhlFTjoi8L9JzdU9yxr%2FHTHO5iETkpmiZTLsRqAt2j1bbsQpsf96K5ZKfkAcGyQKcF2uvQNwMWVBc1mVbvSlRPZfiDbDJ2sCxan2jtMsE%2BClHp5iuewY4e3vvfwi7CKuUq4D3LtVwcOsA0poMFmbwb71wclcknQgAi6SD3CspRU4FQErIo3S1jjRJvOrYDpb2j1JOzSqC4IHN5FWpi1xgMETVVh%2B%2Bt3LTClrWGF85t9qjzfCtYAiRe2dX3k3qR8kPi0IO6EcC08TT6TcZ1HMsPj2hmgzbRDkmeC6SBbOrsGKZxjIuyotZRnSJrLXIaiQyobYlUQshLN1h6MhGd4ihzMN5KY0lCh9JcOdTxUjzfmuEBAjS8zTLl0QGYekWmCj4XnK%2FDLwZhlH%2FEh4i2hWg0vnyUmQXDEt3UELlV%2Bm4HFdpcWxfKE53YWYWPri%2FhO1zQcG23Aw5w%2Bq4qtWk5cdcHGIP8PFb4gmjC46o%2B9BjqkAbpZGD1BMsn5yjCOzJF8zfIj8t2QIzPOVyRYAPu85m%2FBgQ%2FWBhW%2B4V3nWY%2BqH%2F%2FEMGzwpKHFLN%2BG7Vp9c%2FExQJy4kRKM9CG3mjcAQf0OiYTzLLGCeUfYfiAmqiFRQFHbWsPGr1DOwpEAwYoGpzubtt7f39meW8GyC7AAQ6WQlSE6HUsZCGMkw%2BlaiZvEbaArBwo1%2BFVI2my4yX4R0ZjJQGrWCGPg&X-Amz-Signature=92b47d0c974eee93d4d2f7038e25fa091127c364bec16c1a915ef93b51fbbe29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIVVR6KY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIEB10ptqc%2FRIzCPXdNeE%2FseIaU2ESIwNPQ2Kk%2FUCesdTAiBSIezeW5IOQdXw6ltJRSDKSMTxrYR4ypzk1GLOL5WOxSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM3e4oYgSFVkkX2YFFKtwDauYNql3PvyKqDc4TzoEDtmXS%2FGOjwNNqyAylCa%2F3mt5K9HkrH8jOURe3rB7WT2Ko8y1gub07cq7IRfml%2FQJOAdeZd7WtT0AMZ1qWkziRkp1dRN1FKobhG2%2FRUIPjm16RrMe4y060FLbFE0ZAJDHeXOlvdKSjDReQd9HLqRmxg1zLwqUg567Z9SEGWXwFvc0MJ6Z6%2FmT2%2BCRSzndpbGSWYcaTKC6XxoqmI%2B7gi36H%2BmUByTwEfApJCP6B2TKtUP2NyCHPiQrvVwdcwfeLH48xJkTDNP9LUoBPJW4cJ0PQBwWnMBrjfKsAroWhrog205ZLXqlrzCR71M3X8fVg9L%2FNSinrbkleWWa3lVCw3kgEq6GHYJaxU%2BqmayiavxvEIIp3w0d%2BnnEmPm4KPUyxBl92%2BHW1buoUtCwET%2B4If4BSMjXtO5ZaFcEVd5FnHNwr%2FhW%2FsQiinxYUj9pfjuSQXilbZkdr3rqIUY%2B2mHZRUjf4oUNAJNP%2FSAYjng2Sgk4G3KKXyL3s4S3fpZvbvg%2BM32T2oBbyZv5%2BZ0uJT6wucvSdHY4g4yw7zpO16qpDWtBfVXO4VDN9ZjXW9tHT8FAR2QK9sayNa4TSpbz92vqba1r%2BPSlikN34HppoC6fA%2FGQwveqPvQY6pgGghuDUcSz1284vKfs7MOBGAYpB5OzhEHvW974%2BQDQvkqydkKGAeRpsq76WTaT6SrVdzC48GXMb1XHm4H%2FMN9P4oh9ioVCiYHfdVXlNhhjM63ukXHUaqeHo6I1TMd5olm%2FS5RuR5Ms5gllcZD986UvyXE14AWmlrBt%2FbgcdsfH3AfTx%2B2h0OsFe0dlqIPHLcyX0ZA4mQphjrPQBA6RnyUmUjqMbGI7f&X-Amz-Signature=f3b66aab63bf6d8a5ed596660bd8c78a76cc25baa64ad35d7daee463b09c768a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI32E7XX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3oQM4HSS%2F5VD3zmUn7WrKFSH%2FBhZJGo24x%2BzoycEvUwIhAKzikzOySljRz4Tih5rZSxALyCeYoasr5oeq9xkbroAZKv8DCFEQABoMNjM3NDIzMTgzODA1IgxLpZRisNDlKTeGLy8q3APVJ9i%2B%2Busv0Wj1ral9XJUVf2xfKA%2B4GKrBo0zJvIwJXfHY%2Blu3RrUrbMptzUd3GtWLej0O0boWkEsoaZ1YOcbT8RHAGbCVf7rp4kbZWA7OryfjrM3853sSEurccekYN8bdyHmIW7mlHgLcqzJM5rPrniGzzxppYVDidCB5DkZSPME173cYDZi70tFGlCrHlB41pdQOTPtTc0zsw%2FCr1sDClSbfrqm%2FCe%2BhRa8TqWgzI63EFEFo%2BrVHK06Bv%2B2MlrLfRNtuoiyjd0Tve5ASV6obQcTk3l%2FlBdEVhG%2BqYvNm4iRfllYFf8TXuwgxjlW3YEy0LpJpRIp2fliPnitjIO03TguiCQUT4qZiHrrJnnW7CaQcWiUNKAs4%2FbmdL0pFqXQ08MFJ13nNJj%2Fpe5%2Fb8PJ7%2F1AHeWvTZQX3HWCCwTBLVdyUjMwu3oftxJqUN9XggLcAWd7%2FinD6pBgPySMBLSQetiOWv2EzlQFTRqrroMM9QQbuNuddQplISnnGVWwwIqIH%2BMf1gVsCV3f5Gvs%2BzoPfDqPCXngiBf8zF2aFToCXLi8rsQPYbhRDJFlzlF4eseERGO1FNPbo7N%2FFMX%2BLWw8niHY52jtM%2F%2Fb4n41mAWNVLEr76jU7wIa2MzZcMzDd6o%2B9BjqkAbn4qS%2FNzuBxXz5T%2FGyl5Xd4pNRdyK1eIFPBFHtPdGv%2F6GqslUsBin7cBmtcB1fsB1V1H7fE0dqHRR9CfLr%2BkA2doCBllikw7VpdjJpqNv%2BWEblsZlJmAEPgB8xUYWXGQCANI3d1%2BF6qRbbh8VFLQCtykexLPNpIeAnpSTAMChuMHmLamcZmo5Jdb%2BnEjaPFacLeX8HRT3lGN170iAGqA6muHdgp&X-Amz-Signature=fdab0031a1f2f76be54326ad41991679c61879c05c0eca99249e8ae20f580ca9&X-Amz-SignedHeaders=host&x-id=GetObject)
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