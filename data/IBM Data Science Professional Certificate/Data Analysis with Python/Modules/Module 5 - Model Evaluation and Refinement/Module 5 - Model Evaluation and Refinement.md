

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=f7eec97cb88536e5b4f42528db1998d4dd3e96ddccd9ff84b4513493754c13ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=637a035cedbe75b63d100b55fe81b7f3415eca9f60eb33fb043516909a82ed5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=59febb88fe3c3c633b8e2c1d7e1d6d6dcc971c749f6ff2822e1fdebb26603dfc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=b07deab7f0cfd427462d71a921d690ea93c0722a3a402aec6e6b57647a4ce58d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=9e2e68a467be6c8566ab3baf836464885dcb8af13cfc7d2cb80dca328e404196&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=ef62735ea98422230bbbfdfea7cb3c1cde051f1fc31c0066e602a1638c844024&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=8110c7b2b47d4f8809999468a4022e320e91fe8e433cef7c0575a19e3622dbee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=4634f210dda44c9da690e06fb6e7a9fc215ccbb5e241f13cd88987f8117162f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=7ef2590f6d99b1c24b1745cc149ead8cb58845da85987400fae8bfb057db515a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBB5GNJE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIGtKaKmgZbWAbQTNW7fPdvpFHSSRQ8Y0mEI%2FJ8XY0ZThAiB%2FjwfnQ4dIx%2FUqNyrXgRhfW5KygK7wKSRqqTwjolQA6Sr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMp3uTcvlpeEubbCbKKtwDzR%2FJVFE1e2Di%2FtoYXuVdRE3Sm78ANAzeqAO7e%2F4EKk1pD7bLcqZVZqM7XJcMWrvnSJoROXzwDLhKbEw95m9YCocS9gsNyTJegUQRDYOa7LoDW494dIwPvWLxE5Ho6quOOC3doA40X16CPaQcj1jhKjMffhacx8sasf90gifQkaZvonmMtCrVYOBWH7miQ%2BH6Cp%2FVY9UMzyHS61NgmGdp2VVp5e0xHuklcgFJoZERs6EPouuXZKOCKAUZvwDHy432vOC%2FQnneVQCXQ3Ls6FrhAKmDCZGrZTja4ZedInzXhir5w6cYv1NPXv7T26M9BSrfondLBT1OqXtT8mEgvjC22wTwt%2BA1OO2xDHDSPESjhT0QfjMtuCCZdGGY%2FTacMiWVVEEPR6ZZlx8OU%2BE6XM1z%2FViy3cJx3U7bIOaCuk%2BhViAJZGUZw1ICeVwixcYudO6S3IvtDpXgYGQ3Du0yVgE4D1ORQrPAcFX7g7EtQ%2FGl%2BVuwi49ek%2FUQto%2BMtBS0tjV93OOMeFW861MQPu5uKF5TQlHtRpjIysNkNKs6OxGmH5tIW7QwEl%2BMmk%2Fr6jSJDlBd2MnQ%2B2fEW%2FgRbs%2F3Ol4MGif0Q5PDj7GOU8Bclpacy85cqLToE5JaFdJ%2B0Oow7LeUvQY6pgH4uRxj%2BV5VxPvtPVV6dEbZhjX86zTu%2B3UUYxv4y7Qt2YXIREvViEnMHNRCKTHW9i6%2FRNI6eF%2BQ0EYSzm85%2FjQb5Lyk3yVCcEkRK0oxq1u8006TlonXt4MF3p2FqKEJc1Qc5vYuCt7pbwWwMDVr8zgoQStBaUFpdCc54Z%2FkyWa%2FTeX%2Fwbrmsr2WSQLRP5ijiFbWZqqoTyTTIeyJX9%2BE%2Fuhp%2FfJx9IWA&X-Amz-Signature=8e484baf0f85afea470c7d3b7adc7d5a2671bf42a5d2be7349394a79011fa2e0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBB5GNJE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIGtKaKmgZbWAbQTNW7fPdvpFHSSRQ8Y0mEI%2FJ8XY0ZThAiB%2FjwfnQ4dIx%2FUqNyrXgRhfW5KygK7wKSRqqTwjolQA6Sr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMp3uTcvlpeEubbCbKKtwDzR%2FJVFE1e2Di%2FtoYXuVdRE3Sm78ANAzeqAO7e%2F4EKk1pD7bLcqZVZqM7XJcMWrvnSJoROXzwDLhKbEw95m9YCocS9gsNyTJegUQRDYOa7LoDW494dIwPvWLxE5Ho6quOOC3doA40X16CPaQcj1jhKjMffhacx8sasf90gifQkaZvonmMtCrVYOBWH7miQ%2BH6Cp%2FVY9UMzyHS61NgmGdp2VVp5e0xHuklcgFJoZERs6EPouuXZKOCKAUZvwDHy432vOC%2FQnneVQCXQ3Ls6FrhAKmDCZGrZTja4ZedInzXhir5w6cYv1NPXv7T26M9BSrfondLBT1OqXtT8mEgvjC22wTwt%2BA1OO2xDHDSPESjhT0QfjMtuCCZdGGY%2FTacMiWVVEEPR6ZZlx8OU%2BE6XM1z%2FViy3cJx3U7bIOaCuk%2BhViAJZGUZw1ICeVwixcYudO6S3IvtDpXgYGQ3Du0yVgE4D1ORQrPAcFX7g7EtQ%2FGl%2BVuwi49ek%2FUQto%2BMtBS0tjV93OOMeFW861MQPu5uKF5TQlHtRpjIysNkNKs6OxGmH5tIW7QwEl%2BMmk%2Fr6jSJDlBd2MnQ%2B2fEW%2FgRbs%2F3Ol4MGif0Q5PDj7GOU8Bclpacy85cqLToE5JaFdJ%2B0Oow7LeUvQY6pgH4uRxj%2BV5VxPvtPVV6dEbZhjX86zTu%2B3UUYxv4y7Qt2YXIREvViEnMHNRCKTHW9i6%2FRNI6eF%2BQ0EYSzm85%2FjQb5Lyk3yVCcEkRK0oxq1u8006TlonXt4MF3p2FqKEJc1Qc5vYuCt7pbwWwMDVr8zgoQStBaUFpdCc54Z%2FkyWa%2FTeX%2Fwbrmsr2WSQLRP5ijiFbWZqqoTyTTIeyJX9%2BE%2Fuhp%2FfJx9IWA&X-Amz-Signature=1c52d8f897b449f4399d3ab0d509782b618900741801ee12b470ddcb9281919a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBB5GNJE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIGtKaKmgZbWAbQTNW7fPdvpFHSSRQ8Y0mEI%2FJ8XY0ZThAiB%2FjwfnQ4dIx%2FUqNyrXgRhfW5KygK7wKSRqqTwjolQA6Sr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMp3uTcvlpeEubbCbKKtwDzR%2FJVFE1e2Di%2FtoYXuVdRE3Sm78ANAzeqAO7e%2F4EKk1pD7bLcqZVZqM7XJcMWrvnSJoROXzwDLhKbEw95m9YCocS9gsNyTJegUQRDYOa7LoDW494dIwPvWLxE5Ho6quOOC3doA40X16CPaQcj1jhKjMffhacx8sasf90gifQkaZvonmMtCrVYOBWH7miQ%2BH6Cp%2FVY9UMzyHS61NgmGdp2VVp5e0xHuklcgFJoZERs6EPouuXZKOCKAUZvwDHy432vOC%2FQnneVQCXQ3Ls6FrhAKmDCZGrZTja4ZedInzXhir5w6cYv1NPXv7T26M9BSrfondLBT1OqXtT8mEgvjC22wTwt%2BA1OO2xDHDSPESjhT0QfjMtuCCZdGGY%2FTacMiWVVEEPR6ZZlx8OU%2BE6XM1z%2FViy3cJx3U7bIOaCuk%2BhViAJZGUZw1ICeVwixcYudO6S3IvtDpXgYGQ3Du0yVgE4D1ORQrPAcFX7g7EtQ%2FGl%2BVuwi49ek%2FUQto%2BMtBS0tjV93OOMeFW861MQPu5uKF5TQlHtRpjIysNkNKs6OxGmH5tIW7QwEl%2BMmk%2Fr6jSJDlBd2MnQ%2B2fEW%2FgRbs%2F3Ol4MGif0Q5PDj7GOU8Bclpacy85cqLToE5JaFdJ%2B0Oow7LeUvQY6pgH4uRxj%2BV5VxPvtPVV6dEbZhjX86zTu%2B3UUYxv4y7Qt2YXIREvViEnMHNRCKTHW9i6%2FRNI6eF%2BQ0EYSzm85%2FjQb5Lyk3yVCcEkRK0oxq1u8006TlonXt4MF3p2FqKEJc1Qc5vYuCt7pbwWwMDVr8zgoQStBaUFpdCc54Z%2FkyWa%2FTeX%2Fwbrmsr2WSQLRP5ijiFbWZqqoTyTTIeyJX9%2BE%2Fuhp%2FfJx9IWA&X-Amz-Signature=b37e2e7651e986913dfe1103e9fedc01ae133f4c3303c972e8ec5b058081f5f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=c66d4b6617b6c5ee608feaba4a34250fc17dc2c7fd35674e74aeafec3e7f6a07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=ca2d939e05cf2b711b4f4fd6e5f84c03ecc0101955712200f7053db9dafbd2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=96a24d8b75dfa70f7695ee51b1888385daebd5a229f53284e014412a38bb1f1e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=7b6ecbecb55e60da573e4c36e9d77e7b57c88afc7c867a98103ec1296edff1ba&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=8e47133513777e93303def2c161802710c3a0fb372f682955d56ef0ecd2b170d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYLB6B4B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIB0wW6iVeS2f9TZT0MjOjGRptGL9DH2Y3jyxzT2dbGw0AiABT3YQFM0m6Wha2w2s9TIANR4ak%2F0xAjM6LONt6%2Fj4xCr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMIMjrgAzC7AnvLOvwKtwDBNooXIqpnd28D2d0QYDbidItz8ldlRg43KNbAXfjVt0TaQcIUdKWyQJXLfxRYAoJgFi4MKoPZvPwjddmUy20xymWcze4cV9m%2B1%2Bjm1ftj8QyuPoFJmVLK7jG0wGCtutiIS9x7AKMfsSdOVn5MBeuaCI%2FYktBm32QOcZP8dmxd1xG6jEpUDwR%2Fouq3f4%2FkrbggDdCrd11a5F9vh%2BITSzEJ2drKK7gpv7yfgFw3TihzdT7Zc55pr3nMcHbmxlxSpApPUeMYcUJqwP9sgN6hku7YKzSGdcQJZ%2B2VMMIg48QvCdNh1zzWdQ4xM0fuxYv0r5p8MzjFGIyIsIFznjCOm5dBKSBBcBWUP%2BoJHtBBNEZ2d3Pd31KuBJ%2Bm%2Bx0yjQOtk09Rpm7bvOEBWu6pJ6B7nWF7PyVDkaFoSKTqHv1saVjQizkpUuQxbPnAHviNdlI5M2CIAIn3mcWfUGlvAVFBoZxjAKHQyNls1EsN3NYLumXVyav6tEzpIR630tC%2FoC0QggRhxgMAUUdNOkL%2FSOoIsHc8TcTIFPBEr9QcjIHmJmGrr7w%2FOllHVxasz3O1V3dlE9kotw%2BTPgn1plQKJ2DmVPuQWCuUcbriy19dKptHGDbXg71qEwQzB5PuGDHl6Aw47eUvQY6pgFUHBJDQbua1oWfMTFRiwaM%2BUBkO%2FpF3V%2FEksDjl6L6aEAzzu1sKYMAuV6hj2OEk9%2BnQoNzP8S8Db3IYiMJ40nzmNlKfbHsIyiKKflZq3S8ZzVzXVMcxc6MeCVdAYvcBdc3DQh3%2BTNWzpfOuDeJzhineYogsvDCkJ%2Bp1PcUE6dsPDTMSVajJK%2FjI8sfVZsB%2BcGiBaEarzco7W%2FLYbRv9MNrqA7RK0s4&X-Amz-Signature=bc815cdb8c159899886a3ee4d2c63c1afda0c4daa4364fc8b2fee204652e3b63&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KBFWG5U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQD75zaOBShg0XY5y%2BiNC1pN5SC6msITwrl0DkImpLeRwQIhAIqaf%2FBO%2F%2BFHl2H6qcKOKNkCHwDfMT0eHXpr5RF%2BDvtiKv8DCGYQABoMNjM3NDIzMTgzODA1IgykOATaiZFLqaEgpREq3AN0j94kdG1bQO8LpV0vRqsUWOfQkqocxymv8Bl8LfMwZxMPPtWGZ7A9hQaMMByJ8ctTFZhdX0flU%2BBUNTnLzsqieSV8DN0ozPTbGlWRl4dpHuHZDrqg3mtJrn1K1cT5XcK%2B%2BDyxvGzCfKv%2FfQp9kHQolgPNFvpHsI%2FCqnAKAAt9az6UpQp1G%2BQpW0E0wABCVYkQ%2BDrh7jBi4zePdV7%2Bj5txu4nfnxJxrNWphO7htVzH2CaQE5NdE8cRnVZZXUXwXZW550K23U0vz67%2BIIETd0yutEC525JQ7ZwUIioSPRhYvWlk1lHR5ithOH5tE3mng%2FJP1902UmwXF66MJjhF0xWcyXnhqrcN4z6aoeT%2FmfedSp8PbnGz7%2B20wsozFVcNLZmYQYVSR%2B%2F3R4Ag%2Fhg42twCiUgD%2B5jjb8G6y7dSz0Mbtr%2FZD4Maaxw24n4tFud26krJirlafQ%2BQGykfIDO5UCzjtqcw0yOtvNSK%2Fbnjb%2BrYgf8Clzq6xr0L%2BdtmuyaPUTEdFqYSYo%2FFUbYUGeHNutsBEexzDLb637HN6TPTX1Eixi9pnQkM8DI%2BFgXNxuxagOKcBXxbC7V0jPm%2F6rQCCyf6ie%2B6v2qEsg%2FWC7dlGgTdEdNhcMBPX1MkiUXqOjDvt5S9BjqkAW%2FRg%2FyB5nvj9%2Bg4vfWZ9flFCWb83yVe2GxYXHY9K3WmlOhOwg1PZwH1FKFzeeCm3Jk749j16I%2Fbn%2F%2Bse7qIzkNnnxP%2B14eoK0qAUKGgoj3jv4E%2F%2BYf8UIz6Al%2Bxhj7YTaggwEOHtQ6fz4xBD%2FcZxASmQqDqoPENQiguZuidmV%2BLQA130e6l4RaPC7lUfxs1X5XM%2BQxCd1QMPpyJjk6jjwduy6l0&X-Amz-Signature=7af71b84c270a41cf16d7bb6d06dd23a181b19895448e993936740d72de5c84f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KBFWG5U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQD75zaOBShg0XY5y%2BiNC1pN5SC6msITwrl0DkImpLeRwQIhAIqaf%2FBO%2F%2BFHl2H6qcKOKNkCHwDfMT0eHXpr5RF%2BDvtiKv8DCGYQABoMNjM3NDIzMTgzODA1IgykOATaiZFLqaEgpREq3AN0j94kdG1bQO8LpV0vRqsUWOfQkqocxymv8Bl8LfMwZxMPPtWGZ7A9hQaMMByJ8ctTFZhdX0flU%2BBUNTnLzsqieSV8DN0ozPTbGlWRl4dpHuHZDrqg3mtJrn1K1cT5XcK%2B%2BDyxvGzCfKv%2FfQp9kHQolgPNFvpHsI%2FCqnAKAAt9az6UpQp1G%2BQpW0E0wABCVYkQ%2BDrh7jBi4zePdV7%2Bj5txu4nfnxJxrNWphO7htVzH2CaQE5NdE8cRnVZZXUXwXZW550K23U0vz67%2BIIETd0yutEC525JQ7ZwUIioSPRhYvWlk1lHR5ithOH5tE3mng%2FJP1902UmwXF66MJjhF0xWcyXnhqrcN4z6aoeT%2FmfedSp8PbnGz7%2B20wsozFVcNLZmYQYVSR%2B%2F3R4Ag%2Fhg42twCiUgD%2B5jjb8G6y7dSz0Mbtr%2FZD4Maaxw24n4tFud26krJirlafQ%2BQGykfIDO5UCzjtqcw0yOtvNSK%2Fbnjb%2BrYgf8Clzq6xr0L%2BdtmuyaPUTEdFqYSYo%2FFUbYUGeHNutsBEexzDLb637HN6TPTX1Eixi9pnQkM8DI%2BFgXNxuxagOKcBXxbC7V0jPm%2F6rQCCyf6ie%2B6v2qEsg%2FWC7dlGgTdEdNhcMBPX1MkiUXqOjDvt5S9BjqkAW%2FRg%2FyB5nvj9%2Bg4vfWZ9flFCWb83yVe2GxYXHY9K3WmlOhOwg1PZwH1FKFzeeCm3Jk749j16I%2Fbn%2F%2Bse7qIzkNnnxP%2B14eoK0qAUKGgoj3jv4E%2F%2BYf8UIz6Al%2Bxhj7YTaggwEOHtQ6fz4xBD%2FcZxASmQqDqoPENQiguZuidmV%2BLQA130e6l4RaPC7lUfxs1X5XM%2BQxCd1QMPpyJjk6jjwduy6l0&X-Amz-Signature=d13c50cf26f6688396509cf7d4f08d47a72ca2552a077584bbd637398e41b953&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH4Q2H54%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIBPQsAKEsFKte9k4Gj6%2FI5rw%2FKk0t0hHW2NRFuYovQQIAiEAtjjAlKT5IdJqkhpAb%2BvX6eAKRctrtSvBVoOM46zqVooq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGQsYAX11vK27sbAZCrcA1OfD6u2x19Ks7VS9GeEJgC6eHyDgGLmN8VfN9ASlSMCOqngy%2BFDi8CRuV7hgThmRBnsC4a8lhZktBN3jkhqJVx2f1dXa%2BxFaxjNDTj6Q5DG04YfP0PZSzQ6yo2oOHGHMju1Pat92D2OuAwU1K1r%2BlSp82Pa7ECDSDB6zf4shvTbF8BHEofNhnHMePO8LmdJAU77z9KiNvwMF3olESr3cWhyTxXCeWC4F3p6zLvDMfqSqh5vMkP3BBEwtMyK2Xueb%2FMNMmVxOXDcJEyIIr%2BDFhz8x2L76YT%2B9qt1JBamfBpX6E6u%2FLwcZ2fhMgy4THsTo5ITVbhIathk%2FOZwnw6SAYG5ZgNSC2%2Blu2BkZoyjWjIHMrOFhznuYmpoBpToke4NN7wlDRtJa5sggOJn4B1x9d1dYoFKiV1vC4482u%2B3Clj9riVXhNuOH2LpCRSfV1h%2Bv9Rm%2BA%2BfVMIpNr21YCBQSOQtVxQNYq2uOlihddm4Zab28cIF0C5emQ4dL6c32pfE8q3nqA0RyOa%2Bus9cu45rUuFBQpUpNLB3zU7StMHgv5kRgoY6MrFbBaEvN26y3pjsSnOLCfL6gZCMqv3ma%2FMa%2FwA3enNaOwy6ww6jjFneLKAxnetT91q0Z6uCdylXMLu4lL0GOqUBOXtf%2FYssQ3Z9yWJJVovJbXmDxVQOoVpab6PtmJb79ussqxZAnP2cTVq0VI37cvuyRsZ6acC%2BzKgIjlICmR9Hl6t0yVA1aomIYkSt1AfZJS5Qo6MVihTKQhQ62sLX2AhMbSOtKhFZYu2o6UcuHEajRUDe%2BCIz7Gy8dUN%2BFNOawEpDR7qdmsCW7bJ4gFkxpgJruaZb9l9eLZM5ygTE2iOCAR1ofrxZ&X-Amz-Signature=0d683f08a6eabbeee347eb0c4bde8b48d64137ebcbffc2fd5f0bd5240accc188&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KR3NEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDRBjPuT%2ByzKwio8v4i5P8MscxiEyJRB6SOjqiG2UlCcAiEAkjdXSYLFVStaOTTSGSzIYWcYSpMNgj6aEh7Ridc%2BKkQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHF1klYT5ile%2BdKhtircA3L8JH04SGfaAr41uvHUsp08zIpmBOGL5ekDjZP7Cwz4lUlOZbvQpwncz%2BDdsAf9MXdwR5NquWTj2YlGs2Ru7YSOzaoIQ9m9cWSz9UuLRX9fhFjTI2lDHdmtLSQKSK8dwfSsgNkuzbAa8zreaYiKsXJfucA0mX%2FjTroRRSZsbcbJAmfJ2KoB3ayrMEWxItpMF2pNKi9SdQwnxzSkQanaaO52B7tNXd8W0KTWhN5pUQHJDUrb4yv5ksKJhl9dF%2FlC%2Fxo6Zw6z2BSC5muiKGxal1vV9%2Fcvfygk%2FaZT%2FUeTcB3hzy5oyNqrJmDUPMGRcn5Ruvy98yL7f05LnkMKHV26t0PUT1IlCZTffSNTgqDWYBSFoqyWn4a1i%2BsI%2BHbhmtfq4AXPn1ahnAmBK7JGSfyxmt9dUa5I%2B0EKwThDdLR%2BRHWYV2Z3I6H8dOf6DZD%2BXe33ByR%2BQf2%2BV6gdhu3czWtyqDDmoE3BsvZsQlrZ%2B1myO7HBa9C2lEo%2BeOpfegB5GxziIcFD8OieLHCAGpc%2FieP2CNW6v5h63mYZeaml8CcsphUvKrn7otJIS0uQ9GeGBIvRzmSlwLAVnoK5LejNFR6rQPEWofQPdkbKPxY0ob%2FduTtAgmooldQ8T7qRB%2B51MOO3lL0GOqUB9ojM9%2FF9AUMK8d7uxAfmVKhJclserw8rMxx8ucdNeWyImNSAP70pAKL90Rb93dQxnaJJfQ0fyp%2BSsTQWsh1o4%2FwIrfxCZhILq%2FefIFJGOfsWA7hJreidvmwy%2FWlrU0shCMNDAtgy%2BHZ%2Bej23lopixeoZ7k4wqvpHRBigMuhF6lbdssuempP3%2FtW5S9HFMD2tDdlv64fIir49e6v24GsBCUmS9neI&X-Amz-Signature=2e2297fd445f5c62edb55e2a6596564ce23fa4b04570c6acc2ceaf3b66709f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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