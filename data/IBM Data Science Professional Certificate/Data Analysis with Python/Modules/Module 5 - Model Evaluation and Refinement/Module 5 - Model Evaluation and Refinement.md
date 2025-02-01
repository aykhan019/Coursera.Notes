

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=c2396e7e29882dc0eac34a056a9da544b2f12813ba3f2db2576671ba6906dc92&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=7c8120ffabe22d9e097e4430ac59e48cb9b57b873ec6233d2e46d79452d55c0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=623520b34e46184fe1d549575ab648c4fa8bc6499e09348621468adbab3ad105&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=c61ab33eaf9fb125f891231c410472db3ebc38dadc7b2720666c788b76e69bee&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=d37cbdac11e1f233a1c2dfd1871c9ecb7cadacea095f71125a70ae3308026cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=cebf53df928061b03b77d7f6df7e25edb52751fa348592b553ed18e6132fb6c1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=ea158c48590171cf8e857d74bd16813d2e563830178477cf3d112e7c6aa0e66f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=3a266981701f15aebcd622a90a26c573f9074846a6e2f31449c84158a73d6362&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=bedfd2dd93c917de484bf789060e7968cefd6f6669dd29e3c4d7a0f9592ed2d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NKKNBUW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQ4LGizvhu%2FE57V5ydUU86aj0cTT3mTYDZMEWM4OmzNAiEAplEulfRnga0jHrQTjJTXrBKnBaMMkNtife%2BowDU12r8qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXuJi5aQugNOkzY9SrcAzgucoudmeYbN15cFGdudt2x%2Fs5IBwiNo5W2Id8d%2F6TUrP8OOcHzs8jLQV6WFQhgrbeAwIcbDDDRozT3GMlGcdEO3xCACia4iSeoJny2EcHnqLjzOtg2wMi7cKUOnrl5BGkqLkJPpeDeB%2BHSbSFOX8U2X0Pq3fYKfA0wg3jTqbr%2FN8xTI6MFqkkw7uzLZDZOg0sqag8DlsFEDCXR3XtyiOha7S8oSIDRMwrwLRobIOi%2Be2YWthx1PnZ2oxyhNQjvC35z13Ys%2FGAN1qgp0RvQRepHxV%2FjxWwJhEjyCMyyGuSGmwWxTpUsawtGtr8hOL5k3LwQlVz3agzvgEZi9Fp6QSkmOKBnkVjzBPq2zQHoI6M5y9l%2FCANf2mQhZf7z1%2FXybJpmoLdTtKSoMMhDBdEnM7NWzCMxzhWlVFUts49H1bgoU1MuGzeg7ALZltTBEmiaQqWbtUSdLMe8PnMuTT7jJpWSHqWGjotbArhXbYpNVpgxlj1awV8XDfHCEb7YCZi%2FPWyx256wbRr0x5FazJ7%2BYrrfCwBsoAoRshb%2F4Qt3sJhzJTbhakVbH4Rr17EjgezNfIGABt9O7Aug6hYNypfaxGbzOLwMMERtRlfJ%2FZhkd8AZcYaQPhw%2FIwF1TNCfMK7s9bwGOqUBRgl%2FzpzZyIMX%2BRWANc2OOha6m3wEg3rRsJeKkrGD7q2B7uM158%2FTeddwxY0GwtaULSOjTHXxZ8p8MoVNPw0wI3L%2FKqpZNx3qnOPDAAqDcLuloMQt3wJ8KOWZ4YI8TRk7%2BiwVyFFOSpDkVHtwymo6oHQfRiv%2BFocczKgC5FXKSjz7JJHfqsURZBnX99ZWyRH3VCq3FCz4SCVw5MJ1%2BixI4GxHQJFS&X-Amz-Signature=d8d6cf808656deae03616dcfc1a14709cb767060bfd18b0b62fd7f4205e0784b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NKKNBUW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQ4LGizvhu%2FE57V5ydUU86aj0cTT3mTYDZMEWM4OmzNAiEAplEulfRnga0jHrQTjJTXrBKnBaMMkNtife%2BowDU12r8qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXuJi5aQugNOkzY9SrcAzgucoudmeYbN15cFGdudt2x%2Fs5IBwiNo5W2Id8d%2F6TUrP8OOcHzs8jLQV6WFQhgrbeAwIcbDDDRozT3GMlGcdEO3xCACia4iSeoJny2EcHnqLjzOtg2wMi7cKUOnrl5BGkqLkJPpeDeB%2BHSbSFOX8U2X0Pq3fYKfA0wg3jTqbr%2FN8xTI6MFqkkw7uzLZDZOg0sqag8DlsFEDCXR3XtyiOha7S8oSIDRMwrwLRobIOi%2Be2YWthx1PnZ2oxyhNQjvC35z13Ys%2FGAN1qgp0RvQRepHxV%2FjxWwJhEjyCMyyGuSGmwWxTpUsawtGtr8hOL5k3LwQlVz3agzvgEZi9Fp6QSkmOKBnkVjzBPq2zQHoI6M5y9l%2FCANf2mQhZf7z1%2FXybJpmoLdTtKSoMMhDBdEnM7NWzCMxzhWlVFUts49H1bgoU1MuGzeg7ALZltTBEmiaQqWbtUSdLMe8PnMuTT7jJpWSHqWGjotbArhXbYpNVpgxlj1awV8XDfHCEb7YCZi%2FPWyx256wbRr0x5FazJ7%2BYrrfCwBsoAoRshb%2F4Qt3sJhzJTbhakVbH4Rr17EjgezNfIGABt9O7Aug6hYNypfaxGbzOLwMMERtRlfJ%2FZhkd8AZcYaQPhw%2FIwF1TNCfMK7s9bwGOqUBRgl%2FzpzZyIMX%2BRWANc2OOha6m3wEg3rRsJeKkrGD7q2B7uM158%2FTeddwxY0GwtaULSOjTHXxZ8p8MoVNPw0wI3L%2FKqpZNx3qnOPDAAqDcLuloMQt3wJ8KOWZ4YI8TRk7%2BiwVyFFOSpDkVHtwymo6oHQfRiv%2BFocczKgC5FXKSjz7JJHfqsURZBnX99ZWyRH3VCq3FCz4SCVw5MJ1%2BixI4GxHQJFS&X-Amz-Signature=b9adccec040ad5bd432cbd3fc503aa457695180233f822d4e8681c329919652d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NKKNBUW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQ4LGizvhu%2FE57V5ydUU86aj0cTT3mTYDZMEWM4OmzNAiEAplEulfRnga0jHrQTjJTXrBKnBaMMkNtife%2BowDU12r8qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXuJi5aQugNOkzY9SrcAzgucoudmeYbN15cFGdudt2x%2Fs5IBwiNo5W2Id8d%2F6TUrP8OOcHzs8jLQV6WFQhgrbeAwIcbDDDRozT3GMlGcdEO3xCACia4iSeoJny2EcHnqLjzOtg2wMi7cKUOnrl5BGkqLkJPpeDeB%2BHSbSFOX8U2X0Pq3fYKfA0wg3jTqbr%2FN8xTI6MFqkkw7uzLZDZOg0sqag8DlsFEDCXR3XtyiOha7S8oSIDRMwrwLRobIOi%2Be2YWthx1PnZ2oxyhNQjvC35z13Ys%2FGAN1qgp0RvQRepHxV%2FjxWwJhEjyCMyyGuSGmwWxTpUsawtGtr8hOL5k3LwQlVz3agzvgEZi9Fp6QSkmOKBnkVjzBPq2zQHoI6M5y9l%2FCANf2mQhZf7z1%2FXybJpmoLdTtKSoMMhDBdEnM7NWzCMxzhWlVFUts49H1bgoU1MuGzeg7ALZltTBEmiaQqWbtUSdLMe8PnMuTT7jJpWSHqWGjotbArhXbYpNVpgxlj1awV8XDfHCEb7YCZi%2FPWyx256wbRr0x5FazJ7%2BYrrfCwBsoAoRshb%2F4Qt3sJhzJTbhakVbH4Rr17EjgezNfIGABt9O7Aug6hYNypfaxGbzOLwMMERtRlfJ%2FZhkd8AZcYaQPhw%2FIwF1TNCfMK7s9bwGOqUBRgl%2FzpzZyIMX%2BRWANc2OOha6m3wEg3rRsJeKkrGD7q2B7uM158%2FTeddwxY0GwtaULSOjTHXxZ8p8MoVNPw0wI3L%2FKqpZNx3qnOPDAAqDcLuloMQt3wJ8KOWZ4YI8TRk7%2BiwVyFFOSpDkVHtwymo6oHQfRiv%2BFocczKgC5FXKSjz7JJHfqsURZBnX99ZWyRH3VCq3FCz4SCVw5MJ1%2BixI4GxHQJFS&X-Amz-Signature=1f63da265015c9791732a3d70b0dbbd4cb7c0e994cd516190f58932c91217900&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=7bd2ad01ee55290a927a0d9fde97ccf01f2e3b7eda50a61af455bcf0a4db39cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=d58b29f88335b8eeec6b00ec0a3ccab99a6d868afa9754a08e6fc40eeb2e35da&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=225acdb197506d9ab27637a29cc26b227536b27023ec78b6434975bdf177f883&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=535631b63fcbfc07d0893e503f35088848aad8afe33ef628e802423214445972&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=58823c7a37a06fc4213bf3f85f0205b61ae74e675a3483bbe877511361dee19c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ6UYBXS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3f9sJ4ytZkd7%2BPXHsXv6wEZmioP6S1zXTPV3Gn4WfmAiEA8BpT7Y%2FOFxGJ2qyJ1sA0ZHtbbplGx%2Bx8x9fA40P0z08qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBiE770X%2F3IY4FVEXircA6vIhiyR2Wk71VMAiv6n%2FiRUOCyy6jUm1Ssg%2BLAB9sSDRQSQYhXdcuupXqkHf3%2BUnqdWH6nM7dKj55Vx4HrspUa334hRPX4%2BQ4GeGJMTfjqXJ6EByAHgGzyOW%2FADsguSkMaAp6gthQeSIGxjc4TmgZXKDxEoxghx%2FgWfAp%2FoM2Pgyz3l7QbhjsObJJr%2FEaYpcX6gMoaEEqTdjCA1d7NARdLdSaOi%2BF%2B%2B3faxD0Dpk%2FTbJgTTiKmRscHx2BXdTcdl8vPCmXPXcawRitkDGqy1KghYvd51B51lvYIE%2FrrOMQa9vvCy3wgfRsqNyG3MqYM6sUZ43u1An7Q2tQHlJGzTAGXl6IG2TbBsOPkxLjFFmVRqGeR4a3Yd8SoKOkQmLWzP%2B%2FGsSY8DkPN7ZCMruyvup%2Fv7HZm%2BkPEPGZ%2FPVwqSslDYknsz3vgkggxaH4U00tpuBVNAcMfCji8BrucfCKmJiTkfWyYTxvhFWBEKxtglOz3SFuMS6UKNPteq7vloDCT5bsHrRODVe2RZz0po7ZY11WNslZ5qyXRCQCUlpc8%2FSrByrUd56cMsa%2BHB4y2R%2BtS56NU5hIeYUXEOn4w1XPVPGck3uTTQYfuqCtqaBn1hlz4d4RvCBkcyRteDGIrsMM3s9bwGOqUBT6nSlyFZAeZakwsFNR4EN%2BbqKwVXPVQHtT6yQEYsG5kfYPjuz%2BqjOn0gVuZtItNInYO9ovXLVwwvFgzsU5OMoyBI3ynb5Ev6bCi6HLuMVxY6aY52rY%2FnoODV0r3Ci9BXFAklHzlzL4sy3ebvEHaVhap%2Fc9xUn60lrqaUUFpcKMSHR1xrvBBWuokYbr%2F%2B4EIlYYnXn%2BVmNPLLwr4RzoeQOWEY64OS&X-Amz-Signature=243a722f9abf56eb6a053a696053df1d17057617dd61968bc8975f07b0d82502&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URC7MEAF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDn8wwxVUr21MA2kFvu8IuF%2BpZwRzRYkgoAEeirBDx9awIhAJHIjBEZvR%2BpBnEc0Gw3tMFwUgpzXNvJuQgKYLxxCLvbKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDePEjt%2Ftxs2%2BabLwq3AOdWtCPTlKrQZEdieeBA3%2Fo2l%2FuAzJ5mZBNu4cxuWdUiCrQVH%2B87JOtQEYfyA1r%2FapmiigpHUA3sRT36y2jNuNzUJLl9fDExH1vnSG6xXWhQx2hMb2fWDM0AEFcaJD5AR054DgQ%2F2GXdTI6GtCjYV%2FLzsp6pWWdbC62QyCp7Xj%2B3Xin1nfD5nr1lcQgW2ZXzVEQKtHxWJr0Q1C2XXpqbUmhlm4jSWEqbsCbuT3TBR0FPCBShZRCIqp38rzyjxFrRxBoJKXfZfOFmbi5hWzn7PmlR7X2m9fkNfVef9ynRXd8ZL2tcXF%2FYSeIipHHeM%2BSmfcLq5phzWf6oILnKapcazTKdtpCiJziB65aIIXMiB1fNqzRGitTaai%2BSJFnDpH4JAEw4WqyFWvUVNpLue5od2UJctXuxW0qUQ%2ByykbQbTnYLrPcq3UOKV1LvR8jbldo5yStnAQQdMOWPPvTxuLyHoJ84nlJdg32kf3x5Elvt%2FL8zxFPA1oTI5JmK65JdVGUeYtQ%2FV8CDDJzLj4ess2wBakTgM5dBepkOoMOPEggvcL0l07EXIHUp8hjwFwFD4iUyPFE1iiCcxrZpz7hGcaf%2B5vY6aczDzSgLLKDtJMmGT9Z8zMOYJkHSMsWYyX7NTDR%2BPW8BjqkATCfVPWnXT23YpZ1FlX70m9cKA0NqeHaxA2xyVH%2Btwk0qRFTAzv%2BrJirAsxLHQgxIhzjjBm0pv2gURdEeaA2Y%2BH00ShEHSATEIwSciiSyfKFEgtevyg5ZbNSmhGea9fMBen5pY1E0QXLUAQVz7yl8nRwjk5UTkXPQdUaIx1Hjltny%2BvLMzZcknI9uG0O2px1mvHU9IcKk1avRoYX8yoqeSaUirf4&X-Amz-Signature=63c709ab3a1a66141ddf44a639558e4d0472acc94fdb96f797d39b2f9a491962&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URC7MEAF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDn8wwxVUr21MA2kFvu8IuF%2BpZwRzRYkgoAEeirBDx9awIhAJHIjBEZvR%2BpBnEc0Gw3tMFwUgpzXNvJuQgKYLxxCLvbKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDePEjt%2Ftxs2%2BabLwq3AOdWtCPTlKrQZEdieeBA3%2Fo2l%2FuAzJ5mZBNu4cxuWdUiCrQVH%2B87JOtQEYfyA1r%2FapmiigpHUA3sRT36y2jNuNzUJLl9fDExH1vnSG6xXWhQx2hMb2fWDM0AEFcaJD5AR054DgQ%2F2GXdTI6GtCjYV%2FLzsp6pWWdbC62QyCp7Xj%2B3Xin1nfD5nr1lcQgW2ZXzVEQKtHxWJr0Q1C2XXpqbUmhlm4jSWEqbsCbuT3TBR0FPCBShZRCIqp38rzyjxFrRxBoJKXfZfOFmbi5hWzn7PmlR7X2m9fkNfVef9ynRXd8ZL2tcXF%2FYSeIipHHeM%2BSmfcLq5phzWf6oILnKapcazTKdtpCiJziB65aIIXMiB1fNqzRGitTaai%2BSJFnDpH4JAEw4WqyFWvUVNpLue5od2UJctXuxW0qUQ%2ByykbQbTnYLrPcq3UOKV1LvR8jbldo5yStnAQQdMOWPPvTxuLyHoJ84nlJdg32kf3x5Elvt%2FL8zxFPA1oTI5JmK65JdVGUeYtQ%2FV8CDDJzLj4ess2wBakTgM5dBepkOoMOPEggvcL0l07EXIHUp8hjwFwFD4iUyPFE1iiCcxrZpz7hGcaf%2B5vY6aczDzSgLLKDtJMmGT9Z8zMOYJkHSMsWYyX7NTDR%2BPW8BjqkATCfVPWnXT23YpZ1FlX70m9cKA0NqeHaxA2xyVH%2Btwk0qRFTAzv%2BrJirAsxLHQgxIhzjjBm0pv2gURdEeaA2Y%2BH00ShEHSATEIwSciiSyfKFEgtevyg5ZbNSmhGea9fMBen5pY1E0QXLUAQVz7yl8nRwjk5UTkXPQdUaIx1Hjltny%2BvLMzZcknI9uG0O2px1mvHU9IcKk1avRoYX8yoqeSaUirf4&X-Amz-Signature=e8ceac8cec556cc0368e22d8747af1a5fc1259f7e8104342a4a81299ee21ff73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466662LHGHQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEqwT8SYRxSwD%2BXAPbJd42kq00OJYAv%2Bytsx8QRb0TuwIhAJ%2BgPvDowtu43DV4yxdmWSbIqGjJMuJvDM4ZIfWaoOuJKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZwEZmUuJefihvplEq3AMrjM4VBG%2BrmbgK%2BRLMZbSV8gAzelmYX66p2PDKFUs4b2ScAdNT%2BVkrGaEbrTN%2B3IDh9JGYnBaJEp9tLM1BkFVfjNvYesmemnB3rqV3sT%2FOXhVSyoIf5X7qppKc6zpw4sMTT%2B%2BV4Rsoaw4ALalyXU4fAnhkDXA8hpZFPFUJLJ3VAqU23MlEuG0Dow%2BNBvCPZ4fQw%2BaQHeWz%2BdgTmLmXUfY7AQFRhELVlKSEzJoukkOpXOhbG%2B97KGikJLVPobHssVfBb82izHOhs9PfhAuAfRfNppInT73YGtiK8Wi1ChfMkKVdgFVAsPaHfvoyetTe42i2XrF46D8BevlGd4wILzGzyONKIz0DwIETUdAdsa2rWdlxSGXeGyOUK1SuIma3oyw7sStUhaE%2BKJDYQkZbo9jMgKxaYFEzxN90k7n8SpQ8I9CuLpEGVqZSc4VdQoXzu0tCjeTuTuG9YjTLmwWbJJ5YdBPwZ4VjFuK1En3vcKCWXl95wymNpX9KU6byN4ifE1V54ILmjE0v0Pz9aQPWJTUEwUlYqgTgbABmuoShe5p3jcRaY%2BNs46ZUwGFhSpDgwzGvKqGny%2FgmcLJngBxDZ%2BL2TfSM68YG9W%2BbVCNRB70%2BJ9NxIgAMoRI5se7prTDQ%2BPW8BjqkAS1vp3GC7lbbmn2hS%2F%2F9TxymxAG%2F%2Bli05L0xds04sUo8mm3%2FheCM4MDx%2BjYOEZsZyK2H3VDU1IY9fCQylVj2XgmlaT%2FZNhvK0Lbd%2FgjYgu3kLfRaEMkSZ4jzQKBChPXlDmud5cJAl%2F3Hz2NyQFn%2FT9zcOoANBHxYVyqD5%2BtcTFu3RruoKh6BXvWT1Z8ZwZCjL8tUHpE3WHZEiPYV6L%2BjwCGB9ycp&X-Amz-Signature=74345a9680d5d0637a3e67749c6749c66f9711c00b7b301da2277fd2559f443b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PIFSG4T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAgFRLNq3TWCQ%2FFTtoiLSX9qOQf2sONW89506MsyD9jQIhAJ5g4AlcFIjC1slC6iVhZ7LDFcLq2%2BLeWtnrm7FNWce1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwakX0oBj4sBB%2BYAdcq3ANK42%2B3Q1Z41tFXDbqnZdjT2tchnle5Cwb049Q2CeJdakC4Y1Gypb2D0uIMdkMS2wQ5Ny87xpGK%2FU0E%2BJMoiYW9%2FnudtRb1ojgV6aJWtdcqRylYh9a7hLIKzdxzgigWZ37F%2BnWxeK%2FdXyftH1fT8VjgXurCzYkYE%2F42m9yJVvAmJjvpZH4lTFh0IXfrK53vSHMJGF%2FOXh%2BgHiN3uRhRkJSBK5jPM32UXqDHKjQ%2Fa%2F2hdnhp8G%2Bpeq3O%2FfyKA00lQpNiEALeosaNGoXtfs14bf4YTnLp%2FLwJODnIwztHeZIbQejiP2aRterAEF4vOEZppZ4%2B%2BZI6yC3ML9XBF1ogl51zctPm%2BGIUMPAoHyfmSVwC0APbaVE81qvGNJPV%2FVnABp6CRjxui2Zyc%2FbGP95geX%2FaVXpnQJVhukj3JlBGpIXUzK%2FGiTu9zcsW2zUqKlMb1sVh3SThXbo4LseI%2FBuAMbKXUmLJPvL2K1u0MQGgMgkflCflYPAIJPtE06dZVLndWzxpfFRqVVi%2BNvV7AUrUY7rBF8LBOpF%2FvGiO9mmd3XVpNQea0fUKpYRFWclFFdPHtOBGHxm%2FIDEFfPceWOjQMMp%2Fz50NBk6npSr4Tkm7Z6dS%2FBNXuaPw70X0%2FXZgGTDN7PW8BjqkAaUr0r%2B4u%2FLGYXgj8659twvdtsp4wZb8uY6AeSnxLYPcJrrL%2Ff8hL3XJDgdh%2FSejn0Z7C7Z9abgmhDkmAlM3hf3XloX9GaM55CgQjtOe1%2FuWY5AumJpNfm19cWpWbX3lJL%2BDBYc4WuuqHHmNXem%2BaNSWhWKopadVhTX7b0r4jVSQLSIiCHXRjeGfLskHyO8qAS1KLg7%2FR%2B5W%2B3hrCDfXB9TN2peK&X-Amz-Signature=99d9477cfbf4a6f41d958bce760fe55f880a7b2da0da331aa3d161a58db4c759&X-Amz-SignedHeaders=host&x-id=GetObject)
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