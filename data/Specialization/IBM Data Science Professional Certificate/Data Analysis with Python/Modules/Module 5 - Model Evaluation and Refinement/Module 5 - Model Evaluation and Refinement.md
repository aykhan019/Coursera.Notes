

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=25455ebc49cfe1094d58b3eab8caafed97b99f147ae3a22dc52e93a62465bf5a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=64d1889204dc84d1d95f0e2c707af90cfa54e3bfb879f14026968058ddfa4f34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=60a7fe025c8570608275a1287754fb7ab9fee5c956bc71f5a437c355b13ed544&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=c58a536eb132bfb0abd75a6668f319d8d3ac7aa9a757bd5d61833e25e7fed4dc&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=28abd3a76a7fb960c18352fb96e3120e4460dc867812751b2bdbd444c314a0a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=1ee4b0b381ed976fc1d3caf1c8c5ba679e0308c52bc289059a5fca39a519fa5e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=43abfbe636983d61a04adf71220793dee68f76988e881246d5af08f0d7c7774a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=219b17f9c894370de5233389aba77d28c6db2754bbfb8e7c658395ef0a547d74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=e3372c597c9c328ac85bcdb68f211e0be714d6b48d61c6b290dbd601654da600&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=f6c6a6bd0e77d9568509904c6267f3e42245747e855b383177e2e87d114b22da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=41e0b7e054a83cccaeb7cecbd141826430a372c1fa554904565b6b1bfb713b44&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=4156323ba2c3939d4a92b8b88e58ae1c5317c995a441974ca62beb8c7f082dde&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=975755a228ec424d548ce0364a51e252c2f8a038e22b45be59c5495968e74ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=5912d179207ceab53eff0243ff08be4bd9c7d4c5c1b712a77884d18a9ee02dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=f7b39cd08414738eb8c4ac74a0fed74f58b3050018b99af4b7ca217413aa28ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=2cd043fa72b9a925eb9e6e51906a8dd5f08b89b6fa7707d50478f6fd48dcd3e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=95cdd4d7ebc4cbfb5be3da6c9c0ac6aaef905f92b9191c9d58c3de465045ae5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNJBMYS6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG2MZV0Oa%2BUi%2BrQuMK8Z886JEr%2Bn6Q8Q3kpqIxnwS5w%2FAiB%2BOKOrRDpurvMEl7YpJqhK3Arj%2FxFAb4ggwTWiHQC0myqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUUhstUZvcT4janUdKtwD6rIlC6Ra8dzXhzvB9vzVrSf%2Fg%2BZ%2FUMw80v2XyIxklpUg1ggKRotoQj%2BiKq%2B0gw%2BkTHe%2BmHOxcmnIA2c9i%2BK1b%2FPQ18Va0xXJWAZJmT3TPcH9BMzDVGha2s4Cm3yQuaTiet57DsuksHdi7mK65JQKRkhNWYWgWuyXVHqcxps6fdpihq9atZFaZrfRKOklNe0jdu%2BjTRNkbzugyl%2BnDgK2zPFNFf0eon5N9s2scdejpzMcgcWWvaLebPi%2FpSnwzgf1U1XXWIxWApwZmyUjnOoCi0RtChmwx3Z5KNS%2BfWAXEZ0lNIAp%2F0Xwm5LUXnvEdcHssXTnqGnqb0tkJd2UDogyfjQB08hDhfTnvzIBBjVkT%2BIBCMypHM3p4eQcldmGx1YByS%2B5VzkL4%2FM5UwFtlPU30fq3bbOPSYfMpq3IMMECoDXSnUxzZXs9iuVJLSNl4uQ174qwm8enQ9bVqySmlgAf53pHUSRPvh4%2Bj1nJClIMOOlngrTwBSA1L5ltDa0YJA86XK%2F0%2Fa8ypOe2uLaVHqkDZ2zHlGj98aKF5Vtg4hbYnrdLN2L9ckaNiPeQiBBQypQFwkSti5jVFzP%2FzsOoJyqKEqTlRf9v2WGOtJxMblZ0%2FwTWKkuFQQHLcmHn6bgwp4PpvAY6pgGv1WdQ2pmNLytODMkY1fH3WQ8AkzC0wCjCAD2kmNDOJ69157eQXDkmQ6IaeSiOHx00lV1l1cEqCY11kk5s4LLb3Y7JT6xkJ7cr%2FkzXraOR68ztzfkoX0JfH0vR6j1t5KhlO%2BD3HUUaf91LChCKiwoZZesXwMk3FbVpOevGyGci1Y4HZ6sKMOmvxf0ulfz%2F893uoWWkMV%2BkROEgOLO1qBTLT8wVTTbH&X-Amz-Signature=5f43847a1720c76ef2ebbf98eaeca4e2645422c0659eaa0b454f0007490d73a0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOHQSKAI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8yu8dBU9zvUlQx4iZ2ZaoLm9NMURbijf93is7A9NcZwIgY6xtO%2BKtHcj%2BRZXfUDGnJ3LSw9QqcvUHDZQ8emysvlIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzc%2BThWBrLd7LB62CrcAzZ78Cn3%2FNVKb28JpRh1cRdArgnHXxB5iIw34QyPAlxlbnum8u9Gr2uN7hpXzS4ie8RlPpP8ZN9Z99p%2FrwdITbZWaEMjNwBNB2HDAHR1bMqJkpMO2YZFsF3dBewy%2Bgm9FQSO3cJuXXNFPA00BJ%2BaxCNMz6aa82cCqiMc3gn%2B3dHlt0v1qdIMn3wNQHDLzTzjQgnTAeOCVb9O3YrIrqyIphWuIvDML13rov%2Bwuhp%2FmpT%2B2jlAE%2By32o53b8wuVC2jWmjUKMjsJbO4tdPZAkaPlP45MPy5NQR%2Fzk%2FG%2FBjAzvB47A8oTSW4nz0ugxp3ltMropiS0DOrFn6gzZl%2FmzLJn0%2BvL7AbcrpFjxIA3JuFXhkgJ40hXSI6jNZTWg3b8ICejPsX6ak8KvzdOanHkIod5iHOD8RQNqJ2ecFGYKaJWxlceuy89r6yxc7Kphr2TJAWZMxRoulF3NmM%2FNpvVMbOWo9vtnJOTPxmrVA1Dac52JTldJOdmNXVFPR7SRTaNUlZF62eiDFiRmRXEK1OQH94wOp6rrQHp0YmglH8RN5oP6Pn6h4BAjH0e%2FQ8MWHRXjzN4JcAJkdftQkSNH8blKdlJ5i2KmvOX1Vjg3fuO3iuyJ36jxffWDsig8dY2JljMO2D6bwGOqUBXasjdSQLaPSh9vhwCFd2JwuzuVbA%2F2lkNnZk6RcZfo3%2FTbHM5OH2kbPPJNoRTW3JDUuSfYZW1yMDvXWSXMsJ%2BW7IumGXP%2Fn3E9EF7Sf8NFg15Dk9MTM4f3EJDoK3malxXVAauxZUdgiKpk46lSrpKPR31Q3LOxDNB1ZumjCP50JFCoweq0Vj40O1Qtr%2FzMf9%2B7svNJ%2B3owv0wClPpe3NFtIgSVXE&X-Amz-Signature=696481634be98dbecf3d11e95eddaec0c07584a2eadd2e5b92098c4eaf8f67c6&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOHQSKAI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8yu8dBU9zvUlQx4iZ2ZaoLm9NMURbijf93is7A9NcZwIgY6xtO%2BKtHcj%2BRZXfUDGnJ3LSw9QqcvUHDZQ8emysvlIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzc%2BThWBrLd7LB62CrcAzZ78Cn3%2FNVKb28JpRh1cRdArgnHXxB5iIw34QyPAlxlbnum8u9Gr2uN7hpXzS4ie8RlPpP8ZN9Z99p%2FrwdITbZWaEMjNwBNB2HDAHR1bMqJkpMO2YZFsF3dBewy%2Bgm9FQSO3cJuXXNFPA00BJ%2BaxCNMz6aa82cCqiMc3gn%2B3dHlt0v1qdIMn3wNQHDLzTzjQgnTAeOCVb9O3YrIrqyIphWuIvDML13rov%2Bwuhp%2FmpT%2B2jlAE%2By32o53b8wuVC2jWmjUKMjsJbO4tdPZAkaPlP45MPy5NQR%2Fzk%2FG%2FBjAzvB47A8oTSW4nz0ugxp3ltMropiS0DOrFn6gzZl%2FmzLJn0%2BvL7AbcrpFjxIA3JuFXhkgJ40hXSI6jNZTWg3b8ICejPsX6ak8KvzdOanHkIod5iHOD8RQNqJ2ecFGYKaJWxlceuy89r6yxc7Kphr2TJAWZMxRoulF3NmM%2FNpvVMbOWo9vtnJOTPxmrVA1Dac52JTldJOdmNXVFPR7SRTaNUlZF62eiDFiRmRXEK1OQH94wOp6rrQHp0YmglH8RN5oP6Pn6h4BAjH0e%2FQ8MWHRXjzN4JcAJkdftQkSNH8blKdlJ5i2KmvOX1Vjg3fuO3iuyJ36jxffWDsig8dY2JljMO2D6bwGOqUBXasjdSQLaPSh9vhwCFd2JwuzuVbA%2F2lkNnZk6RcZfo3%2FTbHM5OH2kbPPJNoRTW3JDUuSfYZW1yMDvXWSXMsJ%2BW7IumGXP%2Fn3E9EF7Sf8NFg15Dk9MTM4f3EJDoK3malxXVAauxZUdgiKpk46lSrpKPR31Q3LOxDNB1ZumjCP50JFCoweq0Vj40O1Qtr%2FzMf9%2B7svNJ%2B3owv0wClPpe3NFtIgSVXE&X-Amz-Signature=a949a8855d53d10b50fc5e27e0bea2e6cb1035b97e3853b9891072abd3cf62ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6RHM73I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCleDqgJpn4S%2FwTC%2BO9I4KhOhpgwfg8JUdRGavDT9TJRgIhAOxMz31cSHtrF8cKrXiYAFQSDYRfZMA69819pNpwmDthKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWO6HnFVKKc3vURYIq3ANSm%2FzsNPMUvvBtv3l9ymNXFAWF6xuublLWmJd1VZAKFYHZgOtbpfUcaNymLtg%2F8jTp5TwYO%2FYFmzP0%2FGZjW0iEVagT%2FiCTlHlEwy6yPucT7LwGHFGaO7ujE1K7D8%2BiWTY6bRDHU%2BTZaBqrZMXR4UT%2FT6ZoVBnplhBOxiUEi7JQErpR2%2FJPwFrRbxXna337tE3DI09WyUCEbZP88VveXAzfhW5Tk2pJRml0LjpMmRqFBOj75uQFN8FxXfGZ7057dJOyiLqJE2lW8alHjrSG6C55NCJXnfhQozNGJQ906hCdP5hO5X5%2FVuUB7XcECj8RiqWI1U49evYxvqf0YhFngWEoTsi8IgYhYyVjx3llRd%2BlyAVWPs6i07R8gL9na2bT462eOJh1Xofx9Ob6NhwwrTihpMhU6LOkvPgXrekwuX2Xf2y644O848y55BKozPiBQnBxEpsmvFr%2Bi%2BYFPU60oOa967oI6cIF5bHeDjc41b01IbvxHO8T%2FxdldEVfOMXxEZBaU8tGUsXp3hSWENcee1VXpv1bIs4wRpg87tZS5soRIDAMfssELrPGh4duMA9uUQFMPWqsG4CbpF%2BWcvmMKD6m1zaSJxhgEMCXt5lHWmwA6p%2B4WpBbAT9GWuCAkDDsg%2Bm8BjqkATNjCjm5Ryhxha3MeurlKT7fPhdllQg80pR3aYkDGtSEUuUa2j%2BYTQCzi1g2s6%2FOzlvHovnOPB5VKYv%2BNYYjKZOKQO%2FO06W%2B1bghrDK6JHs7N9z0pkHDk6TdoJLDlpRo8mBTedAo2Lpl%2FNjH%2FJvGCsfkQcaAGwDaIQpJOFZ5LK%2FGIxwDFJD49U5l4COL1eWM7ALHStuUQ4FQ2c%2BlaOIe7B3pX%2BhL&X-Amz-Signature=071748bf2b33beabb77200c675087736a821a503771c0b20b952ae3f2df3d057&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=a23242934d6621458944b52882644053620dc7ab05b2fc1186fdd47e806c3c64&X-Amz-SignedHeaders=host&x-id=GetObject)
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