

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=0fa2dfdddecd06fa54b93e06b27877ec7b95d185325276719f30f40f8b89d631&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=212f30c6c9db5b91920709ea13957cc03bfcd1951d0d59e92bb62d873b1b22a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=d715649e2ba939a6362d6ca4337b87885b2a04b4e79c49387bf32e69f6dab6ca&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=730fb15bf5e2e61b6d8a9325c46c36df4221a2b2737c0abedc93c1e57c4ece8b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=2a39058721cf6457c832da1b0b113b1ba5d3d3c6605bcfb5f59c4aba33878260&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=8e51b9bb77d1a11c199ed5a87c7068d9fd4e0bee3299b5aa6727b7b2014e51c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=4c754cab82f8c28805801a94d07f3ea7368c445f6015a7533dee62330712f83d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=f3ed987427ebb1662dc9091ea1b69fe6a543165937b0f98b044d1e2e113266ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=c3526ac163d5870956ba422fa5b4c0eb1cd4a70b4f619f4260f50ba21012bb0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MPUWVL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDckxiZn33XrEHCRgWLf4yse%2FwqqosOjG0mOmAoNP7SLAiEAjGCQJggdljT%2F62AAFu9wxQdXqSK97JRaVZEiImqJuuIq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBFkj%2FJPbgxxVYdRYSrcA%2FTr5G%2FufePqqfg2%2BQpdpnkbvnrpxqMdMQT2ETvMWvsjW%2BBaYKaZl6gaK00WDa6fCjwJq4caAZlNIq5FKYtoqz7fV8M3Nw6S3ZUpLWVlm2APW0ywn39HE1Y%2FfjskcWsTFns73eONNvr%2FAtDRLDngWKapgf%2Fg8RwLqPLzq0fntxt0ZSl6QZQmKDEVjfdFx9Dr%2Fq5xIRf0%2BA6Bn8zr1spbHyJLDThoC2Xx0X0yPdoNoCXNaVQowXPFuKYOVrSHU0ht2K0BQJKzXiKRPA%2BmGUq1vnOcF2%2Bp%2FV6w1zQXhZzNx17yZuPw2%2BQQBT4dlC9Pnp49oz6MNY7k1%2FC6zg6oR6GX4bTxf7GY0dZ8s06gu7N8I1XEUlgJgJ8nWWiPG3X%2BzMV%2BvfihWaxXhc27FRJa43Fk%2FIPYXDZCwGEiKXrhL3BVQlbZvrkS6xKReejdEjffIIGzXXf35HEhgRggopWzhsdk8f0Air7FjAZyeh2a%2Bg9c1X5UxUL%2F82FOoicuDLXwtpqWsjiQoLlnRDvdFVKqZoalN7E8TJc%2Bm741XJOxxj33omTDFWaZ3iP%2FjkQ%2F%2FP1%2BcFjpwY39BNM7N2iNZ0iBdAg0mAhM8FMbEAfPKcsf1pgRLkCycCqYlF4zRzZadE5WMNSuh70GOqUBI7tMKxvqN9QGNhyUHbGY6uJ%2B8ef1bHpzAUnfDEby1aNs8nbaWe%2BL8ik7jvXwSUoNmS792LsrPb5dH2ADib63xrH%2BIPslVmJK2m9LH9%2FicRz7FHPtjcE4E%2BPasxy2EDBQ8EuC9fBdeEUSAhO1TLpDdW6keFriyeGPE7Q6Ji15kHdbWi5V7cDicmcIktM1z%2FCERnBqCbvqu7AAJ6dkFY9eCr1nvsmK&X-Amz-Signature=54d780612dddd7de08a68ba0ac1a6b95e5e4bd4917ede533a8dafafe79721d75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MPUWVL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDckxiZn33XrEHCRgWLf4yse%2FwqqosOjG0mOmAoNP7SLAiEAjGCQJggdljT%2F62AAFu9wxQdXqSK97JRaVZEiImqJuuIq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBFkj%2FJPbgxxVYdRYSrcA%2FTr5G%2FufePqqfg2%2BQpdpnkbvnrpxqMdMQT2ETvMWvsjW%2BBaYKaZl6gaK00WDa6fCjwJq4caAZlNIq5FKYtoqz7fV8M3Nw6S3ZUpLWVlm2APW0ywn39HE1Y%2FfjskcWsTFns73eONNvr%2FAtDRLDngWKapgf%2Fg8RwLqPLzq0fntxt0ZSl6QZQmKDEVjfdFx9Dr%2Fq5xIRf0%2BA6Bn8zr1spbHyJLDThoC2Xx0X0yPdoNoCXNaVQowXPFuKYOVrSHU0ht2K0BQJKzXiKRPA%2BmGUq1vnOcF2%2Bp%2FV6w1zQXhZzNx17yZuPw2%2BQQBT4dlC9Pnp49oz6MNY7k1%2FC6zg6oR6GX4bTxf7GY0dZ8s06gu7N8I1XEUlgJgJ8nWWiPG3X%2BzMV%2BvfihWaxXhc27FRJa43Fk%2FIPYXDZCwGEiKXrhL3BVQlbZvrkS6xKReejdEjffIIGzXXf35HEhgRggopWzhsdk8f0Air7FjAZyeh2a%2Bg9c1X5UxUL%2F82FOoicuDLXwtpqWsjiQoLlnRDvdFVKqZoalN7E8TJc%2Bm741XJOxxj33omTDFWaZ3iP%2FjkQ%2F%2FP1%2BcFjpwY39BNM7N2iNZ0iBdAg0mAhM8FMbEAfPKcsf1pgRLkCycCqYlF4zRzZadE5WMNSuh70GOqUBI7tMKxvqN9QGNhyUHbGY6uJ%2B8ef1bHpzAUnfDEby1aNs8nbaWe%2BL8ik7jvXwSUoNmS792LsrPb5dH2ADib63xrH%2BIPslVmJK2m9LH9%2FicRz7FHPtjcE4E%2BPasxy2EDBQ8EuC9fBdeEUSAhO1TLpDdW6keFriyeGPE7Q6Ji15kHdbWi5V7cDicmcIktM1z%2FCERnBqCbvqu7AAJ6dkFY9eCr1nvsmK&X-Amz-Signature=35a514569c750fe5f5ab1567d0e97cea94a0b81d6323faf5427e9adc90e4ad09&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MPUWVL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDckxiZn33XrEHCRgWLf4yse%2FwqqosOjG0mOmAoNP7SLAiEAjGCQJggdljT%2F62AAFu9wxQdXqSK97JRaVZEiImqJuuIq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBFkj%2FJPbgxxVYdRYSrcA%2FTr5G%2FufePqqfg2%2BQpdpnkbvnrpxqMdMQT2ETvMWvsjW%2BBaYKaZl6gaK00WDa6fCjwJq4caAZlNIq5FKYtoqz7fV8M3Nw6S3ZUpLWVlm2APW0ywn39HE1Y%2FfjskcWsTFns73eONNvr%2FAtDRLDngWKapgf%2Fg8RwLqPLzq0fntxt0ZSl6QZQmKDEVjfdFx9Dr%2Fq5xIRf0%2BA6Bn8zr1spbHyJLDThoC2Xx0X0yPdoNoCXNaVQowXPFuKYOVrSHU0ht2K0BQJKzXiKRPA%2BmGUq1vnOcF2%2Bp%2FV6w1zQXhZzNx17yZuPw2%2BQQBT4dlC9Pnp49oz6MNY7k1%2FC6zg6oR6GX4bTxf7GY0dZ8s06gu7N8I1XEUlgJgJ8nWWiPG3X%2BzMV%2BvfihWaxXhc27FRJa43Fk%2FIPYXDZCwGEiKXrhL3BVQlbZvrkS6xKReejdEjffIIGzXXf35HEhgRggopWzhsdk8f0Air7FjAZyeh2a%2Bg9c1X5UxUL%2F82FOoicuDLXwtpqWsjiQoLlnRDvdFVKqZoalN7E8TJc%2Bm741XJOxxj33omTDFWaZ3iP%2FjkQ%2F%2FP1%2BcFjpwY39BNM7N2iNZ0iBdAg0mAhM8FMbEAfPKcsf1pgRLkCycCqYlF4zRzZadE5WMNSuh70GOqUBI7tMKxvqN9QGNhyUHbGY6uJ%2B8ef1bHpzAUnfDEby1aNs8nbaWe%2BL8ik7jvXwSUoNmS792LsrPb5dH2ADib63xrH%2BIPslVmJK2m9LH9%2FicRz7FHPtjcE4E%2BPasxy2EDBQ8EuC9fBdeEUSAhO1TLpDdW6keFriyeGPE7Q6Ji15kHdbWi5V7cDicmcIktM1z%2FCERnBqCbvqu7AAJ6dkFY9eCr1nvsmK&X-Amz-Signature=8621b6da5db8c5ad9a50ba0b23997cdacb8b030c592fb410532bcca24d7138a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=8c22cfd72337cf08845fc8aa837370ee5e83e08d4c99b42624e51e82d456e5c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=cf2875fb8e2a965482c3f67962b369a813ec1e1f659aee71e3aa6ac1c3d5c024&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=ed59fc54e6c3b13f614e24cdab8ad8e93b06952409f3883bc5168f7f35571ede&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=a795afe8782bd9849982f1e25299a4cf47c8b6f8a29b1fae59f04bcf50da6ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=14be789a9bf263d8fd641cbe7193e188ce4271a5b22de3855e535c5997a0faac&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTMWEZ3L%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIEIonh7fFYqiVX%2F9OFaGTNVBpWK8ti3bydkiG8%2BH1%2F2uAiAq5W4VTwyqD3J6PanHz26YrhCfDhwYhAWWmbKvSf5XrSr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIME1hwTu5rul4d7UezKtwDlPQp5Z7on9pnbIViJkBDuMirtAyof8EXXaGv%2BzEWL5tHFCucIpclnhuaoIDd3uzILfPxIZFlfkdhQu3sl51SMAE9CQS8Jww2S91bBlEVC8YR76o2Y85Gc6xjqrgEpGMDC2%2BtRxv5pCHkQAmek1a8rT60vqeIUkD5qjY45liSrQt6dQcVUlaHCpggWOWUcA3voieOcZIon%2B9JYoTaWLmB5fDE8t5s%2FoyJpov13%2FqNhkwl%2FMrzSP0u%2BElDJg3slsfMJ9RoQJ4ui35g8rD2hmclxGVJDUC9B%2FIzHzamfTu8lJOLtdBujhCRdIIQDnhD1rLvhCRJELknmVvxnxBERuCQONQWgaLn1kvr6L4BdqMFdQ2Oq0%2BYZMvnoq80lRmizyCPEh0VzWt%2F5kwvJLHwM02xrF3IFnWXj%2Fq1pkYwNcAAjCd4yMi0xOLChll3npRZ4%2BZzrw6xFc77XdfjwKxx0BcfrtFo9485eyZfzKwh4Z4ncAaNvzMetM3AGAroaOnHMrot1VvjBoKdvhRyRvO34%2F%2BDErt4%2F7ZoJnJMFXoUyuvsqwFR63%2B%2F8o%2Fud6bpC7Y0%2F7Y%2BzI2MMNZKnname6xWZh6krbJEV9dEfjKYNvHT%2FZmBKLNBA8uwzFRX1cqQH%2BMwxK6HvQY6pgF%2BtDifu6C4PbOWDKjaQ5CM0Gj%2F0K6r1j6a%2FnqaJEhnzgoWF21cI66CC3YataGzjoHMgOlxTbQNowqeFIrjrM8pDtoUuRO7qBrjkojSmlB3QuYtDZacEzN%2FHB5FaEkZL0NXzzXjVzAbzxRuFCk8WJRTPaWkmlCgDLMQ6qnvq6egHxtLmXXF3HqObIDaoXlRrsVaV5G8dRB6t%2FlSDOdX62IvSxar4eXB&X-Amz-Signature=d27a1583ad8fb34458cb6cef633b9475c647076b04f3bff552f43a0b94271019&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLDUXZO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCCnHPfR1rzWMjYU3krD8EJb30hubC2RPY%2FpdByI%2FRwTQIhAMBZx8DfEz2kV54guX6fywWVnKv0amBvDORGwBZnMV3DKv8DCCoQABoMNjM3NDIzMTgzODA1IgzhX%2BpWDQ5u%2BHNW8%2FMq3APRHwtPkOAHe35pqLOvGj6Uh007ijO1UVsZ%2B4Uwk9wzTFUnKYyL7LmVL7FiHS1OLbht%2Br46g6JLXNMkLvuV13YIrLqALbGbGMdQoFhfGKz37o2UhOzAG1iz5Ic%2FkaX3ruOS0pQKY%2F2MHV2GtiL7ZTdhcFcdSfEKxGDcKHsojOefvFLsCLv7Z8ml1d5h%2BE6aHJi4w0NzmrPX4UGSeBQL93SyK8Hq%2B%2FaH6TrRhtwRU21J5G3cC9o0L2hwkBP20WwE4KfN73Wvu08AuvkEG%2FN1n3S4UsmPL7BV4vV7sLIakm27L5jMgB6m7e2FU0sJ6GUnyp2QB2UtDyOxIxHLAtfIEK3mF8m35nWEqOT65kFVO5TMhV%2F7FI5VMZaAtnhNq3jVv1x%2FlKwWe%2F27XAwgqShViNdSM%2F3I8Hf34EphwFosVzUSC4xNSBpQRlvm9qjifUaEVaIogkEGADfLzQ5lwo4sRek4%2BEH21%2Bcl5aciX9YBADG5VJWGJxzOq3VhwzCPD%2BDokm7L6EzQ4%2BZiYVOTXI9BMXDXr3JKL1FrQVTE0ll%2Fb6VeEsUU4huGKBrM1r2S8bfwqf2ne9uSLjJne0AwwUjcbRRCimlP%2BtLIWRD4YqHo8EmDt5N0Fv4BEQPTJ0YJxTDjroe9BjqkAe2tqlbH46RemXlbKHFbPpsTbGH8F6CxVoe7FSuXTjDMrD7By%2FuQvED0dNbjOT8SgjiIXd3wytVmpgOSfYs%2B1p4%2F1wBz1DtLPbbf9UKNW3fvWH1BlJORsgHOzPaowkfATOrYoG1a%2FULJR%2FAfM3EnmjyJFOENnDbovarrkwVtuQABoivlsGO1TwoMO%2ByebkJPEtPemyKQVcB8mjc2%2BfoLEZtPmUgQ&X-Amz-Signature=48607afef3b6ada8a24ceb7e3bc4b62aa0952543a4318b42c71cb6df5fb2b743&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLDUXZO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCCnHPfR1rzWMjYU3krD8EJb30hubC2RPY%2FpdByI%2FRwTQIhAMBZx8DfEz2kV54guX6fywWVnKv0amBvDORGwBZnMV3DKv8DCCoQABoMNjM3NDIzMTgzODA1IgzhX%2BpWDQ5u%2BHNW8%2FMq3APRHwtPkOAHe35pqLOvGj6Uh007ijO1UVsZ%2B4Uwk9wzTFUnKYyL7LmVL7FiHS1OLbht%2Br46g6JLXNMkLvuV13YIrLqALbGbGMdQoFhfGKz37o2UhOzAG1iz5Ic%2FkaX3ruOS0pQKY%2F2MHV2GtiL7ZTdhcFcdSfEKxGDcKHsojOefvFLsCLv7Z8ml1d5h%2BE6aHJi4w0NzmrPX4UGSeBQL93SyK8Hq%2B%2FaH6TrRhtwRU21J5G3cC9o0L2hwkBP20WwE4KfN73Wvu08AuvkEG%2FN1n3S4UsmPL7BV4vV7sLIakm27L5jMgB6m7e2FU0sJ6GUnyp2QB2UtDyOxIxHLAtfIEK3mF8m35nWEqOT65kFVO5TMhV%2F7FI5VMZaAtnhNq3jVv1x%2FlKwWe%2F27XAwgqShViNdSM%2F3I8Hf34EphwFosVzUSC4xNSBpQRlvm9qjifUaEVaIogkEGADfLzQ5lwo4sRek4%2BEH21%2Bcl5aciX9YBADG5VJWGJxzOq3VhwzCPD%2BDokm7L6EzQ4%2BZiYVOTXI9BMXDXr3JKL1FrQVTE0ll%2Fb6VeEsUU4huGKBrM1r2S8bfwqf2ne9uSLjJne0AwwUjcbRRCimlP%2BtLIWRD4YqHo8EmDt5N0Fv4BEQPTJ0YJxTDjroe9BjqkAe2tqlbH46RemXlbKHFbPpsTbGH8F6CxVoe7FSuXTjDMrD7By%2FuQvED0dNbjOT8SgjiIXd3wytVmpgOSfYs%2B1p4%2F1wBz1DtLPbbf9UKNW3fvWH1BlJORsgHOzPaowkfATOrYoG1a%2FULJR%2FAfM3EnmjyJFOENnDbovarrkwVtuQABoivlsGO1TwoMO%2ByebkJPEtPemyKQVcB8mjc2%2BfoLEZtPmUgQ&X-Amz-Signature=d0e0b6e1cba050afbebefda5788db40a984a369d41d984a40bd200a50ab2d592&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4NKJYGC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCsGR34grWMhrz31BK%2Fuzu5eovsFg0iDPT363NTPTsZaQIgYSL5nR9uqh5jFbvbkUZDM0YyDVQtAszOKzldfmFO4lMq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDHCxKf8Oekp%2B2c3G3SrcA33GDVlMf8J%2FDbvvHimFnOSkH42nKUd57S2foziXMMu8mMb50yxgYSpWQUmjnSexJWlFIEnPplZzrm%2FLAw9kyd3nxZ%2B0M14NFIofohVMJyC0gao%2BvK3EJVFV6vkkKwxE7%2Bqs3g4MhuES8BZexI1248tDptXUJAOzidnF6IcxWffRaVuQw0vuFdpkoqPvuZ%2F9h03H%2FreeNNbiXwsZRlU3uggZB3oNsFL2nzNL1goLpj1jIwzhcAWn%2F6TkPUDqcs00QkXOZE7C%2F38QKhm%2BfGVvb%2FBO4jDAfVDy6%2B1xYF1Msx5PEDHJ%2FgDkl8mrCwT0wlJyO3inM%2FvoPU9ooRqSxPHYDgVlKJv%2FbIonLJqO%2B8FaFtJyMd4gEjJM58X8oVnY7NUYm7P4eRX36rQ%2BdKM9pglidXQO3%2BP5oHO7XOAdPyDqMI0ZeEzMJ7Dv5kRBH6vaPan5zxRVyyaC5kowiQbnkA3x8KbR0CSzDnTIMHRVIcNOim3u%2FTKVuBZ5ahay%2FI9d1RVDdrZP99n0QIjwpOJERruOUFJQHS3OKCIERtRatWd%2Bvu43DjYX9gc461%2FPe5Cv95%2BPSt8Ey65N1eMVO6lqolgjB4x8%2FkClDgksfU0RIfdpAgB1TRDDk5fMhMw1eVYKMImuh70GOqUBxW7VyYb1hOEYOPS9rFSO0zXpqzbd4vw%2FGFmRLZ1Ot1fleTg4Z6o8cm1T3PxkLKBu2Ylv1VXElghQAX7oqYJsIgugTMcxRVYTXz%2FVWiIBMI5XwSeYxRCCzdL%2BJNr38snLVeUkEabCoe1ACght6qeFL9eB6EvikrBaG4Hao5WrI1ZcNZootBQwng%2BpcnPA6xrMOEsYogSsW1RPNEfPJ%2BLyaBgBQ5HV&X-Amz-Signature=1e2db389e1e6b803e7b6a646602b080644edd56d34293b329795a0c0e3591451&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDV3GYK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCl6JjoKmkUc3QsGrcmdfR7R%2BGWSySUlbQYjEi8GyMdiQIgCbQWH1TSG9YzlvkmKvexhlkLrNlFVOHlEtkiDlosKy4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOKV7TIeT4c84JvvUSrcA2dO90sKo8r1NSFqKn7Cz5D7kD1fs%2BaRjeibL9nPlbPbHkUfpcaF8xqazKsK4RKmmzKXm8G6e90csh32GALvcmvAmeYrYDPR8YIXcedIj%2Fl4wmuQCCdEICxBou54icHwBb9uuRA9kIgi44IjlzxlnjMDnv7Guy81Yl4yedRmUAvfRX1F%2B9pCgn2OaJ9BIczPjIvphg9RFi06u3B4TxuajrN3rQ2aC4hI1lm1Ji3hXUFo5aNaJeA9IXisFcVMinkoVWv6StfDUqqtLxitP%2FzS3pkIegzTvdTt3SniMBvLOmRPL29n%2BfnG%2FQvEvQLkj3ommH6fdo%2BztwrWnuUn6AIEJ%2Fb2j0jBp9X5k%2B45Shc4C6jj%2F2QlP6V%2ByohP9XxgmU6w3kjy0BklwAxCjfdUPzzMUGNYLTaI2FqLOK%2FLkeGSKF1%2F0tOrMYJzpx9pJmS3aUovqvBSn8W643Ob%2B%2BYutrPJ3%2FkqaBhJ6D4M0EIGi2IB09%2BzpI%2B3YBNwIVk0mGNnkXDMgaBjUVE%2FuanrtpwYquRJUPDmk1zZzEYO0CHOQGZNwgWBPaV3IEltOhpodMOq1BWbVBCiL%2FL8LG61PEJTapjxOtPec%2BPWfFkKveZ9k4Ahh%2BRHJWRwxO1%2B7brmQN9TMMauh70GOqUB%2F7kd9rl33JmxIXomv3tEIuFvMKOyvjGVyTgsfMik0YI3vCQp%2FZLgVnue8tjCIeXwp%2Bma98ZJVMdQJ7OTOqyHHnuuB%2Fz3hFSsJmmpz2D4WP8sJze4TGNCPY5h4tC5ggLz6AHtijEyA65klsAWd2Q9hGovNs%2BwMLp5nmnWdvmT0xK3WoA%2FwlypKR7RsBAjUGtUCVjvwPgWFKdasndwsftllalwE8VW&X-Amz-Signature=da70150061cab89d9d436af0532baba876006057b2b18249b279dc2dc54e9760&X-Amz-SignedHeaders=host&x-id=GetObject)
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