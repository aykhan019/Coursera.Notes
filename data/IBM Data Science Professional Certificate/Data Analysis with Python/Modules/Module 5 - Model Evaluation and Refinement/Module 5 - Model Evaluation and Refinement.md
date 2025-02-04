

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=b01d903ad4420f276b63de9ca018dd7de5855441ef0a1049bcbba41659a3bde8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=057e49c2e66588cb5fc7ec03b7507b495b5e0e3f8e70dda94b99dce4833a0658&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=04963f879aacf51414993e80628d7cf094abcefd27df633500814b6a0e555b3c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=7cdefccca4c0ef105e82ef88e3780985689e7f9e8ad0b0a6d31926ff18941c72&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=7e2e681a7af5e00937009939b5750c5b1293d57dff257ae2943a159c481d189e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=173319060ef6b8a816a591065f16323dced5dec846a059e277f20d6f596dfca5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=c1efb8cb6e71fa7debc1733abadba0b9c99bc967ad7926e016aeb3cacfbe4a3c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=9e96bf28dfedf883a8f8359596d6ef91188399a1b6ab57ca758e12be4d14c633&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=f0b58e47cece30588326a4919f4114d819a6d3997f2758caf5a4839b3edaa538&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAAE3OXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC3yAZfvwGm2whOf%2B1S5yywj6%2B5MBJQqlGb4pZ6QnBiNgIhAO%2FD1VxlyM%2BRW%2FLnuTjHDSBhFL5MsioohbtTTiDnoh%2BbKv8DCCYQABoMNjM3NDIzMTgzODA1Igyy%2F8IPP9zan%2Fewc24q3AMYSayajZGL%2BLSLJrHeKH5DDfJPjcRfFBaTc2LgmPrKSHcnl4n9yhO4NSfoEGdjxHSkhAzJzPzkMxpWoruDSTE7Foj0LQ%2FoVY8PN0aubX8PCtc4wNdNGLI7%2B20bd5QM0iQWwtIH%2BJyxrV7EPR3GbNZR1ku5iL14Dlts%2Bood8GforHhzbtvDotJysqONMF82mBbhbi5YlWgp1pS9hms4n7s3faUp3pE03j0stYA69HWcHW8kWCOv9EA2rReeub5FR1Zhpus5EXZ5DPp0Vzgk3PDblCBzfrZiXd8R56hpzPPFqaS3oqOQgj69HIyXPG2Yhrf4R2YrzJ26hTQeZ%2BnwAdpTg2m0NVsPVUU4PwmGftq14d8Stxa18hEzR2l8VM5m4HwGj7ieC5v%2BeVVFLkP9uvEhqJW3lIvfj92fCCz%2BGFVi1ybeOgaEkSCmguSSw%2Fx1TKVLHLPawx%2B0EYS7a8scerSOrkdD%2BuQymZCDXpgvx7voJVH2HrE15kmVCbihDDu4RNWPtsPsGnmk%2BcxxgEfhRV8ZW%2FUZrFbUhGEAtEHA%2F7b7mMdhxQpBJzDb9UToPjqUYomzqlCk8gGjJIETbfxzQfeYcgGPy3O116eJXp0XYt6cLJJ5ZMbGBsg488rHgjCJv4a9BjqkAWZICMQWO8IUPyf%2FMZqVQ%2F7Eg%2FVzVikkM9ByrsIHT3c6QzriKwGypzmmWIpA6HkGS5l5Q7HRLIPv%2BltYv9GVFSLEOTxEwGHnJGsGtfTXv08WhuzGR2i9nbDLGbo5FwrhS%2BPdU%2FqIuWD9KlXmoKJ%2FBDA8tdAmnfZWXcouGTFPViT2pdpab5l9biHD7U11kPu987MEj4651odhP7tEnWPDyweIaPPK&X-Amz-Signature=db88b87df7f4b0516ef0e9ba54cf6a38658eb877339bdbaed0fa5265d19932d3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAAE3OXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC3yAZfvwGm2whOf%2B1S5yywj6%2B5MBJQqlGb4pZ6QnBiNgIhAO%2FD1VxlyM%2BRW%2FLnuTjHDSBhFL5MsioohbtTTiDnoh%2BbKv8DCCYQABoMNjM3NDIzMTgzODA1Igyy%2F8IPP9zan%2Fewc24q3AMYSayajZGL%2BLSLJrHeKH5DDfJPjcRfFBaTc2LgmPrKSHcnl4n9yhO4NSfoEGdjxHSkhAzJzPzkMxpWoruDSTE7Foj0LQ%2FoVY8PN0aubX8PCtc4wNdNGLI7%2B20bd5QM0iQWwtIH%2BJyxrV7EPR3GbNZR1ku5iL14Dlts%2Bood8GforHhzbtvDotJysqONMF82mBbhbi5YlWgp1pS9hms4n7s3faUp3pE03j0stYA69HWcHW8kWCOv9EA2rReeub5FR1Zhpus5EXZ5DPp0Vzgk3PDblCBzfrZiXd8R56hpzPPFqaS3oqOQgj69HIyXPG2Yhrf4R2YrzJ26hTQeZ%2BnwAdpTg2m0NVsPVUU4PwmGftq14d8Stxa18hEzR2l8VM5m4HwGj7ieC5v%2BeVVFLkP9uvEhqJW3lIvfj92fCCz%2BGFVi1ybeOgaEkSCmguSSw%2Fx1TKVLHLPawx%2B0EYS7a8scerSOrkdD%2BuQymZCDXpgvx7voJVH2HrE15kmVCbihDDu4RNWPtsPsGnmk%2BcxxgEfhRV8ZW%2FUZrFbUhGEAtEHA%2F7b7mMdhxQpBJzDb9UToPjqUYomzqlCk8gGjJIETbfxzQfeYcgGPy3O116eJXp0XYt6cLJJ5ZMbGBsg488rHgjCJv4a9BjqkAWZICMQWO8IUPyf%2FMZqVQ%2F7Eg%2FVzVikkM9ByrsIHT3c6QzriKwGypzmmWIpA6HkGS5l5Q7HRLIPv%2BltYv9GVFSLEOTxEwGHnJGsGtfTXv08WhuzGR2i9nbDLGbo5FwrhS%2BPdU%2FqIuWD9KlXmoKJ%2FBDA8tdAmnfZWXcouGTFPViT2pdpab5l9biHD7U11kPu987MEj4651odhP7tEnWPDyweIaPPK&X-Amz-Signature=4a7a538f85d5eb55105c5f9456e5717dce5c7f0ac613c625d5505df837da0d31&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAAE3OXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC3yAZfvwGm2whOf%2B1S5yywj6%2B5MBJQqlGb4pZ6QnBiNgIhAO%2FD1VxlyM%2BRW%2FLnuTjHDSBhFL5MsioohbtTTiDnoh%2BbKv8DCCYQABoMNjM3NDIzMTgzODA1Igyy%2F8IPP9zan%2Fewc24q3AMYSayajZGL%2BLSLJrHeKH5DDfJPjcRfFBaTc2LgmPrKSHcnl4n9yhO4NSfoEGdjxHSkhAzJzPzkMxpWoruDSTE7Foj0LQ%2FoVY8PN0aubX8PCtc4wNdNGLI7%2B20bd5QM0iQWwtIH%2BJyxrV7EPR3GbNZR1ku5iL14Dlts%2Bood8GforHhzbtvDotJysqONMF82mBbhbi5YlWgp1pS9hms4n7s3faUp3pE03j0stYA69HWcHW8kWCOv9EA2rReeub5FR1Zhpus5EXZ5DPp0Vzgk3PDblCBzfrZiXd8R56hpzPPFqaS3oqOQgj69HIyXPG2Yhrf4R2YrzJ26hTQeZ%2BnwAdpTg2m0NVsPVUU4PwmGftq14d8Stxa18hEzR2l8VM5m4HwGj7ieC5v%2BeVVFLkP9uvEhqJW3lIvfj92fCCz%2BGFVi1ybeOgaEkSCmguSSw%2Fx1TKVLHLPawx%2B0EYS7a8scerSOrkdD%2BuQymZCDXpgvx7voJVH2HrE15kmVCbihDDu4RNWPtsPsGnmk%2BcxxgEfhRV8ZW%2FUZrFbUhGEAtEHA%2F7b7mMdhxQpBJzDb9UToPjqUYomzqlCk8gGjJIETbfxzQfeYcgGPy3O116eJXp0XYt6cLJJ5ZMbGBsg488rHgjCJv4a9BjqkAWZICMQWO8IUPyf%2FMZqVQ%2F7Eg%2FVzVikkM9ByrsIHT3c6QzriKwGypzmmWIpA6HkGS5l5Q7HRLIPv%2BltYv9GVFSLEOTxEwGHnJGsGtfTXv08WhuzGR2i9nbDLGbo5FwrhS%2BPdU%2FqIuWD9KlXmoKJ%2FBDA8tdAmnfZWXcouGTFPViT2pdpab5l9biHD7U11kPu987MEj4651odhP7tEnWPDyweIaPPK&X-Amz-Signature=90b9722c6b35771f34b9f69bdd59defeac958bb108b0d84bc9a9e12a6d90e30c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=0aaa2fb6c0196405e60fafac0268e4bcaeb17b18d046a084157121de46f8c277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=838e33b398d09c8df4b0bf0d128f4f761c3a720e283e51411543dfcac407691d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=63b835d501598528c1cd97028b985f7a91ba8564eb7f839e2ae64fadb6bac95f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=9650e233b706a3673e5763025e35bd282b13864f63e98e866e92bdef068d3af4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=04092410036f3be1f5cb198092ae63328fc8895ee6f4df8d81a40e6932e2d771&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IZDWJF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIH9nBXDSJLpFmNir4mCMepx0%2FFFJI6%2BjfLvlJ0gYQrGGAiBMvgmJbRPkos8KoLrURulWRuIARpPNo9UlGfo7rq5kxir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMyiqBFluL1pQvMa0jKtwDTxkI6R6gco8BHjyrtBrENXFkR3Dku%2BUoz552JrptjavjPGAQ5PWO1UIb8a3%2FCqkzGEfxzAchXWyFrNtiA6hyvoDzgqmQ7PR2LjjIRnybHnfNuE7DZuFKsBm%2FwfV4Op9PCGAb9P9d5ixLhWYewwyvmfwBpoEnRQGhj0XtqReE2ObzmgmYkxDz6CvFqYQM7RS3sq%2BGMtL2K5hubtFiu%2FmnTNA6dLBEErcSJCGCcT10OZR2LbV8oaN1MFOLSfcqHLhFaxNRZzQtsooLZxPBwtm0tw38B9zyS7H5g%2BUacNprxZBpge59G%2Bsydt6ErbnHzC6MDlvmZoqMAbKLJ6AffHscSle5VEL%2BAXplwiuncsZF%2FLH0LwGnhuajAo8fEBKaZYGzpV0757PBeOV2b7bI26kbpRdcfFJhJ939E2GRvLCK2mWsssBDzoiDkfLiFI6ch80HaWNe48CIX5bQiqpxn6LBwIcOgTHDBTTzFTSAwbNnphZKQbrxMWu9x%2BTeVrOtv6XIV6ou2aIK16c9GATpzlD9VAUTy1VCPbh5eDYPUCi5WWm9d0jsRd2zH0I5t8hYtXfx0cy5cIl75p7225QUAd5MFQS3ucQ6BeL7QaEeVNjFhArc4XTdkrenk4OoPtswtL6GvQY6pgF9a8nzggkUU9T3LZBtVfBtaFHwBU2CIBX3IFVlQ7uh8maxEnf9F9XWUvsIckcS%2B%2BLmGk86qxCjQXxTR9zxGuPi3hWPO8vRy%2F7GglhlmySg%2FB%2FUmFaXtSohTQdlRPCNlOCrNy2U30Xy%2BNFXlcG1PH39wjPk3dS0FhMbQoYo4jpfT5GA0mYtE%2BN0dDrq%2BBM7u5XEvZ4rtZsMeh18IFcmNSRbtLQOSTPo&X-Amz-Signature=d5bea9ddcc7a2d40ac20fc442121d8bded1721db60437e49c43ec8f55af79aff&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2PFZIHJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHJ2T9M8SY%2BURmnlRglU%2FC1PukajnHDd4Lc8VcK4I5pQAiEAjZI4js8eO1je0h%2F85Jz0OmQg9jom%2Bnp9MeWpaJI%2FCckq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCluCgH7At2BycQFTyrcA%2FY4Qt4L68beaZ1o7UeB1pKkVfozKjLx1dyDKPEJRYq8DMi2klDsA051A94HOtHOEAm5QNgldfxlhK2VKVt099pivAHCaIMdCQZ%2Fqv0UbpLCGwYgpSNeBZQEX%2FzeSDCDmHKQAKeIs%2BcPCMYGXhrwiRqCaFWRVz%2Bs%2Bo7hpymwE8ivmyw%2FRizEaBXLuFgr8YCJgPsUkINjDhBquwGlInfAN2AiLlCNjg3vfRSfX%2F36qT3K%2BUcEhv4DD7gcEkrTKpWr5mIrJCy%2Fpu%2BuRniIJl%2FuT0pSqKjkUnbsE%2B4f25bllkUcmYoSePErNcadoC55XL8CAircNhzxPc1io6HJHE6U2Io3K19dOQBeZkuAqMtazLSiS9zmpmv2kkrgvLSnx1LrZ1F9PPC0GNqlK2HtKl2%2FBMyMFTDH3xH4ECBFl%2B%2Bi0dESTDGWAbsciTyQfb6%2Biq53PifoQCdpAfR2Gb%2BkJCOMRCHcQBtFmmSYMsNrZhnzpVJhQbmF9dG7IDk0ZfZ5%2FDR56%2BwGjOex7IwDwl5twPz3Z0j6C6SZUMmOA6mltgN0XY5U1kokaitbSDpM6PLfgpcj5VMG%2BPw7ruHXzjYjadOCaCnTEiSP7qo0DfthY2JOoQ%2BoLCp39tpQOrUJoD5TMP6%2Bhr0GOqUBOp1rJydbZNpHeoECfU%2F%2FuS3eE5mRb25Re0D16DxASELWcFh6kJW1GHK9%2FZMl4xZtMIdOh9Anr%2FAYRD0i9yYguQauyNfBYheYpjrwlhKSfLr4Rw%2FGFZ%2FNM%2BwXYd3EG2o9T2Mji1WPOQfkVYBm0SryuAxiOanV9wZ3K6nKWfu%2BS6ec8eGjRi9P9O%2BsHYZe5mR4Dmw73U3m%2FBozlSd%2Bi3JB6LfM7wHl&X-Amz-Signature=d1eef819b6c7d679ae48737ea78e1edab92cecad9ff363997de4b4c68fc2bec9&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2PFZIHJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHJ2T9M8SY%2BURmnlRglU%2FC1PukajnHDd4Lc8VcK4I5pQAiEAjZI4js8eO1je0h%2F85Jz0OmQg9jom%2Bnp9MeWpaJI%2FCckq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCluCgH7At2BycQFTyrcA%2FY4Qt4L68beaZ1o7UeB1pKkVfozKjLx1dyDKPEJRYq8DMi2klDsA051A94HOtHOEAm5QNgldfxlhK2VKVt099pivAHCaIMdCQZ%2Fqv0UbpLCGwYgpSNeBZQEX%2FzeSDCDmHKQAKeIs%2BcPCMYGXhrwiRqCaFWRVz%2Bs%2Bo7hpymwE8ivmyw%2FRizEaBXLuFgr8YCJgPsUkINjDhBquwGlInfAN2AiLlCNjg3vfRSfX%2F36qT3K%2BUcEhv4DD7gcEkrTKpWr5mIrJCy%2Fpu%2BuRniIJl%2FuT0pSqKjkUnbsE%2B4f25bllkUcmYoSePErNcadoC55XL8CAircNhzxPc1io6HJHE6U2Io3K19dOQBeZkuAqMtazLSiS9zmpmv2kkrgvLSnx1LrZ1F9PPC0GNqlK2HtKl2%2FBMyMFTDH3xH4ECBFl%2B%2Bi0dESTDGWAbsciTyQfb6%2Biq53PifoQCdpAfR2Gb%2BkJCOMRCHcQBtFmmSYMsNrZhnzpVJhQbmF9dG7IDk0ZfZ5%2FDR56%2BwGjOex7IwDwl5twPz3Z0j6C6SZUMmOA6mltgN0XY5U1kokaitbSDpM6PLfgpcj5VMG%2BPw7ruHXzjYjadOCaCnTEiSP7qo0DfthY2JOoQ%2BoLCp39tpQOrUJoD5TMP6%2Bhr0GOqUBOp1rJydbZNpHeoECfU%2F%2FuS3eE5mRb25Re0D16DxASELWcFh6kJW1GHK9%2FZMl4xZtMIdOh9Anr%2FAYRD0i9yYguQauyNfBYheYpjrwlhKSfLr4Rw%2FGFZ%2FNM%2BwXYd3EG2o9T2Mji1WPOQfkVYBm0SryuAxiOanV9wZ3K6nKWfu%2BS6ec8eGjRi9P9O%2BsHYZe5mR4Dmw73U3m%2FBozlSd%2Bi3JB6LfM7wHl&X-Amz-Signature=7689c700c9a943fafa6f2be722c8a98826086e8f2b1c1fe5537695a80d0eb368&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTXNO5AN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICNsHHDRVrSqGTcamavoNjs3dB%2F3MbDxNXOEFhDUBxw6AiEAn4Lb169NIjP%2BL%2FqCPviLzbaWPmXVEwGvO06zTCvo9kwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAT5TpDdV2HLdbDztircA96gjDerIomvvhIIf5sNvsyC63veJPtPCWx5OlW4f70oU3d7MdDsa2fNAwd6EIi7SAK1Ds72nZeH2OnGMYDbvslJHiLxl%2FJ9quct5q1PdFHDNCaTWrZ2KZydsMHuoxYIXBWyTKeP7882g0BbRBUuJXAWi1EyIouc0SGtU%2B4%2FxOX4RuQgD%2Bu%2BbCNmNIR6mnkJ1TSc95bqPj%2B2vdq0kSbbfPXK9tMwjOikic3CyYoygbY4DvhZymHMzpP2zza4jQpZBs07%2FcDd4dbNaCZDE1C1dgTzP08tOLuQvCzpn6a2L6pkKhR0J3IYYFmz2Qv8FMkU%2B66CkLXf8JU7MuBj4%2FKwW%2F0djQ%2FWanijwIZPkYZ9o83R%2Br1cXhrQL2ZkUfHsO6bosKIdAzdTfX96HGCirpzczr14fIc2c34QifaLv43hE5HBViTBWuLYZLFy389AK6HuQAKIPeiBsv85E%2BHX4IAfTUJt39U4g4hopD7tYlSaOMd6goZdhjMaAAObGTIlIKDajojJ8wPRh6Yu%2BOoedRtLDdh8N3SrdDcdp4nmTUdILi%2BdvW8LKbbCjteu1WYTf%2FnuS%2FJ80CbiyBVu66umgWqFGblqJ6I2tkVeigJzPrwTOh1exU9K4ZIszZBFr4AQML6%2Bhr0GOqUBJzlruMslXBNFBeyKWniTriG1%2Fobofu5Yhkwu%2F17V7z4W9oZAFg9myvTzAD5TFVTaZvBbNGNbs6B8dnj99AYDal7aDBpz3RaKiFnlXa2JPZ2bLXPakrWF1GB7XkSizwatjqlg4mqO81cCxWSAFPzioo8OZpqkBIgWfsj00g7yT0JX6tJhMsiUCie6cIJLekAV18CkfkNRk%2BHzk6ECvBdEXMDqnaxq&X-Amz-Signature=efc19962f020165c41ed60d52e0820eba9a704825a3342225e303ebb427b949b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMSYCTZT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBtl0TNfaBta9BBK69JOs%2BJjJDRv6MYflsjzUIiE5t6SAiEAg4MRG%2FtPjeYt3Le5dcVzaXYvWzmWYIl66bMNmpD4zqwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNufrwSysIEdm71oPircA63vpnwBGSIW05i3%2F2j0oxHZP4dMUsilEFR83%2FHEm5hGOUaCqxvGGfYzeibNUDs38jLVENkYzrUg%2Bw1QmVoY6wVo8iOqgM6zIXesTky94tGaw8iQ7uxGrm06%2BrPIC2EsUcViWR7w9LA3g5tkn2fi7h8efLAxSuSDKg6UYDU6q5IL1yKfKNOEJtBVKUzqtOtwd2aVFiFHHrWVbRCP%2BBdtCAikKe0RVdaySwDPTUfNl6z7IFdzGJ9y5j8FyGpogf1dsUycd7s18%2BC2DP4J%2B7dBSB2v9q2B9yIO5rTRzEmTHcQ6a7k4efWUGBNRIMkCLu6ZOHI%2FMf2YDdfOaa6euHKD7TGRT0DdiRbkxcZC4tMwkuaF1P5jHkbwSFhb3LiuJkqlcbokMq4fQEHHTMbe6reFoCO73er%2Bkv%2Fr2ch2veO4C7%2FWJ5NkhodxfSzZ%2B40l59fKdSKUgBV82h9jqUnJD6GP8uR%2B9GzLSv6M5jNCMgd%2Bmsf03GkSJ4ojDjYGBxQ9WcgtXBt5G4ZcDzcrpP%2BSVH3nMkbdnqiYpmucOGREanbBQWPhUk%2BI9ou8h2vvvr0ymIbnBOjdx5BoaehLVsJHmhFOKQer8KGjlwHRj1vU7y%2B9iFS5rIifnvF3iZaMgZ4CMOO%2Bhr0GOqUBQUod74gUxlDqCt%2FCQv2kB6IHq1iy5Y3LTB9Gv1C6kMTLPF8FAkUVg5%2Bi%2BFKynReGDNZ4RDCuh%2BfIkehHqhHmzLEmVl1yMaRMy2wrB7IqgWnHAa%2Btr%2FAl8QZeeUMSVVndIsKjGm%2BvP%2BILg1M3HL92HpxvY%2FpRH9KJ8pnyJL0Rb1se91ANPIZu3ZlIcfDoXHYlK8Qw%2Brwr2t8ZGdrziEyUiUlOqnx%2F&X-Amz-Signature=6490dc2d496ff6ad03522a656c4f50aff8fa77eaed6ee588a04ca7fb2fc2882a&X-Amz-SignedHeaders=host&x-id=GetObject)
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