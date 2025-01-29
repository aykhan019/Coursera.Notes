

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=7d7de231326d3ca0bab3df282555aff7fd0fc6f7145624379da60f216d5f0720&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=f6e7382a6df5ad6d3242649bc49f37c496bf53c7225d273911935c87d29fede8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=6d232fc393f408621c84860c52579b077d059cb4d3d6a4c3f849a913c0742581&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=0c3e86c1238de510b1ed4ec907a052a7a00deb0ab40fd1ff0ca55e8ff77fb1ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=306b7c011fe5a682eb2c6656391acd722396f74ff2f05c596463438f600686b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=dc0128fcacceb4d285f40f7888d1761ef7ed29a51c46882298257772b75d7ead&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=2c173babcc561b8d7ee857e943071d45be30eac7673d7aabce8fe28163ff934b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=f7741a04a53a06ea1df3e15a08942a223ff7faec779bfe9864d8f24b2f1bd208&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=039b0f9d0b2e65dc786c55afa69924249ee3734e3d8803aa45e6269805039a59&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673IPQLBO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcGtL6BIByrTTnPfikIlI1HSGiUdNgtrPBTtrqOTEMmAIgWEy8X%2F%2FJlfvxoQXpIOgJRQtknWM%2Fg7VkCZrSyfEyhQoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpx4rZ%2BMk5FrHFtuyrcAx%2FMuihOFzXxnatpqYeiN8rMdHG9HlPrr24HTsJLcUttIkQr7gBYZ4bBmOw%2BeDzOlK7oSUl%2Bhouy8bS66oBtKMPQr0AY%2BoEMugmTil9%2BhHa8K8FH5cnyRSXsFqRgYGYWYNYDfLF2byYSvIng8o%2BlstUB1I%2BNOLlhssfag9WiQHimDMWm6Fy8DcpfzfW%2BaZ7BJAHgU4mMqMc81plXyCQrrPXPE5XRYZKdPZmbyu4yOkEr0e7cAa%2FM80yjxZ4ugNMV7ciT99aR8dQgRdVuFIB4rtjE7TOM8oJtf7Y6TYXsQdME%2B%2FCrYyOgQknslqAatkmOlUWjNthEwkBRsv26b866v62ePdefDsLJU4%2Bzws2Ow4ztu3Zz%2Bts7RxUTA40%2FWEUKxNNUYxYFJZiM6nKJbkk%2FrMiVRweEua179ShvNF04oGzeqoULIGig%2FcSJVjZGgTcmgfn6fvwSqHnDYBgNAdgQBGSfnel1pXRke5hWuZpJba4cZOkPfzd%2FluW2KWYFrb%2F5jsfNDShY7LTepxt1t5o%2FAX0AQCxJ25Pkjg5%2BftC0Ppgc7k2o7hTMT%2BfU%2BwCN5jA7JDwliOtzi2indUBabZw6FOJ0gGndiMp1td9qTWJHXTUWw5fj%2Bmb9H2Qpg3GlMO3%2B57wGOqUBqrc3GZxxJ5oMXxxJNhOT%2BGCzK%2Fx4iyvvwtLyi0CplW0URYTmtEPlRJMa6gzdKCSIm99dWVIEV91z7Xgr0KJxgEM50KA%2BeDGgA89yhR1AvQ%2Bi7U8dnxT%2BhWvWtpZRBbEeoiKB3sOHxd0gPCdldNoPUh7Ue3NnETNps92NOxDJ4XANsfDmX3shqwLx6QjzfW3DakU2R4S9SNcpBOdK9ebgI%2BWQQRlH&X-Amz-Signature=9ee6a985f0366742f59cd122b96d61dfb6caf6dd86dec32f6998a3f84a7a5931&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673IPQLBO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcGtL6BIByrTTnPfikIlI1HSGiUdNgtrPBTtrqOTEMmAIgWEy8X%2F%2FJlfvxoQXpIOgJRQtknWM%2Fg7VkCZrSyfEyhQoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpx4rZ%2BMk5FrHFtuyrcAx%2FMuihOFzXxnatpqYeiN8rMdHG9HlPrr24HTsJLcUttIkQr7gBYZ4bBmOw%2BeDzOlK7oSUl%2Bhouy8bS66oBtKMPQr0AY%2BoEMugmTil9%2BhHa8K8FH5cnyRSXsFqRgYGYWYNYDfLF2byYSvIng8o%2BlstUB1I%2BNOLlhssfag9WiQHimDMWm6Fy8DcpfzfW%2BaZ7BJAHgU4mMqMc81plXyCQrrPXPE5XRYZKdPZmbyu4yOkEr0e7cAa%2FM80yjxZ4ugNMV7ciT99aR8dQgRdVuFIB4rtjE7TOM8oJtf7Y6TYXsQdME%2B%2FCrYyOgQknslqAatkmOlUWjNthEwkBRsv26b866v62ePdefDsLJU4%2Bzws2Ow4ztu3Zz%2Bts7RxUTA40%2FWEUKxNNUYxYFJZiM6nKJbkk%2FrMiVRweEua179ShvNF04oGzeqoULIGig%2FcSJVjZGgTcmgfn6fvwSqHnDYBgNAdgQBGSfnel1pXRke5hWuZpJba4cZOkPfzd%2FluW2KWYFrb%2F5jsfNDShY7LTepxt1t5o%2FAX0AQCxJ25Pkjg5%2BftC0Ppgc7k2o7hTMT%2BfU%2BwCN5jA7JDwliOtzi2indUBabZw6FOJ0gGndiMp1td9qTWJHXTUWw5fj%2Bmb9H2Qpg3GlMO3%2B57wGOqUBqrc3GZxxJ5oMXxxJNhOT%2BGCzK%2Fx4iyvvwtLyi0CplW0URYTmtEPlRJMa6gzdKCSIm99dWVIEV91z7Xgr0KJxgEM50KA%2BeDGgA89yhR1AvQ%2Bi7U8dnxT%2BhWvWtpZRBbEeoiKB3sOHxd0gPCdldNoPUh7Ue3NnETNps92NOxDJ4XANsfDmX3shqwLx6QjzfW3DakU2R4S9SNcpBOdK9ebgI%2BWQQRlH&X-Amz-Signature=61aec33c519f4624769902fb699734a8ec5dab8193e35f5f6c90218a7dfdb7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673IPQLBO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcGtL6BIByrTTnPfikIlI1HSGiUdNgtrPBTtrqOTEMmAIgWEy8X%2F%2FJlfvxoQXpIOgJRQtknWM%2Fg7VkCZrSyfEyhQoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpx4rZ%2BMk5FrHFtuyrcAx%2FMuihOFzXxnatpqYeiN8rMdHG9HlPrr24HTsJLcUttIkQr7gBYZ4bBmOw%2BeDzOlK7oSUl%2Bhouy8bS66oBtKMPQr0AY%2BoEMugmTil9%2BhHa8K8FH5cnyRSXsFqRgYGYWYNYDfLF2byYSvIng8o%2BlstUB1I%2BNOLlhssfag9WiQHimDMWm6Fy8DcpfzfW%2BaZ7BJAHgU4mMqMc81plXyCQrrPXPE5XRYZKdPZmbyu4yOkEr0e7cAa%2FM80yjxZ4ugNMV7ciT99aR8dQgRdVuFIB4rtjE7TOM8oJtf7Y6TYXsQdME%2B%2FCrYyOgQknslqAatkmOlUWjNthEwkBRsv26b866v62ePdefDsLJU4%2Bzws2Ow4ztu3Zz%2Bts7RxUTA40%2FWEUKxNNUYxYFJZiM6nKJbkk%2FrMiVRweEua179ShvNF04oGzeqoULIGig%2FcSJVjZGgTcmgfn6fvwSqHnDYBgNAdgQBGSfnel1pXRke5hWuZpJba4cZOkPfzd%2FluW2KWYFrb%2F5jsfNDShY7LTepxt1t5o%2FAX0AQCxJ25Pkjg5%2BftC0Ppgc7k2o7hTMT%2BfU%2BwCN5jA7JDwliOtzi2indUBabZw6FOJ0gGndiMp1td9qTWJHXTUWw5fj%2Bmb9H2Qpg3GlMO3%2B57wGOqUBqrc3GZxxJ5oMXxxJNhOT%2BGCzK%2Fx4iyvvwtLyi0CplW0URYTmtEPlRJMa6gzdKCSIm99dWVIEV91z7Xgr0KJxgEM50KA%2BeDGgA89yhR1AvQ%2Bi7U8dnxT%2BhWvWtpZRBbEeoiKB3sOHxd0gPCdldNoPUh7Ue3NnETNps92NOxDJ4XANsfDmX3shqwLx6QjzfW3DakU2R4S9SNcpBOdK9ebgI%2BWQQRlH&X-Amz-Signature=024d88c7dbe8a331365e6e52f1b73aaa83d18a77e80fd5e46b9bc0ac22c60b2c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=f8de4e97b14bace622b7b1456286454a717be2a705b8aa2ad64a4bc11d55c245&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=8a9990641635a51c9e8196065544bfdaff3a02bdc0795bf09d5c9bb3d3cfca7f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=dd519760e1e785245d13195b3bea908d190814000c07836c0d729d32652be954&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=61a366aaf047813ac1f708cf04a6f4d581da3d93dcd20e28c5ff79be0ce1ec77&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=c0f3751bfd37dead421295739ca6f9afae9576f31c3cd040f743e2da5739fac3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGF6LSJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTuDQiwlNSkBeyKmjIw0UTyMgfuRrFC2UOv%2F87W1J%2FRAIhAKUckpMS5VibJRSkRupT48uV2Rdtleg629jKV5xU3FRHKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVCDOT7YYO8lOEOcMq3AONjFuDFVx1AfN0jCw7bD3pO%2B1wN23bkJ112%2F74IVlA0CcSzv66vJB303qT%2FWCnyqmEuue%2BJKEMDIxpIkHHn5DUhbclFG1wEy%2BfEcYeYO27TtBaUBo%2Fef4u8SnLrkwp5IFr9rYS8a%2BOeRB6RhNKlU64vbgTDbGdD63N%2B6n0PjkR1NbrKx%2FT8bRzYipDE725rCHET4ysHvhVIYUHoyqP0wzbOxN%2BuWrGbiuIFQKm0IhJLTfjvLEScB2WIaS%2FjL23J0S1v4qt2YcNENqmQQ%2Bo%2FozurkprBS6vjMHXAyPECRv14TJoM5y65p3XA7nCFObIloPwmRk9dnSVpuUjfXsNVG03kFQq%2BDObDJqbF6V0404%2FFjkNUbl%2Bk2imhb425OcXf3f31ORDb9hqJOSBHriPvmFeLUx4NP1amiTm9hClW0m8QzHD%2B7UzGhqXPtMqp8UK%2F8WcLYsVS2wZFnNdWbdPJoi%2FH%2FNWHQh4yVbU0nZSYNxXUxTwB2itCzuNtXb7PNhdRDOGGf32Y%2FdLTwzEB0QZ7JfuVZkvgnQaINu5UGV1gBjyatfnqduEd7ICvJCqLFgvLDIg4dEOAQwpo1gtFRaRHLT%2Baqb%2FEi730hBQg3iLz1f63MH1XNtVhnm1Izmo0zDD%2F%2Be8BjqkAcd2Gji4IMuGnVDpfhTqLK36Ra9YAVPRdbhbu4Ky1LL%2FpjUV3U97AEJJu82qjnVh%2BUaNnerxLolzfnaUrDlkpFkZHuW0J%2B7Xg69nTAcZrXJGejHYpuFCGVQ6jB40Hw8i7VH8dnR79MRa7c8OzLwQ3y2RAJl6tOCjEHAGUiDsu0Vsx0shjH%2FMKWZbMggT1sZrgwEjIFLYhOKN%2BuXqMKESo4%2FTdLeT&X-Amz-Signature=edad4c0c2b2073e03f962351d0e86d78dc887ecc16616904e539948220da1af0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCC6ZAT3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9Ak0unI%2BvvAFjqgOaHUSdBAxBwlDsBSDQnFzlyCvcgIhAPLks1uPd3h7q34s5V9fNfOo88nVaR2XCePRkCceK99lKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj2yTBJTplpoaUjKIq3AOMa4YPN7DPUDzRNuQj4n2lnOKfuCs9%2B7wDH8LW4F2bYXUtjwdPOBTDbiCuR1syKu%2BreAbh0Vxn09VzZ%2Fc8A1M6WYZbMomaxP%2Bm%2BJqyfuypu0p6l7CNwtQgvYDnamahJ53E4gTgRmp5XsUfAkUaB1Cp8tRSW2aU0aojXVLBAac4V5uJ5on3q0oxwP%2BoXmH9cwCwhHOKw4glh4%2F44kPPAwFP%2FBbTzBkC6sOT3rz52RDvAE8iMS6MBu2QDDZ2LEQZz6qfebm7vWPgqkL1yiObA%2Fj%2FE3PbtI6cb%2FtOTNFL0Jg8tE37zuc41Vby2OO9EMb%2BT%2Bp1vgVw0Px3bdQA8wy2KdpBCXpPwkQLc5GKkxRWj07qi2cmJlIdlwzn3FLQf64so7sJ49N2e5Y4O5%2Bw91mymqSb1L1lznPqINXuuFVLKLXT7Cju5AgPjsHsLH%2FAbfqwTQk2ZuFZu395lyE%2FU0kIs7nbLBazH5mv33gIKxqiF6fOlpH19x0ZYkqJOIMmgziiHNmNxEDkdcGAAlR5hukqDaqBGiswWf4iTh1JxgxdRsU82abcAZIku4h7jFLkTOcD2ahfCOeLZzDwxVoFd0h6OamC%2BZgRrDweuIN2BbUMhDIzSTX33R8MQ2%2BKY12ccDDv%2Fue8BjqkAVpShfE8BUvDmhttZYZh9VmN7NkzCcpYW3aZ57%2BLF84on153PWHZIwdBDS7qAAfFwadOSUI3jUTJ7oN7MA2wPp8IJM6s1d6Hk68GboX2pKoenHlI9HXWY6FQCjI2GfJcB%2Fli2k%2Fwvy4H7qDpkSLhv8gdMh0ZPcqK%2B2%2F1UDiAaUdxx5uArDUjK9X9RCCT%2FpMWZ95tyJqUoSl5LowJsTNGyZkvLRqw&X-Amz-Signature=b3b30088ae9075fba289163a56132a50e7de54beea01f395fdb3bb7e168825f4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCC6ZAT3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9Ak0unI%2BvvAFjqgOaHUSdBAxBwlDsBSDQnFzlyCvcgIhAPLks1uPd3h7q34s5V9fNfOo88nVaR2XCePRkCceK99lKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj2yTBJTplpoaUjKIq3AOMa4YPN7DPUDzRNuQj4n2lnOKfuCs9%2B7wDH8LW4F2bYXUtjwdPOBTDbiCuR1syKu%2BreAbh0Vxn09VzZ%2Fc8A1M6WYZbMomaxP%2Bm%2BJqyfuypu0p6l7CNwtQgvYDnamahJ53E4gTgRmp5XsUfAkUaB1Cp8tRSW2aU0aojXVLBAac4V5uJ5on3q0oxwP%2BoXmH9cwCwhHOKw4glh4%2F44kPPAwFP%2FBbTzBkC6sOT3rz52RDvAE8iMS6MBu2QDDZ2LEQZz6qfebm7vWPgqkL1yiObA%2Fj%2FE3PbtI6cb%2FtOTNFL0Jg8tE37zuc41Vby2OO9EMb%2BT%2Bp1vgVw0Px3bdQA8wy2KdpBCXpPwkQLc5GKkxRWj07qi2cmJlIdlwzn3FLQf64so7sJ49N2e5Y4O5%2Bw91mymqSb1L1lznPqINXuuFVLKLXT7Cju5AgPjsHsLH%2FAbfqwTQk2ZuFZu395lyE%2FU0kIs7nbLBazH5mv33gIKxqiF6fOlpH19x0ZYkqJOIMmgziiHNmNxEDkdcGAAlR5hukqDaqBGiswWf4iTh1JxgxdRsU82abcAZIku4h7jFLkTOcD2ahfCOeLZzDwxVoFd0h6OamC%2BZgRrDweuIN2BbUMhDIzSTX33R8MQ2%2BKY12ccDDv%2Fue8BjqkAVpShfE8BUvDmhttZYZh9VmN7NkzCcpYW3aZ57%2BLF84on153PWHZIwdBDS7qAAfFwadOSUI3jUTJ7oN7MA2wPp8IJM6s1d6Hk68GboX2pKoenHlI9HXWY6FQCjI2GfJcB%2Fli2k%2Fwvy4H7qDpkSLhv8gdMh0ZPcqK%2B2%2F1UDiAaUdxx5uArDUjK9X9RCCT%2FpMWZ95tyJqUoSl5LowJsTNGyZkvLRqw&X-Amz-Signature=df6a42526a20a34f74851d14ea92ddce5d34b539e2fc2eafc37920aa0ef5097d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYWA2MTZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7R%2BfyC6T9MvUgI%2BIMstwxcOPxQXgOqhaKd%2BFTrkr%2BsgIgPErBUTab1ALwKeiY7K%2BCZn3HT%2BvGGd0w1cPn75Zsa0IqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRVLG10I%2FOeBOWQ3yrcAxnG4tVYT2AXif7LScbNHnJmVmt%2BEe45ApCJEOuAcR%2B5zIjYtaQF7CAqeXZiiWFMwHF083o5gvbm947fuaaGoeh12CcslkjWijw78tSjfXxmEXUpbA%2BysN9DmhG%2FswtyFzrHhwOPZ0qXA3Iwc6fOE0ALqi2AUD7JDTNR6uYKhOw7xDtrz%2FqYA9kwK4dqGZnOH8VBX%2BrP4BHuhbzjVngRIOtOR%2Fn%2FkxGuTDVkCZmtyzZNwmjOGRqUg69kWn%2ByjyoQ3xWuxU6Xy8a%2BtmDf8GTxYIH6koGR016CbxMUeQIy7W2pX4AiGTJz6LJWUq7B5j%2BWr%2FOXMg1UKXoSUNDNa8Nt0rAg48rW7zhqpO%2FLOYF0V2p8zK7c9QKCz2ALNYeiafRMrXWoJM63OcT3vEj0%2F9wh8I0e09kOiaxLJ47Ha%2Fwx%2FD1n5qacXJPYTBQO1A84zpSOGqfuuFvokkLtqmf6alc25ZoqFGF%2BjJrkWjxn9o2TDdZoQ2tzDvYZHU%2FSiAUFMvi2jeuwiWSb7a4XlPgFYuGQw4bFBQhQ8iOdrFWPCTBdMq%2F%2BpAf1KX%2B%2FRRXrArNGG2LxSN5C3K5yOYOPBRePUMsE%2Bfl2O3L8kxTICUXtW%2F0YaXKufZZujtsADzSpsbBRMPH%2B57wGOqUBSetRgZtv0HiKV0DIjXB3Z%2Bg6WupeS9k9pFeuSF1mgiHmxW%2BZxF%2B%2FDMlWRA9ZB8CK1kZBLhpUe1wYEceLRxMFmNiHQ7HKkP%2FnnvT17NIKbHjI9cgyRFlAUrShovylJWets%2BVLaTjpaVLAfhW05jeW3pIlxzaZ0%2BdkAnkIonHFlZiBn%2FC9gxCmhV72vVv2%2FYVV88ArD1sHdbxmo706kDOojH54ypiQ&X-Amz-Signature=ab32cf7515d95a05aa75d3c4213a92671dfff0603ebed1851492a11d2a96301c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEUPSM4F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BhmT43K0YDPgwbt92PYaHLqCMLufDBGpftcNM5KCblAiEA7fNOiHmiCWQSOt1KTwsYa3g1U0aaTNnirbRxAY59ALEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYrbrPq9icipDiC5CrcA4K8wzjFopbawz5rKqvcrTqZZA04XQY%2BnTMJpIRtg%2FYPSj3ulUHs89r%2FS8XubwNszRMCuaq44BJ6C1eeo5dS5ssf5ggEer1fmhMdZyz%2F%2BbDzvXqhsViVmNRtdh2bdkfAxJWApVtnT1Ba9U%2Fn6B9rSUcCf0gTXTSMmMxU7t%2FXchSPwclSIrswdNyRJXs9G1wVqTgwBNrcJ%2BcGhgWaBH5bnmhKrDJBH9gXkgLmklE%2FUXJl3V%2FnA2VSugJJSA8Z6av19C43F0DBvYrzk7QS%2F7Qn7RRF1rUbsAGZ5edEqMpE0wZWJ4W0TwixEeoVOZvqNN%2BqmHAcWBEi4dC4Gxpdx8J8mrmXC7pKaR5Dt4TkAgFeNYywyuptb6Ahr1vueTptHVFACBrYNtn6YKr3TwczPV29BZTirYoz9Xp4JijLmdbwzCRheVb920aEYYQoNLZaAl%2Fz88KuTLwgwhlHSYCugHofTFTV%2Bu5Kut6r%2FzfICIF1uzQVjYykPxZNxW2bY56kSyFbl%2B5IIKHfjPh0GuRRqBxRtGn5G27vPCGYefJSSlsj8v%2B%2BZD8n49mBHmcxM22PoR6P8xZ5aoLOoWSNTbgYBkg%2Bb2Pnt8yuejZCxPySyjvnzuEnhuc3LbY54zeCmF9WMNn%2B57wGOqUBjTh1cO4qko%2BJPQz3KTNRu6VR9MDINgdBzPqSvXriIkYMZCTYpuSk1OB%2FN4jl%2FekketD2a2TmtCkXHzkuA6Zaec5kr0q%2FwmFYGVDXkPTJwYmVqH2sGmBFBw6VBV8t%2BB%2FMEPUxDfN7%2BcbSl6nfAS5Bz6gG7LsFx%2FSvlokMAiHu5FJk5l%2FEZjXdk7Zggh3A6CVux4SzPvbdneJpQ%2FCxyvindePF%2BfTj&X-Amz-Signature=01b1eff1a9d05cef36d75b199c7279b09f1481ac4b633f3a14a5a267cb2d60a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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