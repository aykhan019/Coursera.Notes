

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=0db91e4c2a42713b12bff423687cf168a7d7cc48d8e1793e627d6c885e5b60d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=28043870cdbe3fbc12d8e19cd6fc311f2e0e1cc0f58400dcfbafd939c6d6ba8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=a6727088c9d2931ea33101da71f5c93daeacaa3b7e776bae30005d0ae85e2c7d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=f30172c881cbd0b2b3df7ec45ae880188c0c5565ed8345ec65e4efdd8b83f9a1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=aa4284832c4fcce1808511479c5180543839303e89532a5122581f8d5b84b3e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=e42e0a4767f341eb0e048e0d86a0bda5ada0b876f4073e8756b26a9fdb4c5040&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=876b7e1ba84df81b0ac3f9789cc3875b818419680b6466fce0ace4d1acb7cde9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=993419334cb2c1aa67b949c8c72bdf011e815ee2600cac5ec36dc2743bfb94ed&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=25b6e9711ac5416e884d570702c666ce63f623390f8ecc1700573cf807ed8d35&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7PVQK7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDvGR%2FmkARe3G%2BX0lCU49xvMRf0EdiyOCgpIorJ3cp5kAiEAuY8gUgSb%2BurVAUW0G7JUHLxrA%2FdS6DAyMU86mHI8Tnkq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHepQWNzvke6h%2BqreCrcAwsMYo3mZjF8bxrSr%2BI7W9zUo9oOsdvvMPPTA2lFMWwwB1uemuD9WEthc5J8K7eER8EfY7HpPXvYH4jxdNKTdOEBzzG%2F%2BY1wYATYh2vmrExZ2Hh4s4WgLX1c2oc1qv5iK%2Be%2FwNkq41FbsODp7i0g0et6kps6dBlJU2YZ8BAClsIdLPoF6nu6Gv2yxI5ZBev84%2BOTKqtByovjY0ifz22JfqY2cufqQvtzXol9zM7JukNKNJ4xdUZASswfk4TLMCc1aBRWbZhRkih0AoTlcAx0QR%2B5we2nMZVwyx%2BDRx4jrICNqYmx754BezNiy0jkZfeF7TIXboMQIu2kvnVWulkH%2BZcg8A08UeaBvLwgjwaWyRpPAxJ%2BIhkKYmb7bGiYv19IanXkeW0kf3qcLG%2Fhl1HxTkx8K3UixVQ0I%2BSn0CZ9dAYOYB0KPVcrZRdeRRmlEMokVoBh%2FJfIlbNXgE0Fu6NpOr4e1GZ69o%2BZyeNmcdgKpoxJLvFop9l4nRwFCiQBLdoo54eI5sk3ia9nq25p8UijtxDGbbrtnLjHf4xJJ6cyGs7X2Vtai0XLYiUxHZo%2FrhcWL6UvkpJaZ2OX1dvkXDW7IvtK%2F2lbWnMLmQO0qvYwv4xRnzce81UKKS0wYCipMNfmiL0GOqUBO7T8ssRqp%2BN97L6vUq0RpCPa1Wz6e24aMdfll7B0JQzuFOHLfFBAIOtqdUZE%2BgEY9Ki37J36E%2FIO89cVYZEWnrn7cmA9NY%2BccLIWF6X5HDcg0cCjNUgXN%2Bk%2BcahWFxnfMK8MshYUtm4e05JvY4Xj8ZfjVM8DvN1holACMW1CI7T3FEqz0H0sxSDYko2UYDDbzI%2BvgEC%2BCsNezSwPWt65Qn%2FeITxI&X-Amz-Signature=4b4a4463f21f215f85767a27a9426777b95ef4acf383722093ff83fd08b2843b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7PVQK7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDvGR%2FmkARe3G%2BX0lCU49xvMRf0EdiyOCgpIorJ3cp5kAiEAuY8gUgSb%2BurVAUW0G7JUHLxrA%2FdS6DAyMU86mHI8Tnkq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHepQWNzvke6h%2BqreCrcAwsMYo3mZjF8bxrSr%2BI7W9zUo9oOsdvvMPPTA2lFMWwwB1uemuD9WEthc5J8K7eER8EfY7HpPXvYH4jxdNKTdOEBzzG%2F%2BY1wYATYh2vmrExZ2Hh4s4WgLX1c2oc1qv5iK%2Be%2FwNkq41FbsODp7i0g0et6kps6dBlJU2YZ8BAClsIdLPoF6nu6Gv2yxI5ZBev84%2BOTKqtByovjY0ifz22JfqY2cufqQvtzXol9zM7JukNKNJ4xdUZASswfk4TLMCc1aBRWbZhRkih0AoTlcAx0QR%2B5we2nMZVwyx%2BDRx4jrICNqYmx754BezNiy0jkZfeF7TIXboMQIu2kvnVWulkH%2BZcg8A08UeaBvLwgjwaWyRpPAxJ%2BIhkKYmb7bGiYv19IanXkeW0kf3qcLG%2Fhl1HxTkx8K3UixVQ0I%2BSn0CZ9dAYOYB0KPVcrZRdeRRmlEMokVoBh%2FJfIlbNXgE0Fu6NpOr4e1GZ69o%2BZyeNmcdgKpoxJLvFop9l4nRwFCiQBLdoo54eI5sk3ia9nq25p8UijtxDGbbrtnLjHf4xJJ6cyGs7X2Vtai0XLYiUxHZo%2FrhcWL6UvkpJaZ2OX1dvkXDW7IvtK%2F2lbWnMLmQO0qvYwv4xRnzce81UKKS0wYCipMNfmiL0GOqUBO7T8ssRqp%2BN97L6vUq0RpCPa1Wz6e24aMdfll7B0JQzuFOHLfFBAIOtqdUZE%2BgEY9Ki37J36E%2FIO89cVYZEWnrn7cmA9NY%2BccLIWF6X5HDcg0cCjNUgXN%2Bk%2BcahWFxnfMK8MshYUtm4e05JvY4Xj8ZfjVM8DvN1holACMW1CI7T3FEqz0H0sxSDYko2UYDDbzI%2BvgEC%2BCsNezSwPWt65Qn%2FeITxI&X-Amz-Signature=8209479caac3156dc5febe0fee2b99933072df53f089e43d85ccae1c97f24c95&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7PVQK7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDvGR%2FmkARe3G%2BX0lCU49xvMRf0EdiyOCgpIorJ3cp5kAiEAuY8gUgSb%2BurVAUW0G7JUHLxrA%2FdS6DAyMU86mHI8Tnkq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHepQWNzvke6h%2BqreCrcAwsMYo3mZjF8bxrSr%2BI7W9zUo9oOsdvvMPPTA2lFMWwwB1uemuD9WEthc5J8K7eER8EfY7HpPXvYH4jxdNKTdOEBzzG%2F%2BY1wYATYh2vmrExZ2Hh4s4WgLX1c2oc1qv5iK%2Be%2FwNkq41FbsODp7i0g0et6kps6dBlJU2YZ8BAClsIdLPoF6nu6Gv2yxI5ZBev84%2BOTKqtByovjY0ifz22JfqY2cufqQvtzXol9zM7JukNKNJ4xdUZASswfk4TLMCc1aBRWbZhRkih0AoTlcAx0QR%2B5we2nMZVwyx%2BDRx4jrICNqYmx754BezNiy0jkZfeF7TIXboMQIu2kvnVWulkH%2BZcg8A08UeaBvLwgjwaWyRpPAxJ%2BIhkKYmb7bGiYv19IanXkeW0kf3qcLG%2Fhl1HxTkx8K3UixVQ0I%2BSn0CZ9dAYOYB0KPVcrZRdeRRmlEMokVoBh%2FJfIlbNXgE0Fu6NpOr4e1GZ69o%2BZyeNmcdgKpoxJLvFop9l4nRwFCiQBLdoo54eI5sk3ia9nq25p8UijtxDGbbrtnLjHf4xJJ6cyGs7X2Vtai0XLYiUxHZo%2FrhcWL6UvkpJaZ2OX1dvkXDW7IvtK%2F2lbWnMLmQO0qvYwv4xRnzce81UKKS0wYCipMNfmiL0GOqUBO7T8ssRqp%2BN97L6vUq0RpCPa1Wz6e24aMdfll7B0JQzuFOHLfFBAIOtqdUZE%2BgEY9Ki37J36E%2FIO89cVYZEWnrn7cmA9NY%2BccLIWF6X5HDcg0cCjNUgXN%2Bk%2BcahWFxnfMK8MshYUtm4e05JvY4Xj8ZfjVM8DvN1holACMW1CI7T3FEqz0H0sxSDYko2UYDDbzI%2BvgEC%2BCsNezSwPWt65Qn%2FeITxI&X-Amz-Signature=77cf7bca881edcee18c51ad0286a7c428f851fd4a9392e3798f28f0397f75a26&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=b305428462cdb7a935ec30f225de05386285f87369bb93562e8660943b2c191a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=aca7a0b6677a14c510f3b8c406b2d4a1e56aa526abdc2c79deddb91e59cfd46b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=1f888323607e67e53a7190dd8ee6242ba76de34607548eb8150f3a77664067ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=ded6dfdab6c602f6b719e925cb9050245fa7c019c23a2009826c0aacab344700&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=da32a9438536d439783a514e90bd6c5c4c4bdd6a041c334d5a9e7e04f644f134&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUQKFFPH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCSsemkYOV0IvF6%2BVjVnle7Ks7D9P41aNHJccDwmNmzwgIgWguUl4kL917rHemRf2Q2v55kRsi8CJ%2FHV5GY1Rm9CR4q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDKYAcvuL642%2B89hj7yrcA8LSLcRMdb0CRwXwDhjLd4EpW7JDDXWCJBcU8dq8POmo8cOdyH1uRyFuENB3edM76dLl1cZp41pKy3rfX9nQCyLyqj6%2BmXF2DovaMivVf4LnESjTJ7yneBrx3vs%2BZ2xJnGYvHQ5fwP0j%2BCqsLvRHZX8VkesPOIE9rwv9icfdtg4uNpVwws7ORCi56h66YJ5bYmY%2FDNfsUx1yokEVU9BFoDPwpsFlTvVxfQvYDUNB2RgR%2FL9y91qoOMHAL5%2Bg6FSPBMyteEYR20E8vCUY4FCYiufUeZzv8t1FdjnkeZ8arN5PdgDW24qMCuxnXq1hiFeW0Qf3keqhWvT%2FAVRG3S8Cek7i7HsGBZYtcREBmsxqexziLty%2B%2FMcksmniAaTCl%2FJjLoyG%2FnY1eggZ2uFk2aVrlysDL1P7ACYfDh2oEUJc6axD4qGBh4wmotRuqoyMxkhA7tjjfap5vr86xoq%2FHcrjeE74vPnM5vMVDRTt9mwEEaxQlBFk0R7P6HU%2Bp7YsSubZfl99BrQjbDbZr6MgBC8Kq5yds66rp6fW%2B6Yi3A8IGr5D3%2FT%2BC1%2BgZKGK75Uz52jhBhj74aaNk3%2FhRZmzcS19yY5iPBR%2BQ9pp7DU2k9194QJFiT1C3dONfwovFDPGMNbmiL0GOqUBcXfKuKyyOVwk7l6bxddrum%2FSpi4TkljapnABMrLyOhNTbWXMCM2nW0BFFL2zN3A4Qtoyx7PGHB75JqqwWvAFEkpnPz%2Fv3wgB1Nq4Xtiw4JJ10ZWXUNWc2W7nIb0HSkd26hGMrfAegKJGjhjRvnhNOCTEoqL017xJ%2FztHRZiiM1WLA17eW1ntN48IrYuMNxmUEG8JmnM6ZvsP%2BMWobHswFOcUU84s&X-Amz-Signature=2fec7cae777b6213992543ea1ec07c636f852e54697e172a9bcb3aef85c4d1d6&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZFBYT6T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFaTSmF8raG%2Ba2NCcUOQZn2%2Bwwi5vxWLEHIwPHaJ6zOQAiAP%2BQw1IixCnZWNyLQY%2FcJBgBtDqO9I%2BFADA8gq%2ByE%2BJSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMzyDF%2BuyCuFGxnxxgKtwDXXFkRUlJwkc0Iz2fmYx4lNy0qMx5JQVV%2BKzgwgCQzl2Wg5nXQUxnIDhO%2BNqTIbL3spq56uZYzUyVF8O9zLQaYGw1iLy%2FU4%2BqpLButGE91WkVrGiRDIgpXMh5AtlZNvE1Z4IhcfJzeLmMrF9%2BBUEGhmLObbLX9qGelCIWevCqyVCo4SxhYnUKvSGGQmPa02PXUq%2FFZ7TNLyz3eeLNcn6KAVS7BQCGLgcKIrgz8iFKi14DUygKNYZXe4cxWehxDvIY4p3vzxL5qj%2BqT5CeSFnxtJmscxFbw1ex%2Fi2IjQuJkmaWlpjVgSynlGJNiyTX3Huf7DhkPQVuqzgq8uVihMUVYnlo3prErmK07vBDnF58r9yjuDAdHytVEpjkEAhGbRo0CDJ8aC5ED%2Bxti4tVjNoepev9dh3iXGUJ7N%2FCqwwvfvJG5BtdAKG9BARFrwVCVcxwL4MtAvVO1B6WNP%2BL6X7nulvXy%2FBwzhktkCrASpw79YLFlRmQg2k6AckVKiHDDM%2BbzxjbAKAthq4wxqXeSeMzcC3dxscKWJjR1sr3Wn8C48cOK9idjqpJKP%2BUVZX4Fd%2BFH0rzHH2W1MmsMWOG9mL1JEvcBDMr%2F%2FUem34ve77K1fYKsTI4sRZDpF2hCH4w0OaIvQY6pgG5LXb0FAUDjJKN4WbtFPpgNXfKM1K1AXcR%2F7kWOwr25w2kuH%2F7LoGptf4nITUVnPJHel%2B1zoEVaQ7pBcNoy05OS10WetUHCL7%2Fl2uA628DVjVqMuYkUQHrhSVeFlQmxJKwe8jY5SMf61WVmSsmxTD%2F1I1Y0c%2BtBKsR0ZJGPzH7SGn%2FzrMSG%2Bnj5ZOnNxWZ6niw2k%2BwyPD5ypJM99BhWPT4lysw2BEH&X-Amz-Signature=dcba0fb127e63d80488ad5a4144e59db2bf845443fda6aac3b05168890bfb3d8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZFBYT6T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFaTSmF8raG%2Ba2NCcUOQZn2%2Bwwi5vxWLEHIwPHaJ6zOQAiAP%2BQw1IixCnZWNyLQY%2FcJBgBtDqO9I%2BFADA8gq%2ByE%2BJSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMzyDF%2BuyCuFGxnxxgKtwDXXFkRUlJwkc0Iz2fmYx4lNy0qMx5JQVV%2BKzgwgCQzl2Wg5nXQUxnIDhO%2BNqTIbL3spq56uZYzUyVF8O9zLQaYGw1iLy%2FU4%2BqpLButGE91WkVrGiRDIgpXMh5AtlZNvE1Z4IhcfJzeLmMrF9%2BBUEGhmLObbLX9qGelCIWevCqyVCo4SxhYnUKvSGGQmPa02PXUq%2FFZ7TNLyz3eeLNcn6KAVS7BQCGLgcKIrgz8iFKi14DUygKNYZXe4cxWehxDvIY4p3vzxL5qj%2BqT5CeSFnxtJmscxFbw1ex%2Fi2IjQuJkmaWlpjVgSynlGJNiyTX3Huf7DhkPQVuqzgq8uVihMUVYnlo3prErmK07vBDnF58r9yjuDAdHytVEpjkEAhGbRo0CDJ8aC5ED%2Bxti4tVjNoepev9dh3iXGUJ7N%2FCqwwvfvJG5BtdAKG9BARFrwVCVcxwL4MtAvVO1B6WNP%2BL6X7nulvXy%2FBwzhktkCrASpw79YLFlRmQg2k6AckVKiHDDM%2BbzxjbAKAthq4wxqXeSeMzcC3dxscKWJjR1sr3Wn8C48cOK9idjqpJKP%2BUVZX4Fd%2BFH0rzHH2W1MmsMWOG9mL1JEvcBDMr%2F%2FUem34ve77K1fYKsTI4sRZDpF2hCH4w0OaIvQY6pgG5LXb0FAUDjJKN4WbtFPpgNXfKM1K1AXcR%2F7kWOwr25w2kuH%2F7LoGptf4nITUVnPJHel%2B1zoEVaQ7pBcNoy05OS10WetUHCL7%2Fl2uA628DVjVqMuYkUQHrhSVeFlQmxJKwe8jY5SMf61WVmSsmxTD%2F1I1Y0c%2BtBKsR0ZJGPzH7SGn%2FzrMSG%2Bnj5ZOnNxWZ6niw2k%2BwyPD5ypJM99BhWPT4lysw2BEH&X-Amz-Signature=b66550d0d8a52a9e25d8d8d15ce174a418ccfba43bc37528a944161d56507bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWBLPHQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQC75jJLw21%2B4R3gEPQc4N9sA9e23yDWua8EpFBVqPlX8wIhAONS2BAThPBvgPmlRrNb3Mzeh4ROzzRFQrTM21m8wlu3Kv8DCDEQABoMNjM3NDIzMTgzODA1IgxX%2FhNIejuIqE5Ug6kq3APrJMgsJgbAkBHClGUKL7I4xyNj1FCAVCfWLyfXdmsFkBIYJqdFridCaHNxqFZ%2FodtZsMH8xReCU53ue9zpKKBlAiS8AAcBDyrdzuaqhrrg32mNPfVDLBq5Kvglxt%2BNTBIUZYai%2BUk84o20vBbQyWUSTK2XERNnXM5DKnKEymxvrCRpBYtPvCJidH8jEMMRvSqoKEDoyh7dpgM7PHW5DZBVN34OOH0NNDwpmQM5yYGCG9wff1VSD2pzGxFV%2FGhjwQvXhzqVTjuBOqYCDDtTtqPp%2BhRvxEG7w8IiPBIcR6c%2BO9dqj5EqcW3VkqOh8TKKgV4gOIPqwDW3uEd%2FcCnPzI3oSuQ3AKfS5QYl9HOd4vb6P8LtFmKehje1SUIS9Aal6tVm2eROVau1d%2BbJx7BLtFGMgfjMTAJOs39UzhNVv1QzNO0iSAP29ZQABdk4lL%2BaeXojZ0zPUGw4QjZwfL82pgDQ1db36ZMAQOmlMlV8lA2BrmFbL18d2d89%2FEr5H6kP8jLR%2FHO9UWaP4t9lKKnSkmwyXE6ZtVJhO%2BeIu5m0HA5kQVWhhUZHJjsTvV4W9ZKj3BJssvQKJWZ%2FBJrYv%2BqAh4rVaDUKDtGB5NCqgNY%2FPy5t1QdHd2UrNtzHKT9GHTCt6Ii9BjqkARpPwkr5q2AYScAkVv8ipjZCLB063j7I%2B5CLrMMTgwi2xnCyAQ0UNnTWDbUBPnNWj4YO2orQOZKr6K5nLgkPrppFl0vImGtUSKUO0buVxuQkM%2BbUEhMIz8bh0ZYqZfnK3YOMkjsocvS6sqa05aRq8E5BEqD%2BoF45S3KK9Dw6N%2B%2BAPUzeOiSFCNVS%2BeONsnm%2BFL3F3XdX70QYS7yfq%2FCd5Vjw%2FqAp&X-Amz-Signature=39288fe794d7da880976d9bc3974eb284ecf2ea2689e2d1a305778dfa5a8fe7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LYTOECL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDlj%2Fn2wOW4YclYc5Q9fzkYUubXEn9WRTR9vn2Jg%2FzZzwIgK1w456gmsK9PdZt8TTY%2Ft32y0rMqq%2BSOUgp%2F0Vtqf1Uq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDNSLRgo%2BFHUzemmQ4ircA%2BV6iZ2%2F9ppDoxf09331%2BMpMY0bOvMg93R4Av%2BH07KEIgLYb2u9tXOTEubCmIcrZcMGneYHpYdrDgP2Q7Fy4fozUagmZjZzC73AIxd08IY2EAhLrwUeXTSUeOXtgPnCZkobfsy2Nq5GRoPXpJdf8ZPg2nPL6m5HQPeuA31tnbR%2BUOgaIV%2F%2BSzpZmkJfrBzplBU4FFCWyf8XS%2Bhb0qtTZ28ht4ele%2B6R7ZeVEfwLXLGuN0N26Xft23tDpmL0zgWRSmvBXA8P9udevMTAbxDwas5feEu9MlB1LsQ1VZOpSa490jbSzuBgF0c6zKqyr3%2BlzANK7K8P2HFMeYBHuABFUtSpJzIB85xxIqaP04C%2FCBjPr0GC1sZ4DSzYI3JWDHeg5nf88btM9COtPQRstlLbheRq6gL4tcG2XZpzilsEHM%2BzLyKIpU5YRH0%2B65k09WzMAATvRo8u5x0fl69PGpAuMg6wpfkADBv%2F%2FsqU%2B1NOY2yRhRn1CoWCBxMuE%2FD1zTj7BI8g7roCeb3oawWTms4M2RQTxWMM4q3uCRALvN4qU4O32d01EGD6oAVH5cZT9c%2FEhEFA3%2BMZTOHqu0d2vcRLcYZl2XZskVzoGXgbSLM9k8Z7icghdKXLy1Jb4uzkEMM7miL0GOqUBuNhVw3kLFAsJSF4XdFQNF5tcoGdWZ8eDRQyJYl1xafQCIl%2FKam8QpPdWDiNZa3caJOVshrB2MmSol75i4ZSh7TpwEOj%2B5UGZbicgtrUdpp%2F14WEgk7mvVw8NoqMNwSruCQBd7alMIXahMx3Rk7Oq9YM4Ku540XEMwCUdaxUNL1cavyab180t55QdFMdqIMIpqN%2BpIxdvmJc8qIRA1OtLVDFqbHim&X-Amz-Signature=2391f2448c7e3bc6ea6268e7113459ac4ccaac3705f68664319341a1bcbc00d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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