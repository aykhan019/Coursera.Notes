

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=09e9866a33021df5982945b209a16110ee1a7b9d9c473b9e00cd5b20942c40dc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=7386b407318da649c2138c1ee5f4834a8b257b470d5747bc95daa4a3405e60d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=ba3419aa854a47cb10003123ba37aa64b052fd8e34c6f2e1567b3428b9c335da&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=9571cca73cac27aecc225da6cd924a27dbce459ba51e099ab8186f7083c1717b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=7c54f368d52fa08f851c0cf712d51296058bd689f87f4ff76ee86ec82d34f146&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=e089606edc7e3edc843c93f8188645c584a70950aff8a336000bc66a441c7fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=934234eacd65865bcf256fa4243fe0198b0cecfb79bf7076df761c1a1bb8136e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=d10631b5a21f8b65cc6b3041056e543b7052b03e1898a42a90118418df5bc873&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=7e0e383dc32f6b6d1d1a56dc62eb6033ca79601f5fa7556dad691007451c44b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYAWDIX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2Bs%2BK4DSojMLph8JgeCH9v70NRcQQVkt%2BIiRtSrWMnyAiEA%2Bq0RUowhbZ9OkqEsUqqn5TnE0rcyMP9pvqeuo6FWhP8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6KnK9DCQzmg95BNSrcA6QJEapORex7QCb2nqv4%2BIzjobj9gPFZB3F0SZuGRCRxzcsIsBHX%2BfExLNYzgXweUVT36OnNYzA73mwfPxAYNDhxq1HZdbpkTguDVmpFgdm3UTvBJw2VXHrGgk83BBP4dtImZFcCm8NgtMeY0pxUseVk2JT%2Fsd7u%2FTasBafjfMx%2BtaPXoUPhdtxrluzLK0fJRf178mfBLA4jDAsjWhE7q6B5fbIDOhXyiLbT9lMEkB0V0rBwY5aKAcpIwvgMQDbYaKuR%2FIYSPv8Yhm%2BHjDiHJYk8xG80roSpBiRvQa6g06BU%2F2roKzLZH9F%2FaZ1QtFBKkMKSZbfxsjE0PAfl3vB8gdgNXi0CG2LxE4GUCb4JyJXySJxTC51YkbBAfnp5m6szYq07Zz7Uy20AGGaR6OgKziTLhalQCMgeOed00Zj4aCI4vn1vrUXJqYPEQOiFpNkF2H4kma4sox5R%2BjBPShntltgAaw6HQbb5HkS0BoF13bgYNbB7x4bQRjkT%2BHrr0HCVii3eejj%2Bs2tmwFf6HNl9x2FTw%2FMrtRZztmNXddrWtkqXQU2a54DPuUSb%2FgWE3K15wqBzaNBadt%2Bz4kqmI1qw1hXDaIHjEG7MSu3TnnCX6nt0jJkarAebnCftvW9%2BMPrP8LwGOqUBVIP9e7JjTXGHFiubhkpgatbSFHqqNkGVsqM%2F7ZdWnCcGZzpc5xyQRkJgs1FbG%2FLEXXuM1hy7QbeQAPzdsJsIixTh7es5r%2FNxX7wAiXtIY46bQ%2BXWFE3LZk%2FuTkcuk7TxbKnZ1fU2Z3psnYodv6Lb%2FffiYWUSNhGsJtujwlmIM2rgdd4Vt82k44v8s4vPEwjxU1vc7SqddueV6kueAtLGC6%2FIYnja&X-Amz-Signature=e3acb662368454157324c110a0d91d4a75f53a3fbe18a80983410e0e3cfb57c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYAWDIX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2Bs%2BK4DSojMLph8JgeCH9v70NRcQQVkt%2BIiRtSrWMnyAiEA%2Bq0RUowhbZ9OkqEsUqqn5TnE0rcyMP9pvqeuo6FWhP8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6KnK9DCQzmg95BNSrcA6QJEapORex7QCb2nqv4%2BIzjobj9gPFZB3F0SZuGRCRxzcsIsBHX%2BfExLNYzgXweUVT36OnNYzA73mwfPxAYNDhxq1HZdbpkTguDVmpFgdm3UTvBJw2VXHrGgk83BBP4dtImZFcCm8NgtMeY0pxUseVk2JT%2Fsd7u%2FTasBafjfMx%2BtaPXoUPhdtxrluzLK0fJRf178mfBLA4jDAsjWhE7q6B5fbIDOhXyiLbT9lMEkB0V0rBwY5aKAcpIwvgMQDbYaKuR%2FIYSPv8Yhm%2BHjDiHJYk8xG80roSpBiRvQa6g06BU%2F2roKzLZH9F%2FaZ1QtFBKkMKSZbfxsjE0PAfl3vB8gdgNXi0CG2LxE4GUCb4JyJXySJxTC51YkbBAfnp5m6szYq07Zz7Uy20AGGaR6OgKziTLhalQCMgeOed00Zj4aCI4vn1vrUXJqYPEQOiFpNkF2H4kma4sox5R%2BjBPShntltgAaw6HQbb5HkS0BoF13bgYNbB7x4bQRjkT%2BHrr0HCVii3eejj%2Bs2tmwFf6HNl9x2FTw%2FMrtRZztmNXddrWtkqXQU2a54DPuUSb%2FgWE3K15wqBzaNBadt%2Bz4kqmI1qw1hXDaIHjEG7MSu3TnnCX6nt0jJkarAebnCftvW9%2BMPrP8LwGOqUBVIP9e7JjTXGHFiubhkpgatbSFHqqNkGVsqM%2F7ZdWnCcGZzpc5xyQRkJgs1FbG%2FLEXXuM1hy7QbeQAPzdsJsIixTh7es5r%2FNxX7wAiXtIY46bQ%2BXWFE3LZk%2FuTkcuk7TxbKnZ1fU2Z3psnYodv6Lb%2FffiYWUSNhGsJtujwlmIM2rgdd4Vt82k44v8s4vPEwjxU1vc7SqddueV6kueAtLGC6%2FIYnja&X-Amz-Signature=6b968363f46022f0f40385fea88d992cac3d45e77365fcea6d931dc9762c8be4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYAWDIX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2Bs%2BK4DSojMLph8JgeCH9v70NRcQQVkt%2BIiRtSrWMnyAiEA%2Bq0RUowhbZ9OkqEsUqqn5TnE0rcyMP9pvqeuo6FWhP8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6KnK9DCQzmg95BNSrcA6QJEapORex7QCb2nqv4%2BIzjobj9gPFZB3F0SZuGRCRxzcsIsBHX%2BfExLNYzgXweUVT36OnNYzA73mwfPxAYNDhxq1HZdbpkTguDVmpFgdm3UTvBJw2VXHrGgk83BBP4dtImZFcCm8NgtMeY0pxUseVk2JT%2Fsd7u%2FTasBafjfMx%2BtaPXoUPhdtxrluzLK0fJRf178mfBLA4jDAsjWhE7q6B5fbIDOhXyiLbT9lMEkB0V0rBwY5aKAcpIwvgMQDbYaKuR%2FIYSPv8Yhm%2BHjDiHJYk8xG80roSpBiRvQa6g06BU%2F2roKzLZH9F%2FaZ1QtFBKkMKSZbfxsjE0PAfl3vB8gdgNXi0CG2LxE4GUCb4JyJXySJxTC51YkbBAfnp5m6szYq07Zz7Uy20AGGaR6OgKziTLhalQCMgeOed00Zj4aCI4vn1vrUXJqYPEQOiFpNkF2H4kma4sox5R%2BjBPShntltgAaw6HQbb5HkS0BoF13bgYNbB7x4bQRjkT%2BHrr0HCVii3eejj%2Bs2tmwFf6HNl9x2FTw%2FMrtRZztmNXddrWtkqXQU2a54DPuUSb%2FgWE3K15wqBzaNBadt%2Bz4kqmI1qw1hXDaIHjEG7MSu3TnnCX6nt0jJkarAebnCftvW9%2BMPrP8LwGOqUBVIP9e7JjTXGHFiubhkpgatbSFHqqNkGVsqM%2F7ZdWnCcGZzpc5xyQRkJgs1FbG%2FLEXXuM1hy7QbeQAPzdsJsIixTh7es5r%2FNxX7wAiXtIY46bQ%2BXWFE3LZk%2FuTkcuk7TxbKnZ1fU2Z3psnYodv6Lb%2FffiYWUSNhGsJtujwlmIM2rgdd4Vt82k44v8s4vPEwjxU1vc7SqddueV6kueAtLGC6%2FIYnja&X-Amz-Signature=0028981c9471f5a12e4e0ad3800b74b445dd36dc52ed26afa066b389206ef8b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=4c256d0ba4823733bb0fb73701cece2df85a24e570f720ef85d2273f7e5e0756&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=321d2407247447f4d96dbf492d98ab6103862a819d0bdba35b2a95001f89bd07&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=a337b60d12165bb69985a92fa2ed8503e8eda87c99664e0cc58e8b3937f19765&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=432cb922bc3a8cb443684b35dcf9423124f5c8dff6a70c65a8f3dea866f8ed6e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=d13d4e9b59015bb8ffd74643fb9365c5c898d2afd2a436bd3c426a0d8123d252&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2C5XLJM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1BWzTwzxUccStC5%2FrpSKoHvx6Al7lNf2wFN7Zw17ogAiBguo65Lj8TgT4hXhhKh2M4nH9uOLz%2FPsm7VDH1xzYRuiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzDFT6XOqxzUMab1bKtwDxwnCDyXZZXmq403u4hegM5QdOpRFG%2FQd%2BeXd3v6YVkyI6RKDokQPYTlpy4virqeYLCAPBbahTNjrD%2BHYqL%2FW9LSuKxyuHQ1Z1cPqyGVS7iQfg54juqlSQsxnMmeHMTGJOpHCuEhiC5B1Cy5TwXQkSSC8fkxm8T9bsG3SZXIe1i8fBotzTwYDRGJ%2FuEucttUQQBZXkg74rIlVO9ZdzmIShxUfdcDx%2BHhgUbTVvoUyKgnjOmWmmaqfrVEYMmfbxGssQATRNs02LF6Z6utiCJzvPPBcknurQFRZRH%2FQnXADWlHUaZ4ZHIkHPl0p%2Bi1nCNdgUTp7%2FaD7jIOXeOAmuLKlXSLonmITez2YCMflQC7y8fcc68rtXa9pTKEalYbaVIbUD9yrfHom3hsrWhAWJawNwbAFjz3Uwn8fmz3ayIHJTpocpzY4Qs3rY6dvgp40wzSX5E4IWlLBpgm%2Bme%2BToTj3453ck5vig6i%2Fa11LCDcFJ%2FqBazDuQMil0a1%2BmQBJyeur8B4Bofwq3fFzJCXKTcTh%2FOYksylLqggiJYAFnWp4F%2BWTcHdLKxhwEymDER0ATbFYJZntFGx3cpgD4smvKF3MI9ztpv9QIN0XvmkKJy0khewZqIeY3f50Dl0XoqswuNHwvAY6pgH%2BnXuw151ibxOUxXzr98WsO%2BBgD8mlBnc9CK4U82NEV0lRMuZMcN7gqTGFn2u2xJCJmYU0U%2BEe3blcZoosRjhPUUzFlPkdg3wHkFtX%2BhF4Ny1P9zMNZR1mDObRJ%2FsPj98RurYl73qHx3VGiRodyoiHqxIvWG%2F8ehH1HR%2B5gGilf6sXtONxG6XpqepqBu96oRIXfH1eii2E6EnYImEclkA6Rbz%2F8JXV&X-Amz-Signature=09f290b039527c6300e00190b991372f8577762da85617cc41eb41c1d9379f5d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMF5IEEL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDubaQiMki2yZrvLag6NrT5jvm6VESB3OxtQU9WuZpeJQIhAKjWtGWeYgjdtxpkOsMV75VdKXp3nYVpjUYZlCXCuyE6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSjMJfm95KhU1EuTUq3ANGHHVUJKP1rvBqITPFkMFe5q5KshcajZrrcOQfWUCydNCsNpc7VeTDFBXched0OPRJnxejuPcPla6SwZkRBwXBPzHsWxlRfFamM7HVNGE18jazN8fOrVRY42n26TzvAO8ER6PPMYpDz3FwBXZ1Ox9sNCInMe%2Fn7KHV3rOYQPvn7Z8C%2BnVQjsZptQW9ybDILItP3fB8bhcJtD9r6eEfz6F4OoUQfjZrEx3IUrrXyh9ZTZVO0qQLw2zLgWAwcaXS4fKN4s%2F7SuvV8L5ZdHXvL53wmBXjMhtke%2BXGkuwKsHvZdXnCQFAE%2Bvassf54Br%2BcX2TMtPBsx7vRRE%2FquGZkuRAR0HUup5P6JQZRKME2Pska9bPpyEyLYBKpzYDzPAD4AZIM5czULSufn7fG9fTSBk%2FYr%2BKzftIl0K%2BTP4ZleKNiYR7oKJ7im1bW1CBMKXRd1eJ7S3rNpCfqvqWqMmofqHZiYMQIScE9oel27V%2BbM4rYGZ7%2F3rfCm3zXMCBEF4Zwb6cORQpl21WB51UvqM%2BtLyR6thHGzb8QfDLGMi02gFQrwL%2BaZaNwbGg6kmMA9Vl%2Bn92yQr%2BOMJTOCEZJfWPrswzBONWwDno7J442wA3wnvOfHTqB9W7P1GajJNKVozDV0PC8BjqkASJJpM39wXWWvc6HDo1BUu5cxZLYmaJKT3cfd81tFfQUap7YgmvE3oAXWEVmpeZY%2Fb6BRZQTp7Ty3WvYtLYxnFBIlnoA0SfXeIQWOgvdEjxFy2q2wKtvlcLmgLzTHc5M6HAHJG71YuYAPZImaSy%2B5e9i%2BTevxZ9uc8i1qhy4XTDeqiHGkPbG%2BF70cl7wgPAPjizzgWGlwCSjndzyMJNpjtzAq9ju&X-Amz-Signature=9a37e052ba29679cbffb1393600dae832e629b10279a1721e3ba19b465cb46e4&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMF5IEEL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDubaQiMki2yZrvLag6NrT5jvm6VESB3OxtQU9WuZpeJQIhAKjWtGWeYgjdtxpkOsMV75VdKXp3nYVpjUYZlCXCuyE6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSjMJfm95KhU1EuTUq3ANGHHVUJKP1rvBqITPFkMFe5q5KshcajZrrcOQfWUCydNCsNpc7VeTDFBXched0OPRJnxejuPcPla6SwZkRBwXBPzHsWxlRfFamM7HVNGE18jazN8fOrVRY42n26TzvAO8ER6PPMYpDz3FwBXZ1Ox9sNCInMe%2Fn7KHV3rOYQPvn7Z8C%2BnVQjsZptQW9ybDILItP3fB8bhcJtD9r6eEfz6F4OoUQfjZrEx3IUrrXyh9ZTZVO0qQLw2zLgWAwcaXS4fKN4s%2F7SuvV8L5ZdHXvL53wmBXjMhtke%2BXGkuwKsHvZdXnCQFAE%2Bvassf54Br%2BcX2TMtPBsx7vRRE%2FquGZkuRAR0HUup5P6JQZRKME2Pska9bPpyEyLYBKpzYDzPAD4AZIM5czULSufn7fG9fTSBk%2FYr%2BKzftIl0K%2BTP4ZleKNiYR7oKJ7im1bW1CBMKXRd1eJ7S3rNpCfqvqWqMmofqHZiYMQIScE9oel27V%2BbM4rYGZ7%2F3rfCm3zXMCBEF4Zwb6cORQpl21WB51UvqM%2BtLyR6thHGzb8QfDLGMi02gFQrwL%2BaZaNwbGg6kmMA9Vl%2Bn92yQr%2BOMJTOCEZJfWPrswzBONWwDno7J442wA3wnvOfHTqB9W7P1GajJNKVozDV0PC8BjqkASJJpM39wXWWvc6HDo1BUu5cxZLYmaJKT3cfd81tFfQUap7YgmvE3oAXWEVmpeZY%2Fb6BRZQTp7Ty3WvYtLYxnFBIlnoA0SfXeIQWOgvdEjxFy2q2wKtvlcLmgLzTHc5M6HAHJG71YuYAPZImaSy%2B5e9i%2BTevxZ9uc8i1qhy4XTDeqiHGkPbG%2BF70cl7wgPAPjizzgWGlwCSjndzyMJNpjtzAq9ju&X-Amz-Signature=f84189dc252cb58e072a11566b5424e5f805df19da3744e089fb1ae21feaf4b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYEPHO3P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHb6xMjSavylU3Oj1%2B8SXw3KWTxA8chZgl2Mgi8g5RIfAiEA4nmoZtzJtmNYp8KSaHIx7NWRCIdMjiRMR%2B92%2F0sqn34qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpsGz5fJzievyjH6CrcA%2BFQRr6dY4NGl4pCnBUlvbM7jsn53kyy2uNJM7usXp%2BYl%2BSjyIhB5ctjLXvo7ViT26XDFO5kLqYz7TiX%2FufhHBxstclp7dLywHh%2FftKm%2FDYE83vXxR4ODaRrGGT2b6EhV2MnBhniefZvwRcyFSHmBMKMfFy%2FbXcHE%2Fc9qyUW%2BtNhBff8c4mq4%2FK4huYhSw0nrXZ7osXwELrFnIwobq32dQpD4Ih0nAbbxNF9cRQABLnDL9%2B6BRzdJMpJaVLYIqvkUORKCDMonzgAvFdNE2vsS8YOEN6lZ87AmtuLSz8ZRh1FYVNc7lXj%2B9hEMCvt%2Bqq3DGLprQMqX62drkDwUo26WeTFwyGiccJL8Ox0GOAlJdMVEjuxWfJdfFCW0yH6GFUKVYxelH3SkR8kq%2FWJ40ux6gwwwIAiL3OmByTQ%2BxTCcBZkk5iwxIcvazdhhk6pZM%2FlEq5L4CixBGLJvReIpOAFnFhqXGK%2ButF4SqHxGykoGV%2FlVQgbURsjSAwOycXNZvbDnwS%2BYG7kLcbBr21ubuIdFwbirU%2FIEKtaI%2FimKZTZmRL2iYcJVw6u3Yoa6MnCKS60IrtGmHBYOI9MeXkjFGgHD%2Frf%2FmcKQcZthYIpscjqTz0RbSzcpO0q%2BKF2WqrLMJnQ8LwGOqUBawkFv2RJO%2B9jOv5sFmS1ztU2TKmdYQcnHJjv7x7%2Fl%2Fkx1Gvl2bUQ3NQCsfsRAzrlqMIKj53nuZYZWKd4zxsPifeelIyfdi%2F6cqOGTADWSwdPRwVSD8O%2Bz3Lw6csKfy8WieaPsekLFL2zd%2B7MrWLYqwVeR51%2BWxrl%2FQ%2BpLInck3FsXSE14AKzbsdDdDusAHS3wA2eaAhk1HdCbF%2Bv8v8wTCYQqwhd&X-Amz-Signature=56507a4e4d644c5c3d19beee128a274233f186cb502e1aed03229579980d43f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGEKYN2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhS6S57oCoiZY4cTTSOfAp4t6GiTfr1YvRFG8TcXWNCAiATYMOtqs4oRRR3XRZRAI8rtxgDwEOGm46ahHycTDrkiSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BFCNCUDkK3ExJ9QgKtwDuRE44t%2BzqvxJZGRF9869a0DTNokZ1vQVzHWOFRK2pFY%2BHu%2BZXyGINubarL4ilmjQC0tlQCRWnKwzeZsEn485F6eKIXBN2sQqaE%2BvSXwk%2BzvuB3d234IZeB%2BGn%2FhNA%2FCbH9K2h5NRGdQfei%2Fn5YKN%2FIXVaz%2F8FunRo0yFcrNY%2BfZZwwL6hgS9uaUVmOsPJNhU04tp1b572PbXtXtY42KdboN7%2Fk%2B9MD0tMB%2Bu7%2FicPsISUev9VOYC4OhIx3elxcZQ%2Ftk6hwxkeFMQyBgtSgfhWA%2FTOivkL5Zw40927eSYzqioxIHr7m%2FxSLJHEtZSdgAEZL7ULQsmQQsnxMakayoy2fePUIiV2Yq65Pkr7O6UIr0bOfV48%2B5JIMII50AwIMLHRsvGYin3GzDDJHbcoirMCFMbpUNnc1IzcI0tOkBFROpMchoQYr8F6y%2BkyyU6toQAQorsrxuhnbvx2ZOwlJi2PG4RU0ZdcgdEcv3gJgNdumHT3CPKQ9WipinQEY1OqEeXE7MzQhQub4hrp%2FxY33a0SvhNEgQtlee3%2BuMEdZQE4kf2pFuLx9HhSM43HUtcvClOBPDIDaiuhRZil9xYFE9A94QIf%2BbmfIri7qP2iS0W3Oko%2FO96pwlPc9R8browodDwvAY6pgF1G6t44lkp%2BISWQO7LUl8kgS2cCQ4fcDlbVNOgX8syCA3EE94kU67DauWO4eoJ3dYYML76WvvKgz2E9Tqazwr0Z9r4rjZiJGR1rdiBZm4b3U8xfHoFpx98BMX2HMJRFlSBWG2c09Ccy8rryyfViwCTfcUFdilcy3%2BdPD24%2BPZrNXXfXP%2F5LGNE8E66s9XkNIX6%2FErHDN8CJRHC8%2FaUiGKZjUb9sLfs&X-Amz-Signature=184b3afd7a16b464617e5265cb20582824bf3f76aa4d9291e6dc07debe5c136d&X-Amz-SignedHeaders=host&x-id=GetObject)
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