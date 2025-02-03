

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=de4202574fad5503d87adda24ca80391a332048a2ea66fc9b2d6e62a81f399ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=99268362cacac0c89db7d2aabb246b7d38d0bfca46eae7f4947710baeb02eeb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=38178ab4c7d97cf086d7bf8c9995eb8023f260ba5f7ca86409cabaab2cc29e4f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=550a4112eb2458a21b47527d9ecd61f7d5117745a6863b755557da120e39a899&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=525dbacb5f06380536939cec5c8a9fd5ef00867962ed55557381b3f13d231550&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=9c82880976b4094ebf7ff3c71b0640eb6fd7576a28d9f3aaa62bf2bed0b9334f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=2b3bae53e768fd86381fc8ac44475410eedfef1fe0871ab1463cc2bbdec6097e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=e434966c87a464b04c21aeb6b1f7884019e4f935b3074ce4bead6b8eecb9d585&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=d8e9e54a011a4349f86e706db179f765516112dad8bb1a243bd80fcddee2ac02&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB3QQOKO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBhFzdYqR3zSgVuNNIoP3c33qQ3DiE9QAhHH9KVTqCzsAiBIug90nsy81YR1osE0zJVXOpo79keKwiYT4cIti4m5vyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMUYVQXo7MYa3R6yggKtwDocazFpR9GHraqvqC16TU%2Fg8GVwlSZt2a%2FNP67DSXjMZ43vkRwedGJvUfvy4Lkpyk%2BiF%2F3al%2BI22KqYe1E8EcgCb%2FAZW2Ug4vapRBzTI8o4zhc%2BkZIVKQA%2B%2BK7rZcp98gN%2FNXOUsSTnB%2Fh0zdsMa4BgDaatq5kEnpEkq0NkXgT7IWYdMOP%2B2HX7rDbCrG05Z%2Bdu%2BHpH5TDpzMdClbH%2BCO0vwx9SznkWRstbtLLrKBoOfP3X71tC6k8x0nfXbQj9dADijEYXgJPbGqzUf8HK9r8%2BxXST2MAmeX2%2B97QE8khm3NwSPzBP18SKClr5ja0ohTdWxC6ZdON2ErRxqlmcIoWFa%2B%2FdXXTcpvdbGz0xuYjT%2BIcShvNkygNrcqTM%2FM%2FVpDULV%2FYmQaXvf%2F2evI6br1923%2BQur4oy6%2BqUij5nYzvu%2BCuSq%2BZFnoo9mIbR3wlZnCwWN8entgPpQLdoDQ0EhpoE01d7RvGX2z1BhqF2dl2258fH%2Bqr32SM2MhTHIfdCmPSngBzRKOs3YtOxgdQmbqLWhw01tJxSgZMIslR3fuQ0HpOoDcsNce7Gys5ibEng5niID0MGOzDpFeGTr2HOPfLEx6bglLrgnYU28dzy1xYVbhVRUlPGjCVj4BiSAwy4OEvQY6pgFRbni04CbPBkiHNt7RVR4xUjzisjgJNUoypfwyO0pbDQYqdLuI5srU5JUL3%2FZKJYBbxXOrv7UkIcwUGxespx2ag%2B6pMRH7Nu6ckqCeZersugCVGUjaGpeteyqZj4XuHa1YbN9D0xr7zDPfjmPl8DaDV6EKDi2uRVhyAzi3EhEWEdcDVSrzOL9fDdG%2F05myR8RzV9RGYoN75iXAHYLMJbBvhy0dg0C2&X-Amz-Signature=e72dd73aca2acbeb4d8c0b4e31dafcd1c074bce9784d937a2be78d6c70f9ea15&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB3QQOKO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBhFzdYqR3zSgVuNNIoP3c33qQ3DiE9QAhHH9KVTqCzsAiBIug90nsy81YR1osE0zJVXOpo79keKwiYT4cIti4m5vyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMUYVQXo7MYa3R6yggKtwDocazFpR9GHraqvqC16TU%2Fg8GVwlSZt2a%2FNP67DSXjMZ43vkRwedGJvUfvy4Lkpyk%2BiF%2F3al%2BI22KqYe1E8EcgCb%2FAZW2Ug4vapRBzTI8o4zhc%2BkZIVKQA%2B%2BK7rZcp98gN%2FNXOUsSTnB%2Fh0zdsMa4BgDaatq5kEnpEkq0NkXgT7IWYdMOP%2B2HX7rDbCrG05Z%2Bdu%2BHpH5TDpzMdClbH%2BCO0vwx9SznkWRstbtLLrKBoOfP3X71tC6k8x0nfXbQj9dADijEYXgJPbGqzUf8HK9r8%2BxXST2MAmeX2%2B97QE8khm3NwSPzBP18SKClr5ja0ohTdWxC6ZdON2ErRxqlmcIoWFa%2B%2FdXXTcpvdbGz0xuYjT%2BIcShvNkygNrcqTM%2FM%2FVpDULV%2FYmQaXvf%2F2evI6br1923%2BQur4oy6%2BqUij5nYzvu%2BCuSq%2BZFnoo9mIbR3wlZnCwWN8entgPpQLdoDQ0EhpoE01d7RvGX2z1BhqF2dl2258fH%2Bqr32SM2MhTHIfdCmPSngBzRKOs3YtOxgdQmbqLWhw01tJxSgZMIslR3fuQ0HpOoDcsNce7Gys5ibEng5niID0MGOzDpFeGTr2HOPfLEx6bglLrgnYU28dzy1xYVbhVRUlPGjCVj4BiSAwy4OEvQY6pgFRbni04CbPBkiHNt7RVR4xUjzisjgJNUoypfwyO0pbDQYqdLuI5srU5JUL3%2FZKJYBbxXOrv7UkIcwUGxespx2ag%2B6pMRH7Nu6ckqCeZersugCVGUjaGpeteyqZj4XuHa1YbN9D0xr7zDPfjmPl8DaDV6EKDi2uRVhyAzi3EhEWEdcDVSrzOL9fDdG%2F05myR8RzV9RGYoN75iXAHYLMJbBvhy0dg0C2&X-Amz-Signature=c8bd6f50dd08324939cc432247c0a2842f5577296373387bdb709510abda570d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB3QQOKO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBhFzdYqR3zSgVuNNIoP3c33qQ3DiE9QAhHH9KVTqCzsAiBIug90nsy81YR1osE0zJVXOpo79keKwiYT4cIti4m5vyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMUYVQXo7MYa3R6yggKtwDocazFpR9GHraqvqC16TU%2Fg8GVwlSZt2a%2FNP67DSXjMZ43vkRwedGJvUfvy4Lkpyk%2BiF%2F3al%2BI22KqYe1E8EcgCb%2FAZW2Ug4vapRBzTI8o4zhc%2BkZIVKQA%2B%2BK7rZcp98gN%2FNXOUsSTnB%2Fh0zdsMa4BgDaatq5kEnpEkq0NkXgT7IWYdMOP%2B2HX7rDbCrG05Z%2Bdu%2BHpH5TDpzMdClbH%2BCO0vwx9SznkWRstbtLLrKBoOfP3X71tC6k8x0nfXbQj9dADijEYXgJPbGqzUf8HK9r8%2BxXST2MAmeX2%2B97QE8khm3NwSPzBP18SKClr5ja0ohTdWxC6ZdON2ErRxqlmcIoWFa%2B%2FdXXTcpvdbGz0xuYjT%2BIcShvNkygNrcqTM%2FM%2FVpDULV%2FYmQaXvf%2F2evI6br1923%2BQur4oy6%2BqUij5nYzvu%2BCuSq%2BZFnoo9mIbR3wlZnCwWN8entgPpQLdoDQ0EhpoE01d7RvGX2z1BhqF2dl2258fH%2Bqr32SM2MhTHIfdCmPSngBzRKOs3YtOxgdQmbqLWhw01tJxSgZMIslR3fuQ0HpOoDcsNce7Gys5ibEng5niID0MGOzDpFeGTr2HOPfLEx6bglLrgnYU28dzy1xYVbhVRUlPGjCVj4BiSAwy4OEvQY6pgFRbni04CbPBkiHNt7RVR4xUjzisjgJNUoypfwyO0pbDQYqdLuI5srU5JUL3%2FZKJYBbxXOrv7UkIcwUGxespx2ag%2B6pMRH7Nu6ckqCeZersugCVGUjaGpeteyqZj4XuHa1YbN9D0xr7zDPfjmPl8DaDV6EKDi2uRVhyAzi3EhEWEdcDVSrzOL9fDdG%2F05myR8RzV9RGYoN75iXAHYLMJbBvhy0dg0C2&X-Amz-Signature=77d3b853a97728139269a4a8ca8a62c7454f22e2c59b76ac0f298e1201c85527&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=5e229ec16b4b57879caaed0c26e0049b582c3d1fe49cc482d8ad26eb8da660c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=022f3ff68f3ff1473bec17201b5b89b84ccb043b1f13c814df2b69055473731d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=fae7cd08dd8120f4413154a5ea55420f44c9b2029833f9f662195da6659a51a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=70a5eb310b13d8209a8204bd5ab6c5c9a167229fd90790da32e146a72ee9fd1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=8571a63e8276518818853c87cca73902f32d37d6563d07c4664f652b627e156f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN6D7TVV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIAdC0fqk%2Fm5seRB3rW06oFLAeth3VxHJBrEfx%2Fuztb5YAiAIhre2A1VmsH%2F2dIEPTPFPsapuFCaC%2Bnm3Msjh85J7%2Bir%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMnS%2BnMu6I4BoLAqlXKtwDWlLubaWJK6TrQ%2FD%2FCg2qGL1XRTsEhCexVVtTUtOfBYJ7EXmiABSvmg3SfuCr%2BOCoWqIEp8eJo9lmSMnEBgANVsqJf1j9Z6AARzNXOKHZbEVg5e5bjweKqiHEB6S9AehuSbuRsNMPZp017X%2FkzowxnqEEPh%2Fgx9dL5h4sw814nECQWR%2Bgrxj%2BrME4ivcF2O5eqvdp8UMk9KnAsH8Wpj%2BOvWAiODOwoGBLV0Ood%2FuIEY8mL%2BpQmMu50FlAzc4035cmKW%2FGWo1aWaOyFK9zaGpxC5Ky%2BNCEO09hQ1lBokBjQyJ3Etf5lD2%2F7xQZNbvMbedHGsk6lYqjoC3B1%2BUOElD3Y9yt3FUKY5T%2BNlthT95UR3TQpRGQ1yTk4O%2BZubiEIuiIw3n7lSmq1VA8f6XD5n%2F6ZnpxX7Z4DC0sgRhgzyJeZkIUHdeBfn%2Bpj5vNoWDFXw8LI8fwa7YIN9zk57t5k54cvTwXG6vmJ9msZNveaaIL%2BWp655ySGPXw8%2Bs0%2Fwkjrv%2FWEXgEb0lMCC79aNPGfE96vBMZ4w2y7XaqYXzoBU2iD3iIX%2BUfjr5jlAO3y%2BVJcvl%2Bui5LCNUwLwdWCBaMKiqYZByXB1we79pT4JP3ze9dY1tOy8SrsptfAdPBVTowrIOEvQY6pgGrv%2B%2FllmyvCRhuQ2v3SOAR4%2FWWU4sNQ0FhAKpySzrjAH6RkbbMzpCaAOP0tvbPPs%2B9LmcMqEndItmg%2Blwq0vU686icmz8OV6Yh9LxL2pu%2FpLSsORqHwq%2BMNQkKgd6FTClt3OfDNGntnjxIUqdKgnUfNWCKC3JDy7QmBKSzhLK2NdjuO0jA6XxWm75Ko1JfN9m7DT715TeYg9fQ5ZDPRFfNT8fBZ%2FLK&X-Amz-Signature=6c55e33d8ef1a9b251a12d3e9e92576e3ee240b995861f1905fb68d197ab646e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6FFYBT3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCBX%2FrA0SJpTbRzlzT7498CMJbaiC05LcR8QR6AonRSKAIhAKwuNjrPjB0tmDhDz%2FhALMbhGA31GKQ7NR8dF4SywCLfKv8DCBsQABoMNjM3NDIzMTgzODA1IgzDC1WqImvulai%2F6Hgq3AONhz7Ap2Enn0xOvytMhW6prFUVQygmofdhJhUHSLZ7mTygKrEqQjQTuQpxm0nzCbfdR5e71%2FjuGHcX9GNVW40dm%2FYSL45MKawVCUnPW7heKGpe%2Bx2Y3ss%2BcsVn5yg47yZsnGYCtjTxeHWR%2FzFRw3Swunp4JBxZjmkbEGb3%2F9pW9%2BPSBKDWVgL5mXaDZMMxmE%2FlJVWLw8G9KNduWOU%2B46UTeq8xmnGGES3oC%2B%2F8HOP9oTb97Ehx2kVcOP3cgSO4dJj1gQl1Dsl0aJ7ecy3B10tJmHhYjuZ1fGLBcBB6wuPpmu1vlEX2sVn0cvcLz5FC9Ci%2BkAtcKVU0WRLFe1NW9Xdkb7ViSjWBcMC%2FxrPOBWXiP7Q3iV8a9%2BrzR4%2FwjNlivCfyoyK4BuzojRD2jYUB5RXsET2rO%2FlcZkJCoA96YULNQl5BWwcZCsvGs7lUv9lMk7QsdoI517HuaZ0Ck7t1kuL9u6BhYzTwHYTO%2BR4K2hHdulXlTqWQxmOin%2BA8KS1miWk%2FvJEZanM35oVAL2fz1bZAggVK%2FL2cZV7QHSbC4VGRFz9G1zuJCg2s1EJgkZmwvs1WXoF78%2Fxs%2FWz6uMa2Ko4rHpF5sna1LGBkq1Z02SOJB3yDEMHkMosBiJkqWzDdhIS9BjqkAZCRQFJbHRxt6nbZo5Xkhs%2BU2f6SpC%2BLtuNzIJ5htND%2Fozh8CqVNfhg9WS%2BlPiv6GtvPCA%2FuEEYIPNiZAabW3lqlugorbB7h6qHoNMuaoOhPy6GQlsnP8Yq318L0ar8DYiBzTGh%2F72Nw9FjoHDMAbaRuez%2Bm6Ddjwg1WthaimZ%2FTEXV6Wc7vvTwEllIRhWHqmBQvjYZvwAN1aimqLV1POByY0s%2BB&X-Amz-Signature=2fc4381265783fd46ffb009edccbe308db797e58fbf89a2763e96807d1387062&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6FFYBT3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCBX%2FrA0SJpTbRzlzT7498CMJbaiC05LcR8QR6AonRSKAIhAKwuNjrPjB0tmDhDz%2FhALMbhGA31GKQ7NR8dF4SywCLfKv8DCBsQABoMNjM3NDIzMTgzODA1IgzDC1WqImvulai%2F6Hgq3AONhz7Ap2Enn0xOvytMhW6prFUVQygmofdhJhUHSLZ7mTygKrEqQjQTuQpxm0nzCbfdR5e71%2FjuGHcX9GNVW40dm%2FYSL45MKawVCUnPW7heKGpe%2Bx2Y3ss%2BcsVn5yg47yZsnGYCtjTxeHWR%2FzFRw3Swunp4JBxZjmkbEGb3%2F9pW9%2BPSBKDWVgL5mXaDZMMxmE%2FlJVWLw8G9KNduWOU%2B46UTeq8xmnGGES3oC%2B%2F8HOP9oTb97Ehx2kVcOP3cgSO4dJj1gQl1Dsl0aJ7ecy3B10tJmHhYjuZ1fGLBcBB6wuPpmu1vlEX2sVn0cvcLz5FC9Ci%2BkAtcKVU0WRLFe1NW9Xdkb7ViSjWBcMC%2FxrPOBWXiP7Q3iV8a9%2BrzR4%2FwjNlivCfyoyK4BuzojRD2jYUB5RXsET2rO%2FlcZkJCoA96YULNQl5BWwcZCsvGs7lUv9lMk7QsdoI517HuaZ0Ck7t1kuL9u6BhYzTwHYTO%2BR4K2hHdulXlTqWQxmOin%2BA8KS1miWk%2FvJEZanM35oVAL2fz1bZAggVK%2FL2cZV7QHSbC4VGRFz9G1zuJCg2s1EJgkZmwvs1WXoF78%2Fxs%2FWz6uMa2Ko4rHpF5sna1LGBkq1Z02SOJB3yDEMHkMosBiJkqWzDdhIS9BjqkAZCRQFJbHRxt6nbZo5Xkhs%2BU2f6SpC%2BLtuNzIJ5htND%2Fozh8CqVNfhg9WS%2BlPiv6GtvPCA%2FuEEYIPNiZAabW3lqlugorbB7h6qHoNMuaoOhPy6GQlsnP8Yq318L0ar8DYiBzTGh%2F72Nw9FjoHDMAbaRuez%2Bm6Ddjwg1WthaimZ%2FTEXV6Wc7vvTwEllIRhWHqmBQvjYZvwAN1aimqLV1POByY0s%2BB&X-Amz-Signature=6379f70d8b8d2920881d09b988bcbaa680c28ef4d27f5dd7d9748ea810f33a94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZENPHKDM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHruJ30aYeWMiRubMeHyMHmx7XRGsCklniKFNJKj01d%2FAiAaAmWyWJX0xi%2BF9RbzmFX4GwzN0EIFmhqoHEgoV9rajir%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMF97rJmxylOIeZinaKtwDZbZ%2BKP3Nkd4lI9lUC7CFWLRFpo%2BERzudIs2hiP1jVNPKIS%2FSnAfLkoHtzv7Lt17IB0%2BvG%2FjcODE1972oQ7JT5HueFh3PLcbxu0NLYD0m8JLEHa8gtPGL0M1pucFhlRVb64lvu1ws8ICvMh3C0OkcTXvvVs2%2FtvPO7nEcD5ofCAdB6gJ2xvsi9kiea%2BHQbD97DqcfptcMRmVLxMs9%2BeAy8eRbTOn%2BEVJ2qgh5rxhwrwwlP9U%2FMqaImYgoL9nytqG2xxmXRUS2ycoJ2W54y%2F4fh6AD%2B3aABYivmVPZhZCMhZkvIR8NVcRbVRC%2BAM0xCumq2A0Xl%2BQH2qfGOne5XoTziuCCl4cVDHrNUKTLZMqm%2Byt01agQs3VZZzkcUlLv2eYzCNczk4MU%2FLeDGlpdrK0aZoce7%2BRzT63HuJYX%2B3ycgNaD7FPbxDtXMxGdZjnYzwu7Jb1%2B4%2BRcytcIDlS3fhr6uWBZbTD%2Fj7ghS89zvNn%2B4enz%2Bpza%2Bzgz3761mEW%2FGwBNV1Ni717bwR%2B5Az3GF%2B0mnaiVLqu28jQ0Gd6842BfAlZ7aWrqhMXmWb4ypd8nfweOMH6VvLjy6QQJDVavyDBxS1W9Fh0zHFWlJ06E1JLu0q6zrapAfcCwFxOLQmAw1oOEvQY6pgHudRr63w8v%2FNKvMm%2Bbbgyi%2B4fG3ux9oyOypRSSPX2Tn%2Fk%2FBAqHh1X42tPT37e9rcNUfagqIDNaEQwKNDOt3JZ2hhzM%2BginxTttNPmfUW5RsDMgUzPtVC1ecS9Zn5eDU9Wq2bOegPaOddz%2BhWl8tNVYX7UUidIOybFGbgV%2FBVYF5TwhoxBhlA1Lup%2FZ33%2FT1OB0nJaD8vSWPfipuHmqa9Ph2TROzJ2A&X-Amz-Signature=4f96ee676ad40f07fb412c737af6a3ea08568e13a33c8c8f7b2fcb23b2a91e52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFQNSZO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDKj90g%2FEutgIk1sgF43eHjJNAp%2BZdJX2NqncjOG6mLzAiEAkPr2C%2BvGS4ufv5iPyLUacSXxMNo1erE4ZCet4Etf%2F3Qq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDDzQetbpY2OCPuHUXircA2R8A%2FAMOWTbnazXa57Y%2FpgRmhT1Ew3bQaSJQKFsgFmhG9AMe3bJjlXc6wmaNy5Wrm%2FvvNhQgFeRTq7ZjOlXEnwCPRV%2BcUhgTU37QH158Z2a%2FpPO9CYD8WnnUh7A5hvn4akXoEPfUIBjsHVMdGj3C1kh7%2FH9S0gAwQO%2BdgkXrrLcE%2FZ5hUbzBjfJcLevMr8SCFs4Ad9TeHkVP09xgtZDdVrNegVHQZmeHyyfwbCDSzgfbNHwNYRi9P8V6qJjnrSywYH5X1S%2BICw8CMvpFFr81ovNchceobHKxBNxIxnqBYx%2BIMjOLc%2F6E2GlKGU8MlicdBjP8%2BTIrFuYBMaBQ3QFPfmSVNCMmMaUxUr6P%2Bpa3vI9UfE%2FzN6zbCGAdJagq8dOzFwzlG5kyOGNkVZNWkx5lZa1nZFSTpKA9bIGzDWHmI2wMo6SgCZH3vGv7pUG1dO%2FR2ND1USQ6l2p7wvKhIkLDHKTypsg9%2F7tbSHbCoPUDhgIb4IYbPI5UTgnFXlt9GATP3JFWPat52IDXzG2RQ4vdl3Vf%2F8HuwCSlLyg%2F3zJcCJn2B9pis6gC2P4TtjVVFN%2FpLIxnjQ%2BBiViHtBhwUjP531Mv2lUk2gS5jtm7WWZgCzSWXChDewt75EmK%2FHmMMyEhL0GOqUBG0T%2B7Lj0gTYPLdF1bEV5sojAdb%2BwCKpAMFPHDNb%2FLYTC7vs9Yqlzx0fmkqLhvx%2FgtpmaCNPCfpssULQYXcS9vTB60O6rfoTAljkAGKXx%2BvSxLMVXqcmkclnZXjO5RheNXwyWDxZaeYoiquskIV9Vff%2F9WyXflZ7PUBjLWkvgAaPiqQk3yQMq0UqQUrp5A1jDcSR3DfOBcTbD0OxTRN%2BfDA%2F7qYZH&X-Amz-Signature=5ac9c0f1b8014973f480a02f42a90418d5d32e0997b91b9cf3cd716fb8599221&X-Amz-SignedHeaders=host&x-id=GetObject)
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