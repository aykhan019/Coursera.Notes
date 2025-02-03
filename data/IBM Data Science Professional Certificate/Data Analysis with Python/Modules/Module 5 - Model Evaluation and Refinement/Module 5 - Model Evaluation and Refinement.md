

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=a6f0a7256edaecffad0d71a0cd9a83f5b57ae653ad3ae776e03c28153eb98934&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=f307c79d1112a0bf777db915c5b714d9b308e580e5f2a8e73b3cfa4b896f2dfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=7316eab7bc205311733db28910d80950e2f49828311c4c2f25b39117fcf3de7e&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=bcad6d9d2d6be8455a620af5810644573941d9f42c7f511e3c91c865e97cb020&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=53dc30bc5baa99531f192a3569c9a7a73097ba5785cee310e8cab61dd6adc88f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=6562925366deb163a24d4af0884579ed8d443babfdf8c260556be284c1c6235e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=d541a4d0e8725c2b759414ae1dbc7191aab8defc4c6f163f79defe00fca2178e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=2b3a28d13ccb2d8d4764a00cc860438fda7af8795c38a45d0e1eb988bef7c67a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=6ecb7fb9244970f91af0a83ce383d452423fbfdbb9392834c8232786f9f315af&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO6JVFSQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMnGeBHeisGA0ZJalOhnR5OfLBKxjpH2m8gWCWIF%2B0iwIhAKqf%2B%2FFKiCKY59%2BFvOIdUIRIgG3hC1s4CNsJy88CBF0xKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjnR689R9F6wgX9Aq3APhNIdJuU9ikJQ3Y2Kg3mAjG3%2FiHfPU9iT6N7by6MXRIFrGrAeZRRHfR8WLadaAQhk4FgQ2UjKvbzkxQaaJufJvQ%2F0gn7yeXQ1l3NU7830b9kdLzhPOs3jC9Kv%2BzMjtHSSs6n6dpK%2BRrpw6fHwRvpyUcn8BdoEUk4D%2FkEDVDO%2B1pW97KSeNzf8uRGqb2yE56zhdQ%2F6IDCp%2BZFzBRAxrJ%2FPW%2B53aoecSN9KF3oiRcYOw4gU%2F3WnlVpsGUYvoJxZlxR3stSZHemvHZKs4S5FnNhMtLmW11zmNY2JW3LOCndleFUCZ6ZYTETy4L6sLSOi7URwW3e33S4B12YJkEePq5ojgMAVPkY36GyHMa42RO5OcmGoD2uFdCvb9ZosKeOJtqUdk9PPVKHPqhYayK0bsfS%2BF0ZqXQ2RXLIlHm5joEgGODNUN6%2FPS5PSMHvJOiiTmWGWDMC65iFk%2FxeeNZdheHC%2Bb3jJ028bBWgpd3Ahjv8e6Q3ntO%2FYmbLOHE6bASPMcIc4Yrg3Vv6SkdzxxisJrjvg7qV2IeouspwtP8saon9bqKjFpYxQCgywXzpxV8hYcHomg8uCRNaWN8lUy3w2RVSauxqkwy2GAlxTrSNym47ARK6umNJjFo4M%2BsgEiyjCLv4C9BjqkAaBUn7S4aKUZR5%2F%2B4ggKu12O7bKCXyOWBTVEiDDVaeWLGE5hLbuimwzG9UwPqWi1E4UGpp1uLvSeZ%2B0Ez%2Bs9hehATyR0uWA6PFRK%2BYyiHuo9Ej3cl9YsnAIzbIlKMWgK2PIjIzeJMFvz0ccf1I5PN4pUfHMlciCzQQuXYRiupI5HtcLqRuAbINScdCt11SAZr7eQMIZq%2FymX%2BxThC87q%2FbLhnbVx&X-Amz-Signature=2cee4abae68a951883657cb208de3840d5101f59c54ec0921fa279ff04d5d4ab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO6JVFSQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMnGeBHeisGA0ZJalOhnR5OfLBKxjpH2m8gWCWIF%2B0iwIhAKqf%2B%2FFKiCKY59%2BFvOIdUIRIgG3hC1s4CNsJy88CBF0xKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjnR689R9F6wgX9Aq3APhNIdJuU9ikJQ3Y2Kg3mAjG3%2FiHfPU9iT6N7by6MXRIFrGrAeZRRHfR8WLadaAQhk4FgQ2UjKvbzkxQaaJufJvQ%2F0gn7yeXQ1l3NU7830b9kdLzhPOs3jC9Kv%2BzMjtHSSs6n6dpK%2BRrpw6fHwRvpyUcn8BdoEUk4D%2FkEDVDO%2B1pW97KSeNzf8uRGqb2yE56zhdQ%2F6IDCp%2BZFzBRAxrJ%2FPW%2B53aoecSN9KF3oiRcYOw4gU%2F3WnlVpsGUYvoJxZlxR3stSZHemvHZKs4S5FnNhMtLmW11zmNY2JW3LOCndleFUCZ6ZYTETy4L6sLSOi7URwW3e33S4B12YJkEePq5ojgMAVPkY36GyHMa42RO5OcmGoD2uFdCvb9ZosKeOJtqUdk9PPVKHPqhYayK0bsfS%2BF0ZqXQ2RXLIlHm5joEgGODNUN6%2FPS5PSMHvJOiiTmWGWDMC65iFk%2FxeeNZdheHC%2Bb3jJ028bBWgpd3Ahjv8e6Q3ntO%2FYmbLOHE6bASPMcIc4Yrg3Vv6SkdzxxisJrjvg7qV2IeouspwtP8saon9bqKjFpYxQCgywXzpxV8hYcHomg8uCRNaWN8lUy3w2RVSauxqkwy2GAlxTrSNym47ARK6umNJjFo4M%2BsgEiyjCLv4C9BjqkAaBUn7S4aKUZR5%2F%2B4ggKu12O7bKCXyOWBTVEiDDVaeWLGE5hLbuimwzG9UwPqWi1E4UGpp1uLvSeZ%2B0Ez%2Bs9hehATyR0uWA6PFRK%2BYyiHuo9Ej3cl9YsnAIzbIlKMWgK2PIjIzeJMFvz0ccf1I5PN4pUfHMlciCzQQuXYRiupI5HtcLqRuAbINScdCt11SAZr7eQMIZq%2FymX%2BxThC87q%2FbLhnbVx&X-Amz-Signature=25bba341950ce59220774e7c9105683b19b004cc6ac421c577de318896a79c44&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO6JVFSQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMnGeBHeisGA0ZJalOhnR5OfLBKxjpH2m8gWCWIF%2B0iwIhAKqf%2B%2FFKiCKY59%2BFvOIdUIRIgG3hC1s4CNsJy88CBF0xKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzjnR689R9F6wgX9Aq3APhNIdJuU9ikJQ3Y2Kg3mAjG3%2FiHfPU9iT6N7by6MXRIFrGrAeZRRHfR8WLadaAQhk4FgQ2UjKvbzkxQaaJufJvQ%2F0gn7yeXQ1l3NU7830b9kdLzhPOs3jC9Kv%2BzMjtHSSs6n6dpK%2BRrpw6fHwRvpyUcn8BdoEUk4D%2FkEDVDO%2B1pW97KSeNzf8uRGqb2yE56zhdQ%2F6IDCp%2BZFzBRAxrJ%2FPW%2B53aoecSN9KF3oiRcYOw4gU%2F3WnlVpsGUYvoJxZlxR3stSZHemvHZKs4S5FnNhMtLmW11zmNY2JW3LOCndleFUCZ6ZYTETy4L6sLSOi7URwW3e33S4B12YJkEePq5ojgMAVPkY36GyHMa42RO5OcmGoD2uFdCvb9ZosKeOJtqUdk9PPVKHPqhYayK0bsfS%2BF0ZqXQ2RXLIlHm5joEgGODNUN6%2FPS5PSMHvJOiiTmWGWDMC65iFk%2FxeeNZdheHC%2Bb3jJ028bBWgpd3Ahjv8e6Q3ntO%2FYmbLOHE6bASPMcIc4Yrg3Vv6SkdzxxisJrjvg7qV2IeouspwtP8saon9bqKjFpYxQCgywXzpxV8hYcHomg8uCRNaWN8lUy3w2RVSauxqkwy2GAlxTrSNym47ARK6umNJjFo4M%2BsgEiyjCLv4C9BjqkAaBUn7S4aKUZR5%2F%2B4ggKu12O7bKCXyOWBTVEiDDVaeWLGE5hLbuimwzG9UwPqWi1E4UGpp1uLvSeZ%2B0Ez%2Bs9hehATyR0uWA6PFRK%2BYyiHuo9Ej3cl9YsnAIzbIlKMWgK2PIjIzeJMFvz0ccf1I5PN4pUfHMlciCzQQuXYRiupI5HtcLqRuAbINScdCt11SAZr7eQMIZq%2FymX%2BxThC87q%2FbLhnbVx&X-Amz-Signature=8b76596d78354d615e7022921a9c2e6584143b6a011b3e9d0eca14151b0c6140&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=a352e6f5af72059c20d597c4adde631eea265fd7381ad6a40baf9b505f878d18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=92dc97878647f8856455917a40fc3c44c3f9bb6e4d38589dc3016e45766be7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=29a8050dfa22d77ad7c06f9512955fea7784d3dce8e4ae81db765428380511c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=7e69e5abfd18234b5fbfd948f6a44a5436c63f8ec75a5fdb7f824f9ae5c45419&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=3711e4a813b3f29d4adba5b26d65f9a820f4698086bb90da2d3ff113b1b9fcc1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCSFGPJW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3ThrIDLf%2BfsxGYUnHiSMt4W3jijE6wDr6w3r2IfELlAiBekJL2J7Fh1nxzFQwiSmsSv5gHyHJZFfwciCWcGtE%2BdCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXe9yE%2FhuvyfzI4bEKtwDq%2Fc2dat52euZiN62PXozQ%2FmP7dENLLOo1jrEFO7%2FRwcQUiVHsqxcKDEjaCDnsYIGotLi3nQ0VWfPHEP7dYhL9Ku%2BewL59XwYq%2Bt4Az9N9uWxOsR0wPZBOthfJLG3NXvPTaEAj2fr1HzQaJBxiNKoqpKTJZalHVq%2FlU2ewLmSKk998WQ5oroB3zaEYrb0OZmorX6%2BjsnUPniQqoJLSVUhl39fDLQE6Vm1tUibZZX9EaDokZbSbp063%2BP9h5JoV1pJNKKTWvBlhJaHwWFWBvnXmblAvgSVDumie2ZbTX7u6DK7xYjOirMl3jP9hYhzHDh2Wdh%2FOP84o6tfH9Wxj6Sm69KalVoeXLxNDgK3NGpusx7zsxySxT%2FytZ1XCye55V3stSUCFDWqlQx%2FW72o4V8arqrTJBbAsI98jwiBKKDxG9cnQjVf%2BZYkDnBD%2BWxTL%2FEiQr4O1tG1K%2F%2FtAEoOg2f%2BXipVbquYnkrA57Cz3yr5WyxVyDIgMqaOY%2B83x3rpG0H6L15g3zKwlQ5jQzlKz35JhrbFw5Z88Cn5BEl3n2PfgJHsDQ6czPCgUfDa0jNNWGrBIeYiaDIGSiJc4WMsie7DgkoV4mlxA%2BcNhmviGMpQOsNJdc20Xfw8hK%2B7eU4wjL%2BAvQY6pgG3oOI%2FokKrGgRVAf3DokRYDRQqYbDctSm%2F8OzVLNa3Vp0yA2eqFNsXnN6gqzCqodmRozVJ4bgWZc2ke%2FsZ3%2FMilTQJhHhuYUYowaqUfMukZVwAspNONwZWzZP8%2F9YecLuwIu89Upytib%2BffEFUWiw7cEWDjaCct4YR18s25HD1SRun20z2C7Ee%2BvI3h7%2FfPa%2FU1u%2FaVBkuM7bNo7TI6W5Cpq3vr5B9&X-Amz-Signature=3132f8e6d385aff7ac92c432c3b177e8a1f2deba8622133b2cea0bdc370026a0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EKFJC7O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Xpe0153oBg%2B%2BXr5%2BX%2BbX0kzoVeHGN8attGUxAIPZZQIhANNonni04gv5V1swBr1QK35P1Dcd1NvM53BxUYpYkKajKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydkbZqm7Y8so7PvaEq3AOWlJI7uOsyJDqFz81TG4OClmU2cDRkSzENazhFPZ%2FF9pNGkw40g0F4vtGMcDWY%2BGrayaRbp3bSHYWPD7xw6%2BSqaMHSGJ4swn1nyFczBGOYUMet0C9QpeqfQ0j75svwenHS0E5K%2FSqRGZwHeEn5TlvKWWQWzH5NKGKMp6tDu5Sju1NF%2FSVe7pT3PxSlALjwq%2FoQhYEOFr0dxv7RslApqjwiWmEFBl8RHxedXSpGumv3rziAn%2FWMfvVDqVHrwqFV4TdtwfZQjoGjkLp0sgOcqn9gea79KtUuvRr7UVdzw7W2%2B%2B%2FPyK9GqS5kBI58R2YP7aEk89tH7HmyMFn1odV1EEvEn%2B7%2BnbqWTHXVEvxzarJv91Glfyop1P5ZRdiIqoaPC5XU1qnxLx0xKxIpKDbC5Qf6cWzNy40pRD0eSETLb%2F1EAYmnTIJup%2F6%2B7QmJvtMwYGL66WDIWXnGN3056WWIpxQJb0G88F0x%2BqkVQKuy8Dmekn7PiYnMt107BPK2%2F11%2F6Ig7EeiH77uT%2Bh3%2BqtciQ%2FWJsAKcordW2CU00fpeErrXenyHmcx7mpzRmKfWDTZF0fedruE1yUF9RuBVNF1Vdstqu6ScQ8S%2BYFWcS%2BXvvEj1e2vQgwkJeSzdn1EA%2BjDAv4C9BjqkAbEEIiCQA9fvaAHe1UDS%2Bj0sQlWcGeBMHmdV8FJeuYwUGuZS2vj3xE4gOzUg5i8OX7MoLIpywUHCGH4l0GIvsk0g%2For7NG3D%2FIBCS7JKM6LmOqv779N7WOvlVHfiuS2ucSzVp7pivDIVRzXeK74zeRYHp50fbEpbkjRinvQMzEktlBPHOnFOv0XedYlS9CZm%2B6IBJcXgq%2BgRR9zGhZgYn4%2BCK1Y2&X-Amz-Signature=4fb842875bb393ed119710ab7af91fb9b88dcf3fe7e8f81c930db3de237fa00b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EKFJC7O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Xpe0153oBg%2B%2BXr5%2BX%2BbX0kzoVeHGN8attGUxAIPZZQIhANNonni04gv5V1swBr1QK35P1Dcd1NvM53BxUYpYkKajKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydkbZqm7Y8so7PvaEq3AOWlJI7uOsyJDqFz81TG4OClmU2cDRkSzENazhFPZ%2FF9pNGkw40g0F4vtGMcDWY%2BGrayaRbp3bSHYWPD7xw6%2BSqaMHSGJ4swn1nyFczBGOYUMet0C9QpeqfQ0j75svwenHS0E5K%2FSqRGZwHeEn5TlvKWWQWzH5NKGKMp6tDu5Sju1NF%2FSVe7pT3PxSlALjwq%2FoQhYEOFr0dxv7RslApqjwiWmEFBl8RHxedXSpGumv3rziAn%2FWMfvVDqVHrwqFV4TdtwfZQjoGjkLp0sgOcqn9gea79KtUuvRr7UVdzw7W2%2B%2B%2FPyK9GqS5kBI58R2YP7aEk89tH7HmyMFn1odV1EEvEn%2B7%2BnbqWTHXVEvxzarJv91Glfyop1P5ZRdiIqoaPC5XU1qnxLx0xKxIpKDbC5Qf6cWzNy40pRD0eSETLb%2F1EAYmnTIJup%2F6%2B7QmJvtMwYGL66WDIWXnGN3056WWIpxQJb0G88F0x%2BqkVQKuy8Dmekn7PiYnMt107BPK2%2F11%2F6Ig7EeiH77uT%2Bh3%2BqtciQ%2FWJsAKcordW2CU00fpeErrXenyHmcx7mpzRmKfWDTZF0fedruE1yUF9RuBVNF1Vdstqu6ScQ8S%2BYFWcS%2BXvvEj1e2vQgwkJeSzdn1EA%2BjDAv4C9BjqkAbEEIiCQA9fvaAHe1UDS%2Bj0sQlWcGeBMHmdV8FJeuYwUGuZS2vj3xE4gOzUg5i8OX7MoLIpywUHCGH4l0GIvsk0g%2For7NG3D%2FIBCS7JKM6LmOqv779N7WOvlVHfiuS2ucSzVp7pivDIVRzXeK74zeRYHp50fbEpbkjRinvQMzEktlBPHOnFOv0XedYlS9CZm%2B6IBJcXgq%2BgRR9zGhZgYn4%2BCK1Y2&X-Amz-Signature=3e6748ce2be286e2a619f6bb7663a0518d074b83cf773508f0b9557c6c6cf93f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666F4ID6VP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXFl8EvCMrjuT13Zn7h3L7U77x61dWIW1jo350I3qMpAiAiQ87lJFZYNX%2BGM2dbLoIAI7z8YDXuQzCR4f61ZYfOnSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzbKn3iMmPI9ltdtQKtwDG6qn57UMs8TTc7jqcvxvQfr%2BKonv82cfM%2F9gCBu1p0bbbxUixXmSntXjUcp%2Ff4fpqBJBVnICdcuy9fT5WjpHzoTm8Z3sMAjhahzJkrdlu88bjDrBj9HOZuw%2FRSWLl2ridgY1cDQk4CCOaeLreXQIkvHAuxicG96D5Bp892xsqHgSqlrHl0cih57nWBVVQWyJhLFd5a7L4VjeLsDbWetPYcTbG%2B2ib4miGoTwgwLf%2FYvYFi0H19eUsCHvlkmpHoRfW5Lljmoe%2B85T62%2FUNvnhG9XXJ%2BqbXMJi7rm%2Fs9S7Di%2FJ6xLjbmhUug9kDxMVGtdlHG8Aap1GZk%2F7plGHwatLu9YflXYoaQlCbMu4M45R3t1o63Li50o5UgUmsgy%2BmBbjQWJ0D%2Ft5NHxlKMkMDC2IhBsbN8ZwZ1J%2BJ0Jyf6v8AFab03fSoX9rMPSoQWnaiGQqqCk2IZdLrx3jL0%2FCwDT7J7YH%2FJHcUiuJpYepzjQAszF5eOpTb1JBtXHTqLugoBlG89CTuFZ2TN0t5C1ctRKduyrZ5iDmccKtW3AufSTgonp3%2FYiMgx3Lpr%2FGCIQiW7aEObNOG%2BTVP8vVpi7a1IMf0KY275qwFqzeRJT63xtQLIolOlfRwwKl%2FhL9p0swvcCAvQY6pgFvv5aIGAS2zCPrYESy%2BhzeD%2BAiZfGG8U%2BUg9c6b4SyUnGgSWm4yYYW1PqiA19Thl1PR%2FM24PBEAAWcAWsJHLUsbKglcLvqhn81JKdw%2BHunebzcY%2Fz5o8prHqNqaTD03m0x%2Fn1oBSIQFhB1NYgtRYFkqfXzHfiF%2BPSzNoxVMygRsrFUQasE4%2FCmk%2BXC5guwQKrFjQvAjPxA9Il09um1A7wR6fpsuiXa&X-Amz-Signature=4da1b108d09fa9c9fbb2785ca4579df4aa962fd644fccfcea86269632af41049&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRGXWPP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk1Yl9FzYRvU0uk508Mmss5BQar0xprz%2BTO%2FzNyQMO4wIgMGIP%2BqFwhPLGJXiSo7OaIpy5qNqq5plzRCjIG%2Fdkeo0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2B%2Fjdc%2FT2WttZld2CrcA6kRuK%2BUKe59amLuSFkn1zFiSeukeyOgUOZZp5TWVI15%2BZVnLRXa3YgKEtlsFukEhgxiE1ECaed3CHoOtgIF3Bi32B5sueDk51GOD2R8NoMQR69ACYxCYGnxVCJL1%2BaYRpxBjTT5g6q0Z0nlxjNVF%2FahB0SjWO31A15OHAGK3fFvcajXZL6C4l1RJrcZXrrjxqsi2qXz2cA8GCtmMVYQ%2FItRbpuUxvWtHJ7YiwrJ3o1gOYk%2BIg445SbSM%2FOQQChFvct6%2Buhb8AmO%2BnlK%2F9EfeOyjIm3xXzUr4JbeI%2F4HRcw2pSA3j88Yo9IWrO%2FOqZG6Cp8J%2FmtUyMbg%2Bo0mbC3xS68DoeYmWXUBn4%2FJ9rQLKcqeMMB0azc%2FQ61rJ%2FCrBrND%2FEBcukjMBgdBUZFMYwQj1WJFemlKEbd0sOLcMUrapKTz1zektzRXS3BgDuAaVGXhpA2MciNacIOIyQ0IVmJoixNKSzhph1D7l5I%2F5AoJkgd9snZ0YZcSF4M9PsTOOfB01AeXGZ8YkehMqBeDphqmO0I3a6UdD%2F0zUa0sG6JRlILwmYgeB%2FH%2F%2F0GQi8ftl5h%2BC0zzSmzjMKSwLlgMru294ECDltb1YI6DdEyERvaVu%2F1EY3kvA16vP24wUlaBMPG%2FgL0GOqUB%2FSZy7HDBaY2kqWmuClZ%2FOURkdki2Is%2F84l%2F%2BIMcxR8PrJ%2BrTFFn%2FQ6GxqQDgpx8qNl6%2FEk3C3P3GS7qsTVA3BP1IzwluR3e6rU1U3TYJ3DPBF8W8tYN%2FT1Mmyi39rdtfPnAbch%2BFjfizIqS0gupuqCJJX79%2Bu5wqe845gmFMV4noOFneJRclGA3nt76C3Wyb1KRdsAdvgxIFCpAGssWSH8DxgP56&X-Amz-Signature=a7798c2cd3b5bda046fe5fe538185238058086c00217225f33d323f0dc95e6ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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