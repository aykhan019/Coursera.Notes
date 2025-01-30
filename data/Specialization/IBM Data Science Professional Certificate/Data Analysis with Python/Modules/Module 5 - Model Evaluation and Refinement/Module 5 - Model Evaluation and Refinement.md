

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=ba1695db3d00d098db2990b406bd1f50327c14c688ee6a2342e2511e09a74c9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=c7b1b4a28ef857c1f83e401b3acc89f877c78d78e0014b46f3a0104bf3443721&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=6305d85fbc7ff8efcc4054ec77941687869198010ab1cb63a0d92a03e653ba97&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=f88256e8a5087f90d44e4ee2a1db43ba2694883fe2d3a6bcbefa4c2d291bc837&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=080a14f73bbe4a1c5ecb05f8564f4e8aa1de6323b8b8aa87b19f9de7c7a15d85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=dcbfaf754518e840635b74c7dec786a8fa21e5a46f25053b3076a8c61502b62f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=415b15f864f9d01d5883078a347cbd8be30c7b8968c15b5fdae723445c01cc96&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=48033da2edd9ffbf183c4eb44f813f5be33632ca97472fc86255cb2ff746ea1f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=04a610cb4ca23f9aead4894addd337a460b3aee0f9a2be69fc8036cb234f90df&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFTECX5E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0oHyxAY%2FFqxaXYOa18yRXjswkNCyfN38Yq%2BQUHWIsEgIgd138anp4ew7TZxgCNo4TxoK38qEqPtcVY8eLmYdjgB8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMFtUQNwAVXY0zPGJyrcAyO0xof6Uch%2FPjT2b9elRRqjfXqZDW7JmwNI8kw7%2FYOIrhLrYJeqSwXZGJ1qI3vTeBo3YrjWM7iUbc2hYXe8Q3YCK%2BOiCA3dzfl6lnjY53XwhE1er%2Bh6vNgrqf5lYw6jZ2QkV5Tnj4B9hIfU0DwQE6USY33Leev5ZR8vev1IcWHjaaJzgneyCV77pcRJ47kB%2FV3wpzRiN2f5DG9iJJKBjVdfdOZTRU2%2BZZp9eNlmOkBHidptiQx7i%2FomLDjfPwe9Vuvv%2BkfEJVFvCB0MclJ8lQxa6GuM1elt3tIPRgYzVhsUwXVxFzrkAzdlS28BBlAIR7g643cKExxx4ihydqS8mCh3B74mFciClM%2F0HtSlkyme608L5fK8F%2Ba2nhkgnTlH3CLjVx7RE2e98yR268AwB%2FHMLu2W0jDg7CmMiM9izW8KmNdJmQxu4%2BXxzG0DVhMH1TI9eBXZp6c%2F3yvoUNfu4w52vOVSMey1A8PhOWAodJt8Jbw8DPDl%2BFU2eDaSDlOAsgvmLPqsJ0hVtF%2B2FKYFAjLY3mO85m22lWxnIHqrNdMNIE91OY%2FUpuCy253wh6r0C9%2BXbnkjcfhFc7DmC0PaAxOl2jnqmATtJMhp9c6VDIg7YQUvjiTryqqmIwW5MMiN77wGOqUBLqZqo6z2ZzcPKY%2BhiFkI0xzEDYesczKfvFcArN1f6lZOBkmaZAg9FEBQLeuKsYW0LZ9ZsRoZfUOXVGFO6CSOcG%2BUCkrO4HUCi11iTaYGVN%2BHDA%2FC5fzcUK5NQ7%2Fg%2B20rpAaJHdw27Um7%2B6EqDweGpQ12MouNkVCx1uth9%2BKTnWXGnAaUWkviYpviWQQmPkLrGomDPSlJjz6Z8j5dVHQNLWmn2fqt&X-Amz-Signature=89720e4ac42a8e13bee154a3133ba51aac54eb91bb9d875086aef21560c63fe2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFTECX5E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0oHyxAY%2FFqxaXYOa18yRXjswkNCyfN38Yq%2BQUHWIsEgIgd138anp4ew7TZxgCNo4TxoK38qEqPtcVY8eLmYdjgB8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMFtUQNwAVXY0zPGJyrcAyO0xof6Uch%2FPjT2b9elRRqjfXqZDW7JmwNI8kw7%2FYOIrhLrYJeqSwXZGJ1qI3vTeBo3YrjWM7iUbc2hYXe8Q3YCK%2BOiCA3dzfl6lnjY53XwhE1er%2Bh6vNgrqf5lYw6jZ2QkV5Tnj4B9hIfU0DwQE6USY33Leev5ZR8vev1IcWHjaaJzgneyCV77pcRJ47kB%2FV3wpzRiN2f5DG9iJJKBjVdfdOZTRU2%2BZZp9eNlmOkBHidptiQx7i%2FomLDjfPwe9Vuvv%2BkfEJVFvCB0MclJ8lQxa6GuM1elt3tIPRgYzVhsUwXVxFzrkAzdlS28BBlAIR7g643cKExxx4ihydqS8mCh3B74mFciClM%2F0HtSlkyme608L5fK8F%2Ba2nhkgnTlH3CLjVx7RE2e98yR268AwB%2FHMLu2W0jDg7CmMiM9izW8KmNdJmQxu4%2BXxzG0DVhMH1TI9eBXZp6c%2F3yvoUNfu4w52vOVSMey1A8PhOWAodJt8Jbw8DPDl%2BFU2eDaSDlOAsgvmLPqsJ0hVtF%2B2FKYFAjLY3mO85m22lWxnIHqrNdMNIE91OY%2FUpuCy253wh6r0C9%2BXbnkjcfhFc7DmC0PaAxOl2jnqmATtJMhp9c6VDIg7YQUvjiTryqqmIwW5MMiN77wGOqUBLqZqo6z2ZzcPKY%2BhiFkI0xzEDYesczKfvFcArN1f6lZOBkmaZAg9FEBQLeuKsYW0LZ9ZsRoZfUOXVGFO6CSOcG%2BUCkrO4HUCi11iTaYGVN%2BHDA%2FC5fzcUK5NQ7%2Fg%2B20rpAaJHdw27Um7%2B6EqDweGpQ12MouNkVCx1uth9%2BKTnWXGnAaUWkviYpviWQQmPkLrGomDPSlJjz6Z8j5dVHQNLWmn2fqt&X-Amz-Signature=bde2df4088d13f6ce230107eb980f60b1d61afc4d7ad42d6d7538d840c8e6b73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFTECX5E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0oHyxAY%2FFqxaXYOa18yRXjswkNCyfN38Yq%2BQUHWIsEgIgd138anp4ew7TZxgCNo4TxoK38qEqPtcVY8eLmYdjgB8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMFtUQNwAVXY0zPGJyrcAyO0xof6Uch%2FPjT2b9elRRqjfXqZDW7JmwNI8kw7%2FYOIrhLrYJeqSwXZGJ1qI3vTeBo3YrjWM7iUbc2hYXe8Q3YCK%2BOiCA3dzfl6lnjY53XwhE1er%2Bh6vNgrqf5lYw6jZ2QkV5Tnj4B9hIfU0DwQE6USY33Leev5ZR8vev1IcWHjaaJzgneyCV77pcRJ47kB%2FV3wpzRiN2f5DG9iJJKBjVdfdOZTRU2%2BZZp9eNlmOkBHidptiQx7i%2FomLDjfPwe9Vuvv%2BkfEJVFvCB0MclJ8lQxa6GuM1elt3tIPRgYzVhsUwXVxFzrkAzdlS28BBlAIR7g643cKExxx4ihydqS8mCh3B74mFciClM%2F0HtSlkyme608L5fK8F%2Ba2nhkgnTlH3CLjVx7RE2e98yR268AwB%2FHMLu2W0jDg7CmMiM9izW8KmNdJmQxu4%2BXxzG0DVhMH1TI9eBXZp6c%2F3yvoUNfu4w52vOVSMey1A8PhOWAodJt8Jbw8DPDl%2BFU2eDaSDlOAsgvmLPqsJ0hVtF%2B2FKYFAjLY3mO85m22lWxnIHqrNdMNIE91OY%2FUpuCy253wh6r0C9%2BXbnkjcfhFc7DmC0PaAxOl2jnqmATtJMhp9c6VDIg7YQUvjiTryqqmIwW5MMiN77wGOqUBLqZqo6z2ZzcPKY%2BhiFkI0xzEDYesczKfvFcArN1f6lZOBkmaZAg9FEBQLeuKsYW0LZ9ZsRoZfUOXVGFO6CSOcG%2BUCkrO4HUCi11iTaYGVN%2BHDA%2FC5fzcUK5NQ7%2Fg%2B20rpAaJHdw27Um7%2B6EqDweGpQ12MouNkVCx1uth9%2BKTnWXGnAaUWkviYpviWQQmPkLrGomDPSlJjz6Z8j5dVHQNLWmn2fqt&X-Amz-Signature=97f43bde660f151594de851bd6f909c15b1547141d7d872f76ee01e7bafcee5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=7a76df83921863437249deaa732f072b4125560723c02f7d09953584c3c1813d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=0f4739b68f442608510f81162d57fe3960b8572b13bb8a9f273afcdca11175ae&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=f6da62cbda993590b0a3b7ddbe4c9d5b32bab817beea2e3dd5b4235a6159db9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=68e35bb946198872793be870e47c8108150eb5dad52b4ed12868353683a4be5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=f4b5ea1872a13f51ea4d225d3d32f4a8b835fe2c22c65d339f7aec8c75b0741c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQH7ZMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsVZDyaW8sDhn0tJN7l7RYgJvhbd4VzKW7CmpcwHlkqQIgV0YpfhE%2BxZb0GYtIDVemDIcZwLHA5d1yrMK7UQbeQzoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7VpabzENEHGzTcVyrcA8uaaK7hv6HZWsk0uR5f%2Ffz0DvEJdoMUKPM6BcJweNXLxiQwWTNxVKtY1qJVGcKt4FZxNlezlSb2HR9tcDuRzRVq3OIPLCstnFJhD6i4SLbt0Z%2B6GKavjZJOt9G0%2BRcggWtJRVFXkwM4LpdqHyF7I68Jxi7yCWRSFb56BH1qNLNqvQr3TLVqoDbvdo1hr2XJyp1tjnuCfGHm2Nby6MmgH09ic3WpcnnP7Q1w72nOhOZPCZgiViTwKMpwEzfqYskxuTBiubRHhkiAIizzww2rkOEZV%2BnAFLvasgx6gl3lr1DF27gyqOyzspcpaVlOQJsjNkZRKbCT82yjzXayLo1HwLBG8PqyEPGESKguQj6Jw8OmkbXdHwoDnfN1qPnlVEhXl8lgy9bsq83AEz%2BGcZNUFo%2FrDGHoMxgTOlR1L5c4HwKFJrY9i%2BxaU75DelaxI4jXzcqjD9Z47jNOd1OKpxUBcRkWbCrSPZYqTX12vTnPbnHVk4RkkRSSWOtL2ykpYO9IlbCI3UgscG%2BEJp4aPWEhgIzp1Dwl1yMhTsHKQaiayJ25FAj6mLHaLED3rSq2vbDCpEEiqzCtXsRDMcn4RnZuCYXX2COT4J9Z1VCMmguSna59VbqH2f5wbcqopukCMIOO77wGOqUBnnyynnvTNPBtjUSCwduKvYm0l%2BKOWfxrdYzgrlgi%2BJ9MBHK0GrwOGJDDMYGqrrSig3ekYCdUrKfwnSNtRcDx7td60w5w7nMwChewha6IVYBmoaApGIFHqu8JqzUv%2BoeTyk5FGTDdAqaOGEv6ZMWxfzHLuNzzj5gfl%2Bzp7DVLI%2BLZB%2BsypVi9F9g43ZIcqBW5jMMKV6GHe6sPh8WwYWzvPsudxgDi&X-Amz-Signature=5193d22492cc1fcb2f2309412bd9f27dc4c58a8abbcb2149ae8e01dda615c43b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPOAZRD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxq4pBHQAF9jliwuiqt4brFl7hBn00fyjJi%2BSW%2B47JXAiBv5xOYcPokJCWsZ3sYPGgsdjNPQs2kuiSg9krnVgbOxCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME%2F%2BfauerkLCX9jOxKtwDhtmo1tSlSWpr8L3X2V6LOOHOxwByxH4FOQitrjcv9sFt%2FP9iyxqpdqlhgsSnp9HyMnRUtnSPBWqggsSaqtFeuL4GQybmN9FfuQiPw2YkrBS3xN2x4KnBj8CHsqsCLT5BCRPbQg5M5HN15BRdxz38KVpF6rwE0MOQJvORDQEisLE%2FV2undwsgTH7%2Fl5kBWrgNeNwTnxa4vRGtfMXixfwH6YtVCR%2FNzDANpQLnEtwSBHH1wfxYzUF%2BZUcGsEu6PyxdlwbtsYrHkHbU6WAN%2BSRMdU%2F%2FhWCNzhDNDf0nDTIzgI63rEAI9chw7oHoQOZ%2BqPzreoK3UWfbDMPOBe64kRIatLD9X91Cqn0qpzMNozL13Zg5mE3XSCBgzV83m22QY0PSPASydA50km8HAZ8kAnawVGibp6P6DdP167HejRmOMM12siOsdLyvvA%2Ba9rlVpRuJeg%2Fd%2FZB1KK1JiTgMjVgeHqS%2B65me8Y0x2XvhGVaqdOoyd1Y29Zddr9MQb8hrZTayTN%2FrGhkDKNPD9nnq2%2BOxqfjfo9fgyakioaJFk1dtDYiFIzwB%2FtuBRuw5rD5JJIN%2Be2A2XxN1QiAnq5xkC5Jit6vRoxHqb4dI05N9niXU5bFMdNP9zmk5UpkLGiYws47vvAY6pgHB5huL8Wtd%2BGN1Tf18AlXi9%2Fq%2FlbLuhS7QXj4mAs0GtST5qXj8eiXjiBuMu1Cq7fVu%2BOLsf98el0LuwgrYfUXVU0iM9UybLze7BdW0m3RLtsbn7z1uCW5H%2BIGHy7twjVjaOLBKcjy7LwrrTiQ0EnmfwEwBmcy%2Bk8E%2BdbWLqAohVBlfxgXgcieIHAAwbDScrOM4%2FnXy1tti%2FaGGyRFOEHHQsrzlCP9f&X-Amz-Signature=ca342f02d23de251f74000f1dfc30e786f55f69c4e06b678ddfd20e004374e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPOAZRD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxq4pBHQAF9jliwuiqt4brFl7hBn00fyjJi%2BSW%2B47JXAiBv5xOYcPokJCWsZ3sYPGgsdjNPQs2kuiSg9krnVgbOxCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME%2F%2BfauerkLCX9jOxKtwDhtmo1tSlSWpr8L3X2V6LOOHOxwByxH4FOQitrjcv9sFt%2FP9iyxqpdqlhgsSnp9HyMnRUtnSPBWqggsSaqtFeuL4GQybmN9FfuQiPw2YkrBS3xN2x4KnBj8CHsqsCLT5BCRPbQg5M5HN15BRdxz38KVpF6rwE0MOQJvORDQEisLE%2FV2undwsgTH7%2Fl5kBWrgNeNwTnxa4vRGtfMXixfwH6YtVCR%2FNzDANpQLnEtwSBHH1wfxYzUF%2BZUcGsEu6PyxdlwbtsYrHkHbU6WAN%2BSRMdU%2F%2FhWCNzhDNDf0nDTIzgI63rEAI9chw7oHoQOZ%2BqPzreoK3UWfbDMPOBe64kRIatLD9X91Cqn0qpzMNozL13Zg5mE3XSCBgzV83m22QY0PSPASydA50km8HAZ8kAnawVGibp6P6DdP167HejRmOMM12siOsdLyvvA%2Ba9rlVpRuJeg%2Fd%2FZB1KK1JiTgMjVgeHqS%2B65me8Y0x2XvhGVaqdOoyd1Y29Zddr9MQb8hrZTayTN%2FrGhkDKNPD9nnq2%2BOxqfjfo9fgyakioaJFk1dtDYiFIzwB%2FtuBRuw5rD5JJIN%2Be2A2XxN1QiAnq5xkC5Jit6vRoxHqb4dI05N9niXU5bFMdNP9zmk5UpkLGiYws47vvAY6pgHB5huL8Wtd%2BGN1Tf18AlXi9%2Fq%2FlbLuhS7QXj4mAs0GtST5qXj8eiXjiBuMu1Cq7fVu%2BOLsf98el0LuwgrYfUXVU0iM9UybLze7BdW0m3RLtsbn7z1uCW5H%2BIGHy7twjVjaOLBKcjy7LwrrTiQ0EnmfwEwBmcy%2Bk8E%2BdbWLqAohVBlfxgXgcieIHAAwbDScrOM4%2FnXy1tti%2FaGGyRFOEHHQsrzlCP9f&X-Amz-Signature=3f00cdc3d31aa8a493a84dbaa257425d1e252b1811414131430d5e1271d4e81e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G32I6SR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeCFIsUw577lOYa2PTY4%2Bj6M8Cn3WYqtPr0vC3I5dTTAiEAo%2FnR9EsjY8shA%2BnjQ1ks%2F6QkV4D13251SlAKDILC818qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI12cZjkZhGdhzfiwircA0vwadBc%2BwLUG4Ft8fj%2BYWr%2FfIhkUc%2FBSqq7y72wOnwSYVCvWpZ5%2BBHpspxwCiUwK9ZO26rHZ6dDAAZw6GJbbIIztrD%2B1sdokqxd2IRP0HzC%2FZNC4kp5qkLB25GDpo5513be70yNPtXusFJ5jYHcerh7jSTVL015mYJ10vZ%2BFwWXMtyvrxTmAEgn5ObnAcKuCTTr%2F8LXT%2Fw6%2FHL8CPlZY0Bp%2BcOUMSMxwCB1E1NOjxrb%2BplhqkyBTVjQvjawqw72inmN%2BocnGA%2BnCLnFD3JpG55HRF8aXPo6CbixQWxBJYm9UMf09qn3fEPuY%2FPlW9%2BigatJb4aD4vPsSqnTc21Exd3%2BLTdOhYtqghKGN27b7dVRJkvcSm4kKUsOTjpUXn3i1KkVtxl6tFmxHuZoAdAX3E3jkMZsT6Rkx1H3qn%2Bb%2F1dlHneonksRc1JURMjEoKoyTkZEJsm5K4%2BZuUMZsTeFWvMLAQrYleWTgRxpWoycrm3BRMBI6rFWOo78aa7nVO8xLtox9dpx5x%2BowJOwaJMsFJu41fFZpMKOgMV5%2F2bLXmNaD%2FoIW4n0vQjZN2o66bznHBKHLWR5tv6%2FYZUAxlxwwGp67jsVsLjkjPUE%2FwZ3SVB%2B6tGfQVPDiYwaO%2FJpMImO77wGOqUBf2fdPk2Sbr3IBURdeFEq1PSzzYW%2FzPRX4rAvO%2F8Ri4bvW8H8Z9zIo4qgI2w2sYudBmJNhL43Qakp%2BEQy3%2BnP43J1rlC3rkwBlaEeQPQ4%2FqtCv%2BwgsQ2%2FhAfiSFPSWBx0tLiYOW2i0llcv0x0yGhfvq3vZ3xo08%2BOGaS1We0%2Fh9gjlC%2BAHSBehd0r2ToJXs1ZmtW2Agu8Pwhu7xQ9YpciB8qHiH%2Fc&X-Amz-Signature=584e1d47c443b0366f7f228c3c2317528f74d18e31a279d7dffa411ee2bfc5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSOCWK4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAMw%2B0wkrG%2B7%2BELdxwMbJbipuDlVa5a29UPhKGlaOGWAiEAuRoLnoZurOh3uUf%2F26fmgEXSCzx3iIF1C2NVlafCZC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaUPt7hoh%2F6Pnp6AyrcA0yhGHs7zO30JQrM68JlBPwg2xekCIBu%2BWAwLowwReg9zi9Wbi5bndI2ewZhrOkVQtklAC%2B24%2F8z7Z7APyPSishHIpCOgqD0t4nRfqwsAurrasZLEauzZqnSVzG4D%2Fi9s5PXLudyIJtWTxvCNyjXY2yb7HE5MyryedTpVQ3vDddftd76ZA39mrjmJie0kqxM%2FutcfcHy8KgMHvTlb5HJaeURpmA3128I%2BsiBkfZRVumdlKc9hh2BIvRzF7sNn98qrzMctqXZFO4Opf0KCS88sUraZXu4xFpRzk393VgMMwAY2yRJ2rA4LfDNmF56%2BGfXgNMi8WFpZH6sJXq%2BjBh3bd1nbjsA639bw28Hod5RXrf2OrgJM%2B0asNKtuj5WVg1n%2BRxhTIiq9Xwuwy93lS4CmAfHtiaKfhmlQNogrlEIXHqRHjJwvosxzF0DT7o6pPncBU1Iz0JvyJJ8jgPsl3tL5rfg8dj5WWDuqF419kff4JMzhWdR7XRtAb8sNKalpbwb1TkR0w0zGmJa%2FRGbkwc4M6n2C%2Fq28JZYbEc808Z0XJaZHRw2R1hZNVtO1P9g9UZytjDfH92HJu%2BLDghJbvFBtrmvKJLejws0wEdzfZ9aoVYinQvGOluj%2BuM03IF8MMmN77wGOqUBEj9o4qn57P2i6rPTY3e0jD5rEhwcKBdL8ANNXbvKcwhwda7nu4HpyT4bTe%2Fcu68UCV455f8N8EQ4Ol9OPmY5sEhe2%2FU9RmUXNzmMAECYTBS%2BTNZKzJicaGHmZ0FpjOzC8Rxm8gMH50Wn%2BgNRdHP396E5Oykfl%2BgtiedIXTX5TnF4jD6xbbIULNQcyNqfAS%2Bw8FkCbaY8lOn2KIRwpNsawBUWzd%2FV&X-Amz-Signature=6abf079d7f5ad5aa0d3c9583f56ed25cd7b66882baa1da821859c86fb33e84ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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