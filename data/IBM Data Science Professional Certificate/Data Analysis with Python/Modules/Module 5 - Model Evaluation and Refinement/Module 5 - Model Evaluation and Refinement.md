

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=77642c02638509e747e9dce1acbbe8260bc96c1305d8f0b7f1d7747754b41e61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=f86ff645f41aa4eecf486f4bddbaf0bb1cab449de92477a361723fe5d6f47cae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=45cd9a1e1d0e71581b185bf81c6af579431aa99745bcb2de4fd920cdda586adf&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=65e53a0db9315423cbdd6414c85e7a9d418c391ba22d4f999b92c2f4069aa25a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=48cbf8610b4d698986e39cea2734ccb5ac2295af5b5c4072436cc2fa18146cd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=83eff532fce13add383a2b5eeeb862d966a4cfca6c6cc4a8f6a7a5c487bc1343&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=a269fe3d33b968bae42bf9d3fbefa08f24fa7affdb62b03b0d9b82133ef024de&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=c34c83b9d4c638c9de34023435fed19cf2de631638f5e528a8391485fb9d4b1e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=eb55f6baa342d3f19b367ff32a908656c35ac21f39b4c00fe3d7646d45230879&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SROSOOUG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDlmeofZtK9ZhfqQHo22HwU%2BUxBVv5Qb%2BLoGmFf8gE5CAiEA8s3PDYZtMLESr%2F9qOrYZx%2BrUZZtUItXBS%2BSJ46A0oKsq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDPkq7hS6WzEUV7%2BamircA5FVo8tBAuEftdHYzYtgkBHMZCWXDmnot35ujZeBmX2O%2B%2Bcton36zN9blI7Gh%2BGco2eBGNs7jPvZPcsyb9fqKD%2B3pxrUWHhg9PMypZ9cko%2BfM1Kz24AP%2Bnr%2BDOjd004rl1YOIUwfc%2BYUyhmECjZWrx0eK9XReVgQrBfWz8CldljqjI3Wtvaj509dV2mgtH3yMx3HBfcMs5RYVm%2FUHjLXvk4J930Y6bOvZc3wyfNvbmJCzsqSt%2FxfotIXZ%2BelmMCwN%2FL1BInwW8d3Huk7RKSMPUj4BlbyNJTGNOVk6LVsFv%2BMqsoEEwggzfakoVxle06VV7U49VMBruz5OX2sutvwmMsN7i3Yxkij%2BAPQEEyee3qZmYJQGvtj5Gqxi4ddjw4JOlWP2EmZGGmTFIE2QmB7VkYfe7IUB%2Ft94FN%2Fa8FNC06DUwi1cn6SZdkdU0jAlDX19gB%2FOSONgYmRCyhtAI1WrzPOcgA11GffpIKg%2FmUxNwucw5DhRWt0gXfJL30Awk8KQZS1fx9Ymg2pKlkGldchOOD2Do5W6YpbNEs7AY0H%2FxQf1TiluThILcCvX25LxsvP1%2BOAyTE2dsXT1sQyTTQYPsbt1Z57bI1Svi%2By5W4zia%2Bt0GMDoB%2BwAViu95zXMI%2FNir0GOqUBkTQFR9lyJTFzurxRNd1HqwgW%2BRvZla3xtGBxvU0UuvXNczb1JUI62sTQNgVr8Ogh0z2MwIGdWK2d5rPcTaxw6%2FIvkXAag7qde2qe5x62ICOU2FtzhiQS20Xwzmg18rk%2ByX3UHhni6NGYWD9K1X7yr1Osf%2FfztqTxXiDhtre%2FZLwMs4dgjZheHJVf%2BQnLdX6gDU5bICgGgMBP2FqBL09zJn0wndxV&X-Amz-Signature=b247655be488784aeaa2144ee5c4b0bbb56f846660452b257d956c2b76e11c4f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SROSOOUG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDlmeofZtK9ZhfqQHo22HwU%2BUxBVv5Qb%2BLoGmFf8gE5CAiEA8s3PDYZtMLESr%2F9qOrYZx%2BrUZZtUItXBS%2BSJ46A0oKsq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDPkq7hS6WzEUV7%2BamircA5FVo8tBAuEftdHYzYtgkBHMZCWXDmnot35ujZeBmX2O%2B%2Bcton36zN9blI7Gh%2BGco2eBGNs7jPvZPcsyb9fqKD%2B3pxrUWHhg9PMypZ9cko%2BfM1Kz24AP%2Bnr%2BDOjd004rl1YOIUwfc%2BYUyhmECjZWrx0eK9XReVgQrBfWz8CldljqjI3Wtvaj509dV2mgtH3yMx3HBfcMs5RYVm%2FUHjLXvk4J930Y6bOvZc3wyfNvbmJCzsqSt%2FxfotIXZ%2BelmMCwN%2FL1BInwW8d3Huk7RKSMPUj4BlbyNJTGNOVk6LVsFv%2BMqsoEEwggzfakoVxle06VV7U49VMBruz5OX2sutvwmMsN7i3Yxkij%2BAPQEEyee3qZmYJQGvtj5Gqxi4ddjw4JOlWP2EmZGGmTFIE2QmB7VkYfe7IUB%2Ft94FN%2Fa8FNC06DUwi1cn6SZdkdU0jAlDX19gB%2FOSONgYmRCyhtAI1WrzPOcgA11GffpIKg%2FmUxNwucw5DhRWt0gXfJL30Awk8KQZS1fx9Ymg2pKlkGldchOOD2Do5W6YpbNEs7AY0H%2FxQf1TiluThILcCvX25LxsvP1%2BOAyTE2dsXT1sQyTTQYPsbt1Z57bI1Svi%2By5W4zia%2Bt0GMDoB%2BwAViu95zXMI%2FNir0GOqUBkTQFR9lyJTFzurxRNd1HqwgW%2BRvZla3xtGBxvU0UuvXNczb1JUI62sTQNgVr8Ogh0z2MwIGdWK2d5rPcTaxw6%2FIvkXAag7qde2qe5x62ICOU2FtzhiQS20Xwzmg18rk%2ByX3UHhni6NGYWD9K1X7yr1Osf%2FfztqTxXiDhtre%2FZLwMs4dgjZheHJVf%2BQnLdX6gDU5bICgGgMBP2FqBL09zJn0wndxV&X-Amz-Signature=7cfb90b7a151bc326433baa79a06bc29d680e082b6f10de1abf894e2e99349b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SROSOOUG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDlmeofZtK9ZhfqQHo22HwU%2BUxBVv5Qb%2BLoGmFf8gE5CAiEA8s3PDYZtMLESr%2F9qOrYZx%2BrUZZtUItXBS%2BSJ46A0oKsq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDPkq7hS6WzEUV7%2BamircA5FVo8tBAuEftdHYzYtgkBHMZCWXDmnot35ujZeBmX2O%2B%2Bcton36zN9blI7Gh%2BGco2eBGNs7jPvZPcsyb9fqKD%2B3pxrUWHhg9PMypZ9cko%2BfM1Kz24AP%2Bnr%2BDOjd004rl1YOIUwfc%2BYUyhmECjZWrx0eK9XReVgQrBfWz8CldljqjI3Wtvaj509dV2mgtH3yMx3HBfcMs5RYVm%2FUHjLXvk4J930Y6bOvZc3wyfNvbmJCzsqSt%2FxfotIXZ%2BelmMCwN%2FL1BInwW8d3Huk7RKSMPUj4BlbyNJTGNOVk6LVsFv%2BMqsoEEwggzfakoVxle06VV7U49VMBruz5OX2sutvwmMsN7i3Yxkij%2BAPQEEyee3qZmYJQGvtj5Gqxi4ddjw4JOlWP2EmZGGmTFIE2QmB7VkYfe7IUB%2Ft94FN%2Fa8FNC06DUwi1cn6SZdkdU0jAlDX19gB%2FOSONgYmRCyhtAI1WrzPOcgA11GffpIKg%2FmUxNwucw5DhRWt0gXfJL30Awk8KQZS1fx9Ymg2pKlkGldchOOD2Do5W6YpbNEs7AY0H%2FxQf1TiluThILcCvX25LxsvP1%2BOAyTE2dsXT1sQyTTQYPsbt1Z57bI1Svi%2By5W4zia%2Bt0GMDoB%2BwAViu95zXMI%2FNir0GOqUBkTQFR9lyJTFzurxRNd1HqwgW%2BRvZla3xtGBxvU0UuvXNczb1JUI62sTQNgVr8Ogh0z2MwIGdWK2d5rPcTaxw6%2FIvkXAag7qde2qe5x62ICOU2FtzhiQS20Xwzmg18rk%2ByX3UHhni6NGYWD9K1X7yr1Osf%2FfztqTxXiDhtre%2FZLwMs4dgjZheHJVf%2BQnLdX6gDU5bICgGgMBP2FqBL09zJn0wndxV&X-Amz-Signature=ec9e1e568e8ae2cf8463ef473e7a6915c085bfe8a7dae5f396a198ac6f5a6f09&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=7b38a0fc9ae09856aa76a309b43113a0873a097ab471301a1799ead2eb0e63cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=bde38b0cf4bcf5ddf79b86638092f45790e613588cd94ec7d75dbde90f1626a9&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=65ad23185ed658e5f42e34c6a764a957376984437527879d3c7497335a033458&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=665d98e76c6ef10c7280debfb4cad9ab741267fa33b3fd7db3963b9c032c2e88&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=ab6ed4f9b50f839dbbb26642fb5e33c52bafa0280776821be485a5b364b35a9e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAOXVADU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGvvivbLcY5NoWxDBf%2Fc0MUA3Jyj%2FHoCX3ris6X4slP9AiEA7Jad6gJaZbwD%2BhnSiSuZCIsq910lJFBtq6Rd70S8lNoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDM6aOgIVjJek1ySloSrcA9vRxOqpgDj4IX3J4ys5ALqBR%2BnZJt1Zk47BCl5rN66IuwzaBPZFaV7ug9h%2FU%2B8DNM0vJVj0LAAIpfdzj0uRocWTgby0Nmzqhc2bQ5B7%2B%2F7BZV657KaYcvrnGlzQqOay%2BDXXGA7vDrs%2F4E7TZt3zGK859WBGGP9Gb5aaNAufra0Vqcf8AmJamS8c25oMIDyQwlD4ZWrTBvz1sGG00Gfgo66146wVEObxHw7Objes9Gaun%2FuQdFJqTj8OimSNondNsqu1dbI29ekAYqEFfiu9ziuBono0r48GH4XZQJixXZS7LdfTFrSZ50I38FOoovDwizgVhqAyaLhsjjpEoZ7mtqgtF5XHB%2Fn1vK9%2FIjcPxRd8DZ8dlryL3iK3MOqiC73lOJpcye477wdJbTDMQf%2FMv2fGuiW2rfwzOUD1NGx8zkS2Ulu%2FJmvgHAkBbHbJ%2BfNM6vZwt2V2i4uQlth73YHkhvMiZfjt9a%2BMrusbUpkmGkTPc1Q5dWj5LRFZ%2FeeBDxhrYkKnyvQ%2FD9NA%2BadIaDFRpFi4AfQtCMUPX%2Fb5QMA4i9OifEB%2FofTQ0ovtaQ5nPjvdDBVadznIupEc0%2BaZmK4SbpHk%2B7dUtE1oj9xRgPWjZ6cq7SMWM%2Fb%2Bus3gAysRMOPNir0GOqUB4Tk%2Fdu80T6HEVeVgAZdsRAB3lsVlxdoZlKKhYXgpv3n%2B3eWcV14XejTQDxYRtxOqbeN5b3id%2BItxLlynNQvmyZB7vgyV3aoikjw1X%2FMAfsn8VfKnrIs2z0QVQDhQzH7wIlXYaNvceG8Y6kT254XIh7ilkrE9C8T2m%2BYx4%2Bay%2B9R74WYIYaJxtlx18I9OuE7iCV5rAQuG3w6y5zXKBX7Mvl65ub%2Fq&X-Amz-Signature=4c6a740f38d66deeec0aabb39666e36f4fa749955fa0914b16f7d1f2a1065653&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQBWZCPB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIB7nTOTyovcEQveTldkMkvj2dEddTV8U2rJjeJ4%2FpG3LAiAvXD2tFs44yWH493PsaZBm9M9%2B3L1fLjNIuJlEKLdgkSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMpsjo%2BujqrEoSmahEKtwDmwypOCsIg0CA2QXRl%2FBCfXNMiRakPGV6Sm2uOk%2B4ZoTrYKE4S2HdzkhQML6SewiIqlsZLoYQdOVS8KNfk0DSKpox%2Fvcu2ArHCMUt9duZrgi1t%2FEMqufL2qvd66rQRBdCsAmNIBUZSZX4Btv9m2Lbm0WsMk7D%2BA9gqq4%2BQqyF3wdYq%2B0%2Bvjf5SB3UVTlJEatgsiM5hcCif1XM4xqCMTXENNPqR83PqFnWcWxV8L5ukRrQaqVO8VVcvStCCM5g%2BT6SU2tr3bwzbOgVJ1jp9lo8%2BxiKM1dvW6trgUt6soYraJGdGlZtxDXQyvmk7XW%2B%2B1EDhFpii%2FIYhZU%2B6PJSKQw7aFNVMl09iZnzBN4ZNSL3P5pCpMP1Q%2F6qulBg1xV6e6idRRuVhwRmqj0SXaKD%2BJnm%2FBCyT8vwVTcpoYGQkAWpyQuQ4%2FDZz3hGt2BYTycGWuDQ3iJ3JFdhQge3IT0R4fcOdV2mfQXWX%2FjnpGJLYM2KhMQDRar5o3v5GfqAYKVghpUOTf8QlNP1bghm4ZmW5hNjwHznOfke%2F9AL2t9OtzBxfppxCZjpQymDfpOQL%2FZ5%2BBP3BBNcjVuy7IpgjAbXzJ6rgL%2Fg0UqaIIA4N%2BQOyuNL4goJIePr3dJD9qa78y4wts2KvQY6pgHTHISM%2F8a3mhX4apqyDu8xP3j19eW2PqcX8gYsO72QaI39hHefTEB8pS2Pv%2F6VOZgCxNz84CAX0P89ebrV%2Bv3%2B7oJ5yGRxWewvaZttFRKyEmfHTy%2B48yUyC1r0XVwa5YrZpstiQoidYLP1rtCxMJyJgngOVq1ntKb2JQ3mMczXn4yRjxiR%2BgESE9W%2FEOAoefaJByvlo8pmdBI3%2BdQSTklJzFpY2iQj&X-Amz-Signature=6384d755257d40a59ef7b9bea4bc94631c6a0e28a824b2dffddd0b8011964851&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQBWZCPB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIB7nTOTyovcEQveTldkMkvj2dEddTV8U2rJjeJ4%2FpG3LAiAvXD2tFs44yWH493PsaZBm9M9%2B3L1fLjNIuJlEKLdgkSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMpsjo%2BujqrEoSmahEKtwDmwypOCsIg0CA2QXRl%2FBCfXNMiRakPGV6Sm2uOk%2B4ZoTrYKE4S2HdzkhQML6SewiIqlsZLoYQdOVS8KNfk0DSKpox%2Fvcu2ArHCMUt9duZrgi1t%2FEMqufL2qvd66rQRBdCsAmNIBUZSZX4Btv9m2Lbm0WsMk7D%2BA9gqq4%2BQqyF3wdYq%2B0%2Bvjf5SB3UVTlJEatgsiM5hcCif1XM4xqCMTXENNPqR83PqFnWcWxV8L5ukRrQaqVO8VVcvStCCM5g%2BT6SU2tr3bwzbOgVJ1jp9lo8%2BxiKM1dvW6trgUt6soYraJGdGlZtxDXQyvmk7XW%2B%2B1EDhFpii%2FIYhZU%2B6PJSKQw7aFNVMl09iZnzBN4ZNSL3P5pCpMP1Q%2F6qulBg1xV6e6idRRuVhwRmqj0SXaKD%2BJnm%2FBCyT8vwVTcpoYGQkAWpyQuQ4%2FDZz3hGt2BYTycGWuDQ3iJ3JFdhQge3IT0R4fcOdV2mfQXWX%2FjnpGJLYM2KhMQDRar5o3v5GfqAYKVghpUOTf8QlNP1bghm4ZmW5hNjwHznOfke%2F9AL2t9OtzBxfppxCZjpQymDfpOQL%2FZ5%2BBP3BBNcjVuy7IpgjAbXzJ6rgL%2Fg0UqaIIA4N%2BQOyuNL4goJIePr3dJD9qa78y4wts2KvQY6pgHTHISM%2F8a3mhX4apqyDu8xP3j19eW2PqcX8gYsO72QaI39hHefTEB8pS2Pv%2F6VOZgCxNz84CAX0P89ebrV%2Bv3%2B7oJ5yGRxWewvaZttFRKyEmfHTy%2B48yUyC1r0XVwa5YrZpstiQoidYLP1rtCxMJyJgngOVq1ntKb2JQ3mMczXn4yRjxiR%2BgESE9W%2FEOAoefaJByvlo8pmdBI3%2BdQSTklJzFpY2iQj&X-Amz-Signature=2853ca43895013b038857d0dfec5c106fcf40307c585319e8900dc5956bf0ddc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P6QXZBM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFUXeUhYwXPgzcq3qoygopGSKOd8O71NzKfHZ5mKsuVYAiEAwq7DumNoGl9Z05fhxhuFoeZzV9zq4hNJUzuEh7VDAW0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDP%2B09MnxMquELbsYZCrcA8ua8RVAuXKPaHy1LxifnBSX6%2Bo3qu%2B6DAYoRxnDabFwhNMhDaTR5j2x5MjyviFoDlkYO%2FdJB5vF%2Fgr%2BmW1AVfKWzCluPQKxOJE9%2BpoKjI%2BZJTkBKXPYakiHcb9ci1zTx0Ncm3hXKD4qATn5B4nJ0DHYVklYlNW8C0j5uIhbsJmH1nFSsjTxEjJYK0ejX%2BKjwudumODxUUUpyCjxS1syAx9crYAUg91ehhqaCcBAqhTWLqJTqeQRPfAznZk7rzYwpV%2FcWgZkangwHLypjyJGCbrhTS6%2FCNUCcIta5ytpCRHm6Tw4jz2br%2FLgGrdpomB6PtO%2B6ydUY0eqradh6vF5W%2FjZMuVglELJhQN%2FOsE0ZGVUg1tS3yjaYq4Nk4eQSahoQ%2BWqM5SY3YNgzBBmJTpldMohirUsd9DU%2FJso%2FDue4e6KoZ%2FNoOXznifE%2F2ACQMPo2ausknjQxXqSoglN9cLaq0KDeVpOEED5PZ2e0Y86FkiW0ClnEMiWlY8uaVIXqMjF5Gk9mmmM6Tgyi2qReywDMnCJrY48RSpnhj1f5hVteDCKPKpX2cjctxpc7S9sRcyYdFDfPfFTLzycAS5Hn7bCBqF3LFZXehV8vW6Iu1sP2TVC9lADv4LCL6xCLU40MOTMir0GOqUBXoFqaGqZp7D94PgY2THu3J6axxIxEnFF9gjhy1xKOe%2FB2jvUgsf2viI%2BW%2F0JXmXcj8fbvM06fdHYM6F8Ffvtr3ESWpe1JvYJXOyFoUBocPRMOt87vOHmt%2F7dBjWGl2FYgHkuVeQWiamVhWzgpSN9tKLCj6KZMGka18YBDbkIeuI0d%2Fk0vifydMLVPLtbm%2BlUc9fP%2FYcWGPLSX4%2Fc%2FHV%2Be%2BbfVbVn&X-Amz-Signature=d62fdafbc50af2f10eb124e6d22b484268e82bcc28d8daf65a6ef22d34e0c7bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZQBPU4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFpGPMf9Sl2CblxLaP1s4BOc3ZELz3QBmXBcPBLa78DZAiEA8hxIgG8JoG05mhHvxFzEgi6nyE2VLQoDE1nAfHiyPv0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMkHDp1rQGtSRy7hSyrcA3F4uUADB%2B2zlNDN3VANxMegBdMLMVpNc%2B%2BUT9aYsuR5Qb8CJ8cnSU%2FyV9Ev9N6%2FJ%2Bt9ptmvnMRR%2F2v2Wi1josI%2BhmomkPXRqtD7qUFTIWHZL%2Fw422lcsfNkh2I5Gqzzpr1sZjJj%2B2%2BE3nUM4l1KOYgto2Cm7urwtezgc6GP%2F5bzaB3N67labiD9yVssf%2FUApBGv%2FH06BDFLzuNXEN0BN6iywGOpQhsqQq%2BWakZtRHIgrQ1QU4fOsJFnY0uRBbw5oIhkKnA%2Bs2z92X7ifslhLdCuMoCrHTP8Dab8Z%2Fof371vMa%2BOdZY7yIMaBRF1rckFeeI7TKl0%2F0wgHJAHx0MoFM2FtuDc3UY2fkDzjRF6jcW0mc6Y%2BKdxgwGQ3bt%2Bnmjg2tzNALdiQpbpEW%2BcV5T9mxj5YP7J976LcsTWdPN6r%2F7nOA7Bw7SYJTU33q0NAdJal5L0D9wVlGW0b%2Bh7jwrbxvHZE0wwsC0FNAQ1%2FphEmfdTUrDkHVBmy17RB0VkcxoRFXn4rBNi5rReCruHOn91nSXd9%2FfskIdUEenV0dyfgaYuJJajlgn7C%2BcOvyJ5lqgeoQbp53og%2F0fqsOdcPG1tQw%2BLLcsAURfCNNU6Ka%2FPoG6hHCbH%2B2aJI5Kn04WXMKTNir0GOqUBwsiBn5DADtm0P9x9h95U4q2YHlSSWhoQKLFT3lovhtlbfkqoVr0RUI1S93Hhr2obDYnJKcYtRPAeQXnnZgFJw9JRKhb001pTSYl7o%2B7sZs0%2FVDdTE%2FVsn36e8vWwjKyipsSTttiJtp8tmvJgD7%2FMP8E3Zm3W6QszmyGeCOcgRpBtoAqduumYzEKyfybr6XYNCsQJKvntVWhRgYXuD4NtgVHRpBbC&X-Amz-Signature=a1cd1b07e893d9d6489fccd4125bbe7b8cc7480c9dff6a7e0406e1e0ccd6f0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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