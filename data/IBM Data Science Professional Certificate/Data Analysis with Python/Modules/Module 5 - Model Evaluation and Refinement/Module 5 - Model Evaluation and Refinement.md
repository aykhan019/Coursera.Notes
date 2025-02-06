

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=1c1727c5f1c27bacb0f5b99a5edb9ac59573f674be7414a28412c90d5c5689a8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=111ed9bd10004afaf7a30ee16b772a5af10a9bec4bb5ff970ad06c5c0bd354b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=9b7b8d612bde14a9026b06954399ceb530bb7d865ba4d18081863f067faf58c6&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=d42137378d63819b6e3b880fa1daca36c1f3799999e2c1525408bc4b16cb3e01&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=b9bc485358ccdec938693fee8f661d5bed86f18b2d562eb48d1553d8510fabed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=953b1c755b72c952a196a3e6fa0784212a7803fb701c5f7bc69bb040651cad3c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=5f3b7f78008181be3d14de8c865a637707c92cd644dd431f513fd3923430914f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=e1b0d2e3233593c18a29e4a3e609d65f01a8fb33a0aa5a28d759c8515f7e4f46&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=0f7bce86415fcd2dadea00d51f4ea28ba33384caf796a0eaabe9935704cb8279&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL7ZSPBB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIGxeANO4BVCi6pKXuVfLMUW44M6JDhtv8X5JEV3tgIiyAiEAoWnQ%2Bn4AKbxZexiqGVOqbFm9HJsKtwqA4gphsvKkVDsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJ%2FtOPdeGMhMXuo2WCrcAx%2BXNK5tuUW9fAaDWLJ8faWxKxU5EfSH1sWMymp2wYvYh9%2FGcDwCdXFo31P%2FO7kzh4dUSxrcmiwRTOGDrt%2Bos%2F%2B4dntEQLmprUvla%2B0ABSF8%2BMWxjhhMG3TAxZvvqh%2BZhAgRm%2FYjEDoR5FDG8YGmHmzyiref7Ho%2FbNe%2FiLE3EuC7JHOnIwuGqvqd%2B8pQ9fQ5ZJQ%2FALk6%2Fk%2BKFwH7gii%2FdbQWqbfCQ8h9MLCpuAV67iNS5LIvxMutv8NrrEbqX6B7oAHV8VmN5We7tJbijgVnkXDEC1BZzJHSCo9dlOv9YKLoXfRGuX88ju8O4reE5yGZwUbGKWDCA1eRqXSSwjEN90vLvH%2BX32Mdpu5NAPOotrCLPgQeZ9fFfO05Aty4sxpUa8PxJNFlDozjA933iM1SnnOj6IGpAY6BFjXr%2BU2P3lt%2BmjIG3yz7uDasrlLG0TGa3MfOpay8c2KTF5cS51xmQMY8HMLUOy1firhCNTW8iJkJP4llOaAzXcIm8YWBgcsEym%2BWMZt1s6lD1E99yLq%2Bp9bFKCL3oP1Dqe9FQmaq5g5A1W9LU3MgErtd7uLRP3tbB0qS%2F%2B3iqgpMRXNw6l3GgOsYRQ9ziouGYDJge%2BaVDuA0moBchn%2BlZIVvrrzoMOrDkr0GOqUBXsqzJ22u3Abf0yN7vHMxcw%2BxwTMPvoj4JmWKUjBRb%2FjUIFXTY5UKsWrDPErGo8ss4drD7%2FeBhMeWGD5RoCl45odz%2BqD2WrtjK4XBTP7mb%2FJeqSayf7JWp4vc6OZ8FStAU0%2Bvs29JDCT5DPSDsZvBnBDOm5tJ%2F%2BP%2FW2X7hGSgstGwxRbGYkz4v1zaV1hYWMwtKFs5C7aIvyVNhwdWxKuIjIELDCKO&X-Amz-Signature=7b841e669168ca2491ff6c5be96da20c5ae3e1e864bc6482cf318a785ffba694&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL7ZSPBB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIGxeANO4BVCi6pKXuVfLMUW44M6JDhtv8X5JEV3tgIiyAiEAoWnQ%2Bn4AKbxZexiqGVOqbFm9HJsKtwqA4gphsvKkVDsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJ%2FtOPdeGMhMXuo2WCrcAx%2BXNK5tuUW9fAaDWLJ8faWxKxU5EfSH1sWMymp2wYvYh9%2FGcDwCdXFo31P%2FO7kzh4dUSxrcmiwRTOGDrt%2Bos%2F%2B4dntEQLmprUvla%2B0ABSF8%2BMWxjhhMG3TAxZvvqh%2BZhAgRm%2FYjEDoR5FDG8YGmHmzyiref7Ho%2FbNe%2FiLE3EuC7JHOnIwuGqvqd%2B8pQ9fQ5ZJQ%2FALk6%2Fk%2BKFwH7gii%2FdbQWqbfCQ8h9MLCpuAV67iNS5LIvxMutv8NrrEbqX6B7oAHV8VmN5We7tJbijgVnkXDEC1BZzJHSCo9dlOv9YKLoXfRGuX88ju8O4reE5yGZwUbGKWDCA1eRqXSSwjEN90vLvH%2BX32Mdpu5NAPOotrCLPgQeZ9fFfO05Aty4sxpUa8PxJNFlDozjA933iM1SnnOj6IGpAY6BFjXr%2BU2P3lt%2BmjIG3yz7uDasrlLG0TGa3MfOpay8c2KTF5cS51xmQMY8HMLUOy1firhCNTW8iJkJP4llOaAzXcIm8YWBgcsEym%2BWMZt1s6lD1E99yLq%2Bp9bFKCL3oP1Dqe9FQmaq5g5A1W9LU3MgErtd7uLRP3tbB0qS%2F%2B3iqgpMRXNw6l3GgOsYRQ9ziouGYDJge%2BaVDuA0moBchn%2BlZIVvrrzoMOrDkr0GOqUBXsqzJ22u3Abf0yN7vHMxcw%2BxwTMPvoj4JmWKUjBRb%2FjUIFXTY5UKsWrDPErGo8ss4drD7%2FeBhMeWGD5RoCl45odz%2BqD2WrtjK4XBTP7mb%2FJeqSayf7JWp4vc6OZ8FStAU0%2Bvs29JDCT5DPSDsZvBnBDOm5tJ%2F%2BP%2FW2X7hGSgstGwxRbGYkz4v1zaV1hYWMwtKFs5C7aIvyVNhwdWxKuIjIELDCKO&X-Amz-Signature=1b526e007a9c7b51c3289a28011ec62f143827571a8ce62ab9cd6c1878683bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL7ZSPBB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIGxeANO4BVCi6pKXuVfLMUW44M6JDhtv8X5JEV3tgIiyAiEAoWnQ%2Bn4AKbxZexiqGVOqbFm9HJsKtwqA4gphsvKkVDsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJ%2FtOPdeGMhMXuo2WCrcAx%2BXNK5tuUW9fAaDWLJ8faWxKxU5EfSH1sWMymp2wYvYh9%2FGcDwCdXFo31P%2FO7kzh4dUSxrcmiwRTOGDrt%2Bos%2F%2B4dntEQLmprUvla%2B0ABSF8%2BMWxjhhMG3TAxZvvqh%2BZhAgRm%2FYjEDoR5FDG8YGmHmzyiref7Ho%2FbNe%2FiLE3EuC7JHOnIwuGqvqd%2B8pQ9fQ5ZJQ%2FALk6%2Fk%2BKFwH7gii%2FdbQWqbfCQ8h9MLCpuAV67iNS5LIvxMutv8NrrEbqX6B7oAHV8VmN5We7tJbijgVnkXDEC1BZzJHSCo9dlOv9YKLoXfRGuX88ju8O4reE5yGZwUbGKWDCA1eRqXSSwjEN90vLvH%2BX32Mdpu5NAPOotrCLPgQeZ9fFfO05Aty4sxpUa8PxJNFlDozjA933iM1SnnOj6IGpAY6BFjXr%2BU2P3lt%2BmjIG3yz7uDasrlLG0TGa3MfOpay8c2KTF5cS51xmQMY8HMLUOy1firhCNTW8iJkJP4llOaAzXcIm8YWBgcsEym%2BWMZt1s6lD1E99yLq%2Bp9bFKCL3oP1Dqe9FQmaq5g5A1W9LU3MgErtd7uLRP3tbB0qS%2F%2B3iqgpMRXNw6l3GgOsYRQ9ziouGYDJge%2BaVDuA0moBchn%2BlZIVvrrzoMOrDkr0GOqUBXsqzJ22u3Abf0yN7vHMxcw%2BxwTMPvoj4JmWKUjBRb%2FjUIFXTY5UKsWrDPErGo8ss4drD7%2FeBhMeWGD5RoCl45odz%2BqD2WrtjK4XBTP7mb%2FJeqSayf7JWp4vc6OZ8FStAU0%2Bvs29JDCT5DPSDsZvBnBDOm5tJ%2F%2BP%2FW2X7hGSgstGwxRbGYkz4v1zaV1hYWMwtKFs5C7aIvyVNhwdWxKuIjIELDCKO&X-Amz-Signature=446c8fa3d9b778763e566a278c3b926eb5352967632f53ac38557c2c96cd648e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=b4754501fe941d8851cb3522bdda65824317f157c6c04a69dde1d73699f3a690&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=7dd23d84e4b0c3a1826d1df994b66e90d93b12c7cd150fe4739dad288a7aa045&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=e4dc271b1a92bf2f0be0db4971eff51875cd059e6eb66e995f1812ad18af31f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=e3161bc90dfd6aad0c1ec1123713cf8f2d33dd54b0272d91bd2e8ac84dc5445c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=8ac4bce0582e27f291ef7a97dd940245eac069cb1da7375570c20860968dc5e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=f21077f4751991fdfb1f6d22f1512d33a669716d09aa2aba505f23ad0025018e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D56T7NT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIAuYpOfFSR88oO6S6mPRAS4RydRJXgJ0r1cgEnBe7T1mAiEAheZYVRYsk%2B50Uu%2FJ1V05pXRUQEWLxngYJ2R%2B8ce53doq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBtlCz5SWT%2FR19zWbSrcA2bs%2BzA1RwyNg3xDCR3cXlB%2BCHj6yGVx1K4k%2FV1cANlnwZbwI8BjtkpXZ7KZWRr4Fv%2BDR%2FYr01JwKE02WRoqVUompw2mxsZervZl41aXJPtZpiPWUm99%2BGCbwt6cM6uqXg7%2FjmM72zCajkJyhcsvgjKrXjGe%2BujOCTtQ7G1nuqX7XK6BPWLUhOUv78IzGUMJpH0gJF1q323Fij89lDbWe%2BBEsz9lHVOBQduG6cxwJBGq1FA%2FHMQYT263ybQ9cdVnw9XYd8XujpUUaBOOUVscpxm90g7863ZCNposTt2TxLLTtxKcarANc8sIqHOCF8ToZ9K1eAMz5m3BbRmxtwiK%2BfHBJoW2HSRob7yUXjb7UtaoE7S4J%2Bxdf3%2BzK%2BQJcnzscrDvSyAjZAg0SLTaLRhyCSW25iIEfM7cVcWeh44YCq19EhO3dGzQhAgZIMXfbpZs0OEIk%2F%2B1i396%2BzQhfL8AOsIeWpwYO3XW83AastEyaQGIaRQ3X8%2FShLJwopl%2BByQpLmj9RqPS%2FIEO7gXtiroTmmLaXokDNgiyqjYDomD%2B62iVLqbA%2BdRjUNfBltiXmon8xlsh%2FrDkzy74htRGbBzgap7JK1u5R24b4fmgIAVtHvBhaXS2Q3uFzlwKLt2pMI3Ekr0GOqUBIoeaG00mp93zf8JTXmdkFKcgV5QWdxIW%2BBeOSDYc7HsDEq7MMv1Ac%2B883SZAcvqf5J3nFoHCyaUJQ0Z%2FrNqMgvCGpz75%2Fen64jHMg95pzLAZW2fMb4oYrmxrmX21JRVRUnefcS0bdyqOboin%2BI%2B%2FgZjGdmgKgsaV9uWfYlNOesavttsriufQ5xCDbC2Ey3kI2NFX2aH2WVzsO5CleXy3F5OmUqFW&X-Amz-Signature=ca377360082267fe80025798109d0a35562d809edbb1727806b31e214e4caa1e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D56T7NT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIAuYpOfFSR88oO6S6mPRAS4RydRJXgJ0r1cgEnBe7T1mAiEAheZYVRYsk%2B50Uu%2FJ1V05pXRUQEWLxngYJ2R%2B8ce53doq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBtlCz5SWT%2FR19zWbSrcA2bs%2BzA1RwyNg3xDCR3cXlB%2BCHj6yGVx1K4k%2FV1cANlnwZbwI8BjtkpXZ7KZWRr4Fv%2BDR%2FYr01JwKE02WRoqVUompw2mxsZervZl41aXJPtZpiPWUm99%2BGCbwt6cM6uqXg7%2FjmM72zCajkJyhcsvgjKrXjGe%2BujOCTtQ7G1nuqX7XK6BPWLUhOUv78IzGUMJpH0gJF1q323Fij89lDbWe%2BBEsz9lHVOBQduG6cxwJBGq1FA%2FHMQYT263ybQ9cdVnw9XYd8XujpUUaBOOUVscpxm90g7863ZCNposTt2TxLLTtxKcarANc8sIqHOCF8ToZ9K1eAMz5m3BbRmxtwiK%2BfHBJoW2HSRob7yUXjb7UtaoE7S4J%2Bxdf3%2BzK%2BQJcnzscrDvSyAjZAg0SLTaLRhyCSW25iIEfM7cVcWeh44YCq19EhO3dGzQhAgZIMXfbpZs0OEIk%2F%2B1i396%2BzQhfL8AOsIeWpwYO3XW83AastEyaQGIaRQ3X8%2FShLJwopl%2BByQpLmj9RqPS%2FIEO7gXtiroTmmLaXokDNgiyqjYDomD%2B62iVLqbA%2BdRjUNfBltiXmon8xlsh%2FrDkzy74htRGbBzgap7JK1u5R24b4fmgIAVtHvBhaXS2Q3uFzlwKLt2pMI3Ekr0GOqUBIoeaG00mp93zf8JTXmdkFKcgV5QWdxIW%2BBeOSDYc7HsDEq7MMv1Ac%2B883SZAcvqf5J3nFoHCyaUJQ0Z%2FrNqMgvCGpz75%2Fen64jHMg95pzLAZW2fMb4oYrmxrmX21JRVRUnefcS0bdyqOboin%2BI%2B%2FgZjGdmgKgsaV9uWfYlNOesavttsriufQ5xCDbC2Ey3kI2NFX2aH2WVzsO5CleXy3F5OmUqFW&X-Amz-Signature=3fa828d604d75ec9e40984c6596722eb0a0295d783138ffb327055a3ae2add60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEUI5VT4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQD1ly0eVVMuJ1H270BtGxe6CS06eD2XcDdVAHWpvIOfaQIgf8sLbfI5dWpS1uqnnQBqi%2B5Q8i8%2BAZYoyMNNIHEsK6Yq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDEfPbhdmUE4AVYJaFircAxlfjvIQ6pppKWXVng5sfB9VNrN4IU0khDioXfoZ0yibL5qbxqehu%2B9wKCl2iv0b4OISH3nOgEGX6K5IamSxExJ6Fr04bp7UUjo%2BJEchJ9dqoiQfi8QHNRvQrLxX4yuRHR0nJYDays1A%2Fjs3fe3C9HuNqGPEu2eeEBeyJQrHKyUI7JjRQ7F0%2F%2F5T1NjimarrItIzwQ5%2BZb%2BCv1QFZR8PFawlMwvkcTERzIiq5g7OcuDRK9l8LlYasgRRwakXi6QX9D6ydcSImKjL2k9g9GapQJDxVCQnoR2OaRNpAi%2BwhAiidNbpJyzS5Qi0LcuLlvaHO8C6PZYV5W2JL8Qv9AYwwJ%2Fiwdtu3nY12MVOTHkJIpFrW%2BfgeNvNExZVnwXuypWVwgpPv7zOA4YsDZYhR8fv78LYlmUNVlFOSACGgH%2BtQ9SV3I%2F1xcA5h2rfC%2BX8Kb61IWkCs9QAmiVvjCs3%2FykQWHpikND4JlK68NHd1E%2Bm7Oh85oMSo7nrUvy9CuL5by4gyUxTHAGdb356%2FTE%2FmR6E%2BjtMuk%2FNvavsGRg9bVJG3Brp%2FjNTxzjekjzsQVpMGuBZ7jGpuZsczNQfe%2FCaavjj%2BCc4P7HCHtvIXHsf7gpl%2Bxg0df8e13tYtVVHM%2FhxMPnDkr0GOqUBlOez9JAtbvvTG5Ba%2BrAWDKAIRWxY8edrvKSHDdI3qemr%2F1x1BLG1%2BbiKF0bS9IYoKlcxDLx4g%2B5KbENGEdN6PG9w1AXgR3bnZAUx8CDIoefBn%2BsQAjDiDnnw2izRYrORKJ09n4MHy7blorjHqifPCkmHWUQdDctk7A1ykCCf0AxFzLecUB%2FwR52FtiGd79%2F8Kv8j%2BmaDLiahfN1sIRP1zmxsyTLy&X-Amz-Signature=5180a3845be2bbb4251e60c7b7f48fd87ea8690782a4204decae4e57b2c8c929&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QY6H3RX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCZbAlJsz7%2B%2Fj9L5E6bQA1fvBvmIPLhc1d3dbUkb%2BiS9QIgODh67QGVI4Jmg1lBIOkZMwmmvQHb1kbUC3Ijtamkr6Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOhNgJ68CtgfibSolyrcAzQZru4DgNNfvh7Wa%2BxxfzsbTNJMqA6xA2X8yBf9Zfm8zOrEm9z%2BMPJqlulVuKpEnQBoZY8kygv1wQGymqCdZxwL1ziwu2qxV6S4vRGeaTR%2FwctIWsCQZEpCScyEc83PzPVC7zIa%2BFkTFL2MRcHyg9fvlBo7nfddV6%2BrlBlcXKqbNb6e561n%2FeJGANPIJNMFAUTD5deEgmBhaivQACLAabKfUzEmdEDv2AmHXXoR638kyASPyAG6bcvXTA333lUQ4chBK9vRlr2AtpYbN5Sq7OI8CyJfKce9tyuc0TGPchfiTlWJjlOEC0oG8sY01KmnFjGb06nA2tDPvVlGqXfQDXXpQao2YzrGOK0QD%2FNLxeyy2RUy5TjKXBvOipSnekP621qwngYD3bUJiQnzIRB%2B4C2gKsj1tjIgIAu1rEBckVMQ%2Fd4tMzVQ%2FcLfXiUdYxCU30TXuptzqe9jEeE2bmzkFuoG%2BNwZihLSuW0rquGrREgAlkDBOF47TE18Z70ah0vfiHB6FH1ogW%2FqRG%2B3GVT1NW4Ij9g6RvK5JBCQD2bt7EWB26svlB09BFic1mGczgKMv86k2kLbOjG9psc2V8ZFMSLb%2FQnc4fiobxRsi0C3hM7i9WGfxT43LIym%2B0IOMJHEkr0GOqUBtd3NjK7OdkILyqiEVmrb7DX3a%2FyJQ07QRgaJ%2FLkvAW07UXNWYC%2FEKQN5k%2BpaVoyDETzfWnXM6l6gTDhNBga0RMMP08c%2FVESfM%2BKkEIaSTuh1s%2FQ3JLu7ypv49%2F77oFE9jVRcuZfh%2BBLid53l7re6iGueA6Yp1i28SIuYO9azhSZVpmNzlWvnZObKMnE3Hh5tsux%2BcKYWMewBetfd4PQ9fy1626Bw&X-Amz-Signature=109b0b372a2b1fbdb3e157f1d0c66d8b1e8e8686095bf9de585707dd2530d243&X-Amz-SignedHeaders=host&x-id=GetObject)
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