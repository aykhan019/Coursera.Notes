

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=f2e11f9154d2db402cb48fbdd1080b5394774ddb280a24481134ce54dec0d063&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=74141e9d121aad4f3269b8d4aa48389a8628f040e09f96108ae64be91eb25510&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=997366714e88363bf740a3aeab9da71036b0b2268f512ddda33f1e5821313fe1&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=0cd96b7a82fcf425c65bdc1cdaf0e41c3471a2e12605448d2c4ef882a28bcde7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=7dce9382f831ee403b7b9d56408bbe732372ae8648a5d3a464eb9226c1a75f46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=5d7b41b50b3de21dc2f6ae502b889cac0dbc3fcfa7d122f3f58dd59873c059e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=ebeca028fe4b238297bfcda63fc14b2a3aa45956717450789afe6682a6668394&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=3a984d900d30c6b8e146e734dab1f4e8ac195e484198a7cc0617a06d2a1b5403&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=8c7364a7d2f7670cac0697810d943a78c94bc1a2ecdeb62f6c137a525fc374c5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XG4RJJD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHFYYB8Yyw%2F%2B4SQCVar%2FHt9L0KDFXrhCSIwl0EuXHFXAiA4pqD6kja2fjqPAIgy3ceFyNTAkhWpZxlKiF76lND4FiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGdv%2BsHD9sg4TXrpdKtwDCgfkeALpR9bZnhx8wSuVIeZ0OObqOWpfUompaMcj1iqOFMOevstoUj5XfHiuRi1gHpczEwbLzP6FQ3aCPHDoByIbuASnw%2Fp0SPvShcQYCM9HWz0tV2ckYrh67raHaVz%2BYVWEcKmnNmc6Q7JTNZjnqC8MNK0BYqF7XlBMaDWdZXlJXtqXAhL45ccr0dbhP42%2ByHqjtx10JjdGWcbkxrjnd3PjoeWH7LSrBLoSxLFqD6pt5jJy7zKymLYPsdsmRIhKxQAKoZ%2FRvuCbFJoP9K9p%2FRzNrGfEVKGsWGWjAT7EUGSX50KOe%2FvLTf8dhT0e2zrOm1JNtcEDGGTTmMgIGPhHPYgAL5U3W8B4btoC8c7M%2BnhixacxtABH%2B%2FTNwc3SKlusQCIXpm0%2B4MTqzKU6LwAVWKgf9gDIlJuEsQJEybDbZAFtMaQqBAcmMKNXtNyQYC6pGLisdXkOf7J3Uq9g6QzdT2nBDwVdUAEIpZs%2F84slM7EqmUvz%2BSX8IqRFYL5egFU%2FoziNBegs7FPOYPTy%2BnzToZQUO2Fve2tbGzHuVkrS4s3pb6qHMpJqJqAh%2BmrD6Gn%2Bb79JL6d1MWmlGOBf6m1oDw4PJWatVBuys%2BJjxnoDrCQ4v4VaY3D%2FdQbZx7Aw88z1vAY6pgGWeZprQVEQvBgLSFNFYMrx6K9JSLSWA7lG31dP7q%2F7mkjXgRZSKU02dZeJMmESIFM63POsBpch05X5k%2FE9nPfaAGsMHxkISRNFY4p3xYroUq6TZLiJVWdMC4YU9ylpjdQJfJmayJa9vuDuk%2BptdaiLyi%2FDZ8FP5nqxwm1scPcJmamiLv8RuxpEMP%2BH9GnDDe04ljCDlTtAISD%2FiJj%2FrSHNxN19dhiS&X-Amz-Signature=59601c3fbe7483c2265a82b769d16341fcc52abc8a80fb9a65033de0ae42cdc2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XG4RJJD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHFYYB8Yyw%2F%2B4SQCVar%2FHt9L0KDFXrhCSIwl0EuXHFXAiA4pqD6kja2fjqPAIgy3ceFyNTAkhWpZxlKiF76lND4FiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGdv%2BsHD9sg4TXrpdKtwDCgfkeALpR9bZnhx8wSuVIeZ0OObqOWpfUompaMcj1iqOFMOevstoUj5XfHiuRi1gHpczEwbLzP6FQ3aCPHDoByIbuASnw%2Fp0SPvShcQYCM9HWz0tV2ckYrh67raHaVz%2BYVWEcKmnNmc6Q7JTNZjnqC8MNK0BYqF7XlBMaDWdZXlJXtqXAhL45ccr0dbhP42%2ByHqjtx10JjdGWcbkxrjnd3PjoeWH7LSrBLoSxLFqD6pt5jJy7zKymLYPsdsmRIhKxQAKoZ%2FRvuCbFJoP9K9p%2FRzNrGfEVKGsWGWjAT7EUGSX50KOe%2FvLTf8dhT0e2zrOm1JNtcEDGGTTmMgIGPhHPYgAL5U3W8B4btoC8c7M%2BnhixacxtABH%2B%2FTNwc3SKlusQCIXpm0%2B4MTqzKU6LwAVWKgf9gDIlJuEsQJEybDbZAFtMaQqBAcmMKNXtNyQYC6pGLisdXkOf7J3Uq9g6QzdT2nBDwVdUAEIpZs%2F84slM7EqmUvz%2BSX8IqRFYL5egFU%2FoziNBegs7FPOYPTy%2BnzToZQUO2Fve2tbGzHuVkrS4s3pb6qHMpJqJqAh%2BmrD6Gn%2Bb79JL6d1MWmlGOBf6m1oDw4PJWatVBuys%2BJjxnoDrCQ4v4VaY3D%2FdQbZx7Aw88z1vAY6pgGWeZprQVEQvBgLSFNFYMrx6K9JSLSWA7lG31dP7q%2F7mkjXgRZSKU02dZeJMmESIFM63POsBpch05X5k%2FE9nPfaAGsMHxkISRNFY4p3xYroUq6TZLiJVWdMC4YU9ylpjdQJfJmayJa9vuDuk%2BptdaiLyi%2FDZ8FP5nqxwm1scPcJmamiLv8RuxpEMP%2BH9GnDDe04ljCDlTtAISD%2FiJj%2FrSHNxN19dhiS&X-Amz-Signature=12ff899dbec9ddc21aa512c13a341544b1d6337dc4ea4512608ea5ec7628d273&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XG4RJJD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHFYYB8Yyw%2F%2B4SQCVar%2FHt9L0KDFXrhCSIwl0EuXHFXAiA4pqD6kja2fjqPAIgy3ceFyNTAkhWpZxlKiF76lND4FiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGdv%2BsHD9sg4TXrpdKtwDCgfkeALpR9bZnhx8wSuVIeZ0OObqOWpfUompaMcj1iqOFMOevstoUj5XfHiuRi1gHpczEwbLzP6FQ3aCPHDoByIbuASnw%2Fp0SPvShcQYCM9HWz0tV2ckYrh67raHaVz%2BYVWEcKmnNmc6Q7JTNZjnqC8MNK0BYqF7XlBMaDWdZXlJXtqXAhL45ccr0dbhP42%2ByHqjtx10JjdGWcbkxrjnd3PjoeWH7LSrBLoSxLFqD6pt5jJy7zKymLYPsdsmRIhKxQAKoZ%2FRvuCbFJoP9K9p%2FRzNrGfEVKGsWGWjAT7EUGSX50KOe%2FvLTf8dhT0e2zrOm1JNtcEDGGTTmMgIGPhHPYgAL5U3W8B4btoC8c7M%2BnhixacxtABH%2B%2FTNwc3SKlusQCIXpm0%2B4MTqzKU6LwAVWKgf9gDIlJuEsQJEybDbZAFtMaQqBAcmMKNXtNyQYC6pGLisdXkOf7J3Uq9g6QzdT2nBDwVdUAEIpZs%2F84slM7EqmUvz%2BSX8IqRFYL5egFU%2FoziNBegs7FPOYPTy%2BnzToZQUO2Fve2tbGzHuVkrS4s3pb6qHMpJqJqAh%2BmrD6Gn%2Bb79JL6d1MWmlGOBf6m1oDw4PJWatVBuys%2BJjxnoDrCQ4v4VaY3D%2FdQbZx7Aw88z1vAY6pgGWeZprQVEQvBgLSFNFYMrx6K9JSLSWA7lG31dP7q%2F7mkjXgRZSKU02dZeJMmESIFM63POsBpch05X5k%2FE9nPfaAGsMHxkISRNFY4p3xYroUq6TZLiJVWdMC4YU9ylpjdQJfJmayJa9vuDuk%2BptdaiLyi%2FDZ8FP5nqxwm1scPcJmamiLv8RuxpEMP%2BH9GnDDe04ljCDlTtAISD%2FiJj%2FrSHNxN19dhiS&X-Amz-Signature=4ee4d8ec04381c22ccdf045204f9b5441fcad43489e1833e1f35bf8ff637a49d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=61cb2cf8f6957bccaa97372ee460727b6546337a90bce9ce8decf698d177841e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=fd108ec83c11dc60a721e0abf0962d705855e7e1d4abdeba8addfe0ac0845a2e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=c75a7ce8952f6faa9ed534e5d2cb1dc01446f752a3add5c93d1ca48f9cd3b8ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=8f3b1021c6e853811b8d51a3708fa61f7b0a0a7fc049b731e888cda290c385bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=2960ee8af7520ad108c2f71373974283938bd7978a2b02d0fa5e894453841728&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQSIGTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuZkO8KIjytqmZFgaNxzy6G4R2nJd49Twp5tONhnxiVAiBuaRLJpQJKbaq34y%2F5Og2JO%2FIrsANh7Xim6IxuiEaAtCqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeHk9c2WlSOgXeSuhKtwDPIfN%2BeMLH871X8p6C740xg9xiDq51TfhKTtIjeX%2BrsqV8SO0Qj9cavFlSYam9ZM%2FEWQFRHN5WkH4KNigz9U70tX3hD8lHqcKzBx3Z0SwdW%2F58YPvbdjEz2g3flzhgfx%2Be2S1VCeQBTeisK5jWAxSk1Pm8VpFRyl2gIktHYpNmzRDPP9TKtz5fjjANKST%2BnTfR7CZrA8FKk%2FPJ5Rbo4gWnIfr81k5nvNl3gDIyYNaQxUdSvekomZjyGUDeSG5wgLxvoWpA6UTGxfGjfAn9MqB1mloXPH%2FyGaqRiw2bqgWatHieOxXasA%2FQ6XASQAGB3%2BRj4%2B6c%2B5sRMi0lCr63IpLehDcrovD%2Fn8mp9y0c9CiHv1x74tQHUyPSxbjhfZRGr8LqYllBUd3dTIdzX7ofV8HsWGeYX7dRP4lbe%2FdAHt%2FwJm5Y35FqHuXDE2XuJcbQ8%2FSKuXJb0xxf8yqhJLyGJID3pVwYeIGh7DMtXux9A9vZRkiJduuopDluwojIHk8zWlgFBqhmBJ2k6NhPCZl3hYmmbSU%2FXn3GnILz9Dt0Ecz9WWENpsAXKoNA3SCbdTCmVnsjVkiEnsDiR4gqCikdlgfmpx8%2Behd0wl0rfKVZQgOfZWG0lGtfmBXOEEHQg0wgc31vAY6pgGYwfoqZU9cJV%2BSu8Bk03HE5r9VP7gyqauG2addtfoQ5CTwPoW%2F9Ls3D9pIyUZ8PMVf%2BOPJE7fHUye2nSvm1b4FQDotSbzxac0M8drs8xO44pCWPtj2Ym34RXtQ7%2B%2F0gVnPEn3c4qJw4KTL1y4hCG2tu6AX89AK%2F94eMcG5hu%2FPxU5Yd6J5lalceXFBbRytiU9of9fu8apUiN2s47EW%2BjYAAf9mXXAa&X-Amz-Signature=557cd1debe84dc53f8d14643732ac8d0cf0c8433b246244f3d4eb568829da588&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHVZYH5W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCp74Q0UMFEBBXx3CyyZ1sSIHVPjDMQ1a4SZtSuu43DMQIgIXIl47%2BlxKOfoojY5pH6jCB7UxlVhZTuyObuVVLSoB8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlWqR9i8zQ225R0SyrcA5esPoTscNGiJomU6%2BV0FOjo3%2B7NkhIIbxcOs0dCN3%2Bhh9DzO3WN60qc56W%2Fj95FrRTw%2FYeACt3TmbUpzhrCuf3lSJxpjjdRC7ln937GDDBybSsKAXTAlum1%2FWlxWRtSvWO261dCL0AsPZ1phHtLdq6W%2BOow3ainAhxPHZMpaefwhmU4mn3Lg%2FHc9Z7Zh91QgIdDIy9KaolWI%2F0gHPJvrPcdFaCQCzB5jECxl8BerUVjT7zGIkfDFkbvKaHUWbsh0DkWPrRba2yR33Jg8kNlhaSlBQxiqgl86b4fWlrlw71sd%2FgYDEI%2B44uXxiTWZILNHQ5LKD08V%2FJWch2P9oCHiw8jQUJREe%2BuXoW5mLjLlARjLeD5gSWiE3n7WyNgjJdPyw6Uug%2BNwMnoUwwB%2FlkCcnnJuzVcyD5PYrt70C7QIY0NH6YzyAmlyu7%2Bu0HGRBf%2BkNkeNYNYdmSeHxAs7Ek4HCDUpQds8Bg9usH1dWOVMSNVh5wv6MkMKaL8XqhgA2tQMgrttsYc%2FHU8q6U3HqfSKWLr17gaPRDlFIBU0FTYH2i%2F9tmUDVaHaJQWBT%2Fx8TACQJCJeNkZMzu0zFgQ%2Fyev8gk%2FGHCn4EVNaEyGzwa4q0KStxt3hAnafs%2F8KzaIMNLM9bwGOqUBt0jh6UGOcieCVKGb01MhqiaD3klFhwLHvQYbNiFB3A%2FdM64kmat7IXAgrGsbWFuls9B3r7CoHa1VCUjt7szpISHa%2FULDwPinO3i7ndC3Z7f7zXrQb7Ebgp%2BTCCDE0nZE0rsglLSz7DHLuhcDHY%2Fg3zElGHQjHsulUGuNIXB7gSE%2FJWrLrlTzW1X8LOjlp%2B2hDnETcsZAuERCe4P%2F2mzTjCXnTmHn&X-Amz-Signature=4ec775f2ce29d6b42a588675e4e2e674db0bae1a7099f7f5334f6e637014546f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHVZYH5W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCp74Q0UMFEBBXx3CyyZ1sSIHVPjDMQ1a4SZtSuu43DMQIgIXIl47%2BlxKOfoojY5pH6jCB7UxlVhZTuyObuVVLSoB8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlWqR9i8zQ225R0SyrcA5esPoTscNGiJomU6%2BV0FOjo3%2B7NkhIIbxcOs0dCN3%2Bhh9DzO3WN60qc56W%2Fj95FrRTw%2FYeACt3TmbUpzhrCuf3lSJxpjjdRC7ln937GDDBybSsKAXTAlum1%2FWlxWRtSvWO261dCL0AsPZ1phHtLdq6W%2BOow3ainAhxPHZMpaefwhmU4mn3Lg%2FHc9Z7Zh91QgIdDIy9KaolWI%2F0gHPJvrPcdFaCQCzB5jECxl8BerUVjT7zGIkfDFkbvKaHUWbsh0DkWPrRba2yR33Jg8kNlhaSlBQxiqgl86b4fWlrlw71sd%2FgYDEI%2B44uXxiTWZILNHQ5LKD08V%2FJWch2P9oCHiw8jQUJREe%2BuXoW5mLjLlARjLeD5gSWiE3n7WyNgjJdPyw6Uug%2BNwMnoUwwB%2FlkCcnnJuzVcyD5PYrt70C7QIY0NH6YzyAmlyu7%2Bu0HGRBf%2BkNkeNYNYdmSeHxAs7Ek4HCDUpQds8Bg9usH1dWOVMSNVh5wv6MkMKaL8XqhgA2tQMgrttsYc%2FHU8q6U3HqfSKWLr17gaPRDlFIBU0FTYH2i%2F9tmUDVaHaJQWBT%2Fx8TACQJCJeNkZMzu0zFgQ%2Fyev8gk%2FGHCn4EVNaEyGzwa4q0KStxt3hAnafs%2F8KzaIMNLM9bwGOqUBt0jh6UGOcieCVKGb01MhqiaD3klFhwLHvQYbNiFB3A%2FdM64kmat7IXAgrGsbWFuls9B3r7CoHa1VCUjt7szpISHa%2FULDwPinO3i7ndC3Z7f7zXrQb7Ebgp%2BTCCDE0nZE0rsglLSz7DHLuhcDHY%2Fg3zElGHQjHsulUGuNIXB7gSE%2FJWrLrlTzW1X8LOjlp%2B2hDnETcsZAuERCe4P%2F2mzTjCXnTmHn&X-Amz-Signature=084a685126ae99af14592f9c2119c0bbf76378fa166a47f688c45c0e4d24dec7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3WH5GYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC7rzdA5uDOX1DMP%2BR7vdEWQQDxozjtmnaXcR3ugLMCyAiB0G8Ujp8qQVu%2BnYw3At5DnGgHzkkhkcC2cRddrrKQVfSqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwcz%2FmEuXdyzIUwGVKtwDP7NNV90RSN1V0jhXE3yuGvv2oiWy0RGFkSqxn%2BO2Uc8CcOx18GR07slL2ik9Euqp3oD8OVdiIrWm4ITalQJLCNk186U6DE3nvSauJtRzCPkybywijbDo7CcugdNEG9IvK1uRDbJISgDKIpjQwdCdDGl9o9hDxFmxypUMGTO83dggo0Ss2z0obJte2QfcAVY3Zq%2F9upCCShvhF0Wqcxi7uoFdNon94idcOAz%2BsGDsW2WgHz6BWhtaqgdd2CJYgaOgFdO2j2bmXpDUbnwl6oHnJU8rIRP%2BSlriaknn3wPL71BwuFWDHCytWwmLdpUCRKM%2FrMmnSqKn1vCvojB4umF6v6kiZDQkIxashPynHaG6bDtFehEcHON8cIr%2B2OJfPtELggpZd2sCRl1NPAziJPJ7LBp0xMufjk5Kf1NFrWlNar2MKwdXbKQ70OSCCiaMQq6K1l5QN9yzoOBWnZZra0n5iQiws4XgzwXsjKbBQanuOCbyHryWDplYbQhpb0meahm6VD6Sb7X6GlTEWI9CC3yxZzQZnvpwEaHTNXv6Kksq3%2Fkeiodal%2Bu9MNjSeM43fE8wv3Qgw2IyRsdlnIfMVJUlTQUcN%2BpN87uQ13R2pLEyI%2Fc4GpIVuPWayl9Z9Xww7cz1vAY6pgHKkBbXSemTKvHHMt%2B4S8fXCOVwLcSRVTuhpH%2B%2F6DPC0mbxUrfynmyxiIarRfqAPuqaB6FDYb6wZQddFE1Ca8iij3L22Xsbk0%2FrKNCP0gnmUDq4xh2rgl0uP%2FDgts1hp8y0qpxhmImPxPL2YeJ%2B66oQqikY8UorMVBlCt6imRPL0smbuxZ80kIAMPQiWlg9Oqri%2B3Xw6F%2B4ihtsL6izsoN8GIYeGppm&X-Amz-Signature=d60d7bb1b21c17142693e867d90a795fb2ba6ca65dde460504b0fb1612b034be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRUO5DE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd9GUW9%2FN2XL%2BRfB99IEZ7hVBIZMd43gBJ5hMHbgbKaQIgNczrxV1VY9AsEbqi5AaIfwlrJm1Plr2%2FcXwxbFe2cg8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzRKrBSKFgY9Hos6ircA6zxG4qIGBzsRy6H%2BN2kKr3PrSF0Fdi2awpnVRJw5vxqFVcmJWl4KYMy3E4YaAFNadqbStU3gGQAmee0o15fildr07r08byZB484R%2BwHSB%2BSF3BNvwT53WkGRlYI%2Bha80ThpZ3n0xayIPgkF2QLuG8HpxWlH8u4sXeUCIcsXYKWkDhNFBQvVHRieTjHn30Ps5MHYNRj7RM4oy7MZZfVTEayZWBVx4pupo3U1oWFjcLbeJP5JBRXWcG2EcVx9NXMXYPvmgskPSlELaKboHT1ghlNHoBy%2FR15adawIOpZ3FlNzli52gIyXD7nRg%2FxdAjByThnzhy5ij%2FingGpSOZWe4c6zbSL6dZOE5MICKjTwdefXJui0CMjM8odDiqmqNeXTRwaKyZ67TX1zts8fiKUyRYliPZnPhPNaVZisHeZOotuWDVWwpAypK%2FanHjQ%2BvCSg6zNc0pfi4i5PVMVMxcdRtjgne%2BPslwJ%2FlpTUlD9N5M74NN14OKC5%2Bk5WJkmfgN4hsaDUZzVLwGC9bZNDob2Bqf88HeMh9D%2Fl6bRM5B4gel%2FJUsosRp16qhQR7y6dldnwG8fz%2B%2FZcPxiRoydCo4nD%2FKCSldF95Eo7cHdLkobLV6zU34xTJtjfERPLbGvmMJDN9bwGOqUBzRElFAkYq8MLJTQALz87nY2t7X4%2BZlEtlTM%2BRK%2FnzNg0u3MXolU4D%2BiLDwOdrV5DEZQiFkrtQQJwDruDF%2FabwFoh3ulYvfDe1cKt%2B8sivQWhTemdzU92%2F2AUSj7UyHAoA2%2FbvW7mhsxEqsOPSlQX2QBKqiLzKxWjHKzpPiX%2BJJ8EKotbWjsiVpY5lZbngsQgfjRVNskvrLMAON9iOeyaCCENRcs%2B&X-Amz-Signature=8a0f15dc031f94b12b0a7cfcec09de81323439c72caa8ef0415d963109cc115a&X-Amz-SignedHeaders=host&x-id=GetObject)
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