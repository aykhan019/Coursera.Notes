

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=5a0da237088a4d4ab18532e2de1725de5900920bcf92590243415479a846b3f4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=08247f6b65ea4620090b5111d080be9c111ca864be9f7cc3274175a361a4e55c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=54025e6c10562e914c89cf3fc06a8364cf37372c88f249bc3555bb964c1d9583&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=4780de1fb9d95b306a78fa76c6f5ad67db86e6716e97953290ace6c9edc4ce8e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=d2d167d3628bec421d11d331f66d61c7d1453ea55087872f6ab0ee8d518c25a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=26136412562b0669dbd5a0ca0f0b411b8d081816fe1eac0eed389e2d207806fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=46d41431eb88388313d0d189fa480c9b50665785dc2ccb2dc5fd6b008d20fb89&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=e5f69dd112e6e59e35c9675eb211b3ad6c70c096c79a0c4c0292a149365684e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=b26247a7153dc53014ac796e52d4ab3d8f98db7a74bd9bb6b66924d3f6764ef4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHH2HPSD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICHdkpWY13XA%2BpTC0nAKBQ8WfUL5YKBRb7%2FZ94dpWIefAiEA4gtX%2FUy9p%2BPoG0eqmVIk1eJrxSDu0WFZl1fWaeAuYGoqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE809nKLA1PsNaBE2SrcA0KgyD2iN2I%2F3NK%2BKt75Tg9KBLHFZJnZz852Wd3HrKrKx%2Bu1BsJq1lctMwKKevaeGPIKF2nftAStLhUHgiJ2Xn7xpRihp5mE0NJC6UxIvRW3zy2nN3UETN%2BqfrqaCcX7A30knvBkLssAuD3JGflwKvaQZt3BcsDirpuBZTHWoQCkFdjVye7E01MKkkC%2FdqLNzEJJ6mXmb%2FjYGt3EQyflbmfQOd5XwMLgrb9HV%2F83k1RICmQm0gfK3ryNDs9QuSPQavX81v9cTGjL6zinEFoHWAvs4ulZW%2FX850%2BCJrk%2B%2BhPJvso4xWgA0rYa8XF0XrQamvlKXM37dB%2BQCI1rP4bB32EC9cux8Y1cm8uW%2BivYn94Pn6gm7G1xuSkFEqqMjQq3f%2Bkxt7R0um1Dw22RegL5vnoVpMLmmOLN72OS2ckToCojTQfDx4IBpBXyVvYgbKySNw%2BYvt7t%2BUQuyUQZUJtnqpeIdzVv%2B3LogTMeFVqkZE4a8202krMt3J%2FDkniK%2BH3ClGWEfSEKHkXzbpFPkDyEYMeUAlF3rFm8%2BXlm3EIYudTfrDWU2%2FPGEinZoIPNVTO5PeYdJfgnEhi%2BwJplVGSiwCdpO1tG5Jvc1bXRDUMBiWBEW8eVC6SFTD%2Bzh5uJMPmb%2FLwGOqUBeZZeBs0S6IPGcGja7o4kVXkzho%2FRnmeLzAbVN3IdrAPOyINdEgc%2FW2pGwX%2Fic0uwUqngBI7UfZssEcyiClQnt%2FRueWzsV%2BnvWmVSMzkgAexiw4jTNuTbqXrAfqfKXwYE6wu1Qu5BlZoNaGBb5ZcwB6j9tdLB99yBOAIeVe4H7tdwBkMMETlVsuo%2B5qaGYsImm62NYHCQWuVR52%2FyylHvUB8BRTlm&X-Amz-Signature=f152dc3a560bc7797bb2e21f7de12ed3f5ebc1e7fd09533d1afb9ef68cfdc809&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHH2HPSD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICHdkpWY13XA%2BpTC0nAKBQ8WfUL5YKBRb7%2FZ94dpWIefAiEA4gtX%2FUy9p%2BPoG0eqmVIk1eJrxSDu0WFZl1fWaeAuYGoqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE809nKLA1PsNaBE2SrcA0KgyD2iN2I%2F3NK%2BKt75Tg9KBLHFZJnZz852Wd3HrKrKx%2Bu1BsJq1lctMwKKevaeGPIKF2nftAStLhUHgiJ2Xn7xpRihp5mE0NJC6UxIvRW3zy2nN3UETN%2BqfrqaCcX7A30knvBkLssAuD3JGflwKvaQZt3BcsDirpuBZTHWoQCkFdjVye7E01MKkkC%2FdqLNzEJJ6mXmb%2FjYGt3EQyflbmfQOd5XwMLgrb9HV%2F83k1RICmQm0gfK3ryNDs9QuSPQavX81v9cTGjL6zinEFoHWAvs4ulZW%2FX850%2BCJrk%2B%2BhPJvso4xWgA0rYa8XF0XrQamvlKXM37dB%2BQCI1rP4bB32EC9cux8Y1cm8uW%2BivYn94Pn6gm7G1xuSkFEqqMjQq3f%2Bkxt7R0um1Dw22RegL5vnoVpMLmmOLN72OS2ckToCojTQfDx4IBpBXyVvYgbKySNw%2BYvt7t%2BUQuyUQZUJtnqpeIdzVv%2B3LogTMeFVqkZE4a8202krMt3J%2FDkniK%2BH3ClGWEfSEKHkXzbpFPkDyEYMeUAlF3rFm8%2BXlm3EIYudTfrDWU2%2FPGEinZoIPNVTO5PeYdJfgnEhi%2BwJplVGSiwCdpO1tG5Jvc1bXRDUMBiWBEW8eVC6SFTD%2Bzh5uJMPmb%2FLwGOqUBeZZeBs0S6IPGcGja7o4kVXkzho%2FRnmeLzAbVN3IdrAPOyINdEgc%2FW2pGwX%2Fic0uwUqngBI7UfZssEcyiClQnt%2FRueWzsV%2BnvWmVSMzkgAexiw4jTNuTbqXrAfqfKXwYE6wu1Qu5BlZoNaGBb5ZcwB6j9tdLB99yBOAIeVe4H7tdwBkMMETlVsuo%2B5qaGYsImm62NYHCQWuVR52%2FyylHvUB8BRTlm&X-Amz-Signature=2eba623ce3b1ce112b69c0162040762bcbe242bc6bdc413c181e8c7761b43766&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHH2HPSD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICHdkpWY13XA%2BpTC0nAKBQ8WfUL5YKBRb7%2FZ94dpWIefAiEA4gtX%2FUy9p%2BPoG0eqmVIk1eJrxSDu0WFZl1fWaeAuYGoqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE809nKLA1PsNaBE2SrcA0KgyD2iN2I%2F3NK%2BKt75Tg9KBLHFZJnZz852Wd3HrKrKx%2Bu1BsJq1lctMwKKevaeGPIKF2nftAStLhUHgiJ2Xn7xpRihp5mE0NJC6UxIvRW3zy2nN3UETN%2BqfrqaCcX7A30knvBkLssAuD3JGflwKvaQZt3BcsDirpuBZTHWoQCkFdjVye7E01MKkkC%2FdqLNzEJJ6mXmb%2FjYGt3EQyflbmfQOd5XwMLgrb9HV%2F83k1RICmQm0gfK3ryNDs9QuSPQavX81v9cTGjL6zinEFoHWAvs4ulZW%2FX850%2BCJrk%2B%2BhPJvso4xWgA0rYa8XF0XrQamvlKXM37dB%2BQCI1rP4bB32EC9cux8Y1cm8uW%2BivYn94Pn6gm7G1xuSkFEqqMjQq3f%2Bkxt7R0um1Dw22RegL5vnoVpMLmmOLN72OS2ckToCojTQfDx4IBpBXyVvYgbKySNw%2BYvt7t%2BUQuyUQZUJtnqpeIdzVv%2B3LogTMeFVqkZE4a8202krMt3J%2FDkniK%2BH3ClGWEfSEKHkXzbpFPkDyEYMeUAlF3rFm8%2BXlm3EIYudTfrDWU2%2FPGEinZoIPNVTO5PeYdJfgnEhi%2BwJplVGSiwCdpO1tG5Jvc1bXRDUMBiWBEW8eVC6SFTD%2Bzh5uJMPmb%2FLwGOqUBeZZeBs0S6IPGcGja7o4kVXkzho%2FRnmeLzAbVN3IdrAPOyINdEgc%2FW2pGwX%2Fic0uwUqngBI7UfZssEcyiClQnt%2FRueWzsV%2BnvWmVSMzkgAexiw4jTNuTbqXrAfqfKXwYE6wu1Qu5BlZoNaGBb5ZcwB6j9tdLB99yBOAIeVe4H7tdwBkMMETlVsuo%2B5qaGYsImm62NYHCQWuVR52%2FyylHvUB8BRTlm&X-Amz-Signature=d6f00fcbfc3fe42d1608f7b0daf0b3e4e8e28730303056c14732857d04dbe90d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=3d34ee4f0a1b4c5d8ba01aaf20c5730cc3d97f7b14ce101beb52f576829100fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=35a0990f59fb907432572512a2d54bbc7c884b2cb3ca3ee4c96b526e0f92d32c&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=0df4450db5cd3054b7fb934a51587bf26e1f2afad0beb709593b68f302d76ee4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=9d8a3eb2c4217774cced46074b7cb0adb3b37b4da30448ec68bec251b34c8654&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=543a98a6e45c9bc27a67aed2246678adfce0a28e196e856982e2abbdb7c9fc51&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYWT72YZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJO4a%2FVi2WV%2B7nQTso%2BTpYsGuBbRWQlwnUXeM4ctCMOwIgal2ztyVHgDfYOynnedpEYcAT6zzHGRNSG3MaIkWEQ2MqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKE%2BVdokBXPXxGi3CrcAyFT7agDCQIo1Lqg6kQ1krJJahUvbQ1MdHPjcfw0Wao5f%2BCcWSQPH5D4d4AnSpEKv2QcS5sfruZ7EJqnyU0c1l0JAhsB4IZPBNevdYURK9dhz3X0eko6WBSBH%2F8ZA%2B9HFilEBDrCUB4hWVukHg5KuNr7DwESBZoctrA0%2F1U20lc6k9LzO8KxPr%2FGJECJR838kdBQLPI6vYbY8MvfB1GtMWxN4zHY1mJVR5%2B05pDHTIckyrcORVkbht2sRYK%2B7UIc%2FkmpJ49VTc8ZK362bRqKOA81ZDMZlX9LuCugEC5unVVCnBmyHdjMUPlb3oZ6dzcEmgk%2F34cGcOkLP6vovi%2FSHqUSoy0MGg6LEEDHyl7FEMrhQw%2BbNNakRY1YKhIOv2r%2FTRUUgJ%2F0Cz1xHCm7aO5GIQ%2F1Ya83J0RLmdGuFOlN54Grd9AcrEKCrh8kNncFIWa73IsDOcGoWnT%2B7tCfAUel3p%2B%2FYcoPmZKghD6KfmROOgHu3QWvuwXJNs2XknX7L7LMY59116P56jYWJWviS56rHI38UlismpRtVdAkobqg7biceuyS1mQ7ost1dY%2BlO5ylqKcUMQT6TCYEK2%2FJx38CKMBR%2FjZIkvtP8MAnRpsMkJm%2BRjlqURvOb2H15xmnMIqc%2FLwGOqUB99eqp9ssoY2OGYqUfbzsJX51esFGERqteDDURmRvTMJYFMyu05bKbgKaXxR8D0I2kZ1M4vSyIJgK7GA%2BwbRPwZaE1RQcGphjXA8T46YT1W2W4HZC7kYQ0EgG9Df9K35OM3I%2BbpV8GPv%2F31mC%2B7n9MDk8Y49Qj0lsBjuYuDqSF2DdPvBiOEs%2By0Bwoi4ngoBW1Yjs0rDkwrCztnvpRV5MsarV4LHU&X-Amz-Signature=d77e8dfa89d2b6c7e67bc0aa40e24f12cb300ad1cb8f24cde0d7a7b7641d4977&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VDA6VRW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg72a9b8kUofnMa7F93oYggNv0uAE%2B%2F%2FVYguN4KZ3DFgIgLH3d6%2BN9dTquTpFYZSQeuZ%2BuTe3ZF4uMulKQixauykAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5TnHNrYbOOzK7XwCrcA3gGxm6HaOAwtFIMnuDnVcPHw2es5FCAG63CVrvTpCmtmU8BJvm077wF9maOg5n2j4tOsSAOyu9tla1xkM4RnQbWXywzbIk%2B4QvsjBwYiN%2BTh8jCv%2BMTegGbMEc1lp3RP6oAnU%2FLc8lwpv1mO0AOp6LllzpLgbqGvsT7si6NJa2zBvSyowMolLNZv1Rm2oL%2BM%2BrLq7wY1iqjDJH3pjNar7TQZmqvkemxTKrXQpxOohfGOj7K6Ht%2FbJzKTAUGwnBB5NSNd%2B8DgmcRTy7sYTjA6Fn8CQq2HCoDGXb0wRup7oJnO%2BqoJfKxlIOHwFE36PvQvSEP8dsLw9kzK1E8%2FIs3vIncU%2BDVmW2UNzkJFINVBegrM4TOXcK8S9%2FctiS4KX7rgA37t8EJk8YoMMuXWlJ3BnKj%2FuuEvySbEOeQVHEqw7UACSOK5x4FOefoZU%2FxqWmqYqztCouBm97S8npmgFTtCN%2B8TpZWK0V3IKbvfbBb9VBFXgbqbXb1upvVcPabk4v0iDdtFZTdCibkEGMAHacbO0ESzgJxxIweICt2dZtpFgc8si%2BPPm%2BkaTwoOER%2Foxe3SV7Bxc%2FLEdzOAhq7I7HB4hCczUKddcrqmEDyrd5hIqowN0kVzqIa8pXh1UVDMLOc%2FLwGOqUBuD9t5JBNcnydLZcW%2BP%2FORPEMJzpavFibglIjv9So74KnsvbC91GxDpSob3LLZq%2FQ%2BptCF0Z4qwihm6OgVaTbuQyA40g8gYtlhU24FOhEdmKIbzywRMZaY9GLuivc64sHRJ0Is1VmE97noDtZeAdYKh2RkjY7yhAbptaVXCMu5wvr009z7g7iIUjTMQ1f0O2qQehTwHLHPR6XBXQHQoXiJJiyqZ4L&X-Amz-Signature=ed48d7cb6c7d9554e715d40ca3085217230e2e9ca2b4ba68a09703d9e658db58&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VDA6VRW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg72a9b8kUofnMa7F93oYggNv0uAE%2B%2F%2FVYguN4KZ3DFgIgLH3d6%2BN9dTquTpFYZSQeuZ%2BuTe3ZF4uMulKQixauykAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5TnHNrYbOOzK7XwCrcA3gGxm6HaOAwtFIMnuDnVcPHw2es5FCAG63CVrvTpCmtmU8BJvm077wF9maOg5n2j4tOsSAOyu9tla1xkM4RnQbWXywzbIk%2B4QvsjBwYiN%2BTh8jCv%2BMTegGbMEc1lp3RP6oAnU%2FLc8lwpv1mO0AOp6LllzpLgbqGvsT7si6NJa2zBvSyowMolLNZv1Rm2oL%2BM%2BrLq7wY1iqjDJH3pjNar7TQZmqvkemxTKrXQpxOohfGOj7K6Ht%2FbJzKTAUGwnBB5NSNd%2B8DgmcRTy7sYTjA6Fn8CQq2HCoDGXb0wRup7oJnO%2BqoJfKxlIOHwFE36PvQvSEP8dsLw9kzK1E8%2FIs3vIncU%2BDVmW2UNzkJFINVBegrM4TOXcK8S9%2FctiS4KX7rgA37t8EJk8YoMMuXWlJ3BnKj%2FuuEvySbEOeQVHEqw7UACSOK5x4FOefoZU%2FxqWmqYqztCouBm97S8npmgFTtCN%2B8TpZWK0V3IKbvfbBb9VBFXgbqbXb1upvVcPabk4v0iDdtFZTdCibkEGMAHacbO0ESzgJxxIweICt2dZtpFgc8si%2BPPm%2BkaTwoOER%2Foxe3SV7Bxc%2FLEdzOAhq7I7HB4hCczUKddcrqmEDyrd5hIqowN0kVzqIa8pXh1UVDMLOc%2FLwGOqUBuD9t5JBNcnydLZcW%2BP%2FORPEMJzpavFibglIjv9So74KnsvbC91GxDpSob3LLZq%2FQ%2BptCF0Z4qwihm6OgVaTbuQyA40g8gYtlhU24FOhEdmKIbzywRMZaY9GLuivc64sHRJ0Is1VmE97noDtZeAdYKh2RkjY7yhAbptaVXCMu5wvr009z7g7iIUjTMQ1f0O2qQehTwHLHPR6XBXQHQoXiJJiyqZ4L&X-Amz-Signature=7b21de4ce282f2676bc7310c9a5209d960a2222ad2ed7d2c05bb53f0872b96b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQV72NHQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETJco2iKEmtiUY5qzRaNASr2KtTHGFauXu5Xj0yBAaLAiB2ovslxNeII%2FOC4Ns93s9od0ORC3s8jPMkDpmm86PRBiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRbTkmoS55eW4VLlnKtwDqg0vxmTtxooJVJpuAqSWXtGgItss18XunRtff2W8KoxJNNuNJNehy20JtjfLgVw1qzuZm0ar6iDJArsd2G%2F3vPLhdehHdb2J%2F3RyE%2B%2FvXzlGdjCB2qXNb9o14q620kXNJsJepe6xGpZ3jouaUJLiZ%2B7s1AuyvTZpIqVGYr8x%2BM0Jmp4iceFxv7%2BEAye4s8dMVBJiahzQ%2FjSAvxSbtOJaBtU6aigsiOTw%2BJUSHbhK6DxZdPDovujIUmPxksjWmofTiPRrwrEQBYsB4ekCbxm0OglRli31oN3tABJT%2Box9%2F6DXRW6uYIied20ImYABB%2F5V0wKlu%2BziRFS6yq7KXIF7GT6qByE1nWmd%2BXOz2sv9jjhd6Hz7PA4bhY7DUbv%2B2LoQ%2FFJgeJvEkAzp7lGfNTlQ0GtR%2B9M37T7st4Cbj7Jb%2BTvDg%2Bp8LQLl%2Bawuh%2Bf1Wn8CWhCBiUIp%2BHuO%2FeZqqXIRG5xLKjbero%2BIfpW8AnPWVWE8fmOThJ3hag%2BWCry5IIjJYU9ZCVMhWWmqrEG78%2F5jFWSyreCsdaAUsF5dtlQPRlSGlbXSET0YyCgCfV1QUlP4Ab4wqahpjgS6tQosymwxwhxO65BuEV8Q%2FgQASNPMV62DTtuUtbnPMIBVbhEwzZv8vAY6pgHMKeWhlMDK8HSTgGcv2otwvQZGeerA1WcoRjP0lWg2fECqiW7RU8LXbdJfv%2FHu%2BksJcjf5gZVbdknrAFguIpGmCG1M3%2FSVynXntBhPxaFnQy3xGbuBgitj2TEhXngDGR3FbIKML11iA69CGuqiKPWL%2BJOSWcMYGY3D%2BurDIRP2Wz%2Fp7fqtwQ4b4cUlxrnNDUcjNRct1wmEjhHkv9Mulb6thVMkFiCW&X-Amz-Signature=32dde887aceb973053a9b736232a91eb2e9dd7c6243c72b2797afe13d0fa93ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XLRYVPU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1WWDGlFtaS4l%2BlraEf5rJ4jajGWRChHUVdzVdokGgwwIhALGZqCMH3JkMHJ5CFe%2FyEsi9NmUqKMREzCR%2B%2FvqmYsinKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B0yASs0XJMTMM2YIq3AMoZ2vIvOiLG%2BXtPeUud8vMdUbN9dwqxR0hMjmEdQuc9unOJ4R2kjr6d7wN4YGAWQ62NPtjmmSHrkZQdlb9HOc5pqGA64FASNWEMU5MdcY3ZEdi0%2FTsdP5TtQ7VHa1Sej3hQx%2FhrowCuf1FlCRlLCrAbpHB81ZTbIiIuBXWcFn2YK4ck8tbotoW8Cbd0z0a6wmiFstRgo78Mnn8jT3D1EHpsWWxZOp6NH3dmxtQSRKCnNLmF8puRVCKW7cvssNt4YyXrI%2BNhMZSf7mrc%2B9vD8XMyh9rrmYiYQBRWQ%2FqmoNiS6fARj1%2BJieInl8ySuUYSzOtA6zAZT8%2FcDoGSFgVJX9J3bZZ%2B6lPX6pQjTEa%2Bc1cbp5QnN%2BPOWTqSYm6NaR6z%2BvADQ5Flt33XsOkPhbWLRc1omRiuS9RHa0deDp5ggs%2B00WDSsyU2fZf9jF09LIhAmsvGlhGPCnse%2BZ%2FtWLaPdNk6RO58qkapRBm1bWsz0BtHZ6XgBxgScDI6L9TBi601B6odcg63s50k2yIbYVbqxRz0r3V8Mw309Yteh7T4WZ22nKWgHqn%2BPc6nJZ4PosgL9TT5cggJW3aOoZuxfXhYOHdKTiD4ryUNF2HGQyk28Vy1jN7avxSqfezQEnPUTCznPy8BjqkAWNCSZVgi9HStUUfy9%2BImMcIsdYIj%2BfMgWq%2BzRq6civS8lUtgBvx9mJ7h3S190SO1eXf6QcKU3OtcvaBEYuHif92FmDk5Q9l%2BYc3J%2FBssu6MeD4YOptSfy7G%2B5CmsIFevNwuA%2B26ggckxJCVoYFvWJw9WHDyhm8I2LXWMWkmg4a3Ptg8ypKyZ04TrSFR9VNpwc5rj4pXULLSylZ5lCO8yHHr1c9Z&X-Amz-Signature=85b2e4f9a90c192c8b42dfef6d6a357f05a1a502479193863a2f3a7bebe9b7f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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