

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=5ef19920d98d0589247fa05515b002e7efa6c556dca67e1e0c0df381ecd4a5bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=80c686805a488afee503bc1361c6a412c0a042ef2891bd08b85974905ec5d92a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=94f2a66530abfd43541e045295e3774dbdd8850c700c67c60d933c36082bf300&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=3ff3973ba879ce67ecc216ee358acf7caf8c13a72bb4a20348e552fdfcafd120&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=76f871c21dbcd90176a2d9efde6be953bce7076e62187d9a787d735b066630f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=b203a95f8532c89d9c3e5cb71adf7d279d93ff9a917b836f39de28e4837e1bb1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=e7a28fdd1734094bfa141ee5d6f0281186fc803145c1a09d8e265679b000d726&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=639dd9f631b811dc87b931fda9fc39fcceee15897caf32780fdae222f5366624&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=3d17556c3fee6eafe1dfaefc8404a029bec45fe889e79dda033c9d34a8cb1361&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W6KI4TQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhz4JrEeyvib22%2BrSS6mIS25iGw%2B9Ya6911fuBmgIjLAiEAmxKPULo%2FkKVI7L6zRtJEQvAJCpyfqu7YJKTFI8NMjnoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKwb686NePnxdHQVuircA0hYN9WkBtx24MWmg2%2BjWHL574nL7OC4YanLJK%2Fg53DXP3hcKm39iQsDi%2BzmPrvzUb0YaTRVh2IJuZr6EcF25n7WcnrU9HpfM0Dr4kCA%2F6OTYBigWGQ0iQrFbB9eFy77aYE%2FCliKWnfbn1%2BYsEWMbBlwncwJJR0imtg7gRTFLAnkSJgenS2MeF%2FvzRMu%2BHKGOYqlW3vK6cA8NtrgE4fiL0irUWOSG9aSiwznV0jHJt%2F9DREaTKEEPjaj4Xl1N27eBhIV0U5ObRYbfrwheApy6OnTOGkFTNIo5ASECLyly77i3G6q%2FFGHxppCYxuHvztVwXFSAZgZ5gC18DMiQA4TDBy80NCohFBcLAmTfb%2FOG0Y2KdIfDKcuJy7UIHJSh5xDBiXhrdLbFdqggoKf2yxUjB0jes4AvIMES6TLotvUJp4JYt1g7ceOyC2zm5eHY75jR3L89NwtDt9JJGxOuHu6INc77PZ%2B6ViMKTKQTQXQwjTlSfUE3KAw1fLkhMpfsQm9v17RmJHN3qPmQJx%2BoocPm3T0zGgQnFDFG%2BNbphVigScRiYlKa3iMZwRrO5fHG63ZzY%2BTftTSjxiOuVWixqwa7nEyjVezWsHSrxnt4LoYUtw4pboyiW0Aksx0KGYvMMql9rwGOqUBOHFWQr6E1KZPyuPxxGDS%2BGUrvLqqEHkRWbo6ItCMWaMuoLt3%2BPwSTwnykUyHoV%2BEd9GCsMnrZ2KkyuZo1seh25KRxAEtLlKE9huwJmFD08kUAkmA98%2B7%2F%2BSt2fz%2FtYdP2VEXPcWiKMjxzSqfnuQhS%2B7v5BjYfoZ1xgR9QNMzCCFLnUZOUrXm5WobIvYjkAZNZvPTltU8PtbV%2BJ%2BaVLXKbMrVsQ4G&X-Amz-Signature=d1c775521846d8f70b6fb2cbd418aa6ee2aa36a325d5c08b777eb13039399998&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W6KI4TQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhz4JrEeyvib22%2BrSS6mIS25iGw%2B9Ya6911fuBmgIjLAiEAmxKPULo%2FkKVI7L6zRtJEQvAJCpyfqu7YJKTFI8NMjnoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKwb686NePnxdHQVuircA0hYN9WkBtx24MWmg2%2BjWHL574nL7OC4YanLJK%2Fg53DXP3hcKm39iQsDi%2BzmPrvzUb0YaTRVh2IJuZr6EcF25n7WcnrU9HpfM0Dr4kCA%2F6OTYBigWGQ0iQrFbB9eFy77aYE%2FCliKWnfbn1%2BYsEWMbBlwncwJJR0imtg7gRTFLAnkSJgenS2MeF%2FvzRMu%2BHKGOYqlW3vK6cA8NtrgE4fiL0irUWOSG9aSiwznV0jHJt%2F9DREaTKEEPjaj4Xl1N27eBhIV0U5ObRYbfrwheApy6OnTOGkFTNIo5ASECLyly77i3G6q%2FFGHxppCYxuHvztVwXFSAZgZ5gC18DMiQA4TDBy80NCohFBcLAmTfb%2FOG0Y2KdIfDKcuJy7UIHJSh5xDBiXhrdLbFdqggoKf2yxUjB0jes4AvIMES6TLotvUJp4JYt1g7ceOyC2zm5eHY75jR3L89NwtDt9JJGxOuHu6INc77PZ%2B6ViMKTKQTQXQwjTlSfUE3KAw1fLkhMpfsQm9v17RmJHN3qPmQJx%2BoocPm3T0zGgQnFDFG%2BNbphVigScRiYlKa3iMZwRrO5fHG63ZzY%2BTftTSjxiOuVWixqwa7nEyjVezWsHSrxnt4LoYUtw4pboyiW0Aksx0KGYvMMql9rwGOqUBOHFWQr6E1KZPyuPxxGDS%2BGUrvLqqEHkRWbo6ItCMWaMuoLt3%2BPwSTwnykUyHoV%2BEd9GCsMnrZ2KkyuZo1seh25KRxAEtLlKE9huwJmFD08kUAkmA98%2B7%2F%2BSt2fz%2FtYdP2VEXPcWiKMjxzSqfnuQhS%2B7v5BjYfoZ1xgR9QNMzCCFLnUZOUrXm5WobIvYjkAZNZvPTltU8PtbV%2BJ%2BaVLXKbMrVsQ4G&X-Amz-Signature=69e997a5556fcca7e52750beb9d938007cb3985d73774a068abf00d03c468c50&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W6KI4TQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhz4JrEeyvib22%2BrSS6mIS25iGw%2B9Ya6911fuBmgIjLAiEAmxKPULo%2FkKVI7L6zRtJEQvAJCpyfqu7YJKTFI8NMjnoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKwb686NePnxdHQVuircA0hYN9WkBtx24MWmg2%2BjWHL574nL7OC4YanLJK%2Fg53DXP3hcKm39iQsDi%2BzmPrvzUb0YaTRVh2IJuZr6EcF25n7WcnrU9HpfM0Dr4kCA%2F6OTYBigWGQ0iQrFbB9eFy77aYE%2FCliKWnfbn1%2BYsEWMbBlwncwJJR0imtg7gRTFLAnkSJgenS2MeF%2FvzRMu%2BHKGOYqlW3vK6cA8NtrgE4fiL0irUWOSG9aSiwznV0jHJt%2F9DREaTKEEPjaj4Xl1N27eBhIV0U5ObRYbfrwheApy6OnTOGkFTNIo5ASECLyly77i3G6q%2FFGHxppCYxuHvztVwXFSAZgZ5gC18DMiQA4TDBy80NCohFBcLAmTfb%2FOG0Y2KdIfDKcuJy7UIHJSh5xDBiXhrdLbFdqggoKf2yxUjB0jes4AvIMES6TLotvUJp4JYt1g7ceOyC2zm5eHY75jR3L89NwtDt9JJGxOuHu6INc77PZ%2B6ViMKTKQTQXQwjTlSfUE3KAw1fLkhMpfsQm9v17RmJHN3qPmQJx%2BoocPm3T0zGgQnFDFG%2BNbphVigScRiYlKa3iMZwRrO5fHG63ZzY%2BTftTSjxiOuVWixqwa7nEyjVezWsHSrxnt4LoYUtw4pboyiW0Aksx0KGYvMMql9rwGOqUBOHFWQr6E1KZPyuPxxGDS%2BGUrvLqqEHkRWbo6ItCMWaMuoLt3%2BPwSTwnykUyHoV%2BEd9GCsMnrZ2KkyuZo1seh25KRxAEtLlKE9huwJmFD08kUAkmA98%2B7%2F%2BSt2fz%2FtYdP2VEXPcWiKMjxzSqfnuQhS%2B7v5BjYfoZ1xgR9QNMzCCFLnUZOUrXm5WobIvYjkAZNZvPTltU8PtbV%2BJ%2BaVLXKbMrVsQ4G&X-Amz-Signature=a9a11fec509097722b39ac684cbaa92483a8637bfd510731ee2cdd9a0362a88c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=6ce87c0955bff9cbf0a6b4501e28842e25eda55864b6678c62c4f6f121a2b143&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=dff00c78ee55168200cafd604b88c52674b1a3377e37da0d5a514ec342aeea0b&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=4be3184d1bcd959693a02cd4240297ab163b3181ce1b183fcdc5922e5368db63&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=1c98efbed3042410a0392b4ff3c78e52519b47430253b7fedcbdb89bd5410d81&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=e127d9825f1f21a07384ae7f355904cd8da5b809c26d01a3d8b93027fec64121&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHSWWIXP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsvd72%2FGwyIbRZGABYJlkV%2FAB1%2FHiAYKVTYhqPHMOj5AiEAumys4njqUi3RBpS%2FrSUxm8%2FrHQRpn%2F9IkyKpkvQvQnQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkPEvNBA%2FUUHIqIwyrcAwumlnUV39nIKqRXFEM13YuvAz5LWNPx8xBNdTcf2jsQvaFgvajPm3uGF8OCDTS7Oe74lfOjpGlArs7H6NLWAwa5oXbNHiLtweczEyGaKg9NTalpcIMxBTds%2FCTj2gwWYItItxgnC80ihKxYYlu7i13%2B8398MhVcpUJGzTTZiI8pIZy3IIrg7qDIqE%2FnZOT5aYWnSRK50JNewSlejVXtm%2BwozXmJhqQ%2Fgta2z9H6PTmPHiDvy42grv0KKmm7PkYY14kGXS64ndBG53%2B82acdZlRbG6B1Hc8zLGogDZP66qJG6MVuk6SdJ4Z%2B756z%2BGtqf04vVm686shvvSiSK9kZP8JqR2q3nNnH45FpFtGhx%2FsrvIg8LNWGYf2OGJcfmO2vIUbiFgRnY8YVuV0Egkk9XrE9pVB3nLeQb%2BrrkTTTv3j%2FyAdVUf4Lo537ej3vk9Bv9DvoYlTjJl3h6D%2FxiSAUX6MjI%2FeK3Cya74nyJD23hngO903EXVTpVOrNyVLBdMEQ%2FHLa5jix9oWve9o4BJNl%2F3J0%2BMzxbLRxrr9rEHTDTSUvbYLgnvU8eNXby4nAVC7vqbMFu%2FrG7uA8L5yu5vSk4EVEcOL9CpgmU5iM1u48itWjaoiSkmLBLCJkijhGMLWm9rwGOqUB451FMTZW%2BCCAcGTPuBB8w9mw%2FcO4gDGK7CVWgrfMKLMbu9Fr9RgmMWWo3f5A%2BhIw3Yho89fE8NkZ6UL%2BHtj%2Bwi3E%2F9%2FAFNL751Jp2hC44Gc%2BjDDaXUgrCh70VuXeB8RqHXkz8xfW0Jt1DdPiaYyrXvGRDyJ2nNSJAeH%2BJCsFATk9kLpqJ4UbdelnPj3EYNUtBtSVGTktt4r3ZUFEaXAuNnshS1dy&X-Amz-Signature=6d2b041c0c7b77020523dc677b1199ee2d568bfec67c0f606a6d1ed23662fc18&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF7HL5JF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLKpX5QrKI5pcq3L6Rx3pDEmaTK0cgDhNP19o%2Fvwf8lgIhAJqBxr2%2FV81bzd1oCAl4v8NffoSBTPkH%2BVaDhC7CGbcJKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0RdBWR8pBeIKF9Soq3AMriLZwijL0ZIZzUJJW057CPLTKq2%2B63TcaMXhGKZZiIZKfpD0GU9yFg5jdWpf9HVBqqiURYz1SxHvefku87Y2bH%2F8795WO2FuSzyqEIZAT%2FlYIwgaUHuQn9Koxi%2B2sNfenBRse34KvpBOTE%2BMGAHbEEI4jdw2UG3lKl0%2Bv4QKOGOVGJZDlATS2FeaxzkYiw2ZAtqhEBNuCRpT9M%2BLjtQKhRkTX5WnNGFVml24NxfB1SpgCtYTeZ1Sh5sTi%2BcAGaWFpyEBEr5s1dIKSI6s%2BfDaXoYnnzWPDKkyUn75HjbSj5eokk8uQc4ZzTs9vYx%2BQB%2FVle3Zn8iNnAHLqxYh6IMQMzqgt5Mod4Ksse8s993l%2BYRFNuHEsz83pLuEyGyI%2BcIGT%2Bf7IbKtUg539piwPDW8xxubuRqlftkExtFh7y7C1tuoJofW2qMZq%2FYLGqB7T8CbTleZuzgiRXAkPiisYK3aeXwF9WGAgD9AiaEQu50Nrf%2B%2FgqWQznhAf%2F9Hs3gzcZG7AxMzLT%2Fbbf6xi7yqMAjixXd89sfkl%2BL%2FJaP8gQvGz2xDWx6DkWD397wvqPlbxYo3e6XdI%2B9%2Bt1YgheSu69Tzj8KpHYBCK9hX1aXd18FfjEShGEPxRQcfCc9XMLDCcpva8BjqkAWp8UEMYYbSqqRBMx3UDL%2F2QKDef%2B%2BwfEmhrvvjQ2F0%2FLXb%2Blf%2Fioj%2BA4B43HHeQ7QJM3hPnogkyeypRiGqniiWGI1osRkJggNVw0llc6jFEHvaSHiKWU%2Faz7gRKXVGAOo8QVJ5MLta9jXPuhOTtDcMGuUe%2F4ZaJa2k0c4kiu0d7M96heiAMe7Ciw%2F1JAVnoZAoYIx06%2Bfxl%2BQmgzmM8rID9cF69&X-Amz-Signature=bbdf30342d65bda488cc174e5bbd04db08456b60851d247dae29ef2114371170&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF7HL5JF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLKpX5QrKI5pcq3L6Rx3pDEmaTK0cgDhNP19o%2Fvwf8lgIhAJqBxr2%2FV81bzd1oCAl4v8NffoSBTPkH%2BVaDhC7CGbcJKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0RdBWR8pBeIKF9Soq3AMriLZwijL0ZIZzUJJW057CPLTKq2%2B63TcaMXhGKZZiIZKfpD0GU9yFg5jdWpf9HVBqqiURYz1SxHvefku87Y2bH%2F8795WO2FuSzyqEIZAT%2FlYIwgaUHuQn9Koxi%2B2sNfenBRse34KvpBOTE%2BMGAHbEEI4jdw2UG3lKl0%2Bv4QKOGOVGJZDlATS2FeaxzkYiw2ZAtqhEBNuCRpT9M%2BLjtQKhRkTX5WnNGFVml24NxfB1SpgCtYTeZ1Sh5sTi%2BcAGaWFpyEBEr5s1dIKSI6s%2BfDaXoYnnzWPDKkyUn75HjbSj5eokk8uQc4ZzTs9vYx%2BQB%2FVle3Zn8iNnAHLqxYh6IMQMzqgt5Mod4Ksse8s993l%2BYRFNuHEsz83pLuEyGyI%2BcIGT%2Bf7IbKtUg539piwPDW8xxubuRqlftkExtFh7y7C1tuoJofW2qMZq%2FYLGqB7T8CbTleZuzgiRXAkPiisYK3aeXwF9WGAgD9AiaEQu50Nrf%2B%2FgqWQznhAf%2F9Hs3gzcZG7AxMzLT%2Fbbf6xi7yqMAjixXd89sfkl%2BL%2FJaP8gQvGz2xDWx6DkWD397wvqPlbxYo3e6XdI%2B9%2Bt1YgheSu69Tzj8KpHYBCK9hX1aXd18FfjEShGEPxRQcfCc9XMLDCcpva8BjqkAWp8UEMYYbSqqRBMx3UDL%2F2QKDef%2B%2BwfEmhrvvjQ2F0%2FLXb%2Blf%2Fioj%2BA4B43HHeQ7QJM3hPnogkyeypRiGqniiWGI1osRkJggNVw0llc6jFEHvaSHiKWU%2Faz7gRKXVGAOo8QVJ5MLta9jXPuhOTtDcMGuUe%2F4ZaJa2k0c4kiu0d7M96heiAMe7Ciw%2F1JAVnoZAoYIx06%2Bfxl%2BQmgzmM8rID9cF69&X-Amz-Signature=ae9a6bf51a67365e813d1f082b10956f8cb4968acf4bfad53c81bef19f37dbd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBRBD6X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAg0wBy1pBSba%2F%2Bh7TleI9Ibyuoy1DbWbI6Bxxpok4FAiA5aytTX%2F9RjuQY4gc8EdyVNKva4zmjeCXCzgZWuMmPXyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyjeWbE3%2BfF9FZQb8KtwDp4N4FIr%2B1YTqXjt7pIdgCqEvQpL0bqqiJ%2BlohAByxl2YbG6hXL6Up5D%2BpMx08pZ4sCkC8Nc2xyYOW4aYigLExnwYNc5P24r0IWyzSbE5RJ6IVZWAbXrEkRTup1ZjnShku%2FdEPweNhbXp9U3yBHLcFqz9Uav5BENWRb7V5c5f%2FZStlWX9lpYNlUh4bGnrtQaJGze8SrfeN3atqwzRoxFF6F6VaHsl3l1muBEd7vVMyC0HY5qgoRL9HXt%2B5JNgRaWbsQjVkjvoWjKbCmcwuZY3Vwg9iCe5jz9AMaglu9iJaAzizzaIQhlFvn48j9JC6M7aO5EK%2F6KK76DEpAXYFYlC6bWymfnieOtEYyBnBJjBu7xh29BHNPzNbaREs9qiuTP2YnQ%2BGmhBLuEr%2F3K5M7u6eemaSy26swqOfPxz3UHtE2HzfIlraFYPrOp29r0sGU3Ogkvx4RJQp4pTv9v%2FhDlEFyb2XiO4V9NmjTkZhEzqYFrIQDFn5yL1msS%2BiBNpFTKc3dbJu%2BFEIf8r6xhBiXMtYo4Y5R4SWAv5jtqNozBDjHxEFIXxtagobYiVaxPTUxqwpkm0aE1c7reVm3s4lOz8yy6A2Miyw%2FOLuZkMJh1Mpx6ml9DZO1hvP7SyMjAwyaX2vAY6pgEwOZjFlN33%2FVF7RHx2u7X%2FPBKmK%2B1qRjHLwtIJPFu7yGo9KArJZXTRDOJ0moCvKXDEYtsQ90NYn8%2Fzqi05gr7NIgjIE15fZSXgSF%2FTODEyz68u42awS47or710jEiaJmSW2Xix2oWSLOg4WY7T6hKsm%2BnFKdAMcyF4uWuGEzyvXDJQ9A8Fp2NarGk9zovpnUZcY8%2F5%2BLsIphPG65FhbEfnFzRVVn9C&X-Amz-Signature=a3171903aaae29d2261f73833bc7f2a75de7ed414e9eec6a8b25e9f7a5b32253&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNVRZZS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMlVQJxgi3Xy%2BglIWzuR6Ohm2wvL0QMuh1pQwd1o73nAiA9UR9OEvLIsR4z%2Fkh7PabXKiQj9xfI9tHKTNxfaR6hbiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJlAZ3Q0%2BPwWzXStKtwD1sKYTm1T6fkZ8M%2FnWg%2FEWw4IgJpUi2oRV173dg1SWAt00Z8yqthpRSRhAUFm1xda1ba8jNaZKLLDE3bNJsve7X7IZMh2haUDCfENKctqvIqNWsxzpL9%2FvjQ%2BRSmpSi9yDU0%2BLM7EZ3JlELgb3QP1%2Bai70przGig2gUCKRt71XL1TbMfMpSEV7tKVQkhUPrTPnAgWSpbxWTJm2AnFPK%2Fv7BaVQDBSGWWUyo61f2P3dpDEEOhnx%2FeXo3pgxNmSS0nQbt3gBtxcMv3N352OQlXmBFKoqc8FnKPkTbzmAHcNG9mzgYbQ2Rn1jjwcLBiXoy%2BLPCygPBV50NatFAK6E8edOqs7uOLZaB6sscZcKgcxYp1ll6Ok7GOpgqtZ%2BaFrXzoRUPtRI8xH2sIjxHCyrpgRvvzHjMvHYzEzEid%2BdfZYZJ9kw%2FuZCYHLVM5d5yhxJZ3kRoc2AQt8FRti%2F69XCzLt1j7mF9apKfEToCA5ghaPqjTW7n%2FIFB29V%2F2%2B3BYlrhnBXV1nyyZ%2Fzeszhijl3PD9E07NICt6gO2EEwKfYJn%2BEmopMH2H0NRZDtESsofinkWLje%2FNYaJesmgrP%2BpBPNpzi1q6aisgmlGvISpbNTk0Sxp24cX3yJjZADuaNnsw86X2vAY6pgE7E0QBBI75ASGA6MkvYrOazRIBUKEXewczbDwGCt6gU%2Bv1rd8uj3ywpg5s5W3648HH5n83MtvN2jLlKB5RV8qfZZC7n7VE0Dkj2JA9FIa%2FohmXyeZKtc9d9YxAQSry9cztVp3PAhChCgmGcFqFnaMgZPE8ugB2f4TKh5dojzieK5NQIIzeLyMIRZA%2Fs4KCry7S1eCkbrLgXnT9AQP4fkKQMjbzK6i8&X-Amz-Signature=cbac89f04e5fdc7c422bf3c5372c4f576a90d99a3863a8be1c8ca597d567a890&X-Amz-SignedHeaders=host&x-id=GetObject)
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