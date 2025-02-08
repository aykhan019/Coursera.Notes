

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=427078e6af9acd08f6724f5df38a44653b2bd161f833586c7c7baa98efa555ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=d5ade36fe089577c6f1e055521714a4a9e524e25cc4a02042192b5714c4da250&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=e4672cc9411e1ac144f0512535e5830f04eef622e81269d1359399a0138b45ac&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=882e51e94dac19e483e4caf820a86e2d69d75a54a0fa2e7bd965bc90384cfe38&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=800115b51ce36361e501e975c4ae804453e01b45b610a8efaefa84cca1d23df4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=580caea4a2f1905faac084816551873f5c45e708a787687aaed671be6827a46c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=13a9f7c8f8655f779e1a3823d1de44cc1d0abd0502336f2d8d1d33c9abab5995&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=40fd7a9728a51b3444372f02a7e5c40299d38a140c66e9934d119cb6c06b7d68&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=a4caffb534027fdd3cc8d7de964a810183ef20992bc4b7c784d67d901f1c33d3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626TYJTSF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE9svmlnv1Y6PtA1EnlRM5eyRpCQgern2cOrrKum5HrkAiAoYj%2BGZf9Hyx5EFgi7eFBpAjX3zdTOoSM2q5bw8LT%2BGSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNccGRqqsMaLXX%2BPoKtwDi7wmICYrZ2%2FtNOOMDl%2FUhfu7CZdm7QriB7ma%2FNSxsbaQYPFQVFWamXNJtxWZlbx0FfMzxYftq1EGNL8tVOk0QCl29TJHzYWOuTnHa4513nqEaDafbaC7oDrG4fPPg8FEtgRZPkFn%2B5tMDJzE6Ck1pe9YLlIDO%2FCVaEC0TpDLDNru2ulVOUDWsYSOBZqciq3Iz5USUSw9CsHYb4%2BVEAJMhpLhcCsWSTiSgdzlVrer2jM5igmSTlgmd4l4m4s%2FuYxATcWWVOwiW4RRYqmOZ%2FE39SmLoJE6sp8G2fU9gRWTW%2BzxLm%2BueRktMZCPe3bhKi0y%2FMA8uCFreGUz4ntyC3A6noM%2F8iNNnqHGe%2FGljaX8Hudm7AbkuRZZFbe3b7Rm1yHh76UJIO%2BJ8XlnLZkxxr4JKPb7em6IUWpeVloFlsDBseQH3whFzM2rPBk8VunJL3lyZCEmH4L4%2BlAFtTT12eDBZ8Vfws7KNwwjWf7peessqMXHtrufsezHR9%2BO7diBGAGx9%2BVIOGNE0Auzuv5eOsaCzyoLlKYYdTde8FQkH3egpE1Seu6i7yEdIHl0biA%2Flbt61jSAnIbtfwQ9G4fLDreDxRoTSYGxgSU6VQhwX3FNbYt28bSQU7ecFgV9%2FKAwq%2B%2BbvQY6pgG%2BvFvc8kR%2BV7%2FzM4d7mZHKh78RlHwmd6AfXxFqQEXJKiF3X2hLJusQDi6kp1gcbdy2Ah48y4niCtA94IHV5D3zZ%2FccARHXsIur15DUw4j9qSyP19UVj1Sfl59nHfT7miO5prZSAvrVhL1A5tP38mfWypoWOcI7EGAJRLpouYhoBmECzf8wq6dt%2BeP6tQkaePk5dg4HbxD0FxdZ15BbV%2Bu7fc3oCwMD&X-Amz-Signature=c3e206b79716d17888746aa609001de3c7991a6d5f101db4cbbad1a5a107f138&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626TYJTSF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE9svmlnv1Y6PtA1EnlRM5eyRpCQgern2cOrrKum5HrkAiAoYj%2BGZf9Hyx5EFgi7eFBpAjX3zdTOoSM2q5bw8LT%2BGSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNccGRqqsMaLXX%2BPoKtwDi7wmICYrZ2%2FtNOOMDl%2FUhfu7CZdm7QriB7ma%2FNSxsbaQYPFQVFWamXNJtxWZlbx0FfMzxYftq1EGNL8tVOk0QCl29TJHzYWOuTnHa4513nqEaDafbaC7oDrG4fPPg8FEtgRZPkFn%2B5tMDJzE6Ck1pe9YLlIDO%2FCVaEC0TpDLDNru2ulVOUDWsYSOBZqciq3Iz5USUSw9CsHYb4%2BVEAJMhpLhcCsWSTiSgdzlVrer2jM5igmSTlgmd4l4m4s%2FuYxATcWWVOwiW4RRYqmOZ%2FE39SmLoJE6sp8G2fU9gRWTW%2BzxLm%2BueRktMZCPe3bhKi0y%2FMA8uCFreGUz4ntyC3A6noM%2F8iNNnqHGe%2FGljaX8Hudm7AbkuRZZFbe3b7Rm1yHh76UJIO%2BJ8XlnLZkxxr4JKPb7em6IUWpeVloFlsDBseQH3whFzM2rPBk8VunJL3lyZCEmH4L4%2BlAFtTT12eDBZ8Vfws7KNwwjWf7peessqMXHtrufsezHR9%2BO7diBGAGx9%2BVIOGNE0Auzuv5eOsaCzyoLlKYYdTde8FQkH3egpE1Seu6i7yEdIHl0biA%2Flbt61jSAnIbtfwQ9G4fLDreDxRoTSYGxgSU6VQhwX3FNbYt28bSQU7ecFgV9%2FKAwq%2B%2BbvQY6pgG%2BvFvc8kR%2BV7%2FzM4d7mZHKh78RlHwmd6AfXxFqQEXJKiF3X2hLJusQDi6kp1gcbdy2Ah48y4niCtA94IHV5D3zZ%2FccARHXsIur15DUw4j9qSyP19UVj1Sfl59nHfT7miO5prZSAvrVhL1A5tP38mfWypoWOcI7EGAJRLpouYhoBmECzf8wq6dt%2BeP6tQkaePk5dg4HbxD0FxdZ15BbV%2Bu7fc3oCwMD&X-Amz-Signature=e7888f66a03afcb500ba9f03f23704ed362af8e065d705a62b8cdbc3bcfb260d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626TYJTSF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE9svmlnv1Y6PtA1EnlRM5eyRpCQgern2cOrrKum5HrkAiAoYj%2BGZf9Hyx5EFgi7eFBpAjX3zdTOoSM2q5bw8LT%2BGSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNccGRqqsMaLXX%2BPoKtwDi7wmICYrZ2%2FtNOOMDl%2FUhfu7CZdm7QriB7ma%2FNSxsbaQYPFQVFWamXNJtxWZlbx0FfMzxYftq1EGNL8tVOk0QCl29TJHzYWOuTnHa4513nqEaDafbaC7oDrG4fPPg8FEtgRZPkFn%2B5tMDJzE6Ck1pe9YLlIDO%2FCVaEC0TpDLDNru2ulVOUDWsYSOBZqciq3Iz5USUSw9CsHYb4%2BVEAJMhpLhcCsWSTiSgdzlVrer2jM5igmSTlgmd4l4m4s%2FuYxATcWWVOwiW4RRYqmOZ%2FE39SmLoJE6sp8G2fU9gRWTW%2BzxLm%2BueRktMZCPe3bhKi0y%2FMA8uCFreGUz4ntyC3A6noM%2F8iNNnqHGe%2FGljaX8Hudm7AbkuRZZFbe3b7Rm1yHh76UJIO%2BJ8XlnLZkxxr4JKPb7em6IUWpeVloFlsDBseQH3whFzM2rPBk8VunJL3lyZCEmH4L4%2BlAFtTT12eDBZ8Vfws7KNwwjWf7peessqMXHtrufsezHR9%2BO7diBGAGx9%2BVIOGNE0Auzuv5eOsaCzyoLlKYYdTde8FQkH3egpE1Seu6i7yEdIHl0biA%2Flbt61jSAnIbtfwQ9G4fLDreDxRoTSYGxgSU6VQhwX3FNbYt28bSQU7ecFgV9%2FKAwq%2B%2BbvQY6pgG%2BvFvc8kR%2BV7%2FzM4d7mZHKh78RlHwmd6AfXxFqQEXJKiF3X2hLJusQDi6kp1gcbdy2Ah48y4niCtA94IHV5D3zZ%2FccARHXsIur15DUw4j9qSyP19UVj1Sfl59nHfT7miO5prZSAvrVhL1A5tP38mfWypoWOcI7EGAJRLpouYhoBmECzf8wq6dt%2BeP6tQkaePk5dg4HbxD0FxdZ15BbV%2Bu7fc3oCwMD&X-Amz-Signature=9acf9ad6df9496bfb1d8e30360bf989c857c1489d72865bfb7eba4c9a3a4c797&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=0e081c577a4367aa66550b1fd2a53e3589c80a17635e1cfb80db4ee7638a4d5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=714c5a25386a78ac50a6f4b813ec7bf3cd2fe26d85df1e2d5a19dafa2ac1f0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=06360242d175366ae0460bebdcff25087ebc55cba5550f8c457a5437bff8c713&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=1b91af1e27e7e1383c30b5803c40773fdb56234fba6956fbee7a28cac9a88339&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=a0daa5ab23f94f3f614aa119568217ab245b884036e16882fb65178d90144f04&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4O4MB5B%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCID7oHPHH0r%2FpGZPGRWS8DGPPFiMHix%2FsWE6mOdoovP%2FJAiBAsKU7%2BVVHYE6Xz3iccVpzwkT6UYbcWRS%2BD92OMMtiCiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2Iv2Tq%2F%2BaiSZJ8lKtwDZ6SLLVFqKsRGjMmMzCQie04UladG6weximqs82Ys3aR911wwTvm1U0WXSwR%2FDNcGWPIGtFzEEq9yNJaH6H307a1LU3ZkTa622Wq9AXlT2kOTYMny226I%2BD%2F1Ah3NIASJBqfvjEnJT4xKOL5CDRGKLFaLKO3Qcmzl%2F5eWgsqQYug7D6TiWHsAP5ZWCu0y2tUagZbc5V8UaNCXnrJUQPFnX3D7plrXZLmwCbAgV1xUD1w%2BPzsllPc6Pn8r%2BY6zl7GxZxELRfEE%2FCiStqRBMs9Umwz4opYBOlLV2HEvVKyLbTuXyodRapl%2Byrk5In%2BIPLJja9zcSOPeAonfatDsUTbOowSPtWOjSHjcrTx1cv9gcffxxzszQ93UDuL%2BsHCIfr9k1ULtipNWXq1JoIaw%2FKKVYYDDMwsE7sl8M4vK8N6DOW7FdUwStf4JGv%2FydbjzCNV5uxal4W1rTNm60xo0zWaeay0O8JCCkT%2BwJiVYjAns1uLm1QjuSNbgygFpYqczQr9avwrl0caGp02n4p3b9Zq7NJq87FC%2BYmb8bsvP5IRjFkP%2FCUXNEFp96EAjOIxV3KUAvcv2eUi015UMr8n3LLsQIZpdJAlGezwgsfcdaD4hpvuIFByyI%2BMuc8FlKWEwwu%2BbvQY6pgGV9Q5tSCbb%2FzwgIRyqHUF65a3xsC5Q8dfDXuTwVDkWmpAGXvFhCWtNYI5iM2AvUMkPqLZjr7dTJqmIF2Kbj6u%2Bm1jxok3GvJJex7Vjp5XKGSuvVGg67Mu%2FDkNjuEaSf4Ub6vj0kAf2ZFSDGlDyxk1cifGxRuUXPv8QPzvbb4eeLf5bKoQZHte2j%2F8zvOqfYF7jQmYAhAVpFcE5EDmZEG4Vcg44uw0t&X-Amz-Signature=6dc4f34750bde7ac6b79c756388f5bd4ccbae0dff83e37d5a6ad4138ceb0d2fd&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XVBIBF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIBz3BfwJmuJm3BvkBujnHcitCdk6GonlOQk9cbX1O9GvAiBPntFwkfACM2d1THRqIOGGzXvr8ZgyHXl6xOkz2EXasSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwsWXApMoVanbD16wKtwDsAlQp5siok1ZHLB6%2FDUPPtlRELhfyHDRFO%2FLU%2BNTBH%2B7G7hGUBelTbsMPhADEFLnuXhhDpezB8KuXPOWleZM3ABR5CZyZ4ppDYPFfufWbMH%2B12Lxpx44dpvcJjd6vSxLoIJpl2CmN4tZ0Mi17%2FZ0lSdje05U44x52D0JzqjfXliIVcAUsS5sGZ0uFw73COlZd4CxIOzUVz0u5bKU8tox0II6C9vCOqe%2F5P8pXRXlddHHz7YpO69SN9KmAjV%2BDgrx%2FvjP8bPReod9jhGgEV1ZmrmfqHsjEOy0W%2B7wfYgEaqPCwva22JmDBBjWmyQNtYKITrb1B897puscmD0CyXqKqmFKc6rs%2BChBgxfUuD3bYMlrJ9XE1t2OYXp8rmwNX%2F7pUHyCPHue9AP%2FYZl7cZ1nuz3leG94GQXNl%2B%2FXb4QqEQaoHDMhuOwIxOgFYTh9JGfjW70VeM4V3UWvS3SWxmqC1U0ND5GvNCB%2FlagmonzOVVo5OG2G84n6MzugJzN15Ajg4zf1qab6rGByTbx%2BKA9tT%2BPgZ71YAakccBQpSvhax6LWiB7hli%2FIQLOAqQ1P3qxy2315UQBbYUOGpeZpIbou4AqofHDvL6H3a4C61nx1D1VVcRjQam5cPB2SHCswj%2B%2BbvQY6pgGNwbfKnLzN5Bkg1RxCMnefeVGU16pC6Aw3Y0jBOGKClqjdx3uqMX2Nq%2BazRjhyUHSm0bjdvD4b2qhj0BHsiouthb0meUbCLh%2FsvAZU5JSKerMzpXq96KiD%2BgosAmyIRpEb%2F%2FL%2BwvCx81T9heVidPkeGXm1HCx%2BaD6XKoeTTGMo5PNRKEyBlHPC30qQpi62E5jO1xwPb51hTaWYGILGNeQPJfOlrlEl&X-Amz-Signature=3f6c378f2448eae78b643476497fcf892d7ba0c35c1daa92a7982965e8248236&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XVBIBF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIBz3BfwJmuJm3BvkBujnHcitCdk6GonlOQk9cbX1O9GvAiBPntFwkfACM2d1THRqIOGGzXvr8ZgyHXl6xOkz2EXasSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwsWXApMoVanbD16wKtwDsAlQp5siok1ZHLB6%2FDUPPtlRELhfyHDRFO%2FLU%2BNTBH%2B7G7hGUBelTbsMPhADEFLnuXhhDpezB8KuXPOWleZM3ABR5CZyZ4ppDYPFfufWbMH%2B12Lxpx44dpvcJjd6vSxLoIJpl2CmN4tZ0Mi17%2FZ0lSdje05U44x52D0JzqjfXliIVcAUsS5sGZ0uFw73COlZd4CxIOzUVz0u5bKU8tox0II6C9vCOqe%2F5P8pXRXlddHHz7YpO69SN9KmAjV%2BDgrx%2FvjP8bPReod9jhGgEV1ZmrmfqHsjEOy0W%2B7wfYgEaqPCwva22JmDBBjWmyQNtYKITrb1B897puscmD0CyXqKqmFKc6rs%2BChBgxfUuD3bYMlrJ9XE1t2OYXp8rmwNX%2F7pUHyCPHue9AP%2FYZl7cZ1nuz3leG94GQXNl%2B%2FXb4QqEQaoHDMhuOwIxOgFYTh9JGfjW70VeM4V3UWvS3SWxmqC1U0ND5GvNCB%2FlagmonzOVVo5OG2G84n6MzugJzN15Ajg4zf1qab6rGByTbx%2BKA9tT%2BPgZ71YAakccBQpSvhax6LWiB7hli%2FIQLOAqQ1P3qxy2315UQBbYUOGpeZpIbou4AqofHDvL6H3a4C61nx1D1VVcRjQam5cPB2SHCswj%2B%2BbvQY6pgGNwbfKnLzN5Bkg1RxCMnefeVGU16pC6Aw3Y0jBOGKClqjdx3uqMX2Nq%2BazRjhyUHSm0bjdvD4b2qhj0BHsiouthb0meUbCLh%2FsvAZU5JSKerMzpXq96KiD%2BgosAmyIRpEb%2F%2FL%2BwvCx81T9heVidPkeGXm1HCx%2BaD6XKoeTTGMo5PNRKEyBlHPC30qQpi62E5jO1xwPb51hTaWYGILGNeQPJfOlrlEl&X-Amz-Signature=ac7817c648a7a795268135bc379a1180786ff1f9b9a770985558350f44f4cacb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJBUKGES%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCBtDAoUIV9Yrr64uDb7VRnd5tE8F2qCDGLCevLAAecLQIhAIuIt8%2F0xL%2B%2Bp53aCba2sn%2BsY1IEg3xiW6f%2Bok7z4w3mKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7y9gEG%2BYxT1y0dJgq3AO9d1sMmn1TJew2E%2Bye6ukfjmOswzzKxekLqPaIckTa4ZZr5lS%2FWrYW7tNFQZ4F2iBWBhJNcnT0gktvA0lQxo6lXytBoz52YqD9q%2B57Nf8Kjk8yaasBtAX%2BX99Ya9j7OIGXWN4ZzHub0YcJwtDNS4pVzmzxH6nLnaixhfavDlxg15zaTLldJItamMhyTKNsJtFQ%2BRhbCU0Qvz2KF%2BGTGIZLGqzrD7QvvBitMycaXy6wnM28WiKM4IHNZ0L%2FRY2HeTAkNe0LBqVmVOVjmK5gJvkLnAl5CT55qFuQD5h2Zyhp2bLSG2dRIaQEiXp9K9F7wssOehoBAZ%2FJIVafndO23124nz5VSIzUvz7pMLPIqP8SCJEXTlgRdltabjwayfrIg%2FpTZM4kUNn4NmHjPHVpdFj3LN%2BLCtOwdjadcYO0BczEw%2BHDIb7nQ07ux7%2BBeDfvT9HpzNvzysTRjhH1ALzEwODkAEwqUhjQALYx%2BFdwdNmZ%2BMveWbI3Ew4omf308D77FYDupVFYYBAhmcPGnljUFL2P%2FR9LTgJHWaxRGnsyW2TeKKv9DHvW8LDt8IgC%2Fi6GL1aeRptZVt8wU5SJ9iJBdJgl%2BFK20zPCbLMxwZKPyidCSIl41PSb5D%2FwKmi1RTCY75u9BjqkAfTPi45XnUW%2FpmDAm5aH8xblBZ8Fk%2F3jHuXSEhd5lyTuRojXNTx0VreLMwZXtV1r5mSovhiUVWyr9yw1Mv%2FnqnlNs4Czx945ZVlk9WUK8AVyz%2FYGG296RuLY%2FdO1pdqOREfwC3tNbbi5JTMuRd9YgUofr1ph4j9oJCaD7uu5dglpg5cVAHSZ87UfaMEhTsIG6lVhzQ1NEkiJJhZoddAogw2bJsq1&X-Amz-Signature=b3c20ed9626bc0ed4ae23fa7e03b0493820f729e46f4a320e32f63250c35281f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OECC7FP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDCiGxT98Rmc7CW136pdGd9cCFiO%2F8l6cqUGahmFeRiAAiEAzxmUR7Kpe7L7qWLQ2IM6jJA7V9Ig8%2BnQ0puD5AcENs4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH8i2sWokrvtH66Z%2BSrcA1tiHqE7U42S%2F%2FC4mD3pP9V9WwPRjB2TFPxZ8VGxuusyv0r9pd7blRwk%2BIo%2B%2BJ39LdsPhZq9lWfWEQP10oF1IB1HLIaTecnEvhsGzdTmXucmudkF74jhpa6o0HPvLRiZKyQzPPaoDNX5q1EorAHooTmPpEbUUHJbVEH5Qdr74aNOroLIc%2BbdLLlwwJ4HQSsTfanPEOXmntFd1o%2F2BzE%2BhOUURdQOAokkhYtWOKZ1NaVt%2BQsspzrS2F5ciQ%2FboVUwtzWCcOCNDgYhoI4qJNumgZ9r9%2FRpEzXn1Dd1Yw0%2FVGjNJtmcF6TkPZTbHYNkT2W1D8Wkn%2FV7szRz2pHpGBMarEwYHePm8KLmr7OXY%2BVpQASt%2BOj%2BiRUMGDRBxr9ir3mWOtoOx5np99ejc%2BrvbwU6Ap6cAf%2BFvRK%2FLMYvQV43UwTDXFwoaiorLt12nAzy1oREhZykNVJtaDVzSFKgL%2BOppl5QwMO08YNraU1xp%2BovWarzubi%2FhxmfnTIx8VlOPz6x83oCugiKtLlTQ7xb6MIxm5lyfTrmciqILici436DQ3X2%2BKxixh3nvR2bKg5gW4Oq%2BHxjZig7FOtb0vDX4F%2Bu8MT2bWCFlj08lLrTo9MiQ8lY7EeOmAMeu1YfgqThMPDum70GOqUBc73uPbELk4R5yPrIfnWitIg7Y6JQtWXZN5w3wUILrBapHjC5cR431GW%2FqDmevZwlijQRFUUY5wO5%2F7%2FsxHJfGFRnu2pmqv7fEjAB0PBC7EUIiooRjo1KXQQF6FlXKB3gGAt%2BmIM0%2FHJJYUnMGWrLqthf9i81VX4K%2FDH9FjJXhBmndPCo%2BcYrinwgqf1%2FPkYsRxns7BMKbFkvF%2Bwo5zq9A3fFUvHU&X-Amz-Signature=16953fb2cf38c1a174ee624a824f91068cbfd6a268b354b9d5092bd3de9e4dd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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