

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=196c5bab4fa92b406062dcc85376195dfc3f146b523e41a3a997cda956f1dd70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=d5a061e33b27eb00293ccee061471359e24167ff9b9b45f6b16af3b57d488d35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=366021857d62320bff9b13add7a9098548a53827eb644e934123650c75580f50&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=5913f78c1ae8b5aa96f6703063d096e4a8c4a922fca8af5e16283253c1954d37&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=8af5f30fda3dcc350e4ef746aa537d7297117a4a3407bf9c97c326d23f7aa6b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=2a6e057adbb4046c562f19f8c70aa26fdceca94687fb2dcdbf212f25721b44ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=e0edbf9cc06cc4f4e1a0091155aec63111e2b961b1129fc697232f445672da95&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=89d552b9cbebdc3215965ee5aa286e07c2092a59b848fd4f0c71f3237020bc55&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=7e6dad97141d7f38150571642f46573bcb7ba27b23dbcea273b6d25292aa93c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWCR5TA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXHAP5OIQYMpG0l29ASFXw7OBrjjJobghQ3c%2FW1fIXMAiEA1exsqbfQoTTghUvLCN5BAJcAbLylMnITGe6cjgjLfh0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkOirenNy1zqf%2FxMircA2UToVBDcfo7V%2BGk8Pbca3nmV9StklXx4eR%2BVoS8MkrGY0FPLQCZ2VZSTbtXPp4qucxCAGzWion7wTcLdXbael6KNdAJ%2BG7UIhe6mU%2BqONh4SzBjPdJ3Rvu5ZhVXJKWuh3LsUi8TEZZjFNvs4%2BHB42okbOOMPlITI2aFQchLGcTNezzxfScuAqSs6d%2B9%2BQN5HoNCxVqasUnCZ3XIIqXN2aeup3acZdnRiCedJQx5ajGROMBBnu5Qh9Z9QI5sSK9QlI1Xz%2B2mkqN%2Fap1XfCBEGwxTh7HMCk1Rr8r9Y8%2BTJbJHroLUrgG4q2zJ2BFDjVfBnclQOBz%2BFgSH0Q%2BxT7Zoihuc%2BEXFQ2rwVziafoW1mRdl6QQYKdWCGxqybihZmMwMlTHW2vjZFT4pblbgfENx0XhuwfM8gaOJUabMyFMdr9PHkaKDmM%2BtLa1BiiAv3AY4fneOi4kyV2cPbqa84w7q3pWsDEIL4hjXpyBa7cfqwi5UXWhaOCw7Lo12r1YMbh1fQkn2BBVPMRRJbCfHMejt6FKDWZN0Ll41iHVbt6mF1ZpsEWJ7bulr0ESOvGU7zHr%2B0Ry1%2B2WEV3Pxa7gT1OdoMzG5Z%2Flv1pLHI6sQUjlIZrYoNvF%2BZq8KyB5%2BhfGnMJX16bwGOqUBs72pLKksili%2FfE7DZ%2BdphsNjGRVD1%2FCXHQj7GlA%2BglBGb9PSpC59VzBNOB4cXiIhFpITHPlPxRas3Q7uvC16BpyxeeFxEhyDAGus88hcnIeXuakq7uQAdaFh4z6JWNxpWZYyWzIcwFBwbjUooEuGcvjtxpqZ6B8IQZBwB8K%2BXXwHUydcVQhmcwP3W9n6ZhAjnzEPQ7iaxIgEmkrgB7JtTLvEv5Gm&X-Amz-Signature=0fc4d4ab7696b4cc7e84781269a259c53a2962ccf47249f756119155d5932b28&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWCR5TA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXHAP5OIQYMpG0l29ASFXw7OBrjjJobghQ3c%2FW1fIXMAiEA1exsqbfQoTTghUvLCN5BAJcAbLylMnITGe6cjgjLfh0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkOirenNy1zqf%2FxMircA2UToVBDcfo7V%2BGk8Pbca3nmV9StklXx4eR%2BVoS8MkrGY0FPLQCZ2VZSTbtXPp4qucxCAGzWion7wTcLdXbael6KNdAJ%2BG7UIhe6mU%2BqONh4SzBjPdJ3Rvu5ZhVXJKWuh3LsUi8TEZZjFNvs4%2BHB42okbOOMPlITI2aFQchLGcTNezzxfScuAqSs6d%2B9%2BQN5HoNCxVqasUnCZ3XIIqXN2aeup3acZdnRiCedJQx5ajGROMBBnu5Qh9Z9QI5sSK9QlI1Xz%2B2mkqN%2Fap1XfCBEGwxTh7HMCk1Rr8r9Y8%2BTJbJHroLUrgG4q2zJ2BFDjVfBnclQOBz%2BFgSH0Q%2BxT7Zoihuc%2BEXFQ2rwVziafoW1mRdl6QQYKdWCGxqybihZmMwMlTHW2vjZFT4pblbgfENx0XhuwfM8gaOJUabMyFMdr9PHkaKDmM%2BtLa1BiiAv3AY4fneOi4kyV2cPbqa84w7q3pWsDEIL4hjXpyBa7cfqwi5UXWhaOCw7Lo12r1YMbh1fQkn2BBVPMRRJbCfHMejt6FKDWZN0Ll41iHVbt6mF1ZpsEWJ7bulr0ESOvGU7zHr%2B0Ry1%2B2WEV3Pxa7gT1OdoMzG5Z%2Flv1pLHI6sQUjlIZrYoNvF%2BZq8KyB5%2BhfGnMJX16bwGOqUBs72pLKksili%2FfE7DZ%2BdphsNjGRVD1%2FCXHQj7GlA%2BglBGb9PSpC59VzBNOB4cXiIhFpITHPlPxRas3Q7uvC16BpyxeeFxEhyDAGus88hcnIeXuakq7uQAdaFh4z6JWNxpWZYyWzIcwFBwbjUooEuGcvjtxpqZ6B8IQZBwB8K%2BXXwHUydcVQhmcwP3W9n6ZhAjnzEPQ7iaxIgEmkrgB7JtTLvEv5Gm&X-Amz-Signature=05f57eece94cf17e5ad5f27c1d3b136b408ab1b2728aba46c9c25be2e0dff775&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWCR5TA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXHAP5OIQYMpG0l29ASFXw7OBrjjJobghQ3c%2FW1fIXMAiEA1exsqbfQoTTghUvLCN5BAJcAbLylMnITGe6cjgjLfh0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkOirenNy1zqf%2FxMircA2UToVBDcfo7V%2BGk8Pbca3nmV9StklXx4eR%2BVoS8MkrGY0FPLQCZ2VZSTbtXPp4qucxCAGzWion7wTcLdXbael6KNdAJ%2BG7UIhe6mU%2BqONh4SzBjPdJ3Rvu5ZhVXJKWuh3LsUi8TEZZjFNvs4%2BHB42okbOOMPlITI2aFQchLGcTNezzxfScuAqSs6d%2B9%2BQN5HoNCxVqasUnCZ3XIIqXN2aeup3acZdnRiCedJQx5ajGROMBBnu5Qh9Z9QI5sSK9QlI1Xz%2B2mkqN%2Fap1XfCBEGwxTh7HMCk1Rr8r9Y8%2BTJbJHroLUrgG4q2zJ2BFDjVfBnclQOBz%2BFgSH0Q%2BxT7Zoihuc%2BEXFQ2rwVziafoW1mRdl6QQYKdWCGxqybihZmMwMlTHW2vjZFT4pblbgfENx0XhuwfM8gaOJUabMyFMdr9PHkaKDmM%2BtLa1BiiAv3AY4fneOi4kyV2cPbqa84w7q3pWsDEIL4hjXpyBa7cfqwi5UXWhaOCw7Lo12r1YMbh1fQkn2BBVPMRRJbCfHMejt6FKDWZN0Ll41iHVbt6mF1ZpsEWJ7bulr0ESOvGU7zHr%2B0Ry1%2B2WEV3Pxa7gT1OdoMzG5Z%2Flv1pLHI6sQUjlIZrYoNvF%2BZq8KyB5%2BhfGnMJX16bwGOqUBs72pLKksili%2FfE7DZ%2BdphsNjGRVD1%2FCXHQj7GlA%2BglBGb9PSpC59VzBNOB4cXiIhFpITHPlPxRas3Q7uvC16BpyxeeFxEhyDAGus88hcnIeXuakq7uQAdaFh4z6JWNxpWZYyWzIcwFBwbjUooEuGcvjtxpqZ6B8IQZBwB8K%2BXXwHUydcVQhmcwP3W9n6ZhAjnzEPQ7iaxIgEmkrgB7JtTLvEv5Gm&X-Amz-Signature=b70d376cbc3bcca616416852c6d92809ddf2c3b50aeb1ec68c7874e397b4d45f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=388c8c471af6c0acdb653222e5b27c8f8f4abafc1cb5450514906049ca712945&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=f75b2c2d6b1a70284b16750159ed06e5803792b2858bc44c3535ea95493db6fd&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=b23642233bc658075eb504b5911cff6e567d2377709447df988bfd98ee546afe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=34c7297aeea9d7ee05322ebf27651dd8821330ceb25416a42b20efe506c7e65d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=95e2f32f28df7a6d2e46ca7f7712a72affaa1cd73c506335c76fc9179fe34bcc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR5LE6W5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpfrbTQJYkukfzSnxzR4iFcMvaYw3n6u1zMvAOtzOHxAiEAzacOgbzJNpHRGSRI%2BSkpp%2BjiNecudsZu038t7T502pgqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCuoaVruhtSlN7muNyrcA53b7YzTDHZ8dorlGkhGyVKuX34dUlzL3pCzSSMMQ15W11tGLWdqXRJ4RAnz4FeOPdR2wy4iNfWsf6qXgkQuHinsW%2BtxVXIC3vJ%2FGa4ewyxMzyV1LS4S7%2BvknW2JgOxnI88Jy27MgV5Q9T1lKdEJhxsuq%2B6oxWOKGMo5WCCizpTKIoKhS2s9ajq%2F%2FtqepX%2F4CDNWfd2pwEj6Jc2qkIl%2FsMVOAAjiT1FgasHVzt9oz3dXhKb7mW0gssZ5HwHcEL1ulyqkIUDUEAZA2T5xvSwnXsYOq%2B6ix9OxeqAngIyvqJBPT16dwW2bhj3%2FPkDTdaYBStDVB426Y3l4Bcu3%2FaRpUmAnBgnRE5cjve%2B7qQmFCFWc0oYz1bGJo8xVOo41dsmHmsNbzZwkXxvFjde1lFeTbmuBaVoddYn6H9%2FjhDMDe1DqPXA8mwEQP8PiHj9eq8akmk6iZkJSw8byjbFLz1Asl3%2BT75rgoxITl%2Bg6Dzx0yxrbUZgi5BMmPfiK1wNcrNzFwwCbCfHaGndUjkiG43MBKMDvAP3dkB8NiQNZNgXAiXC26zAEwvv6%2Bvy%2B90KJCo3IlYkeNEHcmjfa3phumdCdqT0WS8SQgKeZvyCmRLHa59CJ8%2BjGMYQV9XrPCJCxMM306bwGOqUBK8yjPJV1oOuTfOpII2k41CERP9dfrLEm%2B2QgYRGH5x%2FBSeHqi3jwsfiYwaNl8iS1ZoRqManoh12rKCCRzrZ%2FPYqFsJ%2Be%2BxxnrjqmK7uxt1c8OUN2sS1c5P1y1OwIK7BERuf%2BJeWJeaP%2FReMUY3dEnH2nwD2t3VJniiX9qHR%2FuWCSVDKhk6nCMu9Rzt7vw0pt%2FJDYx23k4tLbastPtG7SiBrakf9q&X-Amz-Signature=e6e64b7f987f787b9bc5bafdc22a3dd5658328b58840593212a857c3807f79e3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KHLIRQA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMHMFpAC%2FKfDg5I%2BPYL89glkdWZ6seXa1UfAcxgD%2BI1AIgI4TU9eeBgIDkjv7Hc3NUVbrhtS82APurVL6fDwv0XsQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYidkZzd%2BYXIPmNpSrcA7rxGWos5weQ1eeUiVjIXB9Ha%2FQuevq5s%2FeqNTf28wM7smWNvlJPTrS%2BAq2oemW8XwYjCt%2BFjpfYksW2CMc9ayApiWkDJw85D94lQHQ7LWlSyItkby1191P0xCnkZ4KH0ezqybNJ4uOQKEdUR07gkw9%2Fqs543ZtfBEfAWUdaMYk2Aw0296jGqNQfIY%2B4d6l9au66izeCf6fdAe%2BfM%2B1qvTGjFjsoC7PDtokmBvkQMfSJnSxe%2FWM9U%2BLDlala%2FJH7B2tWMCXUG%2F7BM6uFEjrf8MVbuFKEBfEr%2Fb2wrBlBRE%2BVi1uywGhv2M1cs9LWz6Z25qKrAKsWDIcIYk9r3w0hNPBB%2Bvg6jWxJoNj5m%2F9N58UahCGM%2BV1HjRF1asIv0zLbvE9Ih%2BJKhIYKt3jrUYSHCxaF8vuf5z2xfkCJR1tNEWMRNStdqLPem3yBPadKAAhkiIyl4G6gHZCdDaqZvJz7MH6egnop8lqJrhnn9CW%2BRX2bbljW4j2f%2Boy9sDxFVwoNITAl4l1uqw0oHb3HS1zi50KdrMWfMNyatP9OIx%2BaM3L5yNNlVET9RZnMC%2BzBh9BDVUmwiX3q205VYK7wlzZf7p9Aes%2BxDvRqyYYUKRjPHj%2FZ8hAxjQUu5VvCnsvxMNf06bwGOqUBdXj3cyOq4EkKCVlKDbhW9N412HIUXX6VInqfUDcfjq95ulYtIKE3MJxqJUHr4qSdhoUUz79kJFh1vsTjm9wbtHTDRkgona12Kl1W4Md7w9IpZ1MEtJYXg6zxKpdprzN%2Behu1%2B%2F%2B51QjnlqDIkmsO1%2BokVJAl44phmR2eFFzHgG0t5ucWmlxA4sv2uAQd9%2FsrDmDMbZz5UtiOWZiaoFg%2FF0PCCLxg&X-Amz-Signature=2608ff1b70ee5626ec6402d70253e5a5556ec568186b07dd92736e0b37619b45&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KHLIRQA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMHMFpAC%2FKfDg5I%2BPYL89glkdWZ6seXa1UfAcxgD%2BI1AIgI4TU9eeBgIDkjv7Hc3NUVbrhtS82APurVL6fDwv0XsQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYidkZzd%2BYXIPmNpSrcA7rxGWos5weQ1eeUiVjIXB9Ha%2FQuevq5s%2FeqNTf28wM7smWNvlJPTrS%2BAq2oemW8XwYjCt%2BFjpfYksW2CMc9ayApiWkDJw85D94lQHQ7LWlSyItkby1191P0xCnkZ4KH0ezqybNJ4uOQKEdUR07gkw9%2Fqs543ZtfBEfAWUdaMYk2Aw0296jGqNQfIY%2B4d6l9au66izeCf6fdAe%2BfM%2B1qvTGjFjsoC7PDtokmBvkQMfSJnSxe%2FWM9U%2BLDlala%2FJH7B2tWMCXUG%2F7BM6uFEjrf8MVbuFKEBfEr%2Fb2wrBlBRE%2BVi1uywGhv2M1cs9LWz6Z25qKrAKsWDIcIYk9r3w0hNPBB%2Bvg6jWxJoNj5m%2F9N58UahCGM%2BV1HjRF1asIv0zLbvE9Ih%2BJKhIYKt3jrUYSHCxaF8vuf5z2xfkCJR1tNEWMRNStdqLPem3yBPadKAAhkiIyl4G6gHZCdDaqZvJz7MH6egnop8lqJrhnn9CW%2BRX2bbljW4j2f%2Boy9sDxFVwoNITAl4l1uqw0oHb3HS1zi50KdrMWfMNyatP9OIx%2BaM3L5yNNlVET9RZnMC%2BzBh9BDVUmwiX3q205VYK7wlzZf7p9Aes%2BxDvRqyYYUKRjPHj%2FZ8hAxjQUu5VvCnsvxMNf06bwGOqUBdXj3cyOq4EkKCVlKDbhW9N412HIUXX6VInqfUDcfjq95ulYtIKE3MJxqJUHr4qSdhoUUz79kJFh1vsTjm9wbtHTDRkgona12Kl1W4Md7w9IpZ1MEtJYXg6zxKpdprzN%2Behu1%2B%2F%2B51QjnlqDIkmsO1%2BokVJAl44phmR2eFFzHgG0t5ucWmlxA4sv2uAQd9%2FsrDmDMbZz5UtiOWZiaoFg%2FF0PCCLxg&X-Amz-Signature=8be115180eb40128766f4216f7778fe91c5e4fe9d38374a6153cbbd13bf0ba33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXB2R46Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcrdaIQ4fsV2XpmHFTxR87%2F3kPhijcw88Nl3ETjs6QRAiAU3zel1H2WMQovkYj68lAVgz9cjpdYL4nU981XXa7rEyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMP7dXkhWWeLix%2F4zpKtwD42FwThHlsR3yubYzSRTosb4YViYnVUb7TSsx%2FpJet%2FeMMIeDj5CnYGqKn2Q0B7E0CkTEReC1z4I7d7ulgP7svOn0B8VI8AOsO5Yz%2FGeT1bPMqtfGh1C0hVoZMqQP5gvYhv49LXhhBVSR5tMxE231QY5%2FwaumIuI2nYsdPOGA6xbMF%2BjNEtd07TqNmV2CaWMFAp0EqosUu06XRxVIy63H33chKh3Nrie5vlpLvpeqV12TW4dfVQHMQOzyPgvvk96WlrHT4BoKXsYQhPHwRFXhNjy1oT4VgYKrDGWMiSAkAVawbtvIZxRRv%2ByrnjdbQbuxRPcyaCaA%2FtSXZnXFB86lCW67wFLesiACmHb9UuLQXEQ7xC8K5uG18D81rd5tO7N8yVANmR2aaLNXVr6OBCqEGb5j4H2QSbza51nuBN%2FJsT1rFjwLn%2BwIBE0aguLg4IJ3ljrVItB3BSYxff7acMmw53QvBlqAWialhysBJpu3N7%2BvnXb2Qpx6UyvJv32b2Gp%2F0RyguGIVrctW%2F4PWlXaUiUN5rXpszWzZ3iYgRvkEdcXp3Q6wCe64YGmZy8RMdlhQKtw0%2BxWeONLNbGCOWP6UD7NvZEyTf04wBN%2BgNK1Tuohd8Isbe6Ge5rsQArgwrPXpvAY6pgF7iBzw8v77psS6Z2Zyld6jBhNUqi9JBQI5VFOUPpVtsLLnyGtKY2Gkq3C5p4ioNtxoqpsL%2FPiaV6I3%2FVif4NzN5%2F3wiqFgsBrf8fIR5ZkhVE0%2FzoODnpy5GOmQ2sK9Q6fJsie4ob4mnZGXludVbitKcGHJP5jSTSUcyFURmZKRm9hFsW711%2BecaAiY71hVapXZACA8j5E%2B5ttEzMMGW1Mi%2FEy1BqDa&X-Amz-Signature=30ba9b05119857f049016736acac0e63761beaed0891bcd43e9b52f3f2a4912d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FOHDOXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoXADxjz%2FMH%2Bq%2FkAZO2w%2FKiJfYKzDFY3PFdloNTxN5hAiEAzyosNGX9HItpsx7cJzD85%2Bxa8SPbceoopOImq4deuK8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlXPwdQrDog1B%2FzDyrcA0ptJa2IprTQBpTbYKuq%2B7szfUP4SeEYhz2bBWl0SG5rujU1PcnmjJs%2BVuQQqDXfi2jYvnwaYMZCl1WY0gyTwFzSKSoUz%2BIpRZgeST0qFC6KQY%2BGOsbsa7iyYRsbhJlaGSupJrmO4tYiq42nCC5Y5K9YnT%2FzYwgRWft73snSqLE11zKp3CRHW4u1vmXXa%2BASJcPKjaoWPROcxAkCdJ%2B3%2B6LMUsUiClEBkUPYF2exylOkJJwzWd0W2Eilu94vfwZWxnq%2F0GF5EeYFvfDS%2FB2MX%2Fl6U6C3tL9rNaCiJpK2UPzoBtVha5wunfnyeUSv97pn0nZ72Y409fQTIh836Hnb1yrrzUbSCiISBMk09Vayu5veraMVMS%2Fz8wDkd5LQtqsFSMC2mzXMh77qV8%2F5ijR9%2Bmt0VxzENkOf6XBTfukGjBgxReIELR%2FGdGMBoyCeCsqFbgpv7vnHP2CF%2BOtrZ%2BBvxJLlPkWPwDPrnGPSai1Bcll7bQ9so6maJxbA9MEptUUagzqZzdcHLX298Bsl%2B8IftCJipbDuDYTyaXfKLTGndSQqC7wvPe%2BqwoCmYYu0N2GAT3wQ2cxkKfRBmVFTeLMPB5roP5B9FX%2Fcwg%2BNx9XBHWu%2B9HxbffOtLqIsFY9OMM306bwGOqUBVcpR5jxO4u2P8IxtWszWGUUYmynP8eGz0i99%2FqAcFZtjrWZEd2vSrEqVVrx12naM43QEw5jv1WqJqPlPEUi6YppOiRQ%2BekbCKtikQNhnk4NsbD8qahHCMSdc9PTZmRjo9DIAo39L6Jsj%2BNfgRqXxoQurRdPIywrx%2BsEydMrV24I3Q8RLV1BaPyqE7Vr0vtJ0NUASClDYSAf3yoOzmrYxHUJIjOik&X-Amz-Signature=548381a40a5638e96ae355940e15daa9814ae9ef7cc7746b3f12d9b283b2364b&X-Amz-SignedHeaders=host&x-id=GetObject)
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