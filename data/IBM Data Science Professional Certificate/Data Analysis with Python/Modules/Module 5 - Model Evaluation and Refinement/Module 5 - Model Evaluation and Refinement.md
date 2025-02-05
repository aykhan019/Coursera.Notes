

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=936c2ad5776d36baed389ff2958651629af822d508b884cae091bdeb2b990ff5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=aa1b9985f31b63dc68ac80da947d9b814b235c02f424ae0aff74ef6ef62b6f8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=52940d3b7fc529562c8efe88a32fad4d3e10ad075e6107fc9d9fe6783339cc20&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=131979804525293fe44195bdbc87f15702872507bf1a1b05452a9ad8d55b094c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=5d61046509a85bcf9cc742b0755f26edc0491c580a60254a6484f87fdcddcccf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=b44d7c0a0c7b9eacec02e59cb11ca9d5dd508846550f6d621039e21699dbd7ad&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=34eef5f7e9a1ff2b16cb729ee389b5f1f0dc9070f4c4d394713f09663ab1bed5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=87905263cc758fcc03d3677074802bcf605b47ba7e7f477ccc7442bd084f215d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=8b8fe8c41de302a75c7266c1b6bd0facca563c7f33a428ca3cc0f7a90aa3feae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UOYWZRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIF9HYyJNgqz%2B9clb%2BV8TPK7lHwAs7nMyd8ckixPh4WIAAiEAreVbEPzdRnB%2F6wGyUD%2BVn92h4ybMhCaYv2dgkKTpINAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH7s3AQo16akxa%2FIGCrcA4wZQ8mKHnZx4Aeq0NHbmsx0WVhWpsN4ZPSuUjbCXN155Y5k3lutjaK5qDATVGiwHmqps9zvhVJmE3W5giD%2F7%2FTBOFn9YNLuOUjzn0N4HYjKQhJYR%2FeC2kWm0vrk7SDJBAUzZW6DQRzOhpBkJej8qdEIpK16YVktH9YGTLdP2G5z4GFHHjacyI6PtG5bsVPakBe02Dhi80K%2FBjxvSsuMo98P1oWwuuX%2FQQTGRQ27jVV5oUyyC0VxN%2FpxW2lVDAai5xiKiKqaC4PyhwX4mSRYlsOWPMh2kjcy2hPZH4qCpHQ2lk9PFInY0KqhSljZzewMCT2s73AhCKLadWE8PGdxDKJqVxYWlWvxjCx82r46k7S5IIUbODEC0HmabTj4aNzplmgb4oJloWhrQr%2F03Yf%2ByHKUNcVWp5X%2BKTMtVEZC9izuf7dnm7ELWy1mEzfnfB8fAcmZ99Ev7EpqNc6XdzaPTXQdjsVAnJImnSScMn0opQV%2FfoJGKhwwW5J5gF9YINvnLLV%2BqvUdKzswmuA1sM%2BeAsMYSo9wUF5twahtVNRrPHtCk4CXw4O2aKZtI%2BqC2f7c9AhGo4fXCWhf0m97Pmt3983XOLlLbCtknrbCJYZj4PTbc3JBNByiXmbfrkcxMNa6jr0GOqUBGNlIyF5M2qLUK9OIyLCKxqVbd8rlWTpOu%2FufCG%2BtP8PZKxbvGuoXZsEx3mVx7L2hKwkSwQvx1PiIqYfg0QUZt7RwZrmUiwEQMKpKoNSvY8EiZrZsaLURb0eMgueu16SIyuWSLwziqgYL%2BJNKiiTC5zFjdAUuhj7mI7uZOrgLxjVf%2BTnMUo0n2ftaeBfURL2%2B%2BwD0CRQ89TW5WM9V%2BJsce95BOJCl&X-Amz-Signature=c839a894e6e052c360fef71c142b11d3393ee714721c29a98af21326df4b363b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UOYWZRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIF9HYyJNgqz%2B9clb%2BV8TPK7lHwAs7nMyd8ckixPh4WIAAiEAreVbEPzdRnB%2F6wGyUD%2BVn92h4ybMhCaYv2dgkKTpINAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH7s3AQo16akxa%2FIGCrcA4wZQ8mKHnZx4Aeq0NHbmsx0WVhWpsN4ZPSuUjbCXN155Y5k3lutjaK5qDATVGiwHmqps9zvhVJmE3W5giD%2F7%2FTBOFn9YNLuOUjzn0N4HYjKQhJYR%2FeC2kWm0vrk7SDJBAUzZW6DQRzOhpBkJej8qdEIpK16YVktH9YGTLdP2G5z4GFHHjacyI6PtG5bsVPakBe02Dhi80K%2FBjxvSsuMo98P1oWwuuX%2FQQTGRQ27jVV5oUyyC0VxN%2FpxW2lVDAai5xiKiKqaC4PyhwX4mSRYlsOWPMh2kjcy2hPZH4qCpHQ2lk9PFInY0KqhSljZzewMCT2s73AhCKLadWE8PGdxDKJqVxYWlWvxjCx82r46k7S5IIUbODEC0HmabTj4aNzplmgb4oJloWhrQr%2F03Yf%2ByHKUNcVWp5X%2BKTMtVEZC9izuf7dnm7ELWy1mEzfnfB8fAcmZ99Ev7EpqNc6XdzaPTXQdjsVAnJImnSScMn0opQV%2FfoJGKhwwW5J5gF9YINvnLLV%2BqvUdKzswmuA1sM%2BeAsMYSo9wUF5twahtVNRrPHtCk4CXw4O2aKZtI%2BqC2f7c9AhGo4fXCWhf0m97Pmt3983XOLlLbCtknrbCJYZj4PTbc3JBNByiXmbfrkcxMNa6jr0GOqUBGNlIyF5M2qLUK9OIyLCKxqVbd8rlWTpOu%2FufCG%2BtP8PZKxbvGuoXZsEx3mVx7L2hKwkSwQvx1PiIqYfg0QUZt7RwZrmUiwEQMKpKoNSvY8EiZrZsaLURb0eMgueu16SIyuWSLwziqgYL%2BJNKiiTC5zFjdAUuhj7mI7uZOrgLxjVf%2BTnMUo0n2ftaeBfURL2%2B%2BwD0CRQ89TW5WM9V%2BJsce95BOJCl&X-Amz-Signature=df3f9731b8da86fd509a7a4768ccccc3a8783e631cb58a72ad130057f888d6bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UOYWZRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIF9HYyJNgqz%2B9clb%2BV8TPK7lHwAs7nMyd8ckixPh4WIAAiEAreVbEPzdRnB%2F6wGyUD%2BVn92h4ybMhCaYv2dgkKTpINAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH7s3AQo16akxa%2FIGCrcA4wZQ8mKHnZx4Aeq0NHbmsx0WVhWpsN4ZPSuUjbCXN155Y5k3lutjaK5qDATVGiwHmqps9zvhVJmE3W5giD%2F7%2FTBOFn9YNLuOUjzn0N4HYjKQhJYR%2FeC2kWm0vrk7SDJBAUzZW6DQRzOhpBkJej8qdEIpK16YVktH9YGTLdP2G5z4GFHHjacyI6PtG5bsVPakBe02Dhi80K%2FBjxvSsuMo98P1oWwuuX%2FQQTGRQ27jVV5oUyyC0VxN%2FpxW2lVDAai5xiKiKqaC4PyhwX4mSRYlsOWPMh2kjcy2hPZH4qCpHQ2lk9PFInY0KqhSljZzewMCT2s73AhCKLadWE8PGdxDKJqVxYWlWvxjCx82r46k7S5IIUbODEC0HmabTj4aNzplmgb4oJloWhrQr%2F03Yf%2ByHKUNcVWp5X%2BKTMtVEZC9izuf7dnm7ELWy1mEzfnfB8fAcmZ99Ev7EpqNc6XdzaPTXQdjsVAnJImnSScMn0opQV%2FfoJGKhwwW5J5gF9YINvnLLV%2BqvUdKzswmuA1sM%2BeAsMYSo9wUF5twahtVNRrPHtCk4CXw4O2aKZtI%2BqC2f7c9AhGo4fXCWhf0m97Pmt3983XOLlLbCtknrbCJYZj4PTbc3JBNByiXmbfrkcxMNa6jr0GOqUBGNlIyF5M2qLUK9OIyLCKxqVbd8rlWTpOu%2FufCG%2BtP8PZKxbvGuoXZsEx3mVx7L2hKwkSwQvx1PiIqYfg0QUZt7RwZrmUiwEQMKpKoNSvY8EiZrZsaLURb0eMgueu16SIyuWSLwziqgYL%2BJNKiiTC5zFjdAUuhj7mI7uZOrgLxjVf%2BTnMUo0n2ftaeBfURL2%2B%2BwD0CRQ89TW5WM9V%2BJsce95BOJCl&X-Amz-Signature=f5065774ffb1be0786bb1a6a8ef626f25cb248fbd0a201b758c06f2e716b97bb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=18c94ab4abff0d107d487817c5ee5b9949e944684ced08f17c37cfffec5492f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=c4f490478828d0b62b2159f88b50cd22ba7e8d3f149a96d0b4bec7d88fab4efa&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=71de559b6dfb392d9661919fa696c3bccf6c9b730313f352db19caa5d9ebcb25&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=08953391294040c735742439788169edae4c7e465807a7f53a7b79c5d7a619f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=d8290877fb260079eeaa7dc47628a8a2516ce3fad2e85ed4f80a352a67ab3c21&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PGODALK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAaGvFGJp0hs1cSS1%2BV%2Bhmw3GYBeE828wlzNiR1yD34iAiBii9GkD80l50mZw%2FKT1%2Fl4VJsuZhb73mme2lBwVUB3vSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM1Cba64ILSVPkvfUwKtwDDX%2BGG5uNIzDgUHe%2Bg%2BGzzcDdX2nMkRGOJEDsIenLXTCfA4SqVCYOLEqCbsZxsPf1Yo%2B35JsPyB9Ld7ZgKCCsHw7l09x%2FEe7XVJSHtTeXChWxjOw6919nzz%2F1xyY9g8%2BxaqJz%2F0SvLkJMlk5L2fuYYt0XTXtAJA5zVTKAFkvQsfiR40I3C1TrolPyk2vHPlH8vL7teTVLroIIc6tWBcIHrrHvTJrBzOjCXbOQPzI%2FPnc7PJqYMshNpKZyJSNgxdOKTGo2pHj8lOQMY5CrNRJTANF6Q3P%2FWsy1jQ4wGTLmxvi91N5Kqt3O3Iq6Mu93BXMkZTszE7lEJ5DGeTvsIHyI0hfH1fmTdFwPvSlNJDnaaZZSv7lt%2FtgUrfZjpyUeIHjLHXvDqQA1O%2FnT54neHSN11O1Sf7%2FFdoA1Inp1OZ1mFz1CD14xQ3ZbRYm3BHaF9176KmmM2KICI9tDkyodY2PsQoHVntdi3c5RhE%2FPW0dEQG8K8kwd%2BDe%2BWnfuno%2FZs702KLlt7GHmnZJTFShrtJ78dCeyqBqTl0m8U7ANYFCcIWKni53yAiSyrS%2Fu6HTA1Yh3tnNs2Tw%2B4A2XanY9iuZPYDXWbP0cx8mgy2YWuGty%2FE3Q15hzqeybewCseNswz7qOvQY6pgHNZUEjtzcbVInq9J1YbSS%2FV68bmy1Y1Tt1GHKf%2BCjG%2FxI%2BKRKqDSkGmXuBiF632hP1p9ttPJWkFvaO7TcQ%2FHqB143fYPmkgfy9HObXWwcCs4xYtaw0CBs%2BoPWnelAtzm%2B%2FqoTkdBtRIccjgjKIsM8MZ%2BHjvQ7ERwqGgFTg9%2BfCSyThx%2BBCXBAxN92o6lD8V5CixdxWiP2FzMLLqhvbYjYAdbTxLUA1&X-Amz-Signature=96a8cc554dfa81cd4ed8389e2322eb212b2e7aa67d3f482c848a376293e19cbf&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MURQRBS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCzXNG%2FmGyqX3%2FxtyViRtwFDpRR%2FtaBF8Tz8EQTG7EefAIgZ6MVEis8Df%2FCcFi%2BEU7Ga9R2ktViKAee1JA8chn9jyUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOf%2BF6ebuuX57k3UaircA4ISpvKOTJEAQAPcip3vNszdbo57PcBsc3sNj%2FEBs2Ol%2B5ux%2Bu%2FoTQRT2Gy%2FaRj84Gzt7oXgHa64xDGH8j1mAvpi7DQlWcvesByOgRg9mzKeZhtOHkfHkk79LHiXJ6TUwQwJ%2F7m1KyGBlTnbN9yy%2B7%2FrpwIatF%2FpuAdM8YKchUHyvfiTxPZHCXBKVuoQz3paJGTVNizy9lLo5t8QGBt2zllDp1DHa4GGdwRJg2gOrcRWOJ0AtkIoEt6wWwtIxc5P%2FZi5ZM135am%2Fjsz0Rej%2FxRow808Gzuny0ShgPSuyaCw%2Fh0AOnlpWgyvWkIGkfKRWe1HSQRRRYQCA9p%2FXQiEDYVT4VwaV7FTy1nca8qqPVEqUWGUq2xGUdbcTog9PFI4sckBlXKmSJfzFjuzCf2%2BbZbtSrbe2%2BQV5Ofeh1TSpCAXlj3IM1W38MBMr%2BiYKfqoNf5cmGnULneEAdYACbGkpKuUwqw2AA0uYuR8YBumEhQWKSC8TGZ%2BsLnxvh4tn4%2FxTRuyZxsUskpVxUUi8vIQ6szgNkNw%2BTUwCuudeXWWSChu%2FIPUcVGmz2GAjOqvkAM0Ikx7CI62pMOgNmdI1GHaKDafwfIRKpAm1OBA%2FRn3AV8YUNdes5RGERwoOzkXnMLe6jr0GOqUBDRqdLxUHMq4KPvheIcEefe610lgnAmTRdE%2BfWJOMX%2B0Hl9un9wYYFaa6iqdINit9N%2B1HRnHW0a5yhwaNRh8op2QbDu0FrnAJTQtHvfy8b2oCEJTsGPxbnwjx5FntCGfuVEVgZK%2FJu0JJhSdP5ahTOD2DoeHjI0m8pMtDqyqYvpvEeJYN29%2FGoVsRPCLhQFJ4uzKNzSdEamiymrqSXsz3QpFXi%2Bg7&X-Amz-Signature=adcad9f382d9d6aa3fe19fb0ec2fce4f0ddb82e06e671d1fb1dd4082403da61e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MURQRBS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCzXNG%2FmGyqX3%2FxtyViRtwFDpRR%2FtaBF8Tz8EQTG7EefAIgZ6MVEis8Df%2FCcFi%2BEU7Ga9R2ktViKAee1JA8chn9jyUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOf%2BF6ebuuX57k3UaircA4ISpvKOTJEAQAPcip3vNszdbo57PcBsc3sNj%2FEBs2Ol%2B5ux%2Bu%2FoTQRT2Gy%2FaRj84Gzt7oXgHa64xDGH8j1mAvpi7DQlWcvesByOgRg9mzKeZhtOHkfHkk79LHiXJ6TUwQwJ%2F7m1KyGBlTnbN9yy%2B7%2FrpwIatF%2FpuAdM8YKchUHyvfiTxPZHCXBKVuoQz3paJGTVNizy9lLo5t8QGBt2zllDp1DHa4GGdwRJg2gOrcRWOJ0AtkIoEt6wWwtIxc5P%2FZi5ZM135am%2Fjsz0Rej%2FxRow808Gzuny0ShgPSuyaCw%2Fh0AOnlpWgyvWkIGkfKRWe1HSQRRRYQCA9p%2FXQiEDYVT4VwaV7FTy1nca8qqPVEqUWGUq2xGUdbcTog9PFI4sckBlXKmSJfzFjuzCf2%2BbZbtSrbe2%2BQV5Ofeh1TSpCAXlj3IM1W38MBMr%2BiYKfqoNf5cmGnULneEAdYACbGkpKuUwqw2AA0uYuR8YBumEhQWKSC8TGZ%2BsLnxvh4tn4%2FxTRuyZxsUskpVxUUi8vIQ6szgNkNw%2BTUwCuudeXWWSChu%2FIPUcVGmz2GAjOqvkAM0Ikx7CI62pMOgNmdI1GHaKDafwfIRKpAm1OBA%2FRn3AV8YUNdes5RGERwoOzkXnMLe6jr0GOqUBDRqdLxUHMq4KPvheIcEefe610lgnAmTRdE%2BfWJOMX%2B0Hl9un9wYYFaa6iqdINit9N%2B1HRnHW0a5yhwaNRh8op2QbDu0FrnAJTQtHvfy8b2oCEJTsGPxbnwjx5FntCGfuVEVgZK%2FJu0JJhSdP5ahTOD2DoeHjI0m8pMtDqyqYvpvEeJYN29%2FGoVsRPCLhQFJ4uzKNzSdEamiymrqSXsz3QpFXi%2Bg7&X-Amz-Signature=50b0f1d7951e5f4795d6ff048533bebf71a8d9f398dc654e8eafefb06e56b7e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657E4E4JI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIGejbPm%2BMVU5LAvBMVHS5972CXUD6ujn205c63oqK8Y5AiEAlCpcxt6gHFOyg084UdvRoTJ6FuRgCYRd0COMfQsx%2Ff8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNkNCnZpgnIQlyqy%2FSrcA4riWJ1FrTGwS8g%2FzYo83vRbribL2Gv7WwXzo8MaaRzLdcfKthEJAXyh0mnRYuSGrG7U1Jehxu6iSSrRXWd1rqodrlAiT2CxPf2CPPQY0VmNHV4Sj%2Fwau0r%2B0UcI8idq0%2BmwVbZx1rSjVz48%2BPc%2Fh%2BgVZG7KGpNrXKi1M3KGb9QFY72rdXBa8%2Fc9i8btoOfvZ7pioGZSmp5xt1pxhjI2X51e1%2Ff38vAMbPsvhSB9C74IM9nh6niw5HOZmbjRdT%2Fro36POkKyKX2T7QKROpsGCsNnkT%2FXnMM6RtWqiSkcf0qQOqOSTabFuJ5JkhZC5cK7zE%2BL8TIANBGaW7AL%2FryW%2FbWuadEQmuO1HrgrfqE6YaOMhUo9meRl%2FStsUIz%2BAaf8FsDPk%2Bl%2FkY5Smf6JHf64dyu4Z5kJC%2FJyj0DyjShcR0UD%2BtZrZw8HNvkT6FQPk44zEUTsAPfMdON31ZibJu4lULV%2FMX69vhKX0J4%2FBUaEsU%2BP9yaGRKQxSVawG%2FbclweeIQupAzpbY%2BUWtbChov7ynxShIyoWxvaEvvfRyZdS87L4adKWsYRSvQB%2BFCdeVbS7Je2DjIZUmfOnVLJ0hNT7DDhzaBbUSqU%2FQ%2BJKIDrgiKhON9QRjVFKMHVGvbtIMK26jr0GOqUBjVfZIpInxyI6FSfvKZ%2BmOxQgZblQjI4axVNoGgkCu7ZfLLtVS7AAIAo0ZGBSbXT%2BDHg7w%2FZ%2BfUkFO38KkLTDQIljTSRhzpCxBsFUc6XTtHCNzOrGAfolzwAAbOtJGqY6LTQJAbQrGGwGj9q2tfna%2FCaPZXI0n%2FuWiPzloJM4U2Ugag9CzOnMxp2DDPXX5ZC5Yj8kiGIcq2ZzAOm97SnYaq01R386&X-Amz-Signature=b5a8b8169c1fcda54b06a3cde365f9859ab11441abf4e854c20a3ab76b2e3246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWGLKDPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD02Wx64Iw%2BpP0oMgGEcXaFUWzah5ldtcjM%2BZ0Bp9TDFwIgSNJkCK%2BcJpVixx7q00i2sxking94kP6qKFQYMb1i1wcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLIPfon9P6qimvHmYCrcA8fMrJOUfkt3pivQVOURJ8Jt70lyaqxYSJiOx2rF5T9Dq8c%2B911gY9ki%2B8wLkIab1Srb%2FHuM%2BdtYslDz77ApFXSsUdXfjw2HyiRiAatMSpYR0T1vOqLxpngEoW1WK97wPS51zQGD8TlUD%2F7XqdGP2m%2F18ClQEiCgvHoo3%2ByMWYT%2Bz%2B94w0KgCnB57ewrObVaM42s%2FtR5kPHaUChO2EoBKNc1X0hmgImv7JHE3A0%2FLQwyL823HHvAngSriF2JUcsVkRckE9GQwB9o8EUmYM20aI%2FmN%2FjlBWYdbv5L95J2UD7IqtXOxUcxJvpVI%2FkwQLn5A0VKGAOZm4QsWh4kNT8goTmjFn4SjfEIFbGqzVEscLaiwQ11LPzGUo%2BUS7pXr5Tkjckbv25Oa8sJIv6CrHGbkORMrT50CRfeqQJkzJ0B92P%2BIiA0wCshnPpddBKC%2FSYVP%2BRYKJ19q5LF7yn1FXFdOzVkZxGbtCLYKBji6nR7eMqOGeDRU%2BclrAezeqfzLBl1MovkBnljED21hFd8tfOh%2BPPzXUfvbAcGfp3SwJORatIwfEOFbCuZBzxXPjGgvgk9vn446Jf%2F7CpiAjNsqBVEgtt6hCz5lLMIJpB3AuFuNQvk21KsXdHMn04rtkh3MNy6jr0GOqUBIv7T3AiNUtVeSyymgmyLUc%2FqMJjMdd5s87Ko%2BJMrcTbDVWwf95ZSq9I%2FCSspBg7HmKIg9z75Ex%2FBjIeLGeGMaaKeg4LELvd0%2BlGLPWCvUStN%2Bq%2BR7fL%2Bn1KCDeqPka9ceOcKZo6EL%2BpxODm0pdxpDGhLfl6g%2Fc9BcKhKyZ2pTJoZwdoZCLiECPdyKBB6Cy1zc90XNE5%2BsloxrhF1NfjP4J35HWk2&X-Amz-Signature=97be4dbdb13fd20860e6444a5531a91fe67eef77b2f0b5d9ce94c4a2ae8103a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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