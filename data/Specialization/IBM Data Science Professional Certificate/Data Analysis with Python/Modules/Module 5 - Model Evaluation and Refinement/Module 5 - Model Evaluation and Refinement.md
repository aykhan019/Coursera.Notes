

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=389f7e7fedc0c5713e36f58cbb90956e7e39e486e4bc78235216f806a7f4c0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=b227b901927f5c922a2dbaed9a9b1521e8005cf8957552741000a714c4818c5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=f7ad572fa122b25860b1d8d071662a696959c1ea3eb6473e829c5bd138632d78&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=363efb5b36ff8c3e4b50800e7eae36aa756e78471ca7401f8d0abcc3aacf962f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=22d917704abe74c31d16773c30d23612c1d79905338c558338296c320abaae8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=682b46e4a1e178b2c59d65b12d28f95dd9c0df49f39581f11b00280c3a4b1ec5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=2929df2dc851a0dd10ebfe116d4207906368e1b0f86eabaf2a3ba94a5e98d939&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=419f96a7b4fb725e81effd3e2253f93b4a982390fd85e35872552cb1015250d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=0a0a2732453c063cbbbaeb398a49f87ba34289cc344df503bf3091a19fcd8d73&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4B5UJWH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGY1kMAbtsoyv8ZN69NdqYv3viXVgTP4o5uqxqSNnYpuAiAHH%2BSOEVpzmKwcT%2BIcYKSdMR8v0AsaE0MO7swnqBGXvSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9Z08PssgEBIcNj8bKtwDKzm0L660QIihKfLZpZrc49Tx5zvFptpeHBNeOvkozWjIyLRF2v1FCTJYwq8enqI%2BmvoTCCn0KTktMSVfsQzGEZl%2FiTIaj2qxCRI1oc7xQ6Ajfew8jD1x2KPLOlLMFABZIms%2FpzEVt2Sb%2BjlLTAUlerDVQcMI262tHcb6AmQFkusXrvqVPtgdUBs6V2mSAKSAHcroV82pjXqNKyKxm%2BNy5fTu6Mae4NSv%2FV%2FdSWXe8VEjHZ0Xm%2B1o3%2B0HxjB3IOjLQca10WQCKZ8cJEv6p0tiVfa7Y%2BNPBtpWszAowzriQswacwZQ9ZbPVUm%2BxB0Gy9KY6BF9lJskLuuakDTQHqjrTb5Czm%2BdM48v4trghMaN3HqGV5Hf9Lxi00bRcDTeR5343QyLeAZ57CK4OgO6IoOJmuJldTzZUkP9lo2%2FO6msaGG0osX3CFUXubZzNnClHFjWYkBZWrYbfNO8mcFDC%2F7CEUduriLPoylhZuQ4orsECCXjXv9lfmgYJK50EO8JaGBLZvbPFauudzZU%2Bf%2Bfan3wdcDMnDUEMH7od78VtpICLGGStybtk%2BfBWDYKdK%2FNckorxAHI2pRA5Hj5%2B9qq2Ks939vALrzPgktrcbu%2Be%2BU0HrbYEeYwNqnEC4qxzl4w%2B5DnvAY6pgH5zZvGwN38ekBU7UDtdrgkwlJ49o4xaQoJY4Qoe9aAM4z49p%2B4xVKSuMH9GRL3%2FkOQOfFDl%2BG4mcd5gswt0aBPQBYvJKPKWOhIS3TNUa7QssMZzDWcH5hjK5RORsUVpBmUgyeJCu2zKEDW1qRACNMt9yaOSZcD%2Fvdufj5ypZ2aWWE6fS3W2Eu2rRteqpHdCLXyyCjHT%2FKfIkZlQ6%2FGNGwp1EhWHZnK&X-Amz-Signature=e69508b1944ac40ba010c09069d85e26c196577ac8fc1515f4c0736108d84f46&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4B5UJWH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGY1kMAbtsoyv8ZN69NdqYv3viXVgTP4o5uqxqSNnYpuAiAHH%2BSOEVpzmKwcT%2BIcYKSdMR8v0AsaE0MO7swnqBGXvSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9Z08PssgEBIcNj8bKtwDKzm0L660QIihKfLZpZrc49Tx5zvFptpeHBNeOvkozWjIyLRF2v1FCTJYwq8enqI%2BmvoTCCn0KTktMSVfsQzGEZl%2FiTIaj2qxCRI1oc7xQ6Ajfew8jD1x2KPLOlLMFABZIms%2FpzEVt2Sb%2BjlLTAUlerDVQcMI262tHcb6AmQFkusXrvqVPtgdUBs6V2mSAKSAHcroV82pjXqNKyKxm%2BNy5fTu6Mae4NSv%2FV%2FdSWXe8VEjHZ0Xm%2B1o3%2B0HxjB3IOjLQca10WQCKZ8cJEv6p0tiVfa7Y%2BNPBtpWszAowzriQswacwZQ9ZbPVUm%2BxB0Gy9KY6BF9lJskLuuakDTQHqjrTb5Czm%2BdM48v4trghMaN3HqGV5Hf9Lxi00bRcDTeR5343QyLeAZ57CK4OgO6IoOJmuJldTzZUkP9lo2%2FO6msaGG0osX3CFUXubZzNnClHFjWYkBZWrYbfNO8mcFDC%2F7CEUduriLPoylhZuQ4orsECCXjXv9lfmgYJK50EO8JaGBLZvbPFauudzZU%2Bf%2Bfan3wdcDMnDUEMH7od78VtpICLGGStybtk%2BfBWDYKdK%2FNckorxAHI2pRA5Hj5%2B9qq2Ks939vALrzPgktrcbu%2Be%2BU0HrbYEeYwNqnEC4qxzl4w%2B5DnvAY6pgH5zZvGwN38ekBU7UDtdrgkwlJ49o4xaQoJY4Qoe9aAM4z49p%2B4xVKSuMH9GRL3%2FkOQOfFDl%2BG4mcd5gswt0aBPQBYvJKPKWOhIS3TNUa7QssMZzDWcH5hjK5RORsUVpBmUgyeJCu2zKEDW1qRACNMt9yaOSZcD%2Fvdufj5ypZ2aWWE6fS3W2Eu2rRteqpHdCLXyyCjHT%2FKfIkZlQ6%2FGNGwp1EhWHZnK&X-Amz-Signature=3e87fb923139038cf3ae7a0da68dd591c30afafd3ca48c1640cd4483d55bc57a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4B5UJWH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGY1kMAbtsoyv8ZN69NdqYv3viXVgTP4o5uqxqSNnYpuAiAHH%2BSOEVpzmKwcT%2BIcYKSdMR8v0AsaE0MO7swnqBGXvSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9Z08PssgEBIcNj8bKtwDKzm0L660QIihKfLZpZrc49Tx5zvFptpeHBNeOvkozWjIyLRF2v1FCTJYwq8enqI%2BmvoTCCn0KTktMSVfsQzGEZl%2FiTIaj2qxCRI1oc7xQ6Ajfew8jD1x2KPLOlLMFABZIms%2FpzEVt2Sb%2BjlLTAUlerDVQcMI262tHcb6AmQFkusXrvqVPtgdUBs6V2mSAKSAHcroV82pjXqNKyKxm%2BNy5fTu6Mae4NSv%2FV%2FdSWXe8VEjHZ0Xm%2B1o3%2B0HxjB3IOjLQca10WQCKZ8cJEv6p0tiVfa7Y%2BNPBtpWszAowzriQswacwZQ9ZbPVUm%2BxB0Gy9KY6BF9lJskLuuakDTQHqjrTb5Czm%2BdM48v4trghMaN3HqGV5Hf9Lxi00bRcDTeR5343QyLeAZ57CK4OgO6IoOJmuJldTzZUkP9lo2%2FO6msaGG0osX3CFUXubZzNnClHFjWYkBZWrYbfNO8mcFDC%2F7CEUduriLPoylhZuQ4orsECCXjXv9lfmgYJK50EO8JaGBLZvbPFauudzZU%2Bf%2Bfan3wdcDMnDUEMH7od78VtpICLGGStybtk%2BfBWDYKdK%2FNckorxAHI2pRA5Hj5%2B9qq2Ks939vALrzPgktrcbu%2Be%2BU0HrbYEeYwNqnEC4qxzl4w%2B5DnvAY6pgH5zZvGwN38ekBU7UDtdrgkwlJ49o4xaQoJY4Qoe9aAM4z49p%2B4xVKSuMH9GRL3%2FkOQOfFDl%2BG4mcd5gswt0aBPQBYvJKPKWOhIS3TNUa7QssMZzDWcH5hjK5RORsUVpBmUgyeJCu2zKEDW1qRACNMt9yaOSZcD%2Fvdufj5ypZ2aWWE6fS3W2Eu2rRteqpHdCLXyyCjHT%2FKfIkZlQ6%2FGNGwp1EhWHZnK&X-Amz-Signature=9dfa16b68ee6d1b7888f8550959f2b4983607d0e0330ef4e1a0ad793d27f9674&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=a91a2f86dff4418320ac828e0f62a452f9eb0fa388e0229f41fb5c8bf5a7b562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=32e35496b5b5d499becab34d634dd3891eb2324c5d9be515924f6e722f194076&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=7374154366aea05a808b680d5278b90d7a0d6b812b3f8bf29b8e2af0926c93fc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=7fb8bb9f3144ae69c01f589d46e71557c078f3485acaf3e0e791265e293167e8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=a9fc7e7f94210b089bba80b2d4f07c9fb94d278be45240b2f900021e8c5dff4e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF4NG3QM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIDeL%2BPO7l5Ra3CdK8c9aaS9dXbfIGher3TBTkLNi4oloAiEA1%2FMwqpUj1WMmBq%2B8PMiVHJm8wTXx9OLVdDAV4unZsioqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFP8F2djl3%2BC8te34SrcAzSY3jifS2%2Bp7WrnhXuKe14eHAwlgLBYxER5437PSSFjk9yRhH4gGp1Zy4jyIpCbC8t6JOl9ewklQV5RTPfh296Wfp2O9XzBiY9OiDX6fyJEbUG%2BIAO7NFBOqF45YqPsxw7Y3r1V%2FYLu7P1rKjGjpWPnS%2B0gNP%2B8RDNvIm1l0%2FBSx6Am676%2Fe4fdLjghuDXNmKz6yteIQVqgR7OM7RgXHUjrNAEoAuS2wVRo472hsEa87nvyMEU3UyCIWfET%2BPubJJQ6vNW4%2F6wtqFFDmKX%2FIcc2MfMQffbyP2Jl563Ig2vK5QpzMzxXfEYh1M7bynFIOpZcwC9xOhq%2F3NQubgWe8A5QKcXhzDAUfg2B5nTko%2BvtRwNe9%2FenrtVhq4bE6%2FPnkP8hCV%2FgnSKPh5oDFFKYFWyXH4UpGxeELR6UBTfXr0ezf4W6Ll6Wo1z%2FuCR89UhrTHxihuO%2FYgwhCAZZMQHBHWUSfvbpxo3PAQlC3iDKy5mjE9tPCQe6PXbSV%2BHtVUZFsqdWN0CQIEAlU4KJKuRO%2BRBrWCr7FPt5MkpkBwWitQ7fJmbztYMroddmk3ua%2BqvYCEOo4wHa6QLtEkSCoX8%2F7P6TmV4guKz3rIlM%2FBQaGkKeWlbOWms1fl7Jb%2BChMNSQ57wGOqUBOXfu0CHHJfIjn91SGqJA%2BtsIuBEl0Wy1pqQ2JhfHAE%2Bv0opT4%2BRevstaHQR1JcadEKDlWZDTdf5Iz4iYCwet5%2BxcObi7MKOEEEdVsQkwuOQEx9dAr2NcFKmgjjbA5goV5RqnHdT1IHQFXGv1IO7gaRRaB2ezcz4033%2BH82vbUUsvaBRjWh0qum%2FL6aqBJ8yu%2ByYoaautfh3UJ7AroOf%2F7WoMNf8x&X-Amz-Signature=5cc2af913868cd014def73b555900815d0750455cfc32bc0cd0be4f5c64072ec&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZDOFTA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCESUN1HwNUQNbhxArUiiU%2Bcx7KxJRDA%2FNhR5YOOkNbwAIge2%2FuUdy3XWiCVDygcMcMLJ2PiTxAhyPH9FR6%2F6%2Fju3IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImNY8faSyZdtf%2BZFircA%2Bfd%2Bq%2BEceBGrnKjYOX8%2FQq4gHuQgjmeOY1zaer4gDtiimtD9mSF87nlSVB54GHiHxNibN4Y%2Fr1aRwoRubt%2FMHPJxVtnmVMcNPkbUHx2XrJVlTp9dxKVU8h1T0wm9vBnKpYpQySSbACgjOntnvb2zOrA7y1K%2FZM9jtkNSkhHRUezoD0raK%2BwGRj4Ib284gAytwls1nugie3BsHe%2FGUcDNfWztgzT6jggENbiSJDcfV1BRQ3kc6lwmvA8PDjSHhOeoKdWBEqfMLMIKkDb5ni%2B7NbojILex4K735XL6esmk7t2O2JfUelgdC9f3PGcVuRNFzHsYrHDcKVJNgx6dlav5mFYdh3YnBNwtoDu3xxcwhwVP4fUcbAXBUgHte89VbD0YAnBFBIyWT5U25KcHYw6I%2F7lzfw5gMmE5rDdOGkmCHTmxnOlPEmuTVqNCP%2F3H4OkvOqtdCkzmmo22f65XrAvIbaqJuUF6l2cRd0vxVldnkyhQ2XyJKDdmJ0%2FvPXbGTxuIKGtW9B%2BycTEUYTQTTT69htlW6MCLnrHn6VE7YH36Hzut7EzkyQP8hn4JBsKK9hJ7ueFv6bgHLhDQKrr0JoULVX%2FuUgEb15aN8yvzRcohQuZdjRBRjISObXpzB1dMMmQ57wGOqUBshBFqwGYyQ8UVDz7nTFAGw7IJoyRzdeabJG7y%2BOClDUfRPGfUSyKMCWNLUUnjiFpgLWqR5ptC5gCmAl6Jo37RzqrO9r73RFfonKTcFA%2FCnHqjoKKHCwrqQ1%2BDN0mEXEeFJLs4AKverMU4%2BG97kUGpuXCfDwRqc%2FJaQakM482leYdgSNeD8SybHKAVb7QSJe9CYcPbGKiCKPd9IhxDOdQB1%2ByJ8LZ&X-Amz-Signature=44cd235f298e4f1b44403152b7ca37ddc29b7396169bde7af7b0aecf7c2c59c2&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZDOFTA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCESUN1HwNUQNbhxArUiiU%2Bcx7KxJRDA%2FNhR5YOOkNbwAIge2%2FuUdy3XWiCVDygcMcMLJ2PiTxAhyPH9FR6%2F6%2Fju3IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImNY8faSyZdtf%2BZFircA%2Bfd%2Bq%2BEceBGrnKjYOX8%2FQq4gHuQgjmeOY1zaer4gDtiimtD9mSF87nlSVB54GHiHxNibN4Y%2Fr1aRwoRubt%2FMHPJxVtnmVMcNPkbUHx2XrJVlTp9dxKVU8h1T0wm9vBnKpYpQySSbACgjOntnvb2zOrA7y1K%2FZM9jtkNSkhHRUezoD0raK%2BwGRj4Ib284gAytwls1nugie3BsHe%2FGUcDNfWztgzT6jggENbiSJDcfV1BRQ3kc6lwmvA8PDjSHhOeoKdWBEqfMLMIKkDb5ni%2B7NbojILex4K735XL6esmk7t2O2JfUelgdC9f3PGcVuRNFzHsYrHDcKVJNgx6dlav5mFYdh3YnBNwtoDu3xxcwhwVP4fUcbAXBUgHte89VbD0YAnBFBIyWT5U25KcHYw6I%2F7lzfw5gMmE5rDdOGkmCHTmxnOlPEmuTVqNCP%2F3H4OkvOqtdCkzmmo22f65XrAvIbaqJuUF6l2cRd0vxVldnkyhQ2XyJKDdmJ0%2FvPXbGTxuIKGtW9B%2BycTEUYTQTTT69htlW6MCLnrHn6VE7YH36Hzut7EzkyQP8hn4JBsKK9hJ7ueFv6bgHLhDQKrr0JoULVX%2FuUgEb15aN8yvzRcohQuZdjRBRjISObXpzB1dMMmQ57wGOqUBshBFqwGYyQ8UVDz7nTFAGw7IJoyRzdeabJG7y%2BOClDUfRPGfUSyKMCWNLUUnjiFpgLWqR5ptC5gCmAl6Jo37RzqrO9r73RFfonKTcFA%2FCnHqjoKKHCwrqQ1%2BDN0mEXEeFJLs4AKverMU4%2BG97kUGpuXCfDwRqc%2FJaQakM482leYdgSNeD8SybHKAVb7QSJe9CYcPbGKiCKPd9IhxDOdQB1%2ByJ8LZ&X-Amz-Signature=4db5e2f7e35a6d8c32e9fb76e1bc046ef05be68de06791fee233de92314cf4c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q63HVGUL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIB1z1glxcYpzvVIbmkWxNNe4DCa%2FcCcYL9ChiBbHH%2Fe7AiEAu7M95OO%2BcQenw3LpyzlGaB1BKu17dUKbQGHfTtaz8wcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPo0AHAYZ4zw3T4R%2FyrcA7ZYEqDHNCQxfVE%2FPU62sH1EmRWbr1yc9e2LYKBFf6QWcKOh997%2B8eYLZ8EQZ9XiS7nTWXHUw1XX9nU%2B5oGTXCJ%2Ff5OCS42gtltTmEBJI7kUbbuQ0xp1uw4XUY40ipLj%2B%2Fgvz5nYFWhZEfo8NC%2BDcV6%2BxIA6tq%2FVJ8pQhSlJviqZVIN%2F9BE5f0inJwSX4R%2B3Mhdh8Q0nvceh4FmwJxu%2Fq4bn%2FyLMEhas3FkKsYFMfOde8L%2FftJsXeU3AICDfc1TzD23likXla%2B8bC49U5HGHUsO%2FISAotVole6WJPc0NSPmOocNopyC82BgKNbabX3HmpblA4%2FvwZagzOHJ63LShxDv%2FoSBaXiMgz6Ia85lZyIFXFMcH2HXFVZRw5fsAXNkrcKQ7IPNUQ9Nv1cy60sEVh3viwJPX1CB4lt03HUlO0yZQKskPx%2FgHPOYUM0WlsCYjx%2Fm5sV1o9LMMOUHL6ZlU%2BTgJ%2Fp5w4Vg21QWoY6DXWMpeVFYNoExx%2BQ07ndl1WGiehhr8yGYzQECBV5yjcM1RMIdm%2BHh4Ji6zXdvUFJqLse8QhBGZyJ%2BURgsfs1%2FTbvbKgrYCrS7uTa9v0%2BDJsQBCDob4vs0ZvgZ%2B4aSoKXZjDENXiA5DUlp%2Bj2tWPDuPMPqP57wGOqUBwNz3TMSCff54TqmIkI%2F%2B%2FsfLt7Oehjag%2BedbTznjw7tZLXs6KQ6BECRHGHaiAjeGaTBlQpY4eNJfN23%2B8rSWwS13PN8C11l%2BF7WT7mG839a5fWfFr%2FEGFPbq6%2Fm7BYbM%2FKeLGD2zXGfeb0dEgT0JpLlNbeX64pQStJdQkbLslyOXZ7lgt4gMH1dxyWSLtMUPradmZEUrBZtsuhz8IwB%2B0bMCwyf%2F&X-Amz-Signature=c1c2c200746a2991f6e00875f6c133f23faec9da126582e79f6e531876317fdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBL3U6WC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCRBAdT5nX3sByIfMFHGDLumEMYRrgn8kQz902Glc4nKgIgdlz0jSJskwbwcA2E8IkmmiLSvTBYeSBm2695KyE6V%2BcqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXCmp40XDxlyWVTLircA0SkNGuAzcu%2Bqi3crEF%2BNPevfXdDPhj3%2F%2Fa2RxrcllNCzjRb1TQbuiuwoPpK0Hd5XM6pwjptnbUmYxaOAa1yJdWSJDx8E68MbteSS5x0iOYs2jca%2F9z4cdF8KqcWSK7ErVt9SkG5vpCghVakAg9Zn%2BdzgPga3LYQ00%2F9rMfj2qiFdK80Ka8phLr1mLlBC4Bugle0eMxcECMRgXwWiQmv4tdivwqKj5Ii8jqAl%2BhgeZqXkkMt0yPbcGOHgJBHnoGSAGCuIhjl8lRBa5fhBoJjPbvQCDtShpQnV3lrHTivU4wXnvUlgcdDZ1ekoRkwgw3MjbTWd9W4jVbTuHoWK98SkQ3ureyNIcwYDWG1nV3vb4gCJVmSkZRo615ex3jlgvhR8LICDm%2BToE2N6Ar4UBNUU7fiG456d7lMRLucPawbwmiNG%2FB8RPDQdfZxkVPN4k0RHzqczW2vm3rxXSYd%2Fa73n2aVjhkYuqQZZaiNpueSCf8R7%2FVu89%2BqCu5NfOWW5qeqIqXcT5NRomNXYkvWJqTtzraQrp0vhJJw6jjFwQzbtQK0arZE7YjL6yapuIOZcGRwSQUtofhLW8d5XKR2EZSKTIriCUNWonbZIMP1DgzOxeWS2fo6awIfJm%2BBNnsrMNiQ57wGOqUBtnawjy96fGcpJ2V%2FLm%2F86mI3wEnTrs1cM2pWfsDFKy%2BBVv8HNfdVtZDTCpYeL5CG8LKOl%2FEcdFprmFLUHzuayp6kfS%2BZHQ9SGZsmct%2FGZz2%2B7XwUdYhLQc7SQsaKeXIVECf%2FvU%2BIoiGFoO3pe0zlmAqUsIs7KkbHsLH9Ww5PDbmKWN4p9Ac2ZpBjavTqSmJtZKnyu698GFY27VF54HGeEYKbmuRQ&X-Amz-Signature=1ee03c7152ee5d47bbc698f170d043b663694da2cef6e30862795a74503fef87&X-Amz-SignedHeaders=host&x-id=GetObject)
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