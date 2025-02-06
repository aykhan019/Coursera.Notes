

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=3f494bed70fef3a47a878b1eb6be8eb5ca2e539bdb118e98fbed2db66dd2a4a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=8c1811030ab0ccaf5ede92aae8e52c9bb61480468f455c4c9bcd8ba361c06aee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=0984b4eb6a33e078e37f03491883987565a478042021029fcc965c148f56618f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=95b735b86fb7dfef95d869e677c1e9c17e1b39c4e7e34755d11219f76686ae47&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=e5fb05d03a035a9385938507f47ed40e051a1f93286c559547e0b3d87a66fa7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=b72bcdcf3273b6ec1bd0236a53863b2940fbe245fa40913e2573683e164f0104&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=98ef0e24dd27f03bb10d03467aaa71728b504572064c753c0d9f8335d40b36c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=8d80d6c459fd286636b23f8b7d7fa27e4b2af85a7b30e2c025145e7c41ed9a8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=a5c419d1cd685a94448adbfe9f0e4f01ccb5825df73fbc7f8c2ae02ffc807c84&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTHJPWUS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDfL3WfWgmx%2BnfF96r%2Fyf3MyGmZjKu6XSpIvQ9d%2FI0nxAiEAgXNUSNJ3WjhSIe1IezXO4cAbRR45nV3wkJNs6FQUIBwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDKcLoVAukcnUTE%2B8WSrcA2a%2BcRzLOAFWzTuPj%2B1N0IpnzK9FJTwYqDb9Jep3ELg8xSXwg6MjX6AjSg1LrWM2%2BxOtjS9%2FTeiiIox2uVIVosyN84XTfgSbmiVSK1gh6j8HwwNPYkQUKWcLKeymUjhA%2FpVFQ0W16XILHqgAr3Cl8Yng00VH6KMCqSzG1biLNF2N7lWD62WKJLGVbjRYas%2FX0Yw1jh5bER9N%2B5N3W%2FvfOnMv0XpuMy83p82BMIJp7n2OU3mBnDZY7oK89k21w%2FnYNb4o8WDIfrNb02KfUPkXQvh1g3WoPyRUsckeny%2B6ZRwc7yjHND6BUmQr%2BYKlJpxmZ0FoZzAZxqP0CWDaLu8NiI5n76%2F%2FoYPb7a%2Fou%2BENnaL9uB3hC40Bk0ExkLY9LQG1OyPdtYx9o2dlMadFQk%2FxurEW2UM0UCJcaTj7ZF5nvfacCU2YqtyhxuRGnazlDInJw3sdp2m3G5tZEORZwKU%2BLu9aPW9Ed4z6RwKogn1aFCLroiNTJNySDlByo6BNcpLS6Ag0Qn43jWUKtGsg1a30efJWmqoOXK6%2BY55HLKxHZcSPShV%2FpR1ZSlyS5O8eDd4WOxCdCdTaQjSe94fR%2BuUX59ZG1J70svpvwQoNnCu68FJimtMir2ddDPfmTcRpMJXEkr0GOqUBBNYlavGThQgr%2FJwqTpjB4joLrJ624P8bDfEnIP1wTVc1SrTO3ElNwbJ8lHZkVURqOXzrIq1AAwgg1%2B3IoOowjKQK4e%2Fb8xJ02ZJJQujEPg8IqrOtuhJrOOjZhFjdN9hd8jKA2%2BlPgui6Ca2ZF04YbkiPnPSSBVE4yqNrvh7BTtihstJbHIbSWigIcCxsutAJD4PzviNCu3PaDoZ16OBSL8zYkw6r&X-Amz-Signature=897452c3fb7f8f705b1a8aa86938e016bce3c622ce1f32fcc5eea6581b703404&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTHJPWUS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDfL3WfWgmx%2BnfF96r%2Fyf3MyGmZjKu6XSpIvQ9d%2FI0nxAiEAgXNUSNJ3WjhSIe1IezXO4cAbRR45nV3wkJNs6FQUIBwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDKcLoVAukcnUTE%2B8WSrcA2a%2BcRzLOAFWzTuPj%2B1N0IpnzK9FJTwYqDb9Jep3ELg8xSXwg6MjX6AjSg1LrWM2%2BxOtjS9%2FTeiiIox2uVIVosyN84XTfgSbmiVSK1gh6j8HwwNPYkQUKWcLKeymUjhA%2FpVFQ0W16XILHqgAr3Cl8Yng00VH6KMCqSzG1biLNF2N7lWD62WKJLGVbjRYas%2FX0Yw1jh5bER9N%2B5N3W%2FvfOnMv0XpuMy83p82BMIJp7n2OU3mBnDZY7oK89k21w%2FnYNb4o8WDIfrNb02KfUPkXQvh1g3WoPyRUsckeny%2B6ZRwc7yjHND6BUmQr%2BYKlJpxmZ0FoZzAZxqP0CWDaLu8NiI5n76%2F%2FoYPb7a%2Fou%2BENnaL9uB3hC40Bk0ExkLY9LQG1OyPdtYx9o2dlMadFQk%2FxurEW2UM0UCJcaTj7ZF5nvfacCU2YqtyhxuRGnazlDInJw3sdp2m3G5tZEORZwKU%2BLu9aPW9Ed4z6RwKogn1aFCLroiNTJNySDlByo6BNcpLS6Ag0Qn43jWUKtGsg1a30efJWmqoOXK6%2BY55HLKxHZcSPShV%2FpR1ZSlyS5O8eDd4WOxCdCdTaQjSe94fR%2BuUX59ZG1J70svpvwQoNnCu68FJimtMir2ddDPfmTcRpMJXEkr0GOqUBBNYlavGThQgr%2FJwqTpjB4joLrJ624P8bDfEnIP1wTVc1SrTO3ElNwbJ8lHZkVURqOXzrIq1AAwgg1%2B3IoOowjKQK4e%2Fb8xJ02ZJJQujEPg8IqrOtuhJrOOjZhFjdN9hd8jKA2%2BlPgui6Ca2ZF04YbkiPnPSSBVE4yqNrvh7BTtihstJbHIbSWigIcCxsutAJD4PzviNCu3PaDoZ16OBSL8zYkw6r&X-Amz-Signature=8a5522544428581302e497fa22333567da4f51715d2f91dd6e90f27a7e78b96a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTHJPWUS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDfL3WfWgmx%2BnfF96r%2Fyf3MyGmZjKu6XSpIvQ9d%2FI0nxAiEAgXNUSNJ3WjhSIe1IezXO4cAbRR45nV3wkJNs6FQUIBwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDKcLoVAukcnUTE%2B8WSrcA2a%2BcRzLOAFWzTuPj%2B1N0IpnzK9FJTwYqDb9Jep3ELg8xSXwg6MjX6AjSg1LrWM2%2BxOtjS9%2FTeiiIox2uVIVosyN84XTfgSbmiVSK1gh6j8HwwNPYkQUKWcLKeymUjhA%2FpVFQ0W16XILHqgAr3Cl8Yng00VH6KMCqSzG1biLNF2N7lWD62WKJLGVbjRYas%2FX0Yw1jh5bER9N%2B5N3W%2FvfOnMv0XpuMy83p82BMIJp7n2OU3mBnDZY7oK89k21w%2FnYNb4o8WDIfrNb02KfUPkXQvh1g3WoPyRUsckeny%2B6ZRwc7yjHND6BUmQr%2BYKlJpxmZ0FoZzAZxqP0CWDaLu8NiI5n76%2F%2FoYPb7a%2Fou%2BENnaL9uB3hC40Bk0ExkLY9LQG1OyPdtYx9o2dlMadFQk%2FxurEW2UM0UCJcaTj7ZF5nvfacCU2YqtyhxuRGnazlDInJw3sdp2m3G5tZEORZwKU%2BLu9aPW9Ed4z6RwKogn1aFCLroiNTJNySDlByo6BNcpLS6Ag0Qn43jWUKtGsg1a30efJWmqoOXK6%2BY55HLKxHZcSPShV%2FpR1ZSlyS5O8eDd4WOxCdCdTaQjSe94fR%2BuUX59ZG1J70svpvwQoNnCu68FJimtMir2ddDPfmTcRpMJXEkr0GOqUBBNYlavGThQgr%2FJwqTpjB4joLrJ624P8bDfEnIP1wTVc1SrTO3ElNwbJ8lHZkVURqOXzrIq1AAwgg1%2B3IoOowjKQK4e%2Fb8xJ02ZJJQujEPg8IqrOtuhJrOOjZhFjdN9hd8jKA2%2BlPgui6Ca2ZF04YbkiPnPSSBVE4yqNrvh7BTtihstJbHIbSWigIcCxsutAJD4PzviNCu3PaDoZ16OBSL8zYkw6r&X-Amz-Signature=2f3f85d57e665d5f692ff867461a939d0dfde548da2b0329fcf2fb3b7fa86547&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=de5936ff0940cfb5f6be38cd86f3f79b7df13a9ece93544c6c361dea4929bd6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=9585788a24b482b5a2e28b1c4e3d98fca140fe4aa468873e5670fd061e61ee51&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=d8ae9e93f4f5a86b10c682f442fc3beba25767c43c49b64da1c5b22d481353f2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=68de9833a2549a923305badb84eed4c26fa7316ae5d131198d22bd4710671c17&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=63222020ca00034f512d7acd228b13fff21b684dacc04918e87aa5bff93366fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFOCXSTK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCJykqyfy7K67BgL%2BAguXCEsU%2FzibyprrMbOpsd7vgWfwIhANhuUV%2B%2FCDvqJ0zsJEc%2Bvx4R9jBJRwDQv98cUdUUhEt%2BKv8DCF0QABoMNjM3NDIzMTgzODA1Igwz9dGmmZgUhQzCxcwq3APoVcyPSkwUtO%2FXebYpFhYIBnCDoXZdHdVaCI88UJzpU7hHrshi7PcsMHLewfjsSf%2FOdg%2Fy4uxAlhgdvo8NfYPvNOraaGAcOKwedJVR7d11RgydgJBzh1KBaaXp6LqWjqoCTXbkBsPc6%2BRzs1ODMjuXNcQSf3oeP3ofwNKODqyikQLzv6Heuo6ZYQrkrwvyL1CZkEawl1oMf3ePURsSAO%2FX1zaQWzLdH4%2F5lvPVBgVX7T1vLL%2FJtcT49Rq5I60%2BhJTHUor6PvB6Nf8Nz5fMwUio6jfgZz227N8xE5qDaERtLgSrxi3%2BKeeotAWYfqn72J%2F4U%2FCdp%2FxzKt9sKxtJRM%2BoL6E0xDRucquAmPrSefU58BD4N6z50G1VLFNcHQyfzD1MQG%2FaSNefm7FMBf5qp5hCZeKBlJQ3c6m9DxAJr9jOYDwxcTU6VwOFEO3fLOMHrZfRS6nXJx3VLilqSocVymaePLM1jfzXBCSuSq52IpMLfjC6RMHtdRc09Sp7YKT3vbovZN38VYLDTrrjACaRITNLzL%2FxuEqRKUnmfZYbwUMehD%2FedzPeZm32rOJjgPwK3mgyENd6%2BvHp%2BNXLCwy8Si9cPem1dilP3fYStvYLlH19koNozkKXrKovY5hRhjCAxJK9BjqkAToP3a2nPWzvGIYsgrD67xvVEqmKFM2IOVbKpCFg9zExIj90YNr0VrREmTwIlYiu8iAcyfehxvfXpsmCtrBHbOBG3CWDS2LGJzOJix5Ij6B6qnkPlnQw2hgsFJYUcUIqmJx7SNNrt9Ki4pnxXUfqOrZTAy7SaOg%2FTFyr284PPD0fFCKrzqAcl6suDY44SnaH4WYdyQkBf%2BfpD8OJZMK0AiCr%2FHT2&X-Amz-Signature=b58ee4a9c675f40cadbb14b77531de174c678dbdf1895f2fcdd59db6431c4a9a&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZU5P2S%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDfGFZ8RmynCsLg1Qe9IF8DyT6In8j82YkW6Wt08N%2FBeQIgRe0lwW5u1FWmTq7jexO%2FNFNIJ6s4PW8pAG7yWx8EtSQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJQfIFUrETCo%2FHnA%2FCrcA8SnhSucZxOn%2Ba7vhWEIful5gq1AOmwd9vFy7hFOHyJDnE85lIHffVRQDd3IcsKe7AkIDeku9DOjnokUEJgbrsvXY3ibccAecG8NlHRr2Z7lZL%2BSczgLwx%2Bp%2Bph4gKQNJkpnoV%2FZkrbLOoUOX1qbK6NGtTE9rpcDXqUHLu2SWOpJzasDBX%2F72EjHjHQjIOhVyWFnglUeavAghrzE38ee8cCW88JDU7cFhbXaJkOOE%2BcFKljHh5mRZJMhxYwTdYQhlhAJjJPHloLxCrTbz2Kk7knjwvvPW9g%2B7%2BXK%2BicDCYmUh8KDk208unbW1LS0Z7ecCGt6cqck4ENP7u9iXT2eQXWmxHcPHWmxNINkcF%2BxXCEVsMo22Q%2FBoZF5lkw45T1oQ5bRW4oJpneQNjnzVwTmkC%2Bw0vMCTqraJMBqgjjNMVvO69eejP2G9bWJJsUm1h0jDO2v2Clzspo5gg%2FEwoRGmIOT34g2ftLZOblggVMtPeKx5w444i5qxSx7CKfOqV6oOShJzCe1HaLe4UteTYxi4CT%2BrctwecgbAGhCcDLx%2FEUg5A4t47rwZP1dpCx%2Bs%2FcvsQlUYhy8vTKoJZzQvzE3x07xPq%2BWyrDrf1hgnLVfI%2Fp3v97UVvn4mF4%2BzNw7MIDEkr0GOqUB%2BqyLBsrYEGiZy96qavHCwsXPg0Z%2BpjCM1%2BF3QvucFbbreuRWm5y5FAHmaA91NI34x%2BC5STaW51oKC5Tu7f1kfnsmBm4QzmQ%2FjTdw%2Bt2du7%2FBVSXHu%2FEJ8l8rBFZ7FswDIDbvQjyqANZAJVpi7o53IaUKojS1yUlAKc0ObNqeSQQu2dRgE1vJEkze%2BfKJVuJjkjbpdLpcb93Yk6ZfVya0pUuDZ4Kp&X-Amz-Signature=f0d28448f0546177c4ee3f36d2d8d3d9cab3d4e479bbd30253c425be9e1da569&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZU5P2S%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDfGFZ8RmynCsLg1Qe9IF8DyT6In8j82YkW6Wt08N%2FBeQIgRe0lwW5u1FWmTq7jexO%2FNFNIJ6s4PW8pAG7yWx8EtSQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJQfIFUrETCo%2FHnA%2FCrcA8SnhSucZxOn%2Ba7vhWEIful5gq1AOmwd9vFy7hFOHyJDnE85lIHffVRQDd3IcsKe7AkIDeku9DOjnokUEJgbrsvXY3ibccAecG8NlHRr2Z7lZL%2BSczgLwx%2Bp%2Bph4gKQNJkpnoV%2FZkrbLOoUOX1qbK6NGtTE9rpcDXqUHLu2SWOpJzasDBX%2F72EjHjHQjIOhVyWFnglUeavAghrzE38ee8cCW88JDU7cFhbXaJkOOE%2BcFKljHh5mRZJMhxYwTdYQhlhAJjJPHloLxCrTbz2Kk7knjwvvPW9g%2B7%2BXK%2BicDCYmUh8KDk208unbW1LS0Z7ecCGt6cqck4ENP7u9iXT2eQXWmxHcPHWmxNINkcF%2BxXCEVsMo22Q%2FBoZF5lkw45T1oQ5bRW4oJpneQNjnzVwTmkC%2Bw0vMCTqraJMBqgjjNMVvO69eejP2G9bWJJsUm1h0jDO2v2Clzspo5gg%2FEwoRGmIOT34g2ftLZOblggVMtPeKx5w444i5qxSx7CKfOqV6oOShJzCe1HaLe4UteTYxi4CT%2BrctwecgbAGhCcDLx%2FEUg5A4t47rwZP1dpCx%2Bs%2FcvsQlUYhy8vTKoJZzQvzE3x07xPq%2BWyrDrf1hgnLVfI%2Fp3v97UVvn4mF4%2BzNw7MIDEkr0GOqUB%2BqyLBsrYEGiZy96qavHCwsXPg0Z%2BpjCM1%2BF3QvucFbbreuRWm5y5FAHmaA91NI34x%2BC5STaW51oKC5Tu7f1kfnsmBm4QzmQ%2FjTdw%2Bt2du7%2FBVSXHu%2FEJ8l8rBFZ7FswDIDbvQjyqANZAJVpi7o53IaUKojS1yUlAKc0ObNqeSQQu2dRgE1vJEkze%2BfKJVuJjkjbpdLpcb93Yk6ZfVya0pUuDZ4Kp&X-Amz-Signature=b6bdc4e91f5dea6417275773a1f6798fc610ca0730f84bd0f498e2faf7ab3d85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7T2HUN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBgoV5T%2FHczCxE4ea6qnImuStk5RyPiZlStohuQ3mEG%2BAiEA2nqfEMb7%2Fak1%2Br8L9GATPUGK7fL3i1Ct02TY%2B%2BTgRLsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDKXlhoNtdJBH5cNCFircA6QTwDxJpcQo6g2hjN7X9KrhHqjvWwN4A3Q3VP3xswvqVExJDgccrVP4VZ5oVfVJ5uhfADMD%2F%2F99TNNfsjS%2FZ5lxdYyLtRVszXJ3exSke6%2B61TuFzE522CjaLd0RoV1b7bQgZADKRRINGiB37Ku00Jufkmj6pw3XTVWlvjXgZqAjKgmcDE21rYRkeCxWD5y%2BrrJOB3KgOS31z%2BkotKwFyUuxC9MzeOZxYv4OXzBXf6Y27jbAq2nCyOurIs7Ois6vYcBhRODALP1rMnB7Fw9M0Qgb40h9RT6su5Ve1K2IH3RB8M3U%2BDHxvNX2m6kd57aWRsXVNSFhrW0y0%2FJrnW2jWG%2Bwt5yUNfNxapB8SDtuA1kbtEyF922fik%2FDQCn0Q06c5axiiGuTU5x4QuzC2DJSGzCiGk%2FRtkLkUVhcX8rhH1ON%2BQo4n2rnoDF3dIWUImoLdPyBg%2BNHgJ9CUf9V2bXTAwNeaaMOlCuyxT9MRfMxQKGhBUQ1kQ4Fjru5yDmNIjtSd1qaxd5WFDqefPeAtV7vBYfsl25H8qfGaKt49aCwobWAnArfRXll53jOO7v3edVMxyMXBmKneeO28Z9E6E8Lb7nG3pAQNgHYVH%2BOPCOiyROUaV2eTX%2Bi1uqYATVnMILEkr0GOqUBnDB3bG23du2AgSfoS0EAnm4oTXgwjwE1sa5%2B%2FtgfN6tx3Eyx6cbCN4p%2Fmj2RE6oNM5ZOSd%2BThrotNLTO5OxvHvLVM4Ybt0DSFXXmsyXBRVgKYm128wxB0LTjVCzjynY8hnWx3ABFLHvCIwlEgro9V2WgllU1kT5VFPmfvk3n96TmnVcWlQ2UUG811udykcQ359u%2BPCceiBWdeIsuKIUQwvCeuizW&X-Amz-Signature=3014bf500ae8f2f8373f8b308383417a710b197d10862abe88ec25fd2d18d99b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHUJC3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDw%2FI8pqFgP8VOQTjfUhhJ5RtRAG2nRA7w3UVMivsbiiAIgQQYI5ycMuMphLiyC0EbY7BuvHTRkUuqIDeXby7IWjscq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNgbUPR44mESqGve%2BCrcA3Qpmku7S95qXrC1mubKeFru1h1AJ%2FJBrUQW9GN2e7pFL6yP%2FNfDx4fTRyLVxWxxvD2qqN3KFWXVuBr6%2FGhtfR06BV43tVY1AHAYizvUEmOVCDJg1gm7AvYSWnJyE3bA4nRTqhLW8KAmsOSIZ%2F1iULgteP6RFkLlsvLnm4lPzTkcCqGj2qDLdgfrEc167xKc%2F%2FiSel%2BpvoqDTHC2Zd1MwHi76O66dPCi5%2FyyFEUoswtLCCtj9PMp0a80vBGKCUpNXHxEEdvxrZX2wv5cZCS0zbZTnGcFZ%2B%2F1%2FbJ3JpCGZe4UuGKSxFz5459%2BHDIjjqILJNfs6Ax294B21WiblgVjuESlF7rL%2B5X3xH4goyJJ8bSA9tg2TAoswM%2FtM43o4zqBkU%2F4KQoa66uQjgRZo18n9eG%2FTQPHoESfxjizw6hdIugnaN5euA2f5ztNrvXP6IOY%2Fue1WD846I0yDHJKoQP%2FgnoJTtitKILJnkFJ5DmAJYjmjhvy3j69e%2FJO0WDhV4eLp6Gi6LyChn0H0FD%2BfPZoMoe81rdMKVGgl1du7EMoL8egLgd4Wtn0gVC%2FS5tuGBSkun8EMthNyTdD4NvuBGepzNYjfaS1NZaKsoDDbFFJpFhkbBBkTnD6wc6R110TMI3Ekr0GOqUBeicqRcvHxC%2B%2FmJFE4vKHx9ypiqQH5zsU2K%2FC6eUZPWXVeaVkvaOq45MCR8GwQkBOEAtPPQfdkkTzJ6P%2BtIEShajaOqnD7xBt9X0naxJP9kvWiIt%2BEqZcnlYDMmedLs5IcwLPombAa1IP4uyxnWseWfULlt0URtX%2F%2FDGSJqUFcHNkEw8C3xwWzcTzir3L20kdp8f2L9JFl4KbGtootK%2B4ho3Fm6Il&X-Amz-Signature=dda36a14758d1dcf92be6ef7dfa8b8589349b0d9ca1f8de18bc32b25f314e6d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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