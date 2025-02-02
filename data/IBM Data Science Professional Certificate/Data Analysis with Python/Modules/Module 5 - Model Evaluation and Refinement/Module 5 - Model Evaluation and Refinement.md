

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=2de269140deefc6f416b7fc6f537d0c2d03a8548f4678b63921ec5b4f5d9ead4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=a36dfa6c5649e53740f78327b9dcecb81fdafc5b17108572f7dafa3f708fb0a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=1c2f8d68ff4a42d89305a01530ed098a00499e0c249801f2639574355faccdc0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=5b531b002005d4e466767e359563562f8d023ba678a4232065b91f8817c7c776&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=464d3cf4a40dee1a136a737407491fc404008c3701f6f6cd10676e38f4dfc0de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=8f2ff9041d185f83c11339043e848dc0f6123796d62cfa5750bb02ee65afdf1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=57667ff3bf94b53884bb1b48951f22a930bf3a8b1ef69854f7b29baf35554ec7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=dc18297e2be864ae12397f1f5d077a18a89eedf03fb18e16a2d4147892d75630&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=371e50c4376a3c58c71a67a7e42c9ece5c73bd3cead30ace7af784b55788f5cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQIHTMB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvIQARjuww1tH%2FiCC1hzkwPADppUpTvCnqru8tAK7lDQIgDxTsO30jYf4oRtbhiTMMCIGgFWrdxwfJ9ASpiTPtay4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhx0JdAXjyxzKUe0yrcA%2BGVoA3SUBGD7IV%2Bz3AKtpdWTQa2lp7nB5dMRynLgXahDa5buebYhh0TVQ4Yd5J4Wvdp7X7z5vg7EnoiaVGy7jFZaDJWI%2FzYqmpUwZPCTx2l0uI2OufjK%2BDlvYBfY8pOY0VddXGoxqv8QvFPb8d%2FkBHC%2FqK7OsDGjvHfHwQL1UgUHhmqpe3k6qinjCO8esowOBw%2BiupK3P%2FhokIvMC%2BhQWGRqN9CLEZGKCbieItGBiJR5A5n2AZLKR%2BWTUmYd3cghOhvbHwtDp5E4ypCaGPtkavkjcuKkYYgNUh06%2BBXmjvh2GpXHLB9PTa2kYYIgbbVcSa%2Fxl5Ibz%2B1M2%2BxCPuB3vk5heI%2FVuha9sXBobhvnNv%2Bk6TcawLhQn7OcVHT0Cc8GXHSmjbilpVu5i9Az7pNXULPH8IRiLKe%2B4pM%2F8F7m4s3iVhz0%2BvbmAZtvWV5jmiC0Z2XgKDo9DRaDERVhhl%2BUX4oLyc3xiUbZzI7q30Nti8JCNxqXFJahSQqBQXluzoyTPuKQvgX2aEM3DsEW3mJGMb94FhhmHy147ecWqJBX7naQb2BdDG4Ke8FpHpwVPiEFc6xW1p9DK6SxqEwKz9kYMNCLNC%2Fgj4hjman9OJvONq6yqmZom9HJYtSlyr6MPa8%2FbwGOqUBYXk8oH5lGhxthTAyZ%2FeV6T9J4OcHsZiVA4TCA91S2kBz9fqko%2FV1oqZSgsUmBxtBGmrS6nSztkmystxYXT6D0KV3z25bIPdxQ4q3M12w4BMUPYZ1qjGAnk3lmXi5vQOwt2gVztfzHAU1sUh7Qvu4cQHncEV2jmgFyALisjOwrDiNXw6ZWwgYkklbRJXKZBBYjEiqPl8xXiM62mt5auQRlCKwNvyt&X-Amz-Signature=099cd85c9362aa151e34e42437a491d4a67c377da62f413ba632a2cdde9d5ec1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQIHTMB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvIQARjuww1tH%2FiCC1hzkwPADppUpTvCnqru8tAK7lDQIgDxTsO30jYf4oRtbhiTMMCIGgFWrdxwfJ9ASpiTPtay4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhx0JdAXjyxzKUe0yrcA%2BGVoA3SUBGD7IV%2Bz3AKtpdWTQa2lp7nB5dMRynLgXahDa5buebYhh0TVQ4Yd5J4Wvdp7X7z5vg7EnoiaVGy7jFZaDJWI%2FzYqmpUwZPCTx2l0uI2OufjK%2BDlvYBfY8pOY0VddXGoxqv8QvFPb8d%2FkBHC%2FqK7OsDGjvHfHwQL1UgUHhmqpe3k6qinjCO8esowOBw%2BiupK3P%2FhokIvMC%2BhQWGRqN9CLEZGKCbieItGBiJR5A5n2AZLKR%2BWTUmYd3cghOhvbHwtDp5E4ypCaGPtkavkjcuKkYYgNUh06%2BBXmjvh2GpXHLB9PTa2kYYIgbbVcSa%2Fxl5Ibz%2B1M2%2BxCPuB3vk5heI%2FVuha9sXBobhvnNv%2Bk6TcawLhQn7OcVHT0Cc8GXHSmjbilpVu5i9Az7pNXULPH8IRiLKe%2B4pM%2F8F7m4s3iVhz0%2BvbmAZtvWV5jmiC0Z2XgKDo9DRaDERVhhl%2BUX4oLyc3xiUbZzI7q30Nti8JCNxqXFJahSQqBQXluzoyTPuKQvgX2aEM3DsEW3mJGMb94FhhmHy147ecWqJBX7naQb2BdDG4Ke8FpHpwVPiEFc6xW1p9DK6SxqEwKz9kYMNCLNC%2Fgj4hjman9OJvONq6yqmZom9HJYtSlyr6MPa8%2FbwGOqUBYXk8oH5lGhxthTAyZ%2FeV6T9J4OcHsZiVA4TCA91S2kBz9fqko%2FV1oqZSgsUmBxtBGmrS6nSztkmystxYXT6D0KV3z25bIPdxQ4q3M12w4BMUPYZ1qjGAnk3lmXi5vQOwt2gVztfzHAU1sUh7Qvu4cQHncEV2jmgFyALisjOwrDiNXw6ZWwgYkklbRJXKZBBYjEiqPl8xXiM62mt5auQRlCKwNvyt&X-Amz-Signature=074b8fa5e868f89c2da4ce30f289e33f4bd585e7f5753b45ed0eb45b561fbaf0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQIHTMB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvIQARjuww1tH%2FiCC1hzkwPADppUpTvCnqru8tAK7lDQIgDxTsO30jYf4oRtbhiTMMCIGgFWrdxwfJ9ASpiTPtay4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhx0JdAXjyxzKUe0yrcA%2BGVoA3SUBGD7IV%2Bz3AKtpdWTQa2lp7nB5dMRynLgXahDa5buebYhh0TVQ4Yd5J4Wvdp7X7z5vg7EnoiaVGy7jFZaDJWI%2FzYqmpUwZPCTx2l0uI2OufjK%2BDlvYBfY8pOY0VddXGoxqv8QvFPb8d%2FkBHC%2FqK7OsDGjvHfHwQL1UgUHhmqpe3k6qinjCO8esowOBw%2BiupK3P%2FhokIvMC%2BhQWGRqN9CLEZGKCbieItGBiJR5A5n2AZLKR%2BWTUmYd3cghOhvbHwtDp5E4ypCaGPtkavkjcuKkYYgNUh06%2BBXmjvh2GpXHLB9PTa2kYYIgbbVcSa%2Fxl5Ibz%2B1M2%2BxCPuB3vk5heI%2FVuha9sXBobhvnNv%2Bk6TcawLhQn7OcVHT0Cc8GXHSmjbilpVu5i9Az7pNXULPH8IRiLKe%2B4pM%2F8F7m4s3iVhz0%2BvbmAZtvWV5jmiC0Z2XgKDo9DRaDERVhhl%2BUX4oLyc3xiUbZzI7q30Nti8JCNxqXFJahSQqBQXluzoyTPuKQvgX2aEM3DsEW3mJGMb94FhhmHy147ecWqJBX7naQb2BdDG4Ke8FpHpwVPiEFc6xW1p9DK6SxqEwKz9kYMNCLNC%2Fgj4hjman9OJvONq6yqmZom9HJYtSlyr6MPa8%2FbwGOqUBYXk8oH5lGhxthTAyZ%2FeV6T9J4OcHsZiVA4TCA91S2kBz9fqko%2FV1oqZSgsUmBxtBGmrS6nSztkmystxYXT6D0KV3z25bIPdxQ4q3M12w4BMUPYZ1qjGAnk3lmXi5vQOwt2gVztfzHAU1sUh7Qvu4cQHncEV2jmgFyALisjOwrDiNXw6ZWwgYkklbRJXKZBBYjEiqPl8xXiM62mt5auQRlCKwNvyt&X-Amz-Signature=22d663bdf30ac77bfda38f63b193e94a72a67ce368ef4f3aacff2509de996b15&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=95aa89c13c08bc88b5e474787676d97dfbc17a0bc0cc181adfa3ff11902be735&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=459d3af2cb3e200f936582109306deffd451fe53f43b1a6f972493fe1960b5df&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=cdd5324c34538b77d6cc46397ddb1f23809bf7747af7403149490ebe542b9147&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=64ba98b3ad0fe8bb4e47e15454818709a3851e3fecacb54e9dfd480ad0a93d58&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=ec8dab83d29794aa8fad157626410cbc896cdb8c23b60bfbbe0207a4c008f637&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OZZAXQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDPSuJ6FtHlgz90kQh%2FszKEZUuz240%2FaLbE1Na2CylbMAiAfd4Ymi3mTrU3UouTDa%2BIvjaP%2F3VSslGVMXWolI6uyViqIBAjw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMey5GOTKgYyZKXUCRKtwD8uzmqICI2NGlbn1gjfzIt0BuoJSwm9E1Zlo7aB9fDLX%2Bu%2F%2FzYIjldyLii8Ju9ZRqxjPLz0wEPIxpUMYfEQBBD0tadQfAKMqtfsjFqiHtjpS8I%2FNjCJhkZUJuhJ2vfx7UqQXfFpzwuVFKjeaVtWzdDsaQEr%2FmF4c6EwJYv0lbH08uaB%2FcaXdhsgcy2S3vVCTGqqcOjFAtED1wtD42sVhuWWwsFZu%2F3UGsN1%2Fm3nGnmtNrBGLpthcEacS4bavaylf1jwbtm9UAx%2BpcIBAuu%2FPORMHtlv5B81RN%2BLMOaMnesUuJPLjcd%2BHtR06KvS8DVoxH7W5lMvVwaRBlhCGwkKuFAdQC%2BlbNbuBbtXgx9wcd5yM5CE6L4LkgTQuntb3iZCTpfIJi4O0VZZ5NdxiDNViu7IbKAcA9bPX3atqwBpzqIGWEVoQE80S4eE27Opr0Notr7XW%2Filj3gC%2F1IG9GUj9CKOMq7HAnqx3To11B03gzFeiIWGXjs%2FvjD2gD8t7SfcSNdCCaVxV5feY9gyAgcNsd3dh%2Fy0pjMzWTOM5sWajPVlZQWDxcW46M5LbuIg61ZMzD7A78KRvbSZJIjpxIqYsSVez6%2F40B2o5w%2F1QB7oIHPKkvIqKymsXkqyhPVrAw75P%2BvAY6pgGlG3oWMXOpA1deIRv99BdxyhUAUm3bQc9ziBXhNdexHo%2FuERXXROYyYy6NsxoW%2FfySjxoCtWfNwbpFeMqWr30kwbaU9LhszCbIwwZ0bShnnoO8F2a%2BGkqrOVzfEeADJYEmcb%2FkbP7%2F9TeVnOzTGVKd7nOlvYl4veyvOB3nFgXSdHxxPHw%2BVhjr4FBN5joToN4YVvtyPwBTAvPeh0plJ3dBeH11ZB%2Fq&X-Amz-Signature=12a41d4f967ac8decb2283956b7d229bffff5b95613d6b15101503e50b87c84c&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQVDB5UI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCXpxZX4543rUpCr%2B4yvY%2FeALpN2xnZpZYtw2pyTj1cAiEAipai0KFOhgjZ7obapHIYEd%2FRcSIow9%2BBRbcuy1xdjLwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9nNPiEMnWvrY6o9yrcA66Lsi2I%2BQiUCLMrpnwFyaVaADim3wI64EMgrJJDmgeBlgM8T051KXhiI3NTSvmEZskWRq4Rf03JqzoeghoG6s%2FBiJGpnjZV8j8UFHJClfLk7gJSc0OFvj6X%2BIOMQUXeqXYVAjXxkNGQfNKjvcYwhqosTMn%2Bbri8zwRLPelC4ufd%2BXn7wKwXceX%2FGArrerFQF7pFx8J3pB4c8%2Fz3xBstZ%2Fuc2pH%2FCOKsjrQRJpMq8mY0kllLh9LmM7rfVDjTNh8dwahNmWzsgNVN%2F9Nr2%2FhktZrytji4LYA%2B5KfbQVW60goM5kJct9x5iejcL86r4a0ZaKPUY5CBgMp9VoMZVyrS96FNs1kmUZe5NbnE7cQbjTQJ%2Bs%2F6h%2FSiE9GTMRTZ5N7ikEZ49EaUpLN8E03CEDgEsMb7Io2XAVXbMJYOE9bl6i%2Fpr4Jnt1Sj1jxsI9r2k1RJUnnqBaMH6MTLUbX%2ByfS0XcPrIzkjVNhP%2BGJx8w3NybgW2sizbv01cy6sJ7RuQ%2FHqZUVq46tURh3zMg16t%2Be0pSthtE3WHSHo7E0EkaaCDqeq%2Flt0FtaFAoi%2BH54G%2FAc0Zw3IaZPq%2BCgVafxVD2Jh7WFEZ%2FbzOYvHLH2ZG19YMOq2OlZ8xXzksp0CfH94MK%2B8%2FbwGOqUBcOB3tanxv9US8HdjUOvHjWgrLXRe%2Bnbyq1PzLOHgjNVa9ea2%2BahkBiUlwtXLbW1e4xTtlRttMVwq6uNoTV567TYZxk0uKqEIjQKQNwSVGMDxhGP%2FMup9WyeMxDFgnIrgAQwyeqq0Mk0FMKcSl3ucAOSsSuexzGm5eiapaxa6bBkx9QOEkVIsP6JYjMiF49aDabWFCSXDtxpzXSe7EzoQmSFShkXQ&X-Amz-Signature=c99306161c0f0b776847ff4e2796e483fd8ef65f0315d67d590086f056a4f1e9&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQVDB5UI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCXpxZX4543rUpCr%2B4yvY%2FeALpN2xnZpZYtw2pyTj1cAiEAipai0KFOhgjZ7obapHIYEd%2FRcSIow9%2BBRbcuy1xdjLwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9nNPiEMnWvrY6o9yrcA66Lsi2I%2BQiUCLMrpnwFyaVaADim3wI64EMgrJJDmgeBlgM8T051KXhiI3NTSvmEZskWRq4Rf03JqzoeghoG6s%2FBiJGpnjZV8j8UFHJClfLk7gJSc0OFvj6X%2BIOMQUXeqXYVAjXxkNGQfNKjvcYwhqosTMn%2Bbri8zwRLPelC4ufd%2BXn7wKwXceX%2FGArrerFQF7pFx8J3pB4c8%2Fz3xBstZ%2Fuc2pH%2FCOKsjrQRJpMq8mY0kllLh9LmM7rfVDjTNh8dwahNmWzsgNVN%2F9Nr2%2FhktZrytji4LYA%2B5KfbQVW60goM5kJct9x5iejcL86r4a0ZaKPUY5CBgMp9VoMZVyrS96FNs1kmUZe5NbnE7cQbjTQJ%2Bs%2F6h%2FSiE9GTMRTZ5N7ikEZ49EaUpLN8E03CEDgEsMb7Io2XAVXbMJYOE9bl6i%2Fpr4Jnt1Sj1jxsI9r2k1RJUnnqBaMH6MTLUbX%2ByfS0XcPrIzkjVNhP%2BGJx8w3NybgW2sizbv01cy6sJ7RuQ%2FHqZUVq46tURh3zMg16t%2Be0pSthtE3WHSHo7E0EkaaCDqeq%2Flt0FtaFAoi%2BH54G%2FAc0Zw3IaZPq%2BCgVafxVD2Jh7WFEZ%2FbzOYvHLH2ZG19YMOq2OlZ8xXzksp0CfH94MK%2B8%2FbwGOqUBcOB3tanxv9US8HdjUOvHjWgrLXRe%2Bnbyq1PzLOHgjNVa9ea2%2BahkBiUlwtXLbW1e4xTtlRttMVwq6uNoTV567TYZxk0uKqEIjQKQNwSVGMDxhGP%2FMup9WyeMxDFgnIrgAQwyeqq0Mk0FMKcSl3ucAOSsSuexzGm5eiapaxa6bBkx9QOEkVIsP6JYjMiF49aDabWFCSXDtxpzXSe7EzoQmSFShkXQ&X-Amz-Signature=8178ec6aa17b2308ded245523c8019d069e8eb143db4614ef160a3057d4ccc77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVLZEU2W%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcG3vejEWnErna%2B4s8%2BBJII3rcfqWiDHjd8WN4ohnzzAiEA2kAd7DdIh3O9N5RuQnVfqoQubCXxLlDEr3CaFzcUJ4oqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5Zc4WdMMtnsBuW2CrcA9xnXiYbjV%2F9qnkkESG5awYzLXjgw9chViIiiV0hYOA%2B2Dc8yfd6njXdlHjUx6k7nqT2hV2m2YO904Jt1KbEBLatdelrbTZFg0WAzv8KsDIB17pQi2i6IkWXBEidBLznkT0swN%2FlcBDh7CZDNlFu3ugGtytDsRpl50C9NNTGDdc2xznHoRckrXHuSHdEXfMJv5%2FAVke6p1wJ0X89c2DOg39A8BMwcHXYAeNGCs%2F1mlR6%2Bm7YCDEzc%2FdsbLsbtbu%2BBJjJbDdgVymhmPttaR%2BUQkYJIIIN%2BgYxYP9F9A51ziZWARads6lsggorOfgEXqSqIG1Ss%2Fh8uWiOsQaDa72EX%2F8BjhUp59TWSvgt3Ob%2FXkdL7mMWaSp55ad7cqU2V9%2BnlgJwxHm8bBU2W5ljNIabzSJ6mh7h5EjfSG8EMszSVTAeW7x11iUl4OyzqIqc%2Fwi0cFU7R7T7VSLQSPZgDL0fDHNu5GznBN6B1376Y6Nawke8Tpvj%2Fq6a6m%2BFOI4THXKwmq3DlhQBUZ1jm%2BYsOx7VRQk9cH4ncNwkyCycikoY%2B7YSpD%2B5Pe9vDHSrbqPbQftL8pjZ%2Fa%2F5Nm2tLkrlcqfbETNvdzJhOlJyUn1vTX4rrRIEu8kF8MTAgBc15NgDMInC%2FbwGOqUBXGZCsRkjMA%2BYuTDUAAcXPXqfXnZloG4w4fxXMACcQuOpn3ia1qUqxVgeFTyx30TmFnXljgqu0zNd5bOMDidBoeYuNuOm%2FYgB4h9AbZ55DkZg0ffEzJbB9Ucdl9IduCZZbMgguVg3d%2BCUM777Ah4RSqLYuactEQHOMTydo6qTTROgMe252MZpyAKZB1adeqSQ3Y1ogDDJ4A42sC59xkXFjIduI%2Btb&X-Amz-Signature=806e776f8a4b21b21717d19fa52ad2dd4bd2d3613fbe8b8e8c46e88c2955d6aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=97f4532b27ebd5c60b3910c94291bac3dcf2c83b273108c233ff833ccf0fba8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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