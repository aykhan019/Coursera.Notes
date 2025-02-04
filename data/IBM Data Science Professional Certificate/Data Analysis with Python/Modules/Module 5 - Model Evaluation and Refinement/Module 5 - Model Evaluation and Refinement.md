

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=d82ebfd47f3ed06235d34142c78d583c36dfc722ec63052864549da0d762c38e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=312150226ba13d04a2badc45757abafaa24cd3d9b806e956594b96ff5314c65b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=e79dd310e443afe0f6854538c94802814304ccec2473903f430f81c206afd7f4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=f2bc8aee2f43dbd43ad80def79354e4b4409a3e1740f31cf628f7003edc35db6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=621ad9a7d516ead7dc6e1eb84394531eb6dbc77e61b31a54e3e06392c9db7411&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=900a576348afae4afeddb9a2e3f6c48c7e075691cc34ba28217e1be458ed88a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=af0622b7e0b7a9724f3ecf42ebb2dedcaf69a05d89d58e29c038b918c722e2a7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=e67637363957de44b4d86d53c63ab0bb4247b6f35cc1e0153f9b62becb1d2116&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=76ddb516feb3a110b9fb5a4c18b343463e9fcf228884d903434c113f6d74d6b7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYWOORFR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDUrDmN%2FtiAdET%2BTrmyfiKBwVK4ziEpvD64p43Ysn5sJQIgIFLH708SP%2FcZxgjk6KP2KWtXLHfMP%2Fyo%2Bkl%2BZkTkFpYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDHaBz6uctDBm1cn7fSrcA0jJzORTdCfy4SOcKYf7wEysBnjizPOnxOdtLBnFMN9m5BH9SQMloq%2FTGLPf1y9eW764PzZlnOZ7QYAT0Nfct5i9Obf1qyhwoc1XrbYhK3kjvVBnFlM1zQgcXpKAHoWLKc3O%2FAoFddUJeVCUmamdYYMOn7Q9wveQq7Jhf6IowHc6MWExqXHtwvnfkq6ZbKcAgEAZaaTGaAzR%2BFNFx73Ce%2BFs3cxgQsdlHVt%2BaKSXEjWkHDUvZNFX1KcgZYHAWmKOg6WiH6L5A00S2WwOOYnXEpKlZWGxzNM1DaR62SZmw88F%2BosB4ep1dHu0%2FcTNQpVjUoLFwx9urAxG%2F1f0WsrK0gJns1omP1QB%2BnBNF%2BIozojSF%2FJ08wElLkillsBU8O1CzFPe%2BaeTnM37gxPlF%2BsWodCBRZM%2FuN4g36Yxk7n96xUIpBzAZkKJihfb36vfLgleijEs%2Fx0ZrGcbUp0DhrirX66Vxf8aIHN5zv4K5JDP2TyjAgFy%2B8VE6yGlVMzVGCPc5h%2BoGxEBmzUyyaThzgtSy0m4JvCyQS%2FIyx9sfD7nVbhItU5fRtFx8OeblzqxT7aqD1sxo%2BSpJtOEdVQTUtO5ov6rZXHunKa58u1RwNBp57AkHrbnHkH72Lk53uF2MIOeiL0GOqUBXpku5KJj91OkmgOLHkNkBmagZeGiyl3Mf4x%2B7RQ0akBUU9eXgtVB8YXGoMb6LteuMQ6l2X0XOAivt2ZDCu4Gj7z0t8I4U9yOyr0DTUY5u9U216EL7rUDNpN3SwJ8OXlOLUZP%2FS4SyjpUuBcqpppJQJUsKU%2Fq0a6XYxEtErCvpMbOe7wH6e%2FUwRAWK65Ml9J8nZv9NzyBfPYzhz0Jphp1X%2FICV11R&X-Amz-Signature=56dfb85639d63a5ba12fe2e74a932c767a153f3b891f9beb88734fa584d806b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYWOORFR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDUrDmN%2FtiAdET%2BTrmyfiKBwVK4ziEpvD64p43Ysn5sJQIgIFLH708SP%2FcZxgjk6KP2KWtXLHfMP%2Fyo%2Bkl%2BZkTkFpYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDHaBz6uctDBm1cn7fSrcA0jJzORTdCfy4SOcKYf7wEysBnjizPOnxOdtLBnFMN9m5BH9SQMloq%2FTGLPf1y9eW764PzZlnOZ7QYAT0Nfct5i9Obf1qyhwoc1XrbYhK3kjvVBnFlM1zQgcXpKAHoWLKc3O%2FAoFddUJeVCUmamdYYMOn7Q9wveQq7Jhf6IowHc6MWExqXHtwvnfkq6ZbKcAgEAZaaTGaAzR%2BFNFx73Ce%2BFs3cxgQsdlHVt%2BaKSXEjWkHDUvZNFX1KcgZYHAWmKOg6WiH6L5A00S2WwOOYnXEpKlZWGxzNM1DaR62SZmw88F%2BosB4ep1dHu0%2FcTNQpVjUoLFwx9urAxG%2F1f0WsrK0gJns1omP1QB%2BnBNF%2BIozojSF%2FJ08wElLkillsBU8O1CzFPe%2BaeTnM37gxPlF%2BsWodCBRZM%2FuN4g36Yxk7n96xUIpBzAZkKJihfb36vfLgleijEs%2Fx0ZrGcbUp0DhrirX66Vxf8aIHN5zv4K5JDP2TyjAgFy%2B8VE6yGlVMzVGCPc5h%2BoGxEBmzUyyaThzgtSy0m4JvCyQS%2FIyx9sfD7nVbhItU5fRtFx8OeblzqxT7aqD1sxo%2BSpJtOEdVQTUtO5ov6rZXHunKa58u1RwNBp57AkHrbnHkH72Lk53uF2MIOeiL0GOqUBXpku5KJj91OkmgOLHkNkBmagZeGiyl3Mf4x%2B7RQ0akBUU9eXgtVB8YXGoMb6LteuMQ6l2X0XOAivt2ZDCu4Gj7z0t8I4U9yOyr0DTUY5u9U216EL7rUDNpN3SwJ8OXlOLUZP%2FS4SyjpUuBcqpppJQJUsKU%2Fq0a6XYxEtErCvpMbOe7wH6e%2FUwRAWK65Ml9J8nZv9NzyBfPYzhz0Jphp1X%2FICV11R&X-Amz-Signature=2b4f0367f9446f92c06e5b7e8892f04d42c0485f8f96d9c79de770f73ddfc101&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYWOORFR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDUrDmN%2FtiAdET%2BTrmyfiKBwVK4ziEpvD64p43Ysn5sJQIgIFLH708SP%2FcZxgjk6KP2KWtXLHfMP%2Fyo%2Bkl%2BZkTkFpYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDHaBz6uctDBm1cn7fSrcA0jJzORTdCfy4SOcKYf7wEysBnjizPOnxOdtLBnFMN9m5BH9SQMloq%2FTGLPf1y9eW764PzZlnOZ7QYAT0Nfct5i9Obf1qyhwoc1XrbYhK3kjvVBnFlM1zQgcXpKAHoWLKc3O%2FAoFddUJeVCUmamdYYMOn7Q9wveQq7Jhf6IowHc6MWExqXHtwvnfkq6ZbKcAgEAZaaTGaAzR%2BFNFx73Ce%2BFs3cxgQsdlHVt%2BaKSXEjWkHDUvZNFX1KcgZYHAWmKOg6WiH6L5A00S2WwOOYnXEpKlZWGxzNM1DaR62SZmw88F%2BosB4ep1dHu0%2FcTNQpVjUoLFwx9urAxG%2F1f0WsrK0gJns1omP1QB%2BnBNF%2BIozojSF%2FJ08wElLkillsBU8O1CzFPe%2BaeTnM37gxPlF%2BsWodCBRZM%2FuN4g36Yxk7n96xUIpBzAZkKJihfb36vfLgleijEs%2Fx0ZrGcbUp0DhrirX66Vxf8aIHN5zv4K5JDP2TyjAgFy%2B8VE6yGlVMzVGCPc5h%2BoGxEBmzUyyaThzgtSy0m4JvCyQS%2FIyx9sfD7nVbhItU5fRtFx8OeblzqxT7aqD1sxo%2BSpJtOEdVQTUtO5ov6rZXHunKa58u1RwNBp57AkHrbnHkH72Lk53uF2MIOeiL0GOqUBXpku5KJj91OkmgOLHkNkBmagZeGiyl3Mf4x%2B7RQ0akBUU9eXgtVB8YXGoMb6LteuMQ6l2X0XOAivt2ZDCu4Gj7z0t8I4U9yOyr0DTUY5u9U216EL7rUDNpN3SwJ8OXlOLUZP%2FS4SyjpUuBcqpppJQJUsKU%2Fq0a6XYxEtErCvpMbOe7wH6e%2FUwRAWK65Ml9J8nZv9NzyBfPYzhz0Jphp1X%2FICV11R&X-Amz-Signature=e1f66a629b7b4ae132f0d771770b5f400cd797b34d4543d3448741be97e9b3db&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=09d6f70e1ea7b9a7d0b7a6e1410390cddc4707e3d4b07a43538b6b3d053d68a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=35184c5a212f6186be0b7a9439fec87084ac23f9d0e36975deec2247f0836d00&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=91284c4b03aa3a95d5903fb413932b14b0723ed12a41706a75b8a45066cae9bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=d98ce91c0338fe6c5766cfd49f090b22f606f92b28add3ede450f583c67d8fcd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=7dd61dae3b8873063410e390b92613bd1fece9a84798aae6b9ece57891e94540&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIKV7V7R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIGOSjYz9QuL5%2FWfGkhj3kT3pby%2Fb2XyxwUVCFAuKp3OwAiEAhieUV1HnjnCqr5MtS0BsP1kFtaCj1bXqh9gXMIlJixgq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDOVW%2BhAhrk9oVgP1VSrcA99dnicDqTXLLYa7I%2BiWb5WRaiTTF2Ib51fQylw3REmLVPx%2Fh%2F0HMt%2BSUkQx893B586FNqlmUbrXPl3J5NYpcT7hzLvxeWrzxAGiIvw8DoYGDUVswbyaFmfkzQ%2BM2p7ZOeKXbgWdtXuxt8OrnVBKz9BvHYTAplfFb0AVvphgxY6il7DQVrHKxvEjJwfzOcbcJd80SjBOD38b9zWqcB%2FaDOJnzs4PffwlpRwXrvvXqaajc0HJcm1YWzcarRGbGqckewER8FqMICa0n1E3WyNQCOwsiMlLmcdZlUPzRtN3fw%2BVAQTEEpB7ohTZWiUUPwA7N%2BHfyWeF8iicDTfT9OHj00G9GQ7eIvOoL3ZLhkq3IwlZGhF0JSFFN1p4SGIibtIePg8YQCZO5mzFl%2BtdUH8zcuemXflE1UfVglGuCo5DmGWM6EhYon%2FdwbtOSGQrcUAeYkF6gBFheLTYRseeYa1rIXt4nbcIWb7HIJnXEt1ZDAEoypawiJWM83sDpLdIu5LVeKxibUQP0NpoKsmAPe4eO9R6DweGmOIy3Z%2FeeL%2FvTY2bCGiHGLDFNIrcTx%2BoZ9cNL0Nvkya84nDxKHmZl21k%2BAfeDSUtn6dn5pKYy9TzJAyerWL1cHgQLRQJL%2Bw7MJaeiL0GOqUB5SJkeDngiJdoVrfQ%2FubMTubkawy4TWS2JfW%2BAbXXDWOCBbnSpccWiZxu1A0%2BlHUMhwbMgUNkf3EPgTFnk68sF4XMgMwmgtOrLEmvoJ5lOataivXezXvDbsd%2FOcsH9uidnQgN3ej3qhZNNCJM%2Byaydx8FCx9P9CnU8JwEN%2FRNLQ1C9ff%2BBP%2B0F30Cr6lIbXXkVMYfJkaQasdlY5v5w58qns0s%2F3Jj&X-Amz-Signature=3a832897875cc247eac26bf66df28b4e05a4b79b34dc3deee42cf0448fc2ebdd&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQKKCLOQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDbCnA8VlfRWrxDzL2u5q53lIqxykOcnGDZk30kXvMR5QIhAItV%2ByLVzK02PlMEhY9cgK6Q%2FBFPH15S9G7GwVoFaV8NKv8DCC4QABoMNjM3NDIzMTgzODA1Igy3CkgrkzX7xImptjoq3AMoJpwdEwxXwdylyx9h7sAgEOedMJ7FNqhwoEY6XW8I03c5YIC05IFIoEwO5yWCRBE39mcp0roNelRrNQ1JSFnIjDzna0lDbzUt%2BDlj7KUgOBCIAAeRIA30Nj5%2FoCeU4qmTQ5qxQPOlxMVmuE4ienrCcWNq61rx0VEqh%2B7u0J%2FWxrvRn6l6umnvIsfYapZlvHjxH4G2N4fzdAk2PNfvA97x6i55rLceRuSf5CpKQ74HEbYmHG%2FZgDfAfsGrTsGa7I1SL%2Bw9m%2FbuW7GZyoPDg19Mj90e7oh7YnIx%2BAse%2B006Uae91AWTKAr3I9W0AwUjL57zz6r5u2AlrjnNm9hxTAxDG8z3kcOY216PZpTslDKALWdjPcXnS%2FmNdhrcHkmUIjKDPXgMkaTXuTXO9C2dUQqdL1VooSqoWfLv4zYL3Qe8tHwnggwwnJMno2bI91M%2F1Zr6Hi2F40t2uXMdKWZd3M%2B3M%2FdXUT2zLxRwdi9t%2FgsLdO8JIlYWUhQV73AaDKCwYXyMP2m%2FOzpg939HOfekw7ImMDPQqPF1XKmxqdEQ3s2ockXZffbO3JeT27UJvHMBdxr2gdGQOUph4JiI0UdTCwbKAq9rqvEjqIUrnpM7DBZXmpkij2z0K0lRotEyxzChnoi9BjqkAdLCAFoOVELLcvtecHiF5S41Z3kbBJWFgZhE3uhHvYpSHdM8HODHABwrMcYgZCUILgvRpDseG0i4gvUS1fJGjdBDPcTiwrP%2Fnam40k%2FVGqjUULGOEFh1xTuq7K2LHoA6opvMSyksv3Lg2NasSdawj1RM1sTktsH88H9kTw6wOc7MGHYWl6KIpskoqM8rpo7B6fyAQfjrgE6brDP%2Bsk5mn7SUiDDr&X-Amz-Signature=ceac7670c54f91b97a7dea2d47221060ce40c1e3a66d05962447d8d7e29f8e09&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQKKCLOQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDbCnA8VlfRWrxDzL2u5q53lIqxykOcnGDZk30kXvMR5QIhAItV%2ByLVzK02PlMEhY9cgK6Q%2FBFPH15S9G7GwVoFaV8NKv8DCC4QABoMNjM3NDIzMTgzODA1Igy3CkgrkzX7xImptjoq3AMoJpwdEwxXwdylyx9h7sAgEOedMJ7FNqhwoEY6XW8I03c5YIC05IFIoEwO5yWCRBE39mcp0roNelRrNQ1JSFnIjDzna0lDbzUt%2BDlj7KUgOBCIAAeRIA30Nj5%2FoCeU4qmTQ5qxQPOlxMVmuE4ienrCcWNq61rx0VEqh%2B7u0J%2FWxrvRn6l6umnvIsfYapZlvHjxH4G2N4fzdAk2PNfvA97x6i55rLceRuSf5CpKQ74HEbYmHG%2FZgDfAfsGrTsGa7I1SL%2Bw9m%2FbuW7GZyoPDg19Mj90e7oh7YnIx%2BAse%2B006Uae91AWTKAr3I9W0AwUjL57zz6r5u2AlrjnNm9hxTAxDG8z3kcOY216PZpTslDKALWdjPcXnS%2FmNdhrcHkmUIjKDPXgMkaTXuTXO9C2dUQqdL1VooSqoWfLv4zYL3Qe8tHwnggwwnJMno2bI91M%2F1Zr6Hi2F40t2uXMdKWZd3M%2B3M%2FdXUT2zLxRwdi9t%2FgsLdO8JIlYWUhQV73AaDKCwYXyMP2m%2FOzpg939HOfekw7ImMDPQqPF1XKmxqdEQ3s2ockXZffbO3JeT27UJvHMBdxr2gdGQOUph4JiI0UdTCwbKAq9rqvEjqIUrnpM7DBZXmpkij2z0K0lRotEyxzChnoi9BjqkAdLCAFoOVELLcvtecHiF5S41Z3kbBJWFgZhE3uhHvYpSHdM8HODHABwrMcYgZCUILgvRpDseG0i4gvUS1fJGjdBDPcTiwrP%2Fnam40k%2FVGqjUULGOEFh1xTuq7K2LHoA6opvMSyksv3Lg2NasSdawj1RM1sTktsH88H9kTw6wOc7MGHYWl6KIpskoqM8rpo7B6fyAQfjrgE6brDP%2Bsk5mn7SUiDDr&X-Amz-Signature=dd465bcd265db1f201e9dce57ec0a3bd552524801b30ea1c7e401a038f9f8514&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUCONU5G%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIC%2BwEy6EXB5COfFGBMjy48Ezl4smlfU0XBq%2FYoqm9bgGAiEAmX2QxX1jxlDL%2FSRyFiMeKFg%2FLu3G0nH5CTnRT98iQIAq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDP9lbcCzAIaYpkp4%2FCrcA6rQ1BexW8gQpVA4qQiF56I%2FG2Dkg5BcS6soAHYW6LV4ZNYDejW88G1H%2BhuVlaiL7lf9g5AYt%2FM046UUrZTRE641p8DhSDqrQZp2i5TEVnaw8i2ZZ0CejkRh5Iu2aBbbYJAgwRsqjXtePuVmFYr5XklMFE49ogDVgu06hukCGnZBiJxmCT%2FJ0e3r%2FBpOvnpx1nWGDYbrqGs9Bo7VRL%2BX%2BTnm4j19I40wiE%2Fznh7kFFJAtfE%2BMWxzP29YgquJ%2FCe5iI0CXfOG60GVmUU%2FEdM2bysn7l41DSEJGa0dRexiOdnLk30xWahRYWFlcGUgOy5isj8QBQuqTP9HTBoWYr3FWYPyn3TgeOogcxCVZgJoWB%2F4h39xlEDevA3pSVlxHcr8XPSjvycEiL1Q4FBLQLD9mkjTvEyIOHgydvA8Zkd05OBcM5S9GP0CxePp7ZVGvRH8AajvhR2uRTopomDSEoxlqqpy6icSr5tX88Mi45QRuyvhvLUgZi3yjBoevaLp28ngjCSszMEcG4DFoKMrdunCiYM6Wn7qentt%2F4%2B2AVq1OFM1uTf%2BAdm9uBrY7nSnXTEEh96XiMrDJvIlZ4MRqcwcyKnsWTwJ9YTE02roic3ZQN6apR9UZwZIbzUGyGbGMLKeiL0GOqUBndTebMDpUh7F2Cvd9s1H%2F1PWhLv9fDhnvFqAsnZSy8VJ5vv1biPFOhdaYl8bltWw17tO8SOUBP2LWCNVkNrS6CXdHbM6fI1XZbuJyfq9gyGKQ7HPPSd1AYVmQ8l2Aw7edxNJNQqjLTWi%2BZlZJQKx%2BAC09UVcEf5KlMRQQ2MZZBC9pEjhjw8GL8UT%2BlciMVVxRfgCboC4u0Ax5%2BAb9c6d5xioNkRi&X-Amz-Signature=fb879a33fe48d10e3d21cb2ab2dce67654a2e6ec3f1978f499234db88d55a12b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCK6WYA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIGw4RalwKotEXjeDNJR8dvAGs8POILNL69iwq4M2ff0eAiBsCYNUTjeVGVh9awSROeYREaZv9AVCUhNZjNaSWOG%2F0Cr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMJK7hhGq9rbsHNVbsKtwDAKKeLT%2BT0vC4R6uyDUUDjzVWwo0KN72gzQacJQIvG8FLpBzsMAZ0%2FkSaxsYQX0fkMvoozOtzpxTvF5A21YL9dn8bT2vsy4ru%2FgAO%2BNzOrRYZeiStSYTZjpg75SAlpreM2xJ3OKXdMBShy23Mir5jSjKpxz87vgHH4BD3VbcSx0Lb%2FzSY5XaUkz4Sk%2Fr5G8tYpoM8hGHd%2FK7x7U6tBoIH88OjtLcwen6eQ3NZ7f%2BWj1RicVGwJxhzgB%2FPjGuDdQ8wwI46MzwTihcOKqSXlYOm8UU%2FU7%2BSC8Oc3DCL8X4fi%2BCd6DZLmDE8v5VucTfZxghNsWbFtimJ789joE1DmOTlROc1usQjQPJ6RtBrGhUz7wUUoTk3o7owr80OV6jvVEDS%2BX86i5XN7KcDdAfnrXY7Vp81xKs2PElj%2BUc%2FcXI8V6RfWXpxdxrcHzCVSMx0v88MdAbRHu4pNqlhZCaW9QZsp264WuD0zhxhL%2FUhIS36IqsWLMhSGMNVRsmB8wYR3oNhwU5msk3N1UeiS%2BPfOW1ASiAuq0bXKrCkSQyuzJrBxbuVTfYRfhHjJLNiPsTu0%2FjTTuxi1z0adZFHl0QsnHsMkCvTyynvI%2By4QDyAwHhuJr%2F7XU4kOmKHOJVaFH4wsZ6IvQY6pgGnWgUm28YcAryDSMQyQiPPIBV4f3mu%2BazUzKPotye7B3Iuje5suAB9yQ5atu5DEOG8UvcdCKN2YzzeWwvl2fL0yonbNaoxavJcQwmPQl%2FSxsBB41ejAyBzbwoaf%2FoyULQK%2FpSwgYyMubXOBPEv236heK4PRekI%2FNHkJp%2FGMhS4Wt%2Ft%2BWx36TDpfybmz17KwLXXuEaqYiKoR73hz%2BalVa6wXOgpPdN0&X-Amz-Signature=f171f90145abe6bf9a5f3bbf5234d2a81b0ec3c0807c7918990602d9fabe5287&X-Amz-SignedHeaders=host&x-id=GetObject)
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