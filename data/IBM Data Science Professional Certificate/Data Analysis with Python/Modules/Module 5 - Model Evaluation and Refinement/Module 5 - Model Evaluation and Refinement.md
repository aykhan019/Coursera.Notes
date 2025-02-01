

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=720fb3887233de4875d2b88f715a088bcc811ab5b41fe8dacc87ea210a7a6064&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=c6bbcc199a1c42f1b7496d1dd5c08ae85a6754dbf65ee9ab5845112eb9dd1eaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=58e655b9b8b6a10b0fbad091875cc22b766c83bd602b48e41b7aab097832c561&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=0207c2713fc50265b323aafc12db0de915bf72ed8f1ac4fd21eb44032e2cedc6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=11f63c102886d727837842f5d335ddc418b312f9888f126ae7032382f747216f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=8e216b82611194f393eae0480723466b2d4d42a68fc451a1fbcb7abafe7b4d74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=24e54dff1e044ae48b8e5e06e7f28de3bf4f2296c891f055ddf9b2cc77504bdf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=1681fdc7c177d665a57e8bf975706046431bcdcbedd42d65685721c7dc279db1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=74eb3dc7b0f9e95d8d9df51ae82cbd54fef443f8eae88e9964b848fb18726255&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H5SZ5BO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOy8bcPEPDE3jBhkVCzsfZm2PHZ3vttBnuKW%2BwLqRFqQIgCq363QIaCEyJBiqA4nJmyGHLOuwjZWnO0q7%2FiBf38CEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNC7f%2FMd4f4uVfq1OCrcA6kVE%2Fk00Zq71WNZCpb3SDGqNqXQ%2FXM%2B13m9slN7Ama4g8euWdXmMT4OfzLf6AOMjmG7vWIWGJ%2B46VYP30%2BbL37hSdQTFPhnK9qjLFQg%2FVCq4VxdkZi6Q0QECEZgPxY0J3LfthMy7Ur7rvGhc02iVwIrsMJfJgnehNVpbVVV2eqd5VriL7OqY4uE3Uk0hQ6Z8W%2B7dM8HouAx8lf%2FfI9IWYi3J5C5X%2FdrG3c1M0nXgVUVvqQZyeTZv6drxGzTGoPXhbut0F0s5a8lZslxNCrBfFMGY22BTW4rWDNaC5V1tAQl36lQNygEsNi53pXcubBe1coEr2wm7Q9yyWeVk2WRCoWis2WTqd0gS8Ca92H04FfVGdMOkSpazxBojySH8iJ8nid59hMbntNlxiUJVtSdcu4a%2FYip1iw4%2F1ZoQm0IvMBgxso0wW6StDBJOBahKFcgGygW%2FzFYfX8tP7PEzG0j3zSAmNhCBuHKJNfgfyYc8oTWC8xUybM9hGJPWqaRLDjVh3fQweXzJ4DxLCyXUkQKiTCa7eLr8PoYrlkxyYl9Emewi6OqUUaTpEh947m%2BPtUxwM9MZXSEh7OffkWa%2FCmp4qSxXFbPO9WwhnBrUw9GufPKFm2Y4kcen0PpqBdeMJPG%2BLwGOqUBLFa4t9mDXumpNbyi2XHZlXiQko3ip5%2B9uulNcRhNvQmdwzXWcukwTxwCbYe%2BJ28puEH%2BGV5tVnVoC82WETEHTc87DVNnVwO8LTZPC8hdPdhvRkm4qKRQg%2BAgMKDBE0s8uljUg%2BKeaSOD2%2FQKwN2YUVk2yxac%2Ff%2FkLS8s%2Fw3ngUQMCqXH3Kk%2Ba5rnrvkVdyj8fyHwCwdSFEoVnUMUDL58ZlI7ooac&X-Amz-Signature=f5572e364c6dc82309ed708d4d2d4f39477c54dba270f89ca985ee133de5478d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H5SZ5BO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOy8bcPEPDE3jBhkVCzsfZm2PHZ3vttBnuKW%2BwLqRFqQIgCq363QIaCEyJBiqA4nJmyGHLOuwjZWnO0q7%2FiBf38CEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNC7f%2FMd4f4uVfq1OCrcA6kVE%2Fk00Zq71WNZCpb3SDGqNqXQ%2FXM%2B13m9slN7Ama4g8euWdXmMT4OfzLf6AOMjmG7vWIWGJ%2B46VYP30%2BbL37hSdQTFPhnK9qjLFQg%2FVCq4VxdkZi6Q0QECEZgPxY0J3LfthMy7Ur7rvGhc02iVwIrsMJfJgnehNVpbVVV2eqd5VriL7OqY4uE3Uk0hQ6Z8W%2B7dM8HouAx8lf%2FfI9IWYi3J5C5X%2FdrG3c1M0nXgVUVvqQZyeTZv6drxGzTGoPXhbut0F0s5a8lZslxNCrBfFMGY22BTW4rWDNaC5V1tAQl36lQNygEsNi53pXcubBe1coEr2wm7Q9yyWeVk2WRCoWis2WTqd0gS8Ca92H04FfVGdMOkSpazxBojySH8iJ8nid59hMbntNlxiUJVtSdcu4a%2FYip1iw4%2F1ZoQm0IvMBgxso0wW6StDBJOBahKFcgGygW%2FzFYfX8tP7PEzG0j3zSAmNhCBuHKJNfgfyYc8oTWC8xUybM9hGJPWqaRLDjVh3fQweXzJ4DxLCyXUkQKiTCa7eLr8PoYrlkxyYl9Emewi6OqUUaTpEh947m%2BPtUxwM9MZXSEh7OffkWa%2FCmp4qSxXFbPO9WwhnBrUw9GufPKFm2Y4kcen0PpqBdeMJPG%2BLwGOqUBLFa4t9mDXumpNbyi2XHZlXiQko3ip5%2B9uulNcRhNvQmdwzXWcukwTxwCbYe%2BJ28puEH%2BGV5tVnVoC82WETEHTc87DVNnVwO8LTZPC8hdPdhvRkm4qKRQg%2BAgMKDBE0s8uljUg%2BKeaSOD2%2FQKwN2YUVk2yxac%2Ff%2FkLS8s%2Fw3ngUQMCqXH3Kk%2Ba5rnrvkVdyj8fyHwCwdSFEoVnUMUDL58ZlI7ooac&X-Amz-Signature=05600f990fab41a0171d8d6ffb1bc7d98c496ffdabc8ad006ddf97bbc5514a60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H5SZ5BO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOy8bcPEPDE3jBhkVCzsfZm2PHZ3vttBnuKW%2BwLqRFqQIgCq363QIaCEyJBiqA4nJmyGHLOuwjZWnO0q7%2FiBf38CEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNC7f%2FMd4f4uVfq1OCrcA6kVE%2Fk00Zq71WNZCpb3SDGqNqXQ%2FXM%2B13m9slN7Ama4g8euWdXmMT4OfzLf6AOMjmG7vWIWGJ%2B46VYP30%2BbL37hSdQTFPhnK9qjLFQg%2FVCq4VxdkZi6Q0QECEZgPxY0J3LfthMy7Ur7rvGhc02iVwIrsMJfJgnehNVpbVVV2eqd5VriL7OqY4uE3Uk0hQ6Z8W%2B7dM8HouAx8lf%2FfI9IWYi3J5C5X%2FdrG3c1M0nXgVUVvqQZyeTZv6drxGzTGoPXhbut0F0s5a8lZslxNCrBfFMGY22BTW4rWDNaC5V1tAQl36lQNygEsNi53pXcubBe1coEr2wm7Q9yyWeVk2WRCoWis2WTqd0gS8Ca92H04FfVGdMOkSpazxBojySH8iJ8nid59hMbntNlxiUJVtSdcu4a%2FYip1iw4%2F1ZoQm0IvMBgxso0wW6StDBJOBahKFcgGygW%2FzFYfX8tP7PEzG0j3zSAmNhCBuHKJNfgfyYc8oTWC8xUybM9hGJPWqaRLDjVh3fQweXzJ4DxLCyXUkQKiTCa7eLr8PoYrlkxyYl9Emewi6OqUUaTpEh947m%2BPtUxwM9MZXSEh7OffkWa%2FCmp4qSxXFbPO9WwhnBrUw9GufPKFm2Y4kcen0PpqBdeMJPG%2BLwGOqUBLFa4t9mDXumpNbyi2XHZlXiQko3ip5%2B9uulNcRhNvQmdwzXWcukwTxwCbYe%2BJ28puEH%2BGV5tVnVoC82WETEHTc87DVNnVwO8LTZPC8hdPdhvRkm4qKRQg%2BAgMKDBE0s8uljUg%2BKeaSOD2%2FQKwN2YUVk2yxac%2Ff%2FkLS8s%2Fw3ngUQMCqXH3Kk%2Ba5rnrvkVdyj8fyHwCwdSFEoVnUMUDL58ZlI7ooac&X-Amz-Signature=ed9d6cf96e78bf49d71833512adcb4cb4d794116bca73b1c61b877a8cd221025&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=2082b5df67640dc41699d18759758484d4fc9a50778e7967fe0ca92289c965f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=a2164a7606e424cadd896a545dd4574a534db9c5152269a38caf8320004346f8&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=aa0309d53c801e47b4bdeb08a0e622e92be940fa1dc9afba37d97129618762d2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=580619bdd2220e7c27e3bfc2799e24f1c43afa52897e747765fc65053524add4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=89193694caecba5416961c59d1099ab3ec09ed75a53ea28285b258db418fe271&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP7AYMQK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYUfMV6VBP6WtfySFBiuGD1Yzvs21GptytUzE2zLnjVAiAiO4brcNfJ6ND%2Bp%2FEjrL79P4J6rmtsifTgyyEnpUZaXSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQdja4%2F%2BBgLBBTWJrKtwDdrZM93N1M3S%2BjyjA9WWjO9jnUwVMs3xV0VhPXtT4VykrSkA6lUI5JyOsyIYH%2BtVCqF3WOvFVzvB%2BjO%2Br9FD%2FP5erZLAyx83hCSZI1kUKl16939xa2TEo4ggPIEJgYkoTS8l2OscAhQRFsElG3t7zYPmC4t7HzPE%2BjVSEfFYlOkvZ6fMvRd0cYLU5%2FsiWBApFutFxuv5lkA2TL%2FqmX8YvcHne4J2W4eKJyr%2BdvqKrTjx2fJjLn3xGCOldU6%2FN7dQjBysCs5CcnXsPvfmqRsGOiVguGpFTilnh%2Bzaz%2BH8GSZ0Fl%2BS7v9qh8xemoeKRYrfEiLFaWFvju2XRlY4P2wZ3f12uYCScLEvMstJgbTWvugydzkRSyfC0s4DI%2FMnKtp0iU1quBrjpW%2Bi7cVm8arCnJaaV1h88%2F44dG%2Bb0fzo%2Fi7tVX8J3E%2FQoYzD0N%2BkDNaOEkXpAxEUquLF%2BHsywWrXuSdzZMMNQXvX4uyi8d6tw%2FAUruCiHXui9UtyRKUxvVzFUbJFZMDKrsSiyr8XHnRCtMKJalTOArn9qt9n0ZsI8%2B4Uwc6A%2B%2BhwhSYtoQyhMZjbYq7JSmtHBZiUzNONDJ%2Fbi4lHh7Df%2FZjlaIsCwI57LjYsJ1ilo7t2vlIvkKVAwtsD4vAY6pgEP1YJCGEvya1327prGcmfEP1iGK6%2FTQKWegVdYV%2FfLcVcl655gg6e%2BAin6bH3YTdPrRBAglrivbzIXMNIoaC0XHOXt8FzWSa0d2B0bcn%2BY1ttI1KRK2Ldyaf0GSy9bXiwqFvw3hqq1crDqiBjSDE1LoPDNu6ab6z%2FHpXRpIGkiJnh5vnSxtBzVasMSlOQoKoLBIKUfZVp5djf5mJufigUktOXnXooX&X-Amz-Signature=d43340354208995b90398c3dce7f23da659a5cd4d0e39b8b2dfd6e7543055788&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPTMNBY4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs%2ByJN%2FAi6VmOboxL%2FbX78fR1nKi1HGrabQp%2BpFWjbFAIgENQ%2FSDkVm7YxwK6wspn0JQZwFgq8mxSL1NYtoMbvey0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOcfzkCTfslyjwUaSrcA5qDBQeHsN7mDPoMEZNnw3BgPS0sr7%2B3oWH2XaXeDpyu58Jn0LC%2FE2B0mlGuYFx7RcfLiwu5C%2F7fwKlF214E3NkRyxWNrgXSlLdviS7nD%2BUR%2FQZanbQufOsdboYjVzE%2F%2FXOpsVBUyOxbfRk1cZ07VRdIq9WvOnsfTCAHkkLnk9vNPlhq3mdFKEj0RTMXk6edZkQUlNvBLMw42NuKkz4%2FyRStsQQupghtIBA50RrkYFvFIY3i68z0sbRX6R3ZAuyzMAPoNa1hCxB59tnh3NmH2F5tAkcA8PJwmELGJPCV3%2BC4R765GXQMgQHn%2FA6LfY4bqUD%2FlhaXnLDEZ0Q0TDsWVPVfAZCl9ebFFlF8V9ZEWyafKXWuS1MnB5PiQCQfxr%2BmF64frdO8mBuWDrhRdd51RjBOliokgF9qFrhA564RygeB5%2BYdhdk13N0Iow6wrTK%2FxDsOCR%2FJeQji75vvWrS%2Fxylwn32r021kRdkPj9VD20Yuv1F87t3ZG2OQ78ZXbV8TFdhykvfmvNwE%2BTjZ3CA0bv%2Bbx2OP1Vq7qTBPM5UxyCMTo%2F9XG6E02tWTSBY6OBOHPqN4ZUb6IMHAVyQbuimxdutBzdh5TRyxJP%2FoS2cGujnPouCHQO7zflJsKCUhMI%2FH%2BLwGOqUB9uCREQ2HBNrJsyG948qNeu56FPy1Cq9ovmks0pM3EZu8CThyHsMDJtvi6rFKTP419nzFiAI9G8%2Bg5h%2FDkP8ntyEiQ6LzMQUYnLwfFQgWwUtZn%2BaQekkgFM7NtAJIqERtZ8zuDpeShduMhtlPm0CxRoXkvt7URsdPT88drfsIs%2BZlygZAzhOfwWRZQg8OQaHhR2iJErHpyS80TfwLD96Tq1NSl9Zp&X-Amz-Signature=0ff9ae0a14456014845838b694f8dfe787090d52d9ea41f878349db2f8ba6eac&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPTMNBY4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs%2ByJN%2FAi6VmOboxL%2FbX78fR1nKi1HGrabQp%2BpFWjbFAIgENQ%2FSDkVm7YxwK6wspn0JQZwFgq8mxSL1NYtoMbvey0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOcfzkCTfslyjwUaSrcA5qDBQeHsN7mDPoMEZNnw3BgPS0sr7%2B3oWH2XaXeDpyu58Jn0LC%2FE2B0mlGuYFx7RcfLiwu5C%2F7fwKlF214E3NkRyxWNrgXSlLdviS7nD%2BUR%2FQZanbQufOsdboYjVzE%2F%2FXOpsVBUyOxbfRk1cZ07VRdIq9WvOnsfTCAHkkLnk9vNPlhq3mdFKEj0RTMXk6edZkQUlNvBLMw42NuKkz4%2FyRStsQQupghtIBA50RrkYFvFIY3i68z0sbRX6R3ZAuyzMAPoNa1hCxB59tnh3NmH2F5tAkcA8PJwmELGJPCV3%2BC4R765GXQMgQHn%2FA6LfY4bqUD%2FlhaXnLDEZ0Q0TDsWVPVfAZCl9ebFFlF8V9ZEWyafKXWuS1MnB5PiQCQfxr%2BmF64frdO8mBuWDrhRdd51RjBOliokgF9qFrhA564RygeB5%2BYdhdk13N0Iow6wrTK%2FxDsOCR%2FJeQji75vvWrS%2Fxylwn32r021kRdkPj9VD20Yuv1F87t3ZG2OQ78ZXbV8TFdhykvfmvNwE%2BTjZ3CA0bv%2Bbx2OP1Vq7qTBPM5UxyCMTo%2F9XG6E02tWTSBY6OBOHPqN4ZUb6IMHAVyQbuimxdutBzdh5TRyxJP%2FoS2cGujnPouCHQO7zflJsKCUhMI%2FH%2BLwGOqUB9uCREQ2HBNrJsyG948qNeu56FPy1Cq9ovmks0pM3EZu8CThyHsMDJtvi6rFKTP419nzFiAI9G8%2Bg5h%2FDkP8ntyEiQ6LzMQUYnLwfFQgWwUtZn%2BaQekkgFM7NtAJIqERtZ8zuDpeShduMhtlPm0CxRoXkvt7URsdPT88drfsIs%2BZlygZAzhOfwWRZQg8OQaHhR2iJErHpyS80TfwLD96Tq1NSl9Zp&X-Amz-Signature=4db80774fc7aaecffc096dc7c31b65a1d17a1a94e40a9c4beb45d1f1780a2d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3PLDAV6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8Rb0UzmkUFD4FOBHf3fbgDixYJN5iDWX4YJAY1%2FXM9wIhAL%2FS59wb2JJHnUMrSwpzUXYDmSUcJGGeYeCrCpjhD3aLKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2%2F6oDoGWPcTtu38Mq3AO0U%2Bh%2Bylwu2vyoLJsw0lyydOodUQtksIfYDiUiAJVKVOloty0tzC32H3Yh%2BmA%2Bao%2F18JM1BE8OjGWJgd0p0ETfCVWB%2BUmTJTIDrvlgJNy3ylvtYnxn1NO%2FPw8SBT13%2F2L8eJD0QPbF%2BlqFHyvrfSqEQk9VvkPAOMKYEwEp0Lvx8ssu%2BqYy91E%2FncUtef8oYTjiH5K%2FUtKXRwTFds8Llg93%2Fu7rD7ogP0cjWSfBMnm5QKDzllyI2hu6%2Fl57y5HoUrvZnRz3pgFwrA04x4MZAjjxHxWGm2Oa%2Bg7H0Ne5WxY7DprqSDLGVdsh2HPDi5CjE%2BlET%2B03K4UEOaugwRtdbcbAhPeJGu7O0y%2FCLB%2B4StszAvz8l31uMoFEZdHkFvx%2Bl3vSbQuOR4VsQwfZo5f8YCrtgt52iZbB4rOfkRJ0DjQRgIqoCiFz40OOe%2BtmM7E9rnA9EcISueBv%2FJs3tMict%2B%2BjAR9vsbVqrWLom9a8aNBwfhUElMjlUiJyg839TEyZmZ8xL4jeXqmjtqVWXaY1CfMdWvXjgZZPvlun%2BZ%2FNpjX0GxEEW0%2Bpm9smkduoiX51rXQNqxkM2FpJiOGD1mfPDq41HapRcJNw8lGsVdqleqJRN7fTkJkmcvlOOxuACDC2wPi8BjqkAY5diQK6E%2B8l3zLZMfCU1B7NHYvMh9omYQzJIrDQeIIW05Gx7Ri0Tu8m8XASZhuaMcfRH%2F4xC4zPZCTJwRG4HbuijnkDQGoTryiJofoomnr9F4GHQ5gFudeihRkv3C39ndYnp3tSLO%2Fy%2BCwhf3YYeLkhpqCyDT1F3wmxK78B4TsE9okfcnJmYu3VNivABOgfcAoy4sd2Yl5WP1nyVapQpCJqO0XR&X-Amz-Signature=777a4b5719110147eacc484b9547f31ae909a6cd8999c2393940cff31215a35b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BPR5RT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvPf7XHJiEN%2B5iJvHaENuyBI%2FJ8ogmgxDYagjki%2FL9vQIgJo%2FcRGh%2BLhRSQrl%2BMydYWHS8KXIi6KBVitQnubSgTRAqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXKpOUCD6FE7qswLircA4wD%2BxNwagwLe5ZoPoKPxsywBCjGw248NSa5dY%2BEXG2h1TaIASBGbJBsmO7U88%2BLWm8FvCJrsUhHXe2OEz9VHYxJF0R66Zf8sDA1CFr4A0h0zEvnGFQigbMzBiBmuL7q8rcczMV2sPeb19PQCpgDJ7lAgMCCkEr1junii596TVwlSdkxkXPIUDmNFk%2F7Iojbx%2BMERfNfgXra2McfWK%2Fd8TJofLtNBXXm3dj900Q%2B0SqfmUexX3%2FVwPNyUAYfHNCS%2FWxZyFuTJGPMtE%2FF6T0jSr2MvDmgNZptRN92ewls3p7m4y6sO%2FrjoXNJH%2FVZ7mNVPEJiZpohtj8iuyRT2LHXODJN7y0%2FMYWs3EPhmAPT1Mb%2BfOC35oWBXBeZRO4itLM4Zm6FDzg%2FJkNCPN0vXpctLdkRyX%2Ba17cgwME66tX%2B%2BYqnda37TzIXPtvBaPg%2FQLJxgQlR%2FbQOeir6KfS728ekXhQ1LjRVVRtLZ3MO5I9ou5YyGWrPi6%2BDACykjtiLLUSo%2FRpZ4AkILztlJ%2BCkSJ4TJ3%2FZHN7kbkzCCmAgCOKpU%2Ffg3XQuG5KtXj6DCuI9M1s%2BxO4uvnw5trAVFuI9G4vefSm54wkmI6AMp%2FxtoRDJweMU3YHK5si35dzjA7H3ML%2B9%2BLwGOqUBUFTZ1D4WwORPDj9wGYF%2BNOiz5Kq3g6vraJ0Dp4YLCuJulXNOueKD1pEAjsbLLEgTfuKN6wCEh6GfRSFSvKKZZxthlz%2Fluy0XE3EIE7IWXp7Rf4LnFOyqOwJVd6naK0EtIUa%2BVqMobUVGW8s4W6tfK5N%2FNl7H14FsU7WKCRkje41%2FHPSMYqr%2B532iY2lrRFTFYDjqWSSP7dUNkWbkr4G7t%2F%2F3J1X5&X-Amz-Signature=1c6504472b6d886b7b7ad41dbc127af46c19741e2363322694f5513aad20e1c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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