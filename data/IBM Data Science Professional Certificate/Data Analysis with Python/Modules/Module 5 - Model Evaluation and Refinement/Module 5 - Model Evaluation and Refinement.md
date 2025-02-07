

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=579f5922c31bd46224393dde970d8f4bc6b1600278a8bcf985df09a71bbb1955&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=e0d2b11217c64f98705d48e5b0d4c385c2f75aa61d56702732432a9fab6b7a19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=b9b967929654628251a5ffc59ff486527a500fd515bbcc940bb4db845706ccc2&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=c2ed229f15745909d890bc9c8f7f4f1fcab35ca4d1d8617ce2715dad54474eb1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=5a9d83eab9765a1d3435de6908c98ca16a7e8ace144aaf3a758e4f605052923e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=6a4e4eeba4154ebc6eec3a1bf058d11d401013541c0f153e0bc1a7a8b8f82c35&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=9886ff476208185e15a80a85b2353fcab8c166472eef32a042601372eccaa1f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=f96161e052231e7977b47ce5a25b8745a21c65865acda8d723fd3c296a82522c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=b9cfe659aafbde1bebb4e565f9522a2b08e0515c90ebe637efc051b3c3bd4463&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BDWIB5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEZIBsmOHSPjJaeN%2BzvlwDcdcVkfolqqe4HDyViZqPpeAiA8N0Ylz5wZSqWVr386K1x8ogaIB5XkoIXn9EuXIyHLKCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMVsy0hR8URbnm0d8fKtwD8qmbHLUy84SnJ4i46Yjqd7d0RE4vQSGQFBIc7d0%2FQxUgWw3wM1murkgDfZ90uYugtE9Cq8poG85W1eyxE55BH2hdPVAKYz5g%2BGCKsmhpHrSufencd2OIegYBKXXNtLi0UzaB9lUitVsNPDb9tRwh6s6tAWWAN1LWBJwLqAEalynqTYjat%2FArbZ%2BMymVAI3TUKAKR4%2BfhZ1dODsNSdIgLSGAZ9YZjI9p3a3YN%2Fxys%2F21GwJgSDH6WpKPpVlIhF%2F1PacDTsYKM4QwzoG5Eg%2BIWNCrwUYl2sYXCUyKGLZxgSh049rRX8t2sdwDL70nK0pppFLkMtuG5ArXzG6QKpEVSmw7IdxmRdXyzLiNWlIZHNWDlRXAqSUS1w5gcAsooM6p2BW1JFfejPTRUIrge01IPZWXWm6m%2B3TwKQHsb2HK9wdlXUGaXJc52jlQEtSjkuKPuE1SXkcfIbAEaGblm4KddKDIWZerE4aEoiuHoPsJcPPIefmKs0l4Ws%2BD%2F6POnQHI5otpPnF0oWG2TEgblPWTo7OX86vpEeXo4ClHUj4N8zOa7M82w1Z%2BgdDB12mafdssdyMUXDl6haCpivtDeZ4cL53hTGTMtvI7JXTXctJwnGNh8OkSYvy6avjZUc3Ew2MOYvQY6pgFCOhzzjrx5N1Y9vuqB%2FKSVp6PHW1UDU3JIPnJd3PFcSnlt%2Fe20YXVdy%2Bls3r1H1GG0e1u7BAgnsEwwid4Gfkto5f9UDe39cva1nA4rvgZ389u4plxCrp8zQ57C4m9KK6izwMu220F7Y6KirOHUu9zBFGXVhFFnjc81ntD5dmT3FYxrMsbGK5Vxe7TA57dx2l9gophtSa87N2NLliQjNSZK74MdMpQZ&X-Amz-Signature=904e4236e7697b4deace349ffc14af3f868c7c20ddede9c6a2d1a1f2538a1a71&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BDWIB5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEZIBsmOHSPjJaeN%2BzvlwDcdcVkfolqqe4HDyViZqPpeAiA8N0Ylz5wZSqWVr386K1x8ogaIB5XkoIXn9EuXIyHLKCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMVsy0hR8URbnm0d8fKtwD8qmbHLUy84SnJ4i46Yjqd7d0RE4vQSGQFBIc7d0%2FQxUgWw3wM1murkgDfZ90uYugtE9Cq8poG85W1eyxE55BH2hdPVAKYz5g%2BGCKsmhpHrSufencd2OIegYBKXXNtLi0UzaB9lUitVsNPDb9tRwh6s6tAWWAN1LWBJwLqAEalynqTYjat%2FArbZ%2BMymVAI3TUKAKR4%2BfhZ1dODsNSdIgLSGAZ9YZjI9p3a3YN%2Fxys%2F21GwJgSDH6WpKPpVlIhF%2F1PacDTsYKM4QwzoG5Eg%2BIWNCrwUYl2sYXCUyKGLZxgSh049rRX8t2sdwDL70nK0pppFLkMtuG5ArXzG6QKpEVSmw7IdxmRdXyzLiNWlIZHNWDlRXAqSUS1w5gcAsooM6p2BW1JFfejPTRUIrge01IPZWXWm6m%2B3TwKQHsb2HK9wdlXUGaXJc52jlQEtSjkuKPuE1SXkcfIbAEaGblm4KddKDIWZerE4aEoiuHoPsJcPPIefmKs0l4Ws%2BD%2F6POnQHI5otpPnF0oWG2TEgblPWTo7OX86vpEeXo4ClHUj4N8zOa7M82w1Z%2BgdDB12mafdssdyMUXDl6haCpivtDeZ4cL53hTGTMtvI7JXTXctJwnGNh8OkSYvy6avjZUc3Ew2MOYvQY6pgFCOhzzjrx5N1Y9vuqB%2FKSVp6PHW1UDU3JIPnJd3PFcSnlt%2Fe20YXVdy%2Bls3r1H1GG0e1u7BAgnsEwwid4Gfkto5f9UDe39cva1nA4rvgZ389u4plxCrp8zQ57C4m9KK6izwMu220F7Y6KirOHUu9zBFGXVhFFnjc81ntD5dmT3FYxrMsbGK5Vxe7TA57dx2l9gophtSa87N2NLliQjNSZK74MdMpQZ&X-Amz-Signature=8bc6bcded329aae3d10b53ea1ac558c36270e0babff96e96f53f7f27014a91ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BDWIB5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEZIBsmOHSPjJaeN%2BzvlwDcdcVkfolqqe4HDyViZqPpeAiA8N0Ylz5wZSqWVr386K1x8ogaIB5XkoIXn9EuXIyHLKCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMVsy0hR8URbnm0d8fKtwD8qmbHLUy84SnJ4i46Yjqd7d0RE4vQSGQFBIc7d0%2FQxUgWw3wM1murkgDfZ90uYugtE9Cq8poG85W1eyxE55BH2hdPVAKYz5g%2BGCKsmhpHrSufencd2OIegYBKXXNtLi0UzaB9lUitVsNPDb9tRwh6s6tAWWAN1LWBJwLqAEalynqTYjat%2FArbZ%2BMymVAI3TUKAKR4%2BfhZ1dODsNSdIgLSGAZ9YZjI9p3a3YN%2Fxys%2F21GwJgSDH6WpKPpVlIhF%2F1PacDTsYKM4QwzoG5Eg%2BIWNCrwUYl2sYXCUyKGLZxgSh049rRX8t2sdwDL70nK0pppFLkMtuG5ArXzG6QKpEVSmw7IdxmRdXyzLiNWlIZHNWDlRXAqSUS1w5gcAsooM6p2BW1JFfejPTRUIrge01IPZWXWm6m%2B3TwKQHsb2HK9wdlXUGaXJc52jlQEtSjkuKPuE1SXkcfIbAEaGblm4KddKDIWZerE4aEoiuHoPsJcPPIefmKs0l4Ws%2BD%2F6POnQHI5otpPnF0oWG2TEgblPWTo7OX86vpEeXo4ClHUj4N8zOa7M82w1Z%2BgdDB12mafdssdyMUXDl6haCpivtDeZ4cL53hTGTMtvI7JXTXctJwnGNh8OkSYvy6avjZUc3Ew2MOYvQY6pgFCOhzzjrx5N1Y9vuqB%2FKSVp6PHW1UDU3JIPnJd3PFcSnlt%2Fe20YXVdy%2Bls3r1H1GG0e1u7BAgnsEwwid4Gfkto5f9UDe39cva1nA4rvgZ389u4plxCrp8zQ57C4m9KK6izwMu220F7Y6KirOHUu9zBFGXVhFFnjc81ntD5dmT3FYxrMsbGK5Vxe7TA57dx2l9gophtSa87N2NLliQjNSZK74MdMpQZ&X-Amz-Signature=bdc7dfeafab7287f04694a489acea80f2b57f5b6e04a151479848d1b05096ff2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=197c7082af0c68ab7e0b4e8b657a761cd26d90cb612794572c6be82b9ffc70ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=8b69e9219bd122fa45dd2d15d674138fd4b17305516174929d9318002815aaa4&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=e98a39b982ec0f53d007647ef6e53e407613d24faf079b00cd1068891d1d85ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=462739caa3aecb85f03c7d524d30d12e6c3f2f321ec70f316c95e095630263aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=bf46f68432f753790de9e0a6a7931db117cead852aad3da03250a4b402394b5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5DTUQK5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDc7Kr%2FtEcTTjALRVM4sQnQr8Tx8SE8KZydNk9vB1XcegIgI4girr%2FST1nS4088mqErOKV9d2pAt2SCXAlW%2F7%2FMZs4q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGsCL0MjZeCy8TTm%2FSrcA3onBeH47fKrxdMw%2FM01Tp21ijIvomsOxHLiwQyPP%2BLWF4mQ6zq0BI2y93nEYRggyr5hbNF8lJ2R0wCVXASYw4XzCsf6VKta7KRCADck%2BIdtfNMaG%2BSljaUbahA4cJjhDurjvpmGfI%2FdQNoZmz5lyFdaOdwtf7PzHX9AoX%2FCVqPgJq2Ajdzi06kym%2BlouB0PNRbxjbtumVKkl64oQAqPr%2F7lBOuqDA3afHsvd71HsbPITUfQEtfeBKcKLyFvhpXNplV7C6YuX7NYZhVYMReFVRqap7JS%2Fxym07PXdVnVxvy741mDebMHVxeOjJiEi8vJSXM51uISuS8eSCbXeCBrwmNR2jKcGDyKd8ozUBOlVkALXyzIiaa3w2HuFRDH%2BQZcOKbBPc%2BkJvKXQ%2FkyIVReA%2FjsfHSJL9hoMV7UsD0NtTUWFnnEc%2BCoKuL34F5DM16dR11xRYTgkG2ZbENsUyOP%2Bw2sgzMFQYKREw5kC%2BAJoHqGV5CFbFzvB3%2Fw7GIHY7BQCt%2FC%2BQfFqnw%2FyO3KnLdlNtXL%2FRZkymTac6q0Wse7ADAOdHo5X%2BboRaRkcbKVVRhLPvqpyn4WgXS%2B5Yy%2B7rQa9DIcue73S1%2Be%2FsacO2VKovykJLRQpBiwy1NmHtN4MJ3EmL0GOqUBP5E3FDZM%2FB%2F7WdIlk8UKmpnXTtyAtJvw840cdPEOxgKxH%2BQQydjJSJ5nNW8G7Q9Az87oah7Jbi1Us5SBs0yh%2BWNLTuIMlMA5AwvJrhfenvjuFCOsSMJI%2BXqOd4Zx42QduvYAM7l7%2FY8EmLbnEntMlnmYIwFRWoc%2BteoZU0%2FEtn2yJ2LJtNijaEbSPyNGLCxGDTmvX3xUAjDd9VfusavKOFu54lz4&X-Amz-Signature=e36b51e61b0d21cc3f5b1e0679797f1fa58c954e594c7e73819d2de4218d89f0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY72XUZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCmxAYGXpyzzTOjib1XMU2qjAseUl9A3mjC7uXoZ3wT1wIgDT3q4slFy6%2FYExWoi1Zeby7uGpbwhWxX9xCD9gFfjkcq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDB%2ByiyzypZk4QH2INyrcA%2FJvCr%2BTXTVby9R26Q0E2hYJIy6QvGSN7cQqwRM1LtGFf0pfoi6r5SCkZFM4Ppm6tjU4MQqpDCpwJFwxc1NXQItduqq0l98BquxGbXhXdqo3r8hvxNbSmALT7IYRY82Talt1wvSBUgSBcgCCIjFUe5JBJ%2BPyrO8M%2FiJu9jlyZQNdeiqwRqhTmDTDQ7sAR1F0j%2FRWsL4DbeKvyLe1CnDzv4QYrC8NDCzOh2yS4iMDc4eDzKe%2FrIL2UXitdxnJJrlB5WtDsOm4rEkIMRltIdHajU8ektNMM%2FnyjSYQMz93LwAqAwkXbtZRTQzRZK%2FJenRonFqktxySg%2BkNjnmOgtB0lEMhQ%2F4A60RfpSULfTB%2Fg3u42Q%2BhabyDfPBT0r8SHNA8osYEW22fsjP%2Ff00GGCNiH65WlJRne6NE5LCliQhKOh2ocuJZ%2Bi9Xiiz2nryRj1E%2BkavA1ilngvkIXjwK9s6k%2FLe%2F2en53%2F0cNMIqhOMFfUD0c0BFaQj0utCRkW1OCS9WTm5ILepHnf1DcwREGqYqw9em4KeguQQgS6nMoO0sDIVcm909gp3jhJKt%2Bm%2FsyKz72QBxRzeF8DZ1dQXGSwlYpll%2Fi4nhffYrQoOI4yUS4AFuZ3dfNnOxRPhnvLI7MPvDmL0GOqUB4SQtm%2Fq5mAQ9yePJ80UqAdVtpLVrzjrM2JbXc%2Bb2MLAdL7P76lQ2YmHcV1DVFAwsTe1F1T7kdF85kQiJ2c8M8TF9Jt%2BJaq%2Bnqats%2FuctfO8Q1F07HntYwlcjgDi5gNr9bccxgVOKJJYKPPWYM4hP1AoWygALbJQr3v%2FNp9EHuBwCBjbUZyP%2BHxYXiiyCXQmJY%2BuK7LhoiO2WEa8kD2OOfD203tS1&X-Amz-Signature=105bea0d26f95f60ab7727e68f7f63f3512ee894eb988d09ac8425ad5f971f9b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY72XUZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCmxAYGXpyzzTOjib1XMU2qjAseUl9A3mjC7uXoZ3wT1wIgDT3q4slFy6%2FYExWoi1Zeby7uGpbwhWxX9xCD9gFfjkcq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDB%2ByiyzypZk4QH2INyrcA%2FJvCr%2BTXTVby9R26Q0E2hYJIy6QvGSN7cQqwRM1LtGFf0pfoi6r5SCkZFM4Ppm6tjU4MQqpDCpwJFwxc1NXQItduqq0l98BquxGbXhXdqo3r8hvxNbSmALT7IYRY82Talt1wvSBUgSBcgCCIjFUe5JBJ%2BPyrO8M%2FiJu9jlyZQNdeiqwRqhTmDTDQ7sAR1F0j%2FRWsL4DbeKvyLe1CnDzv4QYrC8NDCzOh2yS4iMDc4eDzKe%2FrIL2UXitdxnJJrlB5WtDsOm4rEkIMRltIdHajU8ektNMM%2FnyjSYQMz93LwAqAwkXbtZRTQzRZK%2FJenRonFqktxySg%2BkNjnmOgtB0lEMhQ%2F4A60RfpSULfTB%2Fg3u42Q%2BhabyDfPBT0r8SHNA8osYEW22fsjP%2Ff00GGCNiH65WlJRne6NE5LCliQhKOh2ocuJZ%2Bi9Xiiz2nryRj1E%2BkavA1ilngvkIXjwK9s6k%2FLe%2F2en53%2F0cNMIqhOMFfUD0c0BFaQj0utCRkW1OCS9WTm5ILepHnf1DcwREGqYqw9em4KeguQQgS6nMoO0sDIVcm909gp3jhJKt%2Bm%2FsyKz72QBxRzeF8DZ1dQXGSwlYpll%2Fi4nhffYrQoOI4yUS4AFuZ3dfNnOxRPhnvLI7MPvDmL0GOqUB4SQtm%2Fq5mAQ9yePJ80UqAdVtpLVrzjrM2JbXc%2Bb2MLAdL7P76lQ2YmHcV1DVFAwsTe1F1T7kdF85kQiJ2c8M8TF9Jt%2BJaq%2Bnqats%2FuctfO8Q1F07HntYwlcjgDi5gNr9bccxgVOKJJYKPPWYM4hP1AoWygALbJQr3v%2FNp9EHuBwCBjbUZyP%2BHxYXiiyCXQmJY%2BuK7LhoiO2WEa8kD2OOfD203tS1&X-Amz-Signature=c82f8cd5145ef53d94c321b8fb9cfc7d7ebab5c11c24004f7270c083c067e0ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FK6OGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDQ6sOQNIPN420y%2FuuT%2BfOawfybX2RvM0JOsZT07%2FHOowIgVmmp2cylJ2OTr3gz0%2FJEHZXGd55e7cJdghre1UcEYLcq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDBkET5aKzen5dA2LqSrcA47evn4MAvauoi5Vo9YvaMG77yK3wsEXiXlK9DQB4tkwdSQuFpMEZUs%2Fg%2Fnxu8gwEsGIaP16IyAsI0ZMaERhHA6Q25zmoUhkRCoH2dj8O3tnohlbYo0GSbVgffkJHsvbU1sLYEJsM7R7ZoMQ1%2B2TVHaJwFHWJdrPZL3H90mEjqUtTARcExFd8Dro%2BVaP%2F9Y7DIgMKscBlaZi%2BxDEWZ3tTxNBzpql0H%2F25ZdqUABObQoh38Aeuq8z9ofXTCirNN5wJxkOKEn9wj4VCMgeaPb6mPhKAxtCUCGiy48p5kLRgpiIu88MmINCKKkp19asLG35LSK%2BT4Gco1kkzWtAh2xshbhDnE%2FfELeJV1s41tyUOXmNdqi2wg%2BcDuS2EiW9031THq%2FL7xfv3o3QfCuG2vN8gy1iuRXAig1fV%2FpQOTZVAU5Z3YCrZ%2Fzq%2Fm3s56grRXbnUsGrJzx%2BKb2F6QyUu3fhQBtYXyIv7Y9IZFADIU%2FJAVdvUvzoaBjgvejYXxfLAEBvKXvT%2FYA0wlu21xfkZOlqglSxzHg3LPuV1K23MkOumbckA6vrJGZ65PGwv3pht7jktZl4bvNZf2SKjvXemaFy2406JspkSiJZTdE8VlVwpf1nQd8%2FunHX1ZnHtDZbMLrEmL0GOqUB4m4FWbGPvU6qG4qpvBV0ndsaGOKynrh9lxCrHx5HOzeDz%2BEcwgSWXnz7uA%2B1AAlDiTod2lAsdXE%2BgtuYftGxSUqdX90P4WUrC8edNkVsFrEtfe2xODsSdkedDUlWODuHkbkscmtSHyj07p6CZnGuPtqVZNt6zRFomEaBZT8%2Fgqen9IHFPbYQnLmilWqiAXFvKTs5ysg%2BBXqkltbyn%2FbUq4iEc65j&X-Amz-Signature=f3f6694e05daaa18273f2e800c21699da8f63ceb920539acf5dde3e69264c12f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHZLEGM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFuGMShu5Koe%2Bu5jEgyh%2Fnw5F2K1VcXYCkgfU4kArt5yAiEAr%2FbOOw%2BWTCKZthRgYD8VZT%2FKkU3J2Im%2FLiolOOO9ADsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDPP9IqO%2Fx43Ytm9xBCrcA3xF0tmedOpg7Nr%2Blpef0IrEE0mE1Yl4FzXKajUgXU57JqkbzHN7uzpOsuwflkbOtA0IV5fXhNwBKHyi8gZYp2PJsYCJdyvR%2FEK9%2FnjS0yayUJVXWYVR0rmC%2Fan6Uy7Z4elVD4seWPyZQcKsn%2FpDcAsH7PtrlIHEyCnXodcVcHJ1K0IHEr4QT0YMSmLa72bO25xqtTpAADxunS5R8ucV0Dndbu9gzlzZ9nVH%2BNnyhs8kVz52OK%2F%2BzNkwMntCZGzX%2BFbxnx5g4AgaL02FCUbzN0FczKQJ24DPYwC9Vz7pgxTlshbeL1xQn9iM%2BC9t3VzmWPI04nSkKLpGt5o5gMvd0kwliIGrIpA4ZzZc39aAEoROCBVuVNpFfxxFlQHD22ffZoUa8Ra3%2BLVgeiHUum8%2BlsrqhINHkHFQLVtgBPz0Q6XJvVKYGiz%2BfpC%2Bj6rra2Mzh28lfoDKTxvC0splNEn6Zu2kxkS%2FkuUP7FhjXTKpuEYwcir8klh1poln2pd9JAYjWogma66HbqAXfKNoypDXhvSMDSgk9BVx2LuSvPc9uic5qOv0wWwSTKYecpWvJXhq3jMZs8Nbkd%2Fcl6eEPoh17Ds0ZU6LcVS76pbYvoMsIH67WqfQRUbu0dXT8t4kMKPEmL0GOqUBLE9KrC5FCy78iFf7KmhH8BWiRb%2BlJfrJ0VKqoDPM%2BIS7hext00h6T47lFbx9S%2BQfMEvEB%2BzilK9bRr1mLiXaThWYc0tA8jXnlFvc3vzElkAcv2P50XQOrjCXEAlos74bY4aXB2FBfyYGsiZ8gUQUZqxo44pF624JKvZcHZdXNzLuNNTE0zo1dGR0WjbiVSINbfWwDD6LcbWH1kKPwNrXYTof2Lfz&X-Amz-Signature=a593eb853e0349d47e7fa59a04b5fbcd63099bbad702b6c314606151a8d832d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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