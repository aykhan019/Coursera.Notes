

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=9b21dbd13e914f1a2d5ae9153fc48e399085ad663f6c3ea2f8f9a3369b6fddfb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=6dcb0d01b433dcd57f1486ff0a05dfa35fc9acf08ffaaadc90c3535fffcd1e92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=2bb33b1301b6f1ccd73d3d069274b07d8fc003b914eedc9f5974850735729ae1&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=a8e9797af3ee1d94a083ac9e452bef867cf7193aa6477841f0f9b61ef90cf3b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=3de1c9b952d8b62bc04aaa47b5fd441f78314e2e7cb16829b7d48610bcb692b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=c2b137af1034a741ecb9a52d93dbb8053eab04fcc74b70eb09199bbd4f600eb3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=5a656da3d98994ed515be3c55f8ee1fd05bab887d0c1c3c9b1ad53e2af0452ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=5d43dae896aa413cf1ec40e3e927aa3e9e5b60918e3cb2e10b4d86ad89b9b81c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=1269e3173c7229e86813ea7bad4a6bc9391378c52142267c7cbdee2ca6e31834&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFIWDGVB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGWEC2wzn%2B%2FKyCOoktzOdc%2B5GPMAAyWt%2B%2BVx2kczYpttAiAGmcek2Wsx4%2FmJq2PJuTHj5U299EMSFKP7H4QVgYk%2F3yr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMOLo1dYB8QrEr8RQuKtwDQFiz8TfN2JWiWbOVhCGvoO%2FRyLHBGeZja9GsSG2QSz6IUNrSYSry%2BXoudz0zVlnFVvhjPUp04KNQI4rleVlw%2ByP0yiVhLRDbg3cLAnyeD82JKiDwBe%2FRDbba1BKcfDLg11ca%2BUNniOVRujBKlknHKrT%2B46w2E3wZnHfAcC0CxqbUHJG29BbZ1KaMcWGvXWuYLWGTLEZK1VlPSPREay2zXpk8cwjKcQlREGQ2UWtx7IM7uytoKSelk%2F82XenAwb8SiaMPBcbHJJ92j9Eny2rAkhBuoFPHRiYP6NFPPaBzfm5mx36DHHGWnaIvGH7yF3fvugF1vfy%2Bjf3PYLGDGiwBqDZFW1m%2BeKRfJBl7yn%2B77HmW4szMvLMw3w%2FdwGOn5FAC78Jn1uAwTDs3un6tJl7EzOCtbujZ%2BoGsNbMnbrw94c%2Fg7GWAIN7T%2F%2BA3MjuYiYeZP4hi0KvEZEEwiEFqlFbzykuB2IW%2BtwgtSHqWaAhLPdQLYdiGcqO1VNdNBoMRc6938t6hxRXaFGoNw4l8thgW91vwLkVEao2umJOd0jOsXqcezyC92yE5tDa3FYs4kGxqnQjdKV6PVXXmXjkr%2BeqYM9ba2TZ1AygnazxZXB0RO7E%2FuSp6gan%2BspZ8g%2BYwpZ2OvQY6pgE3E%2FWN2O%2BgkqZ0VdtDp04hZ1ccaqt3JV4JZvBu50stlt7zXleH%2B56bp10jQxq0nVnXveFJB0xl3Eq%2FmeL4W4DXA4hPn3%2BiXOUd8TkAKygra22aFA1bK%2B8RXuYPp7lZ99oi9l9GkmPmzde2pKZC5KKqL88XgLLDCFMRd9sZhntCpYjd97bHC71Pb%2FY%2F9L1MNagxaeaWI0PwQBdIPD%2BHH6NNpfT%2BLV0I&X-Amz-Signature=3216412ca648026b2726192bc5ab207a46e48a6ec811dfaa6f8115c900c544e7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFIWDGVB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGWEC2wzn%2B%2FKyCOoktzOdc%2B5GPMAAyWt%2B%2BVx2kczYpttAiAGmcek2Wsx4%2FmJq2PJuTHj5U299EMSFKP7H4QVgYk%2F3yr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMOLo1dYB8QrEr8RQuKtwDQFiz8TfN2JWiWbOVhCGvoO%2FRyLHBGeZja9GsSG2QSz6IUNrSYSry%2BXoudz0zVlnFVvhjPUp04KNQI4rleVlw%2ByP0yiVhLRDbg3cLAnyeD82JKiDwBe%2FRDbba1BKcfDLg11ca%2BUNniOVRujBKlknHKrT%2B46w2E3wZnHfAcC0CxqbUHJG29BbZ1KaMcWGvXWuYLWGTLEZK1VlPSPREay2zXpk8cwjKcQlREGQ2UWtx7IM7uytoKSelk%2F82XenAwb8SiaMPBcbHJJ92j9Eny2rAkhBuoFPHRiYP6NFPPaBzfm5mx36DHHGWnaIvGH7yF3fvugF1vfy%2Bjf3PYLGDGiwBqDZFW1m%2BeKRfJBl7yn%2B77HmW4szMvLMw3w%2FdwGOn5FAC78Jn1uAwTDs3un6tJl7EzOCtbujZ%2BoGsNbMnbrw94c%2Fg7GWAIN7T%2F%2BA3MjuYiYeZP4hi0KvEZEEwiEFqlFbzykuB2IW%2BtwgtSHqWaAhLPdQLYdiGcqO1VNdNBoMRc6938t6hxRXaFGoNw4l8thgW91vwLkVEao2umJOd0jOsXqcezyC92yE5tDa3FYs4kGxqnQjdKV6PVXXmXjkr%2BeqYM9ba2TZ1AygnazxZXB0RO7E%2FuSp6gan%2BspZ8g%2BYwpZ2OvQY6pgE3E%2FWN2O%2BgkqZ0VdtDp04hZ1ccaqt3JV4JZvBu50stlt7zXleH%2B56bp10jQxq0nVnXveFJB0xl3Eq%2FmeL4W4DXA4hPn3%2BiXOUd8TkAKygra22aFA1bK%2B8RXuYPp7lZ99oi9l9GkmPmzde2pKZC5KKqL88XgLLDCFMRd9sZhntCpYjd97bHC71Pb%2FY%2F9L1MNagxaeaWI0PwQBdIPD%2BHH6NNpfT%2BLV0I&X-Amz-Signature=e6054668905d7a3f8fb588bb0dc060ffb6febb8bad4a105d853663f7ac1e2c2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFIWDGVB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGWEC2wzn%2B%2FKyCOoktzOdc%2B5GPMAAyWt%2B%2BVx2kczYpttAiAGmcek2Wsx4%2FmJq2PJuTHj5U299EMSFKP7H4QVgYk%2F3yr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMOLo1dYB8QrEr8RQuKtwDQFiz8TfN2JWiWbOVhCGvoO%2FRyLHBGeZja9GsSG2QSz6IUNrSYSry%2BXoudz0zVlnFVvhjPUp04KNQI4rleVlw%2ByP0yiVhLRDbg3cLAnyeD82JKiDwBe%2FRDbba1BKcfDLg11ca%2BUNniOVRujBKlknHKrT%2B46w2E3wZnHfAcC0CxqbUHJG29BbZ1KaMcWGvXWuYLWGTLEZK1VlPSPREay2zXpk8cwjKcQlREGQ2UWtx7IM7uytoKSelk%2F82XenAwb8SiaMPBcbHJJ92j9Eny2rAkhBuoFPHRiYP6NFPPaBzfm5mx36DHHGWnaIvGH7yF3fvugF1vfy%2Bjf3PYLGDGiwBqDZFW1m%2BeKRfJBl7yn%2B77HmW4szMvLMw3w%2FdwGOn5FAC78Jn1uAwTDs3un6tJl7EzOCtbujZ%2BoGsNbMnbrw94c%2Fg7GWAIN7T%2F%2BA3MjuYiYeZP4hi0KvEZEEwiEFqlFbzykuB2IW%2BtwgtSHqWaAhLPdQLYdiGcqO1VNdNBoMRc6938t6hxRXaFGoNw4l8thgW91vwLkVEao2umJOd0jOsXqcezyC92yE5tDa3FYs4kGxqnQjdKV6PVXXmXjkr%2BeqYM9ba2TZ1AygnazxZXB0RO7E%2FuSp6gan%2BspZ8g%2BYwpZ2OvQY6pgE3E%2FWN2O%2BgkqZ0VdtDp04hZ1ccaqt3JV4JZvBu50stlt7zXleH%2B56bp10jQxq0nVnXveFJB0xl3Eq%2FmeL4W4DXA4hPn3%2BiXOUd8TkAKygra22aFA1bK%2B8RXuYPp7lZ99oi9l9GkmPmzde2pKZC5KKqL88XgLLDCFMRd9sZhntCpYjd97bHC71Pb%2FY%2F9L1MNagxaeaWI0PwQBdIPD%2BHH6NNpfT%2BLV0I&X-Amz-Signature=62115bd66456b402f7c42ff70544915b3c2f44bc225c8bb3f90e3c0898c958a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=248e174f68a4ee7ae4287d93eefaec6ed16be225d6cf12c8c758070c892e2806&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=c041bfcbf57bac073aaf9ecbbe5e9ba3777119b60f583f31767f953c196a8d9d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=5527aeb806b5f504f131910c30b6f7a03f97eeb6bdfc6d6869cc88f711a31d08&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=455c98ac0accf9cdfb6376bad7f36499b6e8240546191bb8927498af3bba386d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=a72d4a4c637c3a294c7685d9efeeb7e9a98e75ce3452444d50ac279c8c140215&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWY5MSN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDHa8BdHLBapiDrbsRIiXjW%2Bwx4K5145S5khNR9p1oD8AIgeXKbD4ivOkp1t8w5kI2uVbcqWxuKqm8czViynkVefCQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPHQRNXJ4%2FyAcsxm%2BircA6VpJBg4HYeWVTnKloMz2u80PnL7Ruo3J8gX%2B6DuRR%2BPC%2B3PM0dkhiDr8MDKLK4rx%2BWU8cDun9V%2Bkn%2FodHNvGEGYRyLPtXk%2BCl7tVO1fLLFHKMg2qYuzxXnf%2F3MyfuoxJaLU%2FDqEulhzQnVX0w6FEEdubQZ7vYxuwBkfInfOxkfRFhfV%2BPI7LwsVk4Vgfj2AsQnLfsSx2cGSWBpXIHyCJ82xrMfOzfrKwpGrVCc0MkwZT1q2QwTaMDl0lPUMyMnON5q22u84fAnD4fypAhnCe%2BRU7sVVS9BEKMfoBEJ1Ul43kLQWwaUtd%2BsDpEVtH97zU%2FtVFOgXpKJjmauzeWJQ8wWGCYWaG%2BF81m4Xg%2BJXOmQLtQfeHwmafn31QUTwqLjBV%2FDqDPn%2F7jj1p2AdGaF8EgMYnznBdCYdQ4WGGKzdhO0AFvYQfU41NzYSialn3X3eGAJoaV1X1U%2BzDb3JeVDWCU5Rjq09mSezmGQafPH9OzCpPLnT8a8y7p0W0s8cI8aR9Q8W7pJOjAkoG%2FgtcANa5LrvpossAi2reE8rLjiyDhlg%2B%2Bqqiq84VvvcaG4BWZacThI7xj7uQvMKch3F2FjZNfjJOzJclaH6S8zT0bnoIiVQzJk2DZgIR7O1FhNYMLCdjr0GOqUBl9BPRZscIh3B6V61mvkW8kiG502XDD%2BslWUt9NRq9CZn6h5Oxip2x5OWSt1N94GhOM9Zv0zq9E9zxuGeeJApHCl%2B6OASYCtHVl%2FjAl27gIe3jRaxF%2FfwPJoukJhFUbsxSPoFUanPk9HiKwmARA58RFzOrDD8K5qiaE3qnhlPnZmxcznr6RRzgsB3zzB1vN86hbh1bkJFNIeqUoztL7EWsVaLPOoQ&X-Amz-Signature=6f64049e1c947d16376438cbefb73551302b7b60d79c45153e668c7441d97db4&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTHGQD5R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDmwNGEdisijKcpmCUP591mPk7Lysm2Bo3shN1DBGXjQAIgBY7Htp86yZcURqbwEJOqk2luYzn6Bzskehi64hNboNQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFIsgpFJL9tpRxOItCrcAw%2BxC%2B4Cm61UixVrgTUQz4K9dxUgYUyeSh0gKLFhwpxWW7VHN0qfvmLGJaJbIHftFjmaaS75x9TSP1ZiSlL8bL%2FIbGnHgVpWCFqzV2iMhfBuCSFwPpDdfnvk9VfXy%2FPGuS0B0FxqqZCq8kZc7Qj%2BlYx1n34Qqc%2B9VdFuj3iLybZTlLX%2FdzRoT1FhzqA2Hp4Ab8Gy1VCPF27ZZm266R1qkyHT9SL92BEn%2F%2BN6mqTXA5Kr%2BbFE1Fl7mO4aB6jaiMkySagU7FK1ki0eBX1s2K7yH8h5ucmJJRJbQ2il05GAkXq%2BpEuIY%2FPQeoPzOWiHfVjU8b08WYC8H42n1RwdFmbKX%2B2m1lScwkb6meEEBRg8yW8MxR7EmbEatjBbzn9CGEvl86EwOVikhE%2FhJLYqMv1L7lw%2FPrIIGNLuqDxG%2FGkK%2FyzN7UmkXcqQpTNaGCpKh7cW1B3QrUc9XSRFo73ypAZuff3UvvDwcIHU0ielR63jDn48flG14T4ljnwwJlBp2m%2BIVLxDhnQRhLyQrRozX%2BpGXFBQ916KT3srbh3B5WSBApaRGvAmocijtaN23cV3DD3XQgDWYjIx4kJ5hfj%2B89sbjIx8DJAECkfzmYlX8SZIvoNsLqs%2FnMEJ54G96rDtMOKdjr0GOqUBjH%2Fbczv%2Bd9PiHsVRxPVIwop8EmusKRp8JcNGBwcI1dFQmmw3s4XT9QUlk5iu06LI1D%2Bl1029k9osFPqpIOxSzeQgV36UCxE0f75F3ybLe9EAZ3yjD%2F29%2Fyt6k2fLaK%2BuIKDOQkzFgwcPAGndPLSvt5sbvIIVLwHzf4ALu8I1aSh9OlybkqZrzH5UMvWLL18m5iIc9VaifGEyzNr0TqsbQROQFSp%2B&X-Amz-Signature=be32a957eade0b37e495358eefe9743c607c384d329b9e58b53df930f51e0871&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTHGQD5R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDmwNGEdisijKcpmCUP591mPk7Lysm2Bo3shN1DBGXjQAIgBY7Htp86yZcURqbwEJOqk2luYzn6Bzskehi64hNboNQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFIsgpFJL9tpRxOItCrcAw%2BxC%2B4Cm61UixVrgTUQz4K9dxUgYUyeSh0gKLFhwpxWW7VHN0qfvmLGJaJbIHftFjmaaS75x9TSP1ZiSlL8bL%2FIbGnHgVpWCFqzV2iMhfBuCSFwPpDdfnvk9VfXy%2FPGuS0B0FxqqZCq8kZc7Qj%2BlYx1n34Qqc%2B9VdFuj3iLybZTlLX%2FdzRoT1FhzqA2Hp4Ab8Gy1VCPF27ZZm266R1qkyHT9SL92BEn%2F%2BN6mqTXA5Kr%2BbFE1Fl7mO4aB6jaiMkySagU7FK1ki0eBX1s2K7yH8h5ucmJJRJbQ2il05GAkXq%2BpEuIY%2FPQeoPzOWiHfVjU8b08WYC8H42n1RwdFmbKX%2B2m1lScwkb6meEEBRg8yW8MxR7EmbEatjBbzn9CGEvl86EwOVikhE%2FhJLYqMv1L7lw%2FPrIIGNLuqDxG%2FGkK%2FyzN7UmkXcqQpTNaGCpKh7cW1B3QrUc9XSRFo73ypAZuff3UvvDwcIHU0ielR63jDn48flG14T4ljnwwJlBp2m%2BIVLxDhnQRhLyQrRozX%2BpGXFBQ916KT3srbh3B5WSBApaRGvAmocijtaN23cV3DD3XQgDWYjIx4kJ5hfj%2B89sbjIx8DJAECkfzmYlX8SZIvoNsLqs%2FnMEJ54G96rDtMOKdjr0GOqUBjH%2Fbczv%2Bd9PiHsVRxPVIwop8EmusKRp8JcNGBwcI1dFQmmw3s4XT9QUlk5iu06LI1D%2Bl1029k9osFPqpIOxSzeQgV36UCxE0f75F3ybLe9EAZ3yjD%2F29%2Fyt6k2fLaK%2BuIKDOQkzFgwcPAGndPLSvt5sbvIIVLwHzf4ALu8I1aSh9OlybkqZrzH5UMvWLL18m5iIc9VaifGEyzNr0TqsbQROQFSp%2B&X-Amz-Signature=f45750f8bd470943d5f9482d984003c4de475bcde7fbcd605db131e4f5baed62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=8cac94c35c96ff2ec2fffb1584fa3af41ebe24f9d946d694e38ba5b56ec0c50a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634YOLAQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCmiiYEheUwtv7BoRrUz8Z48JpMZOPnEDUSLV3j8nEXlwIhAMcIZDaV%2FPph2RcCBhsBEqB20ljjKYMlzQ7fJc6AjLNQKv8DCEkQABoMNjM3NDIzMTgzODA1IgyH1hxz%2BHsiBmQdkiUq3AOAgxMuRcboONBxRX1VsCATHLgbSEVDl4bORmZyp9bGncR9tLf4eKjsULCghJoZzfirw1OnwFjVYkJRo%2FjavW6n29vh%2BgpTUQjFV17BSAtu%2FSTtuwuTGBbmNTJRy5BUQUKqQI%2FSzrIMVzHE8QG2lSgk5%2BUsI%2FLldspgjcnM0gjW%2FRgvYHwgoFGGpz2MH3YDzQq84KKJZXAfXcfF3kORpB9uysFOFAGZgBP%2B5F3cMiRqRiT9hZ4nPnsqpjzzGHjSNRWIFO2Sr2nYC84Frgl%2B3S7JwBef792dlPNauSTU8dV%2Fil0F2NqitfE8KrZfYnS8wMLldOBeMqDiavSi5bW3zJ2WWV0TAPk5ci03g5AmdqKa8gIYpDnhx%2BuZIuB%2BW8nR7tZcCjdTXwLEuYsWAIsY0NVD7lDeYAEAu4ygQsgs7lEgj7ob1n2tGADcv6WqrjaUtXqEhEi67%2BN30RcizXs%2FBdPCdjYluFC4vW8f9cZV5L5OBzijERPMU6Z48T%2FjA5qYa1W2K62Cln%2BjKM9egtpr4JXidMI4DWxE6WoClh1BPOwT%2BLpwN6M%2Biu4zETcXY2hHeARIzIii5akDdQV3Ai2ehTZPGIzaj6424zu%2FM98zyTLSCFNC77zRNJdycfTRIzDJnY69BjqkAaIj3iHvlifrx8kY1owDWb%2FBmDQ7eqeeTBJ3mTru3bMblOWkv6x9Cbl6kGO%2BFd0zgsLwAxqD%2B2Q42euklOjmZQ1%2BDzE77cEviTkLGwFk8VDTFIDqk9F0uP%2FyKsOtlXbN657FRL6TtxgSpEd4DyrVa97RR7ihR8PUwYJ80ZTWheCNL0mrtmTTFPlh4U63GTDvBXXcxO5Zp3Utoewm8QaEIyXzG7Oq&X-Amz-Signature=90788d60f856b7aa92e02aa5d0df48d803185a41a72dd8a840ecd8ff11fe5d04&X-Amz-SignedHeaders=host&x-id=GetObject)
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