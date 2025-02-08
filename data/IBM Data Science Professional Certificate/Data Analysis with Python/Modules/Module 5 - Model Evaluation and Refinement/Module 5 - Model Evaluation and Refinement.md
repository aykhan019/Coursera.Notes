

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=9631a33afe4de1d8c79feb5cff6d7565175ff8371ecb0b12fb0c48df8f4f1a92&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=3ed3da7d449129f12ef407d4b2b1fdea88e479ae2a0213ce10be4b8049f90b12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=92800db3652e27e4f3be8603db92f49e0fac41b1d28424ab5863fe577b649f17&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=c928b029d5c1748492df7ebe32d3401c6f30666921d4e5b55ca741a8f37c3017&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=b58d8a53587655c808bb4115f4ef93edf275604eae3037aafc4df343e02f97be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=b1cc239e3e29a717d88bf0b8da88c8c7c55c49772d5f456f09828d47da83e5bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=a94729641d2ac0127d74ceeca190b89ff46744cd078e29d3877e9214b181b4c3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=08c1d1e76d81a0b106e45460bccf7773f21c066b1df8f878d8d49e577b052af2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=1d359ecf3b37373a7bd943b8a9e36597551e9767ea4080cade4408e88bd099da&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDIPMG4M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDFABmWVzYDrRk6CoZoCzyUrCCcKR099GSvaDbDDQ18aQIgbp%2Bdc7H2Rmoj79Wh83H%2BM1GxyhwPh6xdDJftobG%2BjrYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrPceGRKM2yCxnebCrcAzo4jE0HQuksBI2v1Vx2%2Fno%2BY9e5NNPOD4LMr5par9AzGNF2ePATYncLceeVvzC3VJhzUHhnA9%2FLc2Zu6iYKG2u89uVOGzq0s%2FEjqC%2Bx6gRV8SW%2FRr8yp7YQrt49fLuZXWiX6g4MGmGmYO1TQV9xTFkZ1RoZ6rCaBet77HJQcjPqSHKf8ZsI5yNzTBc57fxDmHISH3Ny8lJeiyYDg42IxEiOVtwYxdlFBtq5rOF5Ch1wvJQSQ5KEIRozwNBFvRfBbOLXuIPtqNkuMK8jrFn59DoP%2BcSwstlG%2FecgeX2Ov2nXsVO9bxICpz2lT6g8BaX9HsuZiSzMegHimJ%2BROXLq9HGuPh8SgNRuUUb2mf7gpqatRy1%2BNWX4hYrzbesyGu96J%2Fcp82yuf2ep0xv3b39M7V%2BNDTOqxWW1p2VMm%2FRTBMfPfLuPQRXWYZFzR2%2ByCPI54nwvO7YtgN2iUCjgpaxKDCFTHzTZgj%2Ffidaj755kokThkV6rF4b1rzA%2Bc2bbVZeo3%2BDFE72YnT31TPIEuBsyUeqfhsyDSD28LtQPCBIgeRaqJRjZIFdqbp9ybPSGVfv2NY5D6ImFUdVyZUsiB%2B0I3JhynyKjBAvCTGemhMg5tDW0wcHp0DYQ7iie62SlMMeym70GOqUB7vbZW3Cvf5PiAs5WGtTZbslc8%2BV30bewRi5XGdf%2FpFHKHvK0ufU81EwCwjf%2BCIKYogh3PWqNJnXO%2B0KtzhfStdm4nebdR08pIeVnQpV6dDe18sO4OOz6y9LcFJ%2BsrueZ%2Bk9a%2Fd5tXB3DiGB8nCYbixW4OeeFtkQSEyz1jCsvI9sF4Q9%2BmwRnhi5BEOMcC40lv0jjcyoj6tOl3BcqAOoyZChXOKzc&X-Amz-Signature=cd44e05249ad4c83b51802cce64cf7d6f20f06c674800141804cc942532cfbf2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDIPMG4M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDFABmWVzYDrRk6CoZoCzyUrCCcKR099GSvaDbDDQ18aQIgbp%2Bdc7H2Rmoj79Wh83H%2BM1GxyhwPh6xdDJftobG%2BjrYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrPceGRKM2yCxnebCrcAzo4jE0HQuksBI2v1Vx2%2Fno%2BY9e5NNPOD4LMr5par9AzGNF2ePATYncLceeVvzC3VJhzUHhnA9%2FLc2Zu6iYKG2u89uVOGzq0s%2FEjqC%2Bx6gRV8SW%2FRr8yp7YQrt49fLuZXWiX6g4MGmGmYO1TQV9xTFkZ1RoZ6rCaBet77HJQcjPqSHKf8ZsI5yNzTBc57fxDmHISH3Ny8lJeiyYDg42IxEiOVtwYxdlFBtq5rOF5Ch1wvJQSQ5KEIRozwNBFvRfBbOLXuIPtqNkuMK8jrFn59DoP%2BcSwstlG%2FecgeX2Ov2nXsVO9bxICpz2lT6g8BaX9HsuZiSzMegHimJ%2BROXLq9HGuPh8SgNRuUUb2mf7gpqatRy1%2BNWX4hYrzbesyGu96J%2Fcp82yuf2ep0xv3b39M7V%2BNDTOqxWW1p2VMm%2FRTBMfPfLuPQRXWYZFzR2%2ByCPI54nwvO7YtgN2iUCjgpaxKDCFTHzTZgj%2Ffidaj755kokThkV6rF4b1rzA%2Bc2bbVZeo3%2BDFE72YnT31TPIEuBsyUeqfhsyDSD28LtQPCBIgeRaqJRjZIFdqbp9ybPSGVfv2NY5D6ImFUdVyZUsiB%2B0I3JhynyKjBAvCTGemhMg5tDW0wcHp0DYQ7iie62SlMMeym70GOqUB7vbZW3Cvf5PiAs5WGtTZbslc8%2BV30bewRi5XGdf%2FpFHKHvK0ufU81EwCwjf%2BCIKYogh3PWqNJnXO%2B0KtzhfStdm4nebdR08pIeVnQpV6dDe18sO4OOz6y9LcFJ%2BsrueZ%2Bk9a%2Fd5tXB3DiGB8nCYbixW4OeeFtkQSEyz1jCsvI9sF4Q9%2BmwRnhi5BEOMcC40lv0jjcyoj6tOl3BcqAOoyZChXOKzc&X-Amz-Signature=dbebdda3433341eea937adb29bbb79c5cef98530b6e947a40ea8d8030a62e573&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDIPMG4M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDFABmWVzYDrRk6CoZoCzyUrCCcKR099GSvaDbDDQ18aQIgbp%2Bdc7H2Rmoj79Wh83H%2BM1GxyhwPh6xdDJftobG%2BjrYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrPceGRKM2yCxnebCrcAzo4jE0HQuksBI2v1Vx2%2Fno%2BY9e5NNPOD4LMr5par9AzGNF2ePATYncLceeVvzC3VJhzUHhnA9%2FLc2Zu6iYKG2u89uVOGzq0s%2FEjqC%2Bx6gRV8SW%2FRr8yp7YQrt49fLuZXWiX6g4MGmGmYO1TQV9xTFkZ1RoZ6rCaBet77HJQcjPqSHKf8ZsI5yNzTBc57fxDmHISH3Ny8lJeiyYDg42IxEiOVtwYxdlFBtq5rOF5Ch1wvJQSQ5KEIRozwNBFvRfBbOLXuIPtqNkuMK8jrFn59DoP%2BcSwstlG%2FecgeX2Ov2nXsVO9bxICpz2lT6g8BaX9HsuZiSzMegHimJ%2BROXLq9HGuPh8SgNRuUUb2mf7gpqatRy1%2BNWX4hYrzbesyGu96J%2Fcp82yuf2ep0xv3b39M7V%2BNDTOqxWW1p2VMm%2FRTBMfPfLuPQRXWYZFzR2%2ByCPI54nwvO7YtgN2iUCjgpaxKDCFTHzTZgj%2Ffidaj755kokThkV6rF4b1rzA%2Bc2bbVZeo3%2BDFE72YnT31TPIEuBsyUeqfhsyDSD28LtQPCBIgeRaqJRjZIFdqbp9ybPSGVfv2NY5D6ImFUdVyZUsiB%2B0I3JhynyKjBAvCTGemhMg5tDW0wcHp0DYQ7iie62SlMMeym70GOqUB7vbZW3Cvf5PiAs5WGtTZbslc8%2BV30bewRi5XGdf%2FpFHKHvK0ufU81EwCwjf%2BCIKYogh3PWqNJnXO%2B0KtzhfStdm4nebdR08pIeVnQpV6dDe18sO4OOz6y9LcFJ%2BsrueZ%2Bk9a%2Fd5tXB3DiGB8nCYbixW4OeeFtkQSEyz1jCsvI9sF4Q9%2BmwRnhi5BEOMcC40lv0jjcyoj6tOl3BcqAOoyZChXOKzc&X-Amz-Signature=e4571aa016689690e25c15334a6bcaeca0c11df9183ec7dd2d355ecfdc2ea22e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=db389a1fbb77e6db466fe406f680b0505931ff7f8b1950da121e9ed194ea026d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=397611c195f9fba066812aaf0f159ca3c30803403eb39f7a57c62eb82c270b38&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=01a416df6ef364e91116e4889b9ac47d37ba74d554a1a96f717fa8ee9d7bbfd9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=6973f9ae0d94765f7c52253e4132e4d3ca166ee08ef9be9234f81c528f37c9c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=4aa21029012ed9568ac8a33c8e2d8f634308e6c72be511d78afa6018f9d9aabd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXWFLMBO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCH%2BOdrevyeWpynmwsRaEjU9mKAFrvGDxTANcHwlgjNPwIhANBzp81CFYe7izT5FNyGomS%2BxJYmVhNSCA8B8PRIvkDSKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZt701Pi81ByibgsUq3AMoBWbs462eQbtOeyTBBgNVUACCHu26J8Sf%2FO3CaKPueWzJ2wVPYDVvqCE%2F5ZFy2T7C%2BPD1rXGGXekKyzDIRy1v%2B%2BXVfH4AguvZou1OKnvrOCNr9V97F6%2Bq63swYfl0tvEdKQL9nT0nmO82EVSuHN8dUHdlQlqExWhLypInf0pVIUZDb29YfBtqlfvz5fDJaQKtZRh1FFuAJ8NemMBy773AGYVLHYZC19orsRNPINQq86u3Vgf%2FHU%2FlJuf7t9EDZluIK1f8CFW%2F7NUNlPk9D0uiYJJP7cxCINi0%2FfcrZbh49mZzHg80rQAO%2FhMDzCHHSWo1RqOsyZV5NZLe6G1991nKmApjokQtEg2HUZcV%2FmnCn1KNKltj%2FuUOiR7eG6b%2B%2FSK6WJTY586ecchqXapLWOyMeeq7mCYFoLCocAzuTxvRmTD5b%2FLRHO6yraWyNytjWanKx4Lh5DT8wDiuDXDMNMEXd8PBk%2FtGq2ILuqStHTcgVxWfVvxX0ckXGF6lBxBB6Ypc3TFHKNS9cF9YnnyvPwMxAiFxb5YeZziHwOtWs0%2BkjsiiQqmzYSSdaomPn8MjSUI1%2F2mPtPPmZ8QRlwM0daM%2F9vO2Mc%2FwWxAldJvzV7kc5cHaU%2BCLrRBn4FIFNjCxspu9BjqkAU7H8pGIgv2z8Yfr7pn8uNKAQlsuVFOjwHFC1CdIbW2BvfPUJYQ2mIKY4H%2FP8IMQBITJxPxZH5U%2F0IInuEE1%2F5yAek27DX4arRPt4q7XOItWB9hkLpsDbQO%2FhI0nGDmWvJPJPq16dIwS2K%2BMw9duyzdaVLP1SWDoU%2FHuYw%2F3nHzy0UM91O92%2Fxspop7OYYJlm2cN5PLhsLfyyliDYw%2FbmJDJFjjC&X-Amz-Signature=f26df7683615574e83a3807e33fd7ad95d1172dd28264b9b67183bdaabf562dc&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCADKE6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIHeUF1OFNpSKdxOMgz9Dawnea%2BujZvzUAXnVYRevOICKAiAhTG7ZuzvDs6NbWFYLhv%2FJDrnkJLKtjBUpNNbmTshMFSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD4d4MZQC35JfepBYKtwDZo2rxCYV9dAl2w6v8msH9GFniFjidCyoZMnAEHJhPqOdb06pXMsiFmTEsEV1CnmKacw0TOvWBcQAacq3Z1eJHy1OVMeRA%2Fq3f4DxrutP1RxaG40hPtNEvW%2Fz1QdV0plaV09ncPl9xH3PRvYZ7vwRBLr%2FXYnI0H2hR2Z4m3ITSOW99V1FUlAXuZj5Gh9jGGpDusM0oZ8Ue44Tb84fW4i8tWTiYTnpiOf3rR1peYqwT9JwiaXALcOfhxRJf%2BywafpKKNtIKZMfueFekkfp8amKilepf0KHPjbfoodBr13roU1hcP9eOxpzle1PTE73uQlAMXFvVxIkX5fY%2FMOoH%2BRBnhaBIWasX0lR%2FuX7DQfzUibKO%2FHrV30qFytLWGPtCx1aVLFGd1izX5iOs48y0z9aT4DfLDTnMQ5wa9iNM%2FZyLZMMVarVJtNsyM8nwYS5ILih2oU4yzbFN5VV6dPRB9QEAqeSXfOktfRahr3vAVktUe3FQU7UEqc0zYY6XxJLRM5yQD9Tl8BF7m%2FnL5tpkEylC6lcpk0YWME8bJQdgQIfe7iNXdKMjdEYC5%2FXgedPk2YHvr6VTB3NL8dD%2Bad7ybvBT3HqAslDRjiZ8mj34PCBzoTRwY4qYuagkRGDor0wnbKbvQY6pgH1QNvCl%2B4Bsf78ncFEmxiPs6TwbAmUlSP1acWc5ndS%2BWBUQ%2FLtfVW7fOs2JpPOQb70kxbDnM4yD%2FOoyqnY%2FtSJkgoVNrTb%2FIK6yGK%2Fa%2BM8eLiDSrpzSQd8SKvHpWtoz%2BbNhiCPjZALB9ngZJzeNwUWJxxJbWe5flKf0J4f1j4TzQ5iCATIbJDOL0dLkwZ6lRwlMrOlNN2CkdrfUItGtUqRlvIRldDt&X-Amz-Signature=2fd5883666a14a02493eefcd44532d1fbf30f44c3a39b85ac00cd97e260661c8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCADKE6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIHeUF1OFNpSKdxOMgz9Dawnea%2BujZvzUAXnVYRevOICKAiAhTG7ZuzvDs6NbWFYLhv%2FJDrnkJLKtjBUpNNbmTshMFSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD4d4MZQC35JfepBYKtwDZo2rxCYV9dAl2w6v8msH9GFniFjidCyoZMnAEHJhPqOdb06pXMsiFmTEsEV1CnmKacw0TOvWBcQAacq3Z1eJHy1OVMeRA%2Fq3f4DxrutP1RxaG40hPtNEvW%2Fz1QdV0plaV09ncPl9xH3PRvYZ7vwRBLr%2FXYnI0H2hR2Z4m3ITSOW99V1FUlAXuZj5Gh9jGGpDusM0oZ8Ue44Tb84fW4i8tWTiYTnpiOf3rR1peYqwT9JwiaXALcOfhxRJf%2BywafpKKNtIKZMfueFekkfp8amKilepf0KHPjbfoodBr13roU1hcP9eOxpzle1PTE73uQlAMXFvVxIkX5fY%2FMOoH%2BRBnhaBIWasX0lR%2FuX7DQfzUibKO%2FHrV30qFytLWGPtCx1aVLFGd1izX5iOs48y0z9aT4DfLDTnMQ5wa9iNM%2FZyLZMMVarVJtNsyM8nwYS5ILih2oU4yzbFN5VV6dPRB9QEAqeSXfOktfRahr3vAVktUe3FQU7UEqc0zYY6XxJLRM5yQD9Tl8BF7m%2FnL5tpkEylC6lcpk0YWME8bJQdgQIfe7iNXdKMjdEYC5%2FXgedPk2YHvr6VTB3NL8dD%2Bad7ybvBT3HqAslDRjiZ8mj34PCBzoTRwY4qYuagkRGDor0wnbKbvQY6pgH1QNvCl%2B4Bsf78ncFEmxiPs6TwbAmUlSP1acWc5ndS%2BWBUQ%2FLtfVW7fOs2JpPOQb70kxbDnM4yD%2FOoyqnY%2FtSJkgoVNrTb%2FIK6yGK%2Fa%2BM8eLiDSrpzSQd8SKvHpWtoz%2BbNhiCPjZALB9ngZJzeNwUWJxxJbWe5flKf0J4f1j4TzQ5iCATIbJDOL0dLkwZ6lRwlMrOlNN2CkdrfUItGtUqRlvIRldDt&X-Amz-Signature=9deefefab26bff6cc3cdf22ab9a236098cc4b25268629b2a1f5df5ef2040ddeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=7e4ba8c3c3567cfcd80baee60ea45c89355e6f8f5ca0e9d20503b288be5a7d54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W73HOUS2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2%2F51xT31liMR1YuGs7RK1%2B%2FSel07JjP1Hz8oRXaw72gIhAPGnT63ctVK7%2Fii7YEqxGvgA9ANaOWA%2BBTAGeIVNb5HHKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzw0Yee2QqcxXhR7Toq3ANYOBfMydfvpzIFvanw%2BZ8zv9%2BmFVHp9GP%2BE4mwkLpNQdwbaQ0%2F5pozvQrnv1j4r3MiLwmwptnl8y7X54UarvsAF3rEPy1GUXIjO3s6yeghKDPI91ql5b9kftE3RICE6RfTmrXT5ev3Gv06wlySG8Av95kPtNoaoX%2FIITX%2BwiVKM18lXYQH39TTmEcWgZaaSAarcSURx19AptI70Neincvfao%2F%2B%2Bv6rLij4n0U2PP2TggOFlCoCVdPj1ovSTtGvXO71Sc7KIh%2FanUTORET6yblO8VO8YuvtM074pL46Yi5vczJiMFJX%2BJdsyXwlQkW50t%2FPwwH0WNQ81na8o5mVuoWh1l%2FpdX%2B%2Fu8NfHmabjFSCzVaD%2FUCmmV9eTPkUwau9H4PKeQwtahQPpc9%2FiE6jYydw8yZgnx6%2B8X%2F7AU%2BWgVNvpObge%2FPUf3OZT%2Ft40Asvbizb%2FXbBnFWVFFEAy1wl90UM9nfA%2BBiI%2BpskfqzgZGErZg8jkSxA97eLz2K3c%2BM0vAlv3SyXsUEcB7M6plc%2FvoARVIAWrEMEWVCgkTKZPpPFueJWTwjtZg%2B7YDzsjvrkusvq11GQG7daKiGUWxt%2B138Q%2BYfqE3NbJogjE1Bokqf2cFJ1OXln%2BiKE3ATZzjDespu9BjqkARpyZv5OXPGKR4JZOZmxKlOvCewIDMg7T2s0WKI1C7o3kc3E6xd5NnnjcnrcZXFhPOBKpwTtRcKg5ToRp5gBuvlC%2B2bsHFnVCW60areBgtvPgvYta3JKdURvyM9IR7MJ8S%2BvKQzB5Wk9M7eFC8GDPpblrC8KTJnpeu7wpZ9lKR8ebzhkwyO0LrrdDMNnBMQj8aVgBa788XAFKs9gs96k%2FOHMusEF&X-Amz-Signature=6684d53b2456addf8f7e49a10b299f1462e518b223fbbd2d613c52e1fa516ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
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