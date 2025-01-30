

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=03b03d5f8fae987af6ae7a38ee780fe0c8b43990d56f2edfb1d8536be5eb5d33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=9a5c4240ca9c2f8d7458271365a120ccaf4c3af07c3b72bc98bea251c888bd44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=9f8a80be4664b809471b22e7624a3e635f5f79c5ac76c639802b7df29f96548b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=96a1c8ccef073c8240a96f4a41985947d860d4d38961dc4b44e070068789c7e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=2de0f713ce0fdaef18e178fe7029cb26adc1b31c744122c8ed88c9f74d6d2de6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=04405fe84c04c9f21720fde9d318b411a7eaae3defd0a2e1c2f410ac45909062&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=1c0938e3b53f204fd436300f74a9a5fe089649d2b50a98e5503e1802ceaf6ff3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=8fe4a30955bb602d70379a6832e1d43d1a45bcfe03eb274bb761d2ac2a3ef1fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=1f8cba18e34291a862e41ddd39042400cbb90fd3a235b8debd60cd53c7e01360&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD72DDVW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1Tj48tXl67LtmZIRnuVbjRRKNwjcFMqEJBRTZrMdm5QIgE%2FNKeQoRhSO5fH2lXHi%2Fk964t4pY1ujopH77TXAaEwIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEsPhdiSIbw7bfbbyrcA%2BM%2BCA8e2tYzhXqzbCoKb1D8l50wr6BtD%2BRC16Hp%2FEV7aQPFMnZteRgLp2Du%2FtP5rpOOi3jinCTqbaqIJFul4G%2BME14%2BmSfemTnIiCxo8va2XGKDaIuTjniWeBb%2FmJWHj12ioLNW7kdKTBN6snAFhofPhm80tHvySzwgVOS9o1buimfHngKFPMI7dCSWBbwU4WTqKHWhe9ebCjgkL5b0dPgk35iCUdQID5GqVmeRhWQ7XQdtZKcMQdtUB%2F%2B2BrV6QYdKVbhaPZMVVP5yrTSu36jbwGDjKG%2B6cld16ZObCe8wJdxroqK9CwrF8uJo1rbGMHgAlgLPSjHhaGLVa%2Fr%2FPMtd41kqxYwONuYfpjhdwlcDVsg0S%2F%2FR9OePz3wvgbsiVzhTLD5SftC21eZZSiWuDS4qXlpxF7wP46f2rcVJ%2F%2FvMxjLOoysIxyquu5zFAt8X2Q5fOc4G%2B7KhDkJRUyvZU%2BGJFjEZfYD4%2FYBLc1Eq%2FupynS7U0IJe9JhQRO%2Bh06EuzRx9SIpAKGmfHEAr524VlxaclK5YpFqIruUWLN35vknO3rsONxkTidj6Cwr7zMc5%2FYTQAQde3s9azU6psYhT6%2B4%2Bv1X9iUN5EgCCQ5Z7b4lClYtaAOZqL0ZuArx5MJn77bwGOqUBaJv1%2F6slSTZ0LObY15dmgt2ZzoSGwOvVBQzTD0uc%2F7AX5JOLc2bV71zSBHM5I%2BkC5OUBA9%2FawcF8J%2B8eYp9aD%2FY3tZANvncFI1gJJd8oaHYZFO6wVxjwJ3XNQ%2BLjO9ZL4VD3PPaP%2B0DcNACuPxfpl%2BFIVFs9HZaszEcROl4xdPL6qEPDpz2RXsnZoXL7E18jUY3%2FLwIYFolBs867wteg%2BDMb9J%2BG&X-Amz-Signature=d99835e25a691d69cfaaee23da798563df6c7b2932d18698bd7d6ea5eae2609b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD72DDVW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1Tj48tXl67LtmZIRnuVbjRRKNwjcFMqEJBRTZrMdm5QIgE%2FNKeQoRhSO5fH2lXHi%2Fk964t4pY1ujopH77TXAaEwIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEsPhdiSIbw7bfbbyrcA%2BM%2BCA8e2tYzhXqzbCoKb1D8l50wr6BtD%2BRC16Hp%2FEV7aQPFMnZteRgLp2Du%2FtP5rpOOi3jinCTqbaqIJFul4G%2BME14%2BmSfemTnIiCxo8va2XGKDaIuTjniWeBb%2FmJWHj12ioLNW7kdKTBN6snAFhofPhm80tHvySzwgVOS9o1buimfHngKFPMI7dCSWBbwU4WTqKHWhe9ebCjgkL5b0dPgk35iCUdQID5GqVmeRhWQ7XQdtZKcMQdtUB%2F%2B2BrV6QYdKVbhaPZMVVP5yrTSu36jbwGDjKG%2B6cld16ZObCe8wJdxroqK9CwrF8uJo1rbGMHgAlgLPSjHhaGLVa%2Fr%2FPMtd41kqxYwONuYfpjhdwlcDVsg0S%2F%2FR9OePz3wvgbsiVzhTLD5SftC21eZZSiWuDS4qXlpxF7wP46f2rcVJ%2F%2FvMxjLOoysIxyquu5zFAt8X2Q5fOc4G%2B7KhDkJRUyvZU%2BGJFjEZfYD4%2FYBLc1Eq%2FupynS7U0IJe9JhQRO%2Bh06EuzRx9SIpAKGmfHEAr524VlxaclK5YpFqIruUWLN35vknO3rsONxkTidj6Cwr7zMc5%2FYTQAQde3s9azU6psYhT6%2B4%2Bv1X9iUN5EgCCQ5Z7b4lClYtaAOZqL0ZuArx5MJn77bwGOqUBaJv1%2F6slSTZ0LObY15dmgt2ZzoSGwOvVBQzTD0uc%2F7AX5JOLc2bV71zSBHM5I%2BkC5OUBA9%2FawcF8J%2B8eYp9aD%2FY3tZANvncFI1gJJd8oaHYZFO6wVxjwJ3XNQ%2BLjO9ZL4VD3PPaP%2B0DcNACuPxfpl%2BFIVFs9HZaszEcROl4xdPL6qEPDpz2RXsnZoXL7E18jUY3%2FLwIYFolBs867wteg%2BDMb9J%2BG&X-Amz-Signature=89774ac4c926dc46cc466f2d4b5dafff2a7dcfce6b592963abc3264904507656&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD72DDVW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1Tj48tXl67LtmZIRnuVbjRRKNwjcFMqEJBRTZrMdm5QIgE%2FNKeQoRhSO5fH2lXHi%2Fk964t4pY1ujopH77TXAaEwIqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEsPhdiSIbw7bfbbyrcA%2BM%2BCA8e2tYzhXqzbCoKb1D8l50wr6BtD%2BRC16Hp%2FEV7aQPFMnZteRgLp2Du%2FtP5rpOOi3jinCTqbaqIJFul4G%2BME14%2BmSfemTnIiCxo8va2XGKDaIuTjniWeBb%2FmJWHj12ioLNW7kdKTBN6snAFhofPhm80tHvySzwgVOS9o1buimfHngKFPMI7dCSWBbwU4WTqKHWhe9ebCjgkL5b0dPgk35iCUdQID5GqVmeRhWQ7XQdtZKcMQdtUB%2F%2B2BrV6QYdKVbhaPZMVVP5yrTSu36jbwGDjKG%2B6cld16ZObCe8wJdxroqK9CwrF8uJo1rbGMHgAlgLPSjHhaGLVa%2Fr%2FPMtd41kqxYwONuYfpjhdwlcDVsg0S%2F%2FR9OePz3wvgbsiVzhTLD5SftC21eZZSiWuDS4qXlpxF7wP46f2rcVJ%2F%2FvMxjLOoysIxyquu5zFAt8X2Q5fOc4G%2B7KhDkJRUyvZU%2BGJFjEZfYD4%2FYBLc1Eq%2FupynS7U0IJe9JhQRO%2Bh06EuzRx9SIpAKGmfHEAr524VlxaclK5YpFqIruUWLN35vknO3rsONxkTidj6Cwr7zMc5%2FYTQAQde3s9azU6psYhT6%2B4%2Bv1X9iUN5EgCCQ5Z7b4lClYtaAOZqL0ZuArx5MJn77bwGOqUBaJv1%2F6slSTZ0LObY15dmgt2ZzoSGwOvVBQzTD0uc%2F7AX5JOLc2bV71zSBHM5I%2BkC5OUBA9%2FawcF8J%2B8eYp9aD%2FY3tZANvncFI1gJJd8oaHYZFO6wVxjwJ3XNQ%2BLjO9ZL4VD3PPaP%2B0DcNACuPxfpl%2BFIVFs9HZaszEcROl4xdPL6qEPDpz2RXsnZoXL7E18jUY3%2FLwIYFolBs867wteg%2BDMb9J%2BG&X-Amz-Signature=a205ceb6d616b858b5d54b2caa50720959a29ebd450cd258fde441054dd84c96&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=410f851d1105a26d2b104728806631ed5189cfd647bd949607cd522d48edc3f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=516960240eb46123fb850e54ba2ac33b844ee1cfe18eba77e2cf340c0f44a0ee&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=eee530db99a9c4cdab5f297a3fa81d9ad9a817b73df30df8fc12b97e82cb4c09&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=ab432ad05013468176791739cdabf5fae4628b6515ebb9dd770835e13ba233b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=be23592185b582edeb55081acef0d679864860f8288aa0dd261dd7be236691b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632TFKGHD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFTu%2F%2B7MDypQnEfVyajwEnjgtv28th%2Fl7FAKl0cpm2G%2FAiEAosr6sOeM6CzqtLJffl%2F5mEwSdN0l7DtsBmJxBhI8NoEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBidfbu2khdMpye0%2BircA%2BzemtlJ4%2BoqA6BpxGTBtnuaenaX%2FdjdMi%2B6xAIY6bJYfI%2F7YeT6muNCZTw%2BaO3teuEVL9ue1FEra%2Fuk5WLkcgMdwr4iekwJiDsJXZ57mdg6OG0dI6%2FMTXrmkVfUks%2BaV5J%2B5aDPbhBdMXQ96jmXang%2Fl7Pk5zJS0Ky9qpKE8D9QdQ8hpWKypY27PbBsMLoDXNL04R6HQurtxwSN840O%2BdqIqBOHEKF6PjiPvlhNWSv9qKIV4%2BV%2FdJHFiluyoaE967KDUB5GJPVo8epeC8vmiHU3ti%2Bk9Nn0BZTOHvKaTNcjBvqeK8D3RlXHGxLagyFzl8no9yHIQGH53Lei%2BARC2b%2FFsOFFcH233KlTMUIGbtNy72XfkbEYei%2FiGePJrKeAqJbB%2BAjxKkq6lA4bbB5tbuoCq5UyoCPENqcIw03V26v5HkxF5%2FEN9ARyojVOpXFfGRu4aFRoWUIekSVvLRTOUpAao4CiDCvrntHRgWM6N1c6roVscyw%2BZeAG6iY7kROjTN2IIMeDbVKDMzp%2BVXZ7AEz6CzEX%2BBVpYeBgEz97epaxxbso9Ec8qUL0Mp9WcymYvkBkn4YXqJaA57VBes4879e%2FwcabIWJVVcFI360172KUcEDts%2FW4xVPAw26qMIz77bwGOqUBuD6FxpfOLtnaZ91gP5ItB8fQXl5h9I3ffjs7luYyNK7P%2BkQ4a6Yb4lHUynqDXBLX4JghMap%2BxyWtDnDV13FGcqd%2BEF42yLGv2216AMg7TxytmJoFu3xqdguVqiFeXqC%2BfCdqH4VSU4AKSh4pPNQceaUQdxa8x1UQkvk1UwyeW%2FXxQ2zIZOwPPEol18hbXsrXZzoNXEq9boI4wOabol7NyMX%2FBOCY&X-Amz-Signature=6b9763328b1b0ecb1432ddb74a19d88fa108acf82de9ba314dcc1a97cad80513&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LNBGHOO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF2LkXOY3oj8MEjzsC2UseS3HNS1tXLW9IwrFFhITEUrAiB9%2Fe4hJKfz2nDSBSyXyhZ%2F8Om2t%2BNgVI6ZY0CzJPYsZSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi0spuH7ZeJStjka3KtwDaMSiAzPvpP7T8MbrS%2B8g6od%2FrHl5i5SZFvtX9%2BJSQud2olIqVSa5cpAVfRFtE64R6nLGZoLXaUwmf3FBlLF4bXBLHd%2F1CQJwbg11gkp8gH3oxx%2BmstUV3VYqSJlcJ5JkKhkBjttshJT9Bta%2BXPrQvi9MFgD86d30hIbipl80mkscKoWA0mMfdjFQpD%2BH9QrlJmKpfJhoQlPPaB1Pwu8fM3iZWL%2BGBgIWXAMTwtECADk1y9JA7pih3cPp%2BUcz4mF5igSsdcCu5VAofgDQTXbTRtuO3bivAR9%2B86JLLz110btgNNBWIYWBIvojigaIsK%2B%2BMHq8ZVHEmJjAasjkDDgvXlx%2Bes%2B%2B8t8rCtcGRBjD%2BPVCQhfW73RvWVqC8T5bWX2iRY0NCP%2F4NzxYfiL6ZEjnuU3YF3PSnLNcdhpbl64iinmYKMTABwaB6pgYvg4WlQgNDJ0HGDBSa6M2yuAk%2Bno%2Fz%2FDHZUfHz7x4rW%2FCn9MPSJc8eUiu8hIRwoPxqR8Ao%2FTKweRWVjppk985W71K8BnhK8gl0t50mbaGw5vR5Rnjijc4Ay64GtnEaqk9JO43VXPtxqhyYuG6aKercZGuLdpRWwKVx%2FpHU6PCQjnkUyHXqxDv1VTV3bwtEK8X5skwv%2FrtvAY6pgGM4aubtDDsgSPdDEKgX5yNA%2B1MkmqFzwPBQQx7pg%2BSmkBdjPv1po0nAFKCZ4eQo6dQ4FOpqVl7EtA4HeB3LpW7I4CEDxpMRDe5MRxYdjKSBjCIDvu9Dvk4RReMPr7WLmhQz2OZgK4ZyrCIZVxF702vXqdnSQkPnBqEnkZ9gNJKTXKSVZQYiBrsTQbs%2Fmoqi7EDrrTxIJ8mLVAdhr1ykcmBCJ2r9CVO&X-Amz-Signature=3ef673c8f8d03c5115e647b27364ba2d87a96a82517b5a50f6b9b67180cde794&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LNBGHOO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF2LkXOY3oj8MEjzsC2UseS3HNS1tXLW9IwrFFhITEUrAiB9%2Fe4hJKfz2nDSBSyXyhZ%2F8Om2t%2BNgVI6ZY0CzJPYsZSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi0spuH7ZeJStjka3KtwDaMSiAzPvpP7T8MbrS%2B8g6od%2FrHl5i5SZFvtX9%2BJSQud2olIqVSa5cpAVfRFtE64R6nLGZoLXaUwmf3FBlLF4bXBLHd%2F1CQJwbg11gkp8gH3oxx%2BmstUV3VYqSJlcJ5JkKhkBjttshJT9Bta%2BXPrQvi9MFgD86d30hIbipl80mkscKoWA0mMfdjFQpD%2BH9QrlJmKpfJhoQlPPaB1Pwu8fM3iZWL%2BGBgIWXAMTwtECADk1y9JA7pih3cPp%2BUcz4mF5igSsdcCu5VAofgDQTXbTRtuO3bivAR9%2B86JLLz110btgNNBWIYWBIvojigaIsK%2B%2BMHq8ZVHEmJjAasjkDDgvXlx%2Bes%2B%2B8t8rCtcGRBjD%2BPVCQhfW73RvWVqC8T5bWX2iRY0NCP%2F4NzxYfiL6ZEjnuU3YF3PSnLNcdhpbl64iinmYKMTABwaB6pgYvg4WlQgNDJ0HGDBSa6M2yuAk%2Bno%2Fz%2FDHZUfHz7x4rW%2FCn9MPSJc8eUiu8hIRwoPxqR8Ao%2FTKweRWVjppk985W71K8BnhK8gl0t50mbaGw5vR5Rnjijc4Ay64GtnEaqk9JO43VXPtxqhyYuG6aKercZGuLdpRWwKVx%2FpHU6PCQjnkUyHXqxDv1VTV3bwtEK8X5skwv%2FrtvAY6pgGM4aubtDDsgSPdDEKgX5yNA%2B1MkmqFzwPBQQx7pg%2BSmkBdjPv1po0nAFKCZ4eQo6dQ4FOpqVl7EtA4HeB3LpW7I4CEDxpMRDe5MRxYdjKSBjCIDvu9Dvk4RReMPr7WLmhQz2OZgK4ZyrCIZVxF702vXqdnSQkPnBqEnkZ9gNJKTXKSVZQYiBrsTQbs%2Fmoqi7EDrrTxIJ8mLVAdhr1ykcmBCJ2r9CVO&X-Amz-Signature=fd63218eb52f639451016180341ca53e158f2755e0fd4b3b127cda8c4e25a2f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE36QOM4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGK9P8M8XcqakpNNaa6Hgnx%2F9gdiC2qyJNxZKNxtl3djAiBqQjb6c8RhKOknXQt%2BoCIXqiQQf2tdti%2B0OPfiwiYZkiqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiAHAXn%2FGAcWlKMWXKtwD2pyeS32XknyftS9mGesF8YpZPs2FoIId8w%2FEoQDCIwnRc%2FJ%2F7ZMT1DVpN85wImu4jm%2FyZTo53mlzF2zAfhMUu9qw9wdrH%2BiZK%2Fe9jyAHPrDOPBxHhlJfZYRXtloImuiDg35KEDodjEmeZ%2F41Zmz9X5x8K5oz7Knz5loIXHqsvY%2F7RE1x4nGD6Ghcn8g3Vz9siF0FSuNMbkZPcoD2A2Jc9VPC8Xs45eqUbRxmXpXw%2F5gcTnM971fkZbPyJC6T8sJBGf1IBbk%2FbGa7m6vU4snnzGAHExOwvrhxQhcoqPzx43E4uxRuKzaa8d8lMf9hFGYRXQil5pTkNUmQqrcAgw6Lgd1UZvwQubFMC3cVibbDdqvpUUHIA%2Fl41dBi5RPqUf2vmHcZ%2BcawVUjjf%2FfE8M5frx1qzXVVIratfhBqmLHZ8Ewn3B8JhJcWFAkimmthW5ZJJHvhvXVXcHjtFpaQhWvUpZEP8so27Cwue2D5VuJcTaXak9qbiS03DzlbSI7LKquhfATJYFPcoCVH71pihr14Pm03wWXhZ%2BdPaRZdQoUHqhJVTdRvNvg3ncvlVjubofx17vum4eOP4mZGcQUKy7siHmekD9AzK0j5K8hg5DDbJLR6RoMuOBeFbPUWf44wzvrtvAY6pgG1VwZBIDF%2FgThfpjUa9tjL9PcjBQhqeNoKuC0jR6sfWAh0g%2FzrqUuZrt7NlUa8GqTwkx0MSs78qkQ8C2f38ulIluZ3kf51PbwhjNPyxZFLGwFMkkLJz%2FZleNSZeBxDP8CvF79aqGa%2BQevA4T6XaX%2BvaT%2Fr7XxYeHS%2BFxjrlK8wpB4BEqtrAv0cIQzdVT0oBmjnHAncYAj527X7texUqmWHrJyc0SlD&X-Amz-Signature=4035e5aef459de7b4075fc62898edccff0672f3601b7760f0a8c15faabd0fbb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EU3VHNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDpXPCrvFOYa30XZxlTrF4WS8T%2FkqyEkRQbEhHVoqwOUAiB3x5sBzxHsFzYRXtp5kmlZ2ekqydVgItHBO2yDOw%2BQNSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK%2BEVjpTN6mlKwCbKKtwDUG1veyM5OJIQa0PxRMMVYFG8tnEl4vP5ttS%2B3BIg2iLMnHIdM6hd1R%2B4LJlWktjYj9orIEldB9f2y%2BsyrTxaW1xCl%2FbI5ZhpqCBjZBdq%2B7pjBBsxbSfKPMgYTbLbHLeqECc0rxykwRrA89jIp4%2FmfzQsTeVJ4PZFTmP%2BNGWjjGBjdw7IWi4HMtxHrighrCxKhpI2SHqQxq44UDeNp9jFuUg0Mu0nnA1iOVwFGj%2FxPSFiaAMcQvWEx5pvwPNB5MwJT%2F6PnqummcBQs2yfRy5EZUTU%2FVto9eXQjEg4%2FC3admHt2oNr4Ur%2BMr6Wh6e69GePwGtiNcueOKOM2fXmfX7KfuHhVJyUNI0SX4ToZVD5ittJQ14BUyaZiayLUfxPBU%2BIC%2BqbHuQOU5TvVteWv9YvYaAYun%2F5lod5YadJoSpO4%2FaefqE5z2VcOSYjXJvCmOsl%2Bw%2B5RibUdmBqLhSTkxFdgxsJCZwiGAaOPZnUuZlmVTQoUcExYlxUKCyIxTm6PF7kmrNls1GDn8IA5N%2FTt56XvwphTGD5Dy4rc37XP9gnIujEEg%2BaYBn62qw5VMHYPB2m2i%2FyM2WiXtduNDM4%2FWPgQ1QFZNQxIGERYmEfxThBLVrWP9dnHge39iB6I5kwxfrtvAY6pgEoL6Polas1cAbJtRNSPXwzUySxwveAxGUlBdL%2Bfv8rB8B5vjhZrxxbFMQEXkP7Ythdp6jNBcdXeerKVlonF6yH5BlPdRAda7tQE0u%2Bw4oLeC0bUCCqun%2F6BrfNrwIVuNZ8q3nzQWlKumXQzWM3pWAEVJxcSLTzp18XqLkWeRaJXEwLyMF77BhDKjYVxkGhjHC2xePjWKZakoIetV0Wnm930kVQKT58&X-Amz-Signature=8d9ea2466208218447d786e8aca2d27078e9413a17c5e3000bcd99134d75377a&X-Amz-SignedHeaders=host&x-id=GetObject)
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