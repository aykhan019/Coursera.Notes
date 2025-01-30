

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=d8142b29b493c974b369a065c4738815be8f5444a3e8dd666a0bde320889a769&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=f75b15097b390f555ed1b85ffe5256d648471507e0f2e32198a8d40dd7b28298&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=dabb6f93bb331871f0d7de0c68f47312a184cb03eca42b6c63b2311ffa300a2c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=7f5ee1e7937c6a3d5405c24efdd22b3e5047a2ecc6b452556189ad1d5fc8ac4a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=2a3dc588606ab4ddbd66902bb85b9f48cae05645b3464afde32ff031e588af57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=d49c2aba15bb02d93e9d76cad64515b552d147e4a272b75d55cff7fba7ef2b74&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=b5c90ae5e3cf064f495f2033c8924c8285e9e6b23b5be04fb6d29254fd7b9239&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=db159882b809ac439dac06e26e0126843bd6feec35433a8ea51fefb601652290&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=f26e6ad0d9c3e80e2a6dde7f130ce3bf88ca86df36893596384efabe09bdd7f3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNDVGH5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBq33pJY%2Bv9ThUnxsBkxp8xwIsnByRbaDqunPe%2FyK6vwIhAI4%2FY0KuqhArYGjPBa4Y6RObUVaWpt0ek5rjHNn0AM7oKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyifSrxQESmT13j%2BO0q3AOda0RhmJm6ChY4P6DyimWMmPQKXRpR0%2BVYDfKXl7n4lxW8zxt1nmW6nnOEf7SK3QOiFzKJF0qMiGoDm6FZnZGTIf4iBBSsg1pNaJeVS6X5sY9%2FO54mydUY9EY0sBpIkSmakI8wqCtY2O62JUMm1qcqUAf14AO1jE6ILo1ZgBfVgXS0CvaCmhuOzgX3TtLzoKR%2FPguBPt9DW1O7pN5cpx9gzKz5qdYW5pxxH5w9KOACSzm1H6OBpm0pxUvSSe9BLWz%2B23w9vFc2prnCDfuoWxRuhiXT%2BkV9j2pyNjB1g9JtedFhxJXZyBoyhde1qxu1bGs%2B6%2FkBPkL865d3E5F89UnI1a7W4twPGgZ3mNmyCK%2Bk59rOzHmtNSySzU2SsBBYVDYkz2%2Bnt5clzAFKR%2FytJvtMs5bIQuD0W8%2Bg%2FIOPg%2BiubQ7ZWWtQwpOHzO2CtW0LbdD414aX%2FF9S0x2cCDM30Jv05TX7R8HeRgSauOLTK%2BBuKWbSmPnYHx03cWSNXhs4AErDf2%2BKNDTmSfDcCFaL%2FbeY3Qiwlaqx9nebxcJfKBh2gj%2BpUIpzUmE3Kwis6%2BKFx8L9tSbxbyd0ZjYbGryCvP4vqxlQR1TuTzaEeNu9PK%2BWraVDETMxLVGWyE7OLzC%2Bhuy8BjqkATKTrpfHQ%2FEX9mKByo6cSO%2BSG0lXQWJI73tdbtLkGLMEP%2FGTvXeL7N5peIGnNDFl76U9wAXpKpwxqp%2BVJlBaURbypkbGE3zzMaPr%2B6d1u7Rgi6v%2B9kAkQa1vJiGaO%2FpT45n%2F4kw%2FyV0cLFmFqTqGX%2FSeFtii4I5sR6hpqZwuCERLIoWtvFtLNfhj9UDSSnDYGYerhV2p5%2B7jKOcwope76tmY9yTN&X-Amz-Signature=b2bc4a80351af592cd126662955d04c6dd676ce866202c870e8efd8d6f6050d9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNDVGH5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBq33pJY%2Bv9ThUnxsBkxp8xwIsnByRbaDqunPe%2FyK6vwIhAI4%2FY0KuqhArYGjPBa4Y6RObUVaWpt0ek5rjHNn0AM7oKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyifSrxQESmT13j%2BO0q3AOda0RhmJm6ChY4P6DyimWMmPQKXRpR0%2BVYDfKXl7n4lxW8zxt1nmW6nnOEf7SK3QOiFzKJF0qMiGoDm6FZnZGTIf4iBBSsg1pNaJeVS6X5sY9%2FO54mydUY9EY0sBpIkSmakI8wqCtY2O62JUMm1qcqUAf14AO1jE6ILo1ZgBfVgXS0CvaCmhuOzgX3TtLzoKR%2FPguBPt9DW1O7pN5cpx9gzKz5qdYW5pxxH5w9KOACSzm1H6OBpm0pxUvSSe9BLWz%2B23w9vFc2prnCDfuoWxRuhiXT%2BkV9j2pyNjB1g9JtedFhxJXZyBoyhde1qxu1bGs%2B6%2FkBPkL865d3E5F89UnI1a7W4twPGgZ3mNmyCK%2Bk59rOzHmtNSySzU2SsBBYVDYkz2%2Bnt5clzAFKR%2FytJvtMs5bIQuD0W8%2Bg%2FIOPg%2BiubQ7ZWWtQwpOHzO2CtW0LbdD414aX%2FF9S0x2cCDM30Jv05TX7R8HeRgSauOLTK%2BBuKWbSmPnYHx03cWSNXhs4AErDf2%2BKNDTmSfDcCFaL%2FbeY3Qiwlaqx9nebxcJfKBh2gj%2BpUIpzUmE3Kwis6%2BKFx8L9tSbxbyd0ZjYbGryCvP4vqxlQR1TuTzaEeNu9PK%2BWraVDETMxLVGWyE7OLzC%2Bhuy8BjqkATKTrpfHQ%2FEX9mKByo6cSO%2BSG0lXQWJI73tdbtLkGLMEP%2FGTvXeL7N5peIGnNDFl76U9wAXpKpwxqp%2BVJlBaURbypkbGE3zzMaPr%2B6d1u7Rgi6v%2B9kAkQa1vJiGaO%2FpT45n%2F4kw%2FyV0cLFmFqTqGX%2FSeFtii4I5sR6hpqZwuCERLIoWtvFtLNfhj9UDSSnDYGYerhV2p5%2B7jKOcwope76tmY9yTN&X-Amz-Signature=0397ccb6807cafa340b8207324d713b762704121d06adedf7d820aab8593e9db&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNDVGH5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBq33pJY%2Bv9ThUnxsBkxp8xwIsnByRbaDqunPe%2FyK6vwIhAI4%2FY0KuqhArYGjPBa4Y6RObUVaWpt0ek5rjHNn0AM7oKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyifSrxQESmT13j%2BO0q3AOda0RhmJm6ChY4P6DyimWMmPQKXRpR0%2BVYDfKXl7n4lxW8zxt1nmW6nnOEf7SK3QOiFzKJF0qMiGoDm6FZnZGTIf4iBBSsg1pNaJeVS6X5sY9%2FO54mydUY9EY0sBpIkSmakI8wqCtY2O62JUMm1qcqUAf14AO1jE6ILo1ZgBfVgXS0CvaCmhuOzgX3TtLzoKR%2FPguBPt9DW1O7pN5cpx9gzKz5qdYW5pxxH5w9KOACSzm1H6OBpm0pxUvSSe9BLWz%2B23w9vFc2prnCDfuoWxRuhiXT%2BkV9j2pyNjB1g9JtedFhxJXZyBoyhde1qxu1bGs%2B6%2FkBPkL865d3E5F89UnI1a7W4twPGgZ3mNmyCK%2Bk59rOzHmtNSySzU2SsBBYVDYkz2%2Bnt5clzAFKR%2FytJvtMs5bIQuD0W8%2Bg%2FIOPg%2BiubQ7ZWWtQwpOHzO2CtW0LbdD414aX%2FF9S0x2cCDM30Jv05TX7R8HeRgSauOLTK%2BBuKWbSmPnYHx03cWSNXhs4AErDf2%2BKNDTmSfDcCFaL%2FbeY3Qiwlaqx9nebxcJfKBh2gj%2BpUIpzUmE3Kwis6%2BKFx8L9tSbxbyd0ZjYbGryCvP4vqxlQR1TuTzaEeNu9PK%2BWraVDETMxLVGWyE7OLzC%2Bhuy8BjqkATKTrpfHQ%2FEX9mKByo6cSO%2BSG0lXQWJI73tdbtLkGLMEP%2FGTvXeL7N5peIGnNDFl76U9wAXpKpwxqp%2BVJlBaURbypkbGE3zzMaPr%2B6d1u7Rgi6v%2B9kAkQa1vJiGaO%2FpT45n%2F4kw%2FyV0cLFmFqTqGX%2FSeFtii4I5sR6hpqZwuCERLIoWtvFtLNfhj9UDSSnDYGYerhV2p5%2B7jKOcwope76tmY9yTN&X-Amz-Signature=90ca703def47b2c530cd10f88ee0ce9a42b09bf1d14c551e07abc1d23f5d81c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=6a0118da2d459ef8676fd83f16c4daca30ab328e865aeb841fb64ce9c132e9d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=63dba8c77b245937037e00c5ecc2089353b3ae8dd6860c09baf7811bb1f5f192&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=96456e393a31ad1d24fc5e3207240dcb23171ae9ec969a467cfbbc077b571cd8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=63aeafeaf091494991b19fcf1890a395c7dac9308a86017619a779fabe1dbc96&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=0ce7edc2269d4db26feee20062f9c7532221c2efcee334ac608d9f3a881a0498&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NFYYICE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF2j3okwo3T63JVoyAnec5di1xPgZ%2BAEJkRKW75tcvBCAiEA7LGjM70d%2B7U9Hl9D8Vcgn%2FSiYtUxxkA6f%2FKD%2FlYUE8IqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVaVOtUvBjvIayLvyrcA%2BfV9sdT5s%2Fg8y3FPxoTrv%2FZ7AmUWaF2rLRN3nm%2Fq%2BGz8VkQu6DWzKqQi%2BmyEQGhwTyalDkYPs2k%2F3IaESBO1ZWG93RWJiSut6G0%2FLSBgZ7Fw6EMTIbSQmtmKxrB%2BfN3VRNgBSziQRjHeBGqY2lxuWie4RHf4t%2Fn6LuSN9S60Th8e%2FVaGdeovfl6HIfcqApM29ygh2%2F%2Fx5z5FwB7ldTcyGCHuQATWzYQSAMJ7LJp5PN7YNYMZdUHjXsKe1suXiFwZ0TcW%2BOcnG9eRs4SYYF3LWPxN99nZnws2ze0sytKY8IPG50Vx5YlozIz5pUlSYGFF4yQNB2MsYOy%2BcGmerNG2bGRuXDW8LOuHSHT114H9siOUn9Sb7l4eoFcV1%2ByIlxyMs4s1kqqHL3xlL0pX%2BXl5FtgA0plOixgQPtzDZUJrEMgg1sX5177SwiTfChMnDV%2FFfONfe7fxCzXVxlBL1O8gCG1ZsQ169qZOD7tE6fQYCxJu7LxD4xc8HsA1ph0mI6PYXf2W1etjsle8bTWk2GieDsgArdyttewtWMrrqlSWheNupMz18xCvFNdZhE9owgxpx3oUHP2IiKe4SnJKJyihfcf3767QeqtvoVbioAK4%2FVi0iNQSlDCuHnJAU4lMN2G7LwGOqUBz%2Bx5zRIOfbkTvqBa3JjGZjcpDpczs85juv%2FzcFA3ZZb5WgVF4yS9lcM0gObeMbIsLyIh9SBPk9EHAhxRu4e%2FFi890DA0pHWU4FysASrSNNEoowR2OQ5g8X5zpgwWNK0MkutDHpWLqbT2xo%2BPQ85gnq0fan4fjI%2Bcrk5HomgSx3jh1CN3mh1kU5bQ6tnfyZO2uko614v00gpdbybbXza%2BabyUnZv%2B&X-Amz-Signature=bd525cc0c0b6bed21d3294c9fb0bf7f29ea436ab1cc230376a5c89b131c67f68&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWAWOYBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FXfKzAccyrhe6SpAmvrV9tWEAv4k%2BzRtvZ5kA11xxqgIhAOma0SLev7Gm2GjOmh4Ko4Yc165c8OBCYbk98jWJyCwPKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyePsvT0TJAICWjqtwq3AM0%2FjcS2S%2Fl2myhJIb48Gj%2BREnIPZfqrLnlOyz%2BXIrRsFWSyeKcEghEvlpR%2B7rE0CulJV%2BtIB3a%2BCSVhHn54r4%2Fvziw1ANKodVxnTI5xCkdG%2F1bjskGHVOZV9SdThvy67H5KHssQfjAEf6xUJB%2Bd%2FowOVjHOmBd8h%2FwyHuSNm3luAWbhyCC3vjAN2OuVV8B4GoMpjDsnEVV5xN877XHF8ISU0OP1XLTPp2ZwVrA1C%2FI%2BokT4v%2FMSmw9kUD8Zisk94Y1f560Ol5qnMRsYllHVFIqit3T0KXKWZ6DSk%2F13X9qPBx2EhVkWbQaOE1TIozyNAU%2F2%2B%2BME3dXilETWGB%2B6TMvH5rCjYGChlHeuWi1jhITlSdnLdr%2Fk9nKn6ipryBDrhOS1g3HWDAWmyslR%2BshmOCjfLRxAJ9EvTfMMo3MAMpnrifJeC9urtNLdfCQ7%2FZsObd1f6sHkvwWxL7%2F5POjvsSNiyX3DA%2BUBq8UG3qlEKJP0CzIZWhb8boUS3R%2Bcfle5dg4apY7VFyrBe7BnbUb8na1rdjIkqqYimArI4nyFeIQJl3%2BfSiR3eAOtQ4PypeZ4Jx7GxrVIXglEViVL1be3lDVmtmGaG1ue8f2nu8XSyxr%2FNz2z2F9tjG%2FAFguTDC3huy8BjqkAZZ2tDUTTqv%2BLUzsdUaLC%2FLbTMiP9RXu7Jk89EnooXCBmFgHiTcnUVkf23wWw3QdKMcYVpZWr22SvtwI%2FIEWDK1%2FfhKr6We8Oo%2FT0vkCxewMn%2FrcFbVeXTSuP8MwiGSwHEm5Ubdt89aSTKxH%2FkGL%2B83oOsGMYCO%2F1qryi3IQOPgbzkluH2BXHIZiZIxVbQZTJ3YPcnh8fmdLX%2Fnkeg3NlCIbB2pr&X-Amz-Signature=db77b7f9a839beb41ceb87fbb83c4cb5c29e0f1fb898eb3af5b09e6e40dfa0be&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWAWOYBH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FXfKzAccyrhe6SpAmvrV9tWEAv4k%2BzRtvZ5kA11xxqgIhAOma0SLev7Gm2GjOmh4Ko4Yc165c8OBCYbk98jWJyCwPKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyePsvT0TJAICWjqtwq3AM0%2FjcS2S%2Fl2myhJIb48Gj%2BREnIPZfqrLnlOyz%2BXIrRsFWSyeKcEghEvlpR%2B7rE0CulJV%2BtIB3a%2BCSVhHn54r4%2Fvziw1ANKodVxnTI5xCkdG%2F1bjskGHVOZV9SdThvy67H5KHssQfjAEf6xUJB%2Bd%2FowOVjHOmBd8h%2FwyHuSNm3luAWbhyCC3vjAN2OuVV8B4GoMpjDsnEVV5xN877XHF8ISU0OP1XLTPp2ZwVrA1C%2FI%2BokT4v%2FMSmw9kUD8Zisk94Y1f560Ol5qnMRsYllHVFIqit3T0KXKWZ6DSk%2F13X9qPBx2EhVkWbQaOE1TIozyNAU%2F2%2B%2BME3dXilETWGB%2B6TMvH5rCjYGChlHeuWi1jhITlSdnLdr%2Fk9nKn6ipryBDrhOS1g3HWDAWmyslR%2BshmOCjfLRxAJ9EvTfMMo3MAMpnrifJeC9urtNLdfCQ7%2FZsObd1f6sHkvwWxL7%2F5POjvsSNiyX3DA%2BUBq8UG3qlEKJP0CzIZWhb8boUS3R%2Bcfle5dg4apY7VFyrBe7BnbUb8na1rdjIkqqYimArI4nyFeIQJl3%2BfSiR3eAOtQ4PypeZ4Jx7GxrVIXglEViVL1be3lDVmtmGaG1ue8f2nu8XSyxr%2FNz2z2F9tjG%2FAFguTDC3huy8BjqkAZZ2tDUTTqv%2BLUzsdUaLC%2FLbTMiP9RXu7Jk89EnooXCBmFgHiTcnUVkf23wWw3QdKMcYVpZWr22SvtwI%2FIEWDK1%2FfhKr6We8Oo%2FT0vkCxewMn%2FrcFbVeXTSuP8MwiGSwHEm5Ubdt89aSTKxH%2FkGL%2B83oOsGMYCO%2F1qryi3IQOPgbzkluH2BXHIZiZIxVbQZTJ3YPcnh8fmdLX%2Fnkeg3NlCIbB2pr&X-Amz-Signature=d82f3d9e6d304243f53708304e1ee11dedc1a113c59cba809979c6995b3e09ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3OHJXRD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW5OEaUUUytDEau%2BUyAbwJxAWDGAXm%2BfzvDavZgCgV5AIhAOgTH7%2BmF98GtnBvdLC2uuT7ymTxuvFjn3PdxAn7ANucKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bt2x%2B9kRA4ufr0AMq3ANoMbZTQsBKm40nHRPJyHuNq3mqOFSiScmwQeI6%2BAUH5QpevgjcX%2FfTKXmkPETbs3P95UF71DPOZHB8n1x4%2B4gL47%2FfK9ockmGRMQ4%2FBZ%2B%2B%2Fw0Hz7VcP5ib0ghCZ12EF0Sga%2FbRe6e%2FCgpPlpL%2ByAtzD8Ij6EEzvBXy4aEGXCZKrKkSM59rpGH%2BhfLWu1%2FSswE8OonHcJVKBr4k1e14S%2BLN3rG4ZiM2MZl4Wxep22MAPdwFxw%2F0mvgTgpu4wPTAvdQVXUKDXCGXaIhkrxSjVJHm17FJYC9Ywj1IGD3g0AMi39wwhnWHZA9bezXXTOGt1n3sal1cbahb0ZEgvr%2FiF0CsFzKTM4lzWv06ryaVBVZalT2JV%2BFW%2BcbxU2mbhX5%2BvjWZBzQrmp8E3nV0KtMtik3O8mCW2dS74P8izBq9sUlPq1gRD6kg0HJOPXnyT6IynpzoaFfxcWRjeU8WRtnIVq1qy2EwiSBkIL9BfWPgeUv2CEg2O%2FILAOWKsaKigoMpL8a1b1FKEPl9GWjQiHfL4Pa%2BaIBEsiW%2F5UmZmzLupqtV8a5QujIOBCKpsZpOQ1CnBtWiMR4cPj2Yoc%2Bd%2FvWLoCSvAv09AhIBf8uRVWoP7qfMadkQVGD5uyrpSvddNjDehuy8BjqkAcTm8OtiTHuxyx9ig5viqdlnR7ymhqE2dYHaI44%2BD2Sh18S%2BEh8WFM6DgP5oyhMiIYedfnOGzehUAQMeaq0TBVZFzNv%2BN43DSP0OeN0L%2BJyPHAw7vGZD0yaqZSHgmXbyAjMxjZUZ%2FeoymCIToyGhFkHTTMuNDbbVEEE55dJyEEtU94jFJmCMeBcsEJ2Zz4bn0ZUt4V05j5ELjlrgD1tno7kKA9bm&X-Amz-Signature=a4913dae275e2311069c3d473ccedc672d2de7b8b99e7a66467eec97710647ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T4GYEC7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAn%2BqzvbXyeRD7xzPC3m7I1rRNmPifDxG4klbq7btstWAiEA%2B0tGCDz%2FSePfWo2kA%2FJ1eu63K7jwmkvAg9K5VNvpds0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FARAw%2BzjII%2FLI9WyrcA6SNsAnhkb%2FGOluQI9nfXqQfpWP7PY4JxsauKmvRK1sALVDpMddKuqPnYxs05r9VudFz%2BVLwIve%2BB2xwgC5GrkIXrLN8t%2FBoQgL1P8SKP5MB3CA1s5dTWbl%2FGfsRA25kM9q%2FWAYKvPf29z9MMizg7lhfPgKSdTn357JPE0tFAA6Ylu%2BT6pUjqm6%2BtunIblZtJV92CPFUeq04aL5R5CyVXun%2BPX9mkRJTG0OYDi9dyOX3rFJbx9ZVlhDdgmiqj%2BX2COSN7IC9%2FcO08TcHv2RD38sVw9XEaNPywAVudG7tYufUY%2F0nbpFBheFmmmbAI0Y0R4DCWAhGQO7qBL5oLWgS2dpYFaAiNK2H%2BhRVldTdz9ypl6HTLKlt7LZkddfJ2ElHa1nr8c2vJxAVdBzmuwO5PuZ0kf%2FwXCmeddoH0J2bm37D2BTYlIyXsDbHvekN6JtwO%2FtmjPrsn5DWIA3rWHjFdgLZ8893hJuazukR7wf7x2FpJ8VrwStj2Twf8aIbSX%2FmPPT2CmTwvlJcSEnKmr7CEcFA8siZ2TcD3AYEISRgUhi%2BwaaW19v78P8eP1I7a4oiWJOY%2FjcftRQ%2FAcUdDvmbOmoDVYkXjP%2BPVCqhUEPM40OKW90GCRarjTcywA22ML%2BG7LwGOqUBAudTn8jkn%2Fs%2F%2FjODQIjgL0K4VQA7xiDxYgntyCNaoSmgkTW%2FG11XR%2FYloQkKlNBkGtunnK1lDDzt9zMZk2%2FwjeReBjQNg361eE%2B2IQCeaKgBEIZqhhBtlY%2FIIWpv4AG9%2F%2FDnIWZ2bGVFUVBNXBOGNDV6e4EeizBWPxp9HVyIsGcrg1zaV4RQVsSQxMIeop12adZ%2FyOqiMApxf%2BeEtAmg2KD55kNB&X-Amz-Signature=8f73b45820bf68e50a09aa1f793981a72643563d1eec8eb5b6df87f86e9db53c&X-Amz-SignedHeaders=host&x-id=GetObject)
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