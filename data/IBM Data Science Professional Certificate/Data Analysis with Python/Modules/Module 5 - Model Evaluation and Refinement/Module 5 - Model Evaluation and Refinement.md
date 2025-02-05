

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=a602320d80d5f68780f04e055e7a32a3513e4cdf0fd7c9e3a63e2df1883e6cb3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=242c1903acb9047560288513b146b487b0f617f2115f4e108efb38233449ecd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=3c861becdff0b95e4653cd661d416cf67eb0acb05c93d17466b11768a2bbb4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=67f391fea770245595efc39dba30b2a86204681ebd355297a10886e11b8b2689&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=9fe85c2b26bab9d137749f337009b45f86e5513ac2bc044adbcdda3f8635e4bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=7712db642fbac77572521c32afbc1e6bef5f7b3f7691fc285909393b4cdb1985&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=8fdb350f4f66c051ee903319c0fdba8c4ec030220420f4c5585d04d8a7c306cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=5a04598043cbff3e96fb5d33102f67a5e23009a1d65fba8b2fd39761ab588bf0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=d9c6bfa7a201796f04b612a1e655ffba07041f9408df83bfe2310f2a0ec82220&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBCJHUH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIELytvwMsqi62Y2v6SSfxSRrM3UkVizWheV%2BWYpVdKYcAiEA1gzwSeRN7LPojKrxXcbtWMtQdXAp2ofWYSxA%2FD3orPUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWihm1uVMvMX6W1%2FCrcAw1naQSp15%2Fq1dLawToT9O0n6sDJQmXCFRdgNMe%2FrwKH%2BPiwKy28wRoLzNrEZLy2T1prq81UfXwom13vLyL2taCjIaj1uLbY2SRzAClNLMw7p7x97TbyRcwjZLzhPSeZjahUUokF1nza8THm9%2FXZI%2F0QALgln%2B5Aj%2BFHMQ2vWpP4Ezw%2BYn6U%2BtrZGopluzQBi%2Fj2En0G%2FyBpObqAzie9XXZvE9uoD%2Be3xWgf5YVBLx5018CG08KYNTqTakf7apIeXmbBMY47nSvDGuEZ3u9yKohzbu377wr79VyWT9CAyRTD2wn2IHLYAO7J8lYuLPleYEjwD%2Fkv%2F6Qy7EpjrcR3jopC7gE278rDfFmISvaGcQ4AqYuCxIZ4rAA3zgCxkw2j3qMgMLgatmpeOzFuwwz4GIg59gnzXMrp4sPwG4krk2fNONL6B%2Ff2ylWwaoKWKJNurDBZTAPnd4yrStX5NrjNoGCvpa1jGkbSz2n5pnxVDlQ%2Bay%2BS%2F8dz8EPLeE3ffGllvvfzTsx6IoVZZMaFUNrOIe319WtaAdqLYHSvTzPj0RNCCIp3fj656%2Fk4T2EkErEs8gk22v%2F%2FgLL7PDb6HmcAx7YrlM2A8yboBuk9L52WXQVdTewA2gRDkePZhpXvMPKzjL0GOqUBu07y0%2BByUBsR%2FQZplcn1fSBgk9wh110zwm%2FJI0lPibAPDbFej4zurTXHVhACoN7RzoJ%2Bq6W4yY5BYiusZw5yKL8HZ0ALEjU0DX85HyAPHhi%2B2TGJwAu5dITd3wH8NUCvqOXHTFoBc1nsj8CPJqQcsYtLv%2FuOgoUMS217OywZBiHuPrRV2x29UW6jLC5NlAO0vwsH7fRxWvtHU9UyStjrTxI3B3R%2B&X-Amz-Signature=5f19417f517380089dde51d5c3bf1f665d919abfccf7022bb4b0998666a9d7c7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBCJHUH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIELytvwMsqi62Y2v6SSfxSRrM3UkVizWheV%2BWYpVdKYcAiEA1gzwSeRN7LPojKrxXcbtWMtQdXAp2ofWYSxA%2FD3orPUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWihm1uVMvMX6W1%2FCrcAw1naQSp15%2Fq1dLawToT9O0n6sDJQmXCFRdgNMe%2FrwKH%2BPiwKy28wRoLzNrEZLy2T1prq81UfXwom13vLyL2taCjIaj1uLbY2SRzAClNLMw7p7x97TbyRcwjZLzhPSeZjahUUokF1nza8THm9%2FXZI%2F0QALgln%2B5Aj%2BFHMQ2vWpP4Ezw%2BYn6U%2BtrZGopluzQBi%2Fj2En0G%2FyBpObqAzie9XXZvE9uoD%2Be3xWgf5YVBLx5018CG08KYNTqTakf7apIeXmbBMY47nSvDGuEZ3u9yKohzbu377wr79VyWT9CAyRTD2wn2IHLYAO7J8lYuLPleYEjwD%2Fkv%2F6Qy7EpjrcR3jopC7gE278rDfFmISvaGcQ4AqYuCxIZ4rAA3zgCxkw2j3qMgMLgatmpeOzFuwwz4GIg59gnzXMrp4sPwG4krk2fNONL6B%2Ff2ylWwaoKWKJNurDBZTAPnd4yrStX5NrjNoGCvpa1jGkbSz2n5pnxVDlQ%2Bay%2BS%2F8dz8EPLeE3ffGllvvfzTsx6IoVZZMaFUNrOIe319WtaAdqLYHSvTzPj0RNCCIp3fj656%2Fk4T2EkErEs8gk22v%2F%2FgLL7PDb6HmcAx7YrlM2A8yboBuk9L52WXQVdTewA2gRDkePZhpXvMPKzjL0GOqUBu07y0%2BByUBsR%2FQZplcn1fSBgk9wh110zwm%2FJI0lPibAPDbFej4zurTXHVhACoN7RzoJ%2Bq6W4yY5BYiusZw5yKL8HZ0ALEjU0DX85HyAPHhi%2B2TGJwAu5dITd3wH8NUCvqOXHTFoBc1nsj8CPJqQcsYtLv%2FuOgoUMS217OywZBiHuPrRV2x29UW6jLC5NlAO0vwsH7fRxWvtHU9UyStjrTxI3B3R%2B&X-Amz-Signature=d3ad155798eb190b5eff809861364602ece5ccbda6e37e5da0c2aa914db829ed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBCJHUH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIELytvwMsqi62Y2v6SSfxSRrM3UkVizWheV%2BWYpVdKYcAiEA1gzwSeRN7LPojKrxXcbtWMtQdXAp2ofWYSxA%2FD3orPUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLWihm1uVMvMX6W1%2FCrcAw1naQSp15%2Fq1dLawToT9O0n6sDJQmXCFRdgNMe%2FrwKH%2BPiwKy28wRoLzNrEZLy2T1prq81UfXwom13vLyL2taCjIaj1uLbY2SRzAClNLMw7p7x97TbyRcwjZLzhPSeZjahUUokF1nza8THm9%2FXZI%2F0QALgln%2B5Aj%2BFHMQ2vWpP4Ezw%2BYn6U%2BtrZGopluzQBi%2Fj2En0G%2FyBpObqAzie9XXZvE9uoD%2Be3xWgf5YVBLx5018CG08KYNTqTakf7apIeXmbBMY47nSvDGuEZ3u9yKohzbu377wr79VyWT9CAyRTD2wn2IHLYAO7J8lYuLPleYEjwD%2Fkv%2F6Qy7EpjrcR3jopC7gE278rDfFmISvaGcQ4AqYuCxIZ4rAA3zgCxkw2j3qMgMLgatmpeOzFuwwz4GIg59gnzXMrp4sPwG4krk2fNONL6B%2Ff2ylWwaoKWKJNurDBZTAPnd4yrStX5NrjNoGCvpa1jGkbSz2n5pnxVDlQ%2Bay%2BS%2F8dz8EPLeE3ffGllvvfzTsx6IoVZZMaFUNrOIe319WtaAdqLYHSvTzPj0RNCCIp3fj656%2Fk4T2EkErEs8gk22v%2F%2FgLL7PDb6HmcAx7YrlM2A8yboBuk9L52WXQVdTewA2gRDkePZhpXvMPKzjL0GOqUBu07y0%2BByUBsR%2FQZplcn1fSBgk9wh110zwm%2FJI0lPibAPDbFej4zurTXHVhACoN7RzoJ%2Bq6W4yY5BYiusZw5yKL8HZ0ALEjU0DX85HyAPHhi%2B2TGJwAu5dITd3wH8NUCvqOXHTFoBc1nsj8CPJqQcsYtLv%2FuOgoUMS217OywZBiHuPrRV2x29UW6jLC5NlAO0vwsH7fRxWvtHU9UyStjrTxI3B3R%2B&X-Amz-Signature=269b73cc2e1def79f79771078792b4c26078ca970cde5f43f939b1b665859cdf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=12eb7c00956a6623f7995cbe19ab1cdd23660b25fc689e2649f413f09b39d345&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=8ba2278e0ac854cd638ca97e334969d4ef81892298e4127e0ecc282456d51f13&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=76b3fc9f31fac89989bfb7a91538a10cf68db89898286b72015b6da600ce5eef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=222ae8cb5b0fc001c1abf8fab5657544e358c564338dc9da3eb5baaae99b99b2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=28318f011932cd7a37393ce1eb264eed13c6072bddd9f6c954c00f56042728eb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ELPRLA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEWqFKDKoL3n0uCQG%2FV664C8TJx2biU1Ig5GpFpEd1sMAiB5Pis3cP5tPoLcasxE4pkanQKqUJuNldnGWtXbrd0DvSr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMI96LJJWkhVJjNTfMKtwDT6UTB5bWqkjdC81RBlIVriRXmq%2BzpoUNOLsq%2BpKOQaOG6WziWBJDkjCjHIJFlioP%2BYT99CW3IFuNlWvtUYzTCC5c3%2FNzryqtmkO1kpRBXTA62i4LPmCl0z1LmHjKDgeyJ2Jnr8jnZr1sFQlUENTwyD%2B6sfYb4X44hGL%2FYSjKk0T3%2F9U6zRXmD1iaT7bbeZyP1jJmVPCUuJsE7UBcLbLMZjwnCF1ewEhsm6sBF4FjxUqM8%2FM%2BEygxTEVBlUNbWQrDhw1krqqdQI1TvPOWJTed6%2FAofBxdh75zPKEQAAwuiodePBMCEasCFFdgg7fMiUhpHFpSJmxf%2BhAiYXXnNQobtsCZIwy027%2FLTn%2BW3tYBX%2BiLqaWMFgSre2qiFBNnY9q9a6p7wDzpq5qIhBL5oZaL7FwoBFTqAW6u2urDVrWJQbbKGHbmRDmuw%2Bfwp24SbNi4WzIuO4zyI1RrGSsXdF3OhCQJvEBpSYWwx0jhph6XRHbbWLAJQN4OnimWyjmdyMPjr7keh586i7ViNPxTyv8rD56WVFCpvD%2Ba8Z1BNxfw8ai33UAQNPMpA8Pxy9r4U793M%2FZDtcegugk2K7zmCC6hiku4TBAfBzEDX4pJKzJ4%2B%2F8H8ACz3%2FNQdLzR0QIwnbOMvQY6pgE4MRjM8UPRU3AM4225rWiydoTIYjcirkDQLcYW%2B71um7kLiP%2BVp2TKYOTAplzBgDChJlVh3ceTqPiHciLoVptsKhkxXOR8eHkqu%2Bq%2BChFrlTqB6%2FOzxo%2BRtpkckMw4JuDSQtlqTa4z4pEQ4I%2FvSXUhsMuMqZIaDbw1U52HZvPL83mdEVd%2BQYDBCJUwx2cTIMP3P7B78HOIK2qmQtqmb6Blyrfm10vn&X-Amz-Signature=8b24b721535b390ac6af5d9dcb47d8a6ba6ba1a7575d106f42842132606182df&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AWZBHVC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDSJ4RLJZf5FXwSeABjlTAyil99m9LWs2CvGrfe4szo%2FgIhALJLGyCqabyioebnaIYKLt1H0FR6UY0KiFOok43%2B%2BN%2BwKv8DCEEQABoMNjM3NDIzMTgzODA1IgyQOcNhD7uADcg6jHwq3AP5jr9dkvmXvMObkDSLkwQC6td3PbG0yN6KDtFmg5d%2F9u7JGvbdOxwP6ryQiT4Ceufn7VJ7H5XVdorwcpjFFUBCrshk85oL2hLXUWGrU2nGe1cNJYiewNSHacxgmobrQKkx%2B0pB4SZ%2FNpMhPSrOJ%2F8c2NhXL9FUS3bRsYZGuhRUFtTCHKrr7z1ixNyFaLAONvPv0l9d4FPti4%2B5fIDseGpG4CWCTDhc7ruMdps%2BBQo8VKZhFDwyp5%2FauD4FWUEL7rh8rlamqJCo%2F%2FI%2F7GYC%2F50P1hp0bsnO%2BO9a1u97kvSsiOFDAZvH8AXJjwL79jKQdOZqEKuRxENhAFyR23PfaWsIH%2FmjOKScO7E6pxVMlo%2FihY%2B33locjp16RGZxFEvkDWKhPj5vZD0s7L8sCqQpZJgYD0NsnYupPIHZ5Qc5qGIyXbWY8VFPvI1b5rejSvFLrtIwRJ4Q2sFJ7LIMLve6mcW8b7DZmgZ2GX8WfAmeI7RL4by6NTSHjWAZu%2Fg6iBiWTxnEzctmyyYIqF0394Q%2BohP106%2BFaw9SLXKCjNWZUc3FtEUvEDUFPk6r5G2lKglBWULiWfZ4rBWI7c6LYOBtnr4dsy0b67IA3I09m%2F8lelyNP%2B9T0QO6PJp4q2MxHjDVs4y9BjqkAdkq88iRMTUD4nKTlksleo2l59toJfUKkYCyXjeq5XpOmJv6sIpmDfrIUXGTrwbcd2It5fSeKoYKSXd5ah%2B2SfPU1WAVvjyJA0p%2B530fBU7xyDJUUW8SaWwCeGklKPtJBMTUOT0j%2FZfyxrfH3xnWBjE8fu9FVBG0h4x3DwsOlATBv0eC53oUD3Oj16IDjObaZ9NiKAmPHZK9xXWl3Rwy0dT9ZuIL&X-Amz-Signature=1db1d54390d0c9efa39eb6cb9601694337c809caf96c3a7e7d620ca8ea7de955&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AWZBHVC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDSJ4RLJZf5FXwSeABjlTAyil99m9LWs2CvGrfe4szo%2FgIhALJLGyCqabyioebnaIYKLt1H0FR6UY0KiFOok43%2B%2BN%2BwKv8DCEEQABoMNjM3NDIzMTgzODA1IgyQOcNhD7uADcg6jHwq3AP5jr9dkvmXvMObkDSLkwQC6td3PbG0yN6KDtFmg5d%2F9u7JGvbdOxwP6ryQiT4Ceufn7VJ7H5XVdorwcpjFFUBCrshk85oL2hLXUWGrU2nGe1cNJYiewNSHacxgmobrQKkx%2B0pB4SZ%2FNpMhPSrOJ%2F8c2NhXL9FUS3bRsYZGuhRUFtTCHKrr7z1ixNyFaLAONvPv0l9d4FPti4%2B5fIDseGpG4CWCTDhc7ruMdps%2BBQo8VKZhFDwyp5%2FauD4FWUEL7rh8rlamqJCo%2F%2FI%2F7GYC%2F50P1hp0bsnO%2BO9a1u97kvSsiOFDAZvH8AXJjwL79jKQdOZqEKuRxENhAFyR23PfaWsIH%2FmjOKScO7E6pxVMlo%2FihY%2B33locjp16RGZxFEvkDWKhPj5vZD0s7L8sCqQpZJgYD0NsnYupPIHZ5Qc5qGIyXbWY8VFPvI1b5rejSvFLrtIwRJ4Q2sFJ7LIMLve6mcW8b7DZmgZ2GX8WfAmeI7RL4by6NTSHjWAZu%2Fg6iBiWTxnEzctmyyYIqF0394Q%2BohP106%2BFaw9SLXKCjNWZUc3FtEUvEDUFPk6r5G2lKglBWULiWfZ4rBWI7c6LYOBtnr4dsy0b67IA3I09m%2F8lelyNP%2B9T0QO6PJp4q2MxHjDVs4y9BjqkAdkq88iRMTUD4nKTlksleo2l59toJfUKkYCyXjeq5XpOmJv6sIpmDfrIUXGTrwbcd2It5fSeKoYKSXd5ah%2B2SfPU1WAVvjyJA0p%2B530fBU7xyDJUUW8SaWwCeGklKPtJBMTUOT0j%2FZfyxrfH3xnWBjE8fu9FVBG0h4x3DwsOlATBv0eC53oUD3Oj16IDjObaZ9NiKAmPHZK9xXWl3Rwy0dT9ZuIL&X-Amz-Signature=a372183bf8926846d805a028ef17d04042d65ac1d72ddef87c850b7a263aed90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2JOEG2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIBECn3OH6YLg7JDWBwkEE7EDbqHqwNCVZrYjo%2F%2F0bRN3AiEA8o7Rp%2B3pSMrCzmU7W8dVt7jYo4mlvYfXn2u1vdNkMHEq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDINgAsQuENtllpx1oSrcA7qnZguwR88ZGgB59RsU%2BCL%2BeRuemCAIUGBpRXKd%2FFhEGnchPzF%2BTEocLxfUbBzS%2BpLzt9rKb6LbH95dd6kzL8iZl%2BEmEbOYxNiHqpisPE2Jv8Eu4g2KKfycZLl1hldB4PqPozGJzkETmojzEvTfRMPMhnseome6Ge3nSBrY8tYq9Ox%2BpGNsH2fqfn7DOQ9RQ2642iPEGmzduJmbvrwOL3kLVd2Ua283hOM6rLRQY9VS%2B1nu%2Bt7VF%2BJRXEw8Sa4ICaVGQmmtdE05O0xJn8le%2FWPSqmI5fHv3QLYsvggIfx6xbVBy8Z6XNGjPhqRPaB4RCO6CchqTf1oP3FLOuRhZBxtid%2FiDQZwFPneqlGo2wpSzKgiIkNWrz2Fktk7a3MByjkky86dhSCpWc61b7gqbLh6BPRdYboOEeX%2BOZV9nbOtpnrqJSvUnHMh05OaIkIBQYtOiJ%2FS4OglvG9cjyIUoY0TRiFdhDbVZjeCdMIPDkFUFrf1C6J5pgGKHWQMo2ALXi5dsrjrexZbMSoNbcG%2BD2aHIUzphcpQdoDW5jHve2vxKMC9gDCEnCq003jpPAz7S5E1%2F3cExPpqKLAdKMpY%2BhNXKOWm5%2BFN8fAXjjp2qyQ0lAR6GFmc62bRD7bNRMKGzjL0GOqUBt5Cw5y6Pt1fN3JfB3K%2B8xiALrRXZkKvarXENzmNPavIAbQf7QcLKpYjNkoUZjRizRSVoOnS3yyh9gXAWYd84l7iMHfVDvq3vmC0gXKYME%2BHn%2BNIEpYzgEG62AEaFcdzbDJ6G6u8%2BZD3Rl2hZw6Nx27hNWmvTyUayR4%2FEkURi9EwKjXHfoCg5xDmsq%2FNJUCuS9UuF3aLQicMkbB3URxN3ylX63k7z&X-Amz-Signature=af7668bf506ecfb9cd8909f5afc8133c459aaad560e1904e12c6e8f038c4205e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOD2RSV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIAlNUtTPsKg9td%2FzeEvpvMnuYVbhHjRUYbb9B4wAdNqAAiEA689Wh7K24WJzjR4kL0i6F2GA2Pq%2FjNzVJXAUs1csqTAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFLnpEIprg3lfoCElSrcA6ZOSbEMoiI44lsbb%2BK4u%2FmHGRWP75no%2Bf8UHeVhBuOmvFNc2f2x8BF6QtB4lUTB79tIpTViM1ZOVjtg42Cr5WWrjqCFt2yYGyfDlReg6Ph%2Fa4VSM8ZC5fguWPFd6fl5nIctU04AQrX8ZSelAxY8HFkzE0%2FH5L62wQSXZ0pqnoNNBYp3OeT2asWroMEuZwKqoNZzkjVfYQejb7pGOdaN2deF2gnW9uXGxcxGpxmEJImkvDC3jAb2CyaDW%2Ffpe0%2BIty%2BMCH5vCjFjDgWxmcZs4pQyo3C31tBhEj8zHwAo%2Bz8mpCLplm8cX0TVnWzaLyZeZcArwUna1SZHXReQbb5G1VOODqI08Wg%2FQ4RZomktPvemX%2FNUPGNvVz20DdYWYlAH8gQjwzr%2FT8es3%2FAwoERBbSsU7W6l2BC5qhJHGjRP6Et0AMIB6tzug%2FK3TDXMlJ%2BbxtkKtz82VTME5jhy%2FGc5U7MAoJcDL4u4rL%2FqIyihNZ8Ijr26zkH%2FBrmWys7s%2BRm%2BAUgVqnqLOvWb5XSh618T42a2fPtpWl720GcrIOBXJ1hlEjZ44ZCsK%2BuP%2FtruJpZY7HeO%2BopU7qvS0oCSnVVeCOzY5%2FERB5sqxLxZhrfN7eFMEo0Dq5mPh0BaXCQOMNizjL0GOqUBxRxFapdxRJMFU8xJ4eiG7caZZRObezt6zodC5mnI2U5OR0CnBoEYt3sN9rxPeQBG3GJ4zYO9%2FNTBaPnqGNaal7soZB7OcV1uJpDrKmTvnqnAB9AcyqwYSi4hxgohbzre3Rc65WAJreVX9yO2CO3JNVQ7eXXEJaNfLfxDC0I7h1drmGFgT79guyylrR6sk8Rc0l983AolJA6pPhtM3CCPA9O8u4XZ&X-Amz-Signature=440e625e6b0a69d2cd81795c88a2dc126f4654c185ca25ff8387d7dc54c87faf&X-Amz-SignedHeaders=host&x-id=GetObject)
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