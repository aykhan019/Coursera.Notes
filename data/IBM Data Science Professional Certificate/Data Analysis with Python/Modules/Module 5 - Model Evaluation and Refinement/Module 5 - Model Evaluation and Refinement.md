

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=0435bd67c906e27f70631322d3d6cb5d9aeeecbe6307ff22d73880ee8132b5e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=9da3397fd93aa9198211b3b3d716bed8f02fccb5debabf1a3a0a1141b782ca20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=5db55eae5d0a6e36d90087c4996b11776a0bfa94726a667079450332dfc928df&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=d2cc51e3d3672b0276ebc057b8fca9377b192a58e4a53fa5e94a09c2a7914966&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=7a1a786a652b2a6fc5b4ccdc2f93142bde8a97b5dd8252b74bd42b6cb3968760&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=e2b2213dbba2bd934c5a9c1c719c7469fee5435f704978381d2ebfaa199e450a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=83b850c1a916265b16546f7dfed7bf428aaa983f72ce25c0c96b98e5e23b539d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=b24b3f84f1a21932c39b54ec2298dfffe09a17ab708468684be4dc80ce88c239&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=f79047451483cecdc1c27c84ec62d39958e6fd91adcfc9ee34792c95bda98fba&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H7N4YXE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIByLqc1Za6WoTz8JMRZmC83SLq%2FcQR60GDzgillWy7S0AiA0HEqzrZaY0sPysSSIkGC6KWotlCq42L%2BEdoKOSW8aiyr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMpd3i5lF1IA0RqtfPKtwDLnl4F2UFal7ZRSIi9GyrN3GzxUbeR93eHbnxRiPdWiRhJ7F6gTPfTr2by%2BIp1aJ2fpCJTgqrwvjjyoFN5TqZjmcoIYjyHhb4xLa4ASBy8AJQfI9uGaurU80719GBDCQwMuN5vFE65Z%2FRDYAxeZf6jLDnyRX9GT6OEio91K2kMGz8C6q7RPhmkvpqA2NpIcKus4s2jST6nQ%2BmDpLLvWtGcn7mmYzKGcy4wXdliG5VD5%2FKxmNBQ49qlsEdifjHEifd%2BZnLxevWVlsH32p%2Fh2F06J8us2CdP6X6YHdjDpwOEz5uo97Wo4baBbUx8kOG09CSvX2jYoV4S31%2Fqm%2B1RiQIjR%2BqbTfeTzvkTXPYWH2Wzvv%2FbaLi8f%2FLY6Fnpn22%2FUZco8WHDKk7GvxnxJDl5XDlIEgPXcNjHmKtJoKTuGleNo0WOPEHJCWN0gBFHL8zvjibGD%2B6FKasjypIL0BD96sTPEzU%2BpsTJUBfZS2OAZf7%2F2eGuMzWVQa77t3LlG5Y8hC0y%2F8UZyxRXeDtZosnkwukFjYmO5icTpunFESRdIQPohj6FZ1dlSsy0XqwayGHQ%2FDCaNj291GnglJzr%2Fz%2BFkt0079%2FbssvTMlXCPyCa%2B07T%2BHvbmwqO8gteJb9JBcw%2BfiSvQY6pgHAZrUm%2BO8j2E2FWju0o6nhtHKbDKoqy1qXq51Zh%2Fd%2BTuWojqRXuF0Uq2oOJFuWINYnbUhkuAW4YLjyEP%2Fn4Yoh7gSqq1iZAiXMoQfAfWdbzNu3424gRIkBHgdcR%2BNSKEYnV8gCf2xCUviek3G%2BtI9JMofTViJ8ZdLQ%2Bss5STUm44fBrFgXhBRyLNNWB7f5yN%2FTESOYTyXSuD5USbi0%2BkUGtRQpSOR1&X-Amz-Signature=227fdd594b3a58f559b3d01190243e0f08ee73030938e501aaa0ded28bcae08e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H7N4YXE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIByLqc1Za6WoTz8JMRZmC83SLq%2FcQR60GDzgillWy7S0AiA0HEqzrZaY0sPysSSIkGC6KWotlCq42L%2BEdoKOSW8aiyr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMpd3i5lF1IA0RqtfPKtwDLnl4F2UFal7ZRSIi9GyrN3GzxUbeR93eHbnxRiPdWiRhJ7F6gTPfTr2by%2BIp1aJ2fpCJTgqrwvjjyoFN5TqZjmcoIYjyHhb4xLa4ASBy8AJQfI9uGaurU80719GBDCQwMuN5vFE65Z%2FRDYAxeZf6jLDnyRX9GT6OEio91K2kMGz8C6q7RPhmkvpqA2NpIcKus4s2jST6nQ%2BmDpLLvWtGcn7mmYzKGcy4wXdliG5VD5%2FKxmNBQ49qlsEdifjHEifd%2BZnLxevWVlsH32p%2Fh2F06J8us2CdP6X6YHdjDpwOEz5uo97Wo4baBbUx8kOG09CSvX2jYoV4S31%2Fqm%2B1RiQIjR%2BqbTfeTzvkTXPYWH2Wzvv%2FbaLi8f%2FLY6Fnpn22%2FUZco8WHDKk7GvxnxJDl5XDlIEgPXcNjHmKtJoKTuGleNo0WOPEHJCWN0gBFHL8zvjibGD%2B6FKasjypIL0BD96sTPEzU%2BpsTJUBfZS2OAZf7%2F2eGuMzWVQa77t3LlG5Y8hC0y%2F8UZyxRXeDtZosnkwukFjYmO5icTpunFESRdIQPohj6FZ1dlSsy0XqwayGHQ%2FDCaNj291GnglJzr%2Fz%2BFkt0079%2FbssvTMlXCPyCa%2B07T%2BHvbmwqO8gteJb9JBcw%2BfiSvQY6pgHAZrUm%2BO8j2E2FWju0o6nhtHKbDKoqy1qXq51Zh%2Fd%2BTuWojqRXuF0Uq2oOJFuWINYnbUhkuAW4YLjyEP%2Fn4Yoh7gSqq1iZAiXMoQfAfWdbzNu3424gRIkBHgdcR%2BNSKEYnV8gCf2xCUviek3G%2BtI9JMofTViJ8ZdLQ%2Bss5STUm44fBrFgXhBRyLNNWB7f5yN%2FTESOYTyXSuD5USbi0%2BkUGtRQpSOR1&X-Amz-Signature=f908e0ea514e09879c54cc67961a8afcae1dd0bf544e623fe00f8c4628879c75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H7N4YXE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIByLqc1Za6WoTz8JMRZmC83SLq%2FcQR60GDzgillWy7S0AiA0HEqzrZaY0sPysSSIkGC6KWotlCq42L%2BEdoKOSW8aiyr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMpd3i5lF1IA0RqtfPKtwDLnl4F2UFal7ZRSIi9GyrN3GzxUbeR93eHbnxRiPdWiRhJ7F6gTPfTr2by%2BIp1aJ2fpCJTgqrwvjjyoFN5TqZjmcoIYjyHhb4xLa4ASBy8AJQfI9uGaurU80719GBDCQwMuN5vFE65Z%2FRDYAxeZf6jLDnyRX9GT6OEio91K2kMGz8C6q7RPhmkvpqA2NpIcKus4s2jST6nQ%2BmDpLLvWtGcn7mmYzKGcy4wXdliG5VD5%2FKxmNBQ49qlsEdifjHEifd%2BZnLxevWVlsH32p%2Fh2F06J8us2CdP6X6YHdjDpwOEz5uo97Wo4baBbUx8kOG09CSvX2jYoV4S31%2Fqm%2B1RiQIjR%2BqbTfeTzvkTXPYWH2Wzvv%2FbaLi8f%2FLY6Fnpn22%2FUZco8WHDKk7GvxnxJDl5XDlIEgPXcNjHmKtJoKTuGleNo0WOPEHJCWN0gBFHL8zvjibGD%2B6FKasjypIL0BD96sTPEzU%2BpsTJUBfZS2OAZf7%2F2eGuMzWVQa77t3LlG5Y8hC0y%2F8UZyxRXeDtZosnkwukFjYmO5icTpunFESRdIQPohj6FZ1dlSsy0XqwayGHQ%2FDCaNj291GnglJzr%2Fz%2BFkt0079%2FbssvTMlXCPyCa%2B07T%2BHvbmwqO8gteJb9JBcw%2BfiSvQY6pgHAZrUm%2BO8j2E2FWju0o6nhtHKbDKoqy1qXq51Zh%2Fd%2BTuWojqRXuF0Uq2oOJFuWINYnbUhkuAW4YLjyEP%2Fn4Yoh7gSqq1iZAiXMoQfAfWdbzNu3424gRIkBHgdcR%2BNSKEYnV8gCf2xCUviek3G%2BtI9JMofTViJ8ZdLQ%2Bss5STUm44fBrFgXhBRyLNNWB7f5yN%2FTESOYTyXSuD5USbi0%2BkUGtRQpSOR1&X-Amz-Signature=7b596fab0e74cf7465c12421724b5f76dac87734537f0b328748e77c9e0dbe02&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=561644bd9446758f29799210b2e960dba95b9b16ab25a2c709c52d7205c61c74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=3641cbf491e8879b3db10dc064c1508bbef8dff21088483a94828b1de1cf4317&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=51e899168063d16599492aac578b6e33996d5c4af607304c8c25cececba31279&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=6b536ce7bf9642e7956c9b549ef980474954f8c00cf4587a28f7db13d69c385c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=83cd00c10d04a094ccba6d1050ba6d9f9063815c37f5f4ae54b1548675f67b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ5I3FJG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBUbIXdUtL23au77jzqt7W2Xgd5cRC7eDnqd8vLcuFrMAiEAxxRNyJomkK21YQEsckt6WFq9QFtvL0ibYucvyp86hv8q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDHRQELnSOGgaNj1r%2BircA5cJsrogHTh0Gnzyu5XOj4R83hzq%2BzMnOA%2FLMNnaW%2Fcd9cYq%2BVCgtADRKQE3ZmXQZR0Atsd4oXTGrKeIQEt%2FUf7wKZUwup%2Bv%2FN%2BwxTT6kqeSNz58p4%2FsDQzrmM6HNHP7U5D3PO8r0zwWGhPh3C5bGXquCZfzOaHsMFw3FvAOzzSjeRQI5UYMFRo51YWxX%2F%2FF22n5o1lI9Roa9N0APL4yVYg%2FfLVdDwYr%2FWsHDYRsY%2FiMIvo8Ncuc0jtlQJVlELjiPy2EKpcXTgbC8e%2B1e6IKl7dF7WQhr61R5swG5Ooga4BhsLmdPgA49LeUHuC9H4DNgoNDDPW1HD468oyfcrmXKda%2BmguMM%2FTVKYKWXAh3W4Ubz0gpLljn4f69h%2FT8TSAFM7pxcFe51CUwj6FjEE9VitKvhojOblzi6m4gCCXFaCXP51VWLR2ZgEpPTdlTk6OdlGnuni%2B9Zc4%2BgRFyiMbKJL55CjfiAOWai53NxqRlO2bhXAxN4%2BnqstlPH4EbY91HBQc2Nj4OSbRtSHW0Dl00tEk5Jo%2BwDR3uvx9aZ6o%2BjsQ2AANph9JcRiQF2pyhS7UN1ZeIqS4aZ2YykHhsabq4MRlvWQp546IuQoINbKjELxLIcWDthS0gdsHhM5DsMIP5kr0GOqUBTZsNwr0wiPBtwW7Dd3TaLiAyuOGzjMdIC2mC%2FjhxDt9js22yMkhN6I16G6S10w7TSKTeZJz6VVSAArvtqz7oI5BsL%2BxOokegVhx3wC45VKOsSamOdEHaSWKD5BkXBLwYBz4ynLkJhCVSU1C02TPpz2Pasvb5hWTptHiv9yvkhu%2BCf8ZYEdR4kTwyImlZpwcIOX%2BRnHLqK3rpDhk0jOwH%2F3x%2BVuHP&X-Amz-Signature=e574123fe1bbb58115295e9d61b0e3c828a3f9245f770f750830b335f0d745f9&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX227R2Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDYpNMBomFlUj%2FnSKs78lhHHnXToSgBZFFovok7Ruhd4QIgIptq%2Fwp4yuldh%2FmiJ1pM%2F6ZSYkW%2BZh%2BFFLH8Nr2pO8sq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDPfYiVmbjiKHowPY2SrcA1SiU1cO8IyyhlSM1kxaio2qklY%2Bo5OGgvCJpZV%2FMbKfaQ6OJ5VDC%2Fud4q2fHZok8UE8GlsJ80FRXbKAQlCQzlX1EvLHXXGZU3iemnGn1%2FpxpOPvHS8y40u8TQOwSeExMoNuGqlhzKBC8uM39xhC530dSORVsOG0XpAUXU0uvmT%2BflPlxRLU6NubM1Aa%2BZ5yxpNjIIxRaG%2BWVKwesrhLL1ePZbItN2iI%2B5UOxU1JCpb3gT59JqJKfKwlnnmsDg%2FsXJAffVLgLSheKGHd90MB%2F%2BGuj1O7GIvHOCwnoObkwyyFBr9UINzcL7OkiwfnF%2FSD5fRZWnYKQzQ6cB1j%2F8a0Q%2B3OVQV7l4OoaYPldkARJdF78CznihZulUy9RNBHEHHtHDolKAEc0NUAmN%2Fk16yT3jEknSFRZRbgCew%2BE8hk33tkbFiGT41YFkTuNsvsRX09ZlUDlCc5sGIFZTtVDRZS4o9ONj0JLC5IFxDuM3t9PIMx%2BS1gCwgXdwB5PeDP9kFnU6r2tNniSQMTQQvpufyUFGHrSK5m6pVBBXT%2BhM6vvVJ28A6Gb8k94hWvWDkNqax1QRkdazIpQL912aWC%2BS%2FE2FSAM%2BZjqQHTb01%2BIeOuFXoVDVOP8Iz0gM3C6nsFMKX5kr0GOqUBgjZRkcEe5Ei86PLbbNdU7gVZilWkw%2FMUnB70Y15LybCGG6FRobc7VIop8R9BRk8jVafL5s9SHZwkV0ssrkQCG8oQZWLOTXaKQ%2FcMTm89iEorndRYZvVe3ywDILfpimQ8QFXitX6zL4BOaQzbVgsnwssj37puyejxFieP0mtw8iMzVLmqmgJyt44FPCLHMf8l41LtjnM9c5YOkjnglO9npZPZpg79&X-Amz-Signature=44a4c1352ca970e0d0932d96b19c24ba51933572650b85e75cc65ac9b8001e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX227R2Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDYpNMBomFlUj%2FnSKs78lhHHnXToSgBZFFovok7Ruhd4QIgIptq%2Fwp4yuldh%2FmiJ1pM%2F6ZSYkW%2BZh%2BFFLH8Nr2pO8sq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDPfYiVmbjiKHowPY2SrcA1SiU1cO8IyyhlSM1kxaio2qklY%2Bo5OGgvCJpZV%2FMbKfaQ6OJ5VDC%2Fud4q2fHZok8UE8GlsJ80FRXbKAQlCQzlX1EvLHXXGZU3iemnGn1%2FpxpOPvHS8y40u8TQOwSeExMoNuGqlhzKBC8uM39xhC530dSORVsOG0XpAUXU0uvmT%2BflPlxRLU6NubM1Aa%2BZ5yxpNjIIxRaG%2BWVKwesrhLL1ePZbItN2iI%2B5UOxU1JCpb3gT59JqJKfKwlnnmsDg%2FsXJAffVLgLSheKGHd90MB%2F%2BGuj1O7GIvHOCwnoObkwyyFBr9UINzcL7OkiwfnF%2FSD5fRZWnYKQzQ6cB1j%2F8a0Q%2B3OVQV7l4OoaYPldkARJdF78CznihZulUy9RNBHEHHtHDolKAEc0NUAmN%2Fk16yT3jEknSFRZRbgCew%2BE8hk33tkbFiGT41YFkTuNsvsRX09ZlUDlCc5sGIFZTtVDRZS4o9ONj0JLC5IFxDuM3t9PIMx%2BS1gCwgXdwB5PeDP9kFnU6r2tNniSQMTQQvpufyUFGHrSK5m6pVBBXT%2BhM6vvVJ28A6Gb8k94hWvWDkNqax1QRkdazIpQL912aWC%2BS%2FE2FSAM%2BZjqQHTb01%2BIeOuFXoVDVOP8Iz0gM3C6nsFMKX5kr0GOqUBgjZRkcEe5Ei86PLbbNdU7gVZilWkw%2FMUnB70Y15LybCGG6FRobc7VIop8R9BRk8jVafL5s9SHZwkV0ssrkQCG8oQZWLOTXaKQ%2FcMTm89iEorndRYZvVe3ywDILfpimQ8QFXitX6zL4BOaQzbVgsnwssj37puyejxFieP0mtw8iMzVLmqmgJyt44FPCLHMf8l41LtjnM9c5YOkjnglO9npZPZpg79&X-Amz-Signature=4a7cab61a53fcef064b15750b7dd4d4cba2c5a9f5b0ec654e636a8f82f7763a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAZWRDBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDyuHK7%2FFPUWuGYeU4%2F5B0VfSLAkaiba3zpMBVVJ%2B66NQIgH%2BX2pIK%2FQmlRJvbR5wuxXmnU89RfzY6164KUPfrrSOcq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDFvUMXCeUFqnP4By%2FircA8gBbJ9uLUd4W63hP7ZHe4tlrv7CItwXyKbz9jAVKQcmdckJ983e2WPKQePeyRn8T8RUQO%2FcIXsy%2BzmvKg2nefbbU9UeyJ5PdJdzlTMt44dZFWEISCPj%2FCGthtuie8UUspzDfeaVR9malVt0gOhkBUZB8Ad8UtmLKInmaNjmEkAsIQz1CHbDw9yZofB%2B6aR%2FZaAJwsFAtNkL8dJCXwlBrZXBXg6%2FfF7Zkuu4VdotWwT%2B9%2B6pYemfLZo6rfe66hEZR7%2Fc1WJdVfvx6bUDAOcrz689iACxKqu%2FyXJlatXKGO58kiwz%2B4UdFkzb31%2Byvx5kxSWDkJAvzbjdo%2BM5iqgfL3jXPU0tV0WJVzMs05TcFYieLAaGO%2FdaYURnhhH5O19wlWoomxUDYD2HhDx%2BCu9U5pUHROkx4iddzSyvLlYvCKbqvgPaXpOARGy8YsOQmJFynKn0rtOATosDvQE3TJ6T%2BMgstxJH7rBHepent1VUVoBXB2dTWkYEV0V8N1MTEk1OnAECVNdn9R9DXuUTVnnQ3rlh%2BVzRNC5NX8uTJkd9H%2BVzPlmPHE1wmN7lMVzCaGo99e62b%2BsLknHKs9RO033859S8OTypkXz2bYqdWRokx09eHJAyLfA8YwQqrTjnMIP5kr0GOqUBsT544CjE62CFEmxvRdGvMMcfOb4GMdWx17H3e2Hi5cHaiJip7fd8ozwUQKqJmTrscS7u9chm7wtd2bWZdgXJezg3OZ9eKbi5OriuJX9LIGDGKTgqgWjLaBApbXcjDMFLuFcpVySRIy86lQxk%2BSnlzybHp9ypHoMIRQ0kCFJLDpBf6vxrmixhMR5gv1%2Bg%2FIVwXkIeHuuOhM62m72AeB0nDiDyKBO8&X-Amz-Signature=bc0ac6c302caf905a3c23a42dd15507aae9f8c1db4673860e166c6974596eae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QAJCN4U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD7q0dnxmnOosbydcUGO0FiHLPUYOKqChaBr6Hy6DqGagIhANQhu1TcCwxexIGtF95ixVFKxks4LYNvDs81aT20oLGYKv8DCF8QABoMNjM3NDIzMTgzODA1IgxRCNmUwiNnFji%2FrjUq3ANvQJsgFX4zQlWNM5UfCGBy4vCHavCjE6OYONx8GOuktDEh3xJZUU5sRrxMM4Dtm5eNtd8%2BlpuYGj2jkEKQnAeE9V5E50O9kr2oZ5Yh5cNNhzcZt5tNpf73Q8brY7EnbbyvIQ1ZO4HiH%2BqNxp2%2BTU8CfIH9o%2Ba6OXK%2FtUT6lUCCJBgaL2%2BKtuoQbUNSbpuhBdFdsH%2BIvBd3R0vuSi27rR1rQmtNbJQ3Qil%2Fv4%2FeaHpRqOxAoy%2BJilltf9Jq5D1Krkv4EVDjBcBotahq0xCgElcBhvRWJ2g2pD2YsNTDGkT20B2aYCm1W67LxXfTrO5Be%2BnEDfiNE24mi%2F%2B44g4SCY0ixmZFEKkjuGXAu4x5sSbelvJkbLclvvN3QJQ3ErCCzkXvRIta6DpLt2RcA2HHyQ%2BAUo%2FY6Qk7Sl09%2FJ88petl2IcWVqrHvnhhjZYJF9h6g%2FRZx92r0XmwAKcpu2xJRJDd25HCJLaCH%2Bl3BNr1D6VYkQMT5P26QPE65VRBCljS6KqsTw59Fnitd949BdIKr28lA7aT7u6eawByg0mi3o0QAfKi6%2FIcmO4D1urwPA31R3nyQKVyJu0BLbi4vTFJtqU7ZC0xYQiW3KsR0jdeXEgXGUIG4f6YDdAEr0FQ0TCn%2BZK9BjqkAetl4U3c4tzyxx62gXTcusdCArM3w%2FDu9BuCjUhNdUTvGtUR35D1DJPHZAjISzY7UAtn8IgrI0CrNG%2FHm2WGENmqhrdN3s9s29fCToN05LvAelPVprwFgjB5sqhni81AOP3WuQDIeFylBtlhhi1z62elzXpcRx%2BdZPZgY9MP9Qu6%2BC99SUYxH0vNjfK8bY8lqoKy7HihYbZZzk5UUe%2BU1ABJlF04&X-Amz-Signature=10c2d97ed5bdad8375e65027f70cb0e761cacdf343b6d3fc3dff09178cc64b85&X-Amz-SignedHeaders=host&x-id=GetObject)
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