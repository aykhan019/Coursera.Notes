

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=e015648c5daa6abc8204384c425c2a7050cfea4e43a16e8cad341696da357e58&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=f1823e4d3fd70777843be4cea014aa435a755986ae703e1e8a28333292615fcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=067760f5610461e311a88e5c9e0168b7190a97674ec5cac01adecd05ab091222&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=2fd75995bb983c48bb76fde409d32d3d7da1575b53889eb878f9a716ab04b5d3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=3e105575295ca0102874d6f1ce3f0e7cae5df7984f70c3f133fcc076f1f3937b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=f636c2d9684549a344dc4e1294ea7084463808285e527258b60a77c40dbcabea&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=f9eafd35a9df7b0a75a8ed4f9dc89b140cce1f2f0e54dd618a28339afbb1738f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=ddce38890a1bbf1369ce85b1b83af874ed08a9ad7c3574387a11e0399738d026&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=02961838045dff629ecf144729f5a6ae2ba272fdfa72901fa87a2ef371695e74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HUJXQB5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7gP6wE7AktYrSZcAchU1WtbgWuHnXlCwDN9G%2FAatxUgIhANb%2BuCxHJrJFe%2FcHcc8iVmZcfTaNYgo5tChADh%2F%2FNx4uKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7ASJz7Lk8txZGkQ0q3ANvRruFMf4DhukBXdEUmxgJ5xPHprwsfUQ0BBlL3EDgHbzY0T1PdpuhcYgMi2iZuvoMYp3WAxh%2BqOshZ7dt8UlV4inKtHuNfy5fcwG%2BsCjac8mXjpbtmv33F%2FupEeqBe%2Fn02vo1NK1kGydeI9CKZwR64pOr07Vgzj%2FtpxQjooHTE9yhRX6Vr979JZowl6frqtNX2cYX8S10noU8sX%2F3ptdhcwzBiQwYbl8MWQmOni07OIx3HgzVq1eOZD4cuzB5hDmvXh1BsdAX7W%2F1nqxUzmpm%2F3OQn1cleHsZV4SCIHV1ZPfKqQc20tzrzALbOnpGIPP1p4gFVTgGUxxIiytp7HbCkwUn0tkRoUgaembjs8c7i1JsYcq743DJcw6qhZ3N0dn07BSKMbkOweKhc1cBjkihS0HZ%2FWi3SvRL2XqQdIwQPyaaA3szzqFQjZnfsnqJqbJ7VSC400iU7PA7lmx8QA6DqVVAVtmeDaL5QdUkyW5D4mQmoLTRHHpF6V158QihpnDd5DUT7TpgZz8FT85JIM6k5fQDg4ZFIxaJZsv%2B4gaJD8%2B%2F9k4vqzKO5bxeKrd28wWVYcZbuN%2BKQlyrO5KFz7ZbE77W95JcqEAV%2BEzm4zg6c2GEmm%2BJyVoHZXqdGjCl9PK8BjqkARbcqUalN%2B0j%2Bt%2B%2FTWShatnCyBM75V0z64xx4ko2ZHSsv1lrnGhfDWq1Lgj%2FXKPJRrMpSQgxcB%2FiyE2VW7ccUrATeGTSsJ5D0E6MB8DkB0tyFz6mCxFupY36TOBgkoiFGD885CLrdiZmpZvrH%2F0qo%2FYNsesEtHajKdSl7iRNjws6zrB3X1TJQRDjA306zpPZ%2BSr2wlOUraMJgP4w1nmYTFFijKuE&X-Amz-Signature=81b798c481fdce6a1f5717088261220ecb0ec81d7f25e413c084d8dfeee47ee6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HUJXQB5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7gP6wE7AktYrSZcAchU1WtbgWuHnXlCwDN9G%2FAatxUgIhANb%2BuCxHJrJFe%2FcHcc8iVmZcfTaNYgo5tChADh%2F%2FNx4uKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7ASJz7Lk8txZGkQ0q3ANvRruFMf4DhukBXdEUmxgJ5xPHprwsfUQ0BBlL3EDgHbzY0T1PdpuhcYgMi2iZuvoMYp3WAxh%2BqOshZ7dt8UlV4inKtHuNfy5fcwG%2BsCjac8mXjpbtmv33F%2FupEeqBe%2Fn02vo1NK1kGydeI9CKZwR64pOr07Vgzj%2FtpxQjooHTE9yhRX6Vr979JZowl6frqtNX2cYX8S10noU8sX%2F3ptdhcwzBiQwYbl8MWQmOni07OIx3HgzVq1eOZD4cuzB5hDmvXh1BsdAX7W%2F1nqxUzmpm%2F3OQn1cleHsZV4SCIHV1ZPfKqQc20tzrzALbOnpGIPP1p4gFVTgGUxxIiytp7HbCkwUn0tkRoUgaembjs8c7i1JsYcq743DJcw6qhZ3N0dn07BSKMbkOweKhc1cBjkihS0HZ%2FWi3SvRL2XqQdIwQPyaaA3szzqFQjZnfsnqJqbJ7VSC400iU7PA7lmx8QA6DqVVAVtmeDaL5QdUkyW5D4mQmoLTRHHpF6V158QihpnDd5DUT7TpgZz8FT85JIM6k5fQDg4ZFIxaJZsv%2B4gaJD8%2B%2F9k4vqzKO5bxeKrd28wWVYcZbuN%2BKQlyrO5KFz7ZbE77W95JcqEAV%2BEzm4zg6c2GEmm%2BJyVoHZXqdGjCl9PK8BjqkARbcqUalN%2B0j%2Bt%2B%2FTWShatnCyBM75V0z64xx4ko2ZHSsv1lrnGhfDWq1Lgj%2FXKPJRrMpSQgxcB%2FiyE2VW7ccUrATeGTSsJ5D0E6MB8DkB0tyFz6mCxFupY36TOBgkoiFGD885CLrdiZmpZvrH%2F0qo%2FYNsesEtHajKdSl7iRNjws6zrB3X1TJQRDjA306zpPZ%2BSr2wlOUraMJgP4w1nmYTFFijKuE&X-Amz-Signature=a02688811a74224919361c7df8ee039ba1559ef10252f9dae5ece9d9362119df&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HUJXQB5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7gP6wE7AktYrSZcAchU1WtbgWuHnXlCwDN9G%2FAatxUgIhANb%2BuCxHJrJFe%2FcHcc8iVmZcfTaNYgo5tChADh%2F%2FNx4uKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7ASJz7Lk8txZGkQ0q3ANvRruFMf4DhukBXdEUmxgJ5xPHprwsfUQ0BBlL3EDgHbzY0T1PdpuhcYgMi2iZuvoMYp3WAxh%2BqOshZ7dt8UlV4inKtHuNfy5fcwG%2BsCjac8mXjpbtmv33F%2FupEeqBe%2Fn02vo1NK1kGydeI9CKZwR64pOr07Vgzj%2FtpxQjooHTE9yhRX6Vr979JZowl6frqtNX2cYX8S10noU8sX%2F3ptdhcwzBiQwYbl8MWQmOni07OIx3HgzVq1eOZD4cuzB5hDmvXh1BsdAX7W%2F1nqxUzmpm%2F3OQn1cleHsZV4SCIHV1ZPfKqQc20tzrzALbOnpGIPP1p4gFVTgGUxxIiytp7HbCkwUn0tkRoUgaembjs8c7i1JsYcq743DJcw6qhZ3N0dn07BSKMbkOweKhc1cBjkihS0HZ%2FWi3SvRL2XqQdIwQPyaaA3szzqFQjZnfsnqJqbJ7VSC400iU7PA7lmx8QA6DqVVAVtmeDaL5QdUkyW5D4mQmoLTRHHpF6V158QihpnDd5DUT7TpgZz8FT85JIM6k5fQDg4ZFIxaJZsv%2B4gaJD8%2B%2F9k4vqzKO5bxeKrd28wWVYcZbuN%2BKQlyrO5KFz7ZbE77W95JcqEAV%2BEzm4zg6c2GEmm%2BJyVoHZXqdGjCl9PK8BjqkARbcqUalN%2B0j%2Bt%2B%2FTWShatnCyBM75V0z64xx4ko2ZHSsv1lrnGhfDWq1Lgj%2FXKPJRrMpSQgxcB%2FiyE2VW7ccUrATeGTSsJ5D0E6MB8DkB0tyFz6mCxFupY36TOBgkoiFGD885CLrdiZmpZvrH%2F0qo%2FYNsesEtHajKdSl7iRNjws6zrB3X1TJQRDjA306zpPZ%2BSr2wlOUraMJgP4w1nmYTFFijKuE&X-Amz-Signature=d75989020fa3ddc39fef7f4219571aa3bff4bd5e32eb6d6eac7c1db4fa8a1773&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=560d5b3fa489ec1a94ec8140f5d74bf2be53c778f107fb0a5691859aacf05bed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=cdbc47ab0a5df002b5d845a45e2db9833ef0d940d74ba9ff9accabb88f1d7ac5&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=006be84d03e0b310d169e0c4677a4079213c161c92d67ecee3532a33e3286f92&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=aa3e7b5d29ac2fcb87f7c5f71c456a017f2880edfa9cb33f6469cb36ee541340&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=bc5948eba13c74cf851d396523a630ee7a0dd9e7f7e49c10c972459fa0558849&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R2QA3KW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjhjI08YsZyysPF10M4ig0X2Vzsue9rH%2FE8MCor8f2GAiEAtJ5iNvIHBDvwL8lBTrIG%2BPZoYh6K2ibGHPD%2FB35bg3kqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAz31Idnp12DdXe0oCrcA%2FexxOkKUlOa3Dz%2F7ta%2BdaOpHrY%2FMaVD2EcSCAXp%2BuGM84REcUmlqqXCwGU1u9jXKyGRbu3earSRmzvI7hqYsBF2XDMoj5MWPmr5Lbn8paE6qRsbJfg%2FnrKUewqrdFKozrRAAKIbEMkkC46uOOLKaPkPj8CSy3WJ5%2F2kRwZ4TPm5fTXUIpAqJCy6Y%2BTEzIYbUvCqpQaNMtSk7%2FYiNaNqwLyS9ixwM%2BUzA4%2Bwmh9RXyefyWLI2OHUrMqx9jHEioKAZtOXHUSxQuyHcOdOfCk85VzOYPkfvbNbTnmT1FXXfwiHzoqfe7nvrBD3o0bT4oUcOzMk7z1FqvyWgKPhuAhwe%2BwRzkPjqHtWaEWJ2YQMSaz8TN9ZlWUg6MsRAhS8fyv0niOvf7An9vgICgyNOyDrkXH%2F2D3Ke3w41SbB9KI%2BNRRT57nqQuUyQnEj6%2F0u8tuKAxwJlBSqAx7dDooHKBXSOwijANrDv3PxZNeoNRpbD2roiGmtoGP0rH9TFj%2B%2BhlHXBdAI0YYe%2Bg%2BnZ1jbTBPstoH%2Faq8LMQqHW5LcGh%2BHoon3TTtZYLNFCXy6GHmWI30DhyYoWLl%2FLHIQzaQ3vWuSmlzDYqGaz8CFs%2Bgk3A%2B1LxJ%2B9gexUu7juijMKs5sMPvz8rwGOqUBZ3rtVHaLeipVmTqPQy5ZCX4r1vWKwJwObuXTx%2FqeIxpIlcKAO2b1%2BV2br1IX9SmUao7ikTt%2Bl2ZGBMBADTnJZFVZTminaLB5QKAvy7xtTwfzvGgfhPzqEkufz5CNdU99hGpnbEXaR16OWP7xNGXx66WMNJy0lj5VIEOs1SHHWvC%2BXcg%2FupVFEeDu6lD%2FDB82MDA6XJjUxFhnBWeSgddwlDg1Ique&X-Amz-Signature=b39b018455384c7074460a2853d1cdf44c48b5a2b3dd25a797323f057be0a6d1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644MN4KAO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCymSRlZFD7yt9Z07oAx9MHEu0CuqisONNZFP7rBrRxIQIhAIa%2BQ0ObilB7%2Bml3LSUPPzHB4xloXqyYKPjtuN%2Fp%2BQVjKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwA9sTYjQYNmcFAyjQq3ANGvNH2BYQ%2BKB%2F29tflA5b1XYuH5q2f2wRqdHReDsuDpUrmiSOLMNr%2B79TLFwozMvCLjbEOrqg0Ahdz%2F%2F6EDhJiUkGL88n5%2BXTSSYHiER3VVvLBarfha3%2Fgtpr8BpHlYgl7cCv4wlVl%2Fbo9PemDia%2FKfzZTy7Q9JkPVQkEsyg9Ym3rLnTqYJLidurLWtZd33JD8BedSauHEzZYBvyBJm00jmXdKRezUnwejGNarmXTSBhy%2BeqDVRzMS6%2Bc%2FhBm%2BbhFQAqzlkVHVAgHCTMI41eXY2AMhGATHGtN%2BlTwjULF9NhDA77nhK3qw63ZPHVEnd8CdICfOgn6orP8Piw2n92vsg1TjxZZ9Cl6HnwGA4g%2B05oTKpBFwyf5HA3sGzwMzOv2YI2MxV%2FKzgtvHk6Lem7VibMjbQUUw9smvbiF3qMLm63XT7%2FDVzWF2MBiU%2FNmVPhTn4Vkcafm5UECdltlORmaTF9OpwZTxZFfgWqeKimjYwFs0w14YY2zaRhQcPqymXtk31vAuJnnwHYroVVaOEUF7W%2BcfT1KPiNoL96%2BB8eEfy6iJV8w6RrUl6gT5vZV89fy7lH1wK9tvupojP%2FchRQJBQwaR79GjV2%2BnoMWoteG6phybWsrJiN8eVdquSDDl8%2FK8BjqkAQWjU1n%2FVNPiq7RTM5xTd%2BIOdnc9dj%2BMkcbNcfKDTG13fwAK4X1oDIboThV%2Fg5l%2Bf0SEubVCJxk%2BJPyeo9LxLyxKch%2BRp834uWyVeFCSPSTGRlAdk0HOrJ7qILQX3toshpFvbwkDKX5dMB6JxegUIHNnqU9ihs64PXIcMRRlTlJYrGlBNKXEQAC1h9Qkq1DBFXoSvmK0ovykCsEVHOTHOsJy9IFq&X-Amz-Signature=727972668821bda605bf583e2fbe7629c71aca7abbd3103bff7f6d864b348bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644MN4KAO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCymSRlZFD7yt9Z07oAx9MHEu0CuqisONNZFP7rBrRxIQIhAIa%2BQ0ObilB7%2Bml3LSUPPzHB4xloXqyYKPjtuN%2Fp%2BQVjKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwA9sTYjQYNmcFAyjQq3ANGvNH2BYQ%2BKB%2F29tflA5b1XYuH5q2f2wRqdHReDsuDpUrmiSOLMNr%2B79TLFwozMvCLjbEOrqg0Ahdz%2F%2F6EDhJiUkGL88n5%2BXTSSYHiER3VVvLBarfha3%2Fgtpr8BpHlYgl7cCv4wlVl%2Fbo9PemDia%2FKfzZTy7Q9JkPVQkEsyg9Ym3rLnTqYJLidurLWtZd33JD8BedSauHEzZYBvyBJm00jmXdKRezUnwejGNarmXTSBhy%2BeqDVRzMS6%2Bc%2FhBm%2BbhFQAqzlkVHVAgHCTMI41eXY2AMhGATHGtN%2BlTwjULF9NhDA77nhK3qw63ZPHVEnd8CdICfOgn6orP8Piw2n92vsg1TjxZZ9Cl6HnwGA4g%2B05oTKpBFwyf5HA3sGzwMzOv2YI2MxV%2FKzgtvHk6Lem7VibMjbQUUw9smvbiF3qMLm63XT7%2FDVzWF2MBiU%2FNmVPhTn4Vkcafm5UECdltlORmaTF9OpwZTxZFfgWqeKimjYwFs0w14YY2zaRhQcPqymXtk31vAuJnnwHYroVVaOEUF7W%2BcfT1KPiNoL96%2BB8eEfy6iJV8w6RrUl6gT5vZV89fy7lH1wK9tvupojP%2FchRQJBQwaR79GjV2%2BnoMWoteG6phybWsrJiN8eVdquSDDl8%2FK8BjqkAQWjU1n%2FVNPiq7RTM5xTd%2BIOdnc9dj%2BMkcbNcfKDTG13fwAK4X1oDIboThV%2Fg5l%2Bf0SEubVCJxk%2BJPyeo9LxLyxKch%2BRp834uWyVeFCSPSTGRlAdk0HOrJ7qILQX3toshpFvbwkDKX5dMB6JxegUIHNnqU9ihs64PXIcMRRlTlJYrGlBNKXEQAC1h9Qkq1DBFXoSvmK0ovykCsEVHOTHOsJy9IFq&X-Amz-Signature=225f359f70e256e40f66d5d9405369ae55898ea40d580d3c9a7359085c4c8fb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMTJ23WQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC6tLcJ%2FPAHTesxWF2MDh%2Fsyqnp%2B1WVk4w89Z%2BvbzNVQIhAOCw%2BmZ8ttD41DEF%2BJLmQ7k0HAlWPVZdvQwNNQH7H7x8KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0i7sB8YT7XE%2BIFW4q3AODcNwf6NLXDAPi9O1rjjquSfyQSApvq9piJhV3TDM7F8Jl3G%2FQlHoxE%2Fe4SP%2B5MvCXSQpIuFCJ9fnaeHgJAxrqfQBoym59A%2FirWZTnXVRZAp0gLylCGi5igykHaDGKqPKkIxH2CjmWzRxCBfQ2tfSnRQOLX%2FJgWDs8uIyKq5DMLK1M2hLS8yNaNv6ydDoKYWeuILtHC9YqylrSm4zb7ECafhFNTAvsmqdePz7aOOL9IdzP3we1EqwpHxZHrvn1pkLB0wpU%2F5fkAayUfwLL0Rxq73bfCDU09hQECYvOKhCULjy23bGBAZpSvkcR3lFBOhZA9u3lHW1tWHyLU0pI0lRTMAkUazAbtaRK1U%2BPV3F%2BTfW9lkaX%2BufFi6WVLBoI72jscG11k7HSfNLrfiMoIN0UTg%2Fq%2FOJaNGdpYkqIULIOPVpEJ%2B6P6BGt3JVnXOciwH9Z2emBrG%2BXRQbu5AdIq3FTdnGpEZ6jPiN6cpR8tePQxR5NkF5waQu6zj0McBtpiSYO6qMTQbuHpAsze6eDmqBOO4J1C2VgqJJeny8XFYG17L5FjkZMJjxIBq%2FeWuj8C3QtiLNyu5FIzx8CtSHpBPCDY1bs78Jegz%2BQPqtS5iWwLf41M1gKwTunBVo5hzCF9PK8BjqkAUhKUMVKXrQUN16Q%2B8ujt1ACkV%2FPZU96a4UhUmgoEDNW7IXBUxdY9kI%2FNuvYc4LRhwDRLnBXbrIwxBVVSFRJn8Qc%2Btx3x7yUZmpGIAQ%2BNJ0pHNyzqMiho%2B01JL2nQ5IZROHNw4t7GYu7%2BuOdHlVJ%2BbFTFNYNiRFGbczG0cYJV104ArG6%2F3cZG%2BtvMfvThxknm%2B5YqhgupFqZBitXsJG72UkYEYGp&X-Amz-Signature=2370b064cb09e9d769d163847899887ab238a397e973c50c82967289af7a67d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQT3HTMS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDPr4lwm9lhd459for3nM5jv0CkuAmJj7hunI%2FJ8z1SwIgW9jWcE8lXbRRKh2CTB%2Be8zqMjLGPR3B%2BxZ%2FjtjyexHwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBZvp42bP%2FyVGJ7KSrcA0KKOTTJys261lddhQOAaz%2FdWK0US86rxEaUz9N7bSLGc1Lvq5CL3rN367pMyZ1KDbaAt%2BKXEGMef7js5PXWEChcMS9P1L%2FsB8MdHNyxEscGJozG879L%2B4Y74RrbWGjycfLq7%2Bm2N%2FfyauwycCOz6P1Q90MvnZs8ziRvhUa5OSM8Wpqq9aYbnFTA8YIpTZbi3GHvEWo2T7ijp1su0jwPOUxBgnMXp9VJgIAfWQuqmOnojRrD1XMgFRowde%2F%2BwbXWZazCnM2zylbkt5uEyy35Scxjv9KiZlhITD%2Fp3q0i5PeW3n55EellWxb6oJ4T2iPCZYKvZP1kaifg0tOMczx8AOU%2BUhkrsV1UZTw2Dill1nQBjKwI9ysP%2Bq%2B%2B%2FWYS0%2BzKGaop6vUWPQ6cnTRZyQX3AtYBChTtnPgDCl%2FH%2B22IOmbICrr0TXMbhBOzx48ECUeU7hctgH2ZliX5qsrA%2FXVkIueROqMXMUvgTYTA7P%2BgQkuXZ7vye6tERMtfet8WBwLQfAJVIE0a0mSM3i4w%2BYGOW9PdjpjglLMdtOyeXEXB9uiP3JGF7v6Fuc6bVptc%2B69vfjsuef0YTVM5sPA7V6BfEQ6yZB0jf8GwDQmVDvhSdEbrTtgmnLntC%2F2CLeyAMO3z8rwGOqUBWQqPQfaPhNsxg%2FXSLcaxqiICgsnIccg5fPYO0qjXKAEQfEu7S5fwBSQyDNRl7ayfCBk3WPWgk6uqOt3LREaSr7MpnTUXuKnNfrDAK619FMbd4m%2B%2F4PRRKbRVBOvXTTwhZdGjIUkVjgCtUXGBw8zpWo85dvmvQhLWRhfHmiFb1zRDqbXC%2BeojMqQAk1Jne3N3QhkOH%2BMcs3ca%2F9cxLxzd7C6P3q4J&X-Amz-Signature=58e4cae58413c870b86e85b0ad9cac004b1435beb7994cf910ddbe01c82df788&X-Amz-SignedHeaders=host&x-id=GetObject)
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