

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=69a66c527c7e2249f95717008a6c75c27926b879d43589045fb306d7129767fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=9fcc117e2db90623a21153cacff0025e45aed635c26fe60e0737f92bc37c799b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=3a175e936a573a50c9b86827ede9e305a3748c47edf021bfefc101af9b58385f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=0469cad5d4e68a5e6a7deb9c1fdf34e4757954789ba73ec48169a9448c95e18a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=1a09234e94fffbe609f6907eac11d730f0facfd39787cbbe7da9614b9e1ac5c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=d74c66b552b016ddaa029fb446146080ae9cac4e84a01468baf787602c6451c9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=ae992fea69b1a1d64014e03a66d29f40251ed0fd945de9f48f3c43551a73d9dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=303f743b09001defdfa523ac1e3f4fbb8d64f8135665ca76f5d94bc5110224ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=f3a1dea01f9ca847c0ac80255e98d5ba381958e4f5ea57611d627f212e34b918&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHZ2Z4K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgXmoAuIOzgivl5L60ldrgWsNaMd%2Bq20VB9ho9WggfpQIgYxQx0M0777pf39646OmWzLoS%2B%2FtqVwAiAeZAlQkQoxwqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCwSE%2BM07gTqwjue5yrcA3xxxfmhh9WprQwq%2BOcO4CNPJ20GblQy20%2FU1iUdJ20f1Vu4oh4CGAxgNs%2B9CRI65WUJ6r%2B4LwzXypAcXN6JnF5H6l36rnt6qRUhvNbtiYYtUqEZkucoo1EF0%2FZUawOKfOUVV7Vnq%2BViNZMIpRtYSjr7kc0C9j1BT%2BklbveG8URoP2GkTjbhH2GXrBcFQEs4ExzyusET%2Fx%2BOO%2BLHrXh72T5iD%2FdgUUZdcXtxV4sin%2F7WEEOsVfZeH2HyYr%2B93%2BPKuqAkZC0olBugyVxwK8zsrcM5OcnONO7GJT7rDyHv00hhwVBMcQT77VJLK1s8yGaQNxnY42Vai44piaZbV7fLNrVY8ceDcujQIHYqlHZNXsvGz%2F7JUgUDMxS7JfxGdGfl4%2FNQiC6E9G0GBkCxjPYAOJtLdP%2BZWD%2Bi4c%2BgSui%2BfKyBI8R6Ygcgs2fxEPo9%2FSchl9C%2FRDgJR46QqhltmoyAGvZE5IF5YAO%2FZRSSiw7T3eW9XlBoY8ofKXwJYJTKmRJsM9G2tItLWsGYSMzxiOWXKdfDJmOCI8flJathFxLwpOmiqlI7NPZmUP2oxGHUfW7yAvSKwW74o273iMgq8LVGdC0nO8dxbkj%2BnvQxEj6h7Diej5F9VxxuhCjL2DkVMMTL6LwGOqUBDb1IkaLEvjfPTUF231sa5UUGFeguY40H%2BmYpel6E7n1JZ%2FFpj8xXmbxNWmdA9OAbymvzNj4ldDH7WnfJQ5IzAr977Szc3GZvE2JKGThx1VgQZ0S0ZMUDJDSQQDBghaghSZ3NIp2mIo9NN1v9R%2FXFjMQ6OOg%2FrUwIIrG4Pv7ml%2B0VScWjAbuZfIFlQ5Mt%2FOdlDYnIlbdwJ0z2pFsQurzZpgvKdzFV&X-Amz-Signature=85517fa23c7e1de93e591995e83f864512536ae0869da952b0b4191654aad101&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHZ2Z4K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgXmoAuIOzgivl5L60ldrgWsNaMd%2Bq20VB9ho9WggfpQIgYxQx0M0777pf39646OmWzLoS%2B%2FtqVwAiAeZAlQkQoxwqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCwSE%2BM07gTqwjue5yrcA3xxxfmhh9WprQwq%2BOcO4CNPJ20GblQy20%2FU1iUdJ20f1Vu4oh4CGAxgNs%2B9CRI65WUJ6r%2B4LwzXypAcXN6JnF5H6l36rnt6qRUhvNbtiYYtUqEZkucoo1EF0%2FZUawOKfOUVV7Vnq%2BViNZMIpRtYSjr7kc0C9j1BT%2BklbveG8URoP2GkTjbhH2GXrBcFQEs4ExzyusET%2Fx%2BOO%2BLHrXh72T5iD%2FdgUUZdcXtxV4sin%2F7WEEOsVfZeH2HyYr%2B93%2BPKuqAkZC0olBugyVxwK8zsrcM5OcnONO7GJT7rDyHv00hhwVBMcQT77VJLK1s8yGaQNxnY42Vai44piaZbV7fLNrVY8ceDcujQIHYqlHZNXsvGz%2F7JUgUDMxS7JfxGdGfl4%2FNQiC6E9G0GBkCxjPYAOJtLdP%2BZWD%2Bi4c%2BgSui%2BfKyBI8R6Ygcgs2fxEPo9%2FSchl9C%2FRDgJR46QqhltmoyAGvZE5IF5YAO%2FZRSSiw7T3eW9XlBoY8ofKXwJYJTKmRJsM9G2tItLWsGYSMzxiOWXKdfDJmOCI8flJathFxLwpOmiqlI7NPZmUP2oxGHUfW7yAvSKwW74o273iMgq8LVGdC0nO8dxbkj%2BnvQxEj6h7Diej5F9VxxuhCjL2DkVMMTL6LwGOqUBDb1IkaLEvjfPTUF231sa5UUGFeguY40H%2BmYpel6E7n1JZ%2FFpj8xXmbxNWmdA9OAbymvzNj4ldDH7WnfJQ5IzAr977Szc3GZvE2JKGThx1VgQZ0S0ZMUDJDSQQDBghaghSZ3NIp2mIo9NN1v9R%2FXFjMQ6OOg%2FrUwIIrG4Pv7ml%2B0VScWjAbuZfIFlQ5Mt%2FOdlDYnIlbdwJ0z2pFsQurzZpgvKdzFV&X-Amz-Signature=827e69620a31dc656c87db1b414c6ebc8ccedbd1ffb56c6e4968f0c2b2439adc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHZ2Z4K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgXmoAuIOzgivl5L60ldrgWsNaMd%2Bq20VB9ho9WggfpQIgYxQx0M0777pf39646OmWzLoS%2B%2FtqVwAiAeZAlQkQoxwqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCwSE%2BM07gTqwjue5yrcA3xxxfmhh9WprQwq%2BOcO4CNPJ20GblQy20%2FU1iUdJ20f1Vu4oh4CGAxgNs%2B9CRI65WUJ6r%2B4LwzXypAcXN6JnF5H6l36rnt6qRUhvNbtiYYtUqEZkucoo1EF0%2FZUawOKfOUVV7Vnq%2BViNZMIpRtYSjr7kc0C9j1BT%2BklbveG8URoP2GkTjbhH2GXrBcFQEs4ExzyusET%2Fx%2BOO%2BLHrXh72T5iD%2FdgUUZdcXtxV4sin%2F7WEEOsVfZeH2HyYr%2B93%2BPKuqAkZC0olBugyVxwK8zsrcM5OcnONO7GJT7rDyHv00hhwVBMcQT77VJLK1s8yGaQNxnY42Vai44piaZbV7fLNrVY8ceDcujQIHYqlHZNXsvGz%2F7JUgUDMxS7JfxGdGfl4%2FNQiC6E9G0GBkCxjPYAOJtLdP%2BZWD%2Bi4c%2BgSui%2BfKyBI8R6Ygcgs2fxEPo9%2FSchl9C%2FRDgJR46QqhltmoyAGvZE5IF5YAO%2FZRSSiw7T3eW9XlBoY8ofKXwJYJTKmRJsM9G2tItLWsGYSMzxiOWXKdfDJmOCI8flJathFxLwpOmiqlI7NPZmUP2oxGHUfW7yAvSKwW74o273iMgq8LVGdC0nO8dxbkj%2BnvQxEj6h7Diej5F9VxxuhCjL2DkVMMTL6LwGOqUBDb1IkaLEvjfPTUF231sa5UUGFeguY40H%2BmYpel6E7n1JZ%2FFpj8xXmbxNWmdA9OAbymvzNj4ldDH7WnfJQ5IzAr977Szc3GZvE2JKGThx1VgQZ0S0ZMUDJDSQQDBghaghSZ3NIp2mIo9NN1v9R%2FXFjMQ6OOg%2FrUwIIrG4Pv7ml%2B0VScWjAbuZfIFlQ5Mt%2FOdlDYnIlbdwJ0z2pFsQurzZpgvKdzFV&X-Amz-Signature=6b05f67a1d6f2420967f5677b4454573b7a277bd7f799390c0c11e05881cb1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=08ede51db074d6107d6d442d005ae9fbd4c9eb24f18d71f5471680a2be1b45c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=138cb58fbaf8250c3051f7636ea3fe9ce63ec358e770df8d7292416f7b70980e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=d6015f9787686fc65483f6959c4baf83e9ffc52a2a8285493ac10f00e6c95f5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=0970d09fc15daa46cf39ca8b839ae845f20c4a5c3159d1e3684862e02ca94e5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=93456d55225336f53dce4e7966096146c64cbe45f409be4b9578f170d9a24766&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GULGIB2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCR4Sco18iVgwGtoZc9LwZ3KD07M59oJDCU2%2Fp%2FSwY%2BTQIgZacgCVvr%2BW6i5saVm5CiDHMiNOTbGEtvmx6A7dkQF6gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAeG34So3UBjNyDifCrcA8smmAOxsLGtiSPCwx4HOZxF5vWlMxlrdkjoXMVG4w2Xi8uIWnh2d3czQykoUGYegRi91kPj0iy3NjMPsPRQb%2BCUrv5ExAw9vkl8JXXhalOqGKA%2BXFnjDorWZQDeyzwud7Lmc2K5l3as2kew%2FSGaFNR4QqqnKht63gORQKKqWbvpCc4JIhiGMYaDnAt3%2BCz4S2lg7%2BeozvRPSW7LSmBK7xicNH18CikxBWqmEYEH%2FlPHqVwmP6UTwPrN%2ByqGTb9pUdRygtJi%2Fa7aAK%2B0vKljP2rwz4IZjpLEuqyUwEKsvrjx4OnXnmHuW8nfYVLxPAGVzm8Ls5qUallYmjWCAU1zlMTsrq6VA7VrQvLoDohQsmnm0k1zHOA8XPX%2BN0eS0j%2FjK2Yi9nQ64pqS%2FG76OhZ0BZRNXBNGplZomK1Qa48cilXXqq%2FlBfEulLe83KNcCGdkUamS7UL%2FlHLtGJ9S9cmITNV7%2B5Zr279NkmbEopCcGFpI5H%2FxwJ8CAnyQGtLCj8v7HDDVuSpa%2F1CtUqTbxhG4SIqw5YauG6FqQHqY2VYDRJ8n8wzT%2BYxOaKoATN0azO5R2ZNtq51BPeQj66KtgZ9Ut%2BCRBDKyV0nO4dGcfnHUVpfEC9bFlYQrKb741D2JMM%2FL6LwGOqUBdLVAMvD7jh5IdOr5M8urBLzHw1%2FILEp3vZdPh26pCe01%2FqK1hV1wlKo6ktB53JN5ZoDZ%2BwQwCjCaRqti1CwWQ68bGP5ZkCg2xEa9rTlp9z9JujoWjoqZcnIkd3z4j5wsdZ3303HpkWyVQGw5PZFDaZarXb4KttlIvWdqwemsKmpWzZZ%2BsYQ3u4meLM09QCoOyEo92ZVag5E1Agw4BlOtNi9H2H4i&X-Amz-Signature=f0b6add5f6cee23f41071e64b938f50952ce9892fa81d971d2c1e4031ef7fe64&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KDPBM3S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVt%2Fv5iIPSf1R0DzNlluvlsVjl6wTlngXGy4ecIHBYwAIgQITsdpyiwSmOVS%2Ftl6cg0p0BMZ3L2jHtUYiiukGUcXUqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO9aZpmQo2HQRnGhBSrcA08Xkyp88QKzY3cYndOin56hMWANBX9CRWkzf%2FKZXQyddbKLeo9TFjhhUan%2BYbvIfPUoRWYC7EUPMmJrom1dQVy8s1TS753KB6mokSSMOMvPFZbt1pOWH1iHdCJ57ScgPZ0p%2BQIXLpvK3tl5q%2FAM2x%2FHd9%2FSfOoUQywYEgUe2S6b%2BqWuz7JXyl34VtMaSUDvIV5on4CPgNRu0Pq9jf6OpuERwfqGhYldCGCmWCqsHGidiFreDs2%2B09MJMsPJQhpTgSwRopx8R0xG3wRRPdnlyzU4U9uMcnZ80X9%2FJl6B%2BsLxTU2mbD1OY5xScFZ99PzjCO3jkMWV%2B9BQ%2FSnztOqhDSpvPSPTjfG%2FbbACNPMszoNnG4q602tYme%2BULpxyvwU3FrHc0VZazw2Zddj3spIa2RoEUq8qvdzbPYoNbC2Fw25PWd6CYX%2Fql0bHW2CPnj9c7KiDbwk%2FmC%2FcOC8o4iwmin%2Bgp%2BuVV8DT%2BipvGUzOoeQutaDMqF80ffH0J68gKmCA2PxFvaQ119je%2BfKT26VfKwOQp6tGTBktFwghKXpNePJlxtqyKDEyAAaw1%2FF3YHUKvkcb%2FXYYrDtQyHizFP%2BhXJizwKBUPRuEYTAExhZjzQYD%2FRyxqPyOkpYaubeEMMPL6LwGOqUBow6EJaOUVuZYbnH%2FZM4mSWV3ISfr3ud0FrSrLfNE3QYkeEqMmszMRp2pWT9n%2BlkFvbfEICnK5USeE4hpkR78hNdtREap6NL%2FrS%2FE3r4efeDUlC3XbpXvjWXRpEXXBBfujROy4f4S0o7kfEq0033sYBOwV9n%2BB0ZSZXhz80Hvo7mFd3RUy8JmOaYWQREMoon0h0dtdcQ%2BF6G0B26ZvmOTcrQY%2FfCg&X-Amz-Signature=81c50a3804cf31e7564256f6e22b503f1d0711322b23003709d7cc9a9f117338&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KDPBM3S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVt%2Fv5iIPSf1R0DzNlluvlsVjl6wTlngXGy4ecIHBYwAIgQITsdpyiwSmOVS%2Ftl6cg0p0BMZ3L2jHtUYiiukGUcXUqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO9aZpmQo2HQRnGhBSrcA08Xkyp88QKzY3cYndOin56hMWANBX9CRWkzf%2FKZXQyddbKLeo9TFjhhUan%2BYbvIfPUoRWYC7EUPMmJrom1dQVy8s1TS753KB6mokSSMOMvPFZbt1pOWH1iHdCJ57ScgPZ0p%2BQIXLpvK3tl5q%2FAM2x%2FHd9%2FSfOoUQywYEgUe2S6b%2BqWuz7JXyl34VtMaSUDvIV5on4CPgNRu0Pq9jf6OpuERwfqGhYldCGCmWCqsHGidiFreDs2%2B09MJMsPJQhpTgSwRopx8R0xG3wRRPdnlyzU4U9uMcnZ80X9%2FJl6B%2BsLxTU2mbD1OY5xScFZ99PzjCO3jkMWV%2B9BQ%2FSnztOqhDSpvPSPTjfG%2FbbACNPMszoNnG4q602tYme%2BULpxyvwU3FrHc0VZazw2Zddj3spIa2RoEUq8qvdzbPYoNbC2Fw25PWd6CYX%2Fql0bHW2CPnj9c7KiDbwk%2FmC%2FcOC8o4iwmin%2Bgp%2BuVV8DT%2BipvGUzOoeQutaDMqF80ffH0J68gKmCA2PxFvaQ119je%2BfKT26VfKwOQp6tGTBktFwghKXpNePJlxtqyKDEyAAaw1%2FF3YHUKvkcb%2FXYYrDtQyHizFP%2BhXJizwKBUPRuEYTAExhZjzQYD%2FRyxqPyOkpYaubeEMMPL6LwGOqUBow6EJaOUVuZYbnH%2FZM4mSWV3ISfr3ud0FrSrLfNE3QYkeEqMmszMRp2pWT9n%2BlkFvbfEICnK5USeE4hpkR78hNdtREap6NL%2FrS%2FE3r4efeDUlC3XbpXvjWXRpEXXBBfujROy4f4S0o7kfEq0033sYBOwV9n%2BB0ZSZXhz80Hvo7mFd3RUy8JmOaYWQREMoon0h0dtdcQ%2BF6G0B26ZvmOTcrQY%2FfCg&X-Amz-Signature=99fba57dc32f653519412ded507c4d4b2b81c090bcd602185e5edb56de251270&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SHR6B6S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDArxUTf5v6mNl3rD%2B4nBv1oBKtlYjvR6xQIyOjHN7WxQIhAOSY%2Bb%2BGMe0dbDOxbvRm%2FPOvB0DIH6d79Pr2TVUkAi1XKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypPOLhcfJtCwj2B4Uq3APzCWf3vAAac3MDgYueuJzx%2FnKaBaMHGPl9avQjsVIQtVCDi%2BkEfMe%2FhokOLP7RL1fTDapDx6kGewR1fYPBoQy3tPevQyzIOGBm5jAG7vo1XTqzXjD9%2BQERSzWoB%2FE3YOLfUR6z2YungXaUUXlxwaBpJuCjcJNxqiwv6qgralDIx1AAErtINnGs76Ef2lVPG9yQ2AFxHIKffc%2BIrURY9d0Q07AJxsUs%2BQcPJEshHYvsNzArEpgvjIOBAhHFpHLuPB%2B7B%2BveBi6IhLf%2FdDLSGeJ8UflUWHYqBiAsIZ4%2FkkxAuXkgenc33a90t%2FT9IC3PAu9SaVUr58byh0920h2dfI7F0qfyyS7t5G2iM53JtTVziohz5GdwNb6cfZ3aXZIqC4I%2FLsPip4sh8AhAhG%2BbjPjuGFgTnx3w3SmBOoxlDUiC6XPU0C8zX%2F%2F3SJFfqDX6Kk7BuG6FoM4rVGuv205uWYodoxxUQBk%2B%2F99WPwtCiS0KO7JBQqWYRrDgP6x5bFCQ2GX5lpms3mkzPcKKN9jhdBCpraXnR09V6muvqSzG0fNUSP3B9pNta%2BNvPu7tLKeCbMw5u9G0q43p%2BzUctYX2aMac6pq92NCKb3GYZzG2VZjPhe9zqGWDvI06OOJQHzDdy%2Bi8BjqkAQI%2FRKu2EDrq5BUfPgGqaBTuM3Z2HtRigB8oVtI42ZXV7aZO2m0TjpfIUo3XWPq663e0CrDgJ6nmLwXslEAPAG%2F%2FbZPU8%2BtLh%2FQCtXmBJlprQQCBUnM%2FQR62GmE0mmNz2kFFbWGj%2Fl56D0DmNgXwwbzQvG2sd%2B8B3K61ywU2sNGn0JQOm%2F%2BJL4GGM5IqVB3cIECq42%2FHd%2BK6Xy82r5h2XJ%2FIKOrS&X-Amz-Signature=0a41da0d0a7a08812ab542516760324811ccf61155b5d0adb64456726fa2e7bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR7HMBY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvScEHfVrxJ5hBSZ3KCSuMABkvlK%2BTdS1pBP%2FpkSylAiEAynepUdrA%2F%2B9ENe3MP2XnHXFKmXlAyFeQmeCV2T32450qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3A6L5y8tT%2FqBhkACrcAwij9K6u2TOAn%2BzKVcqktYh%2Fbtf423B3LLClCs%2BDqTAt07wzf7FmqDrLRYJqtJFr7t2e822SfHqMOcXKM%2BuotUUIxvcnukFrRnxtKjNJFFhDbwMCFVup6mxrxC14w0nqzkWBkj2jPsEyTO7YszPywpsLDvM4Vx1ZiViH8fpe95KHko8ASWauGXbb0kLWlo%2Bt39SRJvGArwHWP9DptiBFIJQQER%2Bbk0yGDIbSkGeQ6UCeejcu4%2F6LzI9xB%2Fr2V0YjmWIXL1svf1BJv5QbfMkB%2BGfqBBl8j9JuWEFtCodCjYHEkQqqxo6dzk8LsIAgja1uMhq4%2FdShBugSE3emjgft5gJiDTwl3tCYgr7sEmSaX8C6kvpQw0EJxdodd0k%2Fxek41Mdbb7d53A4W3A27CMUUNb5VI1yMdB%2B22mJes2J63K6pXbN2epxUW3z2e30Kox9h3CQUBHTCF4eI6jCayPbpwX3z2d2rfrJHuj96jVpnZH7RsEoE%2FLwRUO9YPN6OejhbHgTzcqtd77I1A5NhgecsA6nqSfHGu7b6mPj13echOi4ycIFp2mAvZ39Y6xNJl3UAz8C0ygIHnbrTsNBEF6DbsZPrdQS6pBxjx6QSl6wh5v7fplSMqpkkDZjv1Y8CMLDL6LwGOqUBLSGUWewKdrqLSOQR%2FSZYxgLhOmW4cbg1nJ0zIdad64tp3Dnuh6w%2FB2w5UD6%2FdIU4eVwKg5iP5QLv5t6lPwSAnEJ9Iw3TW4AM59BlD50cbXSOod0EKMd%2BikfOQvp3V3vXIH2o1Al6LQUqNGFo4kHU7%2F5uH2xxBSAo78y2BovaegjnGjzjLKftJFJiCEODlUFauT%2BzX7ynGe5Pus4KBLdgb4InDpAX&X-Amz-Signature=dfa4c4fcfd955fbd7994a9bd9aea99998f582b6bf325af63041022a6b9ace2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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