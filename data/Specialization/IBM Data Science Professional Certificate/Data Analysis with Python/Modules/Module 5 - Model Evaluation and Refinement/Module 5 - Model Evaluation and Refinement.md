

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=092a8a2e7a6ec567ce322bedcd745b17474dd6c4cd5abf394aeb6937bdcff4c1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=b936373ed209efcaff7d76b9b021fc414437817a0e3a87db32c0cbe3f3e2a388&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=01f2b42060b65159c753a89a839b05ad024ed1ed19a72dff4f8e8b29e556d770&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=c1686f90cdc0afc6380278d98f6f30a26c961f971e970cc4599ca0a70aa53153&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=bd3c9ef4a089c63cf8d18c9875db3815580b3d5a13a1649686d046bfe2c4d695&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=0234570ad4c8db562339041fb1b8cb80e7dc01d5c00cf72261d4155819a33201&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=062052c5143ace878303e4fbf1bd5367120f8871301cb0c7c67294d95950de8f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=7865bc9dc902fe6997f163a1c825e71714659fd63956fcd70e421d1e1a86d5b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=64c04eeec22829667af4fd9906c94ea0163a1cb1b3facba414dc66563d761193&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI3SR6YJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Dra1ZyMIQyq%2BRI1Q3b6FdGrXQWGTVjYXcFXQPWxb%2BgIhAP4F9g0TsW1H5SD6ekDukDWXoY%2Bi%2Bns7FsGJi0ogPkvsKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzG3s6jDKubsIjI9G4q3APlMVxZJCgQk9PkTiIGCrlIYDMppLl0vjAb1cB%2FuEmNVl0nfe3ZRRJIvN%2BUxVuWbXYmupLN2Y8AKVbLpo8QGXIWP1Kj%2FB%2BLh4Vp8QLmXlEpxGyzug7GlMqq%2Far%2F5d%2FUR5%2FzTi%2FKJ%2FDCTPiBfGrqW2UGNG2wHfItQjr7oPEVQsnnLX1yp%2FsccOt6u8K6%2FwqOE1u66k64P5j6%2FIIKFzbMvLQv%2BkillZj%2BsVuXp0hB0D56%2FNYXKDVe8NgTNKaH9pC0f91k1Ts1C%2FIQur7KmXap%2B3dur2YeF8vf%2F9J%2B85LtjMgwY8sQCMjS7we5JpbN4QyCDFy7dkVq28tTOgtjjP3ZntQna5QYQxQ1n0ZWWxN%2F06RsbY8%2F8wUplozsTE8s6HuqTP3gZTgZmPNKk9HsoMLd1cv9GrVxI8ako3HwUt0IlQAr3XpqbttD3mQqm6GZINBwWGO4J0Lf8pKyoCW1H3kVLc%2Fch7Yz6b%2FhaCg0%2B4q%2BGh0xoRgrm4HvFQB1Y6BIApy2HDahBGDkT77PWl3HnMVUw5thzA960xp49JGesn2ZHdOPcnjzNdch849Lb%2BZ6XnqFBl8RZA56%2BilOQkBneMRp%2Bc7WFQ%2FCDi6H4VWVbYv3JOm%2FTWP%2BeBllX7rsF0pJ5jDemvK8BjqkAYZeuJ3GHqpSTECUHjrRZ7wxAhaOaDgblx42MvjKEKnWtA1f6Mnwu%2BdoZW84zdijs6gXHqYb643p5s3A%2FtILCJQx7Yq0AZK8qllirsHlrqlayvZ18L1WYnX2GaRODv7LSSAXUF1QictCzJw3KaCoFeIJAezlPMeW2gRrKB3MV6TT3j4x17xcdH%2BfBY27bMEiADl13HWnZ6zO0QDpHWJayoR13nLk&X-Amz-Signature=83fd998cd28933cb94ff3a2bc972267ced55c26a8271f6dfa00f13058ebbee9c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI3SR6YJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Dra1ZyMIQyq%2BRI1Q3b6FdGrXQWGTVjYXcFXQPWxb%2BgIhAP4F9g0TsW1H5SD6ekDukDWXoY%2Bi%2Bns7FsGJi0ogPkvsKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzG3s6jDKubsIjI9G4q3APlMVxZJCgQk9PkTiIGCrlIYDMppLl0vjAb1cB%2FuEmNVl0nfe3ZRRJIvN%2BUxVuWbXYmupLN2Y8AKVbLpo8QGXIWP1Kj%2FB%2BLh4Vp8QLmXlEpxGyzug7GlMqq%2Far%2F5d%2FUR5%2FzTi%2FKJ%2FDCTPiBfGrqW2UGNG2wHfItQjr7oPEVQsnnLX1yp%2FsccOt6u8K6%2FwqOE1u66k64P5j6%2FIIKFzbMvLQv%2BkillZj%2BsVuXp0hB0D56%2FNYXKDVe8NgTNKaH9pC0f91k1Ts1C%2FIQur7KmXap%2B3dur2YeF8vf%2F9J%2B85LtjMgwY8sQCMjS7we5JpbN4QyCDFy7dkVq28tTOgtjjP3ZntQna5QYQxQ1n0ZWWxN%2F06RsbY8%2F8wUplozsTE8s6HuqTP3gZTgZmPNKk9HsoMLd1cv9GrVxI8ako3HwUt0IlQAr3XpqbttD3mQqm6GZINBwWGO4J0Lf8pKyoCW1H3kVLc%2Fch7Yz6b%2FhaCg0%2B4q%2BGh0xoRgrm4HvFQB1Y6BIApy2HDahBGDkT77PWl3HnMVUw5thzA960xp49JGesn2ZHdOPcnjzNdch849Lb%2BZ6XnqFBl8RZA56%2BilOQkBneMRp%2Bc7WFQ%2FCDi6H4VWVbYv3JOm%2FTWP%2BeBllX7rsF0pJ5jDemvK8BjqkAYZeuJ3GHqpSTECUHjrRZ7wxAhaOaDgblx42MvjKEKnWtA1f6Mnwu%2BdoZW84zdijs6gXHqYb643p5s3A%2FtILCJQx7Yq0AZK8qllirsHlrqlayvZ18L1WYnX2GaRODv7LSSAXUF1QictCzJw3KaCoFeIJAezlPMeW2gRrKB3MV6TT3j4x17xcdH%2BfBY27bMEiADl13HWnZ6zO0QDpHWJayoR13nLk&X-Amz-Signature=9c25abda254f8d91ccb7256441787560d25a634994358c4d5f3cb590842932e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI3SR6YJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Dra1ZyMIQyq%2BRI1Q3b6FdGrXQWGTVjYXcFXQPWxb%2BgIhAP4F9g0TsW1H5SD6ekDukDWXoY%2Bi%2Bns7FsGJi0ogPkvsKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzG3s6jDKubsIjI9G4q3APlMVxZJCgQk9PkTiIGCrlIYDMppLl0vjAb1cB%2FuEmNVl0nfe3ZRRJIvN%2BUxVuWbXYmupLN2Y8AKVbLpo8QGXIWP1Kj%2FB%2BLh4Vp8QLmXlEpxGyzug7GlMqq%2Far%2F5d%2FUR5%2FzTi%2FKJ%2FDCTPiBfGrqW2UGNG2wHfItQjr7oPEVQsnnLX1yp%2FsccOt6u8K6%2FwqOE1u66k64P5j6%2FIIKFzbMvLQv%2BkillZj%2BsVuXp0hB0D56%2FNYXKDVe8NgTNKaH9pC0f91k1Ts1C%2FIQur7KmXap%2B3dur2YeF8vf%2F9J%2B85LtjMgwY8sQCMjS7we5JpbN4QyCDFy7dkVq28tTOgtjjP3ZntQna5QYQxQ1n0ZWWxN%2F06RsbY8%2F8wUplozsTE8s6HuqTP3gZTgZmPNKk9HsoMLd1cv9GrVxI8ako3HwUt0IlQAr3XpqbttD3mQqm6GZINBwWGO4J0Lf8pKyoCW1H3kVLc%2Fch7Yz6b%2FhaCg0%2B4q%2BGh0xoRgrm4HvFQB1Y6BIApy2HDahBGDkT77PWl3HnMVUw5thzA960xp49JGesn2ZHdOPcnjzNdch849Lb%2BZ6XnqFBl8RZA56%2BilOQkBneMRp%2Bc7WFQ%2FCDi6H4VWVbYv3JOm%2FTWP%2BeBllX7rsF0pJ5jDemvK8BjqkAYZeuJ3GHqpSTECUHjrRZ7wxAhaOaDgblx42MvjKEKnWtA1f6Mnwu%2BdoZW84zdijs6gXHqYb643p5s3A%2FtILCJQx7Yq0AZK8qllirsHlrqlayvZ18L1WYnX2GaRODv7LSSAXUF1QictCzJw3KaCoFeIJAezlPMeW2gRrKB3MV6TT3j4x17xcdH%2BfBY27bMEiADl13HWnZ6zO0QDpHWJayoR13nLk&X-Amz-Signature=40b5d81340347b348d4662f80f4f36c84563d04fffc8d74b13de02e0f91ad119&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=8cd85ac3d2b0b34341000eec7caa0a3327aaeac8d4c72a90b5b2a7e15239319e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=d779ec965e7c659383ada9030a361ee3693e5cd83196831c847c4ced232d1dee&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=db0cb1042b4545d2d6729e10075fdb08b2847df609a30455673e2f67b5c5a0cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=88cb2829ca3493c73f260d8b2de2629de1621e9c3afd5f0866759b480505d56c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=e07b2cb3df7044d563b8ac02b365b23b1a35e72b4f55dba3ab4a60fa36135760&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXTFZN5N%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClT2kJtrZsspNiCKHeczGbm6yVTRz61%2BfO32La6aT%2F7gIhAP9h2v3jB8nQh5cCQK2Z1BLUdnITLc8oOzAcG0DIypkZKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWpUFkAA6a4i0c4IIq3APVEw3AYFdJ0uGux6zcsCbVlnr0hVQsGON2hCSeMA0pqD8UKvyEBhz%2FkIcVDi8FvLjcYuqmhxYwk7%2F2M3%2BtJlOq28ciaRWnwibHKkGSOlY4av%2BCGTWucwtrJaZX3OrEcdLTubIDm7EAHchR%2BAijZj3vj%2F0dyqIl7UCEq2txopOBW2BYZbBXreDt7oaNt91VJ7djCA0uGGjkrCC3vLH71rw2a8V3awf7ld%2B8dszB%2BQlNzCWnPMYC2u0kjYlt2vgti4Uct1z1FzcV8zW%2B3fKowHZ%2BPWkiUhepWzuv0Bveheo950FPw1ubwv5MiLHkALUUAH2AoI1veyF38Wu0MVt%2BN0a940PwwgCS9y0RylJw465ImzVvJleiGSQHWI5Y13zyh%2FqDMCNcx1mcHarAgO8GQ%2BP8sFiqgta9WKbS%2BLYTTU%2BAC20wtIYRGz6zliOLBVNL%2FK1TUGAa57gbOw%2BI%2BrqZ0sKsHhmQ48bccMf5Mm2yvKxW7vW3m5XaseG65LsvVcYtFdGb%2BjQ5ZY3J4O%2Flv3%2BZIDZy4e6f5c9ceBN7PVCqQ3kUJwaHvXxfm6O7eHyqmsHQHN%2B4NiG7iI3wNeLYlVDPTTDBKF7sfV4EK6NqYsx%2FCcV%2B3ZZWcPNswM5aa%2BuoPTDfnfK8BjqkAbfyD0StlCp530Hm9cbttpEoIfbrxyIutco6MPEuk7S46WvUV8Dv5cwpcwOXLK4WkHm5boPQzn99ute7xjuuqXrwdd2fMwyWpa20Hf9Os4L6%2FACT%2BOc4gqmtkwuqmxDZ3UGB3s1TiR3Jw6b9L1gV2T%2F%2FG7nnak4GTEDC069HgA0ob7sxZZ1MnFm39WT8FQ4x%2FXbwkP0tHQhNYuo0KLHOBH%2F5oc%2F%2B&X-Amz-Signature=95ef95e24360229095237b33e296971fb1d95cfc7971c4a82960a4558f7fc6fb&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOTR5QAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDyBgzeoTvia5pslH95UHfiIQt0Pba6GMAtIzITg9ixVAiBsNZgDL8Bs%2B9Q%2BYQZkCHwWEHpibn2Kd3RklhZvdBcT6CqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM69OcHUG7L8uxMhhhKtwDphLtN5lUj5nfTDKmpNT4SPRFNtzEOaWx%2FL8V6UDr9%2FhhI2pDNRb97JxRPMu7e5FuT3Xmm0BoIA4YaNGlCwNt5YuMerp%2Ffbc874FM4oBbjaywWbXa6ClYed8kSDW3wFKdOzReHVkE38AgqZcuyniddJpxE74lH2TnQjLaeUr3ITFjoytN7An6VJj2F2ZI78Kt9vsvVQlTBa8%2BsfFHPRHelZSJ8sXd%2Br5LLxZIUWW16Kl60rU7UsgoQoy3usrKCdOhzTyJppX6FbLF3TzcLn5isc3tfcUCITl3%2BDe6vs2xImps3cFaV3TKI1Z3QzNh4TboFKAIawVBNefQnSQh5Rgbg3gvpRzw%2BR3GWumhU3gI2vAMP5xPz8ZavK6p6eTGfi6BPSCWncOJBTwSNNMiM8aRfpp%2Fhi8SKthKgN%2FAtaUAPs8cjqy%2FcoMABhTwdZ%2FjC3YkV0SgWrLFg2bsPzTZf4n3j2AI4tTzUTE%2B5YpkGX8ukGh2p7vHKM7VRPM9kKsaD3Ht3WrNP5wrcs8XXln53qfOZOh9iQHW7B6GQwOCeqAHpDXhzYzyz%2BvSca4%2F3g7TNTTX%2BWrsnsQuAep9tpPk2bJSMpoC8%2BLqQDcH0ufnI4GS%2FzQmjELIRc6G58949vgwrZryvAY6pgGY5ag4trrsF65v4%2FBYa3WGVpAxTjdGp54sQ1zyrqB%2F2WnuTbiuBG6aXGtOsm7wn8E%2B6vE4FQ9iPMhc1OTNUt4n2pkZTKVneWu64bVWPTYhf8S%2Bu6s9P%2Fh7TGNKkuYx9GkhEBOea0suNbu1mUPjIjufMHiZwki1IAQr30dE6uYEaBY1rx4SUrhB4D%2FxRtc6k%2F1mXblrdwcE8S%2B8iG%2BYmT7291C2tt9L&X-Amz-Signature=a694921181e5b5966b965f6c24440a2872f1aa1b6d1c570fd9f3a9d578a8149c&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOTR5QAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDyBgzeoTvia5pslH95UHfiIQt0Pba6GMAtIzITg9ixVAiBsNZgDL8Bs%2B9Q%2BYQZkCHwWEHpibn2Kd3RklhZvdBcT6CqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM69OcHUG7L8uxMhhhKtwDphLtN5lUj5nfTDKmpNT4SPRFNtzEOaWx%2FL8V6UDr9%2FhhI2pDNRb97JxRPMu7e5FuT3Xmm0BoIA4YaNGlCwNt5YuMerp%2Ffbc874FM4oBbjaywWbXa6ClYed8kSDW3wFKdOzReHVkE38AgqZcuyniddJpxE74lH2TnQjLaeUr3ITFjoytN7An6VJj2F2ZI78Kt9vsvVQlTBa8%2BsfFHPRHelZSJ8sXd%2Br5LLxZIUWW16Kl60rU7UsgoQoy3usrKCdOhzTyJppX6FbLF3TzcLn5isc3tfcUCITl3%2BDe6vs2xImps3cFaV3TKI1Z3QzNh4TboFKAIawVBNefQnSQh5Rgbg3gvpRzw%2BR3GWumhU3gI2vAMP5xPz8ZavK6p6eTGfi6BPSCWncOJBTwSNNMiM8aRfpp%2Fhi8SKthKgN%2FAtaUAPs8cjqy%2FcoMABhTwdZ%2FjC3YkV0SgWrLFg2bsPzTZf4n3j2AI4tTzUTE%2B5YpkGX8ukGh2p7vHKM7VRPM9kKsaD3Ht3WrNP5wrcs8XXln53qfOZOh9iQHW7B6GQwOCeqAHpDXhzYzyz%2BvSca4%2F3g7TNTTX%2BWrsnsQuAep9tpPk2bJSMpoC8%2BLqQDcH0ufnI4GS%2FzQmjELIRc6G58949vgwrZryvAY6pgGY5ag4trrsF65v4%2FBYa3WGVpAxTjdGp54sQ1zyrqB%2F2WnuTbiuBG6aXGtOsm7wn8E%2B6vE4FQ9iPMhc1OTNUt4n2pkZTKVneWu64bVWPTYhf8S%2Bu6s9P%2Fh7TGNKkuYx9GkhEBOea0suNbu1mUPjIjufMHiZwki1IAQr30dE6uYEaBY1rx4SUrhB4D%2FxRtc6k%2F1mXblrdwcE8S%2B8iG%2BYmT7291C2tt9L&X-Amz-Signature=bcd4becaf240f05d604bfa4e59a029d469e45125f66f1e4a41ed9df7cda8bd8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJHBXFH6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBB4Vg5rksc6MJaflu4uhE%2B0OzNe2jWz7KeCk2l7Av8QAiEA51QzRvjvpuVHuiQ9zqJY8S1FbTQt4EzTlcvSgSbVyTIqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpJ5440DrMw91CI6ircA4%2FShBRcbIYQC8PfmBEz3X%2BtWEuB9eXF3cN0Zy1Lhgmrt1LcDlPpkOCrSrZtz6Xz5N%2B3VmHDDHwXvDuqPDcK5PfeGohb9BuN%2FkXujYVvrli%2BC%2FYJYPvZ5W16toZloyb0YXJ35JVxGOYRtpyAfHmHtoHeLEjHLciCFxCJ%2ByAAa6X7XTjC36riWaI6dFCVu%2FZiCxol5mLr%2F1rxDLFlfV0C8jDgebFp%2BS%2FlZl6jYYGSL8PTzm8WWXj5MqSf5MO1C8NRYK0aQFXD8bRobFhkF%2F0WeBOBYeS4Ow5lBDOqFvxo25aIzZFShdFVThUNwDKeLvpa4nsGV88LzoHPMR7Zv8WN5jY6ASM27ghRksq%2FuVVIZyo31ErUabAxBCerf9RqCv7EpfNqLc5vgZz3nPaWDWAEtN0JVW5ZzZ7fbnQgrPPqyt%2BS3e3wy6CGt3rZjXLo9KKrHymurtEFrmroQEHuObiNap8yvCTg06VQy9v15wXzal2n6zQK9uWhuh9geMZzfM16d73Kfl%2F%2BsBUIkQs7Vhxvu0lF08NpyFFpH4ZvYnHX4TVhUb54pUsm8dNjim5L%2FwGdkTvuapZjPAmCPgvyx4KyM31GyYzkW7rRXlKIaDiVj7UuK2NTUkrAmjG99diMMIOb8rwGOqUB87yzc5%2Fjvrk97hcJF5NQYjNiUEuLP%2FtgNyh62Z8EYl6x7n0U6BcZakpKW4LlwQrDUu6wUD6sMq6WE%2FvT590iYoarEIXgvleIRkBiBvCAH9jRAoBpC2NjOPhmIXlx6EreNKyKCtmNqM75grxJ%2BhQOTmN97QWgWlJiKAn6IVlBPuLl7fIQ64lsGt%2BynrtYpNqCKQx94qeRsECx7FCNmH9Gemx2enIV&X-Amz-Signature=3dbc5998f8af39c3f0ac2b7fe8503c186045a67502c9d039c5956699f50d0c4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWGIIKH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJXsUn5r9V8NoXZMDjXZwy0Wq5TOTzwYB%2BpEInTzw8NAiEA%2FeD0M%2F1B%2BH%2FZQCay5g8sUDAqqYKI%2B6JiJpP5o988QwMqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW2PXt2N%2FbRV372TircA%2FKl%2BrJcemJXWmWzZ0a31XEEakRA9dYTsnXVbRspLHqrLDsHsaqpSsUXK4C3li%2Fef5gYJhcvclyddV%2BulSTbg%2BkwaYhOb1YY%2FWsLbADWmOnS58fRnxc5haJxfd8ruPOaQU7qfFm9xh9Ms60VBWDgmA8h6%2FI8A88MfnsDklsXsiMUpifFQOC437LUuWWE08cmTTMFyt33cRLoBifFns6B0kb7JDxEDzpQJCudqV4dUXpuWmbBe%2BGWn7dPDi%2BqAzmawvmOZC1nTV4D7uUOd4%2FNrPpXywhaIMSymvtVnRlkPeEh5tHihv4r56RbXlhd3LlPVnMue1TKglqT68usF3FeeuSwIFQlZn15Cvb5Q5z9sVTgcD0KV7bfEEXBR1GiPjG3p3iX%2BMd5sypkFvYyGCTxZaGcXjGl0t56j%2FJF4xO8vYVb%2BQqozODi5gO%2BFfM5wMc%2F5jZjnITJwTObsKz6psxxoiAoIiACyXnYi5HKTUf1L0nOwPYeB5sC1RKKyzphMmqhAENYNXlw2C%2BWbSm2Rqjj9QbW7moHbbqSQ60HMEdl%2BKzy1LkjcEdRyQYxBAWJhcABkWsHalNQoeeyFNhyZwb3KX2Xhga67PgGTDASH5hiNzMD6%2FZy50uZqUExP%2B6mMJia8rwGOqUB1Wrq061qRJ34UIUuJcXjzBHePnVLyW8s8md5kqp6rWPVGU8RkohztrK1hGDSLzI2BABm9kefwlfDT9wvOpat%2FDPuFAli5bXqFw1e06PebFTvrHAe9Y6YozMiHuG2HnwO8nVrZPdNteNee6fzaVa3zPd23og9TKZvOSk5zrkRNsL%2FLQI%2FjhK5U%2FuwASl1oK37lDHKNpy8T00oWQ6mRZ2p4mLUiKO%2F&X-Amz-Signature=782bae499c68c159a9886833a932f854e7aebcd582d00de41ecabae131b6ad8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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