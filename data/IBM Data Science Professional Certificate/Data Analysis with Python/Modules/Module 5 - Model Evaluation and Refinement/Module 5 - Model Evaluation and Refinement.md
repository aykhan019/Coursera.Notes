

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=23ec427e536018ebd16e5b20c353fddc24f257eeb89c0ad96cee3684ccce867b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=339b6fbd0d89d5d01d6a29a2f0483d9028f292fd130592a088472464b8df4d69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=4c5d0e25bc1bb90d2168bc8943b24eb501f57d73aa2fbcbc7255a981ea65b6fe&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=82382804ce4f11260cc352b337e48219afd1c89b42009d3417dbc9c9d45df509&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=819e3aea7427b1d2b07077ebaefb2501fcfae704701a445c36446b4a68b64a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=f06348f4d59034544c99b3e62a02a087280e3b7d659e4393f4c2b96ac45b5cc3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=8107cf0e2acdbee0338422650b9436038e67f806c92181ffd29fa0ac733d9728&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=395d64ab721246bb3b47593346a68470bd9768dc187bb763cdf5a1e1d7d9ec0c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=c63efda6138df7bd51ce50aa65070d9ffe8ff74456726de81714a5b608a6edda&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3PTYYJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICs7hILH9WEBTAdSQZanY2WpCVpIFRMsvbE1e%2BP8nXSKAiBZHiJmw48T%2B%2FwaXnQEAyhOkb7ziUiX75g%2FgXI%2Fmf%2FxRSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqCxyZ1LVvvyTBU7dKtwDqkOOanFsRoP71GCDYoJXf3yxhM48xp0jD2EzwnuI1%2FKLUeBM1rgAnjHgYe7dY7URFfqm372UxqfaHmG37QBzgqJLn8SDHhMMY67Obk23xvCIweV29fjQgMKxGru2tjXT6Mkf6HRg%2FY3C4NGXK13rvig2V2RMOoEk5%2BexhGq4xo50yleU9Hb4meZkF2IWVDu8NsR1BuoYFvfJ5PsCr2%2FkcbsyoBc57geEEi6YNHkCqYo2yMt9pfPyWa4zyR4J6xDiXaQYcqgEAW15zp0UZ1%2Biet3C%2FxOueswQ7qSIHV%2FlCaLeKWL%2F9Y8oGpvr54ZSgn%2F%2FfadbE67cVnBi0%2BR2Vp33pkxYZRB1hQbR%2FD%2BLCQNLqPK2P7VxRIeHCUgPlxgXOcvXra%2FFmAFq8Mokcap%2BaqEXNvlC1vjieqY1Ix3GguSo2LQTdGGpvnZsy7rm1Y%2F0LEB96zDWDEjzRvhdyqWd5vpy4C8snxktziwAy3uqKVOVl35V4nP3SLrKvuvm7ed6VK14VcUd1laiz%2FQLWK6OQRu5HdAbT9lybJeHVbFZIgEsobXCmOZb4O%2BcWKK6ciVyXzJoh3EfocCk0E%2FiFSMxC1ZrHpc0Eu9%2F5Dlf5HdD3R%2FeFzjgT2x98coRnRYFxdsw2L%2F9vAY6pgH%2BTi%2BINaPJcO7qyblSk5g9iyekoyKTTDRN26Cku3hBVsYAN75OrISfAH0TFpGHxmMnpZhYx2uowCbDdAccYg8LMmtvJdOsjQIfGaR2VpkAdjjxTPK2rm610UZNK4jF8DzhXkhjo%2BJHjS7ZAKHCQwaYeh8OgMffCUFLhVjp0CMKsXVZQOC1rWXu%2FeDcFMUpZs%2Bj1e0Re%2BRdIfFpA18tHtasdfkwc7gv&X-Amz-Signature=1bd70d02ac709c8b6e92e9470a48414d01a8623c63d5d3970e7d70acbbcf5eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3PTYYJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICs7hILH9WEBTAdSQZanY2WpCVpIFRMsvbE1e%2BP8nXSKAiBZHiJmw48T%2B%2FwaXnQEAyhOkb7ziUiX75g%2FgXI%2Fmf%2FxRSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqCxyZ1LVvvyTBU7dKtwDqkOOanFsRoP71GCDYoJXf3yxhM48xp0jD2EzwnuI1%2FKLUeBM1rgAnjHgYe7dY7URFfqm372UxqfaHmG37QBzgqJLn8SDHhMMY67Obk23xvCIweV29fjQgMKxGru2tjXT6Mkf6HRg%2FY3C4NGXK13rvig2V2RMOoEk5%2BexhGq4xo50yleU9Hb4meZkF2IWVDu8NsR1BuoYFvfJ5PsCr2%2FkcbsyoBc57geEEi6YNHkCqYo2yMt9pfPyWa4zyR4J6xDiXaQYcqgEAW15zp0UZ1%2Biet3C%2FxOueswQ7qSIHV%2FlCaLeKWL%2F9Y8oGpvr54ZSgn%2F%2FfadbE67cVnBi0%2BR2Vp33pkxYZRB1hQbR%2FD%2BLCQNLqPK2P7VxRIeHCUgPlxgXOcvXra%2FFmAFq8Mokcap%2BaqEXNvlC1vjieqY1Ix3GguSo2LQTdGGpvnZsy7rm1Y%2F0LEB96zDWDEjzRvhdyqWd5vpy4C8snxktziwAy3uqKVOVl35V4nP3SLrKvuvm7ed6VK14VcUd1laiz%2FQLWK6OQRu5HdAbT9lybJeHVbFZIgEsobXCmOZb4O%2BcWKK6ciVyXzJoh3EfocCk0E%2FiFSMxC1ZrHpc0Eu9%2F5Dlf5HdD3R%2FeFzjgT2x98coRnRYFxdsw2L%2F9vAY6pgH%2BTi%2BINaPJcO7qyblSk5g9iyekoyKTTDRN26Cku3hBVsYAN75OrISfAH0TFpGHxmMnpZhYx2uowCbDdAccYg8LMmtvJdOsjQIfGaR2VpkAdjjxTPK2rm610UZNK4jF8DzhXkhjo%2BJHjS7ZAKHCQwaYeh8OgMffCUFLhVjp0CMKsXVZQOC1rWXu%2FeDcFMUpZs%2Bj1e0Re%2BRdIfFpA18tHtasdfkwc7gv&X-Amz-Signature=fc032705e3804c112973be4d793cbdab1234d6c180e40b80c221758628693c90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3PTYYJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICs7hILH9WEBTAdSQZanY2WpCVpIFRMsvbE1e%2BP8nXSKAiBZHiJmw48T%2B%2FwaXnQEAyhOkb7ziUiX75g%2FgXI%2Fmf%2FxRSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqCxyZ1LVvvyTBU7dKtwDqkOOanFsRoP71GCDYoJXf3yxhM48xp0jD2EzwnuI1%2FKLUeBM1rgAnjHgYe7dY7URFfqm372UxqfaHmG37QBzgqJLn8SDHhMMY67Obk23xvCIweV29fjQgMKxGru2tjXT6Mkf6HRg%2FY3C4NGXK13rvig2V2RMOoEk5%2BexhGq4xo50yleU9Hb4meZkF2IWVDu8NsR1BuoYFvfJ5PsCr2%2FkcbsyoBc57geEEi6YNHkCqYo2yMt9pfPyWa4zyR4J6xDiXaQYcqgEAW15zp0UZ1%2Biet3C%2FxOueswQ7qSIHV%2FlCaLeKWL%2F9Y8oGpvr54ZSgn%2F%2FfadbE67cVnBi0%2BR2Vp33pkxYZRB1hQbR%2FD%2BLCQNLqPK2P7VxRIeHCUgPlxgXOcvXra%2FFmAFq8Mokcap%2BaqEXNvlC1vjieqY1Ix3GguSo2LQTdGGpvnZsy7rm1Y%2F0LEB96zDWDEjzRvhdyqWd5vpy4C8snxktziwAy3uqKVOVl35V4nP3SLrKvuvm7ed6VK14VcUd1laiz%2FQLWK6OQRu5HdAbT9lybJeHVbFZIgEsobXCmOZb4O%2BcWKK6ciVyXzJoh3EfocCk0E%2FiFSMxC1ZrHpc0Eu9%2F5Dlf5HdD3R%2FeFzjgT2x98coRnRYFxdsw2L%2F9vAY6pgH%2BTi%2BINaPJcO7qyblSk5g9iyekoyKTTDRN26Cku3hBVsYAN75OrISfAH0TFpGHxmMnpZhYx2uowCbDdAccYg8LMmtvJdOsjQIfGaR2VpkAdjjxTPK2rm610UZNK4jF8DzhXkhjo%2BJHjS7ZAKHCQwaYeh8OgMffCUFLhVjp0CMKsXVZQOC1rWXu%2FeDcFMUpZs%2Bj1e0Re%2BRdIfFpA18tHtasdfkwc7gv&X-Amz-Signature=470ee3e3f558d78a27951f09f40ceedb7c7fdb5b6f052b1ba4e555ae24f298eb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=c1e6fccd3f2c010712957aee68aefa1687ee22d1489dffb63b88b210a2456970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=42a278e97350ee55643c5c03ba44cc6439f47c5b7ef445e9930fd87a950b9fed&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=ee2b1de7150f30eaa8f1678e9baa57c198dcaa66b82da86004c70b14efb644d8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=189bca7c60d43a9ba51b4092beb76b01209be0d1c16501a016e60a630b0d723b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=2cfdc9756bd17ee344545910073b90699ae9d54fa8ef74d5d7fdc2d3bd4cae7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5WPP7XM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgRJe2xno9xuqTruvtHIUSevXmBGloQBUeqa2Tj%2F7fmgIhAOcWeQi8CUhhkGe6r%2Fn3rpnoQUtZW2bFqtsPMvqfhRz8KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweNV6L97oI%2FmZ4ll4q3ANwfC%2BzBDGEijlRWBStHYH43HolZ4kJXMo9n1o5jKdJK5ddjTvMJZy%2F4UGY3cnrfJpGGiNPDXyjBje4tiTDZSWdkru9z9%2FDhTxDLSqFTJtfYprMPSS9GPPxZj8LzoX4FvFd4UT0G6p%2FxDBgnlNR5mxQETjnEs9z8e2u%2B0f9qrNfZVwRfGZ5Mq8%2Fy0Bckz9gA6SxcyppSgk8BLp5oI589TkFdEbJP8fmjfRiVjOnGzTKkVr2%2FQgHWLwJ48q7bqUl7A6Gzwzsg%2F9mDy9277TozHd6hcJCFznJkwoFti0j5w68qzgoD5QHGWAsaEscdl%2F6d9xQK5c3mw2hKX58T42HEth5tiE%2B990zuztRLkh%2BXjk36wbqlrGp6fvaot%2BZ4J3Dht0lfypT5041lBf%2BcOjuDeYvh93pqC0iFVX%2BOaPfjKyeBl9monzsYus6ruIOWlTrUi2iExY8dg%2FO4v4pBQVaJKkNsXwTmWZTj70Rm2b9DpSJYdz%2BEk7vNhdJxoGb7oNqKf1EifWmyoWiR6rGedrr%2FSggpuqKiJIcB6ZmfC5SWDFHOV09rKFKlaTFLgRWigktB%2FQlT6rIx8dWlTD5zdcex4Kd1NC%2BZ29aqGw1OxMCxSywCno44BPM%2B1%2FAVU7%2BezDkuP28BjqkAVrrNS6tWL%2BVJlmfXDTXgF2jBHOLdXCFo6GJ09pmknpSyeWl2lioemqozQoaH2JZj75j1NpotONQc%2FfaDAr9fJIewoGC4uCo3Wlou%2FDFuExRGsD0p5KFgU0noxpWWx%2B5kG02hSlJRL%2Fxp6Sx%2Fazuh1UVxT8pCH%2BrE8b4QL9j0BOMqHPXaGl4BhGeD6MsAbYVnGjdvymP2T524TAwdfWBJXgXG%2BdN&X-Amz-Signature=fe1b89d6991c1e4e86b9c8e8f1ecd89604892fcb7ce703bc7dca2fdebbb3199d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMTL7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBtCe6Mfmn30hSPA1i6rw9coKIaPWFTA%2BoPM30B9MaQIgWyrGJ73XxIupGO0FfAygBxQXWqyM%2FhdbI0jPSvuLH60qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPy6fHj3nomdiq9q0ircA%2BFF%2FOdhOJZgCq6y5vZpF9h3RBm%2FOvHBaC5YAaLy6IeO32%2FoeHanEDaqaIzf2BNcKmEw7vKcZbWd1T%2FH2dh705UV4gEQHTNlzSs3j0mrONNta0kxB6PMaMHCD2pZftQx8CYqw6cyxESg77YO0yD91V4vWroyMg0pSMvdnbkeSgvdLHFwytbV0%2BtcIwZSHn2IioggJKex1yY07QR7yaXYZIbiDEq4QipDt%2F8aQlhYNBK6RKVj%2FoLEfv2xUOONxFFzRoA3iqWqGsfcBgHozA29NuJR5mz9EPRFkehHF2X76aSaKUYwIC2yJktYnJSucTLjPqTR6oa7t8qZP40CIDup4LN46AjIzhzrl5BD8ZSa9U96mWbdUHU9XSPLDJ6IbPOlyK1Ur6SDT3jTvc1YIj6GIr2JoCKn6ce%2BzOxWSDIPn3wGElmlGVFUaGHlFdYU%2FSqjYvgA5C8xj2YFpUdcW5ASOyoNs%2BxKjigNnza73devqNiruilWGpK%2Bv3SQYmL08My4IbTL5UUwejsj%2B56vtP7vCpnvxKAeN%2FwIsEYwCCUAkLLI%2FAla9UfEaZb12rxcRnAV6rHZcfq9KUNQzzoAe9z5BlobAig%2FlITujDX4sg%2B%2BcPSGh1eGxAcLTl5v9%2B2nMNy7%2FbwGOqUBl3BBSG%2Bz3TUuw9IgOzV6MTUgD9pT8ROYQK5bcwh7RSK9DTu3GD8kc%2FGX%2FbjZJVO8emSAphdRnkcCICwWhu9xrddft%2BGeUX52TIXk%2FT59w0R33SoUoJQD21Vt12Ae5KXE9HyPWLSFMlMt6PMc88GtxNtjbj6grIHAQpH1nRVZlPZTKky%2B8zHNuKI9kdZOMUeG7%2FWgpYOcYzGYhWM0xi6TMW83a8bJ&X-Amz-Signature=db81d0f7a9505ec7838ad4b18341bddb861b049e0fbe644eae8416295a3825e3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROMTL7NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBtCe6Mfmn30hSPA1i6rw9coKIaPWFTA%2BoPM30B9MaQIgWyrGJ73XxIupGO0FfAygBxQXWqyM%2FhdbI0jPSvuLH60qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPy6fHj3nomdiq9q0ircA%2BFF%2FOdhOJZgCq6y5vZpF9h3RBm%2FOvHBaC5YAaLy6IeO32%2FoeHanEDaqaIzf2BNcKmEw7vKcZbWd1T%2FH2dh705UV4gEQHTNlzSs3j0mrONNta0kxB6PMaMHCD2pZftQx8CYqw6cyxESg77YO0yD91V4vWroyMg0pSMvdnbkeSgvdLHFwytbV0%2BtcIwZSHn2IioggJKex1yY07QR7yaXYZIbiDEq4QipDt%2F8aQlhYNBK6RKVj%2FoLEfv2xUOONxFFzRoA3iqWqGsfcBgHozA29NuJR5mz9EPRFkehHF2X76aSaKUYwIC2yJktYnJSucTLjPqTR6oa7t8qZP40CIDup4LN46AjIzhzrl5BD8ZSa9U96mWbdUHU9XSPLDJ6IbPOlyK1Ur6SDT3jTvc1YIj6GIr2JoCKn6ce%2BzOxWSDIPn3wGElmlGVFUaGHlFdYU%2FSqjYvgA5C8xj2YFpUdcW5ASOyoNs%2BxKjigNnza73devqNiruilWGpK%2Bv3SQYmL08My4IbTL5UUwejsj%2B56vtP7vCpnvxKAeN%2FwIsEYwCCUAkLLI%2FAla9UfEaZb12rxcRnAV6rHZcfq9KUNQzzoAe9z5BlobAig%2FlITujDX4sg%2B%2BcPSGh1eGxAcLTl5v9%2B2nMNy7%2FbwGOqUBl3BBSG%2Bz3TUuw9IgOzV6MTUgD9pT8ROYQK5bcwh7RSK9DTu3GD8kc%2FGX%2FbjZJVO8emSAphdRnkcCICwWhu9xrddft%2BGeUX52TIXk%2FT59w0R33SoUoJQD21Vt12Ae5KXE9HyPWLSFMlMt6PMc88GtxNtjbj6grIHAQpH1nRVZlPZTKky%2B8zHNuKI9kdZOMUeG7%2FWgpYOcYzGYhWM0xi6TMW83a8bJ&X-Amz-Signature=5b8f9b339eccdedfbb84f98defd5562a4cff3d55bf94158af8b7e3ac327ca921&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNJTSVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo%2F%2BXKQZ68PkfLtgmTBcZzH6n8b4mI%2BH6YqSf5fDOc3AiAWQRHuvAfRSvIDZpEvDEcy%2BfOdEpTykYQBALnzcYs%2BVCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsspphb85nXhH982YKtwDoIZH8OZxWpB7vE%2FZ%2FxCPiIfELoLH%2FkjRa0okN4VvvscCgGsv97SZGlZAjNWBEHuPrAz8XpezWdKREDQdn0LB4Xy%2Fv%2BAZYTpUIBjxXFY2bGIahvmTyFk3DLuU9wAxADN7ejWLpmZ9KpsbMG5Iua%2F4o3H3l%2F4TdErj6jHL84kAFoBviyzQ1h07WsAq1ijPOgVY0a1Ep3qzGGtVG2zVvPLNSZDFCDVQToRyTvReC4RyEzmhAGNLzHqsXwXsX02zxXf5bhjsuRiEMANG2a1bISo3mgW6DvY%2Ft3p3atdhkXdA%2FZ8qhdwiGOEJvGNXx2xxlTGg%2BJiYAK6Hu8%2FW3jhL2yX2s5qVARu8pzDNoPXvWy65YZH537CufUvbez%2F62pEkiPwie4FGbL9MmNDH1tvw7kh%2BVs8SENZuXgXwVRgBo5L%2BFy0CBBvmWxGHakDZ0KfgFmtS1ZIEGvfYEd4x4R0ox4rb1%2F2Q2na4PVgA6ItTWVmYMvq4EK7c4IdsWkDodrV9UYgYEWAAybCcmWY5KEA%2FSos6DpvhbVdrVaxypzEh5kduqolqu7PR%2FhniiExEDQdY0sJSq1%2B8tkMJMjeVuF%2FBj%2Fc05mNXc3%2Bk06eVMILyhdK5k5gADaQzFwoUXDs0Ku0wucH9vAY6pgHYOvRYzrf3R%2B%2B8qWX29q6gcglPOCSnx5lqRW2TUbWIPVMLg3rInjP%2BH7d5pwX9UY7YawP69vlZTi92a5rdfKOwxF2PGMPzH%2B9Svpr5pSFZ6ezC4%2BlX%2B4rgFlt8NlT8lvv2SwsfOHI53UKfDekfKDBMbRt1S3nBbYyWWeBuDQrLpvsVzrqYea9kPN16PR1UH9kj4U6Wl3VPem0ctzWkcWOCcgm4tBRA&X-Amz-Signature=31ec434eb4df27f50f72c78f35076804009f15a84257fd2db5e9e78aa503425d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=f04a7775559336a259f3363aa63a78bfe68e0c4af0fe92b52232ad476376ceb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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